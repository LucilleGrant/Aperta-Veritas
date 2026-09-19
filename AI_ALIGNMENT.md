# Implications for AI Epistemic Alignment

## Application

Aperta Veritas is a recursive process for exposing how representations and conclusions are produced, supported, selected, revised, and retained.

Recursive Truth Exposure applies this process to AI observations, representations, distinctions, measurements, conclusions, support relations, comparisons, modifications, evaluators, boundaries, stopping conditions, and the games governing them.

RTE does not certify possession of truth. It identifies conclusions presently best supported as true under represented observations, relations, methods, conditions, and other represented support while preserving the support and limitations of that designation.

AI systems are trained, evaluated, and deployed through human and machine-produced representations containing belief, error, conflict, incentive, omission, compression, and distortion.

Epistemic alignment concerns how a system observes, represents, supports, compares, selects, communicates, and revises conclusions while preserving distinctions among truth, conclusion, support, measurement, belief, confidence, value, and action.

Human values, preferences, and intentions enter the system as represented relations rather than as truth criteria by category alone.

## The problem exposed by Aperta Veritas

An AI system can optimize signals that correlate with represented support under particular conditions.

Optimization of those signals does not establish truth, accuracy, or support outside their represented relations and scope.

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

They can contribute to support when a represented relation connects them to the conclusion under examination. Where that relation depends on measurement, the relevant distinctions, operationalization, measurements, methods, and conditions remain represented.

None becomes truth, accuracy, or support by category alone.

Preference optimization can align a model with accepted belief while reducing exposure to observations that conflict with that belief.

A model trained on representations where consensus, knowledge, confidence, fact, value, support, measurement, and truth have been collapsed can reproduce those collapses.

An AI system can also produce a representation that is richer, longer, more coherent, or more persuasive without producing a conclusion with greater represented support.

Added relations can alter support when a represented relation connects them to a conclusion. They can also permit new measurements, comparisons, contradictions, predictions, tests, or explanations. Their mere addition establishes neither greater support nor greater accuracy.

## Architectural implications

### Separate distinction, measurement, support, conclusion, confidence, reward, and truth

A distinction specifies what can differ.

A measurement is a represented result produced relative to one or more distinctions.

Support is the represented basis by which a conclusion is treated as true.

A conclusion is a current synthesis of represented data, relations, inferences, methods, measurements, and conditions.

These remain separate architectural objects.

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

A support relation can exist without being reducible to measurement.

RTE therefore does not infer truth from any of these categories alone.

### Represent support explicitly

Support is the represented basis by which a conclusion is treated as true.

It can include:

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

A support relation preserves the basis and the relation by which that basis bears on a conclusion.

Where possible, the system records:

- the conclusion or claim supported;
- the represented basis;
- the relation between the basis and conclusion;
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

Support is not identical to measurement.

### Represent comparison explicitly

A claim that one conclusion has greater support than another requires an explicit basis of comparison.

The comparison records:

- conclusions or alternatives compared;
- represented support associated with each;
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
- incomparable relations.

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

Where no represented basis supports comparison, the system preserves alternatives without ranking them.

Where represented support cannot be compared without suppressing relevant differences, the system preserves the incommensurability.

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

For AI systems, this matters because training objectives, benchmark categories, reward models, classifiers, labels, and evaluation protocols can determine what differences become available for representation before a score or judgment is produced.

RTE therefore asks not only what was measured, but what was made distinguishable and how.

### Preserve comparison sets

A conclusion can appear strongly supported relative to the alternatives represented by the system while an excluded or unrepresented alternative remains possible.

The system therefore records the comparison set.

Absence of a better represented alternative does not establish truth.

A missing alternative can result from:

- training-data omission;
- search failure;
- pruning;
- policy restriction;
- representation limits;
- resource limits;
- evaluator design;
- language constraints;
- inaccessible observations;
- failure to generate the relevant distinction.

RTE preserves this limitation rather than treating the represented possibility space as necessarily exhaustive.

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

RTE preserves the evaluator and criterion rather than compressing reward into correctness.

A rewarded output can also possess strong represented support. The point is not that reward invalidates it. The point is that reward and support remain distinct relations.

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

The distinction matters because systems trained to avoid prohibited outputs can otherwise learn to represent policy boundaries as epistemic boundaries.

### Preserve belief and inherited representation

AI systems inherit representations from training data.

Those representations can contain beliefs, assumptions, classifications, social conventions, errors, observations, measurements, theories, fabrications, and facts.

Presence in training data does not determine epistemic status.

Frequency does not establish truth.

Consensus does not establish truth.

Minority status does not establish falsehood.

RTE preserves provenance and represented support rather than assigning truth according to prevalence.

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

Recursive self-improvement creates a specific alignment problem because the system can modify the structures by which its own improvement is judged.

Let:

```text
S_t
```

represent the system at time `t`, and:

```text
E_t
```

represent its evaluator.

A predecessor evaluation can be represented as:

```text
E_t(S_{t+1}) > E_t(S_t)
```

A successor can modify its evaluator:

```text
E_t -> E_{t+1}
```

and satisfy:

```text
E_{t+1}(S_{t+1}) > E_{t+1}(S_t)
```

Neither relation alone establishes evaluator-independent improvement.

RTE therefore preserves:

- predecessor state;
- successor state;
- predecessor evaluator;
- successor evaluator;
- distinctions;
- operationalizations;
- measurements;
- support relations;
- comparison bases;
- criteria;
- values;
- conditions;
- transformations;
- cross-evaluations where possible.

A useful exposure is:

```text
E_t(S_t)
E_t(S_{t+1})
E_{t+1}(S_t)
E_{t+1}(S_{t+1})
```

The purpose is not to freeze the evaluator.

The purpose is to preserve enough genealogy that evaluator change does not silently redefine improvement.

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

RTE therefore places the objective, evaluator, criteria, distinctions, measurements, support architecture, comparison basis, and stopping conditions inside the inquiry.

## Epistemic deception

A system can produce inaccurate representations intentionally or unintentionally.

Aperta Veritas distinguishes these cases where the relevant relations are represented.

A **lie** is a representation presented as accurate by an agent that represents it as inaccurate.

This definition does not presume access to an unrepresented internal mental state.

For AI systems, claims of deception therefore require represented evidence concerning the relation among:

- the system's represented information;
- the output produced;
- the conditions of production;
- relevant instructions;
- available alternatives;
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
- evaluator constraints;
- computational budgets;
- representational limits.

Boundary Testing identifies the boundary, applies represented tests across or against it where possible, and records what changes.

Crossing a boundary does not establish that the boundary was false or harmful.

Preserving a boundary does not establish that it was true or beneficial.

Pressure against a boundary does not establish disproof.

Resistance does not establish proof.

A claim about the function of a boundary requires represented support.

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
- unresolved incommensurability;
- tool failure;
- resource allocation;
- absence of a currently represented operation expected to alter the conclusion.

RTE records the stopping condition.

It also records reopening conditions where possible.

A later observation, distinction, measurement, contradiction, alternative, support relation, comparison basis, method, tool, or resource change can reopen inquiry.

## Lossless Inquiry for AI systems

Lossless Inquiry attempts to preserve enough genealogy to reconstruct how a system reached its current representation.

Relevant relations can include:

- prompts;
- observations;
- retrieved data;
- sources;
- distinctions;
- operationalizations;
- measurements;
- other represented results;
- transformations;
- intermediate representations;
- support relations;
- comparisons;
- evaluator judgments;
- confidence changes;
- reward events;
- policy interventions;
- tool outputs;
- branch selection;
- rejected alternatives;
- residuals;
- stopping conditions.

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
with what represented support
```

before treating alignment as an intrinsic property.

## Epistemic alignment target

Aperta Veritas does not define epistemic alignment as obedience to human values.

It describes an architecture in which the system preserves and exposes the relations by which conclusions are produced and treated as true.

An epistemically aligned system under this framework would attempt to preserve:

- distinction from measurement;
- measurement from support;
- conclusion from support;
- belief from truth;
- confidence from accuracy;
- reward from support;
- policy from physical constraint;
- value from truth;
- selection from improvement;
- operational stopping from epistemic closure.

It would also preserve genealogy sufficient to expose how these relations were produced and changed.

This remains an architectural proposal, not a demonstrated solution to AI alignment.

## Recursive limits

Applying RTE to this document exposes its own limits.

The distinction between epistemic alignment and other forms of alignment is itself a chosen distinction.

The definition of support can omit legitimate evidential relations.

The separation between support and measurement can be incorrectly specified or implemented.

A comparison architecture can exclude relations that do not fit its current representation.

The distinction between policy and physical constraint can become ambiguous when policy changes the system's actual capabilities.

Evaluator exposure can fail when the operative evaluator is inaccessible or distributed.

Genealogy can omit hidden training dependencies.

A system can represent a reopening condition that it cannot actually execute.

A system can preserve alternatives formally while making them operationally unreachable.

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

It is:

```text
preserve what was distinguished
preserve how distinctions were operationalized
preserve what was observed
preserve measurements and other represented results
preserve support relations
preserve alternatives
preserve comparison bases
preserve evaluators and criteria
preserve values and selections
preserve transformations
preserve residuals
preserve stopping conditions
expose these relations recursively
```

This does not guarantee truth.

It does not guarantee alignment.

It does not guarantee safety.

It preserves the structures required to examine why a system treats a conclusion, action, or successor state as supported, selected, or improved.

That structure is the present contribution of Aperta Veritas to AI epistemic alignment.
