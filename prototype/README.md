# Executable Prototype

This directory contains the minimum executable Aperta Veritas ledger described in [`../OPERATIONAL_SYSTEM.md`](../OPERATIONAL_SYSTEM.md).

The prototype tests whether core RTE, Convergent Inquiry, and Lossless Inquiry operations can be represented computationally rather than merely stated conceptually.

## Current executable contract

The architecture requires that the implementation be capable of representing the following separately:

- inquiry states;
- conclusions;
- distinctions;
- operationalizations where applicable;
- measurements and other represented results;
- bases;
- acceptance bases;
- inquiry bases;
- inquiry operations;
- allocation bases;
- inquiry priorities;
- allocators;
- resource allocations;
- activation and deactivation events;
- support relations;
- support claims;
- comparison sets;
- comparison bases;
- beliefs;
- confidence;
- values;
- generators;
- generation events;
- evaluators;
- criteria;
- selections;
- active and inactive branches;
- recontextualizations;
- stopping conditions;
- reopening conditions;
- genealogy.

The prototype should demonstrate that:

- inquiry states can be appended rather than overwritten;
- conclusions can remain distinct from the represented support claims concerning whether they should presently be treated as true;
- distinctions can remain distinct from measurements;
- measurements can remain distinct from support;
- bases can remain distinct from support;
- acceptance bases can explain why a state is accepted, selected, retained, or acted upon without automatically becoming epistemic support;
- inquiry bases can represent conditions under which further examination could occur without automatically becoming epistemic support, inquiry priority, or resource allocation;
- possible inquiry operations can be represented without automatically becoming active;
- inquiry priority can remain distinct from inquiry basis and resource allocation;
- allocation bases can remain distinct from epistemic support;
- resource allocations can remain distinct from epistemic support;
- an allocator can remain explicitly represented rather than hidden inside an apparently neutral priority or activation decision;
- allocation can remain distinct from generation and evaluation;
- an inquiry operation can remain open but inactive;
- an unallocated inquiry operation can remain represented without being treated as rejected;
- deactivation can remain distinct from erasure or epistemic closure;
- support relations can be represented without requiring every support relation to be a measurement;
- support claims can remain distinct from the support relations they cite;
- measurements can remain represented without automatically becoming support for a conclusion;
- generation can remain distinct from evaluation;
- generated candidate sets can remain explicitly non-exhaustive;
- a candidate absent from a represented search or generation event is not thereby represented as disproven;
- comparison can identify a conclusion as better supported under an explicit represented comparison basis without certifying it as definitive truth;
- comparison does not require every relevant relation to be converted into a shared measurement;
- alternatives can remain currently unranked when no represented comparison basis supports ranking without asserting intrinsic incommensurability;
- beliefs, confidence, values, measurements, bases, allocation bases, priorities, resource allocations, support relations, and support claims can remain distinct representations;
- selected, inactive, unresolved, superseded, allocated, and unallocated branches or operations can remain genealogically represented;
- selection can require an attributed evaluator and explicit criteria;
- allocation can require an attributed allocator and explicit allocation basis;
- selection can remain distinct from improvement;
- allocation can remain distinct from support;
- later distinctions can create newly represented relations among retained states without rewriting those earlier states;
- recontextualization can produce new inquiry material without automatically creating epistemic support;
- stopping can remain distinct from epistemic closure;
- reopening conditions can remain represented;
- recursive audits can expose their own distinctions, evaluator, criteria, measurements where applicable, bases, acceptance bases, inquiry bases, inquiry operations, allocation bases, inquiry priorities, resource allocations, activation events, support relations, support claims, comparison basis, generation events, recontextualizations, and stopping boundary;
- a hash chain can make alteration of recorded genealogy detectable.

The hash chain is tamper-evident, not physically immutable.

The prototype does not certify truth, losslessness, neutrality, completeness, exhaustive representation, exhaustive candidate generation, exhaustive inquiry generation, exhaustive possibility generation, optimal allocation, or exhaustive evaluation.

It does not assume that:

- the represented comparison set contains every possible conclusion;
- the generated candidate set contains every possible candidate;
- the represented inquiry operations contain every possible continuation of inquiry;
- every relevant distinction has been represented;
- every relevant observation has been made;
- every measurement is valid;
- every measurement supports a conclusion;
- every basis provides epistemic support;
- every acceptance basis provides epistemic support;
- every inquiry basis provides epistemic support;
- every inquiry basis should receive priority;
- every possible inquiry operation should receive resources;
- priority establishes epistemic support;
- allocation establishes epistemic support;
- nonallocation establishes rejection;
- inactivity establishes erasure;
- every support relation is a measurement;
- every support claim is correct;
- every pair of alternatives can presently be ranked;
- failure to represent a comparison basis establishes intrinsic incommensurability;
- the represented comparison basis is uniquely correct;
- the generator is complete;
- the allocator is neutral, complete, or optimal;
- the evaluator is neutral or complete;
- a newly represented relation is accurate merely because it became representable.

## Semantic invariants

The executable architecture should preserve:

```text
distinction != measurement

basis != support
acceptance_basis != support
inquiry_basis != support
allocation_basis != support
inquiry_priority != support
resource_allocation != support

inquiry_basis != inquiry_priority
inquiry_priority != resource_allocation

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

generation != allocation
allocation != evaluation
evaluation != generation

inquiry_generation != inquiry_priority
inquiry_generation != resource_allocation

evaluated_candidates != exhaustive_possibility_space

relational_richness != accuracy
best_supported != definitive_truth

failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential

unranked != necessarily_incommensurable

open_inquiry != active_inquiry
not_allocated != rejected
inactive != erased

stopping != closure
```

These invariants are represented architectural constraints, not truth certificates.

They remain subject to Recursive Truth Exposure at the conceptual level.

## Basis, acceptance, inquiry, allocation, and support

A basis is a represented reason, condition, source, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, inquiry, allocation, evaluation, or support.

Recording a basis does not classify it as epistemic support.

An acceptance basis records why an agent or system accepts, selects, retains, or acts upon a represented state.

An inquiry basis is a represented basis under which further examination of a claim, hypothesis, observation, anomaly, relation, distinction, alternative, unresolved branch, or other represented object could occur.

An inquiry basis does not by itself establish that the object should receive priority or resources.

An inquiry operation is a represented possible continuation of inquiry.

An allocation basis records represented criteria, conditions, constraints, purposes, policies, values, costs, expected consequences, or other bases used in allocating resources among possible inquiry operations.

An inquiry priority records a represented ordering or preference among possible inquiry operations under an explicit allocation basis and represented conditions.

A resource allocation records a represented assignment of available resources to one or more inquiry operations under represented conditions.

An allocator records a represented process participating in resource allocation.

A support relation is a claimed relation between one or more represented bases and whether a conclusion should presently be treated as true under represented conditions.

A support claim asserts that one or more represented support relations bear on whether the conclusion is true.

Therefore:

```text
basis
!=
acceptance basis
!=
inquiry basis
!=
inquiry priority
!=
resource allocation
!=
support relation
!=
support claim
!=
truth
```

This sequence expresses separation, not a mandatory pipeline.

The same represented basis can participate in different relations.

For example, authority can explain why a conclusion is accepted without thereby establishing that the authority supports the truth of the conclusion.

An unresolved anomaly can provide an inquiry basis under which further investigation could occur without supporting a particular explanation of the anomaly.

A possible inquiry operation can remain represented without receiving priority.

A high-priority inquiry operation can remain unallocated when required resources are unavailable.

An allocated inquiry operation does not thereby acquire epistemic support.

A measurement can participate in a support relation without becoming identical to support.

A support relation can participate in comparison without becoming a measurement.

A support claim remains open to examination.

## Convergent Inquiry

The executable architecture treats Convergent Inquiry as the generation and examination of possible continuations of unresolved inquiry, including new:

- distinctions;
- relations;
- hypotheses;
- operationalizations;
- methods;
- observations;
- tests;
- measurements;
- comparison bases;
- support claims;
- inquiry operations.

Convergent Inquiry does not establish that continued investigation supports a preferred conclusion.

It does not establish that every inquiry basis should receive resources.

It does not require every possible inquiry operation to become active.

It does not imply mathematical convergence, monotonic improvement, a fixed limit, or guaranteed approach to truth.

The executable prototype can represent possible inquiry operations and their allocation genealogy.

It does not contain a neutral or autonomous procedure that determines which possible inquiries should receive resources.

## Generation, allocation, activation, and evaluation

Generation, allocation, activation, and evaluation are represented as distinct operations.

A generator records a represented process by which candidate states become available.

A generation event records:

- source states;
- the generator;
- generated states;
- the represented generation operation;
- relevant distinctions;
- represented alternatives;
- known exclusions;
- whether unrepresented alternatives may remain;
- resource costs;
- conditions;
- residuals.

An inquiry operation records a possible continuation of inquiry.

An allocation basis records what represented criteria or conditions are being used to allocate resources.

An inquiry priority can represent an ordering among inquiry operations without itself allocating resources.

An allocator records the represented process participating in allocation.

A resource allocation records which represented inquiry operations received resources, which did not, the represented allocator, allocation bases, priority where applicable, resource assignments, conditions, dependencies, and residuals.

An activation event records that an allocated inquiry operation became active.

A deactivation event records that an inquiry operation ceased to be active without requiring the operation or its inquiry basis to be erased.

The core separations include:

```text
represented state
-> generator
-> generated candidate set
-> evaluator
-> selection
```

and, for inquiry operations:

```text
retained represented state
-> inquiry basis
-> possible inquiry operation
-> allocation basis / inquiry priority
-> allocator
-> resource allocation
-> activation
-> active inquiry
-> represented result
-> evaluation
```

These are architectural relations, not mandatory linear pipelines.

The executable invariants include:

```text
generation != allocation
allocation != evaluation
evaluation != generation

inquiry_basis != inquiry_priority
inquiry_priority != resource_allocation

open_inquiry != active_inquiry
not_allocated != rejected
inactive != erased
```

An evaluator can only evaluate candidates that have become represented to it.

An allocator can only allocate among represented possibilities available to it.

A generated candidate set is therefore not treated as an exhaustive possibility space.

A represented set of inquiry operations is likewise not treated as an exhaustive inquiry possibility space.

The implementation preserves:

```text
evaluated_candidates != exhaustive_possibility_space
absence_from_search != disproof
not_allocated != rejected
```

The compatibility `transition()` interface still accepts externally supplied candidate dictionaries.

Rather than hiding this upstream operation, the ledger records an explicit generation event whose generator states that candidate generation was externally supplied and incompletely represented.

The compatibility path also records allocation as an unresolved boundary rather than pretending that candidate selection supplies a complete allocation genealogy.

The explicit `generate()` and `transition_generated()` operations allow generation and subsequent evaluation to be recorded separately.

The allocation API separately represents inquiry operations, allocation bases, inquiry priorities, resource allocations, and activation events.

## Inquiry operations and allocation

The prototype represents a possible inquiry continuation with `InquiryOperation`.

An inquiry operation can reference:

- target states;
- inquiry bases;
- the represented operation;
- requirements;
- expected outputs;
- conditions;
- dependencies;
- provenance;
- residuals.

Recording an inquiry operation does not automatically prioritize, allocate, activate, support, or evaluate it.

An `AllocationBasis` records:

- the represented account;
- basis IDs;
- allocation criteria;
- conditions;
- constraints;
- purposes;
- provenance;
- residuals.

An `InquiryPriority` records an ordering over an explicit set of represented inquiry operations under an allocation basis.

Priority remains distinct from allocation.

A `ResourceAllocation` records:

- the allocator;
- represented inquiry operations;
- allocation bases;
- an inquiry priority where applicable;
- assigned resources;
- explicitly unallocated operations;
- conditions;
- dependencies;
- residuals.

Every inquiry operation represented by a resource-allocation event must be accounted for as either assigned resources or explicitly unallocated within that event.

This prevents disappearance from the allocation record from being silently interpreted as rejection.

The allocator can expose:

- criteria;
- allocation bases;
- resource conditions;
- constraints;
- generator feedback;
- evaluator feedback;
- conditions;
- exclusions;
- residuals.

The prototype does not assume a neutral allocator.

Possible allocation criteria can include represented cost, available resources, expected information gain, urgency, tractability, novelty, anomaly density, external requests, random sampling, safety constraints, or other represented bases.

Their use in allocation does not make them epistemic support.

## Open and active inquiry

Open inquiry and active inquiry are distinct.

Open inquiry permits relevant future examination or revision.

Active inquiry is currently receiving represented resources for examination.

Therefore an inquiry can be:

- open and active;
- open and inactive;
- deactivated while retaining reopening conditions.

The prototype does not treat inactivity as erasure.

It does not treat nonallocation as rejection.

Conceptually:

```text
inquiry basis exists
-> possible inquiry operation represented
-> operation receives no current allocation
-> operation remains represented
-> later allocation conditions change
-> operation can receive resources
-> operation can become active
```

Operational stopping does not require epistemic closure.

Deactivation can preserve stopping conditions and reopening conditions.

## Comparison

A comparison requires an explicit represented basis for the comparison.

A comparison basis can include:

- alternatives;
- distinctions;
- criteria;
- methods;
- conditions;
- observations;
- bases;
- support relations;
- support claims;
- measurements where applicable;
- evaluator dependencies;
- generator dependencies;
- allocator dependencies where relevant;
- allocation history where relevant;
- exclusions;
- unresolved relations.

A shared scalar measurement is not required by category.

Where a comparison depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions should remain represented.

Where no represented basis supports ranking alternatives, the implementation can preserve the alternatives as currently unranked.

For example:

```text
currently unranked
under represented comparison basis B
```

Failure to represent a ranking basis does not establish that no such basis exists.

The implementation therefore does not encode current failure to rank as intrinsic incommensurability.

A claim that alternatives are intrinsically incommensurable would itself require represented support.

A comparison can identify one or more conclusions as best supported under its represented basis and conditions.

That designation is not a truth certificate.

Allocation history can affect what evidence becomes available to later comparison.

That fact does not make allocation itself epistemic support.

## Distinction and measurement

A distinction specifies what can differ.

It can specify a variable, category, relation, boundary, or other basis of differentiation.

A measurement is primarily a represented result produced relative to one or more distinctions.

Operationalization specifies how a distinction is applied where such specification is needed.

The implementation can therefore preserve a genealogy such as:

```text
distinction
-> operationalization
-> observation or test
-> measurement or other represented result
-> basis
-> claimed support relation
-> support claim
-> comparison
-> conclusion
```

This is not a mandatory linear pipeline.

Not every basis becomes support.

Not every support relation requires a measurement.

Not every measurement becomes support.

Not every support claim is correct.

Not every comparison requires a common measurement.

A new distinction can also make a relation among retained records representable that was unavailable under earlier distinctions.

## Recontextualization

The prototype represents recontextualization explicitly.

A recontextualization records a later represented relation involving retained earlier states and one or more represented distinctions.

Conceptually:

```text
retained state A
+
retained state B
+
new distinction D
->
new represented relation R
```

The earlier states remain unchanged.

The new relation is appended to the genealogy.

Where useful, the recontextualization can also produce a new inquiry state whose parents are the retained earlier states.

This permits later inquiry to use earlier records without overwriting the conditions or representations under which those records were originally produced.

Recontextualization does not certify the new relation as true.

It makes the relation available for subsequent testing, support claims, comparison, generation, allocation, or revision.

A recontextualized relation can also create a new inquiry basis or possible inquiry operation.

Whether that inquiry operation receives resources remains a separate allocation question.

This is a central operational reason for genealogical preservation.

The informational significance of a retained record need not be fixed at the time the record is created.

## Genealogy

The ledger should preserve enough represented genealogy to distinguish:

- a conclusion from its support;
- a basis from a support relation;
- an acceptance basis from epistemic support;
- an inquiry basis from epistemic support;
- an inquiry basis from inquiry priority;
- an inquiry operation from its allocation;
- an allocation basis from epistemic support;
- an inquiry priority from resource allocation;
- a resource allocation from epistemic support;
- an allocator from an evaluator;
- an allocation from activation;
- an open inquiry from an active inquiry;
- an unallocated inquiry operation from a rejected operation;
- a deactivated operation from an erased operation;
- a support claim from truth;
- a support relation from a measurement;
- a measurement from the distinction under which it was produced;
- generation from allocation;
- generation from evaluation;
- allocation from evaluation;
- a generated candidate set from an exhaustive possibility space;
- a represented inquiry-operation set from an exhaustive inquiry possibility space;
- a comparison from its comparison basis;
- a selection from the generation and evaluation that preceded it;
- an inactive branch from an erased branch;
- a recontextualized relation from the earlier records it relates;
- stopping from closure;
- a revision from the state it superseded.

Detectable alteration of recorded genealogy should remain detectable through the hash chain.

This does not establish that unrecorded information was preserved.

It also does not establish that the represented genealogy is complete.

## Lossless Inquiry

In this prototype, lossless inquiry does not mean that every possible fact, state, candidate, inquiry operation, allocation, or relation is represented.

It means that represented inquiry structure is preserved strongly enough that later inquiry can inspect prior states, branches, distinctions, bases, support claims, generation events, inquiry operations, allocation bases, priorities, resource allocations, activation events, selections, and recontextualizations rather than requiring the current state to replace its genealogy.

This matters because a branch that lacks current support can still possess an inquiry basis.

An inquiry basis can generate a possible inquiry operation without establishing that the operation should receive priority.

An inquiry operation can remain unallocated without being rejected.

An open inquiry can remain inactive without being erased.

A later distinction can expose a relation that was unavailable when the branch was first represented.

That relation can then participate in new candidate generation, inquiry generation, allocation, or testing.

Therefore:

```text
failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential

inquiry_basis != inquiry_priority
inquiry_priority != resource_allocation

not_allocated != rejected
inactive != erased
```

Preservation does not require every branch to remain active.

It also does not require every possible inquiry operation to receive resources.

Finite resources require allocation.

The architecture therefore preserves the represented allocation basis, allocator, priority where applicable, resource assignment, unallocated alternatives, conditions, and residuals rather than treating resource assignment as epistemically neutral.

Resource constraints, stopping conditions, deactivation events, and reopening conditions can remain represented.

## Current implementation status

The Python prototype has been revised to implement the current generation-allocation-evaluation architecture.

The implementation now:

- represents distinctions independently from measurements;
- represents operationalization as part of a distinction where applicable;
- requires measurements to reference represented distinctions;
- represents bases independently from support;
- represents acceptance bases independently from epistemic support;
- represents inquiry bases independently from epistemic support and inquiry priority;
- represents possible inquiry operations independently from priority and allocation;
- represents allocation bases independently from epistemic support;
- represents inquiry priorities independently from resource allocations;
- represents allocators explicitly;
- records assigned and unallocated inquiry operations in resource-allocation events;
- requires every operation in an allocation event to be accounted for as allocated or explicitly unallocated;
- represents activation separately from allocation;
- represents deactivation without erasing the inquiry operation;
- permits stopping and reopening conditions to remain represented during deactivation;
- permits measurements to remain represented without automatically becoming support;
- permits support without requiring a measurement;
- requires support relations to reference represented bases and state the claimed relation explicitly;
- represents support claims independently from support relations;
- represents measurements referenced by support separately from the support relation itself;
- represents generators explicitly;
- records generation events separately from evaluation and selection;
- preserves the possibility that generated candidate sets are incomplete;
- retains the earlier `transition()` interface while recording externally supplied generation and unresolved allocation as explicit boundaries;
- permits generated candidates to be evaluated and selected through a separate transition operation;
- permits transitions to reference represented resource allocations and activation events where applicable;
- requires comparisons to state an explicit represented comparison basis;
- permits comparison without a shared measurement;
- preserves alternatives as currently unranked without asserting intrinsic incommensurability;
- keeps conclusions, bases, inquiry operations, allocation bases, priorities, allocations, activations, support relations, support claims, measurements, distinctions, generations, comparisons, and recontextualizations separate through ledger genealogy;
- permits later distinctions to recontextualize retained states without rewriting those states;
- permits recontextualization to produce a new inquiry state while preserving its parent states;
- does not automatically convert recontextualization into support;
- exposes distinctions, measurements, bases, acceptance bases, inquiry bases, inquiry operations, allocation bases, inquiry priorities, resource allocations, activation events, support relations, support claims, comparisons, generation events, recontextualizations, and comparison bases during recursive audit;
- preserves stopping and reopening conditions separately;
- preserves active and inactive branches;
- preserves open but inactive inquiry possibilities;
- maintains a tamper-evident hash chain over recorded genealogy.

The revised semantic test suite tests these separations adversarially, including:

- basis without support;
- acceptance without support;
- inquiry basis without support;
- inquiry basis without priority or allocation;
- inquiry operation without priority or allocation;
- allocation basis without support;
- priority without resource allocation;
- resource allocation without support;
- unallocated inquiry operations preserved without rejection;
- open inquiry without active inquiry;
- activation requiring represented resource allocation;
- activation without automatic support or evaluation;
- deactivation without erasure;
- reopening conditions after deactivation;
- priority ordering integrity;
- allocation and priority operation-set consistency;
- measurement without support;
- support without measurement;
- support claim separate from support relation;
- generation without evaluation;
- selection restricted to generated candidates;
- generated candidate sets that remain explicitly non-exhaustive;
- inactive branches retaining inquiry basis;
- currently unranked alternatives without intrinsic incommensurability;
- best-supported conclusions without truth certification;
- recontextualization without erasure;
- recontextualization without automatic support;
- recursive exposure of generative, allocative, and evaluative architecture;
- hash-chain detection of altered generative, support, and recontextualization records.

The test suite should be run after the current source, test, and documentation revisions are committed.

A passing suite demonstrates only the implemented behaviors exercised by those tests.

It does not establish truth, completeness, exhaustive representation, losslessness, neutrality, exhaustive candidate generation, exhaustive inquiry generation, exhaustive possibility generation, optimal allocation, or correctness outside the tested conditions.

The earlier 24-test baseline and subsequent prototype test states remain part of the implementation genealogy rather than descriptions of the current revision.

## Known limitations

The prototype now represents explicit candidate generation and explicit inquiry allocation, but it does not autonomously discover arbitrary new distinctions, hypotheses, tests, inquiry operations, or representations.

Its generators describe and record represented generation processes. They do not constitute a general discovery engine.

Its allocators describe and record represented allocation processes. They do not constitute a neutral or autonomous solution to inquiry prioritization.

The prototype can represent priorities, resource assignments, unallocated operations, activation, deactivation, and reopening conditions, but it does not autonomously decide which inquiry operations should receive resources.

Recontextualization can represent a newly exposed relation among retained states, but the prototype does not establish that the relation is accurate merely because it was generated.

Open but inactive inquiry operations can remain genealogically represented for later allocation or reactivation.

The hash chain can expose detectable mutation of recorded genealogy, but it cannot preserve information that was never represented.

The ledger cannot establish that its represented candidate space, inquiry-operation space, distinctions, support claims, generator, allocator, evaluator, or genealogy are complete.

The executable prototype remains a bounded research implementation of the current architecture, not a demonstration of general recursive self-improvement.
