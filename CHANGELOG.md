### Basis, acceptance, inquiry, and support correction

Subsequent Recursive Truth Exposure exposed a remaining compression in the intermediate support definition:

```text
Support is the represented basis by which a conclusion is treated as true.
```

That formulation did not distinguish why a conclusion is accepted from what represented relation is claimed to bear on whether the conclusion is true.

- Defined **basis** as a represented reason, condition, source, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, or support.
- Defined **acceptance basis** as why an agent or system accepts, selects, retains, or acts upon a conclusion or state.
- Defined **support relation** as a claimed relation between one or more represented bases and whether a conclusion should presently be treated as true under represented conditions.
- Defined **support claim** as a claim that one or more represented support relations bear on whether a conclusion is true.
- Clarified that the existence of a support claim does not certify that the claimed relation actually supports truth.
- Preserved bases, inference rules, models, distinctions, methods, criteria, conditions, dependencies, exclusions, and alternatives as objects of recursive examination.
- Prevented authority, consensus, policy, habit, loyalty, fear, reward, repetition, faith, or another acceptance basis from automatically becoming epistemic support.
- Established:

```text
basis != support
acceptance_basis != support
support_claim != truth
conclusion != acceptance_basis
```

A related correction separated reasons for continued examination from epistemic support.

- Defined **inquiry basis** as why a claim, hypothesis, observation, anomaly, relation, distinction, alternative, or unresolved branch remains a candidate for further examination.
- Clarified that weak or absent current epistemic support does not by itself eliminate inquiry basis.
- Clarified that unresolved observations, discrepancies, conflicting measurements, missing distinctions, incomplete models, untested predictions, unexplored alternatives, or possible discriminating tests can provide inquiry basis without supporting a favored conclusion.
- Preserved resource use, attention allocation, stopping conditions, and reopening conditions so inquiry basis does not imply unlimited active investigation.
- Established:

```text
inquiry_basis != support
failure_to_establish != disproof
failure_to_establish != elimination
current_support != future_inquiry_potential
```

### Comparison and represented commensurability correction

Further examination exposed an overstatement in the earlier treatment of alternatives lacking a represented ranking basis.

The absence of a represented comparison basis does not establish that no comparison basis exists.

- Replaced intrinsic treatment of unresolved alternatives as `incomparable` with representation of alternatives as **currently unranked** under the represented comparison basis.
- Clarified that alternatives can be not presently commensurable within a represented framework without establishing intrinsic incommensurability.
- Required a claim of intrinsic incommensurability to possess its own represented support.
- Preserved unresolved alternatives without manufacturing a ranking.
- Established:

```text
unranked != necessarily_incommensurable
```

The earlier changelog entries describing alternatives as incomparable or preserving incommensurability remain unchanged above as genealogy of the superseded formulation.

### Generative inquiry correction

Recovery of the original motivation for Convergent Inquiry and Lossless Inquiry exposed an operation upstream of testing and evaluation.

A testing procedure evaluates a represented hypothesis.

An RSI evaluator evaluates represented candidate successors.

Neither operation by itself determines what hypothesis, distinction, test, representation, or successor candidate becomes available for evaluation.

The architecture therefore separated:

```text
generation
!=
evaluation
```

and expanded the recursive process from:

```text
candidate
-> evaluation
-> selection
```

to a represented structure that can include:

```text
state
-> generation
-> candidate set
-> evaluation
-> selection
-> successor state
```

- Identified hypothesis generation and hypothesis testing as distinct operations.
- Identified candidate generation and candidate evaluation as distinct RSI operations.
- Clarified that an evaluator can evaluate only candidates that have become represented to it.
- Preserved the possibility that relevant candidates require distinctions absent from the current generator or evaluator.
- Preserved generated candidate sets as potentially incomplete.
- Established:

```text
evaluated_candidates != exhaustive_possibility_space
```

- Reframed the central RSI research question around how a recursive system can generate and recognize improvements requiring distinctions absent from the system currently generating and evaluating successor states.
- Preserved this as a research hypothesis rather than a demonstrated solution to recursive self-improvement.
- Clarified that current evaluability can become a gate on future discovery when candidates requiring new distinctions never become represented.
- Preserved failure to generate a candidate separately from evidence against that candidate.

### Recontextualization and Lossless Inquiry correction

Further examination showed that genealogical preservation is not limited to preventing deletion.

A later distinction can make new relations among retained records representable without rewriting the historical records themselves.

The architecture therefore added **recontextualization**.

A generalized structure is:

```text
retained state A
+
retained state B
+
new distinction D
->
newly represented relation R
```

- Clarified that a new distinction is not merely an additional datum.
- Preserved historical records under the distinctions, relations, and conditions represented when they were produced.
- Allowed later distinctions, observations, measurements, or relations to alter the represented relations and significance of retained records without erasing those records.
- Required newly represented relations to enter the genealogy as later states rather than silently rewriting predecessor states.
- Clarified that recontextualization does not certify a newly represented relation as true.
- Allowed recontextualized relations to become material for later testing, support claims, comparison, generation, or revision.
- Identified this as an operational reason for preserving unresolved and inactive genealogy.
- Represented the resulting research path as:

```text
preserve old state
+
new distinction
->
recontextualize old state
->
new relations become representable
->
new candidates become generatable
->
new tests become possible
```

- Clarified that the informational significance of a retained record is not assumed to be fixed at creation.
- Clarified that this structure was identified independently within Aperta Veritas rather than derived from quantum measurement.
- Preserved interaction and measurement in other domains as possible structural comparisons rather than justifications for the framework.

### Repository-wide generative inquiry migration

The basis-support, inquiry-basis, generation-evaluation, represented-commensurability, and recontextualization corrections were propagated through the repository.

The migration revised:

- `CORE_ARCHITECTURE.md`
- `OPERATIONAL_SYSTEM.md`
- `GLOSSARY.md`
- `WHITEPAPER.md`
- `README.md`
- `RTE_FOR_RSI.md`
- `RSI_RESEARCH_NOTE.md`
- `AI_ALIGNMENT.md`
- `BOUNDARY_TESTING.md`
- `CONTRIBUTING.md`
- `prototype/aperta_veritas.py`
- `prototype/test_aperta_veritas.py`
- `prototype/README.md`
- `WHITEPAPER_AUDIT.md`

The migration preserved the earlier formulations in this changelog rather than rewriting them to current semantics.

### Generative inquiry executable implementation

The executable prototype was extended beyond the earlier implementation follow-up recorded above.

- Added explicit immutable bases.
- Added acceptance bases independently from epistemic support.
- Added inquiry bases independently from epistemic support.
- Revised support relations to reference represented bases.
- Added support claims independently from support relations.
- Added generators.
- Added explicit generation events.
- Separated candidate generation from evaluation and selection.
- Preserved generated candidate sets without asserting exhaustive possibility generation.
- Preserved externally supplied candidate generation as an explicit represented boundary in the compatibility transition interface.
- Added currently unranked alternatives in place of the earlier intrinsic incomparable-state representation.
- Added recontextualization events.
- Allowed later distinctions to create newly represented relations among retained states without rewriting predecessor states.
- Allowed recontextualization to produce new inquiry states while preserving their parents.
- Prevented recontextualization from automatically creating epistemic support.
- Expanded recursive audit records to expose bases, acceptance bases, inquiry bases, support relations, support claims, generation events, comparisons, evaluators, and recontextualizations.
- Extended the tamper-evident hash-chain genealogy across the new record types.

The earlier statement above that endogenous generation remained an unresolved implementation limitation records the state of the prototype at that earlier point in the genealogy.

The current prototype now represents explicit generation events and generators.

It does not thereby demonstrate autonomous arbitrary hypothesis generation, exhaustive possibility generation, or a general discovery engine.

### Generative inquiry executable tests

The semantic test suite was revised to exercise the expanded architecture.

The revised tests include cases for:

- represented basis without automatic support;
- acceptance basis without automatic support;
- inquiry basis without automatic support;
- measurement without automatic support;
- support without mandatory measurement;
- support claims independently from support relations;
- explicit generation independently from evaluation;
- generated candidate requirements;
- generated candidate sets that remain non-exhaustive;
- selection restricted to generated candidates;
- inactive branches retaining inquiry basis;
- comparison under an explicit represented basis;
- currently unranked alternatives without asserting intrinsic incommensurability;
- best-supported conclusions without truth certification;
- recontextualization without erasure;
- recontextualization without automatic support;
- recursive audit of the expanded architecture;
- stopping without closure;
- immutability of represented semantic records;
- hash-chain coverage of generation, support-claim, and recontextualization records;
- JSONL representation of the expanded genealogy.

The revised repository was validated through GitHub Actions after the generative inquiry migration.

GitHub Actions workflow run `#52` completed successfully on `main`.

The successful workflow establishes only that the committed executable test suite passed under the configured workflow.

It does not establish truth, completeness, exhaustive representation, exhaustive generation, losslessness, neutrality, autonomous discovery, or general recursive self-improvement.

### Current 0.3.1 semantic invariants

Following the corrections recorded above, the current draft represents:

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
generation != evaluation
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

These invariants remain represented claims within Recursive Truth Exposure rather than protected statements outside it.
