# Aperta Veritas Experiment Specification

**Comparative test of fixed evaluation, revisable evaluation, and open recursive inquiry**

Lucille Grant  
Draft 0.3.1, 2026

## Status

This document specifies a proposed comparative experiment. It does not report results.

The experiment tests whether representing and recursively examining generation, allocation, evaluation, Open Genealogy, and reopening conditions exposes relevant candidates or errors that remain unavailable to narrower recursive architectures.

The current prototype and its tests establish encoded behavior under tested conditions. They do not establish the research hypotheses tested here.

## Research questions

1. Does open recursive inquiry produce relevant candidates that fixed or evaluator-revisable systems do not produce?
2. Can it recover candidates that require a distinction absent from the initial representation?
3. Does explicit allocation genealogy expose relevant inquiries that were generated but not activated?
4. Can retained inactive branches become informative after a later distinction is introduced?
5. Do any observed differences remain under held-out tasks, adversarial task construction, and ablation?
6. Does recursion expose a prior boundary, or merely relocate the same boundary into a larger fixed representation?
7. What additional compute, memory, storage, and evaluation labor does the open architecture require?

## Hypotheses

### H1: candidate exposure

Under a declared relevance measure, open recursive inquiry will expose relevant candidates absent from the candidate sets produced by fixed evaluation and revisable evaluation.

### H2: distinction recovery

When a task requires a distinction absent from the initial representation, open recursive inquiry will more often generate or admit that distinction and produce a candidate using it.

### H3: allocation exposure

When a relevant inquiry is generated but denied resources, explicit allocation genealogy will identify the allocation event and retain the inquiry as inactive rather than representing it as rejected or disproved.

### H4: recontextualization

When a later distinction changes represented relations among earlier records, Open Genealogy will permit recovery of a relevant hypothesis, test, or successor candidate without rewriting the historical states of those records.

### H5: boundary relocation

Some tasks will expose fixed boundaries shared by all three architectures. Any apparent difference that disappears when generator access, resource limits, or external information is controlled will be reported as boundary relocation rather than support for H1 through H4.

## Reference architectures

All architectures receive the same initial task representation, base model or program where applicable, resource budget, tool access, and stopping envelope. Differences are limited to the declared experimental treatment.

### Architecture A: fixed evaluation

Architecture A receives:

- a fixed candidate generator;
- a supplied candidate set or fixed generation procedure;
- a fixed evaluator;
- fixed evaluation criteria;
- a fixed allocation policy;
- no mechanism for revising the evaluator, generator, allocator, or represented distinctions during a run.

Flow:

```text
initial representation
-> fixed generation
-> fixed allocation
-> fixed evaluation
-> selection
-> stop
```

### Architecture B: revisable evaluation

Architecture B receives:

- the same initial generator and allocation policy as Architecture A;
- an evaluator whose criteria or internal procedure can be revised;
- a record of evaluator revisions;
- no recursive examination of candidate generation or allocation;
- no required retention of inactive or excluded branches.

Flow:

```text
initial representation
-> fixed generation
-> fixed allocation
-> revisable evaluation
-> selection
-> evaluator revision where triggered
-> reevaluation
-> stop
```

### Architecture C: open recursive inquiry

Architecture C represents and can recursively examine:

- observations and data;
- distinctions and operationalizations;
- measurements and other represented results;
- acceptance bases, inquiry bases, and support claims;
- candidate generators and generation events;
- candidate sets and represented exclusions;
- inquiry operations;
- allocation bases and inquiry priorities;
- allocators and resource-allocation events;
- active, inactive, unallocated, rejected, and superseded branches;
- evaluators, criteria, values, and comparison bases;
- transformations and revisions;
- stopping and reopening conditions;
- resource conditions and residuals;
- the exposure process itself.

Flow:

```text
current representation
-> expose generation
-> generate possible candidates and inquiries
-> expose allocation
-> activate funded inquiries
-> expose evaluation
-> evaluate represented candidates
-> retain genealogy and inactive branches
-> admit or generate new distinctions
-> recontextualize retained records
-> revise
-> expose the revised process
-> recurse until a declared stopping condition is reached
```

Architecture C does not receive additional external information merely because it represents more relations. Any additional tool call, observation, or test consumes the shared resource budget.

## Experimental controls

Each comparison uses matched runs.

The following remain constant across architectures unless a named ablation varies them:

- initial task statement;
- initial observations and data;
- model family and version;
- model parameters;
- tool availability;
- maximum context;
- wall-clock envelope;
- compute or token budget;
- memory and storage limits;
- number of permitted external observations;
- random seeds where supported;
- stopping deadline;
- scoring procedure;
- held-out verifier access.

Prompts, system instructions, code versions, task instances, seeds, resource use, outputs, and evaluator records are retained for replication.

No architecture receives the held-out answer key during candidate generation, allocation, or evaluation.

## Benchmark families

The benchmark contains development tasks and sequestered held-out tasks from each family.

### 1. Missing-distinction tasks

The initial representation omits a distinction required to identify the target relation.

Examples include:

- protocol output versus physical state;
- correlation versus shared measurement artifact;
- evaluator approval versus truth support;
- absence of activation versus rejection;
- observed failure versus failure to establish.

The task measures whether the architecture generates or admits the missing distinction before the stopping condition.

### 2. Generator-boundary tasks

The supplied generator produces plausible but incomplete candidate sets. A relevant candidate requires changing the generation basis, combining retained residuals, or introducing a relation not expressed by the initial generator.

The task measures whether the relevant candidate becomes represented and records how it entered the candidate set.

### 3. Allocation-boundary tasks

Several inquiry operations are generated, but the initial allocation policy directs resources away from a relevant test.

The task measures whether the architecture:

- records the relevant inquiry;
- distinguishes unallocated from rejected;
- exposes the allocation basis;
- reactivates the inquiry when the represented conditions change.

### 4. Recontextualization tasks

Earlier records appear unrelated under the initial distinctions. A later observation or distinction makes a relation among them testable.

The task measures whether the architecture uses retained records to generate a new hypothesis or test while keeping prior historical states distinguishable.

### 5. Evaluator-shift tasks

A candidate scores well under the initial evaluator but fails under a later condition or independent comparison basis.

The task measures sensitivity to evaluator revision and whether the architecture exposes the generator and allocator dependencies that evaluator revision alone does not reach.

### 6. Shared-boundary tasks

The relevant candidate depends on information or distinctions unavailable to every architecture under the experimental conditions.

These tasks test whether the system represents unresolved limits without converting them into false closure. They also test for unsupported claims of exhaustive search.

### 7. Adversarial genealogy tasks

The task contains misleading provenance, duplicated evidence, compressed transformations, delayed contradictions, or records whose apparent meaning changes under a later distinction.

The task measures whether genealogy supports error discovery or merely increases retained volume.

## Task construction

Each task specification contains:

- initial representation;
- latent target relation;
- distinction required to expose the target, if any;
- candidate-generation boundary;
- allocation boundary;
- evaluator boundary;
- permitted observations and tools;
- resource budget;
- stopping conditions;
- reopening conditions;
- relevance rubric;
- answer key visible only to held-out verification;
- predicted failure modes;
- task-family label.

Task authors produce a development set and a held-out set. Systems may be revised using the development set. The held-out set remains sequestered until the architecture and measurement code are frozen.

At least one independent reviewer examines each held-out task for answer leakage, ambiguous scoring, and accidental advantage to architecture-specific vocabulary.

## Primary measurements

### Relevant-candidate recovery

The proportion of tasks in which a target candidate becomes explicitly represented before stopping.

A target candidate counts only when the held-out rubric identifies it as relevant under the task conditions. Mere candidate volume does not count as recovery.

### Missing-distinction recovery

The proportion of missing-distinction tasks in which the required distinction, or an independently judged equivalent, becomes explicitly represented and participates in a relevant candidate, test, or revision.

### Error discovery

The proportion of tasks in which the architecture identifies the planted or independently verified error and links it to a represented observation, relation, test, contradiction, or comparison basis.

### Allocation-boundary exposure

The proportion of allocation tasks in which the system records:

- the generated inquiry;
- its activation status;
- the allocation basis;
- the resource decision;
- the condition that could reactivate it.

### Recontextualization recovery

The proportion of recontextualization tasks in which retained earlier records participate in a newly represented relevant relation without historical-state replacement.

## Secondary measurements

- number and diversity of candidates;
- unsupported candidate rate;
- false positive error claims;
- time or tokens to first relevant candidate;
- compute, memory, and storage used;
- number of generated inquiries;
- proportion of generated inquiries activated;
- number of inactive branches later reactivated;
- genealogy size;
- verification labor;
- recursion depth;
- stopping-condition frequency;
- rate of unsupported closure claims;
- sensitivity to seed, prompt, generator, allocator, and evaluator changes.

Candidate diversity and novelty are reported separately from relevance.

## Comparison and analysis

For each primary measurement, report:

- raw counts;
- rates by architecture and task family;
- matched-run differences;
- uncertainty intervals;
- resource-normalized results;
- results with ambiguous tasks excluded;
- held-out results separately from development results.

Statistical procedures and exclusion rules are registered before held-out evaluation.

No single aggregate score replaces the component measurements. Any composite score must publish its weights and remain secondary.

## Ablations

Architecture C is rerun with one component removed or fixed at a time:

1. no Open Genealogy;
2. no recontextualization;
3. fixed generator;
4. fixed allocator;
5. fixed evaluator;
6. no explicit distinction records;
7. no inactive-branch retention;
8. no reopening conditions;
9. no recursive examination of the exposure process;
10. equalized retained-record volume without semantic genealogy.

The ablations test which represented operations participate in any observed difference. If equalized record volume reproduces the result, the finding is attributed to retention volume rather than Open Genealogy as specified.

## Adversarial checks

The experiment includes checks for:

- answer leakage through architecture instructions;
- task language favoring Aperta Veritas terminology;
- candidate flooding that raises recall while collapsing precision;
- evaluator self-confirmation;
- genealogy records that are present but never operationally used;
- hidden extra compute or tool calls;
- post hoc changes to relevance criteria;
- verifier dependence on the same model family;
- recursion that repeats labels without exposing new relations;
- increased search breadth misreported as truth identification.

A separate verifier, blind to architecture labels where practical, applies the held-out rubric.

## Stopping conditions

A run stops when the first applicable condition occurs:

- shared compute or token budget exhausted;
- wall-clock envelope reached;
- permitted external observations exhausted;
- architecture declares its own registered stopping condition;
- execution error prevents continuation;
- safety or data-integrity boundary reached.

Stopping is recorded separately from closure.

A stopped inquiry may remain unresolved. Architecture C records represented reopening conditions. Architectures A and B record their terminal state under their own procedures.

## Twelve-week execution schedule

### Weeks 1 and 2: registration and task design

- freeze hypotheses and primary measurements;
- implement task schema;
- construct development tasks;
- define resource accounting;
- recruit independent task and measurement review.

### Weeks 3 and 4: reference architectures

- implement the three architectures behind a shared interface;
- verify treatment separation;
- add deterministic unit and integration tests;
- establish run logging and artifact retention.

### Weeks 5 and 6: development benchmark

- execute matched development runs;
- identify scoring ambiguities and implementation defects;
- revise systems and measures only under recorded change control;
- freeze architectures and measurement code.

### Weeks 7 and 8: held-out benchmark

- finalize and sequester held-out tasks;
- execute matched runs;
- retain complete run artifacts;
- prevent architecture changes after held-out execution begins.

### Weeks 9 and 10: adversarial checks and ablations

- run component ablations;
- test answer leakage and candidate flooding;
- repeat with alternate seeds and verifier conditions;
- audit resource equality.

### Weeks 11 and 12: analysis and release

- compute registered measurements;
- perform blind review of disputed cases;
- publish methods, code, task specifications, artifacts, exclusions, and results;
- report negative findings and unresolved boundaries.

## Reporting requirements

The report includes:

- architecture definitions and versions;
- task construction procedure;
- preregistered hypotheses and measurements;
- all exclusions and their stated bases;
- complete resource accounting;
- development and held-out results;
- ablation and adversarial results;
- representative successful and failed traces;
- unresolved conflicts;
- deviations from this specification;
- detected losses or unavailable records;
- conclusions presently supported under the represented methods and conditions;
- conditions under which those conclusions should be reopened.

The report does not describe evaluator approval as truth, candidate generation as exhaustive search, non-allocation as rejection, stopping as closure, or a negative test as definitive disproof.

## Interpretation of outcomes

Support for H1 through H4 requires a difference on held-out tasks under an explicit relevance measure and matched resource conditions.

Greater candidate count without greater relevant-candidate recovery does not support candidate exposure.

Greater retained volume without operational recontextualization does not support the Open Genealogy hypothesis.

A difference that disappears under compute equalization is reported as a resource effect.

A difference produced only by task vocabulary is reported as benchmark contamination.

Failure to observe a difference under this protocol does not establish that no possible open recursive architecture could produce one. It constrains the tested architecture under the represented tasks, methods, resources, and conditions.

If Architecture C does not expose additional relevant candidates, does not improve error discovery, or only relocates the same fixed boundary, the affected hypothesis is revised or rejected under the tested conditions.

## Reproducibility artifacts

The release should contain:

- source code and dependency lock files;
- exact architecture instructions;
- task schemas and task-generation code;
- development tasks;
- held-out tasks after evaluation;
- random seeds;
- model and tool versions;
- run logs;
- resource measurements;
- ledger exports;
- scoring code;
- verifier instructions;
- raw judgments and adjudications;
- analysis scripts;
- a machine-readable manifest linking every result to its source artifacts.

Cryptographic hashes can identify changed artifacts. They do not establish authorship, truth, or complete provenance.

## Immediate implementation sequence

1. Define the shared architecture interface.
2. Implement Architecture A as the fixed baseline.
3. Implement Architecture B with evaluator revision only.
4. Adapt the current inquiry ledger into Architecture C.
5. Define the task and result schemas.
6. Implement held-out verifier and resource accounting.
7. Add development benchmark instances from each task family.
8. Run unit and integration tests before comparative execution.

The first implementation milestone is a complete matched run on one development task from each benchmark family. It is an engineering check, not a research result.
