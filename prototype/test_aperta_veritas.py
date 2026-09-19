import json
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from aperta_veritas import InquiryLedger, evaluator


class InquiryLedgerTests(unittest.TestCase):
    def setUp(self):
        self.ledger = InquiryLedger()
        self.origin = self.ledger.encounter(
            object="coin toss protocol", representation="Every toss produces heads or tails.",
            observations=("heads", "tails", "edge case"), provenance=("protocol",),
            distinctions=("admissible binary result",), residuals=("excluded physical outcomes",))
        self.selector = evaluator(
            "Choose a usable binary result", criteria=("result is heads or tails",),
            measurements=("reported label",), values=("protocol usability",),
            exclusions=("edge", "lost coin", "unsettled coin"))

    def branch(self):
        return self.ledger.transition(
            prior_state_ids=(self.origin.state_id,), operation="separate physical state from report",
            transformation="split one claim into protocol and physical branches", evaluator=self.selector,
            candidates=(
                {"object": "protocol", "representation": "Recorded output is binary.", "status": "tested"},
                {"object": "physical toss", "representation": "Physical outcomes exceed protocol labels.",
                 "status": "unresolved", "residuals": ("excluded-state frequency",)}),
            selected_indexes=(0,), tests=("attempt edge landing",),
            reopening_conditions=("observe an excluded state",))

    def test_selection_preserves_inactive_branch_and_evaluator(self):
        edge = self.branch()
        self.assertEqual(len(edge.resulting_state_ids), 2)
        self.assertEqual(len(edge.inactive_state_ids), 1)
        self.assertIn("edge", edge.evaluator.exclusions)
        self.assertIn(edge.inactive_state_ids[0], self.ledger.states)

    def test_transition_requires_attributed_criteria(self):
        with self.assertRaises(ValueError):
            self.ledger.transition(prior_state_ids=(self.origin.state_id,),
                candidates=({"object": "x", "representation": "y"},), operation="select",
                transformation="selection", evaluator=evaluator("unspecified", criteria=()),
                selected_indexes=(0,))

    def test_recursive_audit_exposes_auditor_and_boundary(self):
        edge = self.branch()
        audit = self.ledger.recursive_audit(
            target_transition_id=edge.transition_id,
            auditor=evaluator("Inspect selection", criteria=("evaluator remains represented",),
                              values=("exposure",)),
            exposed_relations=("selection served protocol usability",),
            unrepresented_relations=("auditor category omissions",),
            stopping_boundary="test time exhausted")
        self.assertEqual(audit["auditor"]["values"], ("exposure",))
        self.assertEqual(audit["stopping_boundary"], "test time exhausted")

    def test_hash_chain_detects_mutation(self):
        self.branch()
        self.assertTrue(self.ledger.verify())
        self.ledger._records[0]["payload"]["representation"] = "altered"
        self.assertFalse(self.ledger.verify())

    def test_states_are_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            self.origin.status = "tested"

    def test_jsonl_export_retains_records(self):
        self.branch()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ledger.jsonl"
            self.ledger.export_jsonl(target)
            records = [json.loads(line) for line in target.read_text().splitlines()]
        self.assertEqual(len(records), len(self.ledger.records))
        self.assertEqual(records[-1]["kind"], "transition")


if __name__ == "__main__":
    unittest.main()
