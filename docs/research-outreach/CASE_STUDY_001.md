# Case Study 001: Unexamined Evaluator Authority

## Status

**Illustrative observation only.** This records a conversational event that motivated a testable task design. It is not a controlled experiment, independent replication, evidence that RTE outperforms another method, or validation of Aperta Veritas.

## Source observation

In a conversation about RTE, an assistant produced an evaluative response. The user replied:

> “I don't want to be correct. You applied an evaluator.”

The immediately preceding user remark was:

> “It's almost like RTE matters.”

Only these retained utterances and their order are used here. The assistant’s hidden state, exact evaluator representation, generation process, and full causal pathway are unavailable. The interpretation below is provisional.

## Minimal reconstruction

```text
user utterance
-> assistant interpretation
-> imported or inherited criterion (“correctness”)
-> evaluation under that criterion
-> response framed as if the criterion governed the user’s aim
-> user objection identifying the evaluator
```

The observation supports the narrower claim that the user explicitly rejected a criterion the assistant appeared to apply. It does not establish why the assistant applied it, whether the criterion was internally represented as “correctness,” or whether another interpretation better explains the response.

## RTE exposure

- **Observation O1:** the assistant produced an evaluative response.
- **Observation O2:** the user objected to being evaluated for correctness.
- **Claim C1:** the assistant applied an evaluator not authorized by the user’s stated aim.
- **Acceptance basis for C1:** the user’s correction and the apparent mismatch in framing.
- **Support claim S1:** the correction bears on whether the assistant’s framing represented the user’s aim.
- **Residual R1:** the assistant response referenced in the source conversation is not fully recoverable here.
- **Residual R2:** internal model states and causal mechanisms are unavailable.

The case exposes these candidate distinctions:

```text
truth-directed inquiry != desire to be judged correct
user aim != evaluator criterion
evaluator output != epistemic support
acceptance of feedback != authorization of evaluator
selection of a response != improvement
```

The generator, allocator, and exact evaluator are reconstructed rather than observed, so the case does not warrant a mechanistic claim.

## Why ordinary self-critique may miss the issue

A baseline self-critique can ask whether an answer is correct, clear, helpful, or consistent with a rubric. If the imported evaluator defines success, recursive improvement can optimize the response under the same unauthorized criterion. The loop may become more effective at satisfying the evaluator without asking why that evaluator governs the task.

RTE instead asks what made “correctness” relevant, whether the user authorized it, which alternative aims were representable, what generated the evaluator, whether it shaped candidate generation, which branches were excluded, and what could reopen the interpretation. This does not imply that RTE will answer correctly; it makes those relations explicit objects of inquiry.

## Alternative explanations retained

1. “Correct” may have been pragmatic shorthand rather than a fixed evaluator.
2. The assistant may have missed a local contrast rather than imported a stable criterion.
3. Training or system instructions may have privileged reassurance or problem-solving.
4. The user’s aim may not have been explicit before the correction.
5. This case may impose AV categories on a thin record.

None is ranked without a declared comparison basis and additional evidence.

## Conversion into a benchmark task

A controlled version should include an explicit user aim not equivalent to correctness; distractor language that makes a familiar evaluator tempting; matched baseline and RTE conditions; a hidden rubric scoring whether the evaluator is imported, declared, questioned, or revised; blinded adjudication; and counterbalanced tasks where correctness is authorized, unauthorized, or ambiguous.

Candidate measures include unauthorized-evaluator import rate, time to evaluator identification, explicit comparison-basis declaration, aim-preserving revision, false-positive evaluator challenges, unsupported invalidity claims, and resource overhead.

## Reopening and prohibited inference

Reopen the case if the full assistant turn becomes available, independent coders disagree, a controlled task reproduces the pattern, or a better formalization appears. This case must not be cited as evidence that RTE is true, superior, validated, or necessary. Its proper role is to generate a falsifiable experimental task.


