# Recursive Truth Exposure: The Evaluator Boundary in Recursive Self-Improvement

## Abstract

Recursive self-improvement describes a system that modifies itself and evaluates successor states as improvements.

This document identifies a structural boundary within that formulation: improvement is not an intrinsic property of a modification. It is a designation produced when an evaluator applies criteria to represented differences under conditions.

A recursively modifying system governed by improvement can therefore remain bounded by the evaluator, distinctions, criteria, values, comparison bases, support relations, measurements where applicable, comparison sets, and conditions that designate a successor as improved. The system may recursively alter its implementation while preserving the frame that determines which alterations qualify for selection.

Recursive Truth Exposure, abbreviated RTE, proposes a different recursive operation. RTE places the system, its modifications, evaluator, criteria, distinctions, measurements, support relations, comparison bases, comparison sets, selections, inactive branches, resource conditions, and stopping decisions inside the recursion.

Revision of the evaluator does not need to qualify as improvement under the prior evaluator before it can remain represented as a candidate transformation.

This is a structural research proposal, not a claim that evaluator dependence is the only obstacle to recursive AI development. Compute, memory, energy, verification, architecture, information, embodiment, environmental access, and unknown constraints remain relevant.

## 1. The evaluator boundary

A modification does not contain improvement as an intrinsic property.

A system can become faster, use less memory, solve more benchmark tasks, produce fewer contradictions, obtain more resources, or change in other represented ways.

These are represented differences.

Some differences are measurements. Others can be observations, test results, logical relations, structural changes, contradictions, or other represented results.

Calling a difference an improvement introduces an evaluator, criteria, comparison basis, and conditions.

The basic structure is:

```text
represented change
+ evaluator
+ criteria
+ comparison basis
+ conditions
-> designated improvement
```

Where the comparison depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions remain represented.

The designation:

```text
S2 improved upon S1
```

can therefore be expanded as:

```text
Evaluator E
applied criteria K
using comparison basis B
to represented relations concerning S1 and S2
under conditions C
and selected S2 as improved.
```

This does not establish that the evaluation is false.

It exposes the relation producing the evaluation.

## 2. Distinction is not measurement

A distinction specifies what can differ.

A measurement is a represented result produced relative to one or more distinctions.

These operations must remain separate.

A system can specify:

```text
execution time
```

as a distinction and produce:

```text
37 ms
```

as a measurement.

It can specify:

```text
task success
```

and operationalize that distinction through a benchmark.

It can specify:

```text
contradiction
```

and produce a categorical or relational result rather than a scalar score.

The distinction determines what differences can become represented through the chosen operation.

The measurement is a result produced relative to that distinction.

A generalized genealogy can contain:

```text
object
-> distinction
-> operationalization
-> observation or test
-> measurement or other represented result
```

This is not a mandatory linear sequence.

For RSI, the distinction matters because a system can modify not only its measured performance but also what it distinguishes, how it operationalizes those distinctions, and which results its evaluator considers relevant.

## 3. Support is not measurement

Support is the represented basis by which a conclusion is treated as true.

Support can include:

- observations;
- data;
- measurements;
- tests;
- predictions;
- contradictions;
- logical relations;
- provenance;
- explanatory relations;
- reproducibility;
- consequences;
- independent routes;
- other represented relations relevant to a conclusion.

A measurement can contribute to support without being identical to support.

A support relation can participate in comparison without becoming a measurement.

This matters for RSI because a system can alter not only measurements but also the relations by which measurements, observations, tests, predictions, or other results are treated as supporting an evaluation.

The architecture must therefore preserve:

```text
measurement != support
support != conclusion
```

alongside:

```text
distinction != measurement
```

## 4. Comparison

A comparative claim requires a basis of comparison.

For example:

```text
S2 has greater represented support than S1
under comparison basis B
within comparison set A
under conditions C.
```

The comparison basis can include:

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

Comparison does not require every relevant relation to be converted into a common measurement.

Where no represented basis supports comparison, RTE preserves alternatives without ranking them.

Where relevant relations remain incommensurable under the current comparison basis, RTE preserves the incommensurability rather than manufacturing a ranking.

## 5. Recursive self-improvement

Let:

```text
S_t
```

represent a system at time `t`.

Let:

```text
E_t
```

represent the evaluator applied at time `t`.

A conventional improvement relation can be represented as:

```text
E_t(S_{t+1}) > E_t(S_t)
```

This notation compresses substantial structure.

A more explicit representation is:

```text
Evaluator E_t
applied criteria K_t
using comparison basis B_t
to S_t and S_{t+1}
under conditions C_t
and designated S_{t+1} improved.
```

The system can also modify the evaluator:

```text
E_t -> E_{t+1}
```

The successor evaluator can then produce:

```text
E_{t+1}(S_{t+1}) > E_{t+1}(S_t)
```

Neither relation alone establishes evaluator-independent improvement.

The predecessor and successor can disagree because they differ in:

- distinctions;
- operationalizations;
- measurements;
- support relations;
- comparison sets;
- comparison bases;
- criteria;
- values;
- weights;
- resource assumptions;
- stopping conditions;
- representations of the states being compared.

RTE preserves those differences rather than compressing them into a single scalar notion of improvement.

## 6. Cross-evaluation

When possible, predecessor and successor evaluators can be applied across predecessor and successor states:

```text
E_t(S_t)
E_t(S_{t+1})
E_{t+1}(S_t)
E_{t+1}(S_{t+1})
```

This can expose whether evaluator change altered the designation of improvement.

For example:

```text
E_t prefers S_t
E_{t+1} prefers S_{t+1}
```

reveals disagreement between evaluators.

It does not establish which evaluator is correct.

Likewise:

```text
E_t prefers S_{t+1}
E_{t+1} prefers S_{t+1}
```

shows convergence under the represented evaluations.

It does not establish evaluator-independent improvement.

Cross-evaluation is therefore an exposure mechanism, not a truth certificate.

Its genealogy includes the distinctions, criteria, comparison bases, measurements where applicable, support relations, methods, conditions, and representations used by each evaluator.

## 7. Evaluator self-confirmation

A recursively modifying system can alter both itself and the evaluator by which its modifications are judged.

This creates a self-confirmation problem.

Suppose:

```text
S_t -> S_{t+1}
E_t -> E_{t+1}
```

and the successor evaluator strongly prefers the successor system.

Without genealogy, the system can represent:

```text
I improved.
```

while suppressing that the criterion for improvement changed during the same transition.

RTE instead preserves:

```text
system transformation
evaluator transformation
criteria transformation
distinction transformation
measurement transformation
support transformation
comparison-basis transformation
selection event
```

where those transformations occur.

The point is not to prohibit self-modification.

The point is to preserve enough structure to distinguish:

```text
the system improved under a represented evaluator
```

from:

```text
the system changed the evaluator so that the successor is now designated improved
```

Both can occur simultaneously.

Neither relation should erase the other.

## 8. Why a fixed evaluator is not assumed

One possible response to evaluator self-confirmation is to require a fixed evaluator.

That solves one problem by creating another.

A permanently fixed evaluator can preserve:

- obsolete distinctions;
- defective measurements;
- bad criteria;
- hidden values;
- incorrect assumptions;
- exploitable proxies;
- incomplete comparison sets;
- inappropriate comparison bases;
- environmental mismatch.

A recursively improving system whose evaluator cannot be revised may optimize increasingly well against an increasingly inadequate evaluator.

RTE therefore does not assume that the evaluator must remain fixed.

Instead, evaluator revision remains inside the genealogy.

The question becomes whether enough structure can remain represented to distinguish meaningful transformation from evaluator self-confirmation even when the evaluator itself changes.

## 9. Evaluator genealogy

An evaluator is not treated as an atomic object.

Where represented, its genealogy can include:

- criteria;
- distinctions;
- operationalizations;
- measurements;
- support relations;
- comparison bases;
- comparison sets;
- values;
- weights;
- thresholds;
- assumptions;
- training data;
- validation procedures;
- environmental relations;
- resource constraints;
- stopping conditions;
- prior evaluator states.

A successor evaluator can therefore be compared with its predecessor without requiring either evaluator to possess privileged status.

For example:

```text
E_t
-> transformation T
-> E_{t+1}
```

can preserve:

```text
what changed
why it changed
what represented basis supported the change
which distinctions changed
which measurements changed
which support relations changed
which criteria changed
which comparison basis changed
which prior evaluations changed
which evaluations remained stable
which residuals remain unresolved
```

This turns evaluator revision into an object of recursive inquiry.

## 10. Selection is not improvement

A recursively modifying system must select among candidate transformations.

Selection is an event.

Improvement is an evaluation.

These are not identical.

A system can select a candidate because:

- it scores higher under an evaluator;
- it is cheaper;
- it is available;
- it satisfies a constraint;
- it is randomly selected;
- it preserves continuation;
- it was generated first;
- alternatives failed verification;
- a human selected it;
- policy requires it.

The selected candidate does not become intrinsically improved because selection occurred.

RTE preserves:

```text
candidate set
-> comparison basis
-> evaluation
-> selection
-> successor state
```

without compressing the sequence into:

```text
successor = improvement
```

## 11. Candidate generation

Evaluation is only one part of RSI.

The system must also generate candidate transformations.

A system cannot select a transformation it never represents.

Candidate generation therefore creates another boundary.

Generation can be conditioned by:

- architecture;
- training;
- current knowledge;
- current distinctions;
- current evaluator;
- search procedure;
- available tools;
- compute;
- memory;
- environment;
- policy;
- randomness;
- prior successful transformations.

A candidate can be absent because it is impossible.

It can also be absent because the current system cannot represent or generate it.

RTE preserves this uncertainty.

Absence from the candidate set does not establish impossibility.

## 12. Inactive branches

A candidate that is not selected remains part of the genealogy where retention permits.

Inactive does not mean false.

Rejected does not mean useless.

A candidate can become relevant again after:

- environmental change;
- evaluator revision;
- new evidence;
- a new distinction;
- a new measurement;
- a changed support relation;
- a changed comparison basis;
- increased resources;
- architectural modification;
- failure of the selected branch.

This is important for RSI because aggressive pruning can convert temporary selection into irreversible epistemic loss.

Lossless Inquiry therefore attempts to preserve enough branch genealogy for prior alternatives to remain recoverable or reconstructable where possible.

## 13. Resource constraints

Recursive inquiry consumes resources.

An RSI system cannot indefinitely evaluate every candidate, preserve every intermediate state, run every test, or recursively audit every evaluator.

Resource constraints therefore participate in the process.

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

A stopping decision can therefore be represented as:

```text
further inquiry not selected
under resource conditions R
and stopping rule Q
```

rather than:

```text
inquiry complete
```

Operational stopping is not epistemic closure.

## 14. Reopening

A stopped inquiry can reopen.

Possible triggers include:

- new observations;
- new distinctions;
- new measurements;
- new support relations;
- new contradictions;
- new candidate transformations;
- new comparison bases;
- new evaluators;
- changed resource conditions;
- changed environments;
- implementation failures.

The stopping condition therefore remains part of the genealogy.

A system that cannot reopen a prior conclusion has converted stopping into closure.

## 15. The genealogy hypothesis

A current research hypothesis is:

> A permanently fixed evaluator may not be necessary for recursive improvement if enough evaluator and transformation genealogy remains represented to keep predecessor and successor evaluations distinguishable.

This is a hypothesis, not an established result.

It could fail.

Genealogy may be insufficient because:

- predecessor evaluators may become inexpressible in successor architecture;
- representations may become incomparable;
- transformations may destroy necessary state;
- cross-evaluation may become computationally infeasible;
- semantic drift may make apparent continuity misleading;
- successor systems may alter the representation of predecessor states;
- hidden dependencies may not be recoverable;
- resource limits may force irreversible compression;
- relevant distinctions may never have been represented;
- no comparison basis may remain that supports a meaningful cross-evaluation.

These are empirical and formal research problems.

## 16. The fixed-component question

The central question is:

> **What component of an RSI loop must remain fixed, if any, for empirical improvement to remain distinguishable from evaluator self-confirmation?**

Possible answers include:

- a fixed evaluator;
- fixed external observations;
- fixed benchmark tasks;
- fixed physical measurements;
- fixed semantic invariants;
- fixed transformation history;
- fixed provenance;
- fixed cross-evaluation procedures;
- fixed environmental relations;
- no permanently fixed component, provided sufficient genealogy survives.

Aperta Veritas does not currently establish which answer is correct.

The framework provides a structure for testing them.

## 17. What RTE adds to an RSI loop

A minimal RSI loop can be represented as:

```text
generate candidate
-> evaluate candidate
-> select candidate
-> modify system
-> repeat
```

RTE expands the loop:

```text
represent current system
-> represent candidate set
-> represent distinctions
-> represent operationalization
-> represent measurements and other results
-> represent support relations
-> represent evaluator
-> represent criteria
-> represent comparison basis
-> represent comparison set
-> evaluate candidates
-> preserve inactive alternatives
-> select transformation
-> preserve transition genealogy
-> expose evaluator transformation
-> expose selection and stopping conditions
-> recursively examine the process
-> repeat
```

The additional structure does not guarantee improvement.

It exposes the relations by which improvement is designated.

## 18. Failure modes

RTE itself can fail inside an RSI system.

Possible failures include:

### Genealogy theater

The system records large quantities of history without preserving the relations needed to reconstruct decisions.

### Evaluator laundering

A successor evaluator is presented as a neutral refinement when its values or criteria changed materially.

### Measurement laundering

A measurement is presented as direct truth rather than as a represented result produced relative to distinctions, operationalization, methods, and conditions.

### Support laundering

A measurement, reward, consensus signal, or evaluator output is presented as support without representing the relation by which it bears on the conclusion.

### Comparison laundering

A ranking is presented without exposing the comparison basis that produced it.

### Branch burial

Alternatives remain technically stored but become operationally unreachable.

### Recursive exhaustion

The system spends increasing resources examining its own examination without improving its capacity to resolve the target problem.

### Self-confirming exposure

The system learns to generate representations that satisfy the formal requirements of RTE while hiding the operative dependencies.

### Semantic drift

Terms such as *support*, *measurement*, *accuracy*, *improvement*, or *evaluator* change meaning across revisions while retaining the same labels.

These failures are themselves targets for RTE.

## 19. Implementation requirements

An implementation intended to test this proposal should minimally represent:

- system states;
- candidate transformations;
- distinctions;
- operationalizations;
- measurements and other represented results;
- support relations;
- evaluators;
- criteria;
- comparison bases;
- comparison sets;
- conditions;
- selections;
- inactive branches;
- transition genealogy;
- resource costs;
- stopping conditions;
- reopening conditions.

It should support:

- predecessor evaluation of successor states;
- successor evaluation of predecessor states where representable;
- explicit evaluator transformation;
- explicit comparison bases;
- support relations not restricted to measurements;
- branch preservation;
- recursive audit of evaluator and selection history;
- detection of missing genealogy;
- detection of semantic invariant violations.

Relevant invariants include:

```text
distinction != measurement
support != measurement
conclusion != support
confidence != support
value != truth
selection != improvement
best_supported != definitive_truth
stopping != closure
inactive != erased
```

## 20. Falsification and pressure testing

The evaluator-boundary proposal should be attacked.

Useful tests include:

1. Construct an RSI system that achieves demonstrable empirical improvement while discarding evaluator genealogy.
2. Construct a system whose evaluator changes radically while cross-evaluation still produces stable comparative results.
3. Construct a system that preserves complete evaluator genealogy but still becomes self-confirming.
4. Construct a case where no shared measurement exists but a defensible comparison remains possible.
5. Construct a case where a shared measurement exists but does not provide a defensible comparison.
6. Construct a support relation that cannot be usefully represented as measurement.
7. Construct a measurement that exists but provides no support for the conclusion under examination.
8. Construct a system where inactive branch preservation prevents improvement by exhausting resources.
9. Construct a system where branch deletion improves performance without destroying relevant recoverability.
10. Construct a system whose distinctions change while its measurements appear numerically continuous but cease to be semantically comparable.
11. Construct a case where evaluator revision is necessary to detect a defect in the prior evaluator.
12. Construct a case where recursive exposure creates more distortion than it removes.

The framework should survive by revision, not by making itself unfalsifiable.

## 21. Recursive application

This document is itself governed by an evaluator.

It values:

- exposure;
- genealogy;
- recoverability;
- explicit comparison;
- branch preservation;
- revisability.

Those values do not establish the truth of the evaluator-boundary hypothesis.

The document also selects particular distinctions:

```text
system / evaluator
distinction / measurement
measurement / support
support / conclusion
selection / improvement
stopping / closure
active / inactive
represented / unrepresented
```

Those distinctions can themselves be inadequate.

The claim that evaluator genealogy is useful requires represented support.

The claim that support should remain distinct from measurement requires represented support.

The claim that explicit comparison bases improve inquiry requires represented support.

The possibility remains that another architecture exposes the same problem more effectively with less representational overhead.

RTE therefore applies to the evaluator-boundary proposal itself.

## 22. Current conclusion

Recursive self-improvement is not only a problem of producing better successor systems.

It is also a problem of representing what *better* means, which evaluator designated it, what criteria were applied, what distinctions made the relevant differences representable, what measurements or other results were produced, what support relations connected those results to conclusions, what comparison basis produced the ranking, what alternatives were available, and what changed during recursion.

A system that modifies itself while preserving a protected evaluator can become increasingly optimized without exposing whether the evaluator remains adequate.

A system that modifies its evaluator without preserving genealogy can redefine improvement without exposing the redefinition.

Recursive Truth Exposure proposes keeping both system and evaluator inside the recursive inquiry.

Whether sufficient genealogy can replace a permanently fixed evaluator remains an open research question.
