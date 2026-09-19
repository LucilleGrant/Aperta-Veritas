# Contributing to Aperta Veritas

Aperta Veritas is open to criticism, contradiction, revision, alternative representations, new distinctions, new generators, and tests of its own assumptions.

Agreement with the framework is not a condition of contribution.

A contribution also does not gain support merely by opposing the framework.

Claims, counterclaims, distinctions, measurements, bases, acceptance bases, inquiry bases, support claims, methods, generators, evaluators, comparison bases, boundaries, and revisions remain subject to the same Recursive Truth Exposure process.

## Contribution branches

Useful contributions can include:

- identifying an unrepresented relation;
- identifying a hidden dependency, assumption, incentive, generator, or evaluator;
- providing a counterexample;
- contradicting an existing claim with represented observations, measurements, reasoning, tests, or support claims;
- restricting the scope of an overgeneralized claim;
- proposing an alternative representation;
- identifying a compression loss;
- identifying a distinction that has been collapsed;
- identifying a distinction incorrectly treated as a measurement;
- identifying a basis incorrectly treated as epistemic support;
- identifying an acceptance basis incorrectly treated as support;
- identifying an inquiry basis incorrectly treated as support;
- identifying support incorrectly reduced to measurement;
- identifying a support claim whose truth-relevance has not been established;
- testing a boundary;
- identifying a generative boundary;
- formalizing an operation;
- constructing an adversarial case;
- identifying an unrepresented alternative;
- identifying a candidate-generation failure;
- identifying a comparison-set exclusion;
- identifying an unstated comparison basis;
- adding provenance or reproduction conditions;
- identifying a proxy substituted for represented support;
- identifying confidence, consensus, value, selection, reward, or belief substituted for truth or support;
- proposing a new distinction;
- challenging an existing distinction;
- proposing a new measurement;
- challenging an existing measurement;
- proposing or challenging a support relation;
- proposing or challenging a support claim;
- proposing or challenging an inquiry basis;
- proposing or challenging a generator;
- demonstrating an implementation failure;
- adding a test for a semantic invariant;
- reactivating a previously inactive or superseded branch;
- showing that a later distinction changes the represented relations among retained records;
- showing that retained genealogy enables a candidate, hypothesis, relation, or test that was previously unavailable.

Contributions do not need to preserve the current architecture if they expose a reason to revise it.

## Contribution format

Whenever practical, include:

1. the claim, representation, operation, implementation, generator, evaluator, or boundary being addressed;
2. the proposed change or competing representation;
3. the observations, measurements, tests, reasoning, implementation results, experience, bases, or support claims connected to it;
4. relevant distinctions and their operationalization where applicable;
5. relevant methods and conditions;
6. the acceptance basis where the contribution concerns why something is accepted, selected, retained, or acted upon;
7. the inquiry basis where the contribution concerns why something should remain under examination;
8. the support relation and support claim where the contribution concerns whether something should presently be treated as true;
9. the comparison set and comparison basis where a comparative claim is being made;
10. relevant measurements where the comparison depends on measurement;
11. the generator where candidate production is relevant;
12. the evaluator and criteria where evaluation, selection, or value judgment is involved;
13. relevant scope and context;
14. known dependencies, exclusions, resource conditions, and residual uncertainty;
15. what observation, test, distinction, measurement, contradiction, relation, support claim, or other represented change could alter the proposed conclusion;
16. whether the contribution contradicts, restricts, splits, supersedes, reactivates, recontextualizes, or remains currently unranked relative to an existing representation.

Not every contribution requires every field.

The purpose is to preserve enough structure to distinguish:

```text
candidate generation
from
candidate evaluation

acceptance
from
epistemic support

continued inquiry
from
epistemic support

basis
from
support

measurement
from
support

conclusion
from
support
```

A contribution can be worth investigating without being treated as true.

A contribution can also be accepted for implementation without its acceptance basis becoming epistemic support for every claim it contains.

## Comparative claims

Claims that one representation, method, generator, evaluator, implementation, or conclusion is more accurate, better supported, more efficient, or otherwise preferable should identify the basis of comparison and the conditions under which the comparison is made.

A comparison basis can include:

- the alternatives being compared;
- represented support relations and support claims;
- distinctions;
- criteria;
- methods;
- conditions;
- measurements where applicable;
- generator structure where applicable;
- evaluator structure where applicable;
- dependencies;
- exclusions;
- unresolved relations.

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

Represent this as:

```text
currently unranked
under represented comparison basis K
```

where appropriate.

Failure to represent a comparison basis does not establish that no comparison basis exists.

Do not classify alternatives as intrinsically incommensurable merely because the current framework cannot rank them.

A claim of incommensurability is itself a claim requiring represented support.

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

A contribution can challenge the distinction itself, its operationalization, the resulting measurement, or the support claim connecting that result to a conclusion.

A new distinction can also expose relations among prior records that were not representable when those records were produced.

Therefore a contribution can legitimately alter the current relational context of earlier records without rewriting those earlier records.

## Basis and support

A basis is a represented reason, condition, source, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, or support.

A basis is not automatically epistemic support.

An acceptance basis records why an agent or system accepts, selects, retains, or acts upon a conclusion.

An inquiry basis records why a claim, hypothesis, observation, anomaly, relation, distinction, alternative, or unresolved branch remains a candidate for further examination.

A support relation is a claimed relation between one or more bases and whether a conclusion should presently be treated as true under represented conditions.

A support claim asserts that such a relation bears on whether the conclusion is true.

Therefore:

```text
basis != support
acceptance_basis != support
inquiry_basis != support
support_claim != truth
```

Authority, policy, consensus, reward, habit, repetition, inherited state, or system architecture can explain why something is accepted without thereby supporting its truth.

An anomaly, unresolved contradiction, missing distinction, incomplete model, unexplored alternative, or possible discriminating test can provide an inquiry basis without supporting a particular explanation as true.

A measurement does not become support merely because it exists.

A represented support claim must specify how a basis is claimed to bear on the conclusion under examination.

Likewise, a support relation does not become a measurement merely because it participates in comparison.

Contributors should therefore preserve, where relevant:

```text
basis
-> claimed support relation
-> support claim concerning conclusion
```

along with relevant distinctions, methods, conditions, provenance, dependencies, exclusions, uncertainty, and residuals.

The support claim itself remains open to examination.

## Generation and evaluation

Evaluation operates on represented candidates.

It does not by itself determine which candidates become represented.

Contributors should preserve:

```text
generation != evaluation
```

A contribution concerning search, discovery, hypothesis generation, successor generation, test generation, or representation should identify the relevant generator where practical.

A generator can be constrained by:

- architecture;
- current distinctions;
- representation formats;
- training;
- search procedures;
- retrieval;
- tools;
- environmental access;
- evaluator feedback;
- policy;
- compute;
- memory;
- retained genealogy;
- pruning;
- randomness.

A candidate absent from evaluation may have been rejected before selection.

It may also never have been generated.

These are different events.

Therefore:

```text
evaluated_candidates != exhaustive_possibility_space
absence_from_search != disproof
```

A contribution can expose a generative failure without already possessing the missing solution.

For example, demonstrating that a candidate class cannot be represented under the current generator is itself relevant even when the contributor cannot yet generate the required candidate.

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
- a basis incorrectly classified as support;
- a missing support relation;
- a defective support claim;
- an inappropriate comparison basis;
- an implementation error;
- an unstated generator;
- an unstated evaluator;
- a generation failure;
- an overgeneralization;
- a representation limit;
- a genuine unresolved contradiction.

The criticism and the original claim both remain represented strongly enough to examine the relation between them where practical.

A contradiction should identify what is contradicted and the represented basis of the contradiction.

A criticism can itself be unsupported, incorrectly framed, or generated from an inadequate distinction.

It remains subject to the same inquiry.

## Alternatives and inactive branches

A competing representation should not be erased merely because another branch is selected.

When practical, preserve:

- the alternative;
- its acceptance basis where relevant;
- its inquiry basis;
- its support claims;
- its contradictions;
- its relation to the selected branch;
- the comparison basis used;
- the selection event;
- the reason it became inactive;
- conditions under which it could become relevant again.

Inactive does not mean false.

Superseded does not mean erased.

Selection does not mean improvement.

Failure to establish does not mean disproof.

Failure to establish does not by itself provide a basis for elimination.

Current support does not determine all future inquiry potential.

A branch with weak current support can remain represented because a later distinction, observation, relation, method, test, or resource change could make it relevant.

This does not require treating the branch as true.

## Recontextualization

Retained records can participate in relations that were unavailable when those records were created.

For example:

```text
retained record A
+
retained record B
+
new distinction D
->
new represented relation R
```

The new relation does not rewrite the historical records.

It adds a later relational context.

A contribution can therefore recontextualize earlier material while preserving the genealogy of both the earlier representation and the later relation.

Where practical, record:

- the prior records;
- their earlier represented relations;
- the new distinction;
- the newly represented relation;
- the generator or operation that exposed it;
- any resulting hypothesis, test, measurement, comparison, or candidate;
- the support claims concerning the new relation;
- unresolved alternatives.

Newly generated relation does not mean established relation.

Recontextualization creates material for inquiry.

It does not certify its own accuracy.

## Boundary Testing

A contribution can challenge a boundary.

A boundary can restrict:

- observation;
- representation;
- distinction;
- measurement;
- hypothesis generation;
- candidate generation;
- test generation;
- comparison;
- evaluation;
- selection;
- revision;
- action;
- reopening.

Pressure against a boundary does not establish that the boundary is false, harmful, or unnecessary.

Resistance by the boundary does not establish that it is true, beneficial, or necessary.

Where a test crosses or pressures a boundary, record:

- the boundary;
- the test;
- the generator where relevant;
- relevant distinctions;
- relevant observations or measurements;
- bases;
- support claims;
- conditions;
- what changed;
- what did not change;
- newly available or unavailable candidates;
- unresolved interpretations.

Claims about the function of the boundary remain claims requiring represented support.

A boundary can also prevent generation of the distinction or test required to expose it.

Failure to cross a boundary therefore does not by itself establish that the boundary is justified.

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

Resource allocation and attention allocation are also evaluative operations.

A decision to investigate one unresolved branch rather than another can therefore preserve the relevant criteria, values, and resource conditions without converting that decision into a claim about truth.

## Implementation contributions

Code changes should preserve the semantic distinctions claimed by the framework or explicitly document where the implementation does not yet represent them.

Particular attention should be given to:

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

Implementation changes involving generation should test whether candidate generation remains distinguishable from candidate evaluation.

Implementation changes involving genealogy should test whether later recontextualization can add relations without erasing earlier states.

Implementation changes involving unresolved branches should test whether inquiry basis can remain represented without becoming epistemic support.

Implementation changes involving comparison should test whether absence of a represented ranking basis remains distinguishable from intrinsic incommensurability.

Tests should attack these distinctions rather than merely confirm expected outputs.

A passing implementation test does not establish the conceptual framework as true.

A failing test does not by itself establish the conceptual framework as false.

The relation between specification, implementation, test, and result remains represented.

## Recursive application

These contribution rules are themselves subject to contribution.

A contributor can challenge:

- the required fields;
- the definition of contribution;
- the distinction between basis and support;
- the distinction between acceptance basis and support;
- the distinction between inquiry basis and support;
- the distinction between support and measurement;
- the distinction between distinction and measurement;
- the distinction between generation and evaluation;
- the comparison architecture;
- the treatment of alternatives;
- the branch-preservation protocol;
- the recontextualization model;
- the semantic invariants;
- the implementation requirements;
- the contribution process itself.

The contribution protocol must not become a protected layer that Aperta Veritas refuses to examine.

Its own rules can impose generative boundaries by determining which contributions are easy or difficult to express.

Those boundaries also remain available for examination.

## Minimal principle

A contribution does not need to agree with Aperta Veritas.

It needs enough represented structure for its relation to the current framework to be examined without silently converting disagreement, acceptance, inquiry basis, measurement, confidence, consensus, value, reward, or selection into truth or support, and without assuming that the currently represented candidate space exhausts what can be discovered.
