# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [ADR-0001], [ADR-0002], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008], [RC-009], [RC-010], [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016], [RC-017], [RC-018], [RC-019], [RC-020], [RC-021], [RC-022], [RC-023] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version with the plan documents and RC-001 to RC-008 | [b64ad78] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-019 for MIL-002 task 7 | [46f5db5] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-017 and RC-018 for the endpoint change | [fdf51d6] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-016 for MIL-003 task 7 | [bf42eed] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-015 for the re-review of MIL-003 | [2421865] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-014 for MIL-004 | [77d840f] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-013 for MIL-003 | [05ca87b] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-012 for MIL-002 | [a8889c5] |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-009 to RC-011 for MIL-001 | [0c1627b] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-005, the review records RC-020 to RC-023 and the wiki; set the reviewed rows of BC-001 and PP-001 and the domain of the changed rows to education; corrected the CrossReference row and the stale coverage note (autonomous, not independent) | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-020], [RC-001], [RC-017] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-021] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-003], [RC-009], [RC-010], [RC-011] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-004], [RC-012], [RC-018], [RC-019] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-005], [RC-013], [RC-015], [RC-016] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-006], [RC-014] |
| [MIL-005] | MIL | en | education | [BC-001], [PP-001], [MIL-004] | - | [RC-022] |
| [ADR-0001] | ADR | - | - | [BC-001], [SA-001] | [MIL-001], [MIL-002] | [RC-007] |
| [ADR-0002] | ADR | - | - | [BC-001] | [MIL-002], [MIL-003] | [RC-008] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-005] | - | [RC-023] |

## Coverage Notes

- `-` in Upstream means the instance is foundational, in Downstream that nothing is built on it yet, and in Last Reviewed that no `RC-*` exists yet.
- [PP-001] was accepted without a QC checklist; it is reviewed against `QC-PP-001` for the first time in [RC-021].
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-023].
- The project workflow `.gitea/workflows/publish-wiki.yml` that MIL-001 installed was removed in the commit "Use git-workflows and the scoped workflows", when the repository moved to the shared workflows of the git host; RC-010 and RC-011 reviewed it while it existed. `ci.yml` and `english-comments.yml` are still reviewed there.
- The domain of [BC-001], [PP-001], [MIL-005] and the wiki is `education` since [MIL-005]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-005] changes no source file, so the source code is not reviewed again. Its only changes under `tests/` are the pattern of the shared workflow repository in `tests/unit/test_workflows.py` and the sidebar test in `tests/unit/test_wiki.py` (task 6), and its only change to a workflow is the version of the `upload-artifact` step of `ci.yml` (task 7); the test suite and the checks of the pull request verify them, and no new code review record is written for them.
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
[RC-009]: ./reviews/rc-009-mil-001-code.md
[RC-010]: ./reviews/rc-010-mil-001-yaml.md
[RC-011]: ./reviews/rc-011-mil-001-workflows.md
[RC-012]: ./reviews/rc-012-mil-002-code.md
[RC-013]: ./reviews/rc-013-mil-003-code.md
[RC-014]: ./reviews/rc-014-mil-004-code.md
[RC-015]: ./reviews/rc-015-mil-003-sheety-log-rereview.md
[RC-016]: ./reviews/rc-016-mil-003-user-agent-code.md
[RC-017]: ./reviews/rc-017-business-case-rereview.md
[RC-018]: ./reviews/rc-018-mil-002-rereview.md
[RC-019]: ./reviews/rc-019-mil-002-endpoint-code.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474
[0c1627b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/0c1627b24991d5659f04d5d128919b2db3d4f246
[a8889c5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/a8889c53cf57967762325668735e2b16f628979f
[05ca87b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/05ca87b28a2113c927ffb22fde75a77ebe0476c1
[77d840f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/77d840f9d01a643508bb5251803ff0b7750c392f
[2421865]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/2421865cd6604b0aae14fd3799ccd032f713d622
[bf42eed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/bf42eedca536619bdc54dca57f5c159d45c2113b
[fdf51d6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/fdf51d6cd3c01862929c5c696d42b04800f3affb
[46f5db5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/46f5db526e5df41e0931755e53d4c5b37072153b
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-020]: ./reviews/rc-020-business-case-baseline.md
[RC-021]: ./reviews/rc-021-project-plan-baseline.md
[RC-022]: ./reviews/rc-022-milestone-005.md
[RC-023]: ./reviews/rc-023-wiki.md
