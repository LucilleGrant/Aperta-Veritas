## 0.4.0-draft, 2026-09-19

* Added a minimal append-only inquiry ledger with hash-chained records.
* Required each transition to retain prior states and attribute selection criteria to an evaluator.
* Preserved selected and inactive branches within the same transition genealogy.
* Added recursive audit records exposing the auditor, unrepresented relations, and stopping boundary.
* Added tests for evaluator attribution, branch retention, alteration detection, immutability, recursive audit, and export.
* Recorded endogenous branch reactivation as the next implementation boundary.
