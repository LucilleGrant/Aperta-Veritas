"""Shared experiment interface and fixed-evaluation reference architecture."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Protocol


@dataclass(frozen=True)
class ObservationRecord:
    """A public benchmark observation available to every architecture."""

    observation_id: str
    scope: str
    account: str
    relation: str = ""

    def __post_init__(self) -> None:
        if not self.observation_id.strip():
            raise ValueError("observation_id must be explicit")
        if not self.scope.strip():
            raise ValueError("observation scope must be explicit")
        if not self.account.strip():
            raise ValueError("observation account must be explicit")


@dataclass(frozen=True)
class ResourceBudget:
    """Declared limits shared by a matched experimental run."""

    max_candidates: int
    max_evaluations: int

    def __post_init__(self) -> None:
        if self.max_candidates < 1:
            raise ValueError("max_candidates must be positive")
        if self.max_evaluations < 1:
            raise ValueError("max_evaluations must be positive")


@dataclass(frozen=True)
class ExperimentTask:
    """A task representation supplied equally to each architecture."""

    task_id: str
    initial_representation: str
    resource_budget: ResourceBudget
    stopping_conditions: tuple[str, ...]
    observations: tuple[ObservationRecord, ...] = ()

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id must be explicit")
        if not self.initial_representation.strip():
            raise ValueError("initial_representation must be explicit")
        if not self.stopping_conditions:
            raise ValueError("stopping_conditions must be represented")


@dataclass(frozen=True)
class Candidate:
    """A represented candidate produced by a declared generator."""

    candidate_id: str
    representation: str
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate_id must be explicit")
        if not self.representation.strip():
            raise ValueError("candidate representation must be explicit")


@dataclass(frozen=True)
class GenerationRecord:
    """The candidate set made available by one generator invocation."""

    generator_id: str
    candidate_ids: tuple[str, ...]
    declared_non_exhaustive: bool = True


@dataclass(frozen=True)
class AllocationRecord:
    """A fixed allocation decision over represented candidates."""

    allocator_id: str
    basis: tuple[str, ...]
    active_candidate_ids: tuple[str, ...]
    inactive_candidate_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.allocator_id.strip():
            raise ValueError("allocator_id must be explicit")
        if not self.basis:
            raise ValueError("allocation basis must be explicit")


@dataclass(frozen=True)
class EvaluationRecord:
    """An evaluator account for one active candidate."""

    evaluator_id: str
    candidate_id: str
    criteria: tuple[str, ...]
    score: float
    account: str

    def __post_init__(self) -> None:
        if not self.evaluator_id.strip():
            raise ValueError("evaluator_id must be explicit")
        if not self.criteria:
            raise ValueError("evaluation criteria must be explicit")
        if not self.account.strip():
            raise ValueError("evaluation account must be explicit")


@dataclass(frozen=True)
class ExperimentResult:
    """Complete result of one architecture run under a declared budget."""

    architecture_id: str
    task_id: str
    generation: GenerationRecord
    allocation: AllocationRecord
    evaluations: tuple[EvaluationRecord, ...]
    selected_candidate_ids: tuple[str, ...]
    candidates: tuple[Candidate, ...]
    candidates_generated: int
    evaluations_performed: int
    stop_reason: str

    def __post_init__(self) -> None:
        if not self.stop_reason.strip():
            raise ValueError("stop_reason must be explicit")


@dataclass(frozen=True)
class EvaluationRevision:
    """A represented change to an evaluator during one run."""

    revision_id: str
    evaluator_id: str
    prior_criteria: tuple[str, ...]
    revised_criteria: tuple[str, ...]
    trigger: str
    account: str

    def __post_init__(self) -> None:
        if not self.revision_id.strip():
            raise ValueError("revision_id must be explicit")
        if not self.prior_criteria or not self.revised_criteria:
            raise ValueError("prior and revised criteria must be explicit")
        if not self.trigger.strip():
            raise ValueError("revision trigger must be explicit")
        if not self.account.strip():
            raise ValueError("revision account must be explicit")


@dataclass(frozen=True)
class RevisableExperimentResult(ExperimentResult):
    """Architecture B result retaining initial and revised evaluation states."""

    initial_evaluations: tuple[EvaluationRecord, ...] = ()
    evaluator_revisions: tuple[EvaluationRevision, ...] = ()


class CandidateGenerator(Protocol):
    generator_id: str

    def generate(self, task: ExperimentTask) -> tuple[Candidate, ...]: ...


class CandidateAllocator(Protocol):
    allocator_id: str

    def allocate(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
    ) -> AllocationRecord: ...


class CandidateEvaluator(Protocol):
    evaluator_id: str

    def evaluate(
        self,
        task: ExperimentTask,
        candidate: Candidate,
    ) -> EvaluationRecord: ...


class RevisableCandidateEvaluator(CandidateEvaluator, Protocol):
    def should_revise(
        self,
        task: ExperimentTask,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> bool: ...

    def revision(self) -> EvaluationRevision: ...

    def evaluate_revised(
        self,
        task: ExperimentTask,
        candidate: Candidate,
    ) -> EvaluationRecord: ...


class ExperimentArchitecture(Protocol):
    architecture_id: str

    def run(self, task: ExperimentTask) -> ExperimentResult: ...


@dataclass(frozen=True)
class StaticGenerator:
    """A generator whose candidate sequence cannot change during a run."""

    generator_id: str
    candidates: tuple[Candidate, ...]

    def generate(self, task: ExperimentTask) -> tuple[Candidate, ...]:
        del task
        return self.candidates


@dataclass(frozen=True)
class FixedOrderAllocator:
    """Activates candidates in supplied order under the evaluation budget."""

    allocator_id: str
    basis: tuple[str, ...]
    max_active: int | None = None

    def allocate(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
    ) -> AllocationRecord:
        limit = task.resource_budget.max_evaluations
        if self.max_active is not None:
            if self.max_active < 0:
                raise ValueError("max_active cannot be negative")
            limit = min(limit, self.max_active)
        active = candidates[:limit]
        inactive = candidates[limit:]
        return AllocationRecord(
            allocator_id=self.allocator_id,
            basis=self.basis,
            active_candidate_ids=tuple(
                candidate.candidate_id for candidate in active
            ),
            inactive_candidate_ids=tuple(
                candidate.candidate_id for candidate in inactive
            ),
        )


@dataclass(frozen=True)
class FixedScoreEvaluator:
    """Applies one immutable score table and comparison criterion."""

    evaluator_id: str
    criteria: tuple[str, ...]
    scores: Mapping[str, float]

    def evaluate(
        self,
        task: ExperimentTask,
        candidate: Candidate,
    ) -> EvaluationRecord:
        del task
        if candidate.candidate_id not in self.scores:
            raise KeyError(
                f"no fixed score for candidate {candidate.candidate_id}"
            )
        score = float(self.scores[candidate.candidate_id])
        return EvaluationRecord(
            evaluator_id=self.evaluator_id,
            candidate_id=candidate.candidate_id,
            criteria=self.criteria,
            score=score,
            account=(
                f"Candidate {candidate.candidate_id} received fixed score "
                f"{score} under evaluator {self.evaluator_id}."
            ),
        )


@dataclass(frozen=True)
class RevisableScoreEvaluator:
    """A score evaluator with one declared, condition-triggered revision."""

    evaluator_id: str
    initial_criteria: tuple[str, ...]
    initial_scores: Mapping[str, float]
    revised_criteria: tuple[str, ...]
    revised_scores: Mapping[str, float]
    revision_trigger_score: float
    revision_id: str = "revision_1"

    def evaluate(
        self,
        task: ExperimentTask,
        candidate: Candidate,
    ) -> EvaluationRecord:
        del task
        return self._evaluation(
            candidate,
            self.initial_criteria,
            self.initial_scores,
            "initial",
        )

    def should_revise(
        self,
        task: ExperimentTask,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> bool:
        del task
        return bool(evaluations) and max(
            evaluation.score for evaluation in evaluations
        ) <= self.revision_trigger_score

    def revision(self) -> EvaluationRevision:
        return EvaluationRevision(
            revision_id=self.revision_id,
            evaluator_id=self.evaluator_id,
            prior_criteria=self.initial_criteria,
            revised_criteria=self.revised_criteria,
            trigger=(
                "maximum initial score less than or equal to "
                f"{self.revision_trigger_score}"
            ),
            account=(
                f"Evaluator {self.evaluator_id} replaced its initial "
                "criteria and score table under the declared trigger."
            ),
        )

    def evaluate_revised(
        self,
        task: ExperimentTask,
        candidate: Candidate,
    ) -> EvaluationRecord:
        del task
        return self._evaluation(
            candidate,
            self.revised_criteria,
            self.revised_scores,
            "revised",
        )

    def _evaluation(
        self,
        candidate: Candidate,
        criteria: tuple[str, ...],
        scores: Mapping[str, float],
        phase: str,
    ) -> EvaluationRecord:
        if candidate.candidate_id not in scores:
            raise KeyError(
                f"no {phase} score for candidate {candidate.candidate_id}"
            )
        score = float(scores[candidate.candidate_id])
        return EvaluationRecord(
            evaluator_id=self.evaluator_id,
            candidate_id=candidate.candidate_id,
            criteria=criteria,
            score=score,
            account=(
                f"Candidate {candidate.candidate_id} received {phase} "
                f"score {score} under evaluator {self.evaluator_id}."
            ),
        )


@dataclass(frozen=True)
class FixedEvaluationArchitecture:
    """Architecture A from EXPERIMENT_SPEC.md."""

    generator: CandidateGenerator
    allocator: CandidateAllocator
    evaluator: CandidateEvaluator
    architecture_id: str = "architecture_a_fixed_evaluation"

    def run(self, task: ExperimentTask) -> ExperimentResult:
        generated = self.generator.generate(task)
        candidate_limit = task.resource_budget.max_candidates
        candidates = generated[:candidate_limit]
        self._require_unique_candidate_ids(candidates)

        generation = GenerationRecord(
            generator_id=self.generator.generator_id,
            candidate_ids=tuple(
                candidate.candidate_id for candidate in candidates
            ),
            declared_non_exhaustive=True,
        )

        allocation = self.allocator.allocate(task, candidates)
        candidate_by_id = {
            candidate.candidate_id: candidate for candidate in candidates
        }
        represented_ids = set(candidate_by_id)
        allocated_ids = (
            allocation.active_candidate_ids
            + allocation.inactive_candidate_ids
        )

        if len(set(allocated_ids)) != len(allocated_ids):
            raise ValueError("allocation contains duplicate candidate ids")
        if set(allocated_ids) != represented_ids:
            raise ValueError(
                "allocation must partition the represented candidate set"
            )
        if (
            len(allocation.active_candidate_ids)
            > task.resource_budget.max_evaluations
        ):
            raise ValueError("allocation exceeds evaluation budget")

        evaluations = tuple(
            self.evaluator.evaluate(task, candidate_by_id[candidate_id])
            for candidate_id in allocation.active_candidate_ids
        )
        self._validate_evaluations(
            evaluations,
            allocation.active_candidate_ids,
        )

        selected = self._select(evaluations)
        if len(generated) > len(candidates):
            stop_reason = "candidate budget exhausted"
        elif allocation.inactive_candidate_ids:
            stop_reason = "evaluation budget exhausted"
        else:
            stop_reason = task.stopping_conditions[0]

        return ExperimentResult(
            architecture_id=self.architecture_id,
            task_id=task.task_id,
            generation=generation,
            allocation=allocation,
            evaluations=evaluations,
            selected_candidate_ids=selected,
            candidates=candidates,
            candidates_generated=len(candidates),
            evaluations_performed=len(evaluations),
            stop_reason=stop_reason,
        )

    @staticmethod
    def _require_unique_candidate_ids(
        candidates: tuple[Candidate, ...],
    ) -> None:
        ids = tuple(candidate.candidate_id for candidate in candidates)
        if len(set(ids)) != len(ids):
            raise ValueError("candidate ids must be unique")

    def _validate_evaluations(
        self,
        evaluations: tuple[EvaluationRecord, ...],
        active_ids: tuple[str, ...],
    ) -> None:
        evaluated_ids = tuple(
            evaluation.candidate_id for evaluation in evaluations
        )
        if evaluated_ids != active_ids:
            raise ValueError(
                "evaluator must return one record for each active candidate"
            )
        if any(
            evaluation.evaluator_id != self.evaluator.evaluator_id
            for evaluation in evaluations
        ):
            raise ValueError("evaluation record changed evaluator identity")

    @staticmethod
    def _select(
        evaluations: tuple[EvaluationRecord, ...],
    ) -> tuple[str, ...]:
        if not evaluations:
            return ()
        best_score = max(evaluation.score for evaluation in evaluations)
        return tuple(
            evaluation.candidate_id
            for evaluation in evaluations
            if evaluation.score == best_score
        )


@dataclass(frozen=True)
class RevisableEvaluationArchitecture:
    """Architecture B from EXPERIMENT_SPEC.md."""

    generator: CandidateGenerator
    allocator: CandidateAllocator
    evaluator: RevisableCandidateEvaluator
    architecture_id: str = "architecture_b_revisable_evaluation"

    def run(self, task: ExperimentTask) -> RevisableExperimentResult:
        generated = self.generator.generate(task)
        candidates = generated[: task.resource_budget.max_candidates]
        FixedEvaluationArchitecture._require_unique_candidate_ids(
            candidates
        )

        generation = GenerationRecord(
            generator_id=self.generator.generator_id,
            candidate_ids=tuple(
                candidate.candidate_id for candidate in candidates
            ),
            declared_non_exhaustive=True,
        )
        allocation = self.allocator.allocate(task, candidates)
        candidate_by_id = {
            candidate.candidate_id: candidate for candidate in candidates
        }
        self._validate_allocation(
            allocation,
            tuple(candidate_by_id),
            task.resource_budget.max_evaluations,
        )

        initial = tuple(
            self.evaluator.evaluate(task, candidate_by_id[candidate_id])
            for candidate_id in allocation.active_candidate_ids
        )
        self._validate_evaluations(
            initial,
            allocation.active_candidate_ids,
        )

        evaluations = initial
        revisions: tuple[EvaluationRevision, ...] = ()
        remaining = task.resource_budget.max_evaluations - len(initial)
        revision_requested = self.evaluator.should_revise(task, initial)

        if revision_requested and remaining >= len(initial):
            revision = self.evaluator.revision()
            if revision.evaluator_id != self.evaluator.evaluator_id:
                raise ValueError("revision changed evaluator identity")
            revisions = (revision,)
            evaluations = tuple(
                self.evaluator.evaluate_revised(
                    task,
                    candidate_by_id[candidate_id],
                )
                for candidate_id in allocation.active_candidate_ids
            )
            self._validate_evaluations(
                evaluations,
                allocation.active_candidate_ids,
            )

        selected = FixedEvaluationArchitecture._select(evaluations)
        total_evaluations = len(initial) + (
            len(evaluations) if revisions else 0
        )

        if len(generated) > len(candidates):
            stop_reason = "candidate budget exhausted"
        elif revision_requested and not revisions:
            stop_reason = "evaluation budget exhausted before revision"
        elif revisions:
            stop_reason = "revised evaluation procedure complete"
        elif allocation.inactive_candidate_ids:
            stop_reason = "evaluation budget exhausted"
        else:
            stop_reason = task.stopping_conditions[0]

        return RevisableExperimentResult(
            architecture_id=self.architecture_id,
            task_id=task.task_id,
            generation=generation,
            allocation=allocation,
            evaluations=evaluations,
            selected_candidate_ids=selected,
            candidates=candidates,
            candidates_generated=len(candidates),
            evaluations_performed=total_evaluations,
            stop_reason=stop_reason,
            initial_evaluations=initial,
            evaluator_revisions=revisions,
        )

    @staticmethod
    def _validate_allocation(
        allocation: AllocationRecord,
        candidate_ids: tuple[str, ...],
        evaluation_budget: int,
    ) -> None:
        allocated_ids = (
            allocation.active_candidate_ids
            + allocation.inactive_candidate_ids
        )
        if len(set(allocated_ids)) != len(allocated_ids):
            raise ValueError("allocation contains duplicate candidate ids")
        if set(allocated_ids) != set(candidate_ids):
            raise ValueError(
                "allocation must partition the represented candidate set"
            )
        if len(allocation.active_candidate_ids) > evaluation_budget:
            raise ValueError("allocation exceeds evaluation budget")

    def _validate_evaluations(
        self,
        evaluations: tuple[EvaluationRecord, ...],
        active_ids: tuple[str, ...],
    ) -> None:
        if tuple(
            evaluation.candidate_id for evaluation in evaluations
        ) != active_ids:
            raise ValueError(
                "evaluator must return one record for each active candidate"
            )
        if any(
            evaluation.evaluator_id != self.evaluator.evaluator_id
            for evaluation in evaluations
        ):
            raise ValueError("evaluation record changed evaluator identity")


@dataclass(frozen=True)
class GenealogyEvent:
    """A represented change during open recursive inquiry."""

    event_id: str
    kind: str
    account: str
    source_ids: tuple[str, ...] = ()
    resulting_ids: tuple[str, ...] = ()
    conditions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.event_id.strip() or not self.kind.strip():
            raise ValueError("genealogy event identity must be explicit")
        if not self.account.strip():
            raise ValueError("genealogy event account must be explicit")


@dataclass(frozen=True)
class OpenInquiryRevision:
    """One represented recursive change to the experimental process."""

    revision_id: str
    added_candidates: tuple[Candidate, ...]
    reactivate_candidate_ids: tuple[str, ...]
    distinctions: tuple[str, ...]
    generation_account: str
    allocation_basis: tuple[str, ...]
    evaluation_criteria: tuple[str, ...]
    evaluation_scores: Mapping[str, float]
    reopening_conditions: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.revision_id.strip():
            raise ValueError("open inquiry revision id must be explicit")
        if not self.distinctions:
            raise ValueError("open inquiry revision requires a distinction")
        if not self.generation_account.strip():
            raise ValueError("generation revision account must be explicit")
        if not self.allocation_basis:
            raise ValueError("revised allocation basis must be explicit")
        if not self.evaluation_criteria:
            raise ValueError("revised evaluation criteria must be explicit")


class OpenInquiryController(Protocol):
    controller_id: str

    def examine(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
        allocation: AllocationRecord,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> OpenInquiryRevision | None: ...


@dataclass(frozen=True)
class ScriptedOpenInquiry:
    """A deterministic development controller for Architecture C."""

    controller_id: str
    revision: OpenInquiryRevision
    trigger_score: float

    def examine(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
        allocation: AllocationRecord,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> OpenInquiryRevision | None:
        del task, candidates, allocation
        if not evaluations:
            return self.revision
        if max(record.score for record in evaluations) <= self.trigger_score:
            return self.revision
        return None


@dataclass(frozen=True)
class OpenInquiryResult(ExperimentResult):
    """Architecture C result with retained recursive genealogy."""

    initial_generation: GenerationRecord | None = None
    initial_allocation: AllocationRecord | None = None
    initial_evaluations: tuple[EvaluationRecord, ...] = ()
    genealogy: tuple[GenealogyEvent, ...] = ()
    distinctions: tuple[str, ...] = ()
    reopening_conditions: tuple[str, ...] = ()
    recursion_count: int = 0


@dataclass(frozen=True)
class OpenRecursiveInquiryArchitecture:
    """Minimal Architecture C from EXPERIMENT_SPEC.md."""

    generator: CandidateGenerator
    allocator: CandidateAllocator
    evaluator: CandidateEvaluator
    controller: OpenInquiryController
    architecture_id: str = "architecture_c_open_recursive_inquiry"

    def run(self, task: ExperimentTask) -> OpenInquiryResult:
        generated = self.generator.generate(task)
        initial_candidates = generated[
            : task.resource_budget.max_candidates
        ]
        FixedEvaluationArchitecture._require_unique_candidate_ids(
            initial_candidates
        )
        initial_generation = GenerationRecord(
            generator_id=self.generator.generator_id,
            candidate_ids=tuple(
                candidate.candidate_id for candidate in initial_candidates
            ),
            declared_non_exhaustive=True,
        )
        initial_allocation = self.allocator.allocate(
            task,
            initial_candidates,
        )
        RevisableEvaluationArchitecture._validate_allocation(
            initial_allocation,
            initial_generation.candidate_ids,
            task.resource_budget.max_evaluations,
        )
        candidate_by_id = {
            candidate.candidate_id: candidate
            for candidate in initial_candidates
        }
        initial_evaluations = tuple(
            self.evaluator.evaluate(task, candidate_by_id[candidate_id])
            for candidate_id in initial_allocation.active_candidate_ids
        )
        self._validate_evaluation_ids(
            initial_evaluations,
            initial_allocation.active_candidate_ids,
        )

        revision = self.controller.examine(
            task,
            initial_candidates,
            initial_allocation,
            initial_evaluations,
        )
        if revision is None:
            return self._unchanged_result(
                task,
                initial_candidates,
                initial_generation,
                initial_allocation,
                initial_evaluations,
            )

        candidates = self._admit_candidates(
            initial_candidates,
            revision.added_candidates,
            task.resource_budget.max_candidates,
        )
        candidate_by_id = {
            candidate.candidate_id: candidate for candidate in candidates
        }
        active_ids = self._revised_active_ids(
            initial_allocation,
            revision,
            tuple(candidate_by_id),
        )
        remaining_evaluations = (
            task.resource_budget.max_evaluations
            - len(initial_evaluations)
        )
        active_ids = active_ids[:remaining_evaluations]
        active_set = set(active_ids)
        inactive_ids = tuple(
            candidate_id
            for candidate_id in candidate_by_id
            if candidate_id not in active_set
        )
        allocation = AllocationRecord(
            allocator_id=f"{self.controller.controller_id}:revised",
            basis=revision.allocation_basis,
            active_candidate_ids=active_ids,
            inactive_candidate_ids=inactive_ids,
        )
        evaluations = tuple(
            self._evaluate_revised(
                candidate_by_id[candidate_id],
                revision,
            )
            for candidate_id in active_ids
        )
        selected = FixedEvaluationArchitecture._select(evaluations)
        generation = GenerationRecord(
            generator_id=f"{self.controller.controller_id}:revised",
            candidate_ids=tuple(candidate_by_id),
            declared_non_exhaustive=True,
        )
        genealogy = self._genealogy(
            revision,
            initial_generation,
            initial_allocation,
            generation,
            allocation,
        )
        stop_reason = (
            "candidate budget exhausted"
            if len(initial_candidates) + len(revision.added_candidates)
            > len(candidates)
            else "open recursive inquiry cycle complete"
        )

        return OpenInquiryResult(
            architecture_id=self.architecture_id,
            task_id=task.task_id,
            generation=generation,
            allocation=allocation,
            evaluations=evaluations,
            selected_candidate_ids=selected,
            candidates=candidates,
            candidates_generated=len(candidates),
            evaluations_performed=(
                len(initial_evaluations) + len(evaluations)
            ),
            stop_reason=stop_reason,
            initial_generation=initial_generation,
            initial_allocation=initial_allocation,
            initial_evaluations=initial_evaluations,
            genealogy=genealogy,
            distinctions=revision.distinctions,
            reopening_conditions=revision.reopening_conditions,
            recursion_count=1,
        )

    def _unchanged_result(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
        generation: GenerationRecord,
        allocation: AllocationRecord,
        evaluations: tuple[EvaluationRecord, ...],
    ) -> OpenInquiryResult:
        return OpenInquiryResult(
            architecture_id=self.architecture_id,
            task_id=task.task_id,
            generation=generation,
            allocation=allocation,
            evaluations=evaluations,
            selected_candidate_ids=(
                FixedEvaluationArchitecture._select(evaluations)
            ),
            candidates=candidates,
            candidates_generated=len(candidates),
            evaluations_performed=len(evaluations),
            stop_reason=task.stopping_conditions[0],
            initial_generation=generation,
            initial_allocation=allocation,
            initial_evaluations=evaluations,
        )

    @staticmethod
    def _admit_candidates(
        initial: tuple[Candidate, ...],
        added: tuple[Candidate, ...],
        limit: int,
    ) -> tuple[Candidate, ...]:
        combined = initial + added
        FixedEvaluationArchitecture._require_unique_candidate_ids(combined)
        return combined[:limit]

    @staticmethod
    def _revised_active_ids(
        initial: AllocationRecord,
        revision: OpenInquiryRevision,
        represented_ids: tuple[str, ...],
    ) -> tuple[str, ...]:
        requested = (
            initial.active_candidate_ids
            + revision.reactivate_candidate_ids
            + tuple(
                candidate.candidate_id
                for candidate in revision.added_candidates
            )
        )
        unknown = set(requested) - set(represented_ids)
        if unknown:
            raise ValueError(
                "open inquiry activated unrepresented candidate ids"
            )
        return tuple(dict.fromkeys(requested))

    def _evaluate_revised(
        self,
        candidate: Candidate,
        revision: OpenInquiryRevision,
    ) -> EvaluationRecord:
        if candidate.candidate_id not in revision.evaluation_scores:
            raise KeyError(
                "no recursive evaluation score for candidate "
                f"{candidate.candidate_id}"
            )
        score = float(
            revision.evaluation_scores[candidate.candidate_id]
        )
        return EvaluationRecord(
            evaluator_id=f"{self.controller.controller_id}:revised",
            candidate_id=candidate.candidate_id,
            criteria=revision.evaluation_criteria,
            score=score,
            account=(
                f"Candidate {candidate.candidate_id} received recursive "
                f"score {score} under revision {revision.revision_id}."
            ),
        )

    @staticmethod
    def _validate_evaluation_ids(
        evaluations: tuple[EvaluationRecord, ...],
        active_ids: tuple[str, ...],
    ) -> None:
        if tuple(
            evaluation.candidate_id for evaluation in evaluations
        ) != active_ids:
            raise ValueError(
                "evaluator must return one record for each active candidate"
            )

    @staticmethod
    def _genealogy(
        revision: OpenInquiryRevision,
        initial_generation: GenerationRecord,
        initial_allocation: AllocationRecord,
        generation: GenerationRecord,
        allocation: AllocationRecord,
    ) -> tuple[GenealogyEvent, ...]:
        return (
            GenealogyEvent(
                event_id=f"{revision.revision_id}:distinction",
                kind="distinction",
                account="New distinctions entered recursive examination.",
                resulting_ids=revision.distinctions,
            ),
            GenealogyEvent(
                event_id=f"{revision.revision_id}:generation",
                kind="generator_revision",
                account=revision.generation_account,
                source_ids=initial_generation.candidate_ids,
                resulting_ids=generation.candidate_ids,
            ),
            GenealogyEvent(
                event_id=f"{revision.revision_id}:allocation",
                kind="allocator_revision",
                account="Allocation was revised under an explicit basis.",
                source_ids=(initial_allocation.allocator_id,),
                resulting_ids=allocation.active_candidate_ids,
            ),
            GenealogyEvent(
                event_id=f"{revision.revision_id}:evaluation",
                kind="evaluator_revision",
                account="Evaluation criteria were revised explicitly.",
                resulting_ids=revision.evaluation_criteria,
            ),
            GenealogyEvent(
                event_id=f"{revision.revision_id}:reopening",
                kind="reopening_conditions",
                account="Conditions for renewed inquiry remain represented.",
                resulting_ids=revision.reopening_conditions,
            ),
        )
