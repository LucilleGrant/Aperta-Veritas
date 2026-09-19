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
    "unranked",
    "inactive",
    "reactivated",
}

SUPPORT_RELATIONS = {
    "supports",
    "contradicts",
    "neutral",
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
            raise ValueError(
                "distinction specification must be explicit"
            )


@dataclass(frozen=True)
class Measurement:
    """A represented result produced relative to distinctions."""

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
class Basis:
    """
    A represented element associated with acceptance, inquiry,
    allocation, evaluation, or support.

    Recording a basis does not classify it as epistemic support.
    """

    basis_id: str
    description: str
    kind: str = "unspecified"
    provenance: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.description.strip():
            raise ValueError("basis description must be explicit")
        if not self.kind.strip():
            raise ValueError("basis kind must be explicit")


@dataclass(frozen=True)
class AcceptanceBasis:
    """Why a represented state is accepted, selected, or acted upon."""

    acceptance_id: str
    state_id: str
    basis_ids: tuple[str, ...]
    account: str
    conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.basis_ids:
            raise ValueError(
                "acceptance basis requires at least one represented basis"
            )
        if not self.account.strip():
            raise ValueError("acceptance account must be explicit")


@dataclass(frozen=True)
class InquiryBasis:
    """
    A represented basis under which further examination could occur.

    Recording an inquiry basis does not assign priority or resources.
    """

    inquiry_basis_id: str
    state_id: str
    basis_ids: tuple[str, ...]
    account: str
    possible_tests: tuple[str, ...] = ()
    missing_distinctions: tuple[str, ...] = ()
    resource_requirements: tuple[str, ...] = ()
    stopping_conditions: tuple[str, ...] = ()
    reopening_conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.basis_ids:
            raise ValueError(
                "inquiry basis requires at least one represented basis"
            )
        if not self.account.strip():
            raise ValueError("inquiry account must be explicit")


@dataclass(frozen=True)
class InquiryOperation:
    """A represented possible continuation of inquiry."""

    inquiry_operation_id: str
    account: str
    target_state_ids: tuple[str, ...]
    inquiry_basis_ids: tuple[str, ...] = ()
    operation: str = ""
    requirements: tuple[str, ...] = ()
    expected_outputs: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.account.strip():
            raise ValueError(
                "inquiry operation account must be explicit"
            )
        if not self.operation.strip():
            raise ValueError(
                "inquiry operation must be explicit"
            )
        if not self.target_state_ids:
            raise ValueError(
                "inquiry operation requires a represented target"
            )


@dataclass(frozen=True)
class AllocationBasis:
    """
    Represented basis used in allocating resources among possible
    inquiry operations.

    Recording an allocation basis does not make it epistemic support.
    """

    allocation_basis_id: str
    account: str
    basis_ids: tuple[str, ...]
    criteria: tuple[str, ...]
    conditions: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    purposes: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.account.strip():
            raise ValueError(
                "allocation basis account must be explicit"
            )
        if not self.basis_ids:
            raise ValueError(
                "allocation basis requires represented basis IDs"
            )
        if not self.criteria:
            raise ValueError(
                "allocation basis requires explicit criteria"
            )


@dataclass(frozen=True)
class InquiryPriority:
    """A represented ordering or preference among inquiry operations."""

    inquiry_priority_id: str
    inquiry_operation_ids: tuple[str, ...]
    allocation_basis_id: str
    ordered_operation_ids: tuple[str, ...]
    account: str
    conditions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.inquiry_operation_ids:
            raise ValueError(
                "inquiry priority requires represented operations"
            )
        if not self.ordered_operation_ids:
            raise ValueError(
                "inquiry priority requires an explicit ordering"
            )
        if set(self.ordered_operation_ids) != set(
            self.inquiry_operation_ids
        ):
            raise ValueError(
                "priority ordering must contain exactly "
                "the represented inquiry operations"
            )
        if len(self.ordered_operation_ids) != len(
            set(self.ordered_operation_ids)
        ):
            raise ValueError(
                "priority ordering cannot contain duplicates"
            )
        if not self.account.strip():
            raise ValueError(
                "inquiry priority account must be explicit"
            )


@dataclass(frozen=True)
class Allocator:
    """A represented process participating in resource allocation."""

    allocator_id: str
    declared_account: str
    criteria: tuple[str, ...]
    allocation_basis_ids: tuple[str, ...] = ()
    resource_conditions: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    generator_feedback: tuple[str, ...] = ()
    evaluator_feedback: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.declared_account.strip():
            raise ValueError("allocator account must be explicit")
        if not self.criteria:
            raise ValueError(
                "allocator requires at least one represented criterion"
            )


@dataclass(frozen=True)
class ResourceAllocation:
    """
    A represented assignment of resources to inquiry operations.

    Allocation does not establish epistemic support or truth.
    """

    resource_allocation_id: str
    allocator: Allocator
    inquiry_operation_ids: tuple[str, ...]
    allocation_basis_ids: tuple[str, ...]
    inquiry_priority_id: str | None
    assigned_resources: dict[str, dict[str, float]]
    unallocated_operation_ids: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.inquiry_operation_ids:
            raise ValueError(
                "resource allocation requires inquiry operations"
            )
        if not self.allocation_basis_ids:
            raise ValueError(
                "resource allocation requires an allocation basis"
            )

        represented = set(self.inquiry_operation_ids)
        assigned = set(self.assigned_resources)
        unallocated = set(self.unallocated_operation_ids)

        if not assigned.issubset(represented):
            raise ValueError(
                "assigned resources refer to unknown inquiry operations"
            )
        if not unallocated.issubset(represented):
            raise ValueError(
                "unallocated operations must belong to allocation set"
            )
        if assigned & unallocated:
            raise ValueError(
                "an inquiry operation cannot be both allocated "
                "and unallocated in the same event"
            )
        if assigned | unallocated != represented:
            raise ValueError(
                "allocation must explicitly account for every "
                "represented inquiry operation"
            )

        for operation_resources in self.assigned_resources.values():
            if not operation_resources:
                raise ValueError(
                    "allocated inquiry operation requires resources"
                )
            for resource, amount in operation_resources.items():
                if not resource.strip():
                    raise ValueError(
                        "resource name must be explicit"
                    )
                if amount < 0:
                    raise ValueError(
                        "resource allocation cannot be negative"
                    )


@dataclass(frozen=True)
class Activation:
    """A represented activation or deactivation of inquiry operations."""

    activation_id: str
    inquiry_operation_ids: tuple[str, ...]
    resource_allocation_id: str | None
    active: bool
    account: str
    conditions: tuple[str, ...] = ()
    stopping_conditions: tuple[str, ...] = ()
    reopening_conditions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.inquiry_operation_ids:
            raise ValueError(
                "activation requires represented inquiry operations"
            )
        if not self.account.strip():
            raise ValueError(
                "activation account must be explicit"
            )
        if self.active and self.resource_allocation_id is None:
            raise ValueError(
                "activation requires a represented resource allocation"
            )


@dataclass(frozen=True)
class Evaluator:
    evaluator_id: str
    declared_account: str
    criteria: tuple[str, ...]
    distinctions: tuple[str, ...] = ()
    measurements: tuple[str, ...] = ()
    basis_ids: tuple[str, ...] = ()
    support_relations: tuple[str, ...] = ()
    support_claims: tuple[str, ...] = ()
    comparison_basis: tuple[str, ...] = ()
    values: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()


@dataclass(frozen=True)
class Generator:
    """A represented process by which candidates become available."""

    generator_id: str
    declared_account: str
    operations: tuple[str, ...]
    distinction_ids: tuple[str, ...] = ()
    source_state_ids: tuple[str, ...] = ()
    retrieval: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    allocator_feedback: tuple[str, ...] = ()
    evaluator_feedback: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()
    resource_limits: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.declared_account.strip():
            raise ValueError("generator account must be explicit")
        if not self.operations:
            raise ValueError(
                "generator requires at least one represented operation"
            )


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
    """
    A claimed relation between represented bases and whether a
    conclusion should presently be treated as true.
    """

    support_id: str
    conclusion_state_id: str
    relation: str
    basis_ids: tuple[str, ...]
    account: str
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
        if not self.basis_ids:
            raise ValueError(
                "support relation requires represented basis IDs"
            )
        if not self.account.strip():
            raise ValueError(
                "support relation account must be explicit"
            )
        if self.score is not None and not 0.0 <= self.score <= 1.0:
            raise ValueError("support score must be between 0 and 1")


@dataclass(frozen=True)
class SupportClaim:
    """
    A claim that represented support relations bear on whether a
    conclusion is true.

    Recording the claim does not certify it.
    """

    support_claim_id: str
    conclusion_state_id: str
    support_relation_ids: tuple[str, ...]
    claim: str
    conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.support_relation_ids:
            raise ValueError(
                "support claim requires a represented support relation"
            )
        if not self.claim.strip():
            raise ValueError("support claim must be explicit")


@dataclass(frozen=True)
class Comparison:
    """A represented comparison among conclusions."""

    comparison_id: str
    conclusion_state_ids: tuple[str, ...]
    support_claim_ids: tuple[str, ...]
    basis: tuple[str, ...]
    distinction_ids: tuple[str, ...] = ()
    measurement_ids: tuple[str, ...] = ()
    criteria: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    evaluator_id: str | None = None
    best_supported_state_ids: tuple[str, ...] = ()
    unranked_state_ids: tuple[str, ...] = ()
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

        represented = set(self.conclusion_state_ids)

        if not set(self.best_supported_state_ids).issubset(
            represented
        ):
            raise ValueError(
                "best-supported conclusions must belong "
                "to the comparison set"
            )

        if not set(self.unranked_state_ids).issubset(represented):
            raise ValueError(
                "unranked conclusions must belong "
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
class Generation:
    """A represented event that makes candidates available."""

    generation_id: str
    generator: Generator
    source_state_ids: tuple[str, ...]
    generated_state_ids: tuple[str, ...]
    operation: str
    distinction_ids: tuple[str, ...] = ()
    generated_alternatives: tuple[str, ...] = ()
    known_exclusions: tuple[str, ...] = ()
    unrepresented_alternatives_possible: bool = True
    resource_cost: dict[str, float] = field(default_factory=dict)
    conditions: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.generated_state_ids:
            raise ValueError(
                "generation must produce at least one represented state"
            )
        if not self.operation.strip():
            raise ValueError("generation operation must be explicit")


@dataclass(frozen=True)
class Transition:
    transition_id: str
    prior_state_ids: tuple[str, ...]
    resulting_state_ids: tuple[str, ...]
    operation: str
    transformation: str
    evaluator: Evaluator
    generation_id: str | None = None
    resource_allocation_id: str | None = None
    activation_ids: tuple[str, ...] = ()
    tests: tuple[str, ...] = ()
    inactive_state_ids: tuple[str, ...] = ()
    acceptance_basis_ids: tuple[str, ...] = ()
    inquiry_basis_ids: tuple[str, ...] = ()
    support_claim_ids: tuple[str, ...] = ()
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


@dataclass(frozen=True)
class Recontextualization:
    """
    A later represented relation involving retained earlier states.

    Earlier states remain unchanged.
    """

    recontextualization_id: str
    prior_state_ids: tuple[str, ...]
    distinction_ids: tuple[str, ...]
    relation: str
    resulting_state_id: str | None = None
    generator_id: str | None = None
    basis_ids: tuple[str, ...] = ()
    support_claim_ids: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()
    residuals: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.prior_state_ids:
            raise ValueError(
                "recontextualization requires retained prior states"
            )
        if not self.distinction_ids:
            raise ValueError(
                "recontextualization requires a represented distinction"
            )
        if not self.relation.strip():
            raise ValueError(
                "recontextualization relation must be explicit"
            )


class InquiryLedger:
    """Append-only graph of represented inquiry genealogy."""

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []

        self.states: dict[str, InquiryState] = {}
        self.transitions: dict[str, Transition] = {}
        self.generations: dict[str, Generation] = {}
        self.recontextualizations: dict[
            str, Recontextualization
        ] = {}

        self.beliefs: dict[str, Belief] = {}
        self.distinctions: dict[str, Distinction] = {}
        self.measurements: dict[str, Measurement] = {}

        self.bases: dict[str, Basis] = {}
        self.acceptance_bases: dict[
            str, AcceptanceBasis
        ] = {}
        self.inquiry_bases: dict[str, InquiryBasis] = {}
        self.inquiry_operations: dict[
            str, InquiryOperation
        ] = {}
        self.allocation_bases: dict[
            str, AllocationBasis
        ] = {}
        self.inquiry_priorities: dict[
            str, InquiryPriority
        ] = {}
        self.resource_allocations: dict[
            str, ResourceAllocation
        ] = {}
        self.activations: dict[str, Activation] = {}

        self.support_relations: dict[
            str, SupportRelation
        ] = {}
        self.support_claims: dict[str, SupportClaim] = {}
        self.comparisons: dict[str, Comparison] = {}

    @property
    def records(self) -> tuple[dict[str, Any], ...]:
        return tuple(self._records)

    def _append(
        self,
        kind: str,
        payload: dict[str, Any],
    ) -> None:
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

    def _require_states(
        self,
        state_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(state_ids)
        for state_id in ids:
            if state_id not in self.states:
                raise KeyError(f"unknown state: {state_id}")
        return ids

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

    def _require_bases(
        self,
        basis_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(basis_ids)
        for basis_id in ids:
            if basis_id not in self.bases:
                raise KeyError(f"unknown basis: {basis_id}")
        return ids

    def _require_acceptance_bases(
        self,
        acceptance_basis_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(acceptance_basis_ids)
        for acceptance_id in ids:
            if acceptance_id not in self.acceptance_bases:
                raise KeyError(
                    f"unknown acceptance basis: {acceptance_id}"
                )
        return ids

    def _require_inquiry_bases(
        self,
        inquiry_basis_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(inquiry_basis_ids)
        for inquiry_basis_id in ids:
            if inquiry_basis_id not in self.inquiry_bases:
                raise KeyError(
                    f"unknown inquiry basis: {inquiry_basis_id}"
                )
        return ids

    def _require_inquiry_operations(
        self,
        inquiry_operation_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(inquiry_operation_ids)
        for inquiry_operation_id in ids:
            if inquiry_operation_id not in self.inquiry_operations:
                raise KeyError(
                    "unknown inquiry operation: "
                    f"{inquiry_operation_id}"
                )
        return ids

    def _require_allocation_bases(
        self,
        allocation_basis_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(allocation_basis_ids)
        for allocation_basis_id in ids:
            if allocation_basis_id not in self.allocation_bases:
                raise KeyError(
                    "unknown allocation basis: "
                    f"{allocation_basis_id}"
                )
        return ids

    def _require_inquiry_priorities(
        self,
        inquiry_priority_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(inquiry_priority_ids)
        for inquiry_priority_id in ids:
            if inquiry_priority_id not in self.inquiry_priorities:
                raise KeyError(
                    "unknown inquiry priority: "
                    f"{inquiry_priority_id}"
                )
        return ids

    def _require_resource_allocations(
        self,
        resource_allocation_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(resource_allocation_ids)
        for resource_allocation_id in ids:
            if (
                resource_allocation_id
                not in self.resource_allocations
            ):
                raise KeyError(
                    "unknown resource allocation: "
                    f"{resource_allocation_id}"
                )
        return ids

    def _require_activations(
        self,
        activation_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(activation_ids)
        for activation_id in ids:
            if activation_id not in self.activations:
                raise KeyError(
                    f"unknown activation: {activation_id}"
                )
        return ids

    def _require_support_relations(
        self,
        support_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(support_ids)
        for support_id in ids:
            if support_id not in self.support_relations:
                raise KeyError(
                    f"unknown support relation: {support_id}"
                )
        return ids

    def _require_support_claims(
        self,
        support_claim_ids: Iterable[str],
    ) -> tuple[str, ...]:
        ids = tuple(support_claim_ids)
        for support_claim_id in ids:
            if support_claim_id not in self.support_claims:
                raise KeyError(
                    f"unknown support claim: {support_claim_id}"
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

        self.distinctions[
            distinction.distinction_id
        ] = distinction
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

        self.measurements[
            measurement.measurement_id
        ] = measurement
        self._append("measurement", asdict(measurement))
        return measurement

    def record_basis(
        self,
        *,
        description: str,
        kind: str = "unspecified",
        provenance: Iterable[str] = (),
        conditions: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Basis:
        basis = Basis(
            basis_id=_id("basis"),
            description=description,
            kind=kind,
            provenance=tuple(provenance),
            conditions=tuple(conditions),
            dependencies=tuple(dependencies),
            residuals=tuple(residuals),
        )

        self.bases[basis.basis_id] = basis
        self._append("basis", asdict(basis))
        return basis

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

    def record_acceptance_basis(
        self,
        *,
        state_id: str,
        basis_ids: Iterable[str],
        account: str,
        conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> AcceptanceBasis:
        self._require_states((state_id,))
        represented_bases = self._require_bases(basis_ids)

        acceptance = AcceptanceBasis(
            acceptance_id=_id("acceptance"),
            state_id=state_id,
            basis_ids=represented_bases,
            account=account,
            conditions=tuple(conditions),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )

        self.acceptance_bases[
            acceptance.acceptance_id
        ] = acceptance
        self._append(
            "acceptance_basis",
            asdict(acceptance),
        )
        return acceptance

    def record_inquiry_basis(
        self,
        *,
        state_id: str,
        basis_ids: Iterable[str],
        account: str,
        possible_tests: Iterable[str] = (),
        missing_distinctions: Iterable[str] = (),
        resource_requirements: Iterable[str] = (),
        stopping_conditions: Iterable[str] = (),
        reopening_conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> InquiryBasis:
        self._require_states((state_id,))
        represented_bases = self._require_bases(basis_ids)

        inquiry_basis = InquiryBasis(
            inquiry_basis_id=_id("inquiry_basis"),
            state_id=state_id,
            basis_ids=represented_bases,
            account=account,
            possible_tests=tuple(possible_tests),
            missing_distinctions=tuple(missing_distinctions),
            resource_requirements=tuple(resource_requirements),
            stopping_conditions=tuple(stopping_conditions),
            reopening_conditions=tuple(reopening_conditions),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )

        self.inquiry_bases[
            inquiry_basis.inquiry_basis_id
        ] = inquiry_basis
        self._append(
            "inquiry_basis",
            asdict(inquiry_basis),
        )
        return inquiry_basis

    def record_inquiry_operation(
        self,
        *,
        account: str,
        target_state_ids: Iterable[str],
        operation: str,
        inquiry_basis_ids: Iterable[str] = (),
        requirements: Iterable[str] = (),
        expected_outputs: Iterable[str] = (),
        conditions: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> InquiryOperation:
        targets = self._require_states(target_state_ids)
        represented_inquiry = self._require_inquiry_bases(
            inquiry_basis_ids
        )

        for inquiry_basis_id in represented_inquiry:
            inquiry_basis = self.inquiry_bases[inquiry_basis_id]
            if inquiry_basis.state_id not in targets:
                raise ValueError(
                    "inquiry basis must concern a target state "
                    "of the inquiry operation"
                )

        inquiry_operation = InquiryOperation(
            inquiry_operation_id=_id("inquiry_operation"),
            account=account,
            target_state_ids=targets,
            inquiry_basis_ids=represented_inquiry,
            operation=operation,
            requirements=tuple(requirements),
            expected_outputs=tuple(expected_outputs),
            conditions=tuple(conditions),
            dependencies=tuple(dependencies),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )

        self.inquiry_operations[
            inquiry_operation.inquiry_operation_id
        ] = inquiry_operation
        self._append(
            "inquiry_operation",
            asdict(inquiry_operation),
        )
        return inquiry_operation

    def record_allocation_basis(
        self,
        *,
        account: str,
        basis_ids: Iterable[str],
        criteria: Iterable[str],
        conditions: Iterable[str] = (),
        constraints: Iterable[str] = (),
        purposes: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> AllocationBasis:
        represented_bases = self._require_bases(basis_ids)

        allocation_basis = AllocationBasis(
            allocation_basis_id=_id("allocation_basis"),
            account=account,
            basis_ids=represented_bases,
            criteria=tuple(criteria),
            conditions=tuple(conditions),
            constraints=tuple(constraints),
            purposes=tuple(purposes),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )

        self.allocation_bases[
            allocation_basis.allocation_basis_id
        ] = allocation_basis
        self._append(
            "allocation_basis",
            asdict(allocation_basis),
        )
        return allocation_basis

    def record_inquiry_priority(
        self,
        *,
        inquiry_operation_ids: Iterable[str],
        allocation_basis_id: str,
        ordered_operation_ids: Iterable[str],
        account: str,
        conditions: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> InquiryPriority:
        operations = self._require_inquiry_operations(
            inquiry_operation_ids
        )
        self._require_allocation_bases((allocation_basis_id,))
        ordered = self._require_inquiry_operations(
            ordered_operation_ids
        )

        priority = InquiryPriority(
            inquiry_priority_id=_id("inquiry_priority"),
            inquiry_operation_ids=operations,
            allocation_basis_id=allocation_basis_id,
            ordered_operation_ids=ordered,
            account=account,
            conditions=tuple(conditions),
            residuals=tuple(residuals),
        )

        self.inquiry_priorities[
            priority.inquiry_priority_id
        ] = priority
        self._append(
            "inquiry_priority",
            asdict(priority),
        )
        return priority

    def allocate_resources(
        self,
        *,
        inquiry_operation_ids: Iterable[str],
        allocator: Allocator,
        allocation_basis_ids: Iterable[str],
        assigned_resources: dict[str, dict[str, float]],
        inquiry_priority_id: str | None = None,
        unallocated_operation_ids: Iterable[str] = (),
        conditions: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> ResourceAllocation:
        operations = self._require_inquiry_operations(
            inquiry_operation_ids
        )
        represented_bases = self._require_allocation_bases(
            allocation_basis_ids
        )

        allocator_basis_ids = self._require_allocation_bases(
            allocator.allocation_basis_ids
        )
        if (
            allocator_basis_ids
            and not set(allocator_basis_ids).issubset(
                set(represented_bases)
            )
        ):
            raise ValueError(
                "allocator allocation bases must be represented "
                "by the allocation event"
            )

        priority_id = inquiry_priority_id
        if priority_id is not None:
            self._require_inquiry_priorities((priority_id,))
            priority = self.inquiry_priorities[priority_id]
            if set(priority.inquiry_operation_ids) != set(operations):
                raise ValueError(
                    "inquiry priority must concern exactly "
                    "the allocation operation set"
                )
            if priority.allocation_basis_id not in represented_bases:
                raise ValueError(
                    "priority allocation basis must be represented "
                    "by the allocation event"
                )

        assigned = {
            operation_id: dict(resources)
            for operation_id, resources
            in assigned_resources.items()
        }
        self._require_inquiry_operations(assigned.keys())

        unallocated = self._require_inquiry_operations(
            unallocated_operation_ids
        )

        allocation = ResourceAllocation(
            resource_allocation_id=_id("resource_allocation"),
            allocator=allocator,
            inquiry_operation_ids=operations,
            allocation_basis_ids=represented_bases,
            inquiry_priority_id=priority_id,
            assigned_resources=assigned,
            unallocated_operation_ids=unallocated,
            conditions=tuple(conditions),
            dependencies=tuple(dependencies),
            residuals=tuple(residuals),
        )

        self.resource_allocations[
            allocation.resource_allocation_id
        ] = allocation
        self._append(
            "resource_allocation",
            asdict(allocation),
        )
        return allocation

    def activate_inquiry(
        self,
        *,
        inquiry_operation_ids: Iterable[str],
        resource_allocation_id: str,
        account: str,
        conditions: Iterable[str] = (),
        stopping_conditions: Iterable[str] = (),
        reopening_conditions: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Activation:
        operations = self._require_inquiry_operations(
            inquiry_operation_ids
        )
        self._require_resource_allocations(
            (resource_allocation_id,)
        )

        allocation = self.resource_allocations[
            resource_allocation_id
        ]
        allocated = set(allocation.assigned_resources)

        if not set(operations).issubset(allocated):
            raise ValueError(
                "active inquiry operations must have represented "
                "resource allocations"
            )

        activation = Activation(
            activation_id=_id("activation"),
            inquiry_operation_ids=operations,
            resource_allocation_id=resource_allocation_id,
            active=True,
            account=account,
            conditions=tuple(conditions),
            stopping_conditions=tuple(stopping_conditions),
            reopening_conditions=tuple(reopening_conditions),
            residuals=tuple(residuals),
        )

        self.activations[
            activation.activation_id
        ] = activation
        self._append(
            "activation",
            asdict(activation),
        )
        return activation

    def deactivate_inquiry(
        self,
        *,
        inquiry_operation_ids: Iterable[str],
        account: str,
        resource_allocation_id: str | None = None,
        conditions: Iterable[str] = (),
        stopping_conditions: Iterable[str] = (),
        reopening_conditions: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Activation:
        operations = self._require_inquiry_operations(
            inquiry_operation_ids
        )

        if resource_allocation_id is not None:
            self._require_resource_allocations(
                (resource_allocation_id,)
            )

        activation = Activation(
            activation_id=_id("activation"),
            inquiry_operation_ids=operations,
            resource_allocation_id=resource_allocation_id,
            active=False,
            account=account,
            conditions=tuple(conditions),
            stopping_conditions=tuple(stopping_conditions),
            reopening_conditions=tuple(reopening_conditions),
            residuals=tuple(residuals),
        )

        self.activations[
            activation.activation_id
        ] = activation
        self._append(
            "activation",
            asdict(activation),
        )
        return activation

    def record_support(
        self,
        *,
        conclusion_state_id: str,
        relation: str,
        basis_ids: Iterable[str],
        account: str,
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
        self._require_states((conclusion_state_id,))
        represented_bases = self._require_bases(basis_ids)

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
            basis_ids=represented_bases,
            account=account,
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
        self._append(
            "support_relation",
            asdict(support),
        )
        return support

    def record_support_claim(
        self,
        *,
        conclusion_state_id: str,
        support_relation_ids: Iterable[str],
        claim: str,
        conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        dependencies: Iterable[str] = (),
        exclusions: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> SupportClaim:
        self._require_states((conclusion_state_id,))

        represented_support = self._require_support_relations(
            support_relation_ids
        )

        for support_id in represented_support:
            support = self.support_relations[support_id]
            if support.conclusion_state_id != conclusion_state_id:
                raise ValueError(
                    "support relation and support claim "
                    "must concern the same conclusion"
                )

        support_claim = SupportClaim(
            support_claim_id=_id("support_claim"),
            conclusion_state_id=conclusion_state_id,
            support_relation_ids=represented_support,
            claim=claim,
            conditions=tuple(conditions),
            provenance=tuple(provenance),
            dependencies=tuple(dependencies),
            exclusions=tuple(exclusions),
            residuals=tuple(residuals),
        )

        self.support_claims[
            support_claim.support_claim_id
        ] = support_claim
        self._append(
            "support_claim",
            asdict(support_claim),
        )
        return support_claim

    def generate(
        self,
        *,
        source_state_ids: Iterable[str],
        candidates: Iterable[dict[str, Any]],
        generator: Generator,
        operation: str,
        distinction_ids: Iterable[str] = (),
        generated_alternatives: Iterable[str] = (),
        known_exclusions: Iterable[str] = (),
        unrepresented_alternatives_possible: bool = True,
        resource_cost: dict[str, float] | None = None,
        conditions: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Generation:
        sources = self._require_states(source_state_ids)

        if not sources:
            raise ValueError(
                "generation requires at least one source state"
            )

        represented_distinctions = self._require_distinctions(
            distinction_ids
        )

        generator_distinctions = self._require_distinctions(
            generator.distinction_ids
        )

        generator_sources = tuple(generator.source_state_ids)
        if generator_sources:
            self._require_states(generator_sources)

        if (
            generator_sources
            and generator_sources != sources
        ):
            raise ValueError(
                "generator source states must match "
                "generation source states"
            )

        if (
            generator_distinctions
            and not set(generator_distinctions).issubset(
                set(represented_distinctions)
            )
        ):
            raise ValueError(
                "generator distinctions must be represented "
                "by the generation event"
            )

        candidate_data = list(candidates)

        if not candidate_data:
            raise ValueError(
                "generation requires at least one candidate"
            )

        created: list[InquiryState] = []

        for candidate in candidate_data:
            belief_ids = tuple(
                candidate.get("beliefs", ())
            )
            for belief_id in belief_ids:
                if belief_id not in self.beliefs:
                    raise KeyError(
                        f"unknown belief: {belief_id}"
                    )

            candidate_distinctions = (
                self._require_distinctions(
                    candidate.get(
                        "distinction_ids",
                        represented_distinctions,
                    )
                )
            )

            candidate_measurements = (
                self._require_measurements(
                    candidate.get(
                        "measurement_ids",
                        (),
                    )
                )
            )

            state = InquiryState(
                state_id=_id("state"),
                object=candidate["object"],
                representation=candidate["representation"],
                status=candidate.get(
                    "status",
                    "untested",
                ),
                observations=tuple(
                    candidate.get("observations", ())
                ),
                provenance=tuple(
                    candidate.get("provenance", ())
                ),
                distinction_ids=candidate_distinctions,
                measurement_ids=candidate_measurements,
                boundaries=tuple(
                    candidate.get("boundaries", ())
                ),
                residuals=tuple(
                    candidate.get("residuals", ())
                ),
                beliefs=belief_ids,
                parent_state_ids=sources,
                active=False,
            )

            self.states[state.state_id] = state
            created.append(state)

        generation = Generation(
            generation_id=_id("generation"),
            generator=generator,
            source_state_ids=sources,
            generated_state_ids=tuple(
                state.state_id for state in created
            ),
            operation=operation,
            distinction_ids=represented_distinctions,
            generated_alternatives=tuple(
                generated_alternatives
            ),
            known_exclusions=tuple(known_exclusions),
            unrepresented_alternatives_possible=(
                unrepresented_alternatives_possible
            ),
            resource_cost=resource_cost or {},
            conditions=tuple(conditions),
            residuals=tuple(residuals),
        )

        self.generations[
            generation.generation_id
        ] = generation

        self._append(
            "generation",
            {
                **asdict(generation),
                "produced_states": [
                    asdict(state)
                    for state in created
                ],
            },
        )

        return generation

    def transition_generated(
        self,
        *,
        generation_id: str,
        operation: str,
        transformation: str,
        evaluator: Evaluator,
        selected_state_ids: Iterable[str],
        resource_allocation_id: str | None = None,
        activation_ids: Iterable[str] = (),
        tests: Iterable[str] = (),
        acceptance_basis_ids: Iterable[str] = (),
        inquiry_basis_ids: Iterable[str] = (),
        support_claim_ids: Iterable[str] = (),
        residuals: Iterable[str] = (),
        resource_cost: dict[str, float] | None = None,
        stopping_conditions: Iterable[str] = (),
        reopening_conditions: Iterable[str] = (),
    ) -> Transition:
        if generation_id not in self.generations:
            raise KeyError(
                f"unknown generation: {generation_id}"
            )

        generation = self.generations[generation_id]
        generated = tuple(generation.generated_state_ids)
        selected = tuple(selected_state_ids)

        if not selected:
            raise ValueError(
                "at least one selected state is required"
            )

        if not set(selected).issubset(set(generated)):
            raise ValueError(
                "selected states must belong to generation"
            )

        represented_acceptance = (
            self._require_acceptance_bases(
                acceptance_basis_ids
            )
        )
        represented_inquiry = self._require_inquiry_bases(
            inquiry_basis_ids
        )
        represented_support_claims = (
            self._require_support_claims(
                support_claim_ids
            )
        )

        represented_activations = self._require_activations(
            activation_ids
        )

        if resource_allocation_id is not None:
            self._require_resource_allocations(
                (resource_allocation_id,)
            )

        for activation_id in represented_activations:
            activation = self.activations[activation_id]
            if (
                resource_allocation_id is not None
                and activation.resource_allocation_id
                not in (None, resource_allocation_id)
            ):
                raise ValueError(
                    "transition activation must refer to the "
                    "represented resource allocation"
                )

        selected_set = set(selected)
        resulting: list[InquiryState] = []
        inactive: list[str] = []

        for state_id in generated:
            old_state = self.states[state_id]
            is_active = state_id in selected_set

            status = old_state.status
            if not is_active and status == "untested":
                status = "inactive"

            state = InquiryState(
                state_id=_id("state"),
                object=old_state.object,
                representation=old_state.representation,
                status=status,
                observations=old_state.observations,
                provenance=old_state.provenance,
                distinction_ids=old_state.distinction_ids,
                measurement_ids=old_state.measurement_ids,
                boundaries=old_state.boundaries,
                residuals=old_state.residuals,
                beliefs=old_state.beliefs,
                parent_state_ids=(old_state.state_id,),
                active=is_active,
            )

            self.states[state.state_id] = state
            resulting.append(state)

            if not is_active:
                inactive.append(state.state_id)

        transition = Transition(
            transition_id=_id("transition"),
            prior_state_ids=generated,
            resulting_state_ids=tuple(
                state.state_id for state in resulting
            ),
            operation=operation,
            transformation=transformation,
            evaluator=evaluator,
            generation_id=generation_id,
            resource_allocation_id=resource_allocation_id,
            activation_ids=represented_activations,
            tests=tuple(tests),
            inactive_state_ids=tuple(inactive),
            acceptance_basis_ids=represented_acceptance,
            inquiry_basis_ids=represented_inquiry,
            support_claim_ids=represented_support_claims,
            residuals=tuple(residuals),
            resource_cost=resource_cost or {},
            stopping_conditions=tuple(stopping_conditions),
            reopening_conditions=tuple(reopening_conditions),
        )

        self.transitions[
            transition.transition_id
        ] = transition

        self._append(
            "transition",
            {
                **asdict(transition),
                "resulting_states": [
                    asdict(state)
                    for state in resulting
                ],
            },
        )

        return transition

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
        """
        Compatibility operation.

        This preserves the earlier convenience API while explicitly
        recording that candidate generation and allocation were supplied
        externally and are not represented by this compatibility path.
        """

        parents = self._require_states(prior_state_ids)

        if not parents:
            raise ValueError(
                "a transition requires at least one prior state"
            )

        candidate_data = list(candidates)
        selected_indexes_tuple = tuple(selected_indexes)

        if not candidate_data:
            raise ValueError(
                "at least one candidate is required"
            )

        if not selected_indexes_tuple:
            raise ValueError(
                "at least one selected index is required"
            )

        selected_index_set = set(selected_indexes_tuple)

        if not selected_index_set.issubset(
            range(len(candidate_data))
        ):
            raise ValueError(
                "selected indexes must identify candidates"
            )

        external_generator = Generator(
            generator_id=_id("generator"),
            declared_account=(
                "Candidates supplied directly to transition "
                "through compatibility API."
            ),
            operations=("external candidate provision",),
            source_state_ids=parents,
            constraints=(
                "candidate-generation process not represented",
                "allocation process not represented",
            ),
            residuals=(
                "generation genealogy incomplete",
                "allocation genealogy incomplete",
            ),
        )

        generation = self.generate(
            source_state_ids=parents,
            candidates=candidate_data,
            generator=external_generator,
            operation="external candidate provision",
            known_exclusions=(
                "candidate-generation process not represented",
                "allocation process not represented",
            ),
            residuals=(
                "compatibility path preserves generation "
                "and allocation as explicit unresolved boundaries",
            ),
        )

        selected_state_ids = tuple(
            generation.generated_state_ids[index]
            for index in selected_indexes_tuple
        )

        return self.transition_generated(
            generation_id=generation.generation_id,
            operation=operation,
            transformation=transformation,
            evaluator=evaluator,
            selected_state_ids=selected_state_ids,
            tests=tests,
            residuals=(
                *tuple(residuals),
                "allocation not represented by compatibility path",
            ),
            resource_cost=resource_cost,
            stopping_conditions=stopping_conditions,
            reopening_conditions=reopening_conditions,
        )

    def compare(
        self,
        *,
        conclusion_state_ids: Iterable[str],
        support_claim_ids: Iterable[str],
        basis: Iterable[str],
        distinction_ids: Iterable[str] = (),
        measurement_ids: Iterable[str] = (),
        criteria: Iterable[str] = (),
        methods: Iterable[str] = (),
        conditions: Iterable[str] = (),
        evaluator_id: str | None = None,
        best_supported_state_ids: Iterable[str] = (),
        unranked_state_ids: Iterable[str] = (),
        known_exclusions: Iterable[str] = (),
        unresolved_relations: Iterable[str] = (),
        unrepresented_alternatives_possible: bool = True,
    ) -> Comparison:
        conclusion_ids = self._require_states(
            conclusion_state_ids
        )
        represented_support_claims = (
            self._require_support_claims(
                support_claim_ids
            )
        )

        represented_conclusions = set(conclusion_ids)

        for support_claim_id in represented_support_claims:
            support_claim = self.support_claims[
                support_claim_id
            ]
            if (
                support_claim.conclusion_state_id
                not in represented_conclusions
            ):
                raise ValueError(
                    "support claim refers to a conclusion "
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
            support_claim_ids=represented_support_claims,
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
            unranked_state_ids=tuple(
                unranked_state_ids
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

    def recontextualize(
        self,
        *,
        prior_state_ids: Iterable[str],
        distinction_ids: Iterable[str],
        relation: str,
        resulting_state: dict[str, Any] | None = None,
        generator_id: str | None = None,
        basis_ids: Iterable[str] = (),
        support_claim_ids: Iterable[str] = (),
        conditions: Iterable[str] = (),
        provenance: Iterable[str] = (),
        residuals: Iterable[str] = (),
    ) -> Recontextualization:
        prior_ids = self._require_states(prior_state_ids)
        represented_distinctions = self._require_distinctions(
            distinction_ids
        )
        represented_bases = self._require_bases(basis_ids)
        represented_support_claims = (
            self._require_support_claims(
                support_claim_ids
            )
        )

        if generator_id is not None:
            generator_exists = any(
                generation.generator.generator_id
                == generator_id
                for generation in self.generations.values()
            )
            if not generator_exists:
                raise KeyError(
                    f"unknown generator: {generator_id}"
                )

        resulting_state_id: str | None = None

        if resulting_state is not None:
            belief_ids = tuple(
                resulting_state.get("beliefs", ())
            )
            for belief_id in belief_ids:
                if belief_id not in self.beliefs:
                    raise KeyError(
                        f"unknown belief: {belief_id}"
                    )

            result_distinctions = (
                self._require_distinctions(
                    resulting_state.get(
                        "distinction_ids",
                        represented_distinctions,
                    )
                )
            )
            result_measurements = (
                self._require_measurements(
                    resulting_state.get(
                        "measurement_ids",
                        (),
                    )
                )
            )

            state = InquiryState(
                state_id=_id("state"),
                object=resulting_state["object"],
                representation=resulting_state[
                    "representation"
                ],
                status=resulting_state.get(
                    "status",
                    "untested",
                ),
                observations=tuple(
                    resulting_state.get(
                        "observations",
                        (),
                    )
                ),
                provenance=tuple(
                    resulting_state.get(
                        "provenance",
                        (),
                    )
                ),
                distinction_ids=result_distinctions,
                measurement_ids=result_measurements,
                boundaries=tuple(
                    resulting_state.get(
                        "boundaries",
                        (),
                    )
                ),
                residuals=tuple(
                    resulting_state.get(
                        "residuals",
                        (),
                    )
                ),
                beliefs=belief_ids,
                parent_state_ids=prior_ids,
                active=resulting_state.get(
                    "active",
                    True,
                ),
            )

            self.states[state.state_id] = state
            resulting_state_id = state.state_id

        event = Recontextualization(
            recontextualization_id=_id(
                "recontextualization"
            ),
            prior_state_ids=prior_ids,
            distinction_ids=represented_distinctions,
            relation=relation,
            resulting_state_id=resulting_state_id,
            generator_id=generator_id,
            basis_ids=represented_bases,
            support_claim_ids=represented_support_claims,
            conditions=tuple(conditions),
            provenance=tuple(provenance),
            residuals=tuple(residuals),
        )

        self.recontextualizations[
            event.recontextualization_id
        ] = event

        payload = asdict(event)

        if resulting_state_id is not None:
            payload["resulting_state"] = asdict(
                self.states[resulting_state_id]
            )

        self._append(
            "recontextualization",
            payload,
        )
        return event

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
        basis_ids: Iterable[str] = (),
        acceptance_basis_ids: Iterable[str] = (),
        inquiry_basis_ids: Iterable[str] = (),
        inquiry_operation_ids: Iterable[str] = (),
        allocation_basis_ids: Iterable[str] = (),
        inquiry_priority_ids: Iterable[str] = (),
        resource_allocation_ids: Iterable[str] = (),
        activation_ids: Iterable[str] = (),
        support_ids: Iterable[str] = (),
        support_claim_ids: Iterable[str] = (),
        comparison_ids: Iterable[str] = (),
        generation_ids: Iterable[str] = (),
        recontextualization_ids: Iterable[str] = (),
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
        represented_bases = self._require_bases(basis_ids)
        represented_acceptance = (
            self._require_acceptance_bases(
                acceptance_basis_ids
            )
        )
        represented_inquiry = self._require_inquiry_bases(
            inquiry_basis_ids
        )
        represented_inquiry_operations = (
            self._require_inquiry_operations(
                inquiry_operation_ids
            )
        )
        represented_allocation_bases = (
            self._require_allocation_bases(
                allocation_basis_ids
            )
        )
        represented_priorities = (
            self._require_inquiry_priorities(
                inquiry_priority_ids
            )
        )
        represented_allocations = (
            self._require_resource_allocations(
                resource_allocation_ids
            )
        )
        represented_activations = self._require_activations(
            activation_ids
        )
        represented_support = (
            self._require_support_relations(
                support_ids
            )
        )
        represented_support_claims = (
            self._require_support_claims(
                support_claim_ids
            )
        )

        represented_comparisons = tuple(comparison_ids)
        for comparison_id in represented_comparisons:
            if comparison_id not in self.comparisons:
                raise KeyError(
                    f"unknown comparison: {comparison_id}"
                )

        represented_generations = tuple(generation_ids)
        for generation_id in represented_generations:
            if generation_id not in self.generations:
                raise KeyError(
                    f"unknown generation: {generation_id}"
                )

        represented_recontextualizations = tuple(
            recontextualization_ids
        )
        for recontextualization_id in (
            represented_recontextualizations
        ):
            if (
                recontextualization_id
                not in self.recontextualizations
            ):
                raise KeyError(
                    "unknown recontextualization: "
                    f"{recontextualization_id}"
                )

        payload = {
            "audit_id": _id("audit"),
            "target_transition_id": target_transition_id,
            "auditor": asdict(auditor),
            "distinction_ids": represented_distinctions,
            "measurement_ids": represented_measurements,
            "basis_ids": represented_bases,
            "acceptance_basis_ids": represented_acceptance,
            "inquiry_basis_ids": represented_inquiry,
            "inquiry_operation_ids": (
                represented_inquiry_operations
            ),
            "allocation_basis_ids": (
                represented_allocation_bases
            ),
            "inquiry_priority_ids": represented_priorities,
            "resource_allocation_ids": represented_allocations,
            "activation_ids": represented_activations,
            "support_ids": represented_support,
            "support_claim_ids": represented_support_claims,
            "comparison_ids": represented_comparisons,
            "generation_ids": represented_generations,
            "recontextualization_ids": (
                represented_recontextualizations
            ),
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
    basis_ids: Iterable[str] = (),
    support_relations: Iterable[str] = (),
    support_claims: Iterable[str] = (),
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
        basis_ids=tuple(basis_ids),
        support_relations=tuple(support_relations),
        support_claims=tuple(support_claims),
        comparison_basis=tuple(comparison_basis),
        values=tuple(values),
        conditions=tuple(conditions),
        exclusions=tuple(exclusions),
    )


def generator(
    declared_account: str,
    *,
    operations: Iterable[str],
    distinction_ids: Iterable[str] = (),
    source_state_ids: Iterable[str] = (),
    retrieval: Iterable[str] = (),
    tools: Iterable[str] = (),
    constraints: Iterable[str] = (),
    allocator_feedback: Iterable[str] = (),
    evaluator_feedback: Iterable[str] = (),
    conditions: Iterable[str] = (),
    exclusions: Iterable[str] = (),
    resource_limits: Iterable[str] = (),
    residuals: Iterable[str] = (),
) -> Generator:
    return Generator(
        generator_id=_id("generator"),
        declared_account=declared_account,
        operations=tuple(operations),
        distinction_ids=tuple(distinction_ids),
        source_state_ids=tuple(source_state_ids),
        retrieval=tuple(retrieval),
        tools=tuple(tools),
        constraints=tuple(constraints),
        allocator_feedback=tuple(allocator_feedback),
        evaluator_feedback=tuple(evaluator_feedback),
        conditions=tuple(conditions),
        exclusions=tuple(exclusions),
        resource_limits=tuple(resource_limits),
        residuals=tuple(residuals),
    )


def allocator(
    declared_account: str,
    *,
    criteria: Iterable[str],
    allocation_basis_ids: Iterable[str] = (),
    resource_conditions: Iterable[str] = (),
    constraints: Iterable[str] = (),
    generator_feedback: Iterable[str] = (),
    evaluator_feedback: Iterable[str] = (),
    conditions: Iterable[str] = (),
    exclusions: Iterable[str] = (),
    residuals: Iterable[str] = (),
) -> Allocator:
    return Allocator(
        allocator_id=_id("allocator"),
        declared_account=declared_account,
        criteria=tuple(criteria),
        allocation_basis_ids=tuple(allocation_basis_ids),
        resource_conditions=tuple(resource_conditions),
        constraints=tuple(constraints),
        generator_feedback=tuple(generator_feedback),
        evaluator_feedback=tuple(evaluator_feedback),
        conditions=tuple(conditions),
        exclusions=tuple(exclusions),
        residuals=tuple(residuals),
    )
