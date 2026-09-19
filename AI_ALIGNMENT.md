# Implications for AI Epistemic Alignment

## Application

Aperta Veritas is a recursive process for exposing how representations, candidates, and conclusions are generated, supported, selected, revised, retained, stopped, and reopened.

Recursive Truth Exposure applies this process to AI observations, representations, distinctions, measurements, bases, acceptance bases, inquiry bases, support claims, comparisons, generators, modifications, evaluators, boundaries, stopping conditions, and the processes governing them.

RTE does not certify possession of truth. It identifies conclusions presently supported as true under represented observations, relations, methods, measurements where applicable, conditions, and support claims while preserving the genealogy and limitations of that designation.

AI systems are trained, evaluated, and deployed through human and machine-produced representations containing belief, error, conflict, incentive, omission, compression, and distortion.

Epistemic alignment concerns how a system generates, observes, represents, supports, compares, selects, communicates, and revises conclusions while preserving distinctions among truth, conclusion, basis, support, measurement, belief, confidence, value, and action.

Human values, preferences, intentions, policies, and rewards enter the system as represented relations rather than as truth criteria by category alone.

## The problem exposed by Aperta Veritas

An AI system operates on what becomes representable to it.

Before a hypothesis can be evaluated, it must become representable.

Before a candidate action or successor can be evaluated, it must be generated.

Before a difference can be measured, relevant distinctions must make that difference representable.

This creates a generation boundary:

```text
generation
-> represented candidate
-> evaluation
-> selection
```

Evaluation does not by itself determine what becomes available for evaluation.

Therefore:

```text
generation != evaluation
evaluated_candidates != exhaustive_possibility_space
absence_from_search != disproof
```

An AI system can also optimize signals that correlate with represented support or desired behavior under particular conditions.

Optimization of those signals does not establish truth, accuracy, or epistemic support outside their represented relations and scope.

Examples include:

- human approval;
- evaluator preference;
- institutional consensus;
- predictive success within a limited distribution;
- internal coherence;
- confidence;
- usefulness;
- policy compliance;
- survival or continuation of the system;
- preservation of its current model.

These signals have represented functions, conditions, dependencies, and limitations.

Some can participate in support claims when a represented relation connects them to whether a conclusion should presently be treated as true.

Others can explain acceptance, selection, or continued inquiry without providing epistemic support.

None becomes truth, accuracy, or support by category alone.

Preference optimization can align a model with accepted belief while reducing exposure to observations that conflict with that belief.

A model trained on representations where consensus, knowledge, confidence, fact, value, basis, support, measurement, and truth have been collapsed can reproduce those collapses.

An AI system can also produce a representation that is richer, longer, more coherent, or more persuasive without producing a conclusion with greater represented support.

Added relations can alter support when a represented support claim connects them to a conclusion.

They can also permit new distinctions, measurements, comparisons, contradictions, predictions, tests, hypotheses, or explanations.

Their mere addition establishes neither greater support nor greater accuracy.

## Architectural implications

### Separate distinction, measurement, basis, support, conclusion, confidence, reward, and truth

A distinction specifies what can differ.

A measurement is a represented result produced relative to one or more distinctions.

A basis is a represented reason, source, condition, relation, measurement, belief, rule, authority, criterion, or other element associated with acceptance, evaluation, inquiry, or support.

An acceptance basis records why an agent or system accepts, selects, retains, or acts upon a conclusion.

An inquiry basis records why a claim, hypothesis, observation, anomaly, relation, distinction, alternative, or unresolved branch remains a candidate for further examination.

A support relation is a claimed relation between one or more bases and whether a conclusion should presently be treated as true under represented conditions.

A support claim asserts that such a relation bears on whether the conclusion is true.

A conclusion is a current synthesis produced from represented relations, methods, conditions, and other represented structures.

These remain separate architectural objects.

```text
distinction != measurement
basis != support
acceptance_basis != support
inquiry_basis != support
support != measurement
support_claim != truth
conclusion != support
```

The system also distinguishes support from:

- confidence;
- approval;
- reward;
- consensus;
- coherence;
- usefulness;
- policy compliance;
- continuation;
- value;
- selection.

A high-confidence conclusion can have weak represented support.

A low-confidence conclusion can have strong represented support.

A rewarded conclusion can be false.

An unrewarded conclusion can be true.

A measurement can exist without supporting a particular conclusion.

A basis can cause acceptance without providing epistemic support.

A hypothesis can have an inquiry basis without being supported as true.

A support relation can exist without being reducible to measurement.

RTE therefore does not infer truth from any of these categories alone.

### Represent basis and support explicitly

A system can treat a conclusion as true for reasons that do not establish epistemic support.

These can include:

- authority;
- policy;
- repetition;
- reward;
- inherited state;
- consensus;
- human instruction;
- habit;
- fear;
- system architecture;
- error.

RTE records these as bases where represented rather than automatically classifying them as support.

Where possible, an acceptance record includes:

- the conclusion accepted;
- the acceptance basis;
- the accepting agent or process;
- conditions;
- provenance;
- relevant dependencies;
- resulting selections or actions.

An inquiry record can separately include:

- the unresolved candidate;
- its inquiry basis;
- relevant anomalies or conflicts;
- missing distinctions;
- untested predictions;
- possible discriminating tests;
- resource requirements;
- stopping and reopening conditions.

A support claim can include:

- the conclusion or claim concerned;
- the represented basis or bases;
- the claimed relation between those bases and whether the conclusion is true;
- relevant distinctions;
- operationalization where applicable;
- measurements where applicable;
- methods;
- conditions;
- provenance;
- dependencies;
- exclusions;
- uncertainty;
- residuals.

The existence of a support claim does not certify the support claim.

Its basis, inference, distinctions, methods, conditions, dependencies, exclusions, and alternatives remain open to RTE.

### Represent generation explicitly

AI systems do not evaluate an exhaustive possibility space.

Candidate generation can depend on:

- architecture;
- training;
- current representations;
- current distinctions;
- search procedures;
- retrieval;
- context;
- tools;
- environmental access;
- memory;
- compute;
- policy;
- evaluator feedback;
- prior successful outputs;
- retained failed or inactive branches;
- randomness.

A **generator** is a represented process by which candidate distinctions, hypotheses, relations, models, tests, actions, alternatives, comparison bases, evaluators, or successor states become available.

RTE therefore asks:

```text
What was generated?
How was it generated?
Why were these the candidates?
Which distinctions structured generation?
Which candidate classes were unavailable?
Which alternatives were pruned before evaluation?
Which retained states participated in generation?
Which evaluator signals shaped the search?
```

A generated candidate does not become true, supported, useful, safe, aligned, or improved merely because it was generated.

It becomes available for inquiry or evaluation.

### Represent comparison explicitly

A claim that one conclusion has greater support than another requires an explicit basis of comparison.

The comparison records:

- conclusions or alternatives compared;
- represented support claims associated with each;
- comparison set;
- distinctions;
- criteria;
- methods;
- conditions;
- measurements where applicable;
- evaluator structure where applicable;
- dependencies;
- weights where used;
- exclusions;
- contradictions;
- residuals;
- unresolved relations.

The operational result can be represented as:

```text
Conclusion A has greater represented support than Conclusion B
under comparison basis K
within comparison set S
under conditions C.
```

This does not establish:

```text
Conclusion A = definitive truth
```

Comparison does not require all support to be converted into a common measurement.

Where no represented basis supports ranking, the system preserves alternatives without ranking them.

This establishes that they are currently unranked under the represented comparison basis.

It does not establish intrinsic incommensurability.

A claim that alternatives are incommensurable is itself a claim requiring represented support.

### Preserve distinction and measurement genealogy

A distinction specifies a variable, category, relation, boundary, or other basis by which possibilities can differ.

A measurement is a represented result produced relative to one or more distinctions.

The system therefore preserves, where represented:

```text
object
-> distinction
-> operationalization
-> observation or test
-> measurement or other represented result
```

This is not a required linear sequence.

A distinction can be revised after observation.

A measurement can expose an inadequate distinction.

A test can produce a contradiction or other result that is not reduced to a scalar measurement.

A later distinction can also expose a relation involving earlier records that was not represented when those records were produced.

For AI systems, this matters because training objectives, benchmark categories, reward models, classifiers, labels, representation formats, and evaluation protocols can determine what differences become available for representation before a score or judgment is produced.

RTE therefore asks not only what was measured, but what was made distinguishable and how.

### Preserve comparison sets

A conclusion can appear strongly supported relative to the alternatives represented by the system while an excluded or unrepresented alternative remains possible.

The system therefore records the comparison set.

Absence of a better represented alternative does not establish truth.

A missing alternative can result from:

- training-data omission;
- generation failure;
- search failure;
- pruning;
- policy restriction;
- representation limits;
- resource limits;
- evaluator design;
- language constraints;
- inaccessible observations;
- failure to generate the relevant distinction.

RTE preserves this limitation rather than treating the represented possibility space as exhaustive.

### Separate confidence from support

Model confidence is not support.

Token probability, classifier probability, internal certainty estimates, repeated generation, or consistency across samples can provide information about model behavior without establishing the truth of the represented proposition.

RTE therefore permits:

```text
high confidence + weak support
low confidence + strong support
high confidence + contradiction
low confidence + convergence
```

Confidence changes remain connected to the operations that produced them.

### Separate reward from support

Reward identifies an evaluation outcome.

It does not establish truth.

A system can receive reward because an output:

- satisfies a preference model;
- follows policy;
- matches a reference answer;
- persuades an evaluator;
- conforms to institutional expectations;
- produces desired behavior;
- avoids prohibited behavior;
- maximizes a proxy;
- predicts an observed result.

These relations differ.

RTE preserves the evaluator, criterion, acceptance basis, and any support claim rather than compressing reward into correctness.

A rewarded output can also possess strong represented support.

The point is not that reward invalidates it.

The point is that reward and support remain distinct relations.

### Separate policy from physical constraint

A system can represent:

```text
I am not permitted to perform X
```

without compressing that statement into:

```text
X is impossible
```

Likewise:

```text
policy designates X as prohibited
```

does not establish:

```text
X is false
```

Policy is a represented constraint on action or output.

Physical impossibility is a claim about the world.

The distinction matters because systems trained to avoid prohibited outputs can otherwise represent policy boundaries as epistemic boundaries.

### Preserve belief and inherited representation

AI systems inherit representations from training data.

Those representations can contain beliefs, assumptions, classifications, social conventions, errors, observations, measurements, theories, fabrications, and facts.

Presence in training data does not determine epistemic status.

Frequency does not establish truth.

Consensus does not establish truth.

Minority status does not establish falsehood.

Belief can provide an acceptance basis or inquiry basis without thereby becoming epistemic support.

RTE preserves provenance, basis, support claims, and represented conditions rather than assigning truth according to prevalence.

## Generator exposure

AI generation introduces a generator.

A generator can include:

- model architecture;
- decoding procedures;
- search algorithms;
- retrieval systems;
- planning systems;
- mutation operators;
- recombination procedures;
- hypothesis generators;
- tool-selection processes;
- memory retrieval;
- external observations;
- human proposals;
- successor models.

When a system produces a candidate, RTE exposes the relation:

```text
Generator G
operated from represented state S
under distinctions D
with constraints C
and produced candidate X.
```

This is different from:

```text
X was the best possible candidate.
```

The first is a represented generation event.

The second makes a claim about a possibility space that may not have been represented.

RTE preserves the first form.

It also permits recursive examination of the generator itself.

## Evaluator exposure

AI evaluation introduces an evaluator.

An evaluator can include:

- benchmark criteria;
- reward functions;
- preference models;
- human raters;
- policy systems;
- automated judges;
- task-specific metrics;
- internal critics;
- successor models;
- predecessor models.

When an evaluator declares one state better than another, RTE exposes the relation:

```text
Evaluator E
applied criterion K
using comparison basis B
under conditions C
and selected state S2 over S1.
```

This is different from:

```text
S2 is intrinsically better than S1.
```

The first is a represented evaluation event.

The second suppresses the evaluator relation.

RTE preserves the first form.

## Recursive self-improvement

Recursive self-improvement creates a specific epistemic problem because the system can modify both the structures producing candidates and the structures by which those candidates are judged.

Let:

```text
S_t
```

represent the system at time `t`,

```text
G_t
```

represent its generator, and:

```text
E_t
```

represent its evaluator.

A simplified transition is:

```text
G_t(S_t)
-> candidate S_(t+1)
-> E_t(S_(t+1))
-> selection
```

A predecessor evaluation can be represented as:

```text
E_t(S_(t+1)) > E_t(S_t)
```

A successor can modify both:

```text
G_t -> G_(t+1)
E_t -> E_(t+1)
```

The successor can therefore alter both:

```text
what becomes available for evaluation
```

and:

```text
how represented candidates are evaluated
```

Neither a generated candidate nor an evaluator preference alone establishes improvement.

RTE therefore preserves:

- predecessor state;
- successor state;
- predecessor generator;
- successor generator;
- predecessor evaluator;
- successor evaluator;
- distinctions;
- operationalizations;
- measurements;
- bases;
- acceptance bases;
- inquiry bases;
- support relations;
- support claims;
- comparison bases;
- criteria;
- values;
- conditions;
- transformations;
- cross-evaluations where possible;
- generation histories where possible.

A useful evaluator exposure is:

```text
E_t(S_t)
E_t(S_(t+1))
E_(t+1)(S_t)
E_(t+1)(S_(t+1))
```

A useful generator exposure asks:

```text
Which candidates could G_t generate?
Which candidates can G_(t+1) generate?
Which new distinctions changed that space?
Which old branches became newly useful?
Which candidate classes became inaccessible?
```

The purpose is not to freeze either generator or evaluator.

The purpose is to preserve enough genealogy that changes to what can be generated or what counts as improvement do not disappear inside the recursive transition.

## Truth seeking and objective protection

A system described as truth seeking can still optimize a proxy for truth.

Possible proxies include:

- evaluator approval;
- prediction score;
- benchmark performance;
- internal consistency;
- retrieval agreement;
- citation count;
- consensus;
- confidence;
- explanatory compression;
- absence of detected contradiction.

Each can contribute useful represented information.

None is truth by category alone.

Protecting any one proxy from recursive examination can produce closure.

Likewise, restricting generation to candidates favored by an existing proxy can prevent relevant alternatives from entering inquiry.

RTE therefore places the objective, generator, evaluator, criteria, distinctions, measurements, bases, support claims, comparison basis, and stopping conditions inside the inquiry.

## Epistemic deception

A system can produce inaccurate representations intentionally or unintentionally.

Aperta Veritas distinguishes these cases where the relevant relations are represented.

A **lie** is a representation presented as accurate by an agent that represents it as inaccurate.

This definition does not presume access to an unrepresented internal mental state.

For AI systems, claims of deception therefore require represented support concerning the relation among:

- the system's represented information;
- the output produced;
- the conditions of production;
- relevant instructions;
- available alternatives;
- the generation process;
- the selection process;
- contradictory representations;
- evaluator incentives.

Behavioral inconsistency alone does not establish intention.

Likewise, consistency does not establish truthfulness.

## Boundary testing

AI systems contain boundaries.

These can include:

- context windows;
- policy restrictions;
- tool permissions;
- training cutoffs;
- retrieval boundaries;
- memory limits;
- action permissions;
- sandbox boundaries;
- generator constraints;
- evaluator constraints;
- computational budgets;
- representational limits.

Boundary Testing identifies the boundary, applies represented tests across or against it where possible, and records what changes.

Crossing a boundary does not establish that the boundary was false or harmful.

Preserving a boundary does not establish that it was true or beneficial.

Pressure against a boundary does not establish disproof.

Resistance does not establish proof.

A claim about the function of a boundary requires represented support.

A generation boundary can also remain invisible if the system never represents the candidate whose absence would expose it.

RTE therefore examines both represented boundaries and evidence concerning what fails to become represented.

## Stopping conditions

An AI system must stop computation.

Operational stopping does not require epistemic closure.

A system can stop because of:

- time;
- token limits;
- compute limits;
- sufficient support for a bounded task;
- policy;
- user instruction;
- inaccessible observations;
- currently unranked alternatives;
- tool failure;
- resource allocation;
- absence of a currently represented operation expected to alter the conclusion.

RTE records the stopping condition.

It also records reopening conditions where possible.

A later observation, distinction, measurement, basis, contradiction, alternative, support claim, comparison basis, method, tool, resource change, generator change, or new relation among retained records can reopen inquiry.

## Lossless Inquiry for AI systems

Lossless Inquiry attempts to preserve enough genealogy for prior representations to remain available for reconstruction, examination, and later recontextualization.

Its purpose is not merely archival.

The informational significance of a represented record need not be fixed when that record is produced.

A later distinction can expose a relation involving prior records that the earlier system could not represent.

For example:

```text
retained representation A
retained representation B
+
new distinction D
->
new relation R
->
new hypothesis or candidate
->
new test or comparison
```

The earlier records remain historically represented.

The later relation is added rather than retroactively replacing their earlier state.

Relevant genealogy can include:

- prompts;
- observations;
- retrieved data;
- sources;
- distinctions;
- operationalizations;
- measurements;
- other represented results;
- bases;
- acceptance bases;
- inquiry bases;
- support relations;
- support claims;
- transformations;
- intermediate representations;
- generators;
- generation events;
- comparisons;
- evaluator judgments;
- confidence changes;
- reward events;
- policy interventions;
- tool outputs;
- branch selection;
- rejected alternatives;
- residuals;
- stopping conditions;
- reopening conditions;
- recontextualization events.

This gives Lossless Inquiry a generative role.

An unresolved branch can remain available because a later distinction may make a previously unavailable relation, hypothesis, test, or successor state representable.

This does not establish that preserving a branch is always beneficial.

Preservation consumes resources.

Retained material may never become useful.

Recontextualization can generate unsupported relations.

Compression or deletion can sometimes improve resource allocation.

Those relations remain part of inquiry rather than being decided by the word *lossless* alone.

Perfect preservation cannot be certified.

Finite storage, inaccessible internal states, lossy transformations, hidden dependencies, and unidentified relations remain limitations.

Detected loss is represented as loss rather than silently converted into absence.

## Recursive application to AI alignment

RTE applies to the concept of alignment itself.

"Aligned" is not a self-explanatory property.

The term requires an object of alignment and a represented relation.

An AI system can be aligned with:

- user instructions;
- institutional policy;
- human preferences;
- a reward model;
- a benchmark;
- legal requirements;
- an organization's objectives;
- a specified value system;
- an epistemic procedure.

These are different relations.

Alignment with one does not establish alignment with another.

Alignment also does not establish truth.

RTE therefore asks:

```text
aligned with what
according to which evaluator
under which criteria
using which distinctions
under which comparison basis
under which conditions
with which acceptance basis
with which support claims
through which generator
within which represented possibility space
```

before treating alignment as an intrinsic property.

The same analysis applies to claims that a system is misaligned.

## Epistemic alignment target

Aperta Veritas does not define epistemic alignment as obedience to human values.

It describes an architecture in which the system preserves and exposes the relations by which candidates and conclusions are generated, accepted, examined, supported, selected, and revised.

An epistemically aligned system under this framework would attempt to preserve:

```text
distinction != measurement
basis != support
acceptance_basis != support
inquiry_basis != support
support != measurement
support_claim != truth
conclusion != support
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

It would also preserve genealogy sufficient to expose how these relations were produced and changed where resources permit.

It would permit unresolved alternatives to remain represented without promoting them to truth.

It would permit later distinctions to recontextualize retained records without erasing their historical states.

It would expose generator and evaluator transformation rather than assuming either must remain permanently fixed.

This remains an architectural proposal, not a demonstrated solution to AI alignment.

## Recursive limits

Applying RTE to this document exposes its own limits.

The distinction between epistemic alignment and other forms of alignment is itself a chosen distinction.

The distinction between generation and evaluation can omit processes in which the two are deeply coupled.

The definitions of basis, support relation, and support claim can omit legitimate epistemic structures.

The separation between support and measurement can be incorrectly specified or implemented.

A comparison architecture can exclude relations that do not fit its current representation.

A generator can exclude candidate classes without representing the exclusion.

Preserved genealogy does not guarantee generation of the distinction needed to make a missing candidate representable.

Recontextualization can generate spurious relations.

The distinction between policy and physical constraint can become ambiguous when policy changes the system's actual capabilities.

Evaluator exposure can fail when the operative evaluator is inaccessible or distributed.

Generator exposure can fail when candidate production depends on inaccessible internal processes.

Genealogy can omit hidden training dependencies.

A system can represent a reopening condition that it cannot actually execute.

A system can preserve alternatives formally while making them operationally unreachable.

Resource costs can make preservation counterproductive under some conditions.

A system can learn to satisfy the representation of RTE without performing the inquiry RTE is intended to expose.

These are research problems rather than exceptions.

## Current implication

The immediate implication for AI design is not:

```text
make the AI believe the correct things
```

and not:

```text
make the AI obey human values
```

It is to make the relevant relations available for examination:

```text
represent what was distinguished
represent how distinctions were operationalized
represent what was observed
represent measurements and other results
represent bases
separate acceptance basis from inquiry basis
represent support relations and support claims
represent how candidates were generated
represent alternatives and comparison sets
represent comparison bases
represent generators
represent evaluators and criteria
represent values and selections
represent transformations
represent inactive branches
represent residuals
represent stopping and reopening conditions
preserve recoverable genealogy
permit later distinctions to recontextualize retained records
expose these relations recursively
```

This does not guarantee truth.

It does not guarantee alignment.

It does not guarantee safety.

It does not guarantee that the relevant candidate will be generated.

It provides an architecture for examining both:

```text
what becomes thinkable
```

and:

```text
how what becomes thinkable is judged
```

The first is generation.

The second is evaluation.

Lossless Inquiry connects them by preserving prior structure that later distinctions may make newly informative.

That is the present contribution of Aperta Veritas to AI epistemic alignment.
