# Executable Prototype

This directory contains the minimum executable Aperta Veritas ledger described in [`../OPERATIONAL_SYSTEM.md`](../OPERATIONAL_SYSTEM.md).

The prototype tests whether core RTE operations can be represented computationally rather than merely stated conceptually.

## Current executable contract

The architecture requires that the implementation be capable of representing the following separately:

- inquiry states;
- conclusions;
- distinctions;
- operationalizations where applicable;
- measurements and other represented results;
- support relations;
- comparison sets;
- comparison bases;
- beliefs;
- confidence;
- values;
- evaluators;
- criteria;
- selections;
- active and inactive branches;
- stopping conditions;
- reopening conditions;
- genealogy.

The prototype should demonstrate that:

- inquiry states can be appended rather than overwritten;
- conclusions can remain distinct from the represented support for treating them as true;
- distinctions can remain distinct from measurements;
- measurements can remain distinct from support;
- support can be represented without requiring every support relation to be a measurement;
- measurements can remain represented without automatically becoming support for a conclusion;
- comparison can identify a conclusion as better supported under an explicit represented comparison basis without certifying it as definitive truth;
- comparison does not require every relevant relation to be converted into a shared measurement;
- alternatives can remain unresolved or incomparable when no represented comparison basis supports ranking;
- beliefs, confidence, values, measurements, and support can remain distinct representations;
- selected, inactive, unresolved, and superseded branches can remain genealogically represented;
- selection can require an attributed evaluator and explicit criteria;
- selection can remain distinct from improvement;
- stopping can remain distinct from epistemic closure;
- reopening conditions can remain represented;
- recursive audits can expose their own distinctions, evaluator, criteria, measurements where applicable, support relations, comparison basis, and stopping boundary;
- a hash chain can make alteration of recorded genealogy detectable.

The hash chain is tamper-evident, not physically immutable.

The prototype does not certify truth, losslessness, neutrality, completeness, exhaustive representation, or exhaustive possibility generation.

It does not assume that:

- the represented comparison set contains every possible conclusion;
- every relevant distinction has been represented;
- every relevant observation has been made;
- every measurement is valid;
- every measurement supports a conclusion;
- every support relation is a measurement;
- every pair of alternatives is comparable;
- the represented comparison basis is uniquely correct;
- the evaluator is neutral or complete.

## Semantic invariants

The executable architecture should preserve:

```text
distinction != measurement
support != measurement
conclusion != support
confidence != support
confidence != accuracy
belief != truth
value != truth
selection != improvement
best_supported != definitive_truth
stopping != closure
inactive != erased
```

These invariants are represented architectural constraints, not truth certificates.

They remain subject to Recursive Truth Exposure at the conceptual level.

## Comparison

A comparison requires an explicit represented basis for the comparison.

A comparison basis can include:

- alternatives;
- distinctions;
- criteria;
- methods;
- conditions;
- observations;
- support relations;
- measurements where applicable;
- evaluator dependencies;
- exclusions;
- unresolved relations.

A shared scalar measurement is not required by category.

Where a comparison depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions should remain represented.

Where no represented basis supports ranking alternatives, the implementation should preserve the alternatives without manufacturing a ranking.

Where relevant relations remain incommensurable, the implementation should be able to preserve that incommensurability.

## Support

Support is the represented basis by which a conclusion is treated as true.

Support can include represented relations involving:

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

A measurement can participate in support without becoming identical to support.

A support relation can participate in comparison without becoming a measurement.

A measurement can remain represented without supporting a particular conclusion.

## Distinction and measurement

A distinction specifies what can differ.

It can specify a variable, category, relation, boundary, or other basis of differentiation.

A measurement is primarily a represented result produced relative to one or more distinctions.

Operationalization specifies how a distinction is applied where such specification is needed.

The implementation should therefore be able to preserve a genealogy such as:

```text
distinction
-> operationalization
-> observation or test
-> measurement or other represented result
-> support relation
-> comparison
-> conclusion
```

This is not a mandatory linear pipeline.

Not every support relation requires a measurement.

Not every measurement becomes support.

Not every comparison requires a common measurement.

## Genealogy

The ledger should preserve enough represented genealogy to distinguish:

- a conclusion from its support;
- a support relation from a measurement;
- a measurement from the distinction under which it was produced;
- a comparison from its comparison basis;
- a selection from the comparison that preceded it;
- an inactive branch from an erased branch;
- stopping from closure;
- a revision from the state it superseded.

Detectable alteration of recorded genealogy should remain detectable through the hash chain.

This does not establish that unrecorded information was preserved.

## Current implementation status

The existing Python prototype predates the complete distinction-measurement and support-measurement corrections.

Its previously verified baseline contains 24 passing tests.

That baseline demonstrates several earlier architectural properties, including:

- append-only state representation;
- conclusion-support separation;
- explicit support records;
- explicit comparisons;
- evaluator attribution;
- active and inactive branches;
- stopping without closure;
- recursive audit records;
- tamper-evident genealogy.

The 24-test baseline does **not** by itself demonstrate compliance with the current executable contract.

The implementation must now be examined for whether it:

1. represents distinctions independently from measurements;
2. represents operationalization where applicable;
3. permits support without requiring a measurement;
4. permits measurements that do not automatically become support;
5. represents an explicit comparison basis;
6. permits defensible comparison without a shared measurement;
7. preserves absence of ranking when no represented comparison basis supports one;
8. preserves incommensurability where applicable;
9. keeps conclusion, support, measurement, and distinction separate through genealogy;
10. exposes these relations during recursive audit.

These are implementation requirements, not claims that the current prototype already satisfies them.

## Known limitation

Endogenous generation and reactivation of inactive branches are not yet implemented.

The ledger can preserve represented alternatives, but preservation does not establish exhaustive generation of the possibility space.

The next implementation revision should modify the prototype and its tests only after checking the existing code against the contract above.
