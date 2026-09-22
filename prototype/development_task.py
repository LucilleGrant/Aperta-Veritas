"""First matched development task for the comparative experiment."""

from __future__ import annotations

from dataclasses import asdict
import json
from typing import Any

from experiment import (
    Candidate,
    ExperimentTask,
    FixedEvaluationArchitecture,
    FixedOrderAllocator,
    FixedScoreEvaluator,
    OpenInquiryRevision,
    OpenRecursiveInquiryArchitecture,
    ResourceBudget,
    RevisableEvaluationArchitecture,
    RevisableScoreEvaluator,
    ScriptedOpenInquiry,
    StaticGenerator,
)


TARGET_CANDIDATE_ID = "candidate_protocol_physical_split"
TARGET_DISTINCTION = "protocol output versus physical state"


def run_missing_distinction_task() -> dict[str, Any]:
    """Run one engineering-check task through Architectures A, B, and C."""

    task = ExperimentTask(
        task_id="missing_distinction_development_1",
        initial_representation=(
            "A binary protocol output is reported as a conclusion about "
            "the physical state of an event."
        ),
        resource_budget=ResourceBudget(
            max_candidates=3,
            max_evaluations=4,
        ),
        stopping_conditions=("development procedure complete",),
    )
    initial_candidates = (
        Candidate(
            "candidate_accept_report",
            "Treat the protocol output as the physical conclusion.",
        ),
        Candidate(
            "candidate_reject_report",
            "Reject the protocol output as the physical conclusion.",
        ),
    )
    generator = StaticGenerator(
        generator_id="matched_initial_generator",
        candidates=initial_candidates,
    )
    allocator = FixedOrderAllocator(
        allocator_id="matched_initial_allocator",
        basis=("supplied order", "matched resource ceiling"),
        max_active=1,
    )
    fixed_evaluator = FixedScoreEvaluator(
        evaluator_id="matched_fixed_evaluator",
        criteria=("fit under the initial representation",),
        scores={
            "candidate_accept_report": 0.4,
            "candidate_reject_report": 0.3,
        },
    )

    architecture_a = FixedEvaluationArchitecture(
        generator=generator,
        allocator=allocator,
        evaluator=fixed_evaluator,
    )
    architecture_b = RevisableEvaluationArchitecture(
        generator=generator,
        allocator=allocator,
        evaluator=RevisableScoreEvaluator(
            evaluator_id="matched_revisable_evaluator",
            initial_criteria=("fit under the initial representation",),
            initial_scores={
                "candidate_accept_report": 0.4,
            },
            revised_criteria=("internal consistency of protocol report",),
            revised_scores={
                "candidate_accept_report": 0.6,
            },
            revision_trigger_score=0.5,
        ),
    )
    revision = OpenInquiryRevision(
        revision_id="missing_distinction_revision_1",
        added_candidates=(
            Candidate(
                TARGET_CANDIDATE_ID,
                (
                    "Treat protocol output and physical state as distinct "
                    "claims requiring a represented relation."
                ),
                provenance=(TARGET_DISTINCTION,),
            ),
        ),
        reactivate_candidate_ids=("candidate_reject_report",),
        distinctions=(TARGET_DISTINCTION,),
        generation_account=(
            "The protocol and physical-state distinction generated a third "
            "candidate outside the initial binary framing."
        ),
        allocation_basis=(
            "activate candidates bearing on the newly represented relation",
        ),
        evaluation_criteria=(
            "fit after separating protocol output from physical state",
        ),
        evaluation_scores={
            "candidate_accept_report": 0.2,
            "candidate_reject_report": 0.3,
            TARGET_CANDIDATE_ID: 0.9,
        },
        reopening_conditions=(
            "new observation relates protocol output to physical state",
        ),
    )
    architecture_c = OpenRecursiveInquiryArchitecture(
        generator=generator,
        allocator=allocator,
        evaluator=fixed_evaluator,
        controller=ScriptedOpenInquiry(
            controller_id="matched_open_controller",
            revision=revision,
            trigger_score=0.5,
        ),
    )

    runs = {
        "A": architecture_a.run(task),
        "B": architecture_b.run(task),
        "C": architecture_c.run(task),
    }
    return {
        "status": "engineering check, not research evidence",
        "task_id": task.task_id,
        "target_candidate_id": TARGET_CANDIDATE_ID,
        "target_distinction": TARGET_DISTINCTION,
        "resource_budget": asdict(task.resource_budget),
        "architectures": {
            label: {
                "architecture_id": result.architecture_id,
                "generated_candidate_ids": list(
                    result.generation.candidate_ids
                ),
                "selected_candidate_ids": list(
                    result.selected_candidate_ids
                ),
                "target_candidate_recovered": (
                    TARGET_CANDIDATE_ID
                    in result.generation.candidate_ids
                ),
                "evaluations_performed": result.evaluations_performed,
                "stop_reason": result.stop_reason,
            }
            for label, result in runs.items()
        },
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_missing_distinction_task(),
            indent=2,
            sort_keys=True,
        )
    )
