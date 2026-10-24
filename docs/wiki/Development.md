**English** · [Dansk](Development-da) · [Bahasa Malaysia](Development-ms)

# Development

## Tests and checks

With the `.venv` active:

```bash
python -m pytest -q --cov
python -m ruff check .
python -m ruff format --check .
python -m mypy --strict src tests
doxygen Doxyfile
```

The tests never reach an external host and never use a real key. The integration and end-to-end tests start a small HTTP server on `127.0.0.1` and send real requests to it.

![The test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/tests.png)

## Source documentation

The source uses Doxygen commands (`@file`, `@brief`, `@param`, `@return`, `@throws`) in docstrings. `doxygen Doxyfile` writes the HTML to `doxygen/html/` (ignored by git).

## Workflows

The files in `.gitea/workflows/` call the shared workflows of `TirSystem/github-action`:

| Workflow | When | What it does |
| --- | --- | --- |
| `ci.yml` | pull request, push to `main` | ruff and mypy (shared), pytest with coverage, code metrics badges on `main` |
| `english-comments.yml` | pull request | fails when a new comment is not English |
| `publish-wiki.yml` | push to `main` that changes `docs/wiki/` | publishes these pages to the wiki; needs the secret `TOKEN_FOR_GITEA_WIKI` |

## Working method

Work is planned in milestones (`docs/milestones/`), one branch and one pull request per milestone, and every pull request closes the issues of its tasks. The wiki pages exist in English, Danish (`-da`) and Bahasa Malaysia (`-ms`); English is the authoritative text.
