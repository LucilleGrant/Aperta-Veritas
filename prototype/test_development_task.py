"""Tests for the first matched comparative development task."""

import unittest

from development_task import (
    TARGET_CANDIDATE_ID,
    run_missing_distinction_task,
)


class MissingDistinctionDevelopmentTaskTests(unittest.TestCase):
    def setUp(self) -> None:
        self.report = run_missing_distinction_task()

    def test_report_is_not_labeled_as_research_evidence(self):
        self.assertEqual(
            self.report["status"],
            "engineering check, not research evidence",
        )

    def test_each_architecture_uses_same_resource_ceiling(self):
        self.assertEqual(
            self.report["resource_budget"],
            {"max_candidates": 3, "max_evaluations": 4},
        )

    def test_fixed_and_revisable_evaluation_do_not_recover_target(self):
        for label in ("A", "B"):
            architecture = self.report["architectures"][label]
            self.assertFalse(architecture["target_candidate_recovered"])
            self.assertNotIn(
                TARGET_CANDIDATE_ID,
                architecture["selected_candidate_ids"],
            )

    def test_open_recursive_inquiry_recovers_and_selects_target(self):
        architecture = self.report["architectures"]["C"]

        self.assertTrue(architecture["target_candidate_recovered"])
        self.assertEqual(
            architecture["selected_candidate_ids"],
            [TARGET_CANDIDATE_ID],
        )


if __name__ == "__main__":
    unittest.main()
