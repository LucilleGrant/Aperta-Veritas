# Executable Prototype

This directory contains the minimum executable Aperta Veritas ledger described in [`../OPERATIONAL_SYSTEM.md`](../OPERATIONAL_SYSTEM.md).

The prototype tests whether core RTE and Lossless Inquiry operations can be represented computationally rather than merely stated conceptually.

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
- inquiry bases can explain why a state remains worth examining without automatically becoming epistemic support;
- support relations can be represented without requiring every support relation to be a measurement;
- support claims can remain distinct from the support relations they cite;
- measurements can remain represented without automatically becoming support for a conclusion;
- generation can remain distinct from evaluation;
- generated candidate sets can remain explicitly non-exhaustive;
- a candidate absent from a represented search or generation event is not thereby represented as disproven;
- comparison can identify a conclusion as better supported under an explicit represented comparison basis without certifying it as definitive truth;
- comparison does not require every relevant relation to be converted into a shared measurement;
- alternatives can remain currently unranked when no represented comparison basis supports ranking without asserting intrinsic incommensurability;
- beliefs, confidence, values, measurements, bases, support relations, and support claims can remain distinct representations;
- selected, inactive, unresolved, and superseded branches can remain genealogically represented;
- selection can require an attributed evaluator and explicit criteria;
- selection can remain distinct from improvement;
- later distinctions can create newly represented relations among retained states without rewriting those earlier states;
- recontextualization can produce new inquiry material without automatically creating epistemic support;
- stopping can remain distinct from epistemic closure;
- reopening conditions can remain represented;
- recursive audits can expose their own distinctions, evaluator, criteria, measurements where applicable, bases, acceptance bases, inquiry bases, support relations, support claims, comparison basis, generation events, recontextualizations, and stopping boundary;
- a hash chain can make alteration of recorded genealogy detectable.

The hash chain is tamper-evident, not physically immutable.

The prototype does not certify truth, losslessness, neutrality, completeness, exhaustive representation, exhaustive candidate generation, or exhaustive possibility generation.

It does not assume that:

- the represented comparison set contains every possible conclusion;
- the generated candidate set contains every possible candidate;
- every relevant distinction has been represented;
- every relevant observation has been made;
- every measurement is valid;
- every measurement supports a conclusion;
- every basis provides epistemic support;
- every acceptance basis provides epistemic support;
- every inquiry basis provides epistemic support;
- every support relation is a measurement;
- every support claim is correct;
- every pair of alternatives can presently be ranked;
- failure to represent a comparison basis establishes intrinsic incommensurability;
- the represented comparison basis is uniquely correct;
- the generator is complete;
- the evaluator is neutral or complete;
- a newly represented relation is accurate merely because it became representable.

## Semantic invariants

The executable architecture should preserve:

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

These invariants are represented architectural constraints, not truth certificates.

They remain subject to Recursive Truth Exposure at the conceptual level.

## Basis, acceptance, inquiry, and support

A basis is a represented reason, condition, source, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, or support.

Recording a basis does not classify it as epistemic support.

An acceptance basis records why an agent or system accepts, selects, retains, or acts upon a represented state.

An inquiry basis records why a claim, hypothesis, observation, anomaly, relation, distinction, alternative, or unresolved branch remains a candidate for further examination.

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
support relation
!=
support claim
!=
truth
```

This sequence expresses separation, not a mandatory pipeline.

The same represented basis can participate in different relations.

For example, authority can explain why a conclusion is accepted without thereby establishing that the authority supports the truth of the conclusion.

An unresolved anomaly can provide an inquiry basis for continuing investigation without supporting a particular explanation of the anomaly.

A measurement can participate in a support relation without becoming identical to support.

A support relation can participate in comparison without becoming a measurement.

A support claim remains open to examination.

## Generation and evaluation

Generation and evaluation are represented as separate operations.

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

The core separation is:

```text
represented state
-> generator
-> generated candidate set
-> evaluator
-> selection
```

and:

```text
generation != evaluation
```

An evaluator can only evaluate candidates that have become represented to it.

A generated candidate set is therefore not treated as an exhaustive possibility space.

The implementation preserves:

```text
evaluated_candidates != exhaustive_possibility_space
absence_from_search != disproof
```

The compatibility `transition()` interface still accepts externally supplied candidate dictionaries.

Rather than hiding this upstream operation, the ledger records an explicit generation event whose generator states that candidate generation was externally supplied and incompletely represented.

The explicit `generate()` and `transition_generated()` operations allow generation and subsequent evaluation to be recorded separately.

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

It makes the relation available for subsequent testing, support claims, comparison, generation, or revision.

This is a central operational reason for genealogical preservation.

The informational significance of a retained record need not be fixed at the time the record is created.

## Genealogy

The ledger should preserve enough represented genealogy to distinguish:

- a conclusion from its support;
- a basis from a support relation;
- an acceptance basis from epistemic support;
- an inquiry basis from epistemic support;
- a support claim from truth;
- a support relation from a measurement;
- a measurement from the distinction under which it was produced;
- generation from evaluation;
- a generated candidate set from an exhaustive possibility space;
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

In this prototype, lossless inquiry does not mean that every possible fact, state, candidate, or relation is represented.

It means that represented inquiry structure is preserved strongly enough that later inquiry can inspect prior states, branches, distinctions, bases, support claims, generation events, selections, and recontextualizations rather than requiring the current state to replace its genealogy.

This matters because a branch that lacks current support can still possess an inquiry basis.

A later distinction can expose a relation that was unavailable when the branch was first represented.

That relation can then participate in new candidate generation or testing.

Therefore:

```text
failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential
```

Preservation does not require every branch to remain active.

Inactive and erased remain distinct states.

Resource constraints, stopping conditions, and reopening conditions can remain represented.

## Current implementation status

The Python prototype has been revised to implement the current generative inquiry architecture.

The implementation now:

- represents distinctions independently from measurements;
- represents operationalization as part of a distinction where applicable;
- requires measurements to reference represented distinctions;
- represents bases independently from support;
- represents acceptance bases independently from epistemic support;
- represents inquiry bases independently from epistemic support;
- permits measurements to remain represented without automatically becoming support;
- permits support without requiring a measurement;
- requires support relations to reference represented bases and state the claimed relation explicitly;
- represents support claims independently from support relations;
- represents measurements referenced by support separately from the support relation itself;
- represents generators explicitly;
- records generation events separately from evaluation and selection;
- preserves the possibility that generated candidate sets are incomplete;
- retains the earlier `transition()` interface while recording its externally supplied generation as an explicit unresolved boundary;
- permits generated candidates to be evaluated and selected through a separate transition operation;
- requires comparisons to state an explicit represented comparison basis;
- permits comparison without a shared measurement;
- preserves alternatives as currently unranked without asserting intrinsic incommensurability;
- keeps conclusions, bases, support relations, support claims, measurements, distinctions, generations, comparisons, and recontextualizations separate through ledger genealogy;
- permits later distinctions to recontextualize retained states without rewriting those states;
- permits recontextualization to produce a new inquiry state while preserving its parent states;
- does not automatically convert recontextualization into support;
- exposes distinctions, measurements, bases, acceptance bases, inquiry bases, support relations, support claims, comparisons, generation events, recontextualizations, and comparison bases during recursive audit;
- preserves stopping and reopening conditions separately;
- preserves active and inactive branches;
- maintains a tamper-evident hash chain over recorded genealogy.

The revised semantic test suite is intended to test these separations adversarially, including:

- basis without support;
- acceptance without support;
- inquiry basis without support;
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
- recursive exposure of generative and evaluative architecture;
- hash-chain detection of altered generative, support, and recontextualization records.

The test suite should be run after the current source and test revisions are committed.

A passing suite demonstrates only the implemented behaviors exercised by those tests.

It does not establish truth, completeness, exhaustive representation, losslessness, neutrality, exhaustive candidate generation, exhaustive possibility generation, or correctness outside the tested conditions.

The earlier 24-test baseline and subsequent prototype test states remain part of the implementation genealogy rather than descriptions of the current revision.

## Known limitations

The prototype now represents explicit candidate generation, but it does not autonomously discover arbitrary new distinctions, hypotheses, tests, or representations.

Its generators describe and record represented generation processes. They do not constitute a general discovery engine.

Recontextualization can represent a newly exposed relation among retained states, but the prototype does not establish that the relation is accurate merely because it was generated.

Inactive branches can retain inquiry bases and reopening conditions, but autonomous resource allocation and autonomous branch reactivation are not yet implemented.

The hash chain can expose detectable mutation of recorded genealogy, but it cannot preserve information that was never represented.

The ledger cannot establish that its represented candidate space, distinctions, support claims, generator, evaluator, or genealogy are complete.

The executable prototype remains a bounded research implementation of the current architecture, not a demonstration of general recursive self-improvement.
