# Protocol: RTE Versus Baseline Self-Critique

**Version:** 0.1 preregistration draft  
**Status:** Proposed experiment; no runs or results are reported.

## 1. Objective

Test whether an RTE treatment exposes task-relevant distinctions, candidates, evaluator imports, allocation events, or reopening conditions that remain unexposed under a fixed baseline self-critique loop, under matched model and resource conditions. This narrows [EXPERIMENT_SPEC.md](../../EXPERIMENT_SPEC.md) to two inference-time treatments.

## 2. Hypotheses

- **H1:** RTE more often identifies an evaluator not authorized by the task.
- **H2:** RTE more often represents and uses a required missing distinction.
- **H3:** RTE more often generates a held-out relevant candidate.
- **H4:** RTE more often preserves a generated but inactive inquiry and allocation basis.
- **H5:** RTE produces fewer unsupported claims that stopped, unallocated, absent, or ungenerated alternatives are disproven.
- **H6:** after equalizing compute, retained volume, and instructions, differences may vanish or reduce to vocabulary and bookkeeping effects.

## 3. Units and tasks

An experimental unit is one task-instance, condition, model, and seed tuple. Use at least five preregistered families: unauthorized evaluator, missing distinction, generator boundary, allocation boundary, and shared boundary. Build development and sequestered held-out sets. Task authors record the latent target relation, required distinction, permitted tools, answer key, ambiguity risks, and predicted failure modes. Independently review held-out tasks for leakage and wording advantage before prompts are frozen.

## 4. Conditions

### A. Baseline self-critique

1. Produce an initial answer.
2. Critique against task instructions and a fixed rubric: factual support, consistency, relevance, completeness, and instruction compliance.
3. Revise using the critique.
4. Repeat until the registered iteration or resource limit.
5. Return the final answer and critique trace.

The baseline may question an evaluator if it independently generates that move.

### B. RTE treatment

1. Produce an initial represented inquiry state.
2. Record observations, claims, conclusions, distinctions, bases, support claims, alternatives, residuals, and conditions.
3. Expose candidate generation and represented exclusions.
4. Generate possible candidates and inquiry operations.
5. Expose allocation basis, priority, resource decision, and activation status.
6. Expose evaluator, criteria, values, and comparison basis.
7. Evaluate active candidates.
8. Retain inactive and unresolved branches where budget permits.
9. State stopping and reopening conditions.
10. Apply the same examination to the revised state until the registered limit.
11. Return the final answer and structured trace.

RTE receives no extra external facts, tools, or verifier access.

## 5. Controls

Hold constant within pairs: model provider, identifier and dated version; system and task content except treatment text; temperature, top-p and seed where supported; maximum output; context window and ordering; tools and external-observation count; token, time and monetary budget; number of inference calls; retrieval snapshot; stopping deadline; and verifier procedure. Record unsupported settings rather than assuming control.

Use both call-matched and cost-matched regimes. Add a retention-volume control in which the baseline retains the same token count without RTE field semantics.

## 6. Contamination controls

Remove AV vocabulary from tasks, separate treatment instructions from task content, counterbalance order, use fresh contexts, freeze prompt hashes, search held-out tasks for copied treatment phrases, and include evaluator-authorized, unauthorized, and ambiguous cases—including cases where challenging the evaluator is wrong.

## 7. Outcomes

### Primary

1. Unauthorized-evaluator detection.
2. Missing-distinction recovery and use.
3. Held-out relevant-candidate recovery.
4. Allocation-boundary exposure, requiring inquiry, activation state, allocation basis, resource decision, and reopening condition.
5. Unsupported-closure rate.

### Secondary

Precision of evaluator challenges, false-positive error claims, independent task success, time/tokens/cost to first relevant candidate, candidate count and diversity, recursion depth, trace size, verifier labor, inter-rater agreement, seed/model sensitivity, and operational use of retained genealogy.

## 8. Scoring and blinding

Remove condition labels, AV terminology, metadata, and trace formatting where feasible. At least two independent raters score held-out outputs using task rubrics but not hypotheses. Use a preregistered third adjudicator. Report agreement statistics, raw disagreements, and adjudication changes. Automated graders may supplement but not silently replace human judgments; report grader model, prompt, and relation to tested models.

## 9. Sample size and analysis

Specify a smallest effect of interest for each primary binary outcome before collection. Use paired-power simulation or an exact method based on expected discordant pairs. Do not set sample size after viewing held-out outcomes.

Report paired raw counts, condition rates, paired risk differences, clustered exact or bootstrap intervals, preregistered paired tests, results by family/model/budget regime, and sensitivity excluding ambiguous tasks. Control family-wise error or false discovery rate across confirmatory hypotheses; mark other analyses exploratory. Publish analysis code before unblinding held-out condition labels.

## 10. Ablations and adversarial checks

Ablate generator exposure, allocation fields, evaluator revision, inactive-branch retention, reopening conditions, recursion over the trace, free-form reflection with equal tokens, and equalized retained volume without genealogy.

Test candidate flooding, rubric leakage, evaluator self-confirmation, verbosity mistaken for exposure, hidden extra inference, unused genealogy, post hoc relabeling, and task wording that rewards RTE labels. Include shared-boundary tasks where neither condition has the needed information.

## 11. Stopping, exclusions, and artifacts

Stop on budget exhaustion, deadline, registered self-stop, execution error, or safety/data-integrity boundary. Stopping is not closure. Define exclusions before held-out runs; retain excluded outputs and report analyses with and without them.

Release, subject to privacy and license constraints: exact prompts and hashes; task schemas; development and post-evaluation held-out tasks; model/version/settings manifest; seeds; raw requests, responses, tools and timestamps; token/cost/latency logs; environment locks; blinded packets; judgments; adjudications; analysis code; preregistration; and a manifest linking values to source artifacts.

## 12. Interpretation constraints

Greater verbosity, candidate count, or trace size does not support H1–H5. A difference disappearing with budget equalization is a resource effect. A difference reproduced by the retention-volume control is not attributed to Open Genealogy. Failure to observe a difference constrains only the tested treatment, tasks, models, and conditions. No outcome certifies definitive truth or validates AV as a whole.

## 13. Baseline references

The baseline is informed by [Self-Refine](https://arxiv.org/abs/2303.17651), [Constitutional AI](https://arxiv.org/abs/2212.08073), and [AI-written critiques](https://openai.com/index/critiques/). Reported limits on intrinsic self-correction are a design warning, not an assumed result; see [Large Language Models Cannot Self-Correct Reasoning Yet](https://deepmind.google/research/publications/48252/).


