"""Tests for answer-key separation and held-out verification."""

import unittest

from benchmark import (
    ContrastiveInquiryController,
    HeldOutVerifier,
    PairwiseContrastiveInquiryController,
    VerificationKey,
    benchmark_cases,
    run_answer_key_separated_case,
    run_benchmark_suite,
)
from experiment import (
    AllocationRecord,
    Candidate,
    ExperimentTask,
    ObservationRecord,
    ResourceBudget,
)


class AnswerKeySeparatedBenchmarkTests(unittest.TestCase):
    def test_controller_generates_from_public_scopes(self):
        task = ExperimentTask(
            task_id="public_scope_test",
            initial_representation="Compare observations.",
            resource_budget=ResourceBudget(3, 4),
            stopping_conditions=("test complete",),
            observations=(
                ObservationRecord("o1", "alpha scope", "Alpha record."),
                ObservationRecord("o2", "beta scope", "Beta record."),
            ),
        )
        candidates = (Candidate("c1", "Initial candidate."),)
        allocation = AllocationRecord(
            "allocator",
            ("test basis",),
            ("c1",),
            (),
        )

        revision = ContrastiveInquiryController().examine(
            task,
            candidates,
            allocation,
            (),
        )

        self.assertIsNotNone(revision)
        self.assertIn("alpha scope", revision.distinctions[0])
        self.assertIn("beta scope", revision.distinctions[0])

    def test_controller_has_no_revision_for_one_scope(self):
        task = ExperimentTask(
            task_id="one_scope_test",
            initial_representation="One observation.",
            resource_budget=ResourceBudget(2, 2),
            stopping_conditions=("test complete",),
            observations=(
                ObservationRecord("o1", "one scope", "One record."),
            ),
        )
        allocation = AllocationRecord(
            "allocator",
            ("test basis",),
            (),
            (),
        )

        revision = ContrastiveInquiryController().examine(
            task,
            (),
            allocation,
            (),
        )

        self.assertIsNone(revision)

    def test_verifier_requires_every_hidden_rubric_term(self):
        key = VerificationKey(
            "case",
            ("alpha", "beta"),
            ("distinct", "relation"),
        )
        partial = Candidate(
            "partial",
            "Alpha and beta are distinct.",
        )
        complete = Candidate(
            "complete",
            "Alpha and beta are distinct scopes with a relation.",
        )

        self.assertFalse(HeldOutVerifier._matches(partial, key))
        self.assertTrue(HeldOutVerifier._matches(complete, key))

    def test_matched_case_keeps_key_out_of_architecture_inputs(self):
        report = run_answer_key_separated_case()

        self.assertFalse(
            report["architecture_inputs_contain_verification_key"]
        )

    def test_only_open_inquiry_recovers_hidden_relation(self):
        report = run_answer_key_separated_case()
        results = report["results"]

        self.assertFalse(
            results["architecture_a_fixed_evaluation"]["recovered"]
        )
        self.assertFalse(
            results["architecture_b_revisable_evaluation"]["recovered"]
        )
        self.assertTrue(
            results["architecture_c_open_recursive_inquiry"]["recovered"]
        )


class MultiCaseBenchmarkTests(unittest.TestCase):
    def test_suite_contains_positive_and_negative_cases(self):
        cases = benchmark_cases()

        self.assertTrue(any(case.expected_recovery for case in cases))
        self.assertTrue(any(not case.expected_recovery for case in cases))

    def test_pairwise_controller_is_order_independent(self):
        controller = PairwiseContrastiveInquiryController()
        candidate = Candidate("c1", "Initial candidate.")
        allocation = AllocationRecord(
            "allocator",
            ("test basis",),
            ("c1",),
            (),
        )
        first = ExperimentTask(
            "first_order",
            "Compare scopes.",
            ResourceBudget(8, 12),
            ("test complete",),
            (
                ObservationRecord("o1", "alpha", "Alpha record."),
                ObservationRecord("o2", "beta", "Beta record."),
                ObservationRecord("o3", "decoy", "Decoy record."),
            ),
        )
        second = ExperimentTask(
            "second_order",
            "Compare scopes.",
            ResourceBudget(8, 12),
            ("test complete",),
            tuple(reversed(first.observations)),
        )

        first_revision = controller.examine(
            first, (candidate,), allocation, ()
        )
        second_revision = controller.examine(
            second, (candidate,), allocation, ()
        )
        first_text = {
            item.representation for item in first_revision.added_candidates
        }
        second_text = {
            item.representation for item in second_revision.added_candidates
        }

        self.assertEqual(first_text, second_text)

    def test_suite_keeps_keys_out_of_architecture_inputs(self):
        report = run_benchmark_suite()

        self.assertFalse(
            report["architecture_inputs_contain_verification_keys"]
        )

    def test_open_inquiry_recovers_all_positive_cases(self):
        report = run_benchmark_suite()
        aggregate = report["aggregates"][
            "architecture_c_open_recursive_inquiry"
        ]

        self.assertEqual(aggregate["positive_cases"], 4)
        self.assertEqual(aggregate["positive_recoveries"], 4)
        self.assertEqual(aggregate["recovery_rate"], 1.0)

    def test_fixed_and_revisable_do_not_recover_positive_cases(self):
        report = run_benchmark_suite()

        for architecture_id in (
            "architecture_a_fixed_evaluation",
            "architecture_b_revisable_evaluation",
        ):
            aggregate = report["aggregates"][architecture_id]
            self.assertEqual(aggregate["positive_recoveries"], 0)
            self.assertEqual(aggregate["recovery_rate"], 0.0)

    def test_no_architecture_triggers_negative_controls(self):
        report = run_benchmark_suite()

        for aggregate in report["aggregates"].values():
            self.assertEqual(aggregate["negative_cases"], 2)
            self.assertEqual(aggregate["false_positives"], 0)
            self.assertEqual(aggregate["false_positive_rate"], 0.0)

    def test_suite_reports_resource_use(self):
        report = run_benchmark_suite()

        for aggregate in report["aggregates"].values():
            self.assertGreater(aggregate["candidates_generated"], 0)
            self.assertGreater(aggregate["evaluations_performed"], 0)

    def test_report_marks_engineering_evidence_boundary(self):
        report = run_benchmark_suite()

        self.assertIn("not research evidence", report["evidence_boundary"])


if __name__ == "__main__":
    unittest.main()
