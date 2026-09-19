import json
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from aperta_veritas import InquiryLedger, evaluator


class InquiryLedgerTests(unittest.TestCase):
    def setUp(self):
        self.ledger = InquiryLedger()

        self.outcome_distinction = self.ledger.record_distinction(
            name="reported outcome",
            specification=(
                "The protocol distinguishes reported heads "
                "from reported tails."
            ),
            operationalization=(
                "classify the reported protocol label",
            ),
            provenance=("protocol",),
        )

        self.origin = self.ledger.encounter(
            object="coin toss protocol",
            representation="Every reported toss is heads or tails.",
            observations=("heads", "tails", "edge case"),
            provenance=("protocol",),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            residuals=("excluded physical outcomes",),
        )

        self.selector = evaluator(
            "Choose a usable binary result",
            criteria=("result is heads or tails",),
            distinctions=(
                self.outcome_distinction.distinction_id,
            ),
            values=("protocol usability",),
            exclusions=("edge", "lost coin", "unsettled coin"),
        )

    def branch(self):
        return self.ledger.transition(
            prior_state_ids=(self.origin.state_id,),
            operation="separate physical state from report",
            transformation=(
                "split one claim into protocol and physical branches"
            ),
            evaluator=self.selector,
            candidates=(
                {
                    "object": "protocol",
                    "representation": "Recorded output is binary.",
                    "status": "tested",
                    "distinction_ids": (
                        self.outcome_distinction.distinction_id,
                    ),
                },
                {
                    "object": "physical toss",
                    "representation": (
                        "Physical outcomes exceed protocol labels."
                    ),
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

    def test_distinction_is_separate_from_measurement(self):
        distinction = self.ledger.record_distinction(
            name="physical resting state",
            specification=(
                "Distinguish stable face, edge, and unresolved motion."
            ),
            operationalization=(
                "inspect the coin after motion ceases",
            ),
        )

        self.assertIn(
            distinction.distinction_id,
            self.ledger.distinctions,
        )
        self.assertEqual(len(self.ledger.measurements), 0)
        self.assertFalse(
            hasattr(distinction, "measurement_id")
        )

    def test_measurement_requires_represented_distinction(self):
        with self.assertRaises(KeyError):
            self.ledger.record_measurement(
                result="heads",
                distinction_ids=("missing_distinction",),
            )

    def test_measurement_preserves_distinction_genealogy(self):
        measurement = self.ledger.record_measurement(
            result="reported heads",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            method=("read protocol output",),
            conditions=("ordinary reporting",),
        )

        self.assertIn(
            self.outcome_distinction.distinction_id,
            measurement.distinction_ids,
        )
        self.assertIn(
            measurement.measurement_id,
            self.ledger.measurements,
        )

    def test_measurement_does_not_automatically_create_support(self):
        measurement = self.ledger.record_measurement(
            result="reported heads",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        self.assertIn(
            measurement.measurement_id,
            self.ledger.measurements,
        )
        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )

    def test_state_can_reference_distinction_and_measurement_separately(self):
        measurement = self.ledger.record_measurement(
            result="reported tails",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        state = self.ledger.encounter(
            object="reported toss",
            representation="The reported result was tails.",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            measurement_ids=(measurement.measurement_id,),
        )

        self.assertIn(
            self.outcome_distinction.distinction_id,
            state.distinction_ids,
        )
        self.assertIn(
            measurement.measurement_id,
            state.measurement_ids,
        )

    def test_support_can_exist_without_measurement(self):
        _, states = self.branch_states()

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=(
                "logical relation between protocol definition "
                "and permitted report labels",
            ),
            logical_relations=(
                "protocol permits only heads or tails labels",
            ),
        )

        self.assertEqual(support.measurement_ids, ())
        self.assertTrue(support.logical_relations)
        self.assertIn(
            support.support_id,
            self.ledger.support_relations,
        )

    def test_support_can_reference_measurement_without_becoming_measurement(
        self,
    ):
        measurement = self.ledger.record_measurement(
            result="reported outputs matched protocol labels",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            method=("compare reports with protocol categories",),
        )

        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            basis=("observed protocol consistency",),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            measurement_ids=(measurement.measurement_id,),
            observations=("heads reported heads",),
        )

        self.assertIn(
            measurement.measurement_id,
            support.measurement_ids,
        )
        self.assertNotEqual(
            measurement.measurement_id,
            support.support_id,
        )

    def test_support_requires_explicit_basis_not_measurement(self):
        with self.assertRaises(ValueError):
            self.ledger.record_support(
                conclusion_state_id=self.origin.state_id,
                relation="supports",
                basis=(),
            )

    def test_support_is_separate_from_conclusion(self):
        _, states = self.branch_states()
        conclusion = states[0]

        support = self.ledger.record_support(
            conclusion_state_id=conclusion.state_id,
            relation="supports",
            basis=("protocol definition",),
            conditions=("protocol reporting rules",),
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
            basis=("ordinary observed outcomes",),
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

    def test_blind_faith_can_be_represented_without_declaring_falsehood(
        self,
    ):
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
        self.assertFalse(hasattr(belief, "truth"))
        self.assertFalse(hasattr(belief, "falsehood"))

    def test_comparison_requires_explicit_basis(self):
        _, states = self.branch_states()

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_ids=(),
                basis=(),
            )

    def test_comparison_does_not_require_measurement(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("protocol definition",),
            logical_relations=(
                "binary output follows from protocol rule",
            ),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("observed edge case",),
            observations=("coin temporarily rested on edge",),
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
            basis=(
                "scope of each conclusion relative to represented evidence",
            ),
            criteria=("represented explanatory scope",),
            conditions=("current observations only",),
        )

        self.assertEqual(comparison.measurement_ids, ())
        self.assertTrue(comparison.basis)

    def test_comparison_preserves_comparison_set(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("protocol fit",),
            score=0.9,
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("physical coverage",),
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
            basis=("represented test coverage",),
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

    def test_incommensurability_can_be_preserved_without_ranking(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("protocol definition",),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("physical observation",),
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
            basis=(
                "different scopes currently lack a represented "
                "basis for ranking",
            ),
            incomparable_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            unresolved_relations=(
                "protocol completeness and physical completeness "
                "are not presently commensurated",
            ),
        )

        self.assertEqual(
            comparison.best_supported_state_ids,
            (),
        )
        self.assertEqual(
            set(comparison.incomparable_state_ids),
            {
                states[0].state_id,
                states[1].state_id,
            },
        )

    def test_best_supported_is_not_truth_certificate(self):
        _, states = self.branch_states()

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("bounded protocol test",),
            score=1.0,
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("partial physical observations",),
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
            basis=("bounded represented support scores",),
            best_supported_state_ids=(
                states[0].state_id,
            ),
        )

        self.assertIn(
            states[0].state_id,
            comparison.best_supported_state_ids,
        )
        self.assertFalse(hasattr(comparison, "truth"))
        self.assertFalse(
            hasattr(comparison, "definitive_truth")
        )

    def test_perfect_score_does_not_create_truth_field(self):
        _, states = self.branch_states()

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("bounded test",),
            score=1.0,
        )

        self.assertEqual(support.score, 1.0)
        self.assertFalse(hasattr(support, "truth"))
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
            basis=("represented test",),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("represented test",),
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
                basis=("represented test relation",),
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
            basis=("external test",),
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
                basis=("represented comparison",),
            )

    def test_recursive_audit_exposes_corrected_architecture(self):
        edge, states = self.branch_states()

        measurement = self.ledger.record_measurement(
            result="binary protocol output observed",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("protocol observation",),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            measurement_ids=(measurement.measurement_id,),
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_ids=(support.support_id,),
            basis=("protocol scope versus physical scope",),
            unresolved_relations=(
                "physical possibility space incomplete",
            ),
        )

        audit = self.ledger.recursive_audit(
            target_transition_id=edge.transition_id,
            auditor=evaluator(
                "Inspect selection",
                criteria=("evaluator remains represented",),
                distinctions=(
                    self.outcome_distinction.distinction_id,
                ),
                comparison_basis=(
                    "audit represented genealogy",
                ),
                values=("exposure",),
            ),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            measurement_ids=(measurement.measurement_id,),
            support_ids=(support.support_id,),
            comparison_ids=(comparison.comparison_id,),
            comparison_basis=(
                "audit represented genealogy",
            ),
            exposed_relations=(
                "selection served protocol usability",
            ),
            unrepresented_relations=(
                "auditor category omissions",
            ),
            stopping_boundary="test time exhausted",
        )

        self.assertIn(
            self.outcome_distinction.distinction_id,
            audit["distinction_ids"],
        )
        self.assertIn(
            measurement.measurement_id,
            audit["measurement_ids"],
        )
        self.assertIn(
            support.support_id,
            audit["support_ids"],
        )
        self.assertIn(
            comparison.comparison_id,
            audit["comparison_ids"],
        )
        self.assertTrue(audit["comparison_basis"])
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
            self.assertNotEqual(
                state.status,
                "superseded",
            )

    def test_states_are_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            self.origin.status = "tested"

    def test_distinctions_are_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            self.outcome_distinction.name = "changed"

    def test_measurements_are_immutable(self):
        measurement = self.ledger.record_measurement(
            result="heads",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        with self.assertRaises(FrozenInstanceError):
            measurement.result = "tails"

    def test_support_relations_are_immutable(self):
        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            basis=("observation",),
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

    def test_hash_chain_detects_mutation(self):
        self.branch()

        self.assertTrue(self.ledger.verify())

        self.ledger._records[0]["payload"][
            "name"
        ] = "altered"

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_distinction_records(self):
        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "distinction"
                and record["payload"]["distinction_id"]
                == self.outcome_distinction.distinction_id
            ):
                record["payload"]["specification"] = "altered"
                break

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_measurement_records(self):
        measurement = self.ledger.record_measurement(
            result="heads",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "measurement"
                and record["payload"]["measurement_id"]
                == measurement.measurement_id
            ):
                record["payload"]["result"] = "altered"
                break

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_support_records(self):
        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            basis=("observation",),
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

    def test_jsonl_export_retains_records(self):
        self.branch()

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ledger.jsonl"
            self.ledger.export_jsonl(target)

            records = [
                json.loads(line)
                for line in target.read_text(
                    encoding="utf-8"
                ).splitlines()
            ]

        self.assertEqual(
            len(records),
            len(self.ledger.records),
        )
        self.assertEqual(
            records[-1]["kind"],
            "transition",
        )

    def test_jsonl_export_includes_corrected_semantic_records(self):
        _, states = self.branch_states()

        measurement = self.ledger.record_measurement(
            result="protocol fit observed",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        first_support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis=("protocol fit",),
            measurement_ids=(measurement.measurement_id,),
        )

        second_support = self.ledger.record_support(
            conclusion_state_id=states[1].state_id,
            relation="supports",
            basis=("physical observation",),
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
            basis=("represented scope comparison",),
            best_supported_state_ids=(
                states[0].state_id,
            ),
        )

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ledger.jsonl"
            self.ledger.export_jsonl(target)

            records = [
                json.loads(line)
                for line in target.read_text(
                    encoding="utf-8"
                ).splitlines()
            ]

        kinds = [record["kind"] for record in records]

        self.assertIn("distinction", kinds)
        self.assertIn("measurement", kinds)
        self.assertIn("support", kinds)
        self.assertIn("comparison", kinds)


if __name__ == "__main__":
    unittest.main()
