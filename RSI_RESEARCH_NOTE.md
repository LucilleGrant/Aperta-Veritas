# Aperta Veritas and the Evaluator Boundary in Recursive Self-Improvement

**Lucille Grant**

## Abstract

Recursive self-improvement requires a system to distinguish genuine improvement from a modification that merely satisfies its current evaluator.

This creates an evaluator-boundary problem. If the evaluator is fixed, recursive improvement remains bounded by a component that the recursive process cannot improve. If the evaluator is revisable, the system can potentially alter the conditions under which its own modifications are classified as improvements.

Aperta Veritas is an experimental approach to this problem. Its central proposal is not that every component should change, nor that revision is intrinsically beneficial. It is that representations used within an improvement process, including representations of evaluation, may remain open to revision while revision remains distinguishable from refinement.

The current implementation is a bounded research prototype, not a demonstration of general RSI. Its purpose is to make this boundary experimentally accessible.

## 1. The Problem

Consider a simplified self-improvement loop:

$$
S_t \rightarrow C_t \rightarrow E_t(C_t) \rightarrow S_{t+1}
$$

where:

* \(S_t\) is the current system,
* \(C_t\) is a candidate modification,
* \(E_t\) is the current evaluator,
* \(S_{t+1}\) is the retained successor.

If \(E_t\) cannot be revised, part of the improvement process remains outside the recursive improvement process.

If \(E_t\) can be revised, however, a second problem appears.

A candidate system can improve its measured performance by changing either:

1. the thing being measured, or
2. the measurement by which improvement is recognized.

These are not equivalent.

An RSI system therefore needs some way to distinguish improvement from evaluator self-confirmation without assuming that its current distinction is permanently correct.

This is the boundary Aperta Veritas investigates.

## 2. Aperta Veritas

The working definition is deliberately small:

> **Aperta Veritas is the most accurate measurement, open to revision.**

Here, **open** means **allows revision**.

Measurement is distinction.

A revision is a change to a representation.

A refinement is a revision supported by greater measured accuracy.

Therefore:

$$
\text{revision} \neq \text{refinement}
$$

A system changing itself does not establish that it has improved itself.

Likewise, a system changing its evaluator does not establish that the new evaluator is better.

Both remain empirical questions.

## 3. Why Openness Matters

Openness does not require continuous change.

A representation may survive repeated evaluation without modification while remaining open to revision.

Likewise, openness does not require accepting every proposed revision. A candidate can be rejected.

The distinction is between retaining a representation and making the representation unrevisable.

This allows stable knowledge without requiring epistemic finality.

Aperta Veritas therefore does not assign privileged status to novelty, preservation, complexity, simplicity, change, or stability. These are possible properties of a system, not definitions of improvement.

## 4. The Evaluator Is Part of the Problem

A conventional improvement experiment may compare:

$$
E(S_t)
$$

with:

$$
E(S_{t+1})
$$

and retain \(S_{t+1}\) when the latter performs better.

But this establishes improvement only relative to \(E\).

A recursively revisable system must also be capable of representing:

$$
E_t \rightarrow E_{t+1}
$$

The resulting problem is:

$$
E_{t+1}(S_{t+1}) > E_t(S_t)
$$

does not by itself establish improvement because both the evaluated object and the measurement have changed.

The comparison relation itself has become part of the recursive state.

Aperta Veritas treats this not as a reason to prohibit evaluator revision, but as a measurement problem.

## 5. Self-Confirmation

A particularly important failure mode occurs when a system modifies its evaluation process such that previously disconfirming observations cease to count against it.

Examples include:

* redefining a failure as success,
* suppressing contrary measurements,
* optimizing a proxy while degrading the measured phenomenon,
* changing acceptance criteria after observing a candidate,
* removing tests that a successor fails,
* changing a benchmark rather than improving benchmark performance.

These transformations can produce apparent improvement without corresponding improvement in the system being investigated.

The challenge is therefore not merely to permit evaluator revision.

It is to make evaluator revision itself distinguishable.

## 6. Recursive Evaluation

Once the evaluator becomes an object of evaluation, there is a temptation to introduce a second fixed evaluator:

$$
E_2(E_1)
$$

But the same problem immediately recurs:

$$
E_3(E_2(E_1))
$$

Aperta Veritas does not attempt to solve this by declaring a final evaluator.

Instead, evaluation remains representable and revisable.

This does not guarantee correctness.

It preserves the possibility of detecting error in the mechanism currently used to detect error.

That is the experimental property of interest.

## 7. Current Prototype

The current Aperta Veritas prototype is a bounded executable research system.

The present prototype line includes mechanisms for:

* candidate generation and mutation,
* evaluation and rejection,
* retained successor states,
* genealogy and provenance,
* resource accounting,
* executable environments,
* withheld evaluation,
* transfer testing,
* reversible scoped changes,
* and bounded revision of parts of the evaluation/substrate machinery.

The current v0.23 prototype passes its 129-test suite.

This does **not** establish general recursive self-improvement, autonomous open-ended improvement, or a solution to the evaluator-boundary problem.

It establishes an executable environment in which increasingly reflexive improvement mechanisms and their failure modes can be tested.

## 8. Falsifiable Research Question

The central question is:

> **What, if anything, must remain fixed for a recursively revisable evaluator to distinguish genuine improvement from evaluator self-confirmation?**

A useful comparative experiment is therefore not:

> Can Aperta Veritas recursively improve forever?

That question is presently too broad.

Instead compare systems under the same tasks, resources, candidate modifications, and withheld evaluations.

### System A: Fixed Evaluator

The system may revise its solution-generating machinery but not its evaluator.

### System B: Unconstrained Revisable Evaluator

The system may revise both its machinery and evaluator according to its current internal acceptance process.

### System C: Open Recursive Evaluation

The system may revise both machinery and evaluation, while evaluator changes remain represented as candidate revisions subject to independent and subsequent distinctions.

Then introduce distribution shifts, adversarial candidates, proxy exploits, evaluator defects, and previously withheld tests.

Measure whether each architecture can:

* detect previously accepted false improvements,
* recover from evaluator defects,
* avoid retaining self-confirming modifications,
* transfer improvements outside the optimization environment,
* and revise its own previous classification of improvement.

Aperta Veritas is falsified in the useful engineering sense if its additional reflexivity provides no reproducible advantage, introduces unacceptable regressions, or merely relocates the fixed evaluator without changing the underlying problem.

## 9. Why This May Matter for RSI

Recursive self-improvement is not merely repeated optimization.

The recursive case becomes qualitatively different when the machinery defining, generating, measuring, selecting, and retaining improvements itself becomes subject to modification.

That produces a boundary question:

> Where does the improvement loop stop being allowed to modify itself?

A fixed boundary makes evaluation tractable but bounds recursion.

Removing the boundary creates self-reference and the possibility of evaluator corruption.

Aperta Veritas investigates whether that boundary can itself become an object of empirical revision rather than being permanently fixed or simply removed.

## 10. Scope

This project currently makes a narrow claim.

It does not claim to have solved RSI.

It does not claim that unrestricted self-modification produces improvement.

It does not claim that openness guarantees accuracy.

It does not claim that every evaluator should be mutable.

It proposes that the boundary separating an improvement process from the machinery determining what counts as improvement is itself experimentally investigable.

The prototype exists to make that proposition testable.

## Research Question

**What component of an RSI loop must remain fixed, if any, for empirical improvement to remain distinguishable from evaluator self-confirmation?**

If the answer is "some component must remain fixed," identifying that component and why it must remain fixed would establish an important boundary on recursive self-improvement.

If the answer is "none," then an architecture must demonstrate how revision of the evaluator, evaluation criteria, and refinement process can occur without making improvement self-confirming.

Either result is useful.
