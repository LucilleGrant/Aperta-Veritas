"""Minimal executable prototype of the Aperta Veritas inquiry ledger."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable
from uuid import uuid4


STATUSES = {"untested", "tested", "contradicted", "scope-restricted", "superseded", "unresolved", "reactivated"}


def _id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class Evaluator:
    evaluator_id: str
    declared_account: str
    criteria: tuple[str, ...]
    measurements: tuple[str, ...] = ()
    values: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()


@dataclass(frozen=True)
class InquiryState:
    state_id: str
    object: str
    representation: str
    status: str = "untested"
    observations: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    distinctions: tuple[str, ...] = ()
    boundaries: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()
    parent_state_ids: tuple[str, ...] = ()
    active: bool = True

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(f"unsupported relational status: {self.status}")
        if not self.object.strip() or not self.representation.strip():
            raise ValueError("object and representation must be explicit")


@dataclass(frozen=True)
class Transition:
    transition_id: str
    prior_state_ids: tuple[str, ...]
    resulting_state_ids: tuple[str, ...]
    operation: str
    transformation: str
    evaluator: Evaluator
    tests: tuple[str, ...] = ()
    inactive_state_ids: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()
    resource_cost: dict[str, float] = field(default_factory=dict)
    reopening_conditions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.prior_state_ids or not self.resulting_state_ids:
            raise ValueError("a transition must connect prior and resulting states")
        if not self.evaluator.criteria:
            raise ValueError("selection criteria must be attributed to an evaluator")


class InquiryLedger:
    """Append-only graph of inquiry states and transitions."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []
        self.states: dict[str, InquiryState] = {}
        self.transitions: dict[str, Transition] = {}

    @property
    def records(self) -> tuple[dict[str, Any], ...]:
        return tuple(self._records)

    def _append(self, kind: str, payload: dict[str, Any]) -> None:
        prior_hash = self._records[-1]["record_hash"] if self._records else None
        body = {"sequence": len(self._records), "kind": kind, "prior_hash": prior_hash, "payload": payload}
        self._records.append({**body, "record_hash": sha256(_canonical(body).encode()).hexdigest()})

    def encounter(self, *, object: str, representation: str, observations: Iterable[str] = (),
                  provenance: Iterable[str] = (), distinctions: Iterable[str] = (),
                  boundaries: Iterable[str] = (), residuals: Iterable[str] = ()) -> InquiryState:
        state = InquiryState(_id("state"), object, representation, observations=tuple(observations),
                             provenance=tuple(provenance), distinctions=tuple(distinctions),
                             boundaries=tuple(boundaries), residuals=tuple(residuals))
        self.states[state.state_id] = state
        self._append("state", asdict(state))
        return state

    def transition(self, *, prior_state_ids: Iterable[str], candidates: Iterable[dict[str, Any]],
                   operation: str, transformation: str, evaluator: Evaluator,
                   selected_indexes: Iterable[int], tests: Iterable[str] = (),
                   residuals: Iterable[str] = (), resource_cost: dict[str, float] | None = None,
                   reopening_conditions: Iterable[str] = ()) -> Transition:
        parents = tuple(prior_state_ids)
        for parent in parents:
            if parent not in self.states:
                raise KeyError(f"unknown prior state: {parent}")
        candidate_data = list(candidates)
        selected = set(selected_indexes)
        if not candidate_data or not selected or not selected.issubset(range(len(candidate_data))):
            raise ValueError("candidates and valid selected indexes are required")
        created, inactive = [], []
        for index, candidate in enumerate(candidate_data):
            state = InquiryState(
                _id("state"), candidate["object"], candidate["representation"],
                candidate.get("status", "untested"), tuple(candidate.get("observations", ())),
                tuple(candidate.get("provenance", ())), tuple(candidate.get("distinctions", ())),
                tuple(candidate.get("boundaries", ())), tuple(candidate.get("residuals", ())),
                parents, index in selected,
            )
            self.states[state.state_id] = state
            created.append(state)
            if not state.active:
                inactive.append(state.state_id)
        edge = Transition(_id("transition"), parents, tuple(s.state_id for s in created), operation,
                          transformation, evaluator, tuple(tests), tuple(inactive), tuple(residuals),
                          resource_cost or {}, tuple(reopening_conditions))
        self.transitions[edge.transition_id] = edge
        self._append("transition", {**asdict(edge), "produced_states": [asdict(s) for s in created]})
        return edge

    def recursive_audit(self, *, target_transition_id: str, auditor: Evaluator,
                        exposed_relations: Iterable[str], unrepresented_relations: Iterable[str],
                        stopping_boundary: str) -> dict[str, Any]:
        if target_transition_id not in self.transitions:
            raise KeyError(f"unknown transition: {target_transition_id}")
        payload = {"audit_id": _id("audit"), "target_transition_id": target_transition_id,
                   "auditor": asdict(auditor), "exposed_relations": tuple(exposed_relations),
                   "unrepresented_relations": tuple(unrepresented_relations),
                   "stopping_boundary": stopping_boundary}
        self._append("recursive_audit", payload)
        return payload

    def verify(self) -> bool:
        prior_hash = None
        for sequence, record in enumerate(self._records):
            body = {"sequence": sequence, "kind": record["kind"], "prior_hash": prior_hash,
                    "payload": record["payload"]}
            if record["sequence"] != sequence or record["record_hash"] != sha256(_canonical(body).encode()).hexdigest():
                return False
            prior_hash = record["record_hash"]
        return True

    def export_jsonl(self, path: str | Path) -> None:
        Path(path).write_text("".join(_canonical(r) + "\n" for r in self._records), encoding="utf-8")


def evaluator(declared_account: str, *, criteria: Iterable[str], measurements: Iterable[str] = (),
              values: Iterable[str] = (), conditions: Iterable[str] = (),
              exclusions: Iterable[str] = ()) -> Evaluator:
    return Evaluator(_id("evaluator"), declared_account, tuple(criteria), tuple(measurements),
                     tuple(values), tuple(conditions), tuple(exclusions))
