[English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

# Arkitektur

Koden følger Clean Architecture. Afhængighederne peger indad: `presentation` kender `application` og `domain`; `infrastructure` kender `application` og `domain`; `domain` kender kun `constants`.

```text
src/exercise_tracker/
  constants.py
  domain/            value_objects/ (Exercise, ExerciseQuery, WorkoutRow, credentials, ...), errors/
  application/       use_cases/ (get_exercises, add_workout_row, log_workout), ports/, dto/, errors/
  infrastructure/    http/ (urllib and dry-run gateways), config/ (environment), clock/
  presentation/      cli.py (composition root), commands/
tests/               unit/, integration/, e2e/
```

| Lag | Indeholder |
| --- | --- |
| `domain` | Værdiobjekter, der håndhæver reglerne (`Exercise`, `ExerciseQuery`, `WorkoutRow`, `SheetEndpoint`, `SheetAuthorization`, ...) og `InvalidInputError` |
| `application` | Use cases, portene `HttpGateway` og `Clock`, `HttpResponse` og fejlene `ApiError`, `GatewayUnreachableError` og `MalformedResponseError` |
| `infrastructure` | Adapterne: `UrllibHttpGateway`, `DryRunHttpGateway`, `SystemClock` og læsning af miljøet |
| `presentation` | Kommandolinjen: én kommando pr. use case, og `cli.py`, composition root, der bygger adapterne |

## Beslutninger

- **Ingen runtime-afhængighed** (ADR-0001). HTTP bruger `urllib` fra standardbiblioteket, kun i infrastrukturlaget og bag porten `HttpGateway`, så de andre lag testes med en falsk gateway.
- **Ingen use cases eller designdiagrammer** (ADR-0002). Projektet er to POST-kald; milepælenes Go/No-Go-kriterier og Doxygen-kommentarerne beskriver adfærden.
- **Hemmeligheder holdes ude af koden.** Værdiobjekterne for legitimationsoplysninger skjuler deres tekst i `str` og `repr`, dry run maskerer de hemmelige headere, og ingen hemmelighed lægges i en URL.
- **Godkendelsen vælges i konfigurationen**, ikke i use cases: et bearer-token, hvis `TOKEN` er sat, ellers basic authentication fra `USERNAME` og `PASSWORD`.
- **Konstanter ligger i `constants.py`**, én gang.

Beslutningerne og planen ligger i `docs/` i repositoriet.
