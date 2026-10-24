# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b64ad78] |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Scope names the 100 Days of Python endpoint of the course instead of the Nutritionix host, and the 50-character query limit | pending |

---

## Executive Summary

The Exercise Tracker is a small Python project built as the Day 38 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". The user types what they did in plain English, such as "ran 5k". The program asks the Nutritionix natural language API (application programming interface) for the exercise, its duration and its calories, and writes one row per exercise to a Google Sheet through the Sheety API, with the current date and time. The project gives course participants readable, runnable code with the assignment's steps and gives visitors to the GitHub repository a clear example with a good description, topics and README. We recommend building it as a repository with a plan, tests, source documentation and a three-language wiki.

## Methodological and Standards Foundation

The project follows the SQA (software quality assurance) and QC (quality control) framework mounted at `framework/`: a Business Case, a Stakeholder Analysis, a Project Plan and milestones come before code, and every step is reviewed against a QC checklist. Quality is judged against ISO/IEC (International Organization for Standardization and International Electrotechnical Commission) 25010:2023. The code follows Clean Architecture (Domain, Application, Infrastructure, Presentation) and the Python conventions of the `coding-conventions` skill (PEP 8 (Python Enhancement Proposal), PEP 257, PEP 484, `ruff`, `mypy --strict`).

## Problem Statement

Tracking workouts on paper is slow, and the calories burned are guessed. The lectures of the assignment show the solution only on screen, step by step, as a loose script that holds the API keys and the bearer token in plain text, with no tests, no instructions to run it and no documentation. A participant who wants to compare solutions, and a visitor who wants an idea, find little they can run and read at once.

## Business Opportunity

A tidy repository turns the lecture code into a reference that others can run in minutes. It also shows a way to keep secrets out of the code, to test HTTP calls without the network and to document a small project in three languages.

## Objectives

1. Turn a plain English sentence into exercises, durations and calories with the Nutritionix natural language exercise endpoint.
2. Append one row per exercise (date, time, exercise in title case, duration, calories) to the Google Sheet through the Sheety endpoint, with the date and time from Python's `datetime`.
3. Authenticate the Sheety requests with a bearer token (or basic authentication) and read every key, endpoint and secret from the process environment, never from the source.
4. Verify the behaviour with automated pytest tests that never use the network.
5. Document how to create and use a local `.venv` and how to run the project and its tests.
6. Document the source with Doxygen comments and provide a `Doxyfile`.
7. Publish a README and a wiki in English, Danish and Bahasa Malaysia with screenshots.
8. Describe the repository on the git host with a description and topics, and run the shared quality workflows of `TirSystem/github-action`.

## Scope

### In Scope

- Python 3.13 or later, a local `.venv`, `pyproject.toml`, a Python `.gitignore` and pytest.
- A query to the natural language exercise endpoint of the course service (`POST https://app.100daysofpython.dev/v1/nutrition/natural/exercise` with the `x-app-id` and `x-app-key` headers, a query of at most 50 characters) and the parsing of its exercises. The answer has the shape of the Nutritionix API.
- One Sheety `POST` per exercise with a camelCase `workout` body, `Authorization: Bearer <token>` or basic authentication.
- A command line to run the program with a dry run that prints the requests (secrets hidden) and sends nothing.
- A `constants.py` for constants, Doxygen comments in the source and a `Doxyfile`.
- The README from the framework template, a wiki in English, Danish and Bahasa Malaysia, and screenshots for both.
- The shared workflows from `TirSystem/github-action` that suit a Python project, the repository description and topics, one pull request per milestone.

### Out of Scope

- Reading, editing or deleting rows in the sheet (only creating rows is part of the assignment).
- Splitting a sentence with two kinds of exercise into separate queries: the user enters one exercise per query, as the assignment advises.
- Reading a `.env` file in the project: the file is personal to the author and is not imported, tested or committed.
- Graphical user interface, a database, packaging for PyPI and any other fitness or sheet service.
- Tests against the live Nutritionix or Sheety services.

## Expected Benefits

### Tangible Benefits

- A runnable project that a participant starts with a few commands from the README.
- A passing pytest suite that runs offline.
- Generated API documentation (Doxygen) and a wiki in three languages.

### Intangible Benefits

- A clear example of secret handling and of layered code for beginners.
- A reference that participants can compare with their own solutions.
- A tidy portfolio repository for the author.

## Strategic Alignment

The project supports the author's goal of finishing the 100 Days of Code course with work that is reviewable and reusable, and the goal of the TirSystem repositories to follow one framework with shared automation.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The assignment's steps exist | A function queries Nutritionix and a function adds a Sheety row; both are importable | A pytest test imports each function |
| 2 | Tests pass offline | 100 % of tests pass, 0 requests to an external host | `python -m pytest` on a machine without internet access |
| 3 | Code is covered by tests | At least 90 % line coverage of `src/` | `pytest --cov` report |
| 4 | No secret is in the repository | 0 keys, tokens or endpoints in tracked files | Search of the tracked files and the `.gitignore` check |
| 5 | A newcomer can run the project | README steps work on a clean clone without changes | Follow the README on a fresh `.venv` |
| 6 | Wiki is complete | 3 languages, the same page set | File list of `docs/wiki/` |
| 7 | Lint and types are clean | 0 `ruff` findings, 0 `mypy --strict` errors | The quality workflow or the local commands |
| 8 | Repository is described | Description and at least 5 topics set | Gitea repository settings |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The author's keys or token reach the repository | A secret is public | `.env` is ignored by git, the project never reads it, credentials are read from the process environment and tests use fake values |
| The Nutritionix or Sheety API changes | Examples stop working | Constants hold the endpoints and field names, tests use a fake HTTP gateway, the wiki names the API documentation |
| The Sheety endpoint is not known to the project | The log step cannot be tried live | The endpoint is an environment variable, the dry run needs no network, and the README says how to create the sheet and the endpoint |
| Translations drift from English | Readers in Danish or Bahasa Malaysia get old text | Same page set in each language, English is authoritative, wiki pages are reviewed with the change |
| The shared workflows need secrets and a runner that the repository may not have | Continuous integration (CI) stays red or does not run | The workflows are installed from the shared repository and the needed secrets are listed in the README |
| The standard library HTTP client is less readable than `requests` for a beginner | S02 finds the code harder to compare with the lecture | The HTTP code is confined to one small adapter and ADR-0001 (Architecture Decision Record) records the decision |

## Assumptions

- The author, S01, is Product Owner, developer and reviewer, and AI stands in for reviewers in autonomous mode.
- The repository `Tirsvad-Udemy-100-days-of-code/038-nutritionix` on git.tirsystem.com (the `origin` of this clone) is the repository of the project and the push target.
- The Nutritionix and Sheety APIs are reachable and stay compatible with the lectures.
- A runner is registered for the repository, or the workflows simply wait until one is.

## Constraints

- Python 3.13 or later and a `venv`; `pytest` for tests.
- The folders `src/`, `tests/` and `docs/`.
- `constants.py` holds the constants; Doxygen comments in the source; a `Doxyfile`.
- No runtime dependency: the standard library is enough (ADR-0001).
- One branch and one pull request per milestone, so the steps stay traceable.
- Keys and tokens come from the personal `.env`, which is not imported, not tested and not committed.

## Cost–Benefit Assessment

The assessment is qualitative: the project is a learning exercise with no revenue, and a money figure would not support the decision. The cost is the author's time and the benefit is shared knowledge.

| Costs | Benefits |
| --- | --- |
| About two days of the author's time, including reviews | A reviewed, reusable reference project |
| Maintenance of three wiki languages | A wider audience for participants who read Danish or Bahasa Malaysia |
| A hand-written HTTP adapter instead of `requests` | No runtime dependency for S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finishes the assignment with reviewable, reusable work |
| S02 | Gets readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | Gets a clear repository description, topics and a README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks are mitigated and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[b64ad78]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/commit/b64ad78da4e7a2bd6357aebc7435f940aabd3474
