# MIL-002: Nutritionix exercises

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b64ad78] |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Endpoint is the 100 Days of Python service; added criteria 8 and 9 and task 7 | [fdf51d6] |

---

## Purpose

This gate decides whether the first assignment step works: a plain English sentence is sent to the Nutritionix natural language exercise endpoint and the answer becomes exercises with a name, a duration and calories. It also decides whether the layers that the second step reuses (domain, the HTTP (Hypertext Transfer Protocol) gateway port, the standard library adapter, the environment configuration) are sound.

## Deliverable

A `get_exercises` function and the domain `Exercise` value object, the `HttpGateway` port, the `urllib` adapter, a dry-run adapter, the environment configuration for `APP_ID` and `API_KEY`, and unit, integration and end-to-end tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `from exercise_tracker import get_exercises` works | Imports | ImportError |
| 2 | A test shows that `get_exercises` sends a POST to `https://app.100daysofpython.dev/v1/nutrition/natural/exercise` with the `x-app-id` and `x-app-key` headers and the JSON (JavaScript Object Notation) body `{"query": ...}` | Pass | Fail |
| 3 | A test shows that the answer is parsed into exercises with name, `duration_min` and `nf_calories` | Pass | Fail |
| 4 | A test shows that an empty query is rejected before any request is sent, and that an HTTP error status raises a specific error | Pass | Fail |
| 5 | A missing `APP_ID` or `API_KEY` raises an error that names the variable and never shows a value | Pass | Fail |
| 6 | The integration test sends a real HTTP request to a local test server only | Local only | Any external host |
| 7 | `ruff`, `mypy --strict` and `pytest` are clean, and the code review against `QC-PY-001` is a Go | Clean and Go | Any finding or No-Go |
| 8 | A test shows that a query of more than 50 characters is rejected before any request is sent | Pass | Fail |
| 9 | A test shows that an error answer of the form `{"error": {"code", "message"}}` gives its message in the raised error | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The project configuration, `constants.py` and the test setup must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 (plain English to exercises) | [BC-001] |
| Objective 3 (keys from the environment) | [BC-001] |
| Objective 4 (offline tests) | Success criteria 1, 2 and 3 of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-26 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Exercise value object and errors | Add the `Exercise` value object (name, duration in minutes, calories) and an `InvalidInputError` in `domain/`, so that bad input and empty queries are stopped before a request. | No | ADR-0002 (Architecture Decision Record) |
| 2 | Add HttpGateway port and response object | Define in `application/ports/` the narrow `HttpGateway` protocol (send one JSON POST with headers) and in `application/dto/` the `HttpResponse` with the status code and the decoded body, so use cases do not depend on `urllib`. | No | ADR-0002 |
| 3 | Implement get_exercises use case | Add `get_exercises(gateway, credentials, query)` in `application/use_cases/` that builds the Nutritionix request of the lecture and parses the exercises of the answer; this is the first assignment step. | No | ADR-0002 |
| 4 | Add urllib gateway and dry-run gateway | Implement `HttpGateway` with `urllib.request` in `infrastructure/http/` (with a timeout, and an HTTP error status returned as a response rather than raised) and a dry-run gateway that prints the request with secrets hidden. | No | ADR-0001 |
| 5 | Add environment configuration | Read `APP_ID` and `API_KEY` from the process environment in `infrastructure/config/`; the project never reads or imports `.env`. | No | |
| 6 | Add tests for Nutritionix exercises | Add unit tests with a fake gateway, an integration test against a local `http.server`, and an end-to-end test of the command, all offline; plus the code review record for the milestone. | No | |
| 7 | Switch to the 100 Days of Python endpoint | Change the endpoint constant to `https://app.100daysofpython.dev/v1/nutrition/natural/exercise` (the keys of the course belong to that service, not to Nutritionix), reject a query of more than 50 characters, read the nested `error.message` of an error answer, and update the tests and documents. | No | |

---

[BC-001]: ../business-case.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474
[fdf51d6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/fdf51d6cd3c01862929c5c696d42b04800f3affb
