# MIL-001: Project setup and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b64ad78] |

---

## Purpose

This gate decides whether the project has a working base on which the two assignment steps can be built: configuration, ignore rules, source documentation settings, run instructions and the shared automation. If the base is not sound, every later gate would build on sand.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, a `Doxyfile`, the `exercise_tracker` package with `constants.py`, a first README with the `.venv` instructions, the shared quality workflows installed, and a repository description with topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install -e ".[dev]"` succeeds in a fresh `.venv` on Python 3.13 or later | Succeeds | Fails |
| 2 | `python -m pytest` runs and passes | Passes | Fails or no test found |
| 3 | `ruff check`, `ruff format --check` and `mypy --strict src` report nothing | Clean | Any finding |
| 4 | `.gitignore` ignores `.venv/`, `.env`, `__pycache__/` and Doxygen output | All four ignored | Any one missing |
| 5 | The README states how to create and use `.venv` and the `python -m pip install --upgrade pip` command | Both present | Either missing |
| 6 | The workflow files for the shared quality checks are in `.gitea/workflows/` and parse as YAML | Present and valid | Missing or invalid |
| 7 | The repository has a description and at least 5 topics on the git host | Set | Not set |
| 8 | No `.env` file, key or token is in the commit | None | Any found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| Accepted [BC-001] and SA-001 | The plan-first gate: no code before the baseline is accepted |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5 (venv and run instructions) | Success criterion 5 of [BC-001] |
| Objective 6 (Doxygen) | Scope of [BC-001] |
| Objective 8 (description, topics, workflows) | Success criterion 8 of [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-25 — within the two-day effort of the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Configure the project for Python 3.13 or later with a `src` layout and no runtime dependency (ADR-0001, Architecture Decision Record), a `dev` extra with pytest, pytest-cov, ruff, mypy and pyyaml, and the tool settings for ruff, mypy and pytest so that all checks run from one file. | No | ADR-0001 |
| 2 | Add Python .gitignore | Ignore the virtual environment `.venv/`, byte code, caches, coverage output, build output, Doxygen output and the personal `.env`, so that no secret or generated file reaches the repository. | No | |
| 3 | Add package skeleton with constants.py | Create `src/exercise_tracker/` with `constants.py` for the Nutritionix and Sheety endpoints, header and field names, the environment variable names and the date and time formats, plus a first smoke test under `tests/unit/` so that pytest has something to run. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` for Python that reads `src/`, writes to a git-ignored `doxygen/` folder and extracts the `@brief`, `@param` and `@return` comments the source uses. | No | |
| 5 | Write first README with venv instructions | Use the framework README template and document how to create and use a local `.venv`, how to run `python -m pip install --upgrade pip`, how to set the environment variables, how to install the project and how to run the tests. | No | |
| 6 | Install shared quality workflows | Copy the quality checks with tests, the English comments check and the code metrics workflow that call `TirSystem/github-action`, pinned to `@v2`, and list the secrets they need in the README. | No | |
| 7 | Set repository description and topics | Set the description and the topics of the repository on git.tirsystem.com through its API (application programming interface), with the token read from the personal `.env` and never printed, so that S03 sees a clear repository page. | No | |

---

[BC-001]: ../business-case.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474
