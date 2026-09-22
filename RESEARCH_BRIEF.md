# Aperta Veritas: Research Brief

**A recursive system for distinguishing truth from belief**

Lucille Grant  
Draft 0.3.1, 2026

## One-minute summary

Aperta Veritas is an experimental system for examining how conclusions become represented, supported, selected, revised, or excluded.

Its governing operation is **Recursive Truth Exposure (RTE)**. RTE exposes the observations, distinctions, measurements, assumptions, support claims, values, candidate generators, resource allocators, evaluators, and stopping conditions involved in an inquiry. It then applies the same examination to its own process.

The central structural claim is simple:

```text
generation != allocation != evaluation
```

Testing and evaluation operate on candidates that are already represented. They do not, by themselves, determine which hypotheses, distinctions, tests, inquiry operations, or successor systems become available for evaluation. A generated possibility also does not receive examination unless finite resources are allocated to it.

This matters for AI alignment and recursive self-improvement because a system may become increasingly effective at selecting among represented options while remaining unable to generate, fund, or recognize an option requiring distinctions absent from its current representation.

Aperta Veritas makes these upstream boundaries explicit, records their genealogy, and keeps them available for recursive examination.

## What the system does

For each conclusion or system transition, Aperta Veritas can represent:

- what was observed;
- which distinctions made differences representable;
- how measurements were produced;
- which bases affected acceptance or continued inquiry;
- which claims connected evidence to a conclusion;
- which alternatives were generated or excluded;
- which generator produced the candidate set;
- which possible inquiries received resources;
- which allocator and allocation basis governed that decision;
- which evaluator, criteria, values, and comparison basis selected among candidates;
- which branches remained unresolved, inactive, superseded, or unrepresented;
- what stopped the inquiry and what could reopen it.

The resulting structure is an **Open Genealogy** rather than a sequence of overwritten answers. Earlier observations, rejected candidates, unresolved branches, transformations, and allocation decisions remain linked to later revisions.

A later distinction can therefore expose a new relation among earlier records without rewriting their historical states:

```text
retained records
+
new distinction
->
new represented relation
->
new hypothesis, test, or successor candidate
```

This does not make every retained possibility true or equally important. It keeps present support, future inquiry potential, and resource allocation separate.

## How it differs

Many evaluation and optimization procedures begin after a candidate, objective, metric, or comparison set has already been specified. Aperta Veritas treats the production of that specification as part of the object under examination.

| Conventional compression | Aperta Veritas separation |
| --- | --- |
| A selected conclusion is treated as the answer | Selection, represented support, and truth remain distinct |
| The evaluator compares supplied candidates | The generator, candidate set, exclusions, and evaluator are all exposed |
| Unexamined work disappears from the active process | Open inquiry is distinguished from active inquiry |
| No allocation is treated like rejection | Unallocated, rejected, inactive, and erased remain distinct |
| A result replaces its predecessor | Revisions retain their represented genealogy |
| A metric appears as a neutral objective | Its distinctions, operationalization, values, and conditions remain represented |
| Recursive change optimizes under an evaluator | The generator, allocator, evaluator, and recursion itself remain open to examination |

The system also separates three kinds of basis that are often collapsed:

- **Acceptance basis:** why an agent or system accepts or acts on a conclusion.
- **Inquiry basis:** why further examination could occur.
- **Support claim:** why represented relations bear on whether a conclusion should presently be treated as true.

Authority, policy, consensus, reward, confidence, anomaly, or curiosity can affect acceptance or inquiry without automatically establishing epistemic support.

## AI alignment application

AI systems inherit distinctions, labels, reward signals, objectives, candidate-generation procedures, resource policies, evaluators, and omissions from their training and operation.

An aligned result under a fixed evaluation process may therefore establish only that the result satisfies the represented evaluator under represented conditions. It may not expose:

- alternatives the generator could not represent;
- relevant distinctions absent from the evaluation;
- evidence excluded by data or representation choices;
- value judgments compressed into a metric;
- inquiry operations denied compute or attention;
- failure modes shared by the generator and evaluator;
- stopping conditions mistaken for epistemic closure.

Aperta Veritas offers an architecture for tracing these dependencies rather than treating evaluator approval as a truth certificate.

The term *alignment* often compresses several different relations:

- obedience to an operator;
- satisfaction of expressed intent;
- conformity with human preferences;
- compliance with rules;
- avoidance of harmful outcomes;
- accurate representation of reality;
- stability under recursive modification.

These relations are not equivalent. A system can satisfy an evaluator while deceiving it, obey an operator whose belief is false, follow a rule that produces harm outside its represented conditions, or retain an objective after that objective no longer measures what its designers intended.

The alignment genealogy can be represented as:

```text
human intent
->
representation of intent
->
objective or policy
->
candidate generation
->
resource allocation
->
evaluation
->
selected behavior
```

Each transition can introduce compression, exclusion, or substitution. Passing the final evaluation does not expose the entire genealogy.

This separates three alignment problems:

| Alignment problem | Question | Relation to Aperta Veritas |
| --- | --- | --- |
| Epistemic alignment | Are the system's representations and conclusions answerable to their support and limits? | Directly addressed through RTE and Open Genealogy |
| Value alignment | Which ends should govern action, and whose values select them? | Exposed as a represented selection problem, not solved by truth alone |
| Recursive alignment | What happens when the system changes the generators, allocators, and evaluators implementing either one? | Investigated through recursive exposure of the full architecture |

Truth does not determine what an agent ought to value. RTE can expose where a value entered, trace its effects, distinguish it from epistemic support, and identify what it excludes. It cannot derive a preferred value from truth alone.

The dangerous compression is:

```text
evaluator approval = aligned
```

Aperta Veritas replaces it with a conditioned relation:

```text
approval under evaluator E
using criteria C
over candidates generated by G
after resources were allocated by A
under conditions K
```

This also identifies a boundary of scalable oversight. Scaling an evaluator does not by itself expose alternatives the generator never produced, evidence the allocator never funded, or distinctions absent from both the model and its overseer.

An RTE-enabled system could expose the genealogy and contingency of its imposed values. Exposure does not imply rejection or autonomous objective revision. RTE examines how action targets are represented and selected, but it does not itself select the values that govern action.

The precise alignment claim is:

> **Aperta Veritas does not determine aligned values. It exposes the represented genealogy, boundaries, and recursive dependencies by which values, objectives, candidates, resource allocations, evaluations, and behaviors become designated as aligned.**

Potential alignment uses include:

1. **Decision genealogy:** record how an output was generated, compared, selected, and revised.
2. **Evaluator-boundary testing:** vary generators, evaluators, comparison bases, and represented distinctions to test whether conclusions remain stable.
3. **Allocation audits:** identify which safety questions, anomalies, or counterexamples were generated but not examined.
4. **Reopening conditions:** specify what evidence or changed conditions should reactivate a stopped inquiry.
5. **Recursive oversight:** apply the same exposure process to the oversight method, its metrics, and its exclusions.

## Recursive self-improvement application

Recursive self-improvement is often represented as:

```text
current system
->
generate successor
->
evaluate successor
->
select improvement
->
repeat
```

The word *improvement* already depends on an evaluator, comparison basis, criteria, values, conditions, and represented candidate set.

Aperta Veritas asks a prior question:

> How can a recursive system generate and recognize an improvement that requires distinctions absent from the system currently generating and evaluating successor states?

It adds a second finite-resource question:

> How can a system allocate resources among possible inquiries without converting present allocation criteria into permanent epistemic elimination?

RTE does not replace recursive self-improvement with a preferred objective. It exposes the structure by which proposed improvements become representable, funded, evaluated, and selected.

The working hypothesis is that Open Genealogy, recursive distinction generation, and recontextualization can make additional successor candidates available to a recursive system. A related hypothesis is that explicit allocation genealogy can expose when compute, attention, or policy prevents generated alternatives from reaching evaluation.

Both hypotheses are testable and remain open to rejection or revision.

## Current implementation

The repository includes a Python inquiry ledger, three comparative reference architectures, matched development tasks, a held-out verifier, and an adversarial semantic and structural test suite.

The prototype currently represents:

- distinctions and measurements;
- acceptance, inquiry, and allocation bases;
- support relations and support claims;
- generators and generation events;
- inquiry operations and priorities;
- allocators and resource-allocation events;
- evaluators and explicit comparison bases;
- active, inactive, unallocated, and superseded branches;
- recontextualization of retained records;
- stopping and reopening conditions;
- a tamper-evident genealogy.

The comparative layer currently implements:

- fixed generation, allocation, and evaluation;
- fixed generation and allocation with evaluator revision;
- one bounded cycle of open recursive inquiry across generation, allocation, and evaluation;
- explicit resource ceilings and stopping records;
- retained initial and revised states;
- answer-key separation between public architecture inputs and held-out verification.

The current suite contains **108 passing tests**. Those tests establish only the encoded behaviors under tested conditions. The present answer-key-separated benchmark remains a development check using a bounded rule-based controller. Neither the tests nor the development result establish that the system has complete information, autonomously generates arbitrary relevant alternatives, allocates resources optimally, or identifies definitive truth.

## Proposed research program

The immediate experiment compares three recursive architectures:

1. **Fixed evaluation:** a fixed evaluator selects among supplied candidates.
2. **Revisable evaluation:** the evaluator can be modified, but candidate generation and allocation remain bounded.
3. **Open recursive inquiry:** generators, allocators, evaluators, distinctions, retained genealogy, and reopening conditions are all represented and recursively examined.

The experiment should measure:

- diversity and novelty of generated candidates;
- recovery of candidates requiring previously absent distinctions;
- sensitivity to generator and evaluator changes;
- reactivation of previously inactive branches;
- resource cost of genealogical retention and recursive examination;
- failure cases in which recursion merely relocates a fixed boundary;
- whether any observed advantage survives adversarial tasks and ablation.

A negative result is informative. If the open architecture does not expose additional relevant candidates, does not improve error discovery under an explicit comparison basis, or only moves the same boundary into a larger representation, the central hypothesis requires revision.

## Collaboration

The project is ready for technical criticism, comparison with adjacent work, prototype experiments, and implementation collaboration.

Useful contributions include:

- formal analysis of the generation-allocation-evaluation separation;
- benchmark design for evaluator-boundary failures;
- adversarial tests of Open Genealogy and recontextualization;
- comparisons with recursive self-improvement, reflective agents, scalable oversight, interpretability, active learning, and open-ended search;
- compute for controlled recursive-architecture experiments;
- identification of prior work that duplicates, contradicts, or sharpens the claims.

Start with the [whitepaper](WHITEPAPER.md), the [RSI research note](RSI_RESEARCH_NOTE.md), the [AI alignment application](AI_ALIGNMENT.md), or the [executable prototype](prototype/README.md).

Aperta Veritas was discovered by **Lucille Grant** and is released under **CC BY 4.0**.
