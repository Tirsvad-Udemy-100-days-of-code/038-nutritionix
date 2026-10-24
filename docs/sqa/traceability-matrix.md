# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [ADR-0001], [ADR-0002], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version with the plan documents and RC-001 to RC-008 | [b64ad78] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-003] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-004] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-005] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | - | [RC-006] |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-007] |
| [ADR-0002] | ADR | - | - | [BC-001] | [MIL-002], [MIL-003] | [RC-008] |

## Coverage Notes

- `-` in Upstream means the instance is foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no `RC-*` exists yet.
- The Project Plan has no QC checklist; S01 accepted it in chat on 2026-10-24, so it has no review record.
- The types KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD and DICT have no instance (ADR-0002).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-nutritionix-exercises.md
[MIL-003]: ../milestones/mil-003-sheety-log.md
[MIL-004]: ../milestones/mil-004-docs-and-wiki.md
[ADR-0001]: ../adr/adr-0001-urllib-no-runtime-dependency.md
[ADR-0002]: ../adr/adr-0002-no-use-case-artifacts.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-project-setup.md
[RC-004]: ./reviews/rc-004-mil-002-nutritionix-exercises.md
[RC-005]: ./reviews/rc-005-mil-003-sheety-log.md
[RC-006]: ./reviews/rc-006-mil-004-docs-and-wiki.md
[RC-007]: ./reviews/rc-007-adr-0001.md
[RC-008]: ./reviews/rc-008-adr-0002.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474
