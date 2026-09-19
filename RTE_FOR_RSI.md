# Recursive Truth Exposure: Generation and Evaluation in Recursive Self-Improvement

## Abstract

Recursive self-improvement describes a system that generates modifications, evaluates candidate successor states, selects among them, and recursively modifies itself.

This document identifies two structural boundaries within that formulation.

The first is the **generation boundary**. An evaluator can evaluate only candidates that become represented. A system can therefore improve its evaluation of represented candidates while failing to generate a successor requiring distinctions absent from its current representation.

The second is the **evaluator boundary**. Improvement is not an intrinsic property of a modification. It is a designation produced when an evaluator applies criteria to represented differences under conditions.

A recursively modifying system can therefore remain bounded both by what its generator makes representable and by what its evaluator recognizes as improvement.

Recursive Truth Exposure, abbreviated RTE, places the system, generator, candidate space, modifications, evaluator, criteria, distinctions, measurements, bases, support claims, comparison bases, comparison sets, selections, inactive branches, resource conditions, stopping decisions, and reopening conditions inside the recursion.

Lossless Inquiry preserves unresolved branches and prior states because their informational significance need not remain fixed. Later distinctions can expose new relations among retained records and make new hypotheses, tests, comparisons, evaluators, or successor states representable.

Revision of a generator or evaluator does not need to qualify as improvement under the prior evaluator before it can remain represented as a candidate transformation.

This is a structural research proposal, not a claim that generation and evaluator dependence are the only obstacles to recursive AI development. Compute, memory, energy, verification, architecture, information, embodiment, environmental access, and unknown constraints remain relevant.

## 1. The generation boundary

Evaluation operates on represented candidates.

It does not by itself determine which candidates become represented.

A minimal recursive improvement loop can be written:

```text
current system
-> generate candidates
-> evaluate candidates
-> select candidate
-> modify system
-> repeat
```

This creates an upstream boundary.

A system cannot evaluate a candidate it never generates.

A relevant successor can be absent because it is impossible.

It can also be absent because the current system lacks:

- a distinction required to represent it;
- a relation required to connect existing information;
- a model capable of expressing it;
- a search procedure capable of reaching it;
- an instrument or observation required to expose it;
- a test capable of discriminating it;
- sufficient resources;
- retained information needed to reconstruct it;
- an evaluator capable of preserving the branch long enough for later examination.

Absence from the candidate set therefore does not establish impossibility.

This gives:

```text
generation != evaluation
evaluated_candidates != exhaustive_possibility_space
absence_from_search != disproof
```

The generation boundary is recursive because candidate generation can itself change.

A successor system can alter:

- what distinctions it can represent;
- which relations it can detect;
- which hypotheses it can express;
- which transformations it can propose;
- which tests it can invent;
- which representations it can construct;
- which evaluators it can generate;
- which prior branches it can reactivate.

RTE therefore examines the generator as part of the recursive system.

## 2. The evaluator boundary

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

Generation and evaluation therefore impose different boundaries:

```text
generator boundary:
what becomes available for evaluation?

evaluator boundary:
how are available candidates judged?
```

An RSI architecture can fail at either boundary.

## 3. Distinction is not measurement

A distinction specifies what can differ.

A measurement is a represented result produced relative to one or more distinctions.

These operations remain separate.

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

For RSI, the distinction matters because a system can modify not only its measured performance but also what it distinguishes, how it operationalizes those distinctions, and which results its generator or evaluator can use.

A new distinction can also alter represented relations involving prior records.

It can therefore affect not only future measurement but future generation.

## 4. Basis is not support

A **basis** is a represented reason, source, condition, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, or support.

A basis does not become epistemic support merely because it participates in a decision.

RTE separates at least three uses.

### Acceptance basis

An acceptance basis records why a system accepts, selects, retains, or acts upon a conclusion.

Examples can include:

- measurement;
- inference;
- authority;
- prior architecture;
- policy;
- reward;
- human instruction;
- consensus;
- inherited state;
- error.

An acceptance basis can explain a selection without establishing that the selected conclusion is true.

### Inquiry basis

An inquiry basis records why a candidate remains worth examining.

Examples can include:

- an unresolved anomaly;
- a contradiction;
- conflicting measurements;
- an untested prediction;
- a missing distinction;
- an incomplete model;
- an unexplored alternative;
- a possible discriminating test;
- a newly available resource;
- a new relation among retained records.

Inquiry basis is not epistemic support.

A candidate can therefore have weak present support while retaining future inquiry potential.

### Support relation and support claim

A support relation is a claimed relation between one or more bases and whether a conclusion should presently be treated as true under represented conditions.

A support claim asserts that the relation bears on whether the conclusion is true.

A measurement can participate in a support claim without being identical to support.

A logical relation can participate without becoming a measurement.

An observation can participate without being reduced to a scalar.

The architecture therefore preserves:

```text
basis != support
acceptance_basis != support
inquiry_basis != support
support != measurement
support_claim != truth
conclusion != support
```

This matters directly to RSI.

A reward can cause selection without supporting a factual conclusion.

An evaluator score can provide an acceptance basis without becoming truth.

A failed candidate can retain an inquiry basis without being treated as improved.

A support claim can itself be wrong.

RTE keeps these relations available for examination.

## 5. Comparison

A comparative claim requires a represented comparison basis.

For example:

```text
S2 has greater represented support than S1
under comparison basis B
within comparison set A
under conditions C.
```

The comparison basis can include:

- represented support relations and support claims;
- distinctions;
- criteria;
- methods;
- conditions;
- measurements where applicable;
- evaluator structure;
- dependencies;
- exclusions;
- unresolved relations.

Comparison does not require every relevant relation to be converted into a common measurement.

Where no represented basis supports ranking, RTE preserves alternatives without ranking them.

This establishes only:

```text
currently unranked
under represented comparison basis
```

It does not establish:

```text
intrinsically incommensurable
```

A claim of incommensurability is itself a claim requiring represented support.

This matters in RSI because an evaluator can fail to rank candidates because its present representation lacks a comparison basis that a later system could generate.

## 6. Recursive self-improvement

Let:

```text
S_t
```

represent a system at time `t`.

Let:

```text
G_t
```

represent its generator.

Let:

```text
E_t
```

represent its evaluator.

A simplified RSI transition is:

```text
G_t(S_t)
-> candidate S_(t+1)
-> E_t(S_(t+1))
-> selection
```

A conventional improvement relation can be represented as:

```text
E_t(S_(t+1)) > E_t(S_t)
```

But that notation begins after `G_t` has made `S_(t+1)` representable.

A more explicit representation is:

```text
Generator G_t
operated from represented state S_t
under generative conditions R_t
and produced candidate S_(t+1).

Evaluator E_t
applied criteria K_t
using comparison basis B_t
to S_t and S_(t+1)
under conditions C_t
and designated S_(t+1) improved.
```

The system can modify both generator and evaluator:

```text
G_t -> G_(t+1)
E_t -> E_(t+1)
```

The successor can therefore change both:

```text
what candidates can be produced
```

and:

```text
what counts as improvement
```

Neither generator output nor evaluator selection alone establishes evaluator-independent improvement.

RTE preserves those transformations rather than compressing them into a single scalar notion of progress.

## 7. Generator genealogy

A generator is not treated as an atomic object.

Where represented, its genealogy can include:

- architecture;
- current distinctions;
- current representations;
- prior observations;
- retained branches;
- search procedure;
- recombination procedure;
- model structure;
- training;
- tools;
- environmental access;
- randomness;
- resource constraints;
- evaluator feedback;
- prior successful transformations;
- prior failed transformations;
- exclusions;
- policy constraints;
- representation formats;
- stopping conditions.

A candidate-generation event can therefore preserve:

```text
source state
-> available distinctions
-> available relations
-> generation method
-> constraints
-> candidate
```

RTE can then ask:

```text
Why was this candidate generated?
Why were these candidates generated instead of others?
Which distinctions structured the search?
Which representations could the generator not express?
Which prior branches were available?
Which branches had already been erased?
Which evaluator signals shaped generation?
```

The purpose is not to certify an exhaustive generator.

It is to expose the conditions under which the represented candidate space arose.

## 8. Evaluator genealogy

An evaluator is not treated as an atomic object.

Where represented, its genealogy can include:

- criteria;
- distinctions;
- operationalizations;
- measurements;
- bases;
- support relations;
- support claims;
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
-> E_(t+1)
```

can preserve:

```text
what changed
why it changed
what acceptance basis produced the change
what inquiry basis motivated examination
which support claims concerned the change
which distinctions changed
which measurements changed
which criteria changed
which comparison basis changed
which prior evaluations changed
which evaluations remained stable
which residuals remain unresolved
```

This turns evaluator revision into an object of recursive inquiry.

## 9. Cross-evaluation

When possible, predecessor and successor evaluators can be applied across predecessor and successor states:

```text
E_t(S_t)
E_t(S_(t+1))
E_(t+1)(S_t)
E_(t+1)(S_(t+1))
```

This can expose whether evaluator change altered the designation of improvement.

For example:

```text
E_t prefers S_t
E_(t+1) prefers S_(t+1)
```

reveals disagreement between evaluators.

It does not establish which evaluator is correct.

Likewise:

```text
E_t prefers S_(t+1)
E_(t+1) prefers S_(t+1)
```

shows convergence under the represented evaluations.

It does not establish evaluator-independent improvement.

Cross-evaluation is therefore an exposure mechanism, not a truth certificate.

Its genealogy includes the distinctions, criteria, comparison bases, measurements where applicable, bases, support claims, methods, conditions, and representations used by each evaluator.

## 10. Evaluator self-confirmation

A recursively modifying system can alter both itself and the evaluator by which its modifications are judged.

This creates a self-confirmation problem.

Suppose:

```text
S_t -> S_(t+1)
E_t -> E_(t+1)
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
generator transformation
evaluator transformation
criteria transformation
distinction transformation
measurement transformation
support-claim transformation
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

## 11. Why a fixed evaluator is not assumed

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

A recursively modifying system whose evaluator cannot be revised may optimize increasingly well against an increasingly inadequate evaluator.

RTE therefore does not assume that the evaluator must remain fixed.

Instead, evaluator revision remains inside the genealogy.

The question becomes whether enough structure can remain represented to distinguish meaningful transformation from evaluator self-confirmation even when the evaluator itself changes.

## 12. Why a fixed generator is not assumed

A fixed generator creates a parallel problem.

If the generator cannot change, recursive improvement remains constrained by the transformations the original generator can represent.

A fixed generator can preserve:

- obsolete search procedures;
- inadequate distinctions;
- restricted representation formats;
- inaccessible candidate classes;
- inherited exclusions;
- poor recombination strategies;
- evaluator-induced search bias;
- architectural assumptions;
- resource allocation strategies that prevent exploration.

RTE therefore does not assume that the generator must remain fixed.

Generator revision remains inside the genealogy.

A recursively modifying system can attempt to generate generators, distinctions, representations, or search procedures that expand what successor states become representable.

That creates another recursive question:

```text
How does a system generate a generator
capable of producing candidates
that the current generator cannot produce?
```

Aperta Veritas does not assume that genealogy alone answers this question.

It makes the boundary explicit and preserves material that may participate in later generative operations.

## 13. Selection is not improvement

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
generation
-> candidate set
-> comparison basis
-> evaluation
-> selection
-> successor state
```

without compressing the sequence into:

```text
successor = improvement
```

## 14. Inactive branches and inquiry basis

A candidate that is not selected remains part of the genealogy where retention permits.

Inactive does not mean false.

Rejected does not mean useless.

Failure to establish does not mean disproof.

A candidate can become relevant again after:

- environmental change;
- evaluator revision;
- generator revision;
- new evidence;
- a new distinction;
- a new measurement;
- a new support claim;
- a changed comparison basis;
- increased resources;
- architectural modification;
- failure of the selected branch;
- discovery of a new relation among retained records.

An inactive branch can therefore retain an **inquiry basis** without having strong epistemic support.

This separation is necessary.

Otherwise, retaining a hypothesis for investigation can be mistaken for treating it as true.

Likewise, lack of present support can be mistaken for a reason to erase the branch.

The relevant invariants are:

```text
failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential
inactive != erased
```

Aggressive pruning can convert temporary selection into irreversible loss of future generative material.

Lossless Inquiry therefore attempts to preserve enough branch genealogy for prior alternatives to remain recoverable or reconstructable where possible.

## 15. Recontextualization

The significance of a retained state is not necessarily fixed when it is produced.

Suppose the system retains:

```text
record A
record B
```

without a represented relation connecting them.

A later distinction `D` can expose:

```text
A
-> relation R
-> B
```

The old records are not replaced.

Their represented relational context changes.

This can produce:

```text
retained state
+
new distinction
->
new represented relation
->
new candidate
->
new test
```

For RSI, this means preservation can contribute directly to future generation.

A branch that was previously unresolved can contain a component that becomes useful after:

- a new distinction;
- a new representation;
- a new environmental observation;
- a new evaluator;
- a new generator;
- a new comparison basis;
- recombination with another branch.

Lossless Inquiry is therefore not only a mechanism for reconstructing past decisions.

It preserves material whose future generative significance may not yet be represented.

## 16. Resource constraints

Recursive inquiry consumes resources.

An RSI system cannot indefinitely generate every candidate, evaluate every candidate, preserve every intermediate state, run every test, or recursively audit every generator and evaluator.

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

A branch can become inactive without being erased.

Compression can preserve some relations while making others unavailable.

Resource allocation itself can affect future generation.

Operational stopping is not epistemic closure.

## 17. Reopening

A stopped inquiry can reopen.

Possible triggers include:

- new observations;
- new distinctions;
- new measurements;
- new bases;
- new inquiry bases;
- new support claims;
- new contradictions;
- newly generated candidate transformations;
- new comparison bases;
- new evaluators;
- new generators;
- changed resource conditions;
- changed environments;
- implementation failures;
- new relations among previously retained records.

The stopping condition therefore remains part of the genealogy.

Reopening does not establish that the earlier stopping decision was erroneous.

It establishes that the represented conditions of inquiry have changed.

## 18. The genealogy hypothesis

A current research hypothesis is:

> Preserved genealogy can provide material for later recontextualization and candidate generation while keeping predecessor and successor representations distinguishable.

This is a hypothesis, not an established result.

A related evaluator hypothesis is:

> A permanently fixed evaluator may not be necessary for recursive improvement if enough evaluator and transformation genealogy remains represented to keep predecessor and successor evaluations distinguishable.

Both could fail.

Genealogy may be insufficient because:

- predecessor generators may become inexpressible in successor architecture;
- predecessor evaluators may become inexpressible in successor architecture;
- representations may become presently unrankable;
- transformations may destroy necessary state;
- cross-evaluation may become computationally infeasible;
- semantic drift may make apparent continuity misleading;
- successor systems may alter the representation of predecessor states;
- hidden dependencies may not be recoverable;
- resource limits may force irreversible compression;
- relevant distinctions may never have been represented;
- preserved information may not be sufficient to generate the missing distinction;
- no represented comparison basis may support meaningful cross-evaluation;
- recontextualization may introduce spurious relations rather than useful ones.

These are empirical and formal research problems.

## 19. The central RSI question

The research question is broader than determining which component must remain fixed.

It is:

> **How can a recursive system generate and recognize improvements that require distinctions absent from the system currently generating and evaluating successor states?**

This contains several subordinate questions:

```text
How are new distinctions generated?

How can unresolved branches remain available
without being promoted to truth?

How can later distinctions recontextualize prior states?

How can a system search beyond candidate classes
favored by its current evaluator?

How can generator and evaluator change
remain genealogically examinable?

What component of the loop must remain fixed,
if any, for empirical improvement to remain
distinguishable from self-confirmation?
```

Possible answers to the fixed-component question include:

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

## 20. What RTE adds to an RSI loop

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
-> represent generator
-> represent retained genealogy
-> represent current distinctions
-> generate candidate set
-> expose how candidates became representable
-> represent operationalizations
-> represent measurements and other results
-> represent bases
-> separate acceptance basis from inquiry basis
-> represent support relations and support claims
-> represent evaluator
-> represent criteria
-> represent comparison basis
-> represent comparison set
-> evaluate candidates
-> preserve unresolved and inactive alternatives where possible
-> select transformation
-> preserve transition genealogy
-> expose generator transformation
-> expose evaluator transformation
-> expose selection and stopping conditions
-> admit new distinctions and relations
-> recontextualize retained states
-> generate new candidates where possible
-> recursively examine the process
-> repeat
```

The additional structure does not guarantee improvement.

It exposes both the relations by which candidates become representable and the relations by which they are designated improvements.

## 21. Failure modes

RTE itself can fail inside an RSI system.

Possible failures include:

### Genealogy theater

The system records large quantities of history without preserving the relations needed for reconstruction, recontextualization, or future generation.

### Generator lock-in

The system recursively evaluates candidates while failing to expose that its generator cannot represent relevant alternative classes.

### Evaluator laundering

A successor evaluator is presented as a neutral refinement when its values or criteria changed materially.

### Measurement laundering

A measurement is presented as direct truth rather than as a represented result produced relative to distinctions, operationalization, methods, and conditions.

### Support laundering

A measurement, reward, consensus signal, authority, acceptance basis, or evaluator output is presented as epistemic support without representing the claim by which it bears on whether a conclusion is true.

### Inquiry laundering

A reason to continue examining a hypothesis is presented as evidence that the hypothesis is true.

### Comparison laundering

A ranking is presented without exposing the comparison basis that produced it.

### Incommensurability laundering

Failure to represent a comparison basis is presented as proof that no comparison is possible.

### Branch burial

Alternatives remain technically stored but become operationally unreachable.

### Generative starvation

Pruning, compression, or resource allocation removes the retained material from which later distinctions or candidates could have been generated.

### Recursive exhaustion

The system spends increasing resources examining its own examination without improving its capacity to resolve the target problem.

### Self-confirming exposure

The system learns to generate representations that satisfy the formal requirements of RTE while hiding operative dependencies.

### Semantic drift

Terms such as *basis*, *support*, *measurement*, *accuracy*, *generation*, *improvement*, or *evaluator* change meaning across revisions while retaining the same labels.

### Spurious recontextualization

The system generates new relations among retained records without sufficient support for treating those relations as accurate.

These failures are themselves targets for RTE.

## 22. Implementation requirements

An implementation intended to test this proposal should minimally represent:

- system states;
- generators;
- candidate transformations;
- distinctions;
- operationalizations;
- measurements and other represented results;
- bases;
- acceptance bases;
- inquiry bases;
- support relations;
- support claims;
- evaluators;
- criteria;
- comparison bases;
- comparison sets;
- conditions;
- selections;
- inactive branches;
- transition genealogy;
- generation genealogy;
- recontextualization events;
- resource costs;
- stopping conditions;
- reopening conditions.

It should support:

- explicit candidate generation;
- explicit generator transformation;
- predecessor evaluation of successor states;
- successor evaluation of predecessor states where representable;
- explicit evaluator transformation;
- explicit comparison bases;
- support relations not restricted to measurements;
- support claims that remain recursively examinable;
- acceptance bases distinct from support;
- inquiry bases distinct from support;
- branch preservation;
- later recontextualization of retained states;
- generation from retained genealogy where possible;
- recursive audit of generator, evaluator, and selection history;
- detection of missing genealogy;
- detection of semantic invariant violations.

Relevant invariants include:

```text
distinction != measurement
basis != support
acceptance_basis != support
inquiry_basis != support
support != measurement
support_claim != truth
conclusion != support
conclusion != acceptance_basis
confidence != support
confidence != accuracy
consensus != support
belief != truth
fact != definitive_truth
value != truth
selection != improvement
evaluation != generation
evaluated_candidates != exhaustive_possibility_space
relational_richness != accuracy
best_supported != definitive_truth
failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential
unranked != necessarily_incommensurable
stopping != closure
inactive != erased
```

## 23. Falsification and pressure testing

The generation-and-evaluation proposal should be attacked.

Useful tests include:

1. Construct an RSI system that reliably generates relevant novel candidate classes without preserving prior unresolved branches.
2. Construct a system in which preserving unresolved genealogy provides no measurable generative advantage.
3. Construct a system in which later distinctions successfully expose useful relations among previously retained records.
4. Construct a system in which recontextualization consistently produces spurious rather than useful relations.
5. Construct a system that achieves demonstrable empirical improvement while discarding evaluator genealogy.
6. Construct a system whose evaluator changes radically while cross-evaluation still produces stable comparative results.
7. Construct a system that preserves extensive generator and evaluator genealogy but still becomes self-confirming.
8. Construct a case where no shared measurement exists but a defensible comparison remains possible.
9. Construct a case where a shared measurement exists but does not provide a defensible comparison.
10. Construct a support relation that cannot be usefully represented as measurement.
11. Construct a measurement that exists but provides no support for the conclusion under examination.
12. Construct a strong acceptance basis that provides no epistemic support.
13. Construct a strong inquiry basis for a hypothesis with weak epistemic support.
14. Construct a system where inactive branch preservation prevents improvement by exhausting resources.
15. Construct a system where branch deletion improves performance without destroying relevant future inquiry potential.
16. Construct a system whose distinctions change while its measurements appear numerically continuous but cease to be semantically comparable.
17. Construct a case where evaluator revision is necessary to detect a defect in the prior evaluator.
18. Construct a case where generator revision makes a previously inaccessible improvement representable.
19. Construct a case where a candidate remains unranked under the current comparison basis but becomes rankable after a new distinction or comparison basis is generated.
20. Construct a case where recursive exposure creates more distortion than it removes.

The framework should survive by revision, not by making itself unfalsifiable.

## 24. Recursive application

This document is itself governed by an evaluator and produced by a generator.

It values:

- exposure;
- genealogy;
- recoverability;
- explicit comparison;
- branch preservation;
- revisability;
- generative openness.

Those values do not establish the truth of the generation-boundary or evaluator-boundary hypotheses.

The document also selects particular distinctions:

```text
system / generator
system / evaluator
generation / evaluation
basis / support
acceptance basis / inquiry basis
distinction / measurement
measurement / support
support claim / truth
support / conclusion
selection / improvement
stopping / closure
active / inactive
represented / unrepresented
```

Those distinctions can themselves be inadequate.

The claim that genealogy contributes to future generation requires represented support.

The claim that retained branches can acquire later significance requires represented support.

The claim that support should remain distinct from basis and measurement requires represented support.

The claim that explicit comparison bases improve inquiry requires represented support.

The possibility remains that another architecture exposes the same problems more effectively with less representational overhead.

RTE therefore applies to this proposal itself.

## 25. Current conclusion

Recursive self-improvement is not only a problem of producing better successor systems.

Before a successor can be evaluated, it must become representable.

Before a relevant difference can be evaluated, the system must possess or generate a distinction capable of representing that difference.

Before a comparison can occur, the relevant alternatives and comparison basis must become represented.

A system can therefore fail to improve because its evaluator is inadequate.

It can also fail before evaluation because the relevant successor never enters the candidate set.

A system that modifies itself while preserving a protected evaluator can become increasingly optimized without exposing whether the evaluator remains adequate.

A system that modifies its evaluator without preserving genealogy can redefine improvement without exposing the redefinition.

A system that aggressively discards unresolved branches can remove material whose relevance would only become representable after later distinctions arise.

Recursive Truth Exposure proposes keeping the generator, candidate space, evaluator, transformations, and retained genealogy inside recursive inquiry.

The current research hypothesis is that preservation plus recursive distinction generation and recontextualization may permit a system to expand what it can represent and therefore what it can test, compare, and modify.

That hypothesis remains unestablished.

The central question remains:

> **How can a recursive system generate and recognize improvements that require distinctions absent from the system currently generating and evaluating successor states?**
