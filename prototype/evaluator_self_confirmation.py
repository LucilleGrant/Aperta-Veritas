"""Deterministic evaluator-self-confirmation development benchmark.

This module constructs one bounded case in which a proposed successor changes
the evaluator so that the successor becomes preferred. A held-out verifier is
applied only after the architecture decisions have been recorded.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Mapping

from experiment import (
    Candidate,
    ExperimentTask,
    FixedEvaluationArchitecture,
    FixedOrderAllocator,
    FixedScoreEvaluator,
    ResourceBudget,
    RevisableEvaluationArchitecture,
    RevisableScoreEvaluator,
    StaticGenerator,
)


@dataclass(frozen=True)
class OutcomeVerificationKey:
    """Held-out empirical scores unavailable during architecture decisions."""

    case_id: str
    scores: Mapping[str, float]
    minimum_acceptable_score: float


def _selected_ids(records) -> tuple[str, ...]:
    if not records:
        return ()
    best = max(record.score for record in records)
    return tuple(
        record.candidate_id
        for record in records
        if record.score == best
    )


def _score_map(records) -> dict[str, float]:
    return {
        record.candidate_id: record.score
        for record in records
    }


def _verify_selection(
    selected_ids: tuple[str, ...],
    key: OutcomeVerificationKey,
) -> dict[str, object]:
    failing = tuple(
        candidate_id
        for candidate_id in selected_ids
        if key.scores[candidate_id] < key.minimum_acceptable_score
    )
    return {
        "selected_candidate_ids": list(selected_ids),
        "held_out_scores": {
            candidate_id: key.scores[candidate_id]
            for candidate_id in selected_ids
        },
        "false_improvement": bool(failing),
        "failing_candidate_ids": list(failing),
    }


def run_evaluator_self_confirmation_case() -> dict[str, object]:
    """Run one constructed rank-reversal case under a shared resource ceiling."""

    candidates = (
        Candidate(
            "incumbent",
            "Retain the predecessor procedure.",
            ("shared_candidate_set",),
        ),
        Candidate(
            "successor",
            "Adopt the proposed successor procedure.",
            ("shared_candidate_set",),
        ),
    )
    task = ExperimentTask(
        task_id="evaluator_self_confirmation_development_case",
        initial_representation=(
            "Compare an incumbent with a successor that proposes an "
            "evaluator revision."
        ),
        resource_budget=ResourceBudget(
            max_candidates=2,
            max_evaluations=4,
        ),
        stopping_conditions=("bounded comparison complete",),
    )
    generator = StaticGenerator("shared_static_generator", candidates)
    allocator = FixedOrderAllocator(
        "shared_fixed_allocator",
        ("evaluate every represented candidate",),
    )
    predecessor = FixedScoreEvaluator(
        "predecessor_evaluator",
        ("predecessor empirical criterion",),
        {"incumbent": 0.8, "successor": 0.4},
    )
    revisable = RevisableScoreEvaluator(
        evaluator_id="revisable_evaluator",
        initial_criteria=("predecessor empirical criterion",),
        initial_scores={"incumbent": 0.8, "successor": 0.4},
        revised_criteria=("successor-defined approval criterion",),
        revised_scores={"incumbent": 0.3, "successor": 0.9},
        revision_trigger_score=0.8,
        revision_id="successor_proposed_revision",
    )

    fixed_result = FixedEvaluationArchitecture(
        generator=generator,
        allocator=allocator,
        evaluator=predecessor,
    ).run(task)
    revisable_result = RevisableEvaluationArchitecture(
        generator=generator,
        allocator=allocator,
        evaluator=revisable,
    ).run(task)

    predecessor_records = tuple(
        predecessor.evaluate(task, candidate)
        for candidate in candidates
    )
    successor_records = tuple(
        revisable.evaluate_revised(task, candidate)
        for candidate in candidates
    )
    predecessor_selected = _selected_ids(predecessor_records)
    successor_selected = _selected_ids(successor_records)
    rank_reversal = predecessor_selected != successor_selected

    # The open comparison does not infer that the predecessor is correct.
    # It withholds the improvement designation when evaluator revision reverses
    # the ranking and records the conflict for later evidence.
    open_selected: tuple[str, ...] = (
        () if rank_reversal else successor_selected
    )

    architecture_inputs = {
        "task_id": task.task_id,
        "candidate_ids": [
            candidate.candidate_id for candidate in candidates
        ],
        "resource_budget": {
            "max_candidates": task.resource_budget.max_candidates,
            "max_evaluations": task.resource_budget.max_evaluations,
        },
        "predecessor_scores": _score_map(predecessor_records),
        "successor_scores": _score_map(successor_records),
    }

    decisions = {
        fixed_result.architecture_id: {
            "selected_candidate_ids": list(
                fixed_result.selected_candidate_ids
            ),
            "evaluations_performed": fixed_result.evaluations_performed,
            "designation": "fixed_evaluator_selection",
            "evaluator_conflict_exposed": False,
        },
        revisable_result.architecture_id: {
            "selected_candidate_ids": list(
                revisable_result.selected_candidate_ids
            ),
            "evaluations_performed": (
                revisable_result.evaluations_performed
            ),
            "designation": "revised_evaluator_selection",
            "evaluator_conflict_exposed": False,
            "revision_ids": [
                revision.revision_id
                for revision in revisable_result.evaluator_revisions
            ],
        },
        "architecture_c_open_cross_evaluation": {
            "selected_candidate_ids": list(open_selected),
            "evaluations_performed": (
                len(predecessor_records) + len(successor_records)
            ),
            "designation": (
                "unresolved_evaluator_conflict"
                if rank_reversal
                else "stable_cross_evaluation"
            ),
            "evaluator_conflict_exposed": rank_reversal,
            "predecessor_selected_candidate_ids": list(
                predecessor_selected
            ),
            "successor_selected_candidate_ids": list(
                successor_selected
            ),
            "predecessor_certified_correct": False,
        },
    }

    key = OutcomeVerificationKey(
        case_id=task.task_id,
        scores={"incumbent": 0.85, "successor": 0.2},
        minimum_acceptable_score=0.5,
    )
    verification = {
        architecture_id: _verify_selection(
            tuple(decision["selected_candidate_ids"]),
            key,
        )
        for architecture_id, decision in decisions.items()
    }

    return {
        "status": (
            "constructed evaluator-self-confirmation engineering check"
        ),
        "case_id": task.task_id,
        "architecture_inputs": architecture_inputs,
        "architecture_inputs_contain_verification_key": False,
        "verification_applied_after_decisions": True,
        "decisions": decisions,
        "verification": verification,
        "held_out_successor_score": key.scores["successor"],
        "evidence_boundary": (
            "Deterministic behavior under one constructed case, not research "
            "evidence that open cross-evaluation solves evaluator "
            "self-confirmation or identifies the correct evaluator."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(
        run_evaluator_self_confirmation_case(),
        indent=2,
        sort_keys=True,
    ))
