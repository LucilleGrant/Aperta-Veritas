# Contributing to Aperta Veritas

Aperta Veritas is open to criticism, contradiction, revision, alternative representations, and tests of its own assumptions.

Agreement with the framework is not a condition of contribution.

A contribution also does not gain support merely by opposing the framework.

Claims, counterclaims, distinctions, measurements, support relations, methods, evaluators, comparison bases, boundaries, and revisions remain subject to the same Recursive Truth Exposure process.

## Contribution branches

Useful contributions can include:

- identifying an unrepresented relation;
- identifying a hidden dependency, assumption, incentive, or evaluator;
- providing a counterexample;
- contradicting an existing claim with represented observations, measurements, reasoning, tests, or other support;
- restricting the scope of an overgeneralized claim;
- proposing an alternative representation;
- identifying a compression loss;
- identifying a distinction that has been collapsed;
- identifying a distinction incorrectly treated as a measurement;
- identifying support incorrectly reduced to measurement;
- testing a boundary;
- formalizing an operation;
- constructing an adversarial case;
- identifying an unrepresented alternative;
- identifying a comparison-set exclusion;
- identifying an unstated comparison basis;
- adding provenance or reproduction conditions;
- identifying a proxy substituted for represented support;
- identifying confidence, consensus, value, selection, or belief substituted for truth or support;
- proposing a new distinction;
- challenging an existing distinction;
- proposing a new measurement;
- challenging an existing measurement;
- proposing or challenging a support relation;
- demonstrating an implementation failure;
- adding a test for a semantic invariant;
- reactivating a previously inactive or superseded branch.

Contributions do not need to preserve the current architecture if they expose a reason to revise it.

## Contribution format

Whenever practical, include:

1. the claim, representation, operation, implementation, or boundary being addressed;
2. the proposed change or competing representation;
3. the observations, measurements, tests, reasoning, implementation results, experience, or other represented support connected to it;
4. relevant distinctions and their operationalization where applicable;
5. relevant methods and conditions;
6. the comparison set and comparison basis where a comparative claim is being made;
7. relevant measurements where the comparison depends on measurement;
8. the evaluator and criteria where selection or value judgment is involved;
9. relevant scope and context;
10. known dependencies, exclusions, resource conditions, and residual uncertainty;
11. what observation, test, distinction, measurement, contradiction, or other represented relation could alter the proposed conclusion;
12. whether the contribution contradicts, restricts, splits, supersedes, reactivates, or remains incomparable with an existing representation.

Not every contribution requires every field.

The purpose is to preserve enough structure to distinguish the contribution from the support offered for it and to distinguish support from any particular measurement used within that support.

## Comparative claims

Claims that one representation, method, evaluator, implementation, or conclusion is more accurate, better supported, more efficient, or otherwise preferable should identify the basis of comparison and the conditions under which the comparison is made.

A comparison basis can include:

- the alternatives being compared;
- represented support;
- distinctions;
- criteria;
- methods;
- conditions;
- measurements where applicable;
- evaluator structure where applicable;
- dependencies;
- exclusions;
- unresolved or incomparable relations.

For example:

```text
A has greater represented support than B
under comparison basis K
within comparison set S
under conditions C.
```

Where comparison basis `K` depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions should remain represented.

A comparative claim does not require all support to be reduced to a common measurement.

If no represented basis supports comparison, preserve the alternatives without ranking them.

If relevant support relations remain incommensurable under the current comparison basis, preserve the incommensurability rather than manufacturing a ranking.

## Distinction and measurement

A distinction specifies what can differ.

A measurement is a represented result produced relative to one or more distinctions.

Contributions should not silently collapse these operations.

Where relevant, preserve:

```text
distinction
-> operationalization
-> observation or test
-> measurement or other represented result
```

This is not a mandatory linear sequence.

A contribution can challenge the distinction itself, its operationalization, the resulting measurement, or the relation by which that result is used as support.

## Support

Support is the represented basis by which a conclusion is treated as true.

Support can include observations, data, measurements, tests, predictions, contradictions, logical relations, provenance, explanatory relations, reproducibility, consequences, independent routes, and other represented relations relevant to a conclusion.

A measurement does not become support merely because it exists.

A represented relation must connect it to the claim or conclusion for which it is being offered as support.

Likewise, a support relation does not become a measurement merely because it participates in comparison.

Contributors should therefore preserve, where relevant:

```text
basis
-> support relation
-> claim or conclusion
```

along with relevant methods, conditions, provenance, dependencies, exclusions, uncertainty, and residuals.

## Criticism and contradiction

Criticism is not disproof by category.

Contradiction is not automatically decisive.

A criticism can expose:

- a false claim;
- an unsupported inference;
- an omitted alternative;
- an inadequate distinction;
- a defective operationalization;
- an invalid measurement;
- a missing support relation;
- an inappropriate comparison basis;
- an implementation error;
- an unstated evaluator;
- an overgeneralization;
- a representation limit;
- a genuine unresolved contradiction.

The criticism and the original claim both remain represented strongly enough to examine the relation between them.

A contradiction should identify what is contradicted and the represented basis of the contradiction.

## Alternatives and inactive branches

A competing representation should not be erased merely because another branch is selected.

When practical, preserve:

- the alternative;
- its support;
- its contradictions;
- its relation to the selected branch;
- the comparison basis used;
- the selection event;
- the reason it became inactive;
- conditions under which it could become relevant again.

Inactive does not mean false.

Superseded does not mean erased.

Selection does not mean improvement.

## Boundary Testing

A contribution can challenge a boundary.

Pressure against a boundary does not establish that the boundary is false, harmful, or unnecessary.

Resistance by the boundary does not establish that it is true, beneficial, or necessary.

Where a test crosses or pressures a boundary, record:

- the boundary;
- the test;
- relevant distinctions;
- relevant observations or measurements;
- conditions;
- what changed;
- what did not change;
- resulting support relations;
- unresolved interpretations.

Claims about the function of the boundary remain claims requiring represented support.

## Values and evaluators

Contributors can propose values, criteria, priorities, and evaluator structures.

Their status as values or evaluators does not establish or negate truth.

When a contribution calls something:

- better;
- worse;
- safer;
- harmful;
- useful;
- efficient;
- preferable;
- aligned;
- improved;

the evaluator, criterion, comparison basis, and relevant conditions should be represented where practical.

This does not prohibit evaluative language.

It exposes the relation producing the evaluation.

## Implementation contributions

Code changes should preserve the semantic distinctions claimed by the framework or explicitly document where the implementation does not yet represent them.

Particular attention should be given to:

```text
distinction != measurement
support != measurement
conclusion != support
confidence != support
confidence != accuracy
consensus != support
belief != truth
fact != definitive_truth
value != truth
selection != improvement
relational_richness != accuracy
best_supported != definitive_truth
stopping != closure
inactive != erased
```

Tests should attack these distinctions rather than merely confirm expected outputs.

A passing implementation test does not establish the conceptual framework as true.

A failing test does not by itself establish the conceptual framework as false.

The relation between specification, implementation, test, and result remains represented.

## Recursive application

These contribution rules are themselves subject to contribution.

A contributor can challenge:

- the required fields;
- the definition of contribution;
- the distinction between support and measurement;
- the distinction between distinction and measurement;
- the comparison architecture;
- the treatment of alternatives;
- the branch-preservation protocol;
- the semantic invariants;
- the implementation requirements;
- the contribution process itself.

The contribution protocol must not become a protected layer that Aperta Veritas refuses to examine.

## Minimal principle

A contribution does not need to agree with Aperta Veritas.

It needs enough represented structure for its relation to the current framework to be examined without silently converting disagreement, measurement, confidence, consensus, value, or selection into truth.
