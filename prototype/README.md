# Executable Prototype

This directory contains the minimum executable Aperta Veritas ledger described in [`../OPERATIONAL_SYSTEM.md`](../OPERATIONAL_SYSTEM.md).

The prototype tests whether core RTE operations can be represented computationally rather than merely stated conceptually.

It demonstrates that:

- inquiry states can be appended rather than overwritten;
- conclusions can remain distinct from the represented support for treating them as true;
- comparison can identify a conclusion as better supported under explicit measurements and conditions without certifying it as definitive truth;
- beliefs, confidence, values, and support can remain distinct representations;
- selected, inactive, unresolved, and superseded branches can remain genealogically represented;
- selection can require an attributed evaluator and explicit criteria;
- stopping can remain distinct from epistemic closure;
- reopening conditions can remain represented;
- recursive audits can expose their own evaluator, criteria, measurements, and stopping boundary;
- a hash chain can make alteration of recorded genealogy detectable.

The hash chain is tamper-evident, not physically immutable.

The prototype does not certify truth, losslessness, neutrality, completeness, or exhaustive representation. It does not assume that the represented comparison set contains every possible conclusion.

Its operational invariant is:

```text
best_supported != definitive_truth
