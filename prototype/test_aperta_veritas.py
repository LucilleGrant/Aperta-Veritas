import json
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from aperta_veritas import (
    InquiryLedger,
    allocator,
    evaluator,
    generator,
)


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
            stopping_conditions=(
                "current test sequence complete",
            ),
            reopening_conditions=(
                "observe an excluded state",
            ),
        )

    def branch_states(self):
        edge = self.branch()
        states = [
            self.ledger.states[state_id]
            for state_id in edge.resulting_state_ids
        ]
        return edge, states

    def basis(self, description, kind="observation"):
        return self.ledger.record_basis(
            description=description,
            kind=kind,
        )

    def support_claim(
        self,
        state,
        *,
        description="represented observation",
        relation="supports",
        claim="The represented basis bears on the conclusion.",
        score=None,
        measurement_ids=(),
        distinction_ids=(),
        observations=(),
        logical_relations=(),
        residuals=(),
    ):
        basis = self.basis(description)

        support = self.ledger.record_support(
            conclusion_state_id=state.state_id,
            relation=relation,
            basis_ids=(basis.basis_id,),
            account=(
                "The represented basis is claimed to bear "
                "on whether the conclusion should be treated as true."
            ),
            measurement_ids=measurement_ids,
            distinction_ids=distinction_ids,
            observations=observations,
            logical_relations=logical_relations,
            residuals=residuals,
            score=score,
        )

        claim_record = self.ledger.record_support_claim(
            conclusion_state_id=state.state_id,
            support_relation_ids=(support.support_id,),
            claim=claim,
        )

        return basis, support, claim_record

    def allocation_fixture(self):
        basis = self.basis(
            "An unresolved physical branch can be examined.",
            kind="inquiry condition",
        )

        inquiry = self.ledger.record_inquiry_basis(
            state_id=self.origin.state_id,
            basis_ids=(basis.basis_id,),
            account=(
                "Further examination could occur under the "
                "represented unresolved condition."
            ),
            possible_tests=("repeat physical tosses",),
        )

        first = self.ledger.record_inquiry_operation(
            account="Test the unresolved physical branch.",
            target_state_ids=(self.origin.state_id,),
            operation="repeat physical tosses",
            inquiry_basis_ids=(inquiry.inquiry_basis_id,),
            requirements=("coin",),
            expected_outputs=("additional physical outcomes",),
        )

        second = self.ledger.record_inquiry_operation(
            account="Inspect reporting exclusions.",
            target_state_ids=(self.origin.state_id,),
            operation="inspect excluded protocol states",
            inquiry_basis_ids=(inquiry.inquiry_basis_id,),
            requirements=("protocol record",),
            expected_outputs=("represented exclusions",),
        )

        allocation_basis = self.ledger.record_allocation_basis(
            account="Allocate limited test time.",
            basis_ids=(basis.basis_id,),
            criteria=(
                "available test time",
                "expected information gain",
            ),
            conditions=("one operation can be active",),
            constraints=("finite test time",),
        )

        return (
            basis,
            inquiry,
            first,
            second,
            allocation_basis,
        )

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

    def test_compatibility_transition_records_generation_boundary(self):
        edge = self.branch()

        self.assertIsNotNone(edge.generation_id)
        self.assertIn(
            edge.generation_id,
            self.ledger.generations,
        )

        generation_event = self.ledger.generations[
            edge.generation_id
        ]

        self.assertIn(
            "candidate-generation process not represented",
            generation_event.known_exclusions,
        )
        self.assertEqual(
            generation_event.generator.operations,
            ("external candidate provision",),
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
                "Distinguish stable face, edge, "
                "and unresolved motion."
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
        self.assertEqual(
            len(self.ledger.support_claims),
            0,
        )

    def test_state_can_reference_distinction_and_measurement_separately(
        self,
    ):
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

    def test_basis_does_not_automatically_create_support(self):
        basis = self.basis(
            "The operator accepts the protocol because "
            "an authority requires it.",
            kind="authority",
        )

        self.assertIn(basis.basis_id, self.ledger.bases)
        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )
        self.assertEqual(
            len(self.ledger.support_claims),
            0,
        )

    def test_acceptance_basis_does_not_create_support(self):
        basis = self.basis(
            "Institutional policy requires this representation.",
            kind="policy",
        )

        acceptance = self.ledger.record_acceptance_basis(
            state_id=self.origin.state_id,
            basis_ids=(basis.basis_id,),
            account="The state is accepted because policy requires it.",
        )

        self.assertIn(
            acceptance.acceptance_id,
            self.ledger.acceptance_bases,
        )
        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )
        self.assertEqual(
            len(self.ledger.support_claims),
            0,
        )

    def test_inquiry_basis_does_not_create_support(self):
        basis = self.basis(
            "An unexplained edge case remains.",
            kind="anomaly",
        )

        inquiry = self.ledger.record_inquiry_basis(
            state_id=self.origin.state_id,
            basis_ids=(basis.basis_id,),
            account=(
                "Further examination could occur because "
                "the unresolved observation remains."
            ),
            possible_tests=("attempt stable edge landings",),
        )

        self.assertIn(
            inquiry.inquiry_basis_id,
            self.ledger.inquiry_bases,
        )
        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )
        self.assertEqual(
            len(self.ledger.support_claims),
            0,
        )

    def test_same_basis_can_participate_in_different_relations(self):
        basis = self.basis(
            "A protocol authority issued the rule.",
            kind="authority",
        )

        acceptance = self.ledger.record_acceptance_basis(
            state_id=self.origin.state_id,
            basis_ids=(basis.basis_id,),
            account="The operator accepts the rule.",
        )

        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="unresolved",
            basis_ids=(basis.basis_id,),
            account=(
                "Whether authority bears on the truth of the "
                "physical claim remains unresolved."
            ),
        )

        self.assertEqual(
            acceptance.basis_ids,
            support.basis_ids,
        )
        self.assertNotEqual(
            acceptance.acceptance_id,
            support.support_id,
        )

    def test_support_can_exist_without_measurement(self):
        _, states = self.branch_states()

        basis = self.basis(
            "Logical relation between protocol definition "
            "and permitted report labels.",
            kind="logical relation",
        )

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account=(
                "The protocol definition is claimed to support "
                "the conclusion about permitted labels."
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
            method=(
                "compare reports with protocol categories",
            ),
        )

        basis = self.basis(
            "Observed protocol consistency.",
            kind="observation",
        )

        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account=(
                "Observed consistency is claimed to support "
                "the bounded protocol conclusion."
            ),
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

    def test_support_requires_represented_basis(self):
        with self.assertRaises(ValueError):
            self.ledger.record_support(
                conclusion_state_id=self.origin.state_id,
                relation="supports",
                basis_ids=(),
                account="No represented basis was supplied.",
            )

    def test_support_rejects_unknown_basis(self):
        with self.assertRaises(KeyError):
            self.ledger.record_support(
                conclusion_state_id=self.origin.state_id,
                relation="supports",
                basis_ids=("missing_basis",),
                account="Unknown basis should not be accepted.",
            )

    def test_support_claim_is_separate_from_support_relation(self):
        _, states = self.branch_states()

        _, support, claim = self.support_claim(
            states[0],
            description="protocol definition",
        )

        self.assertIn(
            support.support_id,
            claim.support_relation_ids,
        )
        self.assertNotEqual(
            support.support_id,
            claim.support_claim_id,
        )
        self.assertFalse(hasattr(claim, "truth"))

    def test_support_claim_rejects_relation_for_other_conclusion(self):
        _, states = self.branch_states()

        _, support, _ = self.support_claim(
            states[0],
            description="protocol definition",
        )

        with self.assertRaises(ValueError):
            self.ledger.record_support_claim(
                conclusion_state_id=states[1].state_id,
                support_relation_ids=(support.support_id,),
                claim=(
                    "A relation concerning another conclusion "
                    "must not be silently reassigned."
                ),
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

        basis = self.basis(
            "Ordinary observed outcomes.",
            kind="observation",
        )

        support = self.ledger.record_support(
            conclusion_state_id=state.state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account=(
                "Ordinary observations are claimed to support "
                "the proposition under represented conditions."
            ),
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
        self.assertEqual(
            len(self.ledger.support_claims),
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

    def test_explicit_generation_is_distinct_from_evaluation(self):
        candidate_generator = generator(
            "Generate protocol and physical interpretations.",
            operations=("branch represented interpretations",),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            source_state_ids=(self.origin.state_id,),
        )

        generation_event = self.ledger.generate(
            source_state_ids=(self.origin.state_id,),
            candidates=(
                {
                    "object": "protocol",
                    "representation": "Recorded output is binary.",
                    "status": "tested",
                },
                {
                    "object": "physical toss",
                    "representation": (
                        "Physical outcomes may exceed labels."
                    ),
                    "status": "unresolved",
                },
            ),
            generator=candidate_generator,
            operation="generate alternative interpretations",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        self.assertEqual(
            len(generation_event.generated_state_ids),
            2,
        )
        self.assertEqual(len(self.ledger.transitions), 0)

        for state_id in generation_event.generated_state_ids:
            self.assertFalse(
                self.ledger.states[state_id].active
            )

    def test_generation_requires_source_state(self):
        candidate_generator = generator(
            "Generate a candidate.",
            operations=("generate",),
        )

        with self.assertRaises(ValueError):
            self.ledger.generate(
                source_state_ids=(),
                candidates=(
                    {
                        "object": "candidate",
                        "representation": "A candidate.",
                    },
                ),
                generator=candidate_generator,
                operation="generate",
            )

    def test_generation_requires_candidate(self):
        candidate_generator = generator(
            "Generate candidates.",
            operations=("generate",),
            source_state_ids=(self.origin.state_id,),
        )

        with self.assertRaises(ValueError):
            self.ledger.generate(
                source_state_ids=(self.origin.state_id,),
                candidates=(),
                generator=candidate_generator,
                operation="generate",
            )

    def test_generation_can_preserve_possible_unrepresented_alternatives(
        self,
    ):
        candidate_generator = generator(
            "Generate known interpretations.",
            operations=("generate represented alternatives",),
            source_state_ids=(self.origin.state_id,),
            constraints=("current vocabulary",),
        )

        generation_event = self.ledger.generate(
            source_state_ids=(self.origin.state_id,),
            candidates=(
                {
                    "object": "protocol",
                    "representation": "Recorded output is binary.",
                },
            ),
            generator=candidate_generator,
            operation="generate represented alternative",
            known_exclusions=("unmodeled physical states",),
            unrepresented_alternatives_possible=True,
        )

        self.assertTrue(
            generation_event.unrepresented_alternatives_possible
        )
        self.assertIn(
            "unmodeled physical states",
            generation_event.known_exclusions,
        )

    def test_generated_selection_preserves_unselected_candidate(self):
        candidate_generator = generator(
            "Generate two interpretations.",
            operations=("branch interpretations",),
            source_state_ids=(self.origin.state_id,),
        )

        generation_event = self.ledger.generate(
            source_state_ids=(self.origin.state_id,),
            candidates=(
                {
                    "object": "protocol",
                    "representation": "Recorded output is binary.",
                    "status": "tested",
                },
                {
                    "object": "physical toss",
                    "representation": (
                        "Physical outcomes may exceed labels."
                    ),
                    "status": "unresolved",
                },
            ),
            generator=candidate_generator,
            operation="generate alternatives",
        )

        selected = generation_event.generated_state_ids[0]

        transition = self.ledger.transition_generated(
            generation_id=generation_event.generation_id,
            operation="select represented candidate",
            transformation="evaluate generated alternatives",
            evaluator=self.selector,
            selected_state_ids=(selected,),
        )

        self.assertEqual(
            transition.generation_id,
            generation_event.generation_id,
        )
        self.assertEqual(
            len(transition.inactive_state_ids),
            1,
        )

        inactive = self.ledger.states[
            transition.inactive_state_ids[0]
        ]
        self.assertFalse(inactive.active)

    def test_selection_rejects_state_outside_generation(self):
        candidate_generator = generator(
            "Generate one candidate.",
            operations=("generate",),
            source_state_ids=(self.origin.state_id,),
        )

        generation_event = self.ledger.generate(
            source_state_ids=(self.origin.state_id,),
            candidates=(
                {
                    "object": "candidate",
                    "representation": "Generated candidate.",
                },
            ),
            generator=candidate_generator,
            operation="generate",
        )

        external = self.ledger.encounter(
            object="external",
            representation="Not generated by this event.",
        )

        with self.assertRaises(ValueError):
            self.ledger.transition_generated(
                generation_id=generation_event.generation_id,
                operation="select",
                transformation="evaluate",
                evaluator=self.selector,
                selected_state_ids=(external.state_id,),
            )

    def test_inquiry_basis_can_preserve_inactive_branch(self):
        edge = self.branch()
        inactive = self.ledger.states[
            edge.inactive_state_ids[0]
        ]

        basis = self.basis(
            "Excluded-state frequency remains unknown.",
            kind="unresolved question",
        )

        inquiry = self.ledger.record_inquiry_basis(
            state_id=inactive.state_id,
            basis_ids=(basis.basis_id,),
            account=(
                "Further examination of the inactive branch could occur "
                "because an unresolved observation remains."
            ),
            possible_tests=("repeat physical tosses",),
            reopening_conditions=(
                "new observation distinguishes excluded states",
            ),
        )

        self.assertFalse(inactive.active)
        self.assertIn(
            inquiry.inquiry_basis_id,
            self.ledger.inquiry_bases,
        )
        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )

    def test_inquiry_basis_does_not_create_priority_or_allocation(self):
        basis = self.basis(
            "An unresolved observation remains.",
            kind="anomaly",
        )

        inquiry = self.ledger.record_inquiry_basis(
            state_id=self.origin.state_id,
            basis_ids=(basis.basis_id,),
            account="Further examination could occur.",
        )

        self.assertIn(
            inquiry.inquiry_basis_id,
            self.ledger.inquiry_bases,
        )
        self.assertEqual(len(self.ledger.inquiry_priorities), 0)
        self.assertEqual(len(self.ledger.resource_allocations), 0)

    def test_inquiry_operation_does_not_create_priority_or_allocation(self):
        _, _, first, _, _ = self.allocation_fixture()

        self.assertIn(
            first.inquiry_operation_id,
            self.ledger.inquiry_operations,
        )
        self.assertEqual(len(self.ledger.inquiry_priorities), 0)
        self.assertEqual(len(self.ledger.resource_allocations), 0)

    def test_allocation_basis_does_not_create_support(self):
        _, _, _, _, allocation_basis = self.allocation_fixture()

        self.assertIn(
            allocation_basis.allocation_basis_id,
            self.ledger.allocation_bases,
        )
        self.assertEqual(len(self.ledger.support_relations), 0)
        self.assertEqual(len(self.ledger.support_claims), 0)

    def test_priority_does_not_allocate_resources(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        priority = self.ledger.record_inquiry_priority(
            inquiry_operation_ids=(
                first.inquiry_operation_id,
                second.inquiry_operation_id,
            ),
            allocation_basis_id=allocation_basis.allocation_basis_id,
            ordered_operation_ids=(
                first.inquiry_operation_id,
                second.inquiry_operation_id,
            ),
            account="Prefer the lower-cost represented test first.",
        )

        self.assertIn(
            priority.inquiry_priority_id,
            self.ledger.inquiry_priorities,
        )
        self.assertEqual(len(self.ledger.resource_allocations), 0)
        self.assertEqual(len(self.ledger.activations), 0)

    def test_resource_allocation_does_not_create_support(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        represented_allocator = allocator(
            "Allocate finite test time.",
            criteria=("available test time",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        allocation = self.ledger.allocate_resources(
            inquiry_operation_ids=(
                first.inquiry_operation_id,
                second.inquiry_operation_id,
            ),
            allocator=represented_allocator,
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
            assigned_resources={
                first.inquiry_operation_id: {
                    "minutes": 10.0,
                },
            },
            unallocated_operation_ids=(
                second.inquiry_operation_id,
            ),
        )

        self.assertIn(
            allocation.resource_allocation_id,
            self.ledger.resource_allocations,
        )
        self.assertEqual(len(self.ledger.support_relations), 0)
        self.assertEqual(len(self.ledger.support_claims), 0)

    def test_unallocated_operation_is_preserved_not_rejected(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        represented_allocator = allocator(
            "Allocate one available test slot.",
            criteria=("one available slot",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        allocation = self.ledger.allocate_resources(
            inquiry_operation_ids=(
                first.inquiry_operation_id,
                second.inquiry_operation_id,
            ),
            allocator=represented_allocator,
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
            assigned_resources={
                first.inquiry_operation_id: {
                    "slots": 1.0,
                },
            },
            unallocated_operation_ids=(
                second.inquiry_operation_id,
            ),
        )

        self.assertIn(
            second.inquiry_operation_id,
            allocation.unallocated_operation_ids,
        )
        self.assertIn(
            second.inquiry_operation_id,
            self.ledger.inquiry_operations,
        )
        self.assertFalse(
            hasattr(allocation, "rejected_operation_ids")
        )

    def test_open_inquiry_is_distinct_from_active_inquiry(self):
        _, inquiry, first, _, _ = self.allocation_fixture()

        self.assertIn(
            inquiry.inquiry_basis_id,
            self.ledger.inquiry_bases,
        )
        self.assertIn(
            first.inquiry_operation_id,
            self.ledger.inquiry_operations,
        )
        self.assertEqual(len(self.ledger.activations), 0)

    def test_activation_requires_represented_resource_allocation(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        represented_allocator = allocator(
            "Allocate one operation.",
            criteria=("available resource",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        allocation = self.ledger.allocate_resources(
            inquiry_operation_ids=(
                first.inquiry_operation_id,
                second.inquiry_operation_id,
            ),
            allocator=represented_allocator,
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
            assigned_resources={
                first.inquiry_operation_id: {
                    "minutes": 5.0,
                },
            },
            unallocated_operation_ids=(
                second.inquiry_operation_id,
            ),
        )

        with self.assertRaises(ValueError):
            self.ledger.activate_inquiry(
                inquiry_operation_ids=(
                    second.inquiry_operation_id,
                ),
                resource_allocation_id=(
                    allocation.resource_allocation_id
                ),
                account=(
                    "Attempt to activate an unallocated operation."
                ),
            )

    def test_activation_does_not_create_support_or_evaluation(self):
        _, _, first, _, allocation_basis = self.allocation_fixture()

        represented_allocator = allocator(
            "Allocate test time.",
            criteria=("available test time",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        allocation = self.ledger.allocate_resources(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            allocator=represented_allocator,
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
            assigned_resources={
                first.inquiry_operation_id: {
                    "minutes": 5.0,
                },
            },
        )

        activation = self.ledger.activate_inquiry(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            resource_allocation_id=(
                allocation.resource_allocation_id
            ),
            account="Begin the allocated inquiry operation.",
        )

        self.assertTrue(activation.active)
        self.assertEqual(len(self.ledger.support_relations), 0)
        self.assertEqual(len(self.ledger.support_claims), 0)
        self.assertEqual(len(self.ledger.transitions), 0)

    def test_deactivation_preserves_operation_and_reopening_conditions(
        self,
    ):
        _, _, first, _, allocation_basis = self.allocation_fixture()

        represented_allocator = allocator(
            "Allocate test time.",
            criteria=("available test time",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        allocation = self.ledger.allocate_resources(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            allocator=represented_allocator,
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
            assigned_resources={
                first.inquiry_operation_id: {
                    "minutes": 5.0,
                },
            },
        )

        self.ledger.activate_inquiry(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            resource_allocation_id=(
                allocation.resource_allocation_id
            ),
            account="Begin inquiry.",
        )

        deactivation = self.ledger.deactivate_inquiry(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            resource_allocation_id=(
                allocation.resource_allocation_id
            ),
            account="Current resource window ended.",
            stopping_conditions=("test time exhausted",),
            reopening_conditions=(
                "new test time becomes available",
            ),
        )

        self.assertFalse(deactivation.active)
        self.assertIn(
            first.inquiry_operation_id,
            self.ledger.inquiry_operations,
        )
        self.assertIn(
            "new test time becomes available",
            deactivation.reopening_conditions,
        )

    def test_priority_requires_exact_operation_ordering(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        with self.assertRaises(ValueError):
            self.ledger.record_inquiry_priority(
                inquiry_operation_ids=(
                    first.inquiry_operation_id,
                    second.inquiry_operation_id,
                ),
                allocation_basis_id=(
                    allocation_basis.allocation_basis_id
                ),
                ordered_operation_ids=(
                    first.inquiry_operation_id,
                ),
                account=(
                    "Incomplete ordering must not be accepted."
                ),
            )

    def test_allocation_priority_must_match_operation_set(self):
        _, _, first, second, allocation_basis = self.allocation_fixture()

        priority = self.ledger.record_inquiry_priority(
            inquiry_operation_ids=(first.inquiry_operation_id,),
            allocation_basis_id=(
                allocation_basis.allocation_basis_id
            ),
            ordered_operation_ids=(first.inquiry_operation_id,),
            account="Priority for one represented operation.",
        )

        represented_allocator = allocator(
            "Allocate across two operations.",
            criteria=("available test time",),
            allocation_basis_ids=(
                allocation_basis.allocation_basis_id,
            ),
        )

        with self.assertRaises(ValueError):
            self.ledger.allocate_resources(
                inquiry_operation_ids=(
                    first.inquiry_operation_id,
                    second.inquiry_operation_id,
                ),
                allocator=represented_allocator,
                allocation_basis_ids=(
                    allocation_basis.allocation_basis_id,
                ),
                assigned_resources={
                    first.inquiry_operation_id: {
                        "minutes": 5.0,
                    },
                },
                inquiry_priority_id=(
                    priority.inquiry_priority_id
                ),
            )

    def test_comparison_requires_explicit_basis(self):
        _, states = self.branch_states()

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_claim_ids=(),
                basis=(),
            )

    def test_comparison_does_not_require_measurement(self):
        _, states = self.branch_states()

        _, _, first_claim = self.support_claim(
            states[0],
            description="protocol definition",
            logical_relations=(
                "binary output follows from protocol rule",
            ),
        )

        _, _, second_claim = self.support_claim(
            states[1],
            description="observed edge case",
            observations=(
                "coin temporarily rested on edge",
            ),
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(
                first_claim.support_claim_id,
                second_claim.support_claim_id,
            ),
            basis=(
                "scope of each conclusion relative "
                "to represented support",
            ),
            criteria=("represented explanatory scope",),
            conditions=("current observations only",),
        )

        self.assertEqual(comparison.measurement_ids, ())
        self.assertTrue(comparison.basis)

    def test_comparison_preserves_comparison_set(self):
        _, states = self.branch_states()

        _, _, first_claim = self.support_claim(
            states[0],
            description="protocol fit",
            score=0.9,
        )

        _, _, second_claim = self.support_claim(
            states[1],
            description="physical coverage",
            score=0.7,
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(
                first_claim.support_claim_id,
                second_claim.support_claim_id,
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

    def test_unranked_does_not_assert_intrinsic_incommensurability(
        self,
    ):
        _, states = self.branch_states()

        _, _, first_claim = self.support_claim(
            states[0],
            description="protocol definition",
        )

        _, _, second_claim = self.support_claim(
            states[1],
            description="physical observation",
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(
                first_claim.support_claim_id,
                second_claim.support_claim_id,
            ),
            basis=(
                "Current represented relations do not "
                "support a ranking."
            ),
            unranked_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            unresolved_relations=(
                "A future comparison basis may alter ranking.",
            ),
        )

        self.assertEqual(
            comparison.best_supported_state_ids,
            (),
        )
        self.assertEqual(
            set(comparison.unranked_state_ids),
            {
                states[0].state_id,
                states[1].state_id,
            },
        )
        self.assertFalse(
            hasattr(comparison, "incomparable_state_ids")
        )

    def test_comparison_rejects_external_unranked_state(self):
        _, states = self.branch_states()

        external = self.ledger.encounter(
            object="external alternative",
            representation="Another possibility.",
        )

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_claim_ids=(),
                basis=("represented comparison",),
                unranked_state_ids=(external.state_id,),
            )

    def test_best_supported_is_not_truth_certificate(self):
        _, states = self.branch_states()

        _, _, first_claim = self.support_claim(
            states[0],
            description="bounded protocol test",
            score=1.0,
        )

        _, _, second_claim = self.support_claim(
            states[1],
            description="partial physical observations",
            score=0.5,
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(
                first_claim.support_claim_id,
                second_claim.support_claim_id,
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

        _, support, claim = self.support_claim(
            states[0],
            description="bounded test",
            score=1.0,
        )

        self.assertEqual(support.score, 1.0)
        self.assertFalse(hasattr(support, "truth"))
        self.assertFalse(
            hasattr(support, "definitive_truth")
        )
        self.assertFalse(hasattr(claim, "truth"))

    def test_comparison_rejects_external_best_supported_state(self):
        _, states = self.branch_states()

        external = self.ledger.encounter(
            object="external alternative",
            representation="Another possibility.",
        )

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_claim_ids=(),
                basis=("represented test relation",),
                best_supported_state_ids=(
                    external.state_id,
                ),
            )

    def test_comparison_rejects_claim_for_external_conclusion(self):
        _, states = self.branch_states()

        external = self.ledger.encounter(
            object="external alternative",
            representation="Another possibility.",
        )

        _, _, external_claim = self.support_claim(
            external,
            description="external test",
        )

        with self.assertRaises(ValueError):
            self.ledger.compare(
                conclusion_state_ids=(
                    states[0].state_id,
                    states[1].state_id,
                ),
                support_claim_ids=(
                    external_claim.support_claim_id,
                ),
                basis=("represented comparison",),
            )

    def test_recontextualization_preserves_prior_states(self):
        _, states = self.branch_states()

        new_distinction = self.ledger.record_distinction(
            name="report versus physical state",
            specification=(
                "Distinguish protocol output from "
                "physical configuration."
            ),
        )

        before = {
            state.state_id: state
            for state in states
        }

        event = self.ledger.recontextualize(
            prior_state_ids=tuple(before),
            distinction_ids=(new_distinction.distinction_id,),
            relation=(
                "The protocol and physical claims concern "
                "different represented relations."
            ),
        )

        self.assertIn(
            event.recontextualization_id,
            self.ledger.recontextualizations,
        )

        for state_id, original_state in before.items():
            self.assertIs(
                self.ledger.states[state_id],
                original_state,
            )

    def test_recontextualization_can_create_new_state(self):
        _, states = self.branch_states()

        new_distinction = self.ledger.record_distinction(
            name="projection relation",
            specification=(
                "Distinguish an object's represented projection "
                "from a claim about the whole object."
            ),
        )

        event = self.ledger.recontextualize(
            prior_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            distinction_ids=(new_distinction.distinction_id,),
            relation=(
                "Earlier representations can be related "
                "under the new distinction."
            ),
            resulting_state={
                "object": "recontextualized toss model",
                "representation": (
                    "Protocol output and physical outcome "
                    "are distinct represented relations."
                ),
                "status": "untested",
            },
        )

        self.assertIsNotNone(event.resulting_state_id)
        self.assertIn(
            event.resulting_state_id,
            self.ledger.states,
        )

        result = self.ledger.states[
            event.resulting_state_id
        ]

        self.assertEqual(
            set(result.parent_state_ids),
            {
                states[0].state_id,
                states[1].state_id,
            },
        )

    def test_recontextualization_does_not_create_support(self):
        _, states = self.branch_states()

        new_distinction = self.ledger.record_distinction(
            name="new relational distinction",
            specification=(
                "A later distinction exposes a possible relation."
            ),
        )

        self.ledger.recontextualize(
            prior_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            distinction_ids=(new_distinction.distinction_id,),
            relation="A newly representable relation.",
        )

        self.assertEqual(
            len(self.ledger.support_relations),
            0,
        )
        self.assertEqual(
            len(self.ledger.support_claims),
            0,
        )

    def test_recontextualization_requires_new_represented_distinction(
        self,
    ):
        with self.assertRaises(KeyError):
            self.ledger.recontextualize(
                prior_state_ids=(self.origin.state_id,),
                distinction_ids=("missing_distinction",),
                relation="An unsupported relation.",
            )

    def test_recursive_audit_exposes_generative_architecture(self):
        edge, states = self.branch_states()

        measurement = self.ledger.record_measurement(
            result="binary protocol output observed",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        basis = self.basis(
            "Protocol observation.",
            kind="observation",
        )

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account=(
                "The observation is claimed to support "
                "the bounded protocol conclusion."
            ),
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
            measurement_ids=(measurement.measurement_id,),
        )

        support_claim = self.ledger.record_support_claim(
            conclusion_state_id=states[0].state_id,
            support_relation_ids=(support.support_id,),
            claim=(
                "The protocol observation bears on the "
                "bounded protocol conclusion."
            ),
        )

        inquiry_basis_record = self.ledger.record_inquiry_basis(
            state_id=states[1].state_id,
            basis_ids=(basis.basis_id,),
            account=(
                "The physical branch remains open "
                "for further examination."
            ),
        )

        comparison = self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(
                support_claim.support_claim_id,
            ),
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
            basis_ids=(basis.basis_id,),
            inquiry_basis_ids=(
                inquiry_basis_record.inquiry_basis_id,
            ),
            support_ids=(support.support_id,),
            support_claim_ids=(
                support_claim.support_claim_id,
            ),
            comparison_ids=(comparison.comparison_id,),
            generation_ids=(edge.generation_id,),
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
            basis.basis_id,
            audit["basis_ids"],
        )
        self.assertIn(
            inquiry_basis_record.inquiry_basis_id,
            audit["inquiry_basis_ids"],
        )
        self.assertIn(
            support.support_id,
            audit["support_ids"],
        )
        self.assertIn(
            support_claim.support_claim_id,
            audit["support_claim_ids"],
        )
        self.assertIn(
            comparison.comparison_id,
            audit["comparison_ids"],
        )
        self.assertIn(
            edge.generation_id,
            audit["generation_ids"],
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

    def test_bases_are_immutable(self):
        basis = self.basis("Observation.")

        with self.assertRaises(FrozenInstanceError):
            basis.description = "changed"

    def test_support_relations_are_immutable(self):
        basis = self.basis("Observation.")

        support = self.ledger.record_support(
            conclusion_state_id=self.origin.state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account="Observation is claimed to support conclusion.",
        )

        with self.assertRaises(FrozenInstanceError):
            support.relation = "contradicts"

    def test_support_claims_are_immutable(self):
        _, _, claim = self.support_claim(
            self.origin,
            description="observation",
        )

        with self.assertRaises(FrozenInstanceError):
            claim.claim = "changed"

    def test_beliefs_are_immutable(self):
        belief = self.ledger.record_belief(
            proposition="A proposition",
            holder="agent",
        )

        with self.assertRaises(FrozenInstanceError):
            belief.confidence = 1.0

    def test_generation_records_are_immutable(self):
        candidate_generator = generator(
            "Generate candidate.",
            operations=("generate",),
            source_state_ids=(self.origin.state_id,),
        )

        generation_event = self.ledger.generate(
            source_state_ids=(self.origin.state_id,),
            candidates=(
                {
                    "object": "candidate",
                    "representation": "Candidate representation.",
                },
            ),
            generator=candidate_generator,
            operation="generate",
        )

        with self.assertRaises(FrozenInstanceError):
            generation_event.operation = "changed"

    def test_hash_chain_detects_mutation(self):
        self.branch()

        self.assertTrue(self.ledger.verify())

        self.ledger._records[0]["payload"][
            "name"
        ] = "altered"

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_generation_records(self):
        edge = self.branch()

        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "generation"
                and record["payload"]["generation_id"]
                == edge.generation_id
            ):
                record["payload"]["operation"] = "altered"
                break

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_support_claim_records(self):
        _, _, claim = self.support_claim(
            self.origin,
            description="observation",
        )

        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "support_claim"
                and record["payload"]["support_claim_id"]
                == claim.support_claim_id
            ):
                record["payload"]["claim"] = "altered"
                break

        self.assertFalse(self.ledger.verify())

    def test_hash_chain_covers_recontextualization_records(self):
        distinction = self.ledger.record_distinction(
            name="later distinction",
            specification="Expose a later relation.",
        )

        event = self.ledger.recontextualize(
            prior_state_ids=(self.origin.state_id,),
            distinction_ids=(distinction.distinction_id,),
            relation="A later relation.",
        )

        self.assertTrue(self.ledger.verify())

        for record in self.ledger._records:
            if (
                record["kind"] == "recontextualization"
                and record["payload"][
                    "recontextualization_id"
                ]
                == event.recontextualization_id
            ):
                record["payload"]["relation"] = "altered"
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

    def test_jsonl_export_includes_generative_semantic_records(self):
        _, states = self.branch_states()

        measurement = self.ledger.record_measurement(
            result="protocol fit observed",
            distinction_ids=(
                self.outcome_distinction.distinction_id,
            ),
        )

        basis = self.basis(
            "Protocol fit.",
            kind="observation",
        )

        support = self.ledger.record_support(
            conclusion_state_id=states[0].state_id,
            relation="supports",
            basis_ids=(basis.basis_id,),
            account=(
                "Protocol fit is claimed to support "
                "the bounded conclusion."
            ),
            measurement_ids=(measurement.measurement_id,),
        )

        claim = self.ledger.record_support_claim(
            conclusion_state_id=states[0].state_id,
            support_relation_ids=(support.support_id,),
            claim="Protocol fit bears on the bounded conclusion.",
        )

        inquiry_basis_record = self.ledger.record_inquiry_basis(
            state_id=states[1].state_id,
            basis_ids=(basis.basis_id,),
            account=(
                "The unresolved physical branch remains "
                "available for inquiry."
            ),
        )

        distinction = self.ledger.record_distinction(
            name="scope relation",
            specification=(
                "Distinguish protocol scope from physical scope."
            ),
        )

        self.ledger.recontextualize(
            prior_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            distinction_ids=(distinction.distinction_id,),
            relation=(
                "The retained branches concern different scopes."
            ),
        )

        self.ledger.compare(
            conclusion_state_ids=(
                states[0].state_id,
                states[1].state_id,
            ),
            support_claim_ids=(claim.support_claim_id,),
            basis=("represented scope comparison",),
            unranked_state_ids=(
                states[0].state_id,
                states[1].state_id,
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
        self.assertIn("basis", kinds)
        self.assertIn("inquiry_basis", kinds)
        self.assertIn("support_relation", kinds)
        self.assertIn("support_claim", kinds)
        self.assertIn("generation", kinds)
        self.assertIn("recontextualization", kinds)
        self.assertIn("comparison", kinds)


if __name__ == "__main__":
    unittest.main()
