"""Tests for answer-key separation and held-out verification."""

import unittest

from benchmark import (
    ContrastiveInquiryController,
    HeldOutVerifier,
    VerificationKey,
    run_answer_key_separated_case,
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


if __name__ == "__main__":
    unittest.main()
