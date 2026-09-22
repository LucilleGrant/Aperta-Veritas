"""Tests for the comparative experiment interface and Architecture A."""

from dataclasses import FrozenInstanceError
import unittest

from experiment import (
    AllocationRecord,
    Candidate,
    ExperimentTask,
    FixedEvaluationArchitecture,
    FixedOrderAllocator,
    FixedScoreEvaluator,
    ResourceBudget,
    StaticGenerator,
)


class FixedEvaluationArchitectureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.candidates = (
            Candidate("candidate_a", "First candidate."),
            Candidate("candidate_b", "Second candidate."),
            Candidate("candidate_c", "Third candidate."),
        )
        self.task = ExperimentTask(
            task_id="development_task_1",
            initial_representation="Compare represented candidates.",
            resource_budget=ResourceBudget(
                max_candidates=3,
                max_evaluations=2,
            ),
            stopping_conditions=("fixed procedure complete",),
        )
        self.architecture = FixedEvaluationArchitecture(
            generator=StaticGenerator(
                generator_id="fixed_generator",
                candidates=self.candidates,
            ),
            allocator=FixedOrderAllocator(
                allocator_id="fixed_allocator",
                basis=("supplied order", "evaluation budget"),
            ),
            evaluator=FixedScoreEvaluator(
                evaluator_id="fixed_evaluator",
                criteria=("declared score table",),
                scores={
                    "candidate_a": 0.25,
                    "candidate_b": 0.75,
                    "candidate_c": 1.0,
                },
            ),
        )

    def test_run_separates_generation_allocation_and_evaluation(self):
        result = self.architecture.run(self.task)

        self.assertEqual(result.generation.generator_id, "fixed_generator")
        self.assertEqual(result.allocation.allocator_id, "fixed_allocator")
        self.assertEqual(
            {record.evaluator_id for record in result.evaluations},
            {"fixed_evaluator"},
        )

    def test_generation_is_declared_non_exhaustive(self):
        result = self.architecture.run(self.task)

        self.assertTrue(result.generation.declared_non_exhaustive)

    def test_only_active_candidates_are_evaluated(self):
        result = self.architecture.run(self.task)

        self.assertEqual(
            tuple(record.candidate_id for record in result.evaluations),
            ("candidate_a", "candidate_b"),
        )
        self.assertEqual(
            result.allocation.inactive_candidate_ids,
            ("candidate_c",),
        )

    def test_selection_uses_fixed_evaluator_score(self):
        result = self.architecture.run(self.task)

        self.assertEqual(result.selected_candidate_ids, ("candidate_b",))

    def test_tied_scores_retain_each_selected_candidate(self):
        architecture = FixedEvaluationArchitecture(
            generator=self.architecture.generator,
            allocator=self.architecture.allocator,
            evaluator=FixedScoreEvaluator(
                evaluator_id="fixed_evaluator",
                criteria=("declared score table",),
                scores={
                    "candidate_a": 0.5,
                    "candidate_b": 0.5,
                    "candidate_c": 0.0,
                },
            ),
        )

        result = architecture.run(self.task)

        self.assertEqual(
            result.selected_candidate_ids,
            ("candidate_a", "candidate_b"),
        )

    def test_candidate_budget_bounds_generation_record(self):
        task = ExperimentTask(
            task_id="bounded_generation",
            initial_representation="Bound the candidate set.",
            resource_budget=ResourceBudget(
                max_candidates=2,
                max_evaluations=2,
            ),
            stopping_conditions=("fixed procedure complete",),
        )

        result = self.architecture.run(task)

        self.assertEqual(
            result.generation.candidate_ids,
            ("candidate_a", "candidate_b"),
        )
        self.assertEqual(result.stop_reason, "candidate budget exhausted")

    def test_evaluation_budget_is_recorded_as_stop_reason(self):
        result = self.architecture.run(self.task)

        self.assertEqual(result.stop_reason, "evaluation budget exhausted")

    def test_declared_stop_is_used_when_budgets_do_not_bind(self):
        task = ExperimentTask(
            task_id="complete_fixed_run",
            initial_representation="Evaluate every supplied candidate.",
            resource_budget=ResourceBudget(
                max_candidates=3,
                max_evaluations=3,
            ),
            stopping_conditions=("fixed procedure complete",),
        )

        result = self.architecture.run(task)

        self.assertEqual(result.stop_reason, "fixed procedure complete")

    def test_allocation_must_partition_candidate_set(self):
        class InvalidAllocator:
            allocator_id = "invalid_allocator"

            def allocate(self, task, candidates):
                del task, candidates
                return AllocationRecord(
                    allocator_id=self.allocator_id,
                    basis=("invalid test allocation",),
                    active_candidate_ids=("candidate_a",),
                    inactive_candidate_ids=(),
                )

        architecture = FixedEvaluationArchitecture(
            generator=self.architecture.generator,
            allocator=InvalidAllocator(),
            evaluator=self.architecture.evaluator,
        )

        with self.assertRaises(ValueError):
            architecture.run(self.task)

    def test_duplicate_candidate_ids_are_rejected(self):
        architecture = FixedEvaluationArchitecture(
            generator=StaticGenerator(
                generator_id="duplicate_generator",
                candidates=(
                    self.candidates[0],
                    Candidate("candidate_a", "Duplicate identifier."),
                ),
            ),
            allocator=self.architecture.allocator,
            evaluator=self.architecture.evaluator,
        )

        with self.assertRaises(ValueError):
            architecture.run(self.task)

    def test_result_is_immutable(self):
        result = self.architecture.run(self.task)

        with self.assertRaises(FrozenInstanceError):
            result.stop_reason = "changed"

    def test_evaluation_does_not_create_truth_field(self):
        result = self.architecture.run(self.task)

        self.assertFalse(hasattr(result.evaluations[0], "truth"))
        self.assertFalse(hasattr(result, "truth"))


if __name__ == "__main__":
    unittest.main()
