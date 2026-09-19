# Aperta Veritas and the Evaluator Boundary in Recursive Self-Improvement

**Lucille Grant**

## Abstract

Recursive self-improvement requires a system to distinguish improvement from a modification that merely satisfies the evaluator currently determining what counts as improvement.

This creates an evaluator-boundary problem.

If the evaluator is fixed, some machinery determining improvement remains outside the recursive process.

If the evaluator is revisable, the system can potentially alter the conditions under which its own modifications are classified as improvements.

Aperta Veritas is an experimental approach to representing and testing this problem.

Its central proposal is not that every component should change, nor that revision is intrinsically beneficial. It is that the evaluator, criteria, distinctions, measurements, support relations, comparison basis, comparison set, selection operation, and designation of improvement can remain represented within the same recursive inquiry process as the system being modified.

The current implementation is a bounded research prototype, not a demonstration of general recursive self-improvement. Its purpose is to make this boundary experimentally accessible.

## 1. The Problem

Consider a simplified self-improvement loop:

\[
S_t \rightarrow C_t \rightarrow E_t(C_t) \rightarrow S_{t+1}
\]

where:

- \(S_t\) is the current system;
- \(C_t\) is a candidate modification;
- \(E_t\) is the current evaluator;
- \(S_{t+1}\) is the retained successor.

If \(E_t\) cannot be revised, part of the machinery determining improvement remains outside the recursive improvement process.

If \(E_t\) can be revised, however, a second problem appears.

A candidate system can change its apparent performance by changing either:

1. the system being evaluated;
2. the distinctions, measurements, criteria, support relations, or comparison basis by which the change is evaluated.

These transformations are not equivalent.

An RSI system therefore needs some way to distinguish:

\[
\text{selected as better under evaluator } E
\]

from:

\[
\text{improved}
\]

without assuming that its current distinctions, evaluator, or comparison basis are permanently correct.

This is the boundary Aperta Veritas investigates.

## 2. Aperta Veritas

Aperta Veritas is a recursive process for exposing how representations and conclusions are produced, supported, selected, revised, and retained.

Its governing operation is Recursive Truth Exposure.

RTE identifies conclusions presently best supported as true under represented observations, relations, methods, conditions, and other represented support.

It does not establish that a presently best-supported conclusion is identical with definitive truth.

Applied to recursive self-improvement, the same distinction becomes:

\[
\text{selected successor} \neq \text{improved successor}
\]

and:

\[
\text{higher evaluator score} \neq \text{improvement}
\]

unless a represented comparison basis supports that relation under stated conditions.

Where that comparison depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions remain represented.

A revision is a change to a represented state or process.

A refinement is a revision for which greater accuracy or support is established under an explicit represented comparison basis.

Therefore:

\[
\text{revision} \neq \text{refinement}
\]

A system changing itself does not establish that it has improved itself.

Likewise, a system changing its evaluator does not establish that the new evaluator is better.

The transition, evaluator, criteria, distinctions, measurements, support relations, comparison basis, conditions, and resulting selection remain objects of inquiry.

## 3. Why Openness Matters

Open means that revision remains possible.

Openness does not require continuous change.

A representation can survive repeated evaluation without modification while remaining open to revision.

Likewise, openness does not require accepting every proposed revision. A candidate can be rejected, superseded, or made inactive while remaining genealogically represented.

The distinction is between retaining a representation and insulating that representation from relevant distinction or revision.

This permits stable conclusions without requiring epistemic finality.

Aperta Veritas therefore does not assign privileged status to novelty, preservation, complexity, simplicity, change, or stability.

These can be represented properties or criteria. None defines improvement by category alone.

## 4. The Evaluator Is Part of the Problem

A conventional improvement experiment can compare:

\[
E(S_t)
\]

with:

\[
E(S_{t+1})
\]

and retain \(S_{t+1}\) when the latter receives the preferred evaluation.

This establishes selection relative to \(E\).

It does not establish improvement independently of the evaluator, criteria, distinctions, comparison basis, support relations, measurements where applicable, conditions, and comparison set that produced the selection.

A recursively revisable system must also be capable of representing:

\[
E_t \rightarrow E_{t+1}
\]

The resulting expression:

\[
E_{t+1}(S_{t+1}) > E_t(S_t)
\]

does not by itself establish improvement because both the evaluated object and the evaluation process have changed.

The comparison relation has become part of the recursive state.

Aperta Veritas treats this not as a reason to prohibit evaluator revision, but as a problem of represented comparison and genealogy.

The system should retain, where representable:

```text
predecessor system
candidate modification
successor system
predecessor evaluator
successor evaluator
criteria
distinctions
operationalizations
measurements and other represented results
support relations
comparison basis
conditions
comparison set
selection operation
residuals
genealogy
```

The purpose is not to preserve these structures as permanently correct.

The purpose is to keep their transformation available for examination.

## 5. Support and Measurement

Support is the represented basis by which a conclusion is treated as true.

Measurement is a represented result produced relative to one or more distinctions.

They are not identical.

A measurement can contribute to support when a represented relation connects it to a conclusion.

Support can also include observations, tests, predictions, contradictions, logical relations, provenance, explanatory relations, reproducibility, consequences, independent routes, and other represented relations.

Therefore:

\[
\text{support} \neq \text{measurement}
\]

and:

\[
\text{conclusion} \neq \text{support}
\]

This matters for RSI because an evaluator can change not only what is measured, but how represented results are interpreted as supporting a designation of improvement.

A system that preserves measurements while silently changing their support relations can alter its evaluation architecture without exposing the change.

## 6. Comparison Basis

A comparative judgment requires a represented basis of comparison.

A comparison basis can include:

- alternatives being compared;
- represented support;
- distinctions;
- criteria;
- methods;
- conditions;
- measurements where applicable;
- evaluator structure;
- dependencies;
- exclusions;
- unresolved or incomparable relations.

A comparative claim can therefore be represented as:

```text
S2 is designated better than S1
under evaluator E
using criteria K
under comparison basis B
within comparison set A
under conditions C.
```

This representation does not establish evaluator-independent improvement.

It exposes the basis under which the designation was produced.

Where no represented basis supports comparison, alternatives remain represented without ranking.

Comparison does not require every relevant relation to be converted into a common measurement.

## 7. Cross-Evaluation

A useful test is to preserve both predecessor and successor evaluators.

Let:

\[
E_t
\]

be the predecessor evaluator and:

\[
E_{t+1}
\]

the successor evaluator.

Then compare:

\[
E_t(S_t)
\]

\[
E_t(S_{t+1})
\]

\[
E_{t+1}(S_t)
\]

\[
E_{t+1}(S_{t+1})
\]

This produces four represented evaluation relations.

Suppose:

\[
E_t(S_t) > E_t(S_{t+1})
\]

while:

\[
E_{t+1}(S_{t+1}) > E_{t+1}(S_t)
\]

The successor is preferred only after the evaluator changes.

That does not prove the successor is worse.

It does not prove the successor evaluator is defective.

It exposes a relation that would disappear if the predecessor evaluator were erased.

Conversely, if both evaluators prefer \(S_{t+1}\), that convergence can contribute to a represented case for improvement.

It still does not establish evaluator-independent improvement by category alone.

The independence, criteria, comparison bases, conditions, and dependencies of the evaluations remain relevant.

## 8. The Genealogy Hypothesis

One current hypothesis is that a permanently fixed evaluator may not be necessary.

Instead, sufficient genealogy may allow a recursively modifying system to revise its evaluator while preserving the ability to distinguish predecessor and successor judgments.

Represent:

\[
E_t \rightarrow E_{t+1}
\]

along with:

- what changed;
- which distinctions changed;
- how operationalizations changed;
- which measurements or other results changed;
- which support relations changed;
- which criteria changed;
- which comparison basis changed;
- which values changed;
- which prior judgments changed;
- which judgments remained stable;
- why the transformation was selected;
- which alternatives remained inactive;
- which residuals remain unresolved.

Then evaluator revision itself becomes an object of inquiry.

This does not establish that genealogy is sufficient.

It makes the sufficiency of genealogy testable.

## 9. Candidate Generation

Evaluation is not the entire RSI problem.

A system cannot select a candidate it never generates.

Candidate generation can depend on:

- current architecture;
- represented knowledge;
- distinctions;
- search procedures;
- tools;
- training;
- evaluator structure;
- compute;
- memory;
- environmental access;
- prior transformations;
- policy;
- randomness.

Absence from the candidate set does not establish impossibility.

It can indicate only that the current process did not represent the alternative.

This means the comparison set is itself conditioned by the candidate-generation process.

RTE therefore keeps candidate generation inside the inquiry.

## 10. Selection Is Not Improvement

Selection is an event.

Improvement is an evaluation.

A system can select a candidate because:

- an evaluator prefers it;
- it uses fewer resources;
- it satisfies a constraint;
- other candidates fail;
- policy requires it;
- it was generated first;
- it preserves continuation;
- it was randomly selected.

The fact of selection does not establish improvement.

Therefore:

\[
\text{selection} \neq \text{improvement}
\]

The selection operation and the evaluation supporting it remain separate represented relations.

## 11. Inactive Branches

A candidate that is not selected can remain represented.

Inactive does not mean false.

Rejected does not mean permanently irrelevant.

A candidate can become relevant after:

- evaluator revision;
- environmental change;
- new observations;
- new distinctions;
- new measurements;
- new support relations;
- new comparison bases;
- increased resources;
- failure of the selected branch.

Preserving branch genealogy prevents temporary selection from automatically becoming historical erasure.

Finite resources may still require compression or deletion.

Where detectable, that loss should remain represented as loss.

## 12. Resource Constraints

Recursive inquiry consumes resources.

A system cannot preserve every physical detail, evaluate every candidate, perform every possible test, or recurse indefinitely.

Relevant constraints include:

- compute;
- memory;
- storage;
- energy;
- time;
- bandwidth;
- environmental access;
- tool availability;
- verification cost.

A stopping event can therefore mean:

```text
further inquiry not selected under current resource conditions
```

rather than:

```text
the inquiry is complete
```

Operational stopping is not epistemic closure.

## 13. Reopening

A stopped inquiry can reopen when relevant conditions change.

Possible triggers include:

- new observation;
- new distinction;
- new measurement;
- new support relation;
- new contradiction;
- new candidate;
- new comparison basis;
- evaluator revision;
- increased resources;
- implementation failure;
- environmental change.

The reopening condition remains part of the genealogy where possible.

## 14. Current Prototype

The current Aperta Veritas prototype is a bounded inquiry ledger.

It is intended to test whether explicit representation of inquiry genealogy can preserve distinctions that ordinary optimization loops tend to compress.

The prototype is not an RSI system.

It does not demonstrate autonomous recursive self-improvement.

It does not establish the genealogy hypothesis.

Its role is narrower:

1. represent inquiry states;
2. preserve transitions;
3. represent evaluators;
4. represent support and comparison;
5. preserve inactive branches;
6. preserve stopping conditions;
7. expose selected semantic invariants;
8. test whether genealogy survives revision.

The implementation should be treated as a testable representation of the framework rather than as proof of the framework.

Its architecture must also be revised when the conceptual specification exposes distinctions that the implementation does not yet represent.

## 15. Current Implementation Gap

The conceptual architecture now explicitly separates:

```text
distinction != measurement
support != measurement
conclusion != support
```

An implementation that requires every support relation to be a measurement would therefore fail to represent the current framework.

Likewise, an implementation that records measurements without representing the distinctions and operationalizations producing them compresses part of the current architecture.

The prototype should therefore be tested for whether it can represent:

- distinctions independently of measurements;
- measurements independently of support;
- support without requiring measurement;
- measurements that provide no support for a particular conclusion;
- comparison bases that do not require a common measurement;
- incommensurable alternatives;
- explicit conclusion-support separation.

These are implementation requirements derived from the current conceptual model, not claims that the prototype already satisfies them.

## 16. Research Questions

The central question is:

> **What component of an RSI loop must remain fixed, if any, for empirical improvement to remain distinguishable from evaluator self-confirmation?**

Related questions include:

1. Is a fixed evaluator necessary?
2. Can evaluator genealogy substitute for evaluator immutability?
3. What minimum genealogy is required for meaningful cross-evaluation?
4. Can predecessor and successor evaluators remain comparable after architectural change?
5. What happens when no common comparison basis survives evaluator revision?
6. Which distinctions must remain stable for measurements across revisions to remain comparable?
7. Can support remain comparable when measurements do not?
8. Can measurements remain numerically comparable while their semantic basis changes?
9. How much inactive branch history must be preserved?
10. When does genealogy preservation become computationally prohibitive?
11. Can a system detect when its evaluator has become self-confirming?
12. Can recursive exposure itself become a self-confirming evaluator?
13. What forms of support cannot usefully be reduced to measurement?
14. What relations must remain external, if any?

Aperta Veritas does not currently answer these questions.

It provides a structure in which they can be represented and tested.

## 17. Pressure Tests

Useful experiments include:

### Evaluator replacement

Allow a successor to replace its evaluator and test whether predecessor and successor judgments remain reconstructable.

### Distinction mutation

Change the distinctions used by the evaluator while preserving apparently similar measurements and test whether semantic comparability survives.

### Measurement mutation

Change the measurement procedure while preserving the criterion label and test whether the system detects the altered basis.

### Support mutation

Preserve the same measurement while changing the relation by which it supports an evaluation and test whether the system represents the change.

### Comparison-basis mutation

Preserve states and measurements while changing the comparison basis and test whether the resulting selection is distinguishable from the prior evaluation.

### Candidate omission

Remove the strongest candidate before evaluation and test whether the system distinguishes:

```text
best represented candidate
```

from:

```text
best possible candidate
```

### Genealogy deletion

Delete evaluator history and test which comparative claims become unreconstructable.

### Branch reactivation

Reject a candidate, change conditions, and test whether the candidate can become active again without being regenerated from scratch.

### Resource pressure

Reduce available storage or compute and test whether the system records what genealogy was compressed or discarded.

### Self-application

Allow RTE to revise its own distinctions, comparison rules, or stopping conditions and test whether prior states remain distinguishable.

## 18. Failure Conditions

The research direction would be weakened if experiments show that:

- evaluator genealogy adds no useful distinction beyond ordinary versioning;
- cross-evaluation becomes meaningless after modest evaluator revision;
- support relations cannot be represented without arbitrary evaluator assumptions;
- explicit comparison bases add representation without improving reconstructability;
- branch preservation consumes resources without providing recoverable value;
- recursive exposure consistently creates more ambiguity than it resolves;
- a simpler architecture preserves the same relevant distinctions with less overhead.

These outcomes should not be excluded by definition.

They would be evidence for revising or abandoning parts of the approach.

## 19. Recursive Application

This research note is itself a represented proposal.

It selects:

- evaluator dependence as a research problem;
- genealogy as a candidate mechanism;
- cross-evaluation as a useful test;
- openness as a desired property;
- distinction, measurement, support, comparison, and conclusion as separate objects.

Those selections do not establish their own correctness.

The distinction:

\[
\text{support} \neq \text{measurement}
\]

is itself a claim.

The distinction:

\[
\text{distinction} \neq \text{measurement}
\]

is itself a claim.

The hypothesis that genealogy can preserve meaningful comparison across evaluator revision is also a claim.

Each remains open to testing and revision.

## 20. Current Position

The current position is not:

> A fixed evaluator prevents RSI.

Nor is it:

> Aperta Veritas solves RSI.

The current position is narrower:

> Recursive self-improvement contains an evaluator-boundary problem because the system, the evaluator, and the basis by which successor states are designated improved can all become objects of recursive modification.

Aperta Veritas proposes explicit genealogy, support representation, comparison-basis representation, cross-evaluation, and recursive exposure as mechanisms for studying that problem.

Whether those mechanisms are sufficient remains open.
