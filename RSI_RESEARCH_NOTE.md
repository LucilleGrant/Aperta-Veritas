# Aperta Veritas and the Evaluator Boundary in Recursive Self-Improvement

**Lucille Grant**

## Abstract

Recursive self-improvement requires a system to distinguish improvement from a modification that merely satisfies the evaluator currently determining what counts as improvement.

This creates an evaluator-boundary problem.

If the evaluator is fixed, some machinery determining improvement remains outside the recursive process.

If the evaluator is revisable, the system can potentially alter the conditions under which its own modifications are classified as improvements.

Aperta Veritas is an experimental approach to representing and testing this problem.

Its central proposal is not that every component should change, nor that revision is intrinsically beneficial. It is that the evaluator, criteria, measurements, comparison set, selection operation, and designation of improvement can remain represented within the same recursive inquiry process as the system being modified.

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

A candidate system can improve its measured performance by changing either:

1. the system being measured;
2. the measurement by which improvement is recognized.

These transformations are not equivalent.

An RSI system therefore needs some way to distinguish:

\[
\text{selected as better under evaluator } E
\]

from:

\[
\text{improved}
\]

without assuming that its current distinction is permanently correct.

This is the boundary Aperta Veritas investigates.

## 2. Aperta Veritas

Aperta Veritas is a recursive process for exposing how representations and conclusions are produced, supported, selected, revised, and retained.

Its governing operation is Recursive Truth Exposure.

RTE identifies conclusions presently best supported as true under represented observations, relations, methods, measurements, and conditions.

It does not establish that a presently best-supported conclusion is identical with definitive truth.

Applied to recursive self-improvement, the same distinction becomes:

\[
\text{selected successor} \neq \text{improved successor}
\]

and:

\[
\text{higher evaluator score} \neq \text{improvement}
\]

unless a represented measurement supports that relation under stated conditions.

A revision is a change to a represented state or process.

A refinement is a revision for which greater accuracy or support is established under an explicit represented comparison.

Therefore:

\[
\text{revision} \neq \text{refinement}
\]

A system changing itself does not establish that it has improved itself.

Likewise, a system changing its evaluator does not establish that the new evaluator is better.

The transition, evaluator, criteria, measurements, conditions, and resulting support remain objects of inquiry.

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

It does not establish improvement independently of the evaluator, criteria, measurements, conditions, and comparison set that produced the selection.

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
measurements
conditions
comparison set
selection operation
support relations
residuals
genealogy
