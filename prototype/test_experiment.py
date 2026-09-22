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
    RevisableEvaluationArchitecture,
    RevisableScoreEvaluator,
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


class RevisableEvaluationArchitectureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.candidates = (
            Candidate("candidate_a", "First candidate."),
            Candidate("candidate_b", "Second candidate."),
        )
        self.task = ExperimentTask(
            task_id="revisable_evaluator_task",
            initial_representation="Evaluate supplied candidates.",
            resource_budget=ResourceBudget(
                max_candidates=2,
                max_evaluations=4,
            ),
            stopping_conditions=("revisable procedure complete",),
        )
        self.architecture = RevisableEvaluationArchitecture(
            generator=StaticGenerator(
                generator_id="fixed_generator",
                candidates=self.candidates,
            ),
            allocator=FixedOrderAllocator(
                allocator_id="fixed_allocator",
                basis=("supplied order", "evaluation budget"),
            ),
            evaluator=RevisableScoreEvaluator(
                evaluator_id="revisable_evaluator",
                initial_criteria=("initial criterion",),
                initial_scores={
                    "candidate_a": 0.4,
                    "candidate_b": 0.3,
                },
                revised_criteria=("revised criterion",),
                revised_scores={
                    "candidate_a": 0.2,
                    "candidate_b": 0.8,
                },
                revision_trigger_score=0.5,
            ),
        )

    def test_triggered_revision_changes_selected_candidate(self):
        result = self.architecture.run(self.task)

        self.assertEqual(
            tuple(
                evaluation.candidate_id
                for evaluation in result.initial_evaluations
                if evaluation.score == 0.4
            ),
            ("candidate_a",),
        )
        self.assertEqual(result.selected_candidate_ids, ("candidate_b",))

    def test_revision_genealogy_retains_prior_and_revised_criteria(self):
        result = self.architecture.run(self.task)

        self.assertEqual(len(result.evaluator_revisions), 1)
        revision = result.evaluator_revisions[0]
        self.assertEqual(revision.prior_criteria, ("initial criterion",))
        self.assertEqual(revision.revised_criteria, ("revised criterion",))
        self.assertTrue(revision.trigger)

    def test_revision_does_not_change_generator_or_allocator(self):
        result = self.architecture.run(self.task)

        self.assertEqual(result.generation.generator_id, "fixed_generator")
        self.assertEqual(result.allocation.allocator_id, "fixed_allocator")

    def test_revision_accounts_for_both_evaluation_passes(self):
        result = self.architecture.run(self.task)

        self.assertEqual(result.evaluations_performed, 4)
        self.assertEqual(
            result.stop_reason,
            "revised evaluation procedure complete",
        )

    def test_insufficient_budget_records_unperformed_revision(self):
        task = ExperimentTask(
            task_id="bounded_revision",
            initial_representation="Evaluate supplied candidates.",
            resource_budget=ResourceBudget(
                max_candidates=2,
                max_evaluations=2,
            ),
            stopping_conditions=("revisable procedure complete",),
        )

        result = self.architecture.run(task)

        self.assertEqual(result.evaluator_revisions, ())
        self.assertEqual(
            result.stop_reason,
            "evaluation budget exhausted before revision",
        )
        self.assertEqual(result.selected_candidate_ids, ("candidate_a",))

    def test_untriggered_evaluator_retains_initial_evaluations(self):
        architecture = RevisableEvaluationArchitecture(
            generator=self.architecture.generator,
            allocator=self.architecture.allocator,
            evaluator=RevisableScoreEvaluator(
                evaluator_id="revisable_evaluator",
                initial_criteria=("initial criterion",),
                initial_scores={
                    "candidate_a": 0.9,
                    "candidate_b": 0.3,
                },
                revised_criteria=("revised criterion",),
                revised_scores={
                    "candidate_a": 0.2,
                    "candidate_b": 0.8,
                },
                revision_trigger_score=0.5,
            ),
        )

        result = architecture.run(self.task)

        self.assertEqual(result.evaluator_revisions, ())
        self.assertEqual(result.evaluations, result.initial_evaluations)
        self.assertEqual(result.selected_candidate_ids, ("candidate_a",))

    def test_revised_evaluation_does_not_create_truth_field(self):
        result = self.architecture.run(self.task)

        self.assertFalse(hasattr(result, "truth"))
        self.assertFalse(hasattr(result.evaluator_revisions[0], "truth"))


if __name__ == "__main__":
    unittest.main()
