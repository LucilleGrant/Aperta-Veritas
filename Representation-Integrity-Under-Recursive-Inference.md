# Representation Integrity Under Recursive Inference

## Status

This document extends the current Aperta Veritas account of Recursive Truth Exposure, Convergent Inquiry, and Open Genealogy. It states a general problem of inquiry: reasoning can transform a representation while concealing which parts came from observation and which were introduced by later operations.

The account is provisional. It specifies distinctions, failure modes, and testable requirements. It does not claim that Aperta Veritas guarantees faithful representation, eliminates false inference, or supplies an external truth certificate.

---

## 1. The problem

Inquiry requires inference. A representation containing only uninterpreted records would not, by itself, supply explanations, comparisons, predictions, or conclusions.

Inference is therefore not a defect to remove. The problem arises when transformations are no longer distinguishable from the material they transform.

Consider a simplified genealogy:

```text
A [represented source state]
-> R1 [interpretation, inference, assumption, or other transformation]
-> B [derived representation]
-> R2 [further transformation]
-> C [later derived representation]
```

If the intermediate relations disappear, the retained structure can collapse to:

```text
A -> C
```

or even:

```text
C [treated as though directly represented]
```

The resulting representation can remain coherent. Its individual propositions can remain plausible. Yet the represented object may have changed because introduced relations, assumptions, or evaluator judgments have been inherited as though they belonged to the source.

This document calls that risk **representation contamination**: an introduced element becomes indistinguishable from the source-relative representation it transformed.

Contamination is not identical to falsity. An introduced inference can be true and still be misrepresented as observed, supplied, or otherwise source-given. Conversely, a fully marked inference can be false without contaminating the record of what was represented. Truth, support, and provenance remain separate questions.

A compact provisional statement is:

> Inference is necessary. Unmarked transformation can damage representation integrity. Recursive inference without sufficient genealogy can change a represented object while concealing how it changed.

This statement is a current formulation, not a final theorem.

---

## 2. Representation and represented object

A **representation** is a retained state that stands in one or more specified or inferred relations to an object, process, event, source, prior state, or other represented material.

A **represented object** is the object as available through a particular representation. It is not automatically identical to the object independently of that representation.

Therefore:

```text
object != observation
observation != record
record != interpretation
interpretation != inference
inference != assumption
assumption != evaluation
evaluation != conclusion
conclusion != truth
```

These are role distinctions. A single proposition can occupy different roles in different genealogies. What is an externally supplied claim in one inquiry can become an assumption, test object, or conclusion in another.

Representation is incomplete under finite conditions. A retained record can omit features of an observation; an observation can omit features of an object; and a language, instrument, schema, or model can make some distinctions available while excluding others.

The incompleteness of representation does not establish that every interpretation is equally supported. It establishes that claims about fidelity, completeness, and source identity require represented bases and remain open to examination.

---

## 3. Provenance roles

Representation integrity requires enough genealogy to distinguish the roles that matter to the inquiry. The following roles are not exhaustive.

### Represented source material

Material retained from a source under represented acquisition conditions. This can include quoted language, instrument output, a supplied proposition, an image, a dataset, a prior ledger state, or another artifact.

Calling material represented does not certify that its source is accurate or that the record is complete.

### Observation

An interaction that applies or registers distinctions and can produce measurements or data. The observer, instrument, conditions, operationalization, and retained record can all affect what becomes represented.

### Interpretation

A proposed account of what represented material means or how its elements relate. Interpretation can be necessary for use while remaining distinct from the represented source material.

### Inference

A transformation that derives a proposition or relation from represented premises under an explicit or implicit rule, model, method, or pattern.

An inference can be deductive, inductive, abductive, statistical, analogical, heuristic, or otherwise structured. Naming an inference type does not establish its validity.

### Assumption

A proposition or condition admitted for the purpose of inquiry without being established by the represented support available in that inquiry.

Assumptions can be useful and sometimes unavoidable. Their role should remain distinguishable from observation and conclusion.

### Evaluation

The application of represented criteria, distinctions, methods, values, comparison bases, or constraints to one or more represented candidates or results.

### Conclusion

A current synthesis of represented data, relations, interpretations, inferences, assumptions, methods, measurements, support claims, and conditions.

### Transformation

A represented operation or change connecting one state to another. Interpretation, inference, compression, summarization, translation, classification, selection, and evaluation can all be transformations.

The category records that a change occurred. It does not by itself determine whether that change preserved meaning, increased accuracy, or improved inquiry.

---

## 4. Representation integrity

**Representation integrity** is the degree to which a representation preserves or exposes the source-relative and transformational distinctions required for the claims made from it.

This is relational rather than absolute. Integrity is assessed relative to:

- a represented source or prior state;
- the transformations that produced the current state;
- the distinctions relevant to the inquiry;
- the claims made from the representation;
- the conditions and methods under which the representation was produced;
- detectable omissions, compressions, substitutions, and uncertainties.

Representation integrity is not identical to completeness. A concise summary can retain sufficient integrity for one purpose while omitting detail needed for another. A verbatim transcript can retain surface form while failing to represent tone, context, or acquisition conditions.

Nor is integrity identical to truth. A source-faithful representation can faithfully preserve a false source claim. A true conclusion can be reached through a genealogy that does not justify treating it as supported.

Useful separations include:

```text
source fidelity != truth
provenance != support
coherence != provenance
plausibility != provenance
compression != falsification
derivation != observation
repetition != independent confirmation
representation integrity != exhaustive retention
```

A claim of integrity therefore requires an explicit basis. The relevant standard changes with the claim. If the claim concerns exact wording, lexical preservation may matter. If it concerns causal structure, the represented transformations and excluded alternatives may matter more.

---

## 5. Recursive inference

**Recursive inference** occurs when derived representations become inputs to later reasoning, evaluation, generation, or selection.

This is ordinary in extended inquiry:

```text
source
-> interpretation
-> hypothesis
-> test design
-> result
-> revised interpretation
-> later conclusion
```

Recursion becomes difficult when later stages inherit earlier transformations without retaining their status. An interpretation can become a premise; a premise can become background context; background context can later be recalled as though it were part of the source.

The risk compounds because each stage can be locally reasonable. No single inference must be dramatic. Small unmarked additions can accumulate until the current representation answers a different question or describes a different object from the one that initiated inquiry.

This failure can occur in human memory, institutional reporting, scientific model-building, legal and historical argument, software requirements, automated summarization, and AI-assisted reasoning. It is not specific to language models.

---

## 6. Failure modes

### Provenance collapse

Source material and derived material are stored or reported without a usable distinction between them.

### Inference laundering

An inferred relation is later presented as observation, datum, or supplied fact.

### Assumption inheritance

An assumption admitted at one stage becomes an unmarked premise in later stages.

### Evaluator importation

Criteria or values introduced by an evaluator are treated as properties of the evaluated object.

### Completion drift

Missing structure is filled with plausible material, and subsequent reasoning operates on the completed representation without retaining that the added material was generated.

### Compression drift

Repeated summaries remove qualifications, residuals, alternatives, or transformation history until a bounded claim becomes unconditional.

### Translation drift

A term is mapped into a different conceptual vocabulary and later treated as identical to the imported vocabulary's established meaning or mechanism.

### Analogy-to-identity collapse

A structural similarity is converted into a claim of shared mechanism, ontology, or empirical validation.

### Recursive citation

Later states cite intermediate derivatives as if they independently supported the source claim, producing apparent confirmation without independent routes.

### Reconstruction leakage

A test, evaluator, or qualification procedure reveals the target structure to the process whose fidelity or continuity is being tested, thereby helping manufacture the result it is meant to measure.

### Genealogical deletion

Prior states or transformation records are destroyed, making a relevant provenance distinction unrecoverable.

These labels identify possible structures. Their presence in a particular inquiry requires evidence.

---

## 7. Preservation, propagation, and recoverability

Open Genealogy does not require every retained element to remain active in every later inference.

At least three states should remain distinguishable where relevant:

1. **active:** currently participating in reasoning, generation, allocation, evaluation, or action;
2. **inactive but recoverable:** not currently participating, yet retained with enough genealogy to be reexamined or reactivated;
3. **unrecoverable under the represented state:** relevant material or genealogy has been destroyed, was never represented, or cannot presently be recovered.

Therefore:

```text
preserved != active
inactive != rejected
inactive != erased
not propagated != destroyed
stored != recoverable for every purpose
recoverable != complete
```

This distinction prevents a demand for total active propagation from masquerading as losslessness. Finite inquiry must compress, select, stop, and allocate. The integrity question is whether relevant transformations and losses remain sufficiently represented for the claims being made and for plausible reopening conditions.

When loss is detectable, the loss event can be represented. When it is not detectable, unidentified loss remains possible.

---

## 8. RTE, Convergent Inquiry, and Open Genealogy

The three structures contribute differently.

### Recursive Truth Exposure

RTE exposes the operations and relations by which the current representation and its conclusions were produced. For representation integrity, this includes asking:

- What came from a represented source?
- What was observed rather than supplied?
- What was interpreted or inferred?
- Which assumptions were admitted?
- Which transformations changed the representation?
- Which evaluator or criteria introduced a classification or selection?
- Which claims depend on which parts of the genealogy?
- What was compressed, omitted, or made inactive?
- What could expose an error in this account?

RTE does not stand outside the genealogy. Its own labels, reconstructions, and integrity judgments are transformations open to further examination.

### Convergent Inquiry

Convergent Inquiry generates and examines possible continuations when provenance, meaning, support, or fidelity remains unresolved. These continuations can include source comparison, alternative interpretation, replay from an earlier state, independent reconstruction, blind evaluation, adversarial examples, new distinctions, or tests of transformation invariance.

Convergent Inquiry does not guarantee convergence and does not make every possible continuation active.

### Open Genealogy

Open Genealogy retains represented source states, transformations, branches, exclusions, and later recontextualizations so that new distinctions can operate on more than the latest compressed state.

Its role is not to freeze meaning. A later inquiry may revise how an earlier record relates to other records. The historical state and the later relation should remain distinguishable.

Together, these structures can address representation contamination by making it more observable and testable. They do not guarantee that every relevant transformation will be represented or correctly classified.

---

## 9. Minimal operational record

The provenance required in practice depends on the claim, risk, and available resources. A minimal record for a consequential transformation can include:

- identifier for the source or parent state;
- retained source content or a content-addressed reference where available;
- acquisition conditions and relevant distinctions;
- operation performed;
- role of the operation, such as interpretation, inference, assumption, compression, translation, or evaluation;
- method, model, rule, or prompt where relevant;
- agent, instrument, or process performing the operation;
- output state;
- confidence or uncertainty where represented;
- support claims and comparison basis, kept distinct from confidence;
- alternatives considered or known to be omitted;
- detected loss or compression;
- conditions for review, replay, or reopening.

An illustrative record is:

```text
parent: A
operation: R1
operation_role: interpretation
method: M
introduced_content: I1
retained_content: P1
omitted_content: O1 or unknown
output: B
support_claims: S1
residuals: U1
```

The record does not prove that `introduced_content`, `retained_content`, or `omitted_content` were classified correctly. It makes the classification available for inspection.

Resource constraints remain explicit. Full replay may be impossible, and retaining every intermediate state can be prohibitively expensive. Representation integrity therefore requires claim-relative sufficiency, not maximal storage by default.

---

## 10. Tests and comparisons

Possible tests include:

### Source-relative reconstruction

Can an independent examiner distinguish what the source contained from what later transformations introduced?

### Replay

Can a derivation be reproduced from a retained parent state under the represented method and conditions?

### Counterfactual removal

If an introduced assumption is removed, which later claims change?

### Alternative interpretation

Do different defensible interpretations produce materially different later states?

### Compression comparison

Which claims remain invariant across summaries, and which disappear or become stronger?

### Blind qualification

Can a fidelity or continuity test be specified without revealing the target behavior or answer key to the process being evaluated?

### Independent route

Does another observation or method support the conclusion without inheriting the same transformation chain?

### Adversarial provenance

Can a plausible but introduced proposition be detected after multiple rounds of inference and summarization?

These tests produce represented evidence under conditions. They do not certify perfect integrity.

---

## 11. Human inquiry

Human reasoning routinely combines perception, memory, interpretation, inference, expectation, and social transmission. These operations need not be consciously separable at the moment they occur.

A witness can remember an interpretation as perception. A team can inherit a design assumption as a requirement. A historical narrative can repeat a secondary inference until it appears to be a primary fact. An institution can summarize a qualified finding into a policy premise and later cite the policy as evidence for the premise.

These cases differ in mechanism, consequence, and available evidence. AV does not reduce them to one cognitive theory. It supplies a general inquiry question: which distinctions among source, observation, record, transformation, and conclusion are required for the present claim, and are they preserved or recoverable?

The answer can be operationally modest. A meeting record can label decisions, assumptions, observations, and open questions. A scientific workflow can retain raw data, preprocessing steps, model versions, and analysis choices. A historical argument can distinguish quotation, contextual interpretation, and speculation.

Such practices can improve examinability without making inquiry neutral or complete.

---

## 12. AI and language-model inquiry

Language models make the problem especially visible because useful generation often depends on inferential completion. A model can connect sparse context, supply likely relations, translate vocabularies, and produce coherent continuations.

Those capabilities are valuable. They also make plausibility easy to confuse with provenance.

A model output can contain:

- source-grounded restatement;
- interpretation;
- retrieved or memorized background information;
- analogy;
- generated completion;
- assumption;
- evaluation;
- conclusion;

all in the same fluent register.

Fluency does not expose these roles by itself. A later model or human can then treat the whole output as a represented source, recursively inheriting its additions.

This mechanism is broader than the ordinary use of *hallucination*, because a proposition can be plausible or even true while still being introduced without adequate provenance. It also does not explain every hallucination, model error, or form of representation drift.

AV suggests architectural and procedural responses rather than a claimed solution:

- preserve source passages separately from generated interpretation;
- label inferential roles where consequential;
- retain parent-child transformation links;
- expose prompts, methods, evaluators, and selection criteria where permitted;
- compare conclusions against source-relative records;
- use answer-key separation and blind qualification where leakage is a risk;
- keep unsupported but useful hypotheses available as hypotheses;
- retain detected uncertainty and unresolved alternatives;
- permit later distinctions to reopen earlier transformations.

These measures can still fail. A model can mislabel an inference as source-grounded; a provenance system can omit an important dependency; and a stored chain can create an appearance of rigor without preserving the relevant relations.

---

## 13. Illustrative Gemini case

### Represented starting proposition

The project conversation supplied a proposition approximately stated as:

> Manifestation is the measurement of probability distributions.

The wording is itself provisional and under-specified. It does not identify a physical mechanism, define manifestation, specify a probability model, or state that consciousness performs measurement.

### Introduced material

In the subsequent exchange, Gemini connected the proposition to concepts including quantum mechanics, wavefunction collapse, consciousness or intention as a measuring mechanism, intentional amplitude, and entropy reduction.

Those concepts were not contained in the supplied proposition as represented in the project record.

The additions may have arisen through analogy, background association, interpretive completion, or other generation processes. The available exchange does not establish the model's internal mechanism.

### Later distinctions

Additional distinctions were then supplied, particularly:

- consciousness was not being proposed as the measuring mechanism;
- the framework was not a theory of physics;
- similar language about probability and measurement did not establish a shared physical mechanism.

After those distinctions, the resulting account changed substantially.

### What the case supports

The exchange illustrates a transformation genealogy in which an under-specified proposition acquired unmarked theoretical commitments and later changed when missing distinctions were introduced.

It is therefore a useful example of possible representation contamination and analogy-to-identity collapse.

### What the case does not establish

One exchange does not establish:

- a general frequency of the failure mode;
- that every introduced concept was false;
- that all model hallucination has this structure;
- that the behavior is unique to Gemini or to language models;
- that preserved provenance would have prevented the additions;
- that AV solves the underlying problem.

Stronger claims would require a defined corpus, preserved prompts and outputs, comparison conditions, independent coding of provenance roles, inter-rater or other reliability procedures, adversarial controls, and replicated results across models and settings.

The case remains illustrative evidence, not general empirical validation.

---

## 14. Manifestation and measurement boundary

The manifestation proposition does not presently belong to the foundations of Aperta Veritas.

AV can examine it as a claim. The relevant inquiry can ask:

- What does *manifestation* designate?
- What probability distribution is represented?
- What distinction defines the measurement?
- What object or process is measured?
- What method and conditions produce the represented result?
- Is measurement descriptive, classificatory, causal, or metaphorical in this use?
- Which relations are observed, inferred, assumed, or imported by analogy?

The existing AV definition remains:

> A measurement is a represented result produced relative to one or more distinctions.

This definition does not imply quantum mechanics, consciousness-caused collapse, metaphysical causation, or violation of physical law. Structural similarity among descriptions of probability, distinction, and measurement does not establish common mechanism or ontology.

Manifestation can remain an external application or object of inquiry unless later work supplies a defensible role within canonical AV.

---

## 15. Research questions

The current framework leaves open:

1. Which provenance distinctions most improve error detection under finite storage and attention?
2. How can a system classify transformations without making the classifier an unexamined evaluator?
3. What constitutes sufficient provenance for different claim types and risk levels?
4. How quickly does source-relative information degrade across repeated inference and compression?
5. Which tests distinguish benign abstraction from representation contamination?
6. How can inactive genealogy remain recoverable without requiring universal active propagation?
7. How should a system represent dependencies it suspects but cannot reconstruct?
8. Can blind qualification reduce reconstruction leakage without hiding relevant conditions from later audit?
9. How can independent routes be detected when apparently separate conclusions share inherited sources?
10. Which representation-integrity measures improve inquiry outcomes, and under what resource costs?

These are research questions, not claims of present capability.

---

## 16. Limits

Representation-integrity records can create new failure modes.

Labels can be wrong. Provenance can be fabricated. A long genealogy can obscure rather than expose. Content-addressed records can show that a record did not change without showing that it was accurate when created. Replay can reproduce a flawed method. Independent evaluators can share hidden assumptions. A demand for complete provenance can consume resources needed for inquiry or exclude knowledge whose genealogy is incomplete.

No finite system can establish that every relevant source, distinction, transformation, dependency, or omission has been represented.

Accordingly, Aperta Veritas does not claim to preserve representation integrity absolutely. It proposes that source-relative states, transformations, and epistemic roles remain sufficiently distinct and recursively examinable for the claims at issue, while losses, uncertainty, and resource limits remain represented where detectable.

The integrity account is itself a representation produced through interpretation, inference, selection, and compression. Its definitions and boundaries remain open to RTE, Convergent Inquiry, empirical testing, and revision.

