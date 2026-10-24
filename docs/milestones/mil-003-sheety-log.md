# MIL-003: Sheety log

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This gate decides whether the second and third assignment steps work: one row per exercise is posted to the Sheety endpoint with the current date and time, the request is authenticated with a bearer token or basic authentication, and every secret and endpoint comes from the process environment. It also decides whether the command line ties the two steps together.

## Deliverable

An `add_workout_row` function and a `log_workout` use case, the Sheety authentication header (bearer or basic), the environment configuration for `SHEET_ENDPOINT`, `TOKEN`, `USERNAME` and `PASSWORD`, a `log` command with a dry run, and tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `from exercise_tracker import add_workout_row` works | Imports | ImportError |
| 2 | A test shows that one POST per exercise is sent to the sheet endpoint with the camelCase body `{"workout": {"date", "time", "exercise", "duration", "calories"}}` | Pass | Fail |
| 3 | A test shows that the date is `dd/mm/YYYY`, the time is `HH:MM:SS` (both from an injected clock) and the exercise name is in title case | Pass | Fail |
| 4 | A test shows that `Authorization: Bearer <token>` is sent when `TOKEN` is set, basic authentication when only `USERNAME` and `PASSWORD` are set, and the bearer wins when both are set | Pass | Fail |
| 5 | `python -m exercise_tracker --dry-run log "ran 5k"` prints the requests with secrets hidden and sends nothing | Secrets hidden | Any secret printed |
| 6 | A missing `SHEET_ENDPOINT` raises an error that names the variable without showing any value | Pass | Fail |
| 7 | The integration and end-to-end tests use a local test server only | Local only | Any external host |
| 8 | `ruff`, `mypy --strict` and `pytest` are clean with at least 90 % line coverage, and the code review against `QC-PY-001` is a Go | Clean and Go | Any finding or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The gateway port, adapters, configuration and `get_exercises` must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2 (one row per exercise with date and time) | [BC-001] |
| Objective 3 (authentication and environment variables) | [BC-001] |
| Objective 4 (offline tests) | Success criteria 2, 3 and 4 of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-27 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add WorkoutRow value object and Clock port | Add a `WorkoutRow` in `domain/` that formats date and time with `strftime` and the exercise name with `.title()`, and a `Clock` port so tests can fix the time. | No | ADR-0002 (Architecture Decision Record) |
| 2 | Implement add_workout_row use case | Add `add_workout_row(gateway, sheet, row)` in `application/use_cases/` that posts the camelCase `workout` body of the lecture to the sheet endpoint; this is the second assignment step. | No | ADR-0002 |
| 3 | Add Sheety authentication | Build the `Authorization` header from the bearer token, or from the username and password with basic authentication, and keep the choice in configuration so the use cases do not know it. | No | |
| 4 | Extend environment configuration | Read `SHEET_ENDPOINT`, `TOKEN`, `USERNAME` and `PASSWORD` from the process environment with clear errors; the project never reads or imports `.env`. | No | |
| 5 | Implement log_workout and the log command | Combine the two steps: query Nutritionix, then post one row per exercise. Add the composition root and the `log` command with `--dry-run` in `presentation/`, and export the functions from the package. | No | |
| 6 | Add tests for the Sheety log | Add unit tests with a fake gateway and a fixed clock, an integration test against a local `http.server`, and an end-to-end test of the command, all offline; plus the code review record for the milestone. | No | |

---

[BC-001]: ../business-case.md
