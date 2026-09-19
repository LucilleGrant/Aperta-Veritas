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
            object="coin toss protocol",
            representation="Every toss produces heads or tails.",
            observations=("heads", "tails", "edge case"),
            provenance=("protocol",),
            distinctions=("admissible binary result",),
            residuals=("excluded physical outcomes",),
        )

        self.selector = evaluator(
            "Choose a usable binary result",
            criteria=("result is heads or tails",),
            measurements=("reported label",),
            values=("protocol usability",),
            exclusions=("edge", "lost coin", "unsettled coin"),
        )

    def branch(self):
        return self.ledger.transition(
            prior_state_ids=(self.origin.state_id,),
            operation="separate physical state from report",
            transformation="split one claim into protocol and physical branches",
            evaluator=self.selector,
            candidates=(
                {
                    "object": "protocol",
                    "representation": "Recorded output is binary.",
                    "status": "tested",
                },
                {
                    "object": "physical toss",
                    "representation": "Physical outcomes exceed protocol labels.",
                    "status": "unresolved",
                    "residuals": ("excluded-state frequency",),
                },
            ),
            selected_indexes=(0,),
            tests=("attempt edge landing",),
            stopping_conditions=("current test sequence complete",),
            reopening_conditions=("observe an excluded state",),
        )

    def branch_states(self):
        edge = self.branch()
        states = [
            self.ledger.states[state_id]
            for state_id in edge.resulting_state_ids
        ]
        return edge, states

    def test_selection_preserves_inactive_branch_and_evaluator(self):
        edge = self.branch()

        self.assertEqual(len(edge.resulting_state_ids), 2)
        self.assertEqual(len(edge.inactive_state_ids), 1)
        self.assertIn("edge", edge.evaluator.exclusions)
        self.assertIn(
            edge.inactive_state_ids[0],
            self.ledger.states,
        )

    def test_inactive_branch_is_not_erased(self):
        edge = self.branch()

        inactive_id = edge.inactive_state_ids[0]
        inactive = self.ledger.states[inactive_id]

        self.assertFalse(inactive.active)
        self.assertEqual(inactive.status, "unresolved")
        self.assertIn(
            "excluded-state frequency",
            inactive.residuals,
        )

    def test_transition_requires_attributed_criteria(self):
        with self.assertRaises(ValueError):
            self.ledger.transition(
                prior_state_ids=(self.origin.state_id,),
                candidates=(
                    {
                        "object": "x",
                        "representation": "y",
                    },
                ),
                operation="select",
                transformation="selection",
                evaluator=evaluator(
                    "unspecified",
                    criteria=(),
                ),
                selected_indexes=(0,),
            )

    def test_recursive_audit_exposes_auditor_and_boundary(self):
        edge = self.branch()

        audit = self.ledger.recursive_audit(
            target_transition_id=edge.transition_id,
            auditor=evaluator(
                "Inspect selection",
                criteria=("evaluator remains represented",),
                values=("exposure",),
            ),
            exposed_relations=(
                "selection served protocol usability",
            ),
            unrepresented_relations=(
                "auditor category omissions",
            ),
            stopping_boundary="test time exhausted",
        )

        self.assertEqual(
            audit["auditor"]["values"],
            ("exposure",),
        )
        self.assertEqual(
            audit["stopping_boundary"],
            "test time exhausted",
        )

    def test_stopping_is_distinct_from_closure(self):
        edge = self.branch()

        self.assertIn(
            "current test sequence complete",
            edge.stopping_conditions,
        )
        self.assertIn(
            "observe an excluded state",
            edge.reopening_conditions,
        )

        for state_id in edge.resulting_state_ids:
            state = self.ledger.states[state_id]
            self.assertNotEqual(state.status, "superseded")

    def test_belief_is_separate_from_support(self):
        belief = self.ledger.record_belief(
            proposition="All physical tosses are binary.",
            holder="protocol operator",
            basis=("protocol specification",),
            confidence=0.95,
            revision_conditions=(
                "observe stable nonbinary outcome",
            ),
        )

        state = self.ledger.encounter(
            object="operator belief",
            representation="All physical tosses are binary.",
            beliefs=(belief.belief_id,),
        )

        support = self.ledger.record_support(
            conclusion_state_id=state.state_id,
            relation="supports",
            measurements=("protocol consistency",),
            observations=("heads", "tails"),
            residuals=("edge case unresolved",),
        )

        self.assertEqual(belief.confidence, 0.95)
        self.assertIn(
            belief.belief_id,
            state.beliefs,
        )
        self.assertNotEqual(
            belief.belief_id,
            support.support_id,
        )
        self.assertNotEqual(
            belief.confidence,
            support.score,
        )

    def test_rational_faith_can_preserve_revision_conditions(self):
        belief = self.ledger.record_belief(
            proposition="The protocol captures normal tosses.",
            holder="investigator",
            basis=("repeated ordinary trials",),
            confidence=0.8,
            revision_conditions=(
                "systematic excluded outcomes observed",
            ),
        )

        self.assertTrue(belief.revision_conditions)
        self.assertFalse(belief.insulated_from)

    def test_blind_faith_can_be_represented_without_declaring_falsehood(self):
        belief = self.ledger.record_belief(
            proposition="The protocol is universally complete.",
            holder="operator",
            confidence=1.0,
            insulated_from=(
                "edge outcomes",
                "contradictory observations",
            ),
        )

        self.assertTrue(belief.insulated_from)
        self.assertEqual(belief.confidence, 1.0)

        self.assertFalse(
            hasattr(belief, "truth")
        )
        self.assertFalse(
            hasattr(belief, "falsehood")
        )

    def test_support_is_separate_from_conclusion(self):
        _, states = self.branch_states()

        conclusion = states[0]

        support = self.ledger.record_support(
            conclusion_state_id=conclusion.state_id,
            relation="supports",
            measurements=(
                "reported-label consistency",
            ),
            conditions=(
                "protocol reporting rules",
            ),
            observations=(
                "heads recorded as heads",
                "tails recorded as tails",
            ),
        )

        self.assertEqual(
            support.conclusion_state_id,
            conclusion.state_id,
        )
        self.assertNotEqual(
            support.support_id,
            conclusion.state_id,
        )
        self.assertNotIn(
            "support",
            conclusion.__dataclass_fields__,
        )

    def test_support_requires_explicit_measurement(self):
        _, states = self.branch_states()

        with self.assertRaises(ValueError):
            self.ledger.record_support(
                conclusion_state_id=states[0].state_id,
                relation="supports",
                measurements=(),
            )

    def test_confidence_does_not_create_support(self):
        belief = self.ledger.record_belief(
            proposition="The coin cannot land on edge.",
            holder="operator",
            confidence=1.0,
        )

        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )
        self.assertEqual(belief.confidence, 1.0)

    def test_comparison_preserves_comparison_set(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            measurements=("protocol fit",),
            score=0.9,
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            measurements=("physical coverage",),
            score=0.7,
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_ids=(
                first_support.support_id,
                second_support.support_id,
            ),
            measurements=("represented test coverage",),
            conditions=("current observations only",),
            best_supported_state_ids=(
                states[0].state_id,
            ),
            known_exclusions=(
                "unobserved physical outcomes",
            ),
        )

        self.assertEqual(
            len(comparison.conclusion_state_ids),
            2,
        )
        self.assertIn(
            states[0].state_id,
            comparison.best_supported_state_ids,
        )
        self.assertTrue(
            comparison.unrepresented_alternatives_possible
        )

    def test_best_supported_is_not_truth_certificate(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            measurements=("test fit",),
            score=1.0,
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            measurements=("test fit",),
            score=0.5,
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_ids=(
                first_support.support_id,
                second_support.support_id,
            ),
            measurements=("test fit",),
            best_supported_state_ids=(
                states[0].state_id,
            ),
        )

        self.assertIn(
            states[0].state_id,
            comparison.best_supported_state_ids,
        )

        self.assertFalse(
            hasattr(comparison, "truth")
        )
        self.assertFalse(
            hasattr(comparison, "definitive_truth")
        )

    def test_perfect_score_does_not_create_truth_field(self):
        _, states = self.branch_states()

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            measurements=("bounded test",),
            score=1.0,
        )

        self.assertEqual(support.score, 1.0)
        self.assertFalse(
            hasattr(support, "truth")
        )
        self.assertFalse(
            hasattr(support, "definitive_truth")
        )

    def test_comparison_rejects_external_best_supported_state(self):
        _, states = self.branch_states()

        external = self.ledger.encounter(
            object="external alternative",
            representation="Another possibility.",
        )

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            measurements=("test",),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            measurements=("test",),
        )

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_ids=(
                    first_support.support_id,
                    second_support.support_id,
                ),
                measurements=("test",),
                best_supported_state_ids=(
                    external.state_id,
                ),
            )

    def test_comparison_rejects_support_for_external_conclusion(self):
        _, states = self.branch_states()

        external = self.ledger.encounter(
            object="external alternative",
            representation="Another possibility.",
        )

        external_support = self.ledger.record_support(
            conclusion_state_id=external.state_id,
            relation="supports",
            measurements=("test",),
        )

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_ids=(
                    external_support.support_id,
                ),
                measurements=("test",),
            )

    def test_comparison_requires_explicit_measurement(self):
        _, states = self.branch_states()

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_ids=(),
                measurements=(),
            )

    def test_hash_chain_detects_mutation(self):
        self.branch()

        self.assertTrue(self.ledger.verify())

        self.ledger._records[0]["payload"][
            "representation"
        ] = "altered"

        self.assertFalse(self.ledger.verify())

    def test_states_are_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            self.origin.status = "tested"

    def test_support_relations_are_immutable(self):
        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            measurements=("observation",),
        )

        with self.assertRaises(FrozenInstanceError):
            support.relation = "contradicts"

    def test_beliefs_are_immutable(self):
        belief = self.ledger.record_belief(
            proposition="A proposition",
            holder="agent",
        )

        with self.assertRaises(FrozenInstanceError):
            belief.confidence = 1.0

    def test_jsonl_export_retains_records(self):
        self.branch()

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ledger.jsonl"
            self.ledger.export_jsonl(target)

            records = [
                json.loads(line)
                for line in target.read_text().splitlines()
            ]

        self.assertEqual(
            len(records),
            len(self.ledger.records),
        )
        self.assertEqual(
            records[-1]["kind"],
            "transition",
        )

    def test_jsonl_export_includes_support_and_comparison(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            measurements=("test fit",),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            measurements=("test fit",),
        )

        self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_ids=(
                first_support.support_id,
                second_support.support_id,
            ),
            measurements=("test fit",),
            best_supported_state_ids=(
                states[0].state_id,
            ),
        )

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ledger.jsonl"
            self.ledger.export_jsonl(target)

            records = [
                json.loads(line)
                for line in target.read_text().splitlines()
            ]

        kinds = [record["kind"] for record in records]

        self.assertIn("support", kinds)
        self.assertIn("comparison", kinds)

    def test_hash_chain_covers_support_records(self):
        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            measurements=("observation",),
        )

        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "support"
                and record["payload"]["support_id"]
                == support.support_id
            ):
                record["payload"]["relation"] = "contradicts"
                break

        self.assertFalse(self.ledger.verify())


if __name__ == "__main__":
    unittest.main()
