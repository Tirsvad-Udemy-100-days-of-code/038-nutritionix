# RC-014: MIL-004 Python code review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-24 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked on the files of the milestone; the criterion is met. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked on the files of the milestone; the criterion is met. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` (ruff 0.6.9) report nothing. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict src tests` (mypy 1.11.2) reports no issue; every function and test is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling is needed; assertions carry messages. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked on the files of the milestone; the criterion is met. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are read with `Path.read_text`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked on the files of the milestone; the criterion is met. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging`/injected streams only; no `print`; no secret in a message, repr or log (checked by tests). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists (ADR-0002); the classes trace to the tasks of MIL-004. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | test_wiki.py adds 58 offline tests: same page set in three languages, language line, sidebar links, existing images, identical code blocks. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` clean; no `Any` is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependency (ADR-0001); the dev tools are pinned in `pyproject.toml`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The expected language line is built once in a helper. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The test imports no project layer. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One module, one concern, small helpers. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | The test reads documents, not a layer; it sits in tests/unit. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are lower snake_case English without spaces. |

## Overall Verdict

Go — All Mandatory criteria of QC-PY-001 pass or are not applicable.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-004]: ../../milestones/mil-004-docs-and-wiki.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
