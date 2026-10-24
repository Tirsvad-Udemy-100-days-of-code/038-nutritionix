# 🚀 Exercise Tracker

A small Python project that turns a plain English sentence such as "ran 5k" into rows of a Google Sheet. [Nutritionix][nutritionix-docs] finds the exercise, its duration and the calories, and [Sheety][sheety-docs] writes one row per exercise. It is the Day 38 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants who want readable, runnable code and for visitors who want an idea.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The project follows the steps of the assignment:

1. send the sentence to the Nutritionix natural language exercise endpoint (`get_exercises`),
2. post one row per exercise to the Sheety endpoint, with the current date and time and the exercise name in title case (`add_workout_row`),
3. authenticate the Sheety request with a bearer token or with basic authentication,
4. read every key, token and endpoint from environment variables.

| Part | What it is for |
| --- | --- |
| `src/exercise_tracker/` | The package. `constants.py` holds every constant; the layers `domain`, `application`, `infrastructure` and `presentation` follow Clean Architecture |
| `tests/` | The pytest tests; none of them reaches an external host |
| `docs/` | The plan, the reviews, the screenshots (`docs/images/`) and the wiki sources (`docs/wiki/`, in English, Danish and Bahasa Malaysia) |
| `pyproject.toml` | Project configuration: pytest, ruff, mypy |
| `Doxyfile` | Configuration of the Doxygen source documentation |

No key, token or endpoint is in the source. They are read from the process environment; the project does not read a `.env` file.

## 📋 Requirements

- Python 3.13 or later, to run the code and the tests.
- No runtime dependency: HTTP calls use the standard library (decision [ADR-0001][ADR-0001]).
- `pytest`, `pytest-cov`, `ruff`, `mypy` and `pyyaml` for development; they are installed with the `dev` extra.
- A free [Nutritionix][nutritionix-docs] application id and API key, and a Google Sheet with a [Sheety][sheety-docs] endpoint, to send real requests. The sheet is named `workouts` and has the columns Date, Time, Exercise, Duration and Calories, so that Sheety expects the row inside `workout`.
- [Doxygen][doxygen] 1.9 or later, only if you want to build the source documentation.

## 🛠️ Setup

Create and use a local virtual environment named `.venv`, then upgrade `pip` and install the project with its development tools.

On Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The folder `.venv` is ignored by git.

Put your keys in the environment of your shell. Never write them in a file that you commit.

| Variable | Meaning |
| --- | --- |
| `APP_ID` | Nutritionix application id |
| `API_KEY` | Nutritionix API key |
| `SHEET_ENDPOINT` | Sheety endpoint of the sheet, for example `https://api.sheety.co/<id>/<project>/workouts` |
| `TOKEN` | Sheety bearer token (used when set) |
| `USERNAME`, `PASSWORD` | Sheety basic authentication (used when `TOKEN` is not set) |

```bash
export APP_ID="your-app-id"
export API_KEY="your-api-key"
export SHEET_ENDPOINT="https://api.sheety.co/<id>/<project>/workouts"
export TOKEN="your-sheety-bearer-token"
```

In PowerShell use `$env:APP_ID = "your-app-id"` and so on. Keep your own keys in a personal `.env` file that git ignores, and load it into the shell yourself, for example `set -a; source .env; set +a` in bash. Beware that on Windows the system already sets `USERNAME`; it is only used when `PASSWORD` is set too and `TOKEN` is not.

## ▶️ Run

Give one kind of exercise per query, as the assignment advises: "ran 5k" and "cycled for 20 minutes" are two queries, and so two sets of rows. Add `--dry-run` before the command name to print the requests, with the secrets hidden, and send nothing. Remove it to send the requests.

| Step of the assignment | Command | Python function |
| --- | --- | --- |
| 1. Ask Nutritionix and add a row per exercise to the sheet | `python -m exercise_tracker log "ran 5k"` | `get_exercises`, `add_workout_row` |
| Try it without sending anything | `python -m exercise_tracker --dry-run log "ran 5k"` | |

The installed program is also available as `exercise-tracker`. The date is `dd/mm/YYYY` and the time `HH:MM:SS`, both from the clock of your computer.

## 🧪 Tests

With the virtual environment active:

```bash
python -m pytest
```

Add `--cov` for the coverage report. The quality checks that the pull requests run are:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy --strict src tests
```

Build the source documentation with `doxygen Doxyfile`; the result is in `doxygen/html/index.html`.

## 📄 License

GNU Affero General Public License, version 3. See [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]
- [Nutritionix API documentation][nutritionix-docs]
- [Sheety documentation][sheety-docs]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Decisions][adr] | Why there is no runtime dependency and why there are no use cases |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

### CI secrets

The workflows in `.gitea/workflows/` call the shared workflows of `TirSystem/github-action`. The quality checks and the English comments check need no secret. The wiki publishing (`publish-wiki.yml`) needs the secret `TOKEN_FOR_GITEA_WIKI` in the organisation of the repository: a Gitea token with the scope `write:repository` for a user who can write this repository. Enable the wiki in the repository settings.

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/issues
[nutritionix-docs]: https://docx.syndigo.com/developers/docs/natural-language-for-exercise
[sheety-docs]: https://sheety.co/docs
[doxygen]: https://www.doxygen.nl/
[license]: ./LICENSE
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[adr]: ./docs/adr/
[ADR-0001]: ./docs/adr/adr-0001-urllib-no-runtime-dependency.md
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
