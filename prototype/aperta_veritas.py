"""Minimal executable prototype of the Aperta Veritas inquiry ledger."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Iterable
from uuid import uuid4


STATUSES = {
    "untested",
    "tested",
    "contradicted",
    "scope-restricted",
    "superseded",
    "unresolved",
    "incomparable",
    "inactive",
    "reactivated",
}

SUPPORT_RELATIONS = {
    "supports",
    "contradicts",
    "neutral",
    "incomparable",
    "unresolved",
}


def _id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def _canonical(value: Any) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


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
class Belief:
    belief_id: str
    proposition: str
    holder: str
    basis: tuple[str, ...] = ()
    confidence: float | None = None
    revision_conditions: tuple[str, ...] = ()
    insulated_from: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.proposition.strip():
            raise ValueError("belief proposition must be explicit")
        if not self.holder.strip():
            raise ValueError("belief holder must be explicit")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class SupportRelation:
    support_id: str
    conclusion_state_id: str
    relation: str
    measurements: tuple[str, ...]
    conditions: tuple[str, ...] = ()
    observations: tuple[str, ...] = ()
    contradictions: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()
    score: float | None = None

    def __post_init__(self) -> None:
        if self.relation not in SUPPORT_RELATIONS:
            raise ValueError(f"unsupported support relation: {self.relation}")
        if not self.measurements:
            raise ValueError("support requires explicit measurements")


@dataclass(frozen=True)
class Comparison:
    comparison_id: str
    conclusion_state_ids: tuple[str, ...]
    support_ids: tuple[str, ...]
    measurements: tuple[str, ...]
    conditions: tuple[str, ...] = ()
    best_supported_state_ids: tuple[str, ...] = ()
    incomparable_state_ids: tuple[str, ...] = ()
    known_exclusions: tuple[str, ...] = ()
    unrepresented_alternatives_possible: bool = True

    def __post_init__(self) -> None:
        if len(self.conclusion_state_ids) < 2:
            raise ValueError("comparison requires at least two conclusions")
        if not self.measurements:
            raise ValueError("comparison requires explicit measurements")
        if not set(self.best_supported_state_ids).issubset(
            self.conclusion_state_ids
        ):
            raise ValueError(
                "best-supported conclusions must belong to the comparison set"
            )
        if not set(self.incomparable_state_ids).issubset(
            self.conclusion_state_ids
        ):
            raise ValueError(
                "incomparable conclusions must belong to the comparison set"
            )


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
    beliefs: tuple[str, ...] = ()
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
    stopping_conditions: tuple[str, ...] = ()
    reopening_conditions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.prior_state_ids or not self.resulting_state_ids:
            raise ValueError(
                "a transition must connect prior and resulting states"
            )
        if not self.evaluator.criteria:
            raise ValueError(
                "selection criteria must be attributed to an evaluator"
            )


class InquiryLedger:
    """Append-only graph of inquiry states and transitions."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []
        self.states: dict[str, InquiryState] = {}
        self.transitions: dict[str, Transition] = {}
        self.beliefs: dict[str, Belief] = {}
        self.support_relations: dict[str, SupportRelation] = {}
        self.comparisons: dict[str, Comparison] = {}

    @property
    def records(self) -> tuple[dict[str, Any], ...]:
        return tuple(self._records)

    def _append(self, kind: str, payload: dict[str, Any]) -> None:
        prior_hash = (
            self._records[-1]["record_hash"] if self._records else None
        )
        body = {
            "sequence": len(self._records),
            "kind": kind,
            "prior_hash": prior_hash,
            "payload": payload,
        }
        record_hash = sha256(_canonical(body).encode()).hexdigest()
        self._records.append({**body, "record_hash": record_hash})

    def encounter(
        self,
        *,
        object: str,
        representation: str,
        observations: Iterable[str] = (),
        provenance: Iterable[str] = (),
        distinctions: Iterable[str] = (),
        boundaries: Iterable[str] = (),
        residuals: Iterable[str] = (),
        beliefs: Iterable[str] = (),
    ) -> InquiryState:
        belief_ids = tuple(beliefs)
        for belief_id in belief_ids:
            if belief_id not in self.beliefs:
                raise KeyError(f"unknown belief: {belief_id}")

        state = InquiryState(
            state_id=_id("state"),
            object=object,
            representation=representation,
            observations=tuple(observations),
            provenance=tuple(provenance),
            distinctions=tuple(distinctions),
            boundaries=tuple(boundaries),
            residuals=tuple(residuals),
            beliefs=belief_ids,
        )
        self.states[state.state_id] = state
        self._append("state", asdict(state))
        return state

    def record_belief(
        self,
        *,
        proposition: str,
        holder: str,
        basis: Iterable[str] = (),
        confidence: float | None = None,
        revision_conditions: Iterable[str] = (),
        insulated_from: Iterable[str] = (),
    ) -> Belief:
        belief = Belief(
            belief_id=_id("belief"),
            proposition=proposition,
            holder=holder,
            basis=tuple(basis),
            confidence=confidence,
            revision_conditions=tuple(revision_conditions),
            insulated_from=tuple(insulated_from),
        )
        self.beliefs[belief.belief_id] = belief
        self._append("belief", asdict(belief))
        return belief

    def transition(
        self,
        *,
        prior_state_ids: Iterable[str],
        candidates: Iterable[dict[str, Any]],
        operation: str,
        transformation: str,
        evaluator: Evaluator,
        selected_indexes: Iterable[int],
        tests: Iterable[str] = (),
        residuals: Iterable[str] = (),
        resource_cost: dict[str, float] | None = None,
        stopping_conditions: Iterable[str] = (),
        reopening_conditions: Iterable[str] = (),
    ) -> Transition:
        parents = tuple(prior_state_ids)
        for parent in parents:
            if parent not in self.states:
                raise KeyError(f"unknown prior state: {parent}")

        candidate_data = list(candidates)
        selected = set(selected_indexes)

        if not candidate_data:
            raise ValueError("at least one candidate is required")

        if not selected:
            raise ValueError("at least one selected index is required")

        if not selected.issubset(range(len(candidate_data))):
            raise ValueError("selected indexes must identify candidates")

        created: list[InquiryState] = []
        inactive: list[str] = []

        for index, candidate in enumerate(candidate_data):
            belief_ids = tuple(candidate.get("beliefs", ()))
            for belief_id in belief_ids:
                if belief_id not in self.beliefs:
                    raise KeyError(f"unknown belief: {belief_id}")

            is_active = index in selected
            candidate_status = candidate.get("status", "untested")

            if not is_active and candidate_status == "untested":
                candidate_status = "inactive"

            state = InquiryState(
                state_id=_id("state"),
                object=candidate["object"],
                representation=candidate["representation"],
                status=candidate_status,
                observations=tuple(candidate.get("observations", ())),
                provenance=tuple(candidate.get("provenance", ())),
                distinctions=tuple(candidate.get("distinctions", ())),
                boundaries=tuple(candidate.get("boundaries", ())),
                residuals=tuple(candidate.get("residuals", ())),
                beliefs=belief_ids,
                parent_state_ids=parents,
                active=is_active,
            )

            self.states[state.state_id] = state
            created.append(state)

            if not state.active:
                inactive.append(state.state_id)

        edge = Transition(
            transition_id=_id("transition"),
            prior_state_ids=parents,
            resulting_state_ids=tuple(
                state.state_id for state in created
            ),
            operation=operation,
            transformation=transformation,
            evaluator=evaluator,
            tests=tuple(tests),
            inactive_state_ids=tuple(inactive),
            residuals=tuple(residuals),
            resource_cost=resource_cost or {},
            stopping_conditions=tuple(stopping_conditions),
            reopening_conditions=tuple(reopening_conditions),
        )

        self.transitions[edge.transition_id] = edge
        self._append(
            "transition",
            {
                **asdict(edge),
                "produced_states": [
                    asdict(state) for state in created
                ],
            },
        )
        return edge

    def record_support(
        self,
        *,
        conclusion_state_id: str,
        relation: str,
        measurements: Iterable[str],
        conditions: Iterable[str] = (),
        observations: Iterable[str] = (),
        contradictions: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        residuals: Iterable[str] = (),
        score: float | None = None,
    ) -> SupportRelation:
        if conclusion_state_id not in self.states:
            raise KeyError(
                f"unknown conclusion state: {conclusion_state_id}"
            )

        support = SupportRelation(
            support_id=_id("support"),
            conclusion_state_id=conclusion_state_id,
            relation=relation,
            measurements=tuple(measurements),
            conditions=tuple(conditions),
            observations=tuple(observations),
            contradictions=tuple(contradictions),
            dependencies=tuple(dependencies),
            residuals=tuple(residuals),
            score=score,
        )

        self.support_relations[support.support_id] = support
        self._append("support", asdict(support))
        return support

    def compare(
        self,
        *,
        conclusion_state_ids: Iterable[str],
        support_ids: Iterable[str],
        measurements: Iterable[str],
        conditions: Iterable[str] = (),
        best_supported_state_ids: Iterable[str] = (),
        incomparable_state_ids: Iterable[str] = (),
        known_exclusions: Iterable[str] = (),
        unrepresented_alternatives_possible: bool = True,
    ) -> Comparison:
        conclusion_ids = tuple(conclusion_state_ids)
        support_relation_ids = tuple(support_ids)

        for state_id in conclusion_ids:
            if state_id not in self.states:
                raise KeyError(f"unknown conclusion state: {state_id}")

        for support_id in support_relation_ids:
            if support_id not in self.support_relations:
                raise KeyError(
                    f"unknown support relation: {support_id}"
                )

        represented_conclusions = set(conclusion_ids)
        for support_id in support_relation_ids:
            support = self.support_relations[support_id]
            if support.conclusion_state_id not in represented_conclusions:
                raise ValueError(
                    "support relation refers to a conclusion outside "
                    "the comparison set"
                )

        comparison = Comparison(
            comparison_id=_id("comparison"),
            conclusion_state_ids=conclusion_ids,
            support_ids=support_relation_ids,
            measurements=tuple(measurements),
            conditions=tuple(conditions),
            best_supported_state_ids=tuple(
                best_supported_state_ids
            ),
            incomparable_state_ids=tuple(
                incomparable_state_ids
            ),
            known_exclusions=tuple(known_exclusions),
            unrepresented_alternatives_possible=(
                unrepresented_alternatives_possible
            ),
        )

        self.comparisons[comparison.comparison_id] = comparison
        self._append("comparison", asdict(comparison))
        return comparison

    def recursive_audit(
        self,
        *,
        target_transition_id: str,
        auditor: Evaluator,
        exposed_relations: Iterable[str],
        unrepresented_relations: Iterable[str],
        stopping_boundary: str,
    ) -> dict[str, Any]:
        if target_transition_id not in self.transitions:
            raise KeyError(
                f"unknown transition: {target_transition_id}"
            )

        payload = {
            "audit_id": _id("audit"),
            "target_transition_id": target_transition_id,
            "auditor": asdict(auditor),
            "exposed_relations": tuple(exposed_relations),
            "unrepresented_relations": tuple(
                unrepresented_relations
            ),
            "stopping_boundary": stopping_boundary,
        }

        self._append("recursive_audit", payload)
        return payload

    def verify(self) -> bool:
        prior_hash = None

        for sequence, record in enumerate(self._records):
            body = {
                "sequence": sequence,
                "kind": record["kind"],
                "prior_hash": prior_hash,
                "payload": record["payload"],
            }

            expected_hash = sha256(
                _canonical(body).encode()
            ).hexdigest()

            if record["sequence"] != sequence:
                return False

            if record["record_hash"] != expected_hash:
                return False

            prior_hash = record["record_hash"]

        return True

    def export_jsonl(self, path: str | Path) -> None:
        Path(path).write_text(
            "".join(
                _canonical(record) + "\n"
                for record in self._records
            ),
            encoding="utf-8",
        )


def evaluator(
    declared_account: str,
    *,
    criteria: Iterable[str],
    measurements: Iterable[str] = (),
    values: Iterable[str] = (),
    conditions: Iterable[str] = (),
    exclusions: Iterable[str] = (),
) -> Evaluator:
    return Evaluator(
        evaluator_id=_id("evaluator"),
        declared_account=declared_account,
        criteria=tuple(criteria),
        measurements=tuple(measurements),
        values=tuple(values),
        conditions=tuple(conditions),
        exclusions=tuple(exclusions),
    )
