"""Shared experiment interface and fixed-evaluation reference architecture."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Protocol


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

    def allocate(
        self,
        task: ExperimentTask,
        candidates: tuple[Candidate, ...],
    ) -> AllocationRecord:
        limit = task.resource_budget.max_evaluations
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
