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
class Distinction:
    """A represented specification of what can differ."""

    distinction_id: str
    name: str
    specification: str
    operationalization: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("distinction name must be explicit")
        if not self.specification.strip():
            raise ValueError("distinction specification must be explicit")


@dataclass(frozen=True)
class Measurement:
    """A represented result produced relative to one or more distinctions."""

    measurement_id: str
    result: str
    distinction_ids: tuple[str, ...]
    method: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.result.strip():
            raise ValueError("measurement result must be explicit")
        if not self.distinction_ids:
            raise ValueError(
                "measurement requires at least one represented distinction"
            )


@dataclass(frozen=True)
class Evaluator:
    evaluator_id: str
    declared_account: str
    criteria: tuple[str, ...]
    distinctions: tuple[str, ...] = ()
    measurements: tuple[str, ...] = ()
    support_relations: tuple[str, ...] = ()
    comparison_basis: tuple[str, ...] = ()
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
        if (
            self.confidence is not None
            and not 0.0 <= self.confidence <= 1.0
        ):
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class SupportRelation:
    """A represented basis relevant to treating a conclusion as true."""

    support_id: str
    conclusion_state_id: str
    relation: str
    basis: tuple[str, ...]
    distinction_ids: tuple[str, ...] = ()
    measurement_ids: tuple[str, ...] = ()
    observations: tuple[str, ...] = ()
    tests: tuple[str, ...] = ()
    predictions: tuple[str, ...] = ()
    contradictions: tuple[str, ...] = ()
    logical_relations: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    explanatory_relations: tuple[str, ...] = ()
    reproducibility: tuple[str, ...] = ()
    consequences: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()
    score: float | None = None

    def __post_init__(self) -> None:
        if self.relation not in SUPPORT_RELATIONS:
            raise ValueError(
                f"unsupported support relation: {self.relation}"
            )
        if not self.basis:
            raise ValueError(
                "support requires an explicit represented basis"
            )
        if self.score is not None and not 0.0 <= self.score <= 1.0:
            raise ValueError("support score must be between 0 and 1")


@dataclass(frozen=True)
class Comparison:
    """A represented comparison among conclusions."""

    comparison_id: str
    conclusion_state_ids: tuple[str, ...]
    support_ids: tuple[str, ...]
    basis: tuple[str, ...]
    distinction_ids: tuple[str, ...] = ()
    measurement_ids: tuple[str, ...] = ()
    criteria: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    evaluator_id: str | None = None
    best_supported_state_ids: tuple[str, ...] = ()
    incomparable_state_ids: tuple[str, ...] = ()
    known_exclusions: tuple[str, ...] = ()
    unresolved_relations: tuple[str, ...] = ()
    unrepresented_alternatives_possible: bool = True

    def __post_init__(self) -> None:
        if len(self.conclusion_state_ids) < 2:
            raise ValueError(
                "comparison requires at least two conclusions"
            )
        if not self.basis:
            raise ValueError(
                "comparison requires an explicit represented basis"
            )
        if not set(self.best_supported_state_ids).issubset(
            self.conclusion_state_ids
        ):
            raise ValueError(
                "best-supported conclusions must belong "
                "to the comparison set"
            )
        if not set(self.incomparable_state_ids).issubset(
            self.conclusion_state_ids
        ):
            raise ValueError(
                "incomparable conclusions must belong "
                "to the comparison set"
            )


@dataclass(frozen=True)
class InquiryState:
    state_id: str
    object: str
    representation: str
    status: str = "untested"
    observations: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    distinction_ids: tuple[str, ...] = ()
    measurement_ids: tuple[str, ...] = ()
    boundaries: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()
    beliefs: tuple[str, ...] = ()
    parent_state_ids: tuple[str, ...] = ()
    active: bool = True

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(
                f"unsupported relational status: {self.status}"
            )
        if not self.object.strip() or not self.representation.strip():
            raise ValueError(
                "object and representation must be explicit"
            )


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
    """Append-only graph of represented inquiry genealogy."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []
        self.states: dict[str, InquiryState] = {}
        self.transitions: dict[str, Transition] = {}
        self.beliefs: dict[str, Belief] = {}
        self.distinctions: dict[str, Distinction] = {}
        self.measurements: dict[str, Measurement] = {}
        self.support_relations: dict[str, SupportRelation] = {}
        self.comparisons: dict[str, Comparison] = {}

    @property
    def records(self) -> tuple[dict[str, Any], ...]:
        return tuple(self._records)

    def _append(self, kind: str, payload: dict[str, Any]) -> None:
        prior_hash = (
            self._records[-1]["record_hash"]
            if self._records
            else None
        )
        body = {
            "sequence": len(self._records),
            "kind": kind,
            "prior_hash": prior_hash,
            "payload": payload,
        }
        record_hash = sha256(
            _canonical(body).encode()
        ).hexdigest()
        self._records.append(
            {**body, "record_hash": record_hash}
        )

    def _require_distinctions(
        self,
        distinction_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(distinction_ids)
        for distinction_id in ids:
            if distinction_id not in self.distinctions:
                raise KeyError(
                    f"unknown distinction: {distinction_id}"
                )
        return ids

    def _require_measurements(
        self,
        measurement_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(measurement_ids)
        for measurement_id in ids:
            if measurement_id not in self.measurements:
                raise KeyError(
                    f"unknown measurement: {measurement_id}"
                )
        return ids

    def record_distinction(
        self,
        *,
        name: str,
        specification: str,
        operationalization: Iterable[str] = (),
        conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Distinction:
        distinction = Distinction(
            distinction_id=_id("distinction"),
            name=name,
            specification=specification,
            operationalization=tuple(operationalization),
            conditions=tuple(conditions),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )
        self.distinctions[distinction.distinction_id] = distinction
        self._append("distinction", asdict(distinction))
        return distinction

    def record_measurement(
        self,
        *,
        result: str,
        distinction_ids: Iterable[str],
        method: Iterable[str] = (),
        conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Measurement:
        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        measurement = Measurement(
            measurement_id=_id("measurement"),
            result=result,
            distinction_ids=represented_distinctions,
            method=tuple(method),
            conditions=tuple(conditions),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )
        self.measurements[measurement.measurement_id] = measurement
        self._append("measurement", asdict(measurement))
        return measurement

    def encounter(
        self,
        *,
        object: str,
        representation: str,
        observations: Iterable[str] = (),
        provenance: Iterable[str] = (),
        distinction_ids: Iterable[str] = (),
        measurement_ids: Iterable[str] = (),
        boundaries: Iterable[str] = (),
        residuals: Iterable[str] = (),
        beliefs: Iterable[str] = (),
    ) -> InquiryState:
        belief_ids = tuple(beliefs)
        for belief_id in belief_ids:
            if belief_id not in self.beliefs:
                raise KeyError(f"unknown belief: {belief_id}")

        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        represented_measurements = self._require_measurements(
            measurement_ids
        )

        state = InquiryState(
            state_id=_id("state"),
            object=object,
            representation=representation,
            observations=tuple(observations),
            provenance=tuple(provenance),
            distinction_ids=represented_distinctions,
            measurement_ids=represented_measurements,
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
                raise KeyError(
                    f"unknown prior state: {parent}"
                )

        candidate_data = list(candidates)
        selected = set(selected_indexes)

        if not candidate_data:
            raise ValueError(
                "at least one candidate is required"
            )

        if not selected:
            raise ValueError(
                "at least one selected index is required"
            )

        if not selected.issubset(
            range(len(candidate_data))
        ):
            raise ValueError(
                "selected indexes must identify candidates"
            )

        created: list[InquiryState] = []
        inactive: list[str] = []

        for index, candidate in enumerate(candidate_data):
            belief_ids = tuple(
                candidate.get("beliefs", ())
            )
            for belief_id in belief_ids:
                if belief_id not in self.beliefs:
                    raise KeyError(
                        f"unknown belief: {belief_id}"
                    )

            distinction_ids = self._require_distinctions(
                candidate.get("distinction_ids", ())
            )
            measurement_ids = self._require_measurements(
                candidate.get("measurement_ids", ())
            )

            is_active = index in selected
            candidate_status = candidate.get(
                "status",
                "untested",
            )

            if (
                not is_active
                and candidate_status == "untested"
            ):
                candidate_status = "inactive"

            state = InquiryState(
                state_id=_id("state"),
                object=candidate["object"],
                representation=candidate["representation"],
                status=candidate_status,
                observations=tuple(
                    candidate.get("observations", ())
                ),
                provenance=tuple(
                    candidate.get("provenance", ())
                ),
                distinction_ids=distinction_ids,
                measurement_ids=measurement_ids,
                boundaries=tuple(
                    candidate.get("boundaries", ())
                ),
                residuals=tuple(
                    candidate.get("residuals", ())
                ),
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
                    asdict(state)
                    for state in created
                ],
            },
        )
        return edge

    def record_support(
        self,
        *,
        conclusion_state_id: str,
        relation: str,
        basis: Iterable[str],
        distinction_ids: Iterable[str] = (),
        measurement_ids: Iterable[str] = (),
        observations: Iterable[str] = (),
        tests: Iterable[str] = (),
        predictions: Iterable[str] = (),
        contradictions: Iterable[str] = (),
        logical_relations: Iterable[str] = (),
        provenance: Iterable[str] = (),
        explanatory_relations: Iterable[str] = (),
        reproducibility: Iterable[str] = (),
        consequences: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        conditions: Iterable[str] = (),
        residuals: Iterable[str] = (),
        score: float | None = None,
    ) -> SupportRelation:
        if conclusion_state_id not in self.states:
            raise KeyError(
                f"unknown conclusion state: {conclusion_state_id}"
            )

        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        represented_measurements = self._require_measurements(
            measurement_ids
        )

        support = SupportRelation(
            support_id=_id("support"),
            conclusion_state_id=conclusion_state_id,
            relation=relation,
            basis=tuple(basis),
            distinction_ids=represented_distinctions,
            measurement_ids=represented_measurements,
            observations=tuple(observations),
            tests=tuple(tests),
            predictions=tuple(predictions),
            contradictions=tuple(contradictions),
            logical_relations=tuple(logical_relations),
            provenance=tuple(provenance),
            explanatory_relations=tuple(
                explanatory_relations
            ),
            reproducibility=tuple(reproducibility),
            consequences=tuple(consequences),
            dependencies=tuple(dependencies),
            conditions=tuple(conditions),
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
        basis: Iterable[str],
        distinction_ids: Iterable[str] = (),
        measurement_ids: Iterable[str] = (),
        criteria: Iterable[str] = (),
        methods: Iterable[str] = (),
        conditions: Iterable[str] = (),
        evaluator_id: str | None = None,
        best_supported_state_ids: Iterable[str] = (),
        incomparable_state_ids: Iterable[str] = (),
        known_exclusions: Iterable[str] = (),
        unresolved_relations: Iterable[str] = (),
        unrepresented_alternatives_possible: bool = True,
    ) -> Comparison:
        conclusion_ids = tuple(conclusion_state_ids)
        support_relation_ids = tuple(support_ids)

        for state_id in conclusion_ids:
            if state_id not in self.states:
                raise KeyError(
                    f"unknown conclusion state: {state_id}"
                )

        for support_id in support_relation_ids:
            if support_id not in self.support_relations:
                raise KeyError(
                    f"unknown support relation: {support_id}"
                )

        represented_conclusions = set(conclusion_ids)
        for support_id in support_relation_ids:
            support = self.support_relations[support_id]
            if (
                support.conclusion_state_id
                not in represented_conclusions
            ):
                raise ValueError(
                    "support relation refers to a conclusion "
                    "outside the comparison set"
                )

        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        represented_measurements = self._require_measurements(
            measurement_ids
        )

        comparison = Comparison(
            comparison_id=_id("comparison"),
            conclusion_state_ids=conclusion_ids,
            support_ids=support_relation_ids,
            basis=tuple(basis),
            distinction_ids=represented_distinctions,
            measurement_ids=represented_measurements,
            criteria=tuple(criteria),
            methods=tuple(methods),
            conditions=tuple(conditions),
            evaluator_id=evaluator_id,
            best_supported_state_ids=tuple(
                best_supported_state_ids
            ),
            incomparable_state_ids=tuple(
                incomparable_state_ids
            ),
            known_exclusions=tuple(known_exclusions),
            unresolved_relations=tuple(
                unresolved_relations
            ),
            unrepresented_alternatives_possible=(
                unrepresented_alternatives_possible
            ),
        )

        self.comparisons[
            comparison.comparison_id
        ] = comparison
        self._append(
            "comparison",
            asdict(comparison),
        )
        return comparison

    def recursive_audit(
        self,
        *,
        target_transition_id: str,
        auditor: Evaluator,
        exposed_relations: Iterable[str],
        unrepresented_relations: Iterable[str],
        stopping_boundary: str,
        distinction_ids: Iterable[str] = (),
        measurement_ids: Iterable[str] = (),
        support_ids: Iterable[str] = (),
        comparison_ids: Iterable[str] = (),
        comparison_basis: Iterable[str] = (),
    ) -> dict[str, Any]:
        if target_transition_id not in self.transitions:
            raise KeyError(
                f"unknown transition: {target_transition_id}"
            )

        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        represented_measurements = self._require_measurements(
            measurement_ids
        )

        represented_support = tuple(support_ids)
        for support_id in represented_support:
            if support_id not in self.support_relations:
                raise KeyError(
                    f"unknown support relation: {support_id}"
                )

        represented_comparisons = tuple(comparison_ids)
        for comparison_id in represented_comparisons:
            if comparison_id not in self.comparisons:
                raise KeyError(
                    f"unknown comparison: {comparison_id}"
                )

        payload = {
            "audit_id": _id("audit"),
            "target_transition_id": target_transition_id,
            "auditor": asdict(auditor),
            "distinction_ids": represented_distinctions,
            "measurement_ids": represented_measurements,
            "support_ids": represented_support,
            "comparison_ids": represented_comparisons,
            "comparison_basis": tuple(comparison_basis),
            "exposed_relations": tuple(exposed_relations),
            "unrepresented_relations": tuple(
                unrepresented_relations
            ),
            "stopping_boundary": stopping_boundary,
        }

        self._append(
            "recursive_audit",
            payload,
        )
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

    def export_jsonl(
        self,
        path: str | Path,
    ) -> None:
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
    distinctions: Iterable[str] = (),
    measurements: Iterable[str] = (),
    support_relations: Iterable[str] = (),
    comparison_basis: Iterable[str] = (),
    values: Iterable[str] = (),
    conditions: Iterable[str] = (),
    exclusions: Iterable[str] = (),
) -> Evaluator:
    return Evaluator(
        evaluator_id=_id("evaluator"),
        declared_account=declared_account,
        criteria=tuple(criteria),
        distinctions=tuple(distinctions),
        measurements=tuple(measurements),
        support_relations=tuple(support_relations),
        comparison_basis=tuple(comparison_basis),
        values=tuple(values),
        conditions=tuple(conditions),
        exclusions=tuple(exclusions),
    )
