"""Answer-key-separated benchmark components for Aperta Veritas."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
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
