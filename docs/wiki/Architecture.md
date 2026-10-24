**English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

# Architecture

The code follows Clean Architecture. Dependencies point inward: `presentation` knows `application` and `domain`; `infrastructure` knows `application` and `domain`; `domain` knows only `constants`.

```text
src/exercise_tracker/
  constants.py
  domain/            value_objects/ (Exercise, ExerciseQuery, WorkoutRow, credentials, ...), errors/
  application/       use_cases/ (get_exercises, add_workout_row, log_workout), ports/, dto/, errors/
  infrastructure/    http/ (urllib and dry-run gateways), config/ (environment), clock/
  presentation/      cli.py (composition root), commands/
tests/               unit/, integration/, e2e/
```

| Layer | Holds |
| --- | --- |
| `domain` | Value objects that enforce the rules (`Exercise`, `ExerciseQuery`, `WorkoutRow`, `SheetEndpoint`, `SheetAuthorization`, ...) and `InvalidInputError` |
| `application` | The use cases, the `HttpGateway` and `Clock` ports, `HttpResponse` and the errors `ApiError`, `GatewayUnreachableError` and `MalformedResponseError` |
| `infrastructure` | The adapters: `UrllibHttpGateway`, `DryRunHttpGateway`, `SystemClock` and the reading of the environment |
| `presentation` | The command line: one command per use case, and `cli.py`, the composition root that builds the adapters |

## Decisions

- **No runtime dependency** (ADR-0001). HTTP uses `urllib` from the standard library, only in the infrastructure layer and behind the `HttpGateway` port, so the other layers are tested with a fake gateway.
- **No use cases or design diagrams** (ADR-0002). The project is two POST requests; the Go/No-Go criteria of the milestones and the Doxygen comments describe the behaviour.
- **Secrets stay out of the code.** The credential value objects hide their text in `str` and `repr`, the dry run masks the secret headers, and no secret is placed in a URL.
- **The authentication is chosen in the configuration**, not in the use cases: a bearer token if `TOKEN` is set, otherwise basic authentication from `USERNAME` and `PASSWORD`.
- **Constants live in `constants.py`**, once.

The decisions and the plan are in `docs/` of the repository.
