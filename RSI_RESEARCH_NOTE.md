# Aperta Veritas and Generative Inquiry in Recursive Self-Improvement

**Lucille Grant**

## Abstract

Recursive self-improvement requires a system to generate candidate modifications, allocate finite resources among represented possibilities, and distinguish improvement from a modification that merely satisfies the evaluator currently determining what counts as improvement.

This creates three related boundaries.

The **generation boundary** concerns which candidate successors, distinctions, relations, tests, representations, inquiry operations, allocators, and evaluators become available for examination.

The **allocation boundary** concerns which represented possibilities receive finite resources and become active.

The **evaluator boundary** concerns how represented candidates and results are compared and designated as improvements.

A system can therefore fail before evaluation because a relevant successor never becomes representable. It can fail after generation because a relevant inquiry or transformation never receives the resources required to become active. It can also fail during evaluation because its current evaluator, distinctions, criteria, values, comparison basis, or support claims inadequately represent the relevant differences.

Aperta Veritas is an experimental approach to representing and testing these problems.

Its central proposal is not that every component should change, nor that revision is intrinsically beneficial. It is that generators, allocators, evaluators, criteria, distinctions, measurements, bases, support claims, comparison bases, comparison sets, inquiry operations, inquiry priorities, resource allocations, selection operations, retained branches, transformations, and designations of improvement can remain represented within the same recursive inquiry process as the system being modified.

Lossless Inquiry adds a further hypothesis: unresolved, inactive, and unallocated representations can retain future inquiry potential because later distinctions may expose relations that were not representable when those records were produced.

Convergent Inquiry generates and examines possible continuations of unresolved inquiry. It does not establish which continuation should receive resources, and the term *convergent* does not imply guaranteed mathematical convergence or approach to truth.

The current implementation is a bounded research prototype, not a demonstration of general recursive self-improvement. Its purpose is to make these boundaries experimentally accessible.

## 1. The Problem

Consider a simplified self-improvement loop:

\[
S_t \rightarrow G_t(S_t) \rightarrow C_t \rightarrow A_t(C_t) \rightarrow E_t(C_t) \rightarrow S_{t+1}
\]

where:

- \(S_t\) is the current system;
- \(G_t\) is the current generator;
- \(C_t\) is a generated candidate modification or inquiry operation;
- \(A_t\) is the current allocator;
- \(E_t\) is the current evaluator;
- \(S_{t+1}\) is the retained successor.

This loop contains at least three distinct problems.

First:

\[
G_t(S_t) \rightarrow C_t
\]

determines which candidates become available.

Second:

\[
A_t(C_t)
\]

participates in determining which represented possibilities receive resources and become active.

Third:

\[
E_t(C_t)
\]

determines how represented candidates or results are evaluated.

These operations are not equivalent.

A system cannot evaluate a candidate it never generates.

A system cannot execute every represented inquiry or transformation when resources are finite.

A system also cannot evaluate a difference requiring a distinction it cannot represent.

Therefore:

\[
\text{generation} \neq \text{allocation}
\]

\[
\text{allocation} \neq \text{evaluation}
\]

\[
\text{generation} \neq \text{evaluation}
\]

and:

\[
\text{evaluated candidates} \neq \text{exhaustive possibility space}
\]

The allocator and evaluator introduce additional recursive problems.

If \(A_t\) cannot be revised, part of the machinery determining which represented possibilities become active remains outside the recursive improvement process.

If \(A_t\) can be revised, the system can alter which questions, tests, transformations, and alternatives receive resources.

If \(E_t\) cannot be revised, part of the machinery determining improvement remains outside the recursive improvement process.

If \(E_t\) can be revised, a system can alter the conditions under which its own modifications are classified as improvements.

A candidate system can therefore change:

1. the system being evaluated;
2. the generator producing candidate systems and inquiry operations;
3. the distinctions through which candidate differences become representable;
4. the allocator, allocation bases, priorities, and resource assignments determining which possibilities become active;
5. the evaluator, criteria, support claims, or comparison basis by which represented candidates are judged.

These transformations are not equivalent.

Aperta Veritas investigates the recursive relations among them.

## 2. Generation Before Allocation and Evaluation

Evaluation begins after a candidate exists.

Allocation also operates on represented possibilities.

This creates a structural limit.

A candidate can be absent because it is impossible.

It can also be absent because the current system cannot represent or generate it.

Candidate generation can depend on:

- architecture;
- represented knowledge;
- distinctions;
- represented relations;
- search procedures;
- representation formats;
- tools;
- training;
- allocator structure;
- evaluator structure;
- compute;
- memory;
- environmental access;
- prior transformations;
- retained inactive branches;
- policy;
- randomness.

Absence from the candidate set therefore does not establish impossibility.

It may establish only that the current generative process did not produce the alternative.

This gives:

\[
\text{absence from search} \neq \text{disproof}
\]

The same structure appears in inquiry more generally.

Testing can evaluate a represented hypothesis.

Testing does not by itself determine which hypothesis, distinction, model, observation, instrument, discriminating test, or inquiry operation becomes representable next.

Aperta Veritas therefore places generation inside recursive inquiry rather than treating the candidate set as given.

## 3. Allocation Before Active Inquiry

Generation does not imply activation.

A finite system can represent more possible inquiries and transformations than it can execute.

An **inquiry operation** is a represented possible continuation of inquiry.

An inquiry operation can include:

- introducing or applying a distinction;
- generating a hypothesis;
- searching for a relation;
- changing an operationalization;
- making an observation;
- performing a test;
- producing a measurement;
- comparing alternatives;
- recontextualizing retained records;
- examining a generator, allocator, or evaluator;
- activating a retained branch.

An **allocation basis** represents criteria, conditions, constraints, purposes, policies, values, costs, expected consequences, or other bases used in allocating resources among possible inquiry operations.

An **inquiry priority** is a represented ordering or preference among possible inquiry operations under an explicit allocation basis and represented conditions.

A **resource allocation** is a represented assignment of available resources to one or more inquiry operations under represented conditions.

An **allocator** is the represented process or agent participating in prioritization and resource allocation.

The allocation structure can therefore be represented as:

```text
possible inquiry operations
-> allocation basis
-> inquiry priority
-> resource conditions
-> allocator
-> resource allocation
-> active inquiry
```

These relations remain separate:

\[
\text{inquiry basis} \neq \text{inquiry priority}
\]

\[
\text{inquiry priority} \neq \text{resource allocation}
\]

\[
\text{allocation basis} \neq \text{support}
\]

\[
\text{resource allocation} \neq \text{support}
\]

A generated possibility can remain unallocated.

An unallocated possibility can remain open.

An inactive branch can remain genealogically represented.

Therefore:

\[
\text{open inquiry} \neq \text{active inquiry}
\]

\[
\text{not allocated} \neq \text{rejected}
\]

\[
\text{inactive} \neq \text{erased}
\]

No neutral allocator is assumed.

Allocation can depend on expected information gain, urgency, cost, tractability, novelty, anomaly density, external request, random sampling, safety constraints, available instruments, compute, memory, storage, energy, time, policy, values, or other represented conditions.

Those conditions can govern attention without becoming epistemic support for the proposition being investigated.

## 4. Aperta Veritas

Aperta Veritas is a recursive process for exposing how representations, candidates, inquiry operations, and conclusions are generated, prioritized, allocated, supported, selected, revised, retained, stopped, and reopened.

Its governing operation is Recursive Truth Exposure.

Truth is what is true.

RTE identifies conclusions presently supported as true under represented observations, relations, methods, measurements where applicable, conditions, and support claims.

It does not establish that a presently supported conclusion is identical with definitive truth.

Applied to recursive self-improvement:

\[
\text{generated successor} \neq \text{improved successor}
\]

\[
\text{allocated successor} \neq \text{improved successor}
\]

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

A system changing its generator does not establish that the new generator is better.

A system changing its allocator does not establish that the new allocator is better.

A system changing its evaluator does not establish that the new evaluator is better.

Each transition remains an object of inquiry.

## 5. Basis, Acceptance, Inquiry, Allocation, and Support

A **basis** is a represented reason, source, condition, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, allocation, or support.

Basis is not identical to support.

An **acceptance basis** records why a system accepts, selects, retains, or acts upon a conclusion.

An acceptance basis can include:

- observation;
- measurement;
- inference;
- evaluator output;
- reward;
- authority;
- policy;
- human instruction;
- prior architecture;
- consensus;
- habit;
- inherited state;
- error.

These can explain acceptance without establishing truth.

An **inquiry basis** is a represented basis under which further examination of a claim, hypothesis, observation, anomaly, relation, distinction, alternative, unresolved branch, or other represented object could occur.

An inquiry basis can include:

- unresolved observations;
- discrepancies;
- conflicting measurements;
- contradictions;
- missing distinctions;
- incomplete models;
- untested predictions;
- unexplored alternatives;
- possible discriminating tests;
- new methods;
- new resources;
- relations exposed by later distinctions.

Inquiry basis is not epistemic support.

Inquiry basis is not inquiry priority.

The existence of an inquiry basis does not establish that resources should presently be allocated to it.

An **allocation basis** represents criteria, conditions, constraints, purposes, policies, values, costs, expected consequences, or other bases used in allocating resources among possible inquiry operations.

Allocation basis is not epistemic support.

A **support relation** is a claimed relation between one or more bases and whether a conclusion should presently be treated as true under represented conditions.

A **support claim** asserts that such a relation bears on whether the conclusion is true.

Therefore:

\[
\text{basis} \neq \text{support}
\]

\[
\text{acceptance basis} \neq \text{support}
\]

\[
\text{inquiry basis} \neq \text{support}
\]

\[
\text{inquiry basis} \neq \text{inquiry priority}
\]

\[
\text{allocation basis} \neq \text{support}
\]

\[
\text{resource allocation} \neq \text{support}
\]

\[
\text{support claim} \neq \text{truth}
\]

The existence of a support claim does not certify that the represented relation actually supports truth.

Its basis, inference, distinctions, methods, conditions, dependencies, exclusions, and alternatives remain open to RTE.

## 6. Convergent Inquiry

**Convergent Inquiry** is the generation and examination of possible continuations of unresolved inquiry, including new distinctions, relations, hypotheses, operationalizations, methods, observations, tests, measurements, comparison bases, and support claims.

Convergent Inquiry does not establish that continued investigation supports a preferred conclusion.

It does not establish that one unresolved object should receive resources before another.

It does not require every inquiry basis to remain operationally active.

The term **convergent** does not assert that inquiry necessarily approaches a fixed limit, monotonically improves, or converges mathematically to truth.

A claim that a particular inquiry converges remains a claim requiring represented support.

A possible operational decomposition is:

```text
retained unresolved material
-> generation of possible inquiry operations
-> allocation basis
-> inquiry priority
-> resource allocation
-> active inquiry
-> execution
-> evaluation
-> represented result
-> genealogical preservation and recontextualization
```

This is not a mandatory linear sequence.

Convergent Inquiry can generate possible inquiry operations without determining which receive resources.

A possible inquiry can remain represented without active examination.

## 7. Why Openness Matters

Open means that revision remains possible.

Openness does not require continuous change.

A representation can survive repeated evaluation without modification while remaining open to revision.

Likewise, openness does not require accepting every proposed revision.

A candidate can be rejected, superseded, made inactive, unallocated, or currently unranked while remaining genealogically represented.

Open inquiry and active inquiry are distinct.

An inquiry can remain open while receiving no current resources.

The distinction is between retaining a representation and insulating that representation from relevant distinction or revision.

This permits stable conclusions without requiring epistemic finality.

It also permits operational stopping or inactivity without requiring permanent closure.

Aperta Veritas therefore does not assign privileged status to novelty, preservation, complexity, simplicity, change, stability, priority, or activation.

These can be represented properties or criteria.

None defines improvement or truth by category alone.

## 8. The Evaluator Is Part of the Problem

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

It does not establish improvement independently of the evaluator, criteria, distinctions, comparison basis, support claims, measurements where applicable, conditions, and comparison set that produced the selection.

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
predecessor generator
successor generator
predecessor allocator
successor allocator
predecessor evaluator
successor evaluator
criteria
distinctions
operationalizations
measurements and other represented results
bases
acceptance bases
inquiry bases
inquiry operations
allocation bases
inquiry priorities
resource allocations
support relations
support claims
comparison basis
conditions
comparison set
selection operation
residuals
genealogy
```

The purpose is not to preserve these structures as permanently correct.

The purpose is to keep their transformation available for examination.

## 9. The Allocator Is Part of the Problem

A conventional finite inquiry process allocates attention, compute, time, storage, energy, tools, or other resources among represented possibilities.

This establishes operational activity relative to an allocator and allocation basis.

It does not establish epistemic superiority.

A recursively revisable system must therefore also be capable of representing:

\[
A_t \rightarrow A_{t+1}
\]

The successor allocator can alter:

- allocation bases;
- inquiry priorities;
- resource estimates;
- stopping conditions;
- activation thresholds;
- preservation policies;
- search budgets;
- verification budgets;
- compute distribution;
- memory distribution;
- environmental access;
- tool use.

A change in allocation can change which observations and evaluations ever become available.

This creates an allocation self-confirmation risk.

If a successor allocator increasingly directs resources toward inquiries compatible with the current system while leaving potentially disconfirming inquiries inactive, later evaluation can operate on a systematically conditioned evidence stream.

This does not establish that the successor system is false.

It exposes a dependency between allocation and later evidence.

RTE therefore preserves allocation genealogy where represented.

## 10. Distinction and Measurement

A distinction specifies a variable, category, relation, boundary, or other basis by which possibilities can differ.

A measurement is a represented result produced relative to one or more distinctions.

Therefore:

\[
\text{distinction} \neq \text{measurement}
\]

A measurement depends on the distinction applied, its operationalization, the object or process examined, the method, and the conditions under which the result was produced.

For RSI this matters across generation, allocation, and evaluation.

First, an evaluator can change what it measures by changing its distinctions.

Second, a generator can change what it can produce by changing the distinctions available to representation and search.

Third, an allocator can change which distinctions, observations, tests, or measurements receive the resources required to become operational.

A new distinction can therefore change future generation, allocation, and measurement.

## 11. Support and Measurement

Measurement and support are not identical.

A measurement can participate in a support claim when a represented relation connects it to a conclusion.

A measurement can also exist without supporting the conclusion under examination.

Support claims can involve observations, tests, predictions, contradictions, logical relations, provenance, explanatory relations, reproducibility, consequences, independent routes, and other represented bases.

Therefore:

\[
\text{support} \neq \text{measurement}
\]

and:

\[
\text{conclusion} \neq \text{support}
\]

This matters for RSI because an evaluator can change not only what is measured, but the relation by which represented results are claimed to bear on a designation of improvement.

An allocator can also change which measurements or observations are ever produced.

A system that preserves measurements while silently changing those relations can alter its evaluation architecture without exposing the change.

A system that preserves evaluation rules while silently changing allocation can alter the evidence reaching those rules without exposing the change.

## 12. Comparison Basis

A comparative judgment requires a represented basis of comparison.

A comparison basis can include:

- alternatives being compared;
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

Where no represented basis supports ranking, alternatives remain represented without ranking.

This means they are presently unranked under the represented comparison basis.

It does not establish that no comparison basis exists.

It also does not establish intrinsic incommensurability.

A claim of incommensurability itself requires represented support.

Comparison does not require every relevant relation to be converted into a common measurement.

## 13. Cross-Evaluation

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

Conversely, if both evaluators prefer \(S_{t+1}\), that convergence can participate in a represented support claim concerning improvement.

It still does not establish evaluator-independent improvement by category alone.

The independence, criteria, comparison bases, conditions, dependencies, and support claims of the evaluations remain relevant.

Cross-evaluation itself consumes resources.

A possible cross-evaluation can therefore remain unperformed because it was not allocated sufficient resources.

Failure to perform it is not equivalent to rejection of the comparison.

## 14. Generator Genealogy

A generator can change recursively:

\[
G_t \rightarrow G_{t+1}
\]

The transformation can alter:

- candidate representation;
- inquiry-operation generation;
- search strategy;
- distinctions;
- recombination;
- model structure;
- access to retained states;
- tool use;
- environmental interaction;
- resource requirements;
- allocator feedback;
- evaluator feedback;
- exploration;
- stopping rules.

A generator transition can therefore preserve:

```text
what changed
why it changed
which distinctions changed
which candidate classes became representable
which inquiry operations became representable
which candidate classes ceased to be representable
which retained branches became accessible
which search constraints changed
which allocator signals affected generation
which evaluator signals affected generation
which resources changed
which exclusions changed
which residuals remain unresolved
```

Generator revision itself becomes an object of inquiry.

This creates a recursive problem:

> How can a system generate a generator capable of producing candidates that its current generator cannot produce?

Aperta Veritas does not currently answer that question.

It makes the boundary explicit.

## 15. Allocator Genealogy

An allocator can change recursively:

\[
A_t \rightarrow A_{t+1}
\]

The transformation can alter:

- allocation bases;
- inquiry priorities;
- cost models;
- resource estimates;
- purposes;
- values;
- policies;
- activation rules;
- stopping rules;
- compute distribution;
- memory distribution;
- storage allocation;
- tool access;
- environmental access;
- verification budgets;
- preservation budgets;
- generator feedback;
- evaluator feedback.

An allocation transition can therefore preserve:

```text
what changed
why it changed
which allocation bases changed
which priorities changed
which resource conditions changed
which inquiry operations became active
which inquiry operations became inactive
which possibilities remained unallocated
which generator signals affected allocation
which evaluator signals affected allocation
which stopping conditions changed
which residuals remain unresolved
```

Allocator revision itself becomes an object of inquiry.

This creates another recursive problem:

> How can a system revise allocation without assuming that its current allocation basis is the correct basis for deciding which revisions receive resources?

Aperta Veritas does not currently answer that question.

It exposes the dependency.

## 16. The Genealogy and Recontextualization Hypothesis

One current hypothesis is that genealogy can do more than reconstruct prior decisions.

A retained representation can acquire new significance after a later distinction becomes available.

Suppose a system retains:

```text
record A
record B
```

without representing a relation between them.

A later distinction \(D\) can expose:

```text
A
-> relation R
-> B
```

The historical records do not need to be rewritten.

Instead, the new relation is added while their earlier states remain preserved.

This creates the pattern:

```text
retained state
+
new distinction
->
new represented relation
->
new candidate
->
new possible inquiry
```

The hypothesis is therefore:

> Preserved genealogy can provide material for later recontextualization and candidate generation while keeping earlier and later representations distinguishable.

This is not established.

Preservation may fail to produce useful new relations.

The relevant distinction may never be generated.

The retained material may be insufficient.

Recontextualization can produce spurious relations.

Resource costs can exceed the value of preservation.

Allocation can prevent a useful possible inquiry from becoming active.

These are empirical questions.

A related evaluator hypothesis remains:

> A permanently fixed evaluator may not be necessary if enough evaluator and transformation genealogy remains represented to keep predecessor and successor evaluations distinguishable.

A related allocation hypothesis is:

> A permanently fixed allocator may not be necessary if enough allocation basis, priority, resource, activation, and allocator genealogy remains represented to expose how finite attention changes across recursive transitions.

These also remain unestablished.

## 17. Selection Is Not Improvement

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

Generation, allocation, evaluation, selection, and designation of improvement remain separate represented relations.

A candidate can receive resources without being selected.

A selected candidate can have been chosen under operational constraints different from the criteria used in an epistemic comparison.

## 18. Open, Active, and Inactive Inquiry

A candidate that is not selected can remain represented.

A possible inquiry that receives no current resources can remain open.

Inactive does not mean false.

Unallocated does not mean rejected.

Rejected does not mean permanently irrelevant.

Failure to establish a hypothesis does not establish its negation.

A candidate or inquiry can become relevant after:

- generator revision;
- allocator revision;
- evaluator revision;
- environmental change;
- new observations;
- new distinctions;
- new measurements;
- new support claims;
- new comparison bases;
- new allocation bases;
- changed inquiry priorities;
- increased resources;
- failure of the selected branch;
- discovery of a new relation among retained records.

An unresolved branch can therefore retain an inquiry basis even when present epistemic support is weak and no resources are currently allocated.

This gives:

\[
\text{failure to establish} \neq \text{disproof}
\]

\[
\text{failure to establish} \neq \text{elimination}
\]

\[
\text{current support} \neq \text{future inquiry potential}
\]

\[
\text{open inquiry} \neq \text{active inquiry}
\]

\[
\text{not allocated} \neq \text{rejected}
\]

\[
\text{inactive} \neq \text{erased}
\]

Preserving branch genealogy prevents temporary selection or allocation from automatically becoming historical erasure.

Finite resources may still require compression or deletion.

Where detectable, that loss remains represented as loss.

## 19. Resource Constraints and Allocation

Recursive inquiry consumes resources.

A system cannot preserve every physical detail, generate every candidate, evaluate every candidate, perform every possible test, activate every possible inquiry, or recurse indefinitely.

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

Resource constraint and resource allocation remain distinct.

A resource constraint represents a limit.

Resource allocation assigns available resources among represented possibilities under an allocation basis.

A stopping or deactivation event can therefore mean:

```text
further active inquiry not allocated
under allocation basis L
resource conditions R
and stopping rule Q
```

rather than:

```text
the inquiry is complete
```

Resource allocation can change future generation.

Deleting an inactive branch can reduce storage cost while eliminating material that a later distinction could have recontextualized.

Preserving every branch can consume resources that prevent useful search elsewhere.

Lossless Inquiry therefore does not make preservation free or automatically preferable.

The resource relation and allocation decision remain represented.

Operational stopping is not epistemic closure.

## 20. Reopening

A stopped or inactive inquiry can reopen when relevant conditions change.

Possible triggers include:

- new observation;
- new distinction;
- new measurement;
- new basis;
- new inquiry basis;
- new support claim;
- new contradiction;
- newly generated candidate;
- newly generated inquiry operation;
- new comparison basis;
- generator revision;
- allocator revision;
- evaluator revision;
- changed allocation basis;
- changed inquiry priority;
- increased resources;
- implementation failure;
- environmental change;
- a new relation among previously retained records.

The stopping, deallocation, inactivity, and reopening conditions remain part of the genealogy where possible.

Reopening does not establish that the earlier stopping or allocation decision was wrong.

The represented inquiry state has changed.

## 21. Current Prototype

The current Aperta Veritas prototype is a bounded inquiry ledger.

It is intended to test whether explicit representation of inquiry genealogy can preserve distinctions that ordinary optimization loops can compress.

The prototype is not an RSI system.

It does not demonstrate autonomous recursive self-improvement.

It does not establish the genealogy, allocation, or recontextualization hypotheses.

Its role is narrower:

1. represent inquiry states;
2. preserve transitions;
3. represent distinctions independently of measurements;
4. represent bases independently of support;
5. represent support claims independently of conclusions;
6. represent generators;
7. represent evaluators;
8. represent comparison bases;
9. preserve inactive branches;
10. preserve stopping and reopening conditions;
11. expose selected semantic invariants;
12. test whether genealogy survives revision;
13. provide an executable substrate for testing generation and recontextualization semantics.

The current prototype does not yet fully represent the allocation architecture described in this note.

That gap is intentional as a research target, not evidence that the executable implementation already satisfies the conceptual specification.

The implementation should be revised when the conceptual specification exposes distinctions that it does not yet represent.

## 22. Current Implementation Gap

The conceptual architecture now explicitly separates:

```text
distinction != measurement
basis != support
acceptance_basis != support
inquiry_basis != support
inquiry_basis != inquiry_priority
inquiry_priority != support
allocation_basis != support
resource_allocation != support
inquiry_priority != resource_allocation
support != measurement
support_claim != truth
conclusion != support
evaluation != generation
generation != allocation
allocation != evaluation
inquiry_generation != inquiry_priority
inquiry_generation != resource_allocation
open_inquiry != active_inquiry
not_allocated != rejected
inactive != erased
```

It also requires the representation of:

```text
retained prior state
+
later distinction
->
new represented relation
```

without erasing the prior state.

The prototype should therefore be tested and extended so it can represent:

- distinctions independently of measurements;
- measurements independently of support;
- bases independently of support;
- acceptance bases that provide no epistemic support;
- inquiry bases that provide no epistemic support;
- inquiry bases without automatically creating priority;
- inquiry operations independently of activation;
- allocation bases independently of support;
- inquiry priorities independently of resource allocation;
- resource allocations independently of epistemic support;
- allocators and allocator transitions;
- support claims whose truth-relevance remains examinable;
- support without requiring measurement;
- measurements that provide no support for a particular conclusion;
- comparison bases that do not require a common measurement;
- alternatives that are currently unranked without declaring intrinsic incommensurability;
- explicit conclusion-support separation;
- candidate generation separately from allocation and evaluation;
- open inquiry separately from active inquiry;
- inactive and unallocated branches as future generative material;
- activation and deactivation without erasure;
- later recontextualization of retained states;
- generation of a new candidate or inquiry operation from a newly represented relation;
- preservation of both the historical representation and later recontextualization;
- allocation genealogy;
- reopening after allocator or resource changes.

These are implementation requirements derived from the current conceptual model, not claims that the prototype already satisfies them.

## 23. Research Questions

The central question is:

> **How can a recursive system generate and recognize improvements that require distinctions absent from the system currently generating and evaluating successor states?**

Related questions include:

1. How are genuinely new distinctions generated?
2. Can retained genealogy contribute to generating distinctions or candidates unavailable to the earlier system?
3. Can later distinctions reliably recontextualize prior states without producing uncontrolled spurious relations?
4. How should unresolved branches be retained without treating inquiry basis as epistemic support?
5. Can a generator expand beyond candidate classes favored by its current evaluator?
6. Can generator genealogy make failures of candidate generation empirically detectable?
7. How are possible inquiry operations generated and allocated under finite resources?
8. Can inquiry basis remain operationally distinct from inquiry priority?
9. Can inquiry priority remain operationally distinct from actual resource allocation?
10. Can an allocator avoid converting present priority into permanent elimination?
11. Can allocator genealogy expose systematic inquiry starvation?
12. Can an allocator change without silently conditioning later evidence?
13. Is a fixed allocator necessary?
14. Can allocator genealogy substitute for allocator immutability?
15. Is a fixed evaluator necessary?
16. Can evaluator genealogy substitute for evaluator immutability?
17. What minimum genealogy is required for meaningful cross-evaluation?
18. Can predecessor and successor evaluators remain comparable after architectural change?
19. What happens when no represented comparison basis survives evaluator revision?
20. Which distinctions must remain stable for measurements across revisions to remain comparable?
21. Can support claims remain comparable when measurements do not?
22. Can measurements remain numerically comparable while their semantic basis changes?
23. How much inactive and unallocated branch history must be preserved?
24. When does genealogy preservation become computationally prohibitive?
25. Can a system detect when its evaluator has become self-confirming?
26. Can a system detect when its allocator has become self-confirming?
27. Can recursive exposure itself become a self-confirming evaluator or allocator?
28. What forms of support cannot usefully be reduced to measurement?
29. What relations must remain external, if any?

Aperta Veritas does not currently answer these questions.

It provides a structure in which they can be represented and tested.

## 24. Pressure Tests

Useful experiments include:

### Generator mutation

Change the candidate-generation process while preserving allocator and evaluator structure and test whether new candidate classes become representable.

### Distinction generation

Introduce or generate a distinction unavailable to an earlier state and test whether it exposes new relations among retained records.

### Recontextualization

Preserve earlier observations with no represented relation, introduce a later distinction, and test whether a new relation can be represented without overwriting the earlier states.

### Generative recovery

Deactivate a branch, later introduce a new distinction, and test whether the retained branch contributes to a candidate or inquiry operation that could not previously be generated.

### Spurious recontextualization

Permit new relations among retained records and test whether the system can distinguish useful recontextualization from unsupported relation generation.

### Allocation without support

Allocate resources to an inquiry because it is cheap, urgent, novel, randomly sampled, or externally requested and test whether the system avoids treating allocation as epistemic support.

### Inquiry basis without priority

Represent an inquiry basis while assigning no present priority and test whether the inquiry remains open without becoming active.

### Priority without allocation

Assign high inquiry priority while withholding resources because a required dependency is unavailable and test whether priority remains distinct from allocation.

### Allocation mutation

Change the allocation basis while preserving the generator and evaluator and test whether different inquiry operations become active.

### Allocator replacement

Allow a successor to replace its allocator and test whether predecessor and successor allocation decisions remain reconstructable.

### Allocation self-confirmation

Bias allocation toward inquiries compatible with the current system and test whether RTE exposes the resulting conditioning of later evidence.

### Inquiry starvation

Generate a useful inquiry operation but repeatedly allocate insufficient resources for execution and test whether nonexecution remains distinct from rejection.

### Random allocation

Compare a designed priority function with random allocation under the same resource budget and test whether either produces greater represented information under an explicit comparison basis.

### Evaluator replacement

Allow a successor to replace its evaluator and test whether predecessor and successor judgments remain reconstructable.

### Distinction mutation

Change the distinctions used by the evaluator while preserving apparently similar measurements and test whether semantic comparability survives.

### Measurement mutation

Change the measurement procedure while preserving the criterion label and test whether the system detects the altered basis.

### Support mutation

Preserve the same measurement while changing the support claim connecting it to a conclusion and test whether the system represents the change.

### Acceptance without support

Cause a system to accept a conclusion because of authority, policy, reward, or inherited state and test whether acceptance remains distinct from epistemic support.

### Inquiry without support

Retain a hypothesis because of an unresolved anomaly while withholding epistemic support for that hypothesis and test whether the system preserves the distinction.

### Comparison-basis mutation

Preserve states and measurements while changing the comparison basis and test whether the resulting selection is distinguishable from the prior evaluation.

### Candidate omission

Remove the strongest represented candidate before evaluation and test whether the system distinguishes:

```text
best represented candidate
```

from:

```text
best possible candidate
```

### Unranked alternatives

Remove the represented comparison basis and test whether the system preserves alternatives as currently unranked without asserting intrinsic incommensurability.

### Genealogy deletion

Delete generator, allocator, or evaluator history and test which generative, allocation, or comparative claims become unreconstructable.

### Branch reactivation

Reject or deactivate a candidate, change conditions, and test whether the candidate can become active again without being regenerated from scratch.

### Resource pressure

Reduce available storage or compute and test whether the system records what genealogy was compressed or discarded, how resources were allocated, and whether the loss changes future candidate generation.

### Self-application

Allow RTE to revise its own distinctions, generation rules, allocation rules, comparison rules, or stopping conditions and test whether prior states remain distinguishable.

## 25. Failure Conditions

The research direction would be weakened if experiments show that:

- generator genealogy adds no useful information beyond ordinary search logs;
- retained unresolved branches provide no useful future generative material;
- recontextualization does not produce useful new candidate relations;
- recontextualization primarily generates unsupported associations;
- allocator genealogy adds no useful distinction beyond ordinary resource logs;
- inquiry basis, inquiry priority, and resource allocation cannot be operationally distinguished;
- explicit allocation bases add representation without improving reconstructability;
- allocation history does not help distinguish rejection from nonexecution;
- allocator revision cannot be meaningfully reconstructed;
- open and active inquiry cannot be operationally distinguished;
- evaluator genealogy adds no useful distinction beyond ordinary versioning;
- cross-evaluation becomes meaningless after modest evaluator revision;
- support claims cannot be represented without arbitrary evaluator assumptions;
- explicit comparison bases add representation without improving reconstructability;
- acceptance basis, inquiry basis, and support cannot be operationally distinguished;
- branch preservation consumes resources without providing recoverable or generative value;
- recursive exposure consistently creates more ambiguity than it resolves;
- a simpler architecture preserves the same relevant distinctions with less overhead.

These outcomes should not be excluded by definition.

They would be evidence for revising or abandoning parts of the approach.

## 26. Recursive Application

This research note is itself a represented proposal.

It selects:

- generation as a research problem;
- allocation as a research problem;
- evaluator dependence as a research problem;
- genealogy as a candidate mechanism;
- recontextualization as a candidate generative mechanism;
- Convergent Inquiry as a model for generating possible continuations;
- explicit allocation as a desired property;
- cross-evaluation as a useful test;
- openness as a desired property;
- distinction, measurement, basis, support, comparison, generation, allocation, evaluation, and conclusion as separate objects.

Those selections do not establish their own correctness.

The distinction:

\[
\text{generation} \neq \text{allocation}
\]

is itself a claim.

The distinction:

\[
\text{allocation} \neq \text{evaluation}
\]

is itself a claim.

The distinction:

\[
\text{generation} \neq \text{evaluation}
\]

is itself a claim.

The distinction:

\[
\text{basis} \neq \text{support}
\]

is itself a claim.

The distinction:

\[
\text{inquiry basis} \neq \text{inquiry priority}
\]

is itself a claim.

The distinction:

\[
\text{resource allocation} \neq \text{support}
\]

is itself a claim.

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

The hypothesis that preserved genealogy can contribute to later generation is a claim.

The hypothesis that new distinctions can usefully recontextualize prior records is a claim.

The hypothesis that allocation genealogy can expose how finite attention conditions later evidence is a claim.

The hypothesis that genealogy can preserve meaningful comparison across evaluator revision is a claim.

Each remains open to testing and revision.

## 27. Current Position

The current position is not:

> A fixed evaluator prevents RSI.

Nor is it:

> A fixed allocator prevents RSI.

Nor is it:

> Preserving every unresolved branch produces discovery.

Nor is it:

> Every possible inquiry should receive resources.

Nor is it:

> Aperta Veritas solves RSI.

The current position is:

> Recursive self-improvement contains a generation boundary because an evaluator can examine only candidates that become representable, an allocation boundary because finite resources determine which represented possibilities become active, and an evaluator boundary because the system can recursively alter the machinery by which represented successors are designated improved.

Aperta Veritas proposes explicit generator, allocator, and evaluator genealogy; separation of acceptance basis, inquiry basis, inquiry priority, allocation basis, resource allocation, and support; preservation of unresolved and unallocated branches; Convergent Inquiry; recontextualization under later distinctions; explicit comparison bases; cross-evaluation; and recursive exposure as mechanisms for studying those boundaries.

The central research hypothesis is that retained genealogy can provide material from which later distinctions make new relations, inquiry operations, and candidates representable.

A related hypothesis is that explicit allocation genealogy can expose how finite attention and resources condition which represented possibilities become examinable.

Whether these mechanisms produce useful recursive improvement, whether they scale, and whether they are sufficient remain open empirical questions.
