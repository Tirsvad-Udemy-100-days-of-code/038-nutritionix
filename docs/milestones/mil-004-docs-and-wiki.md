# MIL-004: Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This gate decides whether S02 and S03 can understand and run the project from its documents alone: the README, the screenshots, the wiki in three languages and the Doxygen output.

## Deliverable

The final README with screenshots, a wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia with the same page set, the wiki publish workflow, and the project documents brought up to date.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README follows the framework template and `check-readme.sh` passes | Passes | Fails |
| 2 | The README and the wiki show at least two screenshots (the dry run and the tests) that exist as files | Present | Missing |
| 3 | `docs/wiki/` has the same pages in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) and a `_Sidebar.md` that lists every language | Same page set | Any page missing |
| 4 | `check-languages.sh` reports no defect | Clean | Any defect |
| 5 | `doxygen Doxyfile` runs without a warning, or the criterion is reported as not verified when `doxygen` is not installed | Clean or reported | Warnings |
| 6 | The workflow that publishes the wiki is in `.gitea/workflows/` | Present | Missing |
| 7 | No key, token or endpoint of the author is in a document, a screenshot or the git history | None | Any found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The documents describe the finished program and the screenshots show it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 7 (README, wiki, screenshots) | Success criterion 6 of [BC-001] |
| Objective 5 (run instructions) | Success criterion 5 of [BC-001] |
| Objective 6 (Doxygen) | Scope of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-28 — the end of the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Take screenshots | Capture the dry run of the `log` command with fake values and the pytest run as images in `docs/images/`, so the README and the wiki can show them; no real key or endpoint may appear. | No | |
| 2 | Finish the README | Complete the README from the framework template with the screenshots, the mapping from each lecture step to a function, the environment variables and the list of secrets the workflows need. | No | |
| 3 | Write the English wiki | Write the pages Home, Getting Started, Usage, Architecture and Development in `docs/wiki/` with `_Sidebar.md`, as `framework/process/wiki.md` describes. | No | |
| 4 | Translate the wiki to Danish and Bahasa Malaysia | Add the `-da` and `-ms` page for every English page, with the language line at the top and code, commands and IDs unchanged. | No | |
| 5 | Install the wiki publish workflow | Copy the publish-wiki workflow that calls `TirSystem/github-action`, and list the secret `TOKEN_FOR_GITEA_WIKI` in the README. | No | |
| 6 | Update the project documents | Record the final state in the Project Plan (milestone links) and the traceability matrix, and generate the Doxygen output once to check it. | No | |

---

[BC-001]: ../business-case.md
