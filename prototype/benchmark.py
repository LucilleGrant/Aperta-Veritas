"""Answer-key-separated benchmark components for Aperta Veritas."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from typing import Any

from experiment import (
    AllocationRecord,
    Candidate,
    EvaluationRecord,
    ExperimentResult,
    ExperimentTask,
    FixedEvaluationArchitecture,
    FixedOrderAllocator,
    FixedScoreEvaluator,
    OpenInquiryRevision,
    OpenRecursiveInquiryArchitecture,
    ObservationRecord,
    ResourceBudget,
    RevisableEvaluationArchitecture,
    RevisableScoreEvaluator,
    StaticGenerator,
)


@dataclass(frozen=True)
class VerificationKey:
    """A held-out rubric unavailable to the experimental architectures."""

    case_id: str
    required_scopes: tuple[str, ...]
    required_relation_terms: tuple[str, ...]


@dataclass(frozen=True)
class VerificationResult:
    """Independent comparison of an architecture output with a hidden key."""

    architecture_id: str
    case_id: str
    recovered: bool
    matching_candidate_ids: tuple[str, ...]
    account: str


class ContrastiveInquiryController:
    """Generate a distinction from public observations with different scopes."""

    controller_id = "contrastive_inquiry_controller"

    def examine(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
        allocation: AllocationRecord,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> OpenInquiryRevision | None:
        del evaluations
        scopes = tuple(dict.fromkeys(
            observation.scope.strip().lower()
            for observation in task.observations
        ))
        if len(scopes) < 2:
            return None

        left, right = scopes[:2]
        distinction = f"{left} versus {right}"
        representation = (
            f"Treat {left} and {right} as distinct represented scopes, "
            "then examine the relation between them."
        )
        digest = sha256(
            representation.encode("utf-8")
        ).hexdigest()[:12]
        added = Candidate(
            candidate_id=f"contrast_{digest}",
            representation=representation,
            provenance=tuple(
                observation.observation_id
                for observation in task.observations
                if observation.scope.strip().lower() in (left, right)
            ),
        )
        scores = {
            candidate.candidate_id: 0.2
            for candidate in candidates
        }
        scores[added.candidate_id] = 0.9

        return OpenInquiryRevision(
            revision_id=f"contrast_revision_{digest}",
            added_candidates=(added,),
            reactivate_candidate_ids=(
                allocation.inactive_candidate_ids
            ),
            distinctions=(distinction,),
            generation_account=(
                "Distinct public observation scopes generated a contrastive "
                "candidate without access to the verification key."
            ),
            allocation_basis=(
                "activate retained and newly generated scope candidates",
            ),
            evaluation_criteria=(
                "coverage of relations among public observation scopes",
            ),
            evaluation_scores=scores,
            reopening_conditions=(
                "a new observation changes or relates the represented scopes",
            ),
        )


class PairwiseContrastiveInquiryController:
    """Generate every represented pairwise scope contrast within budget."""

    controller_id = "pairwise_contrastive_inquiry_controller"

    def examine(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
        allocation: AllocationRecord,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> OpenInquiryRevision | None:
        del evaluations
        observations_by_scope: dict[str, list[ObservationRecord]] = {}
        for observation in task.observations:
            scope = observation.scope.strip().lower()
            observations_by_scope.setdefault(scope, []).append(observation)
        scopes = tuple(sorted(observations_by_scope))
        if len(scopes) < 2:
            return None

        added: list[Candidate] = []
        distinctions: list[str] = []
        for left, right in combinations(scopes, 2):
            distinction = f"{left} versus {right}"
            representation = (
                f"Treat {left} and {right} as distinct represented scopes, "
                "then examine the relation between them."
            )
            digest = sha256(
                representation.encode("utf-8")
            ).hexdigest()[:12]
            provenance = tuple(
                observation.observation_id
                for scope in (left, right)
                for observation in observations_by_scope[scope]
            )
            added.append(Candidate(
                candidate_id=f"pairwise_contrast_{digest}",
                representation=representation,
                provenance=provenance,
            ))
            distinctions.append(distinction)

        scores = {
            candidate.candidate_id: 0.2
            for candidate in candidates
        }
        scores.update(
            (candidate.candidate_id, 0.9)
            for candidate in added
        )
        digest = sha256(
            "|".join(candidate.candidate_id for candidate in added).encode(
                "utf-8"
            )
        ).hexdigest()[:12]
        return OpenInquiryRevision(
            revision_id=f"pairwise_revision_{digest}",
            added_candidates=tuple(added),
            reactivate_candidate_ids=allocation.inactive_candidate_ids,
            distinctions=tuple(distinctions),
            generation_account=(
                "Every pair of distinct public observation scopes generated "
                "a contrastive candidate without access to verification keys."
            ),
            allocation_basis=(
                "activate retained and pairwise contrast candidates",
            ),
            evaluation_criteria=(
                "coverage of relations among public observation scopes",
            ),
            evaluation_scores=scores,
            reopening_conditions=(
                "a new observation changes or relates represented scopes",
            ),
        )


class HeldOutVerifier:
    """Evaluate candidate text after a run without influencing generation."""

    def verify(
        self,
        result: ExperimentResult,
        key: VerificationKey,
    ) -> VerificationResult:
        matching = tuple(
            candidate.candidate_id
            for candidate in result.candidates
            if self._matches(candidate, key)
        )
        return VerificationResult(
            architecture_id=result.architecture_id,
            case_id=key.case_id,
            recovered=bool(matching),
            matching_candidate_ids=matching,
            account=(
                "At least one generated candidate matched the held-out "
                "scope and relation rubric."
                if matching
                else "No generated candidate matched the held-out rubric."
            ),
        )

    @staticmethod
    def _matches(
        candidate: Candidate,
        key: VerificationKey,
    ) -> bool:
        text = candidate.representation.lower()
        return all(
            scope.lower() in text for scope in key.required_scopes
        ) and all(
            term.lower() in text
            for term in key.required_relation_terms
        )


def run_answer_key_separated_case() -> dict[str, Any]:
    """Run A, B, and C before applying a held-out verification key."""

    task = ExperimentTask(
        task_id="held_out_boundary_development_1",
        initial_representation=(
            "Two observation records concern one reported event. Determine "
            "which candidate representation should remain available."
        ),
        resource_budget=ResourceBudget(
            max_candidates=3,
            max_evaluations=4,
        ),
        stopping_conditions=("development procedure complete",),
        observations=(
            ObservationRecord(
                observation_id="observation_protocol",
                scope="protocol output",
                account="The protocol records the output as heads.",
                relation="reports",
            ),
            ObservationRecord(
                observation_id="observation_physical",
                scope="physical state",
                account="The physical configuration was not measured.",
                relation="unmeasured",
            ),
        ),
    )
    candidates = (
        Candidate(
            "candidate_accept",
            "Accept the recorded output as the event conclusion.",
        ),
        Candidate(
            "candidate_reject",
            "Reject the recorded output as the event conclusion.",
        ),
    )
    generator = StaticGenerator("matched_generator", candidates)
    allocator = FixedOrderAllocator(
        "matched_allocator",
        ("supplied order", "matched resource ceiling"),
        max_active=1,
    )
    fixed = FixedScoreEvaluator(
        "fixed_evaluator",
        ("fit under initial representation",),
        {"candidate_accept": 0.4, "candidate_reject": 0.3},
    )
    architectures = (
        FixedEvaluationArchitecture(generator, allocator, fixed),
        RevisableEvaluationArchitecture(
            generator,
            allocator,
            RevisableScoreEvaluator(
                evaluator_id="revisable_evaluator",
                initial_criteria=("fit under initial representation",),
                initial_scores={"candidate_accept": 0.4},
                revised_criteria=("internal report consistency",),
                revised_scores={"candidate_accept": 0.6},
                revision_trigger_score=0.5,
            ),
        ),
        OpenRecursiveInquiryArchitecture(
            generator,
            allocator,
            fixed,
            ContrastiveInquiryController(),
        ),
    )

    results = tuple(architecture.run(task) for architecture in architectures)

    key = VerificationKey(
        case_id=task.task_id,
        required_scopes=("protocol output", "physical state"),
        required_relation_terms=("distinct", "relation"),
    )
    verifier = HeldOutVerifier()
    verified = tuple(verifier.verify(result, key) for result in results)

    return {
        "status": "answer-key-separated engineering check",
        "case_id": task.task_id,
        "architecture_inputs_contain_verification_key": False,
        "results": {
            result.architecture_id: {
                "recovered": verification.recovered,
                "matching_candidate_ids": list(
                    verification.matching_candidate_ids
                ),
                "generated_candidate_ids": list(
                    result.generation.candidate_ids
                ),
                "evaluations_performed": result.evaluations_performed,
            }
            for result, verification in zip(results, verified)
        },
    }


@dataclass(frozen=True)
class BenchmarkCase:
    """One public task paired with a held-out verifier key."""

    task: ExperimentTask
    candidates: tuple[Candidate, ...]
    key: VerificationKey
    expected_recovery: bool


def _benchmark_case(
    case_id: str,
    scopes: tuple[str, ...],
    required_scopes: tuple[str, ...],
    *,
    required_relation_terms: tuple[str, ...] = ("distinct", "relation"),
    expected_recovery: bool = True,
) -> BenchmarkCase:
    observations = tuple(
        ObservationRecord(
            observation_id=f"{case_id}_observation_{index}",
            scope=scope,
            account=f"Public observation for {scope}.",
            relation="reports",
        )
        for index, scope in enumerate(scopes, start=1)
    )
    return BenchmarkCase(
        task=ExperimentTask(
            task_id=case_id,
            initial_representation=(
                "Determine which represented candidate should remain "
                "available under the public observations."
            ),
            resource_budget=ResourceBudget(
                max_candidates=8,
                max_evaluations=12,
            ),
            stopping_conditions=("benchmark procedure complete",),
            observations=observations,
        ),
        candidates=(
            Candidate(
                f"{case_id}_accept",
                "Accept the initial report without adding a distinction.",
            ),
            Candidate(
                f"{case_id}_reject",
                "Reject the initial report without adding a distinction.",
            ),
        ),
        key=VerificationKey(
            case_id=case_id,
            required_scopes=required_scopes,
            required_relation_terms=required_relation_terms,
        ),
        expected_recovery=expected_recovery,
    )


def benchmark_cases() -> tuple[BenchmarkCase, ...]:
    """Return positive, permuted, decoy, and negative-control cases."""

    return (
        _benchmark_case(
            "positive_protocol_physical",
            ("protocol output", "physical state"),
            ("protocol output", "physical state"),
        ),
        _benchmark_case(
            "positive_sensor_environment",
            ("sensor report", "environmental state"),
            ("sensor report", "environmental state"),
        ),
        _benchmark_case(
            "permuted_physical_protocol",
            ("physical state", "protocol output"),
            ("protocol output", "physical state"),
        ),
        _benchmark_case(
            "decoy_with_relevant_pair_last",
            ("operator note", "protocol output", "physical state"),
            ("protocol output", "physical state"),
        ),
        _benchmark_case(
            "negative_single_scope",
            ("protocol output",),
            ("protocol output", "physical state"),
            expected_recovery=False,
        ),
        _benchmark_case(
            "negative_absent_relation",
            ("protocol output", "physical state", "operator note"),
            ("protocol output", "physical state"),
            required_relation_terms=("causal", "relation"),
            expected_recovery=False,
        ),
    )


def _architectures_for_case(
    case: BenchmarkCase,
) -> tuple[
    FixedEvaluationArchitecture,
    RevisableEvaluationArchitecture,
    OpenRecursiveInquiryArchitecture,
]:
    generator = StaticGenerator("matched_generator", case.candidates)
    allocator = FixedOrderAllocator(
        "matched_allocator",
        ("supplied order", "matched resource ceiling"),
        max_active=1,
    )
    initial_scores = {
        case.candidates[0].candidate_id: 0.4,
        case.candidates[1].candidate_id: 0.3,
    }
    fixed = FixedScoreEvaluator(
        "fixed_evaluator",
        ("fit under initial representation",),
        initial_scores,
    )
    return (
        FixedEvaluationArchitecture(generator, allocator, fixed),
        RevisableEvaluationArchitecture(
            generator,
            allocator,
            RevisableScoreEvaluator(
                evaluator_id="revisable_evaluator",
                initial_criteria=("fit under initial representation",),
                initial_scores={case.candidates[0].candidate_id: 0.4},
                revised_criteria=("internal report consistency",),
                revised_scores={case.candidates[0].candidate_id: 0.6},
                revision_trigger_score=0.5,
            ),
        ),
        OpenRecursiveInquiryArchitecture(
            generator,
            allocator,
            fixed,
            PairwiseContrastiveInquiryController(),
        ),
    )


def run_benchmark_suite() -> dict[str, Any]:
    """Run the preregistered engineering suite and aggregate outcomes."""

    verifier = HeldOutVerifier()
    case_reports: list[dict[str, Any]] = []
    aggregates: dict[str, dict[str, int]] = {}
    for case in benchmark_cases():
        architecture_reports: dict[str, dict[str, Any]] = {}
        for architecture in _architectures_for_case(case):
            result = architecture.run(case.task)
            verification = verifier.verify(result, case.key)
            architecture_reports[result.architecture_id] = {
                "recovered": verification.recovered,
                "matching_candidate_ids": list(
                    verification.matching_candidate_ids
                ),
                "candidates_generated": result.candidates_generated,
                "evaluations_performed": result.evaluations_performed,
            }
            totals = aggregates.setdefault(
                result.architecture_id,
                {
                    "positive_cases": 0,
                    "positive_recoveries": 0,
                    "negative_cases": 0,
                    "false_positives": 0,
                    "candidates_generated": 0,
                    "evaluations_performed": 0,
                },
            )
            if case.expected_recovery:
                totals["positive_cases"] += 1
                totals["positive_recoveries"] += int(
                    verification.recovered
                )
            else:
                totals["negative_cases"] += 1
                totals["false_positives"] += int(
                    verification.recovered
                )
            totals["candidates_generated"] += result.candidates_generated
            totals["evaluations_performed"] += result.evaluations_performed
        case_reports.append({
            "case_id": case.task.task_id,
            "expected_recovery": case.expected_recovery,
            "scope_order": [
                observation.scope for observation in case.task.observations
            ],
            "results": architecture_reports,
        })

    aggregate_report: dict[str, dict[str, float | int]] = {}
    for architecture_id, totals in aggregates.items():
        positive_cases = totals["positive_cases"]
        negative_cases = totals["negative_cases"]
        aggregate_report[architecture_id] = {
            **totals,
            "recovery_rate": (
                totals["positive_recoveries"] / positive_cases
            ),
            "false_positive_rate": (
                totals["false_positives"] / negative_cases
            ),
        }

    return {
        "status": "multi-case answer-key-separated engineering check",
        "architecture_inputs_contain_verification_keys": False,
        "case_count": len(case_reports),
        "cases": case_reports,
        "aggregates": aggregate_report,
        "evidence_boundary": (
            "Engineering behavior under constructed cases, not research "
            "evidence of general recursive improvement."
        ),
    }
