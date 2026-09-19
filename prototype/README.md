Executable Prototype
This directory contains the minimum executable Aperta Veritas ledger described in `docs/OPERATIONAL_SYSTEM.md`.
It demonstrates that inquiry states can be appended rather than overwritten, selected and inactive branches can remain represented, selection can require an attributed evaluator and explicit criteria, recursive audits can expose their own evaluator and stopping boundary, and a hash chain can make alteration of recorded genealogy detectable.
The hash chain is tamper-evident, not physically immutable. The prototype does not certify truth, losslessness, neutrality, or completeness.
Run the tests from this directory:
```bash
python -m unittest -v
```
The next implementation boundary is endogenous branch reactivation. The prototype records reopening conditions but does not yet evaluate them against new observations.
