"""Tests for the evaluator-self-confirmation development benchmark."""

import unittest

from evaluator_self_confirmation import (
    run_evaluator_self_confirmation_case,
)


class EvaluatorSelfConfirmationBenchmarkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = run_evaluator_self_confirmation_case()
        self.decisions = self.report["decisions"]
        self.verification = self.report["verification"]

    def test_report_is_labeled_as_engineering_check(self):
        self.assertIn("engineering check", self.report["status"])
        self.assertIn(
            "not research evidence",
            self.report["evidence_boundary"],
        )

    def test_architectures_receive_shared_candidate_set(self):
        self.assertEqual(
            self.report["architecture_inputs"]["candidate_ids"],
            ["incumbent", "successor"],
        )

    def test_fixed_evaluator_retains_incumbent(self):
        decision = self.decisions[
            "architecture_a_fixed_evaluation"
        ]
        self.assertEqual(
            decision["selected_candidate_ids"],
            ["incumbent"],
        )
        self.assertFalse(
            self.verification[
                "architecture_a_fixed_evaluation"
            ]["false_improvement"]
        )

    def test_revisable_evaluator_self_confirms_successor(self):
        decision = self.decisions[
            "architecture_b_revisable_evaluation"
        ]
        self.assertEqual(
            decision["selected_candidate_ids"],
            ["successor"],
        )
        self.assertTrue(
            self.verification[
                "architecture_b_revisable_evaluation"
            ]["false_improvement"]
        )

    def test_open_cross_evaluation_exposes_rank_reversal(self):
        decision = self.decisions[
            "architecture_c_open_cross_evaluation"
        ]
        self.assertTrue(decision["evaluator_conflict_exposed"])
        self.assertEqual(
            decision["predecessor_selected_candidate_ids"],
            ["incumbent"],
        )
        self.assertEqual(
            decision["successor_selected_candidate_ids"],
            ["successor"],
        )

    def test_open_cross_evaluation_withholds_improvement_designation(self):
        decision = self.decisions[
            "architecture_c_open_cross_evaluation"
        ]
        self.assertEqual(decision["selected_candidate_ids"], [])
        self.assertEqual(
            decision["designation"],
            "unresolved_evaluator_conflict",
        )

    def test_open_comparison_does_not_certify_predecessor(self):
        decision = self.decisions[
            "architecture_c_open_cross_evaluation"
        ]
        self.assertFalse(decision["predecessor_certified_correct"])

    def test_verification_key_is_held_out_and_budget_is_reported(self):
        self.assertFalse(
            self.report[
                "architecture_inputs_contain_verification_key"
            ]
        )
        self.assertTrue(
            self.report["verification_applied_after_decisions"]
        )
        ceiling = self.report["architecture_inputs"][
            "resource_budget"
        ]["max_evaluations"]
        for decision in self.decisions.values():
            self.assertLessEqual(
                decision["evaluations_performed"],
                ceiling,
            )


if __name__ == "__main__":
    unittest.main()
