[English](Development) · **Dansk** · [Bahasa Malaysia](Development-ms)

# Udvikling

## Test og tjek

Med `.venv` aktivt:

```bash
python -m pytest -q --cov
python -m ruff check .
python -m ruff format --check .
python -m mypy --strict src tests
doxygen Doxyfile
```

Testene når aldrig en ekstern vært og bruger aldrig en rigtig nøgle. Integrations- og end-to-end-testene starter en lille HTTP-server på `127.0.0.1` og sender rigtige kald til den.

![Testkørslen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/tests.png)

## Kildedokumentation

Kilden bruger Doxygen-kommandoer (`@file`, `@brief`, `@param`, `@return`, `@throws`) i docstrings. `doxygen Doxyfile` skriver HTML til `doxygen/html/` (ignoreret af git).

## Workflows

Filerne i `.gitea/workflows/` kalder de fælles workflows fra `TirSystem/github-action`:

| Workflow | Hvornår | Hvad det gør |
| --- | --- | --- |
| `ci.yml` | pull request, push til `main` | ruff og mypy (fælles), pytest med dækning, kodemetrik-badges på `main` |
| `english-comments.yml` | pull request | fejler, når en ny kommentar ikke er på engelsk |
| `publish-wiki.yml` | push til `main`, der ændrer `docs/wiki/` | udgiver disse sider til wikien; kræver hemmeligheden `TOKEN_FOR_GITEA_WIKI` |

## Arbejdsmetode

Arbejdet planlægges i milepæle (`docs/milestones/`), én branch og én pull request pr. milepæl, og hver pull request lukker issues for sine opgaver. Wiki-siderne findes på engelsk, dansk (`-da`) og bahasa malaysia (`-ms`); engelsk er den gældende tekst.
