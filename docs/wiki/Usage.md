**English** · [Dansk](Usage-da) · [Bahasa Malaysia](Usage-ms)

# Usage

Put `--dry-run` before the command name to see the requests without sending them. Give one kind of exercise per sentence, at most 50 characters, as the assignment advises: "ran 5k" and "cycled for 20 minutes" are two sentences, and so two commands.

## The commands

```bash
python -m exercise_tracker exercises "ran 5k"
python -m exercise_tracker log "ran 5k"
python -m exercise_tracker --dry-run log "cycled for 20 minutes"
```

| Command | Needs | What it does |
| --- | --- | --- |
| `exercises "<sentence>"` | `APP_ID`, `API_KEY` | Asks Nutritionix and prints each exercise with its duration and calories; the sheet is not touched |
| `log "<sentence>"` | `APP_ID`, `API_KEY`, `SHEET_ENDPOINT`, `TOKEN` (or `USERNAME` and `PASSWORD`) | Asks Nutritionix, then posts one row per exercise to the sheet with the current date (`dd/mm/YYYY`) and time (`HH:MM:SS`) |

Each row sent to Sheety looks like this (the keys are camelCase and the exercise name is in title case):

```json
{
  "workout": {
    "date": "24/10/2026",
    "time": "21:56:23",
    "exercise": "Running",
    "duration": 30.0,
    "calories": 300.0
  }
}
```

![The log command in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

In dry-run mode the answer of Nutritionix is a built-in sample (one running exercise), so you can see both requests without an account.

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Every request was accepted (or the dry run finished) |
| 1 | An API refused the request or answered with something that cannot be understood |
| 2 | Invalid input or a missing environment variable; nothing was sent |
| 3 | An API could not be reached |

## From Python

The functions of the assignment take a gateway and the data. This example prints the requests instead of sending them:

```python
import sys

from exercise_tracker import log_workout
from exercise_tracker.domain.value_objects.exercise_query import ExerciseQuery
from exercise_tracker.domain.value_objects.nutritionix_credentials import NutritionixCredentials
from exercise_tracker.domain.value_objects.sheet_authorization import SheetAuthorization
from exercise_tracker.domain.value_objects.sheet_endpoint import SheetEndpoint
from exercise_tracker.infrastructure.clock.system_clock import SystemClock
from exercise_tracker.infrastructure.http.dry_run_http_gateway import DryRunHttpGateway

rows = log_workout(
    DryRunHttpGateway(sys.stdout),  # UrllibHttpGateway() sends for real
    NutritionixCredentials("your-app-id", "your-api-key"),
    SheetEndpoint("https://api.sheety.co/<id>/<project>/workouts"),
    SheetAuthorization.bearer("your-sheety-bearer-token"),
    SystemClock(),
    ExerciseQuery("ran 5k"),
)
```

`get_exercises` and `add_workout_row` can be called one by one. A refusal by an API raises `ApiError`, an unreachable server raises `GatewayUnreachableError`, and a value that breaks a rule raises `InvalidInputError` before any request.
