[English](Usage) · **Dansk** · [Bahasa Malaysia](Usage-ms)

# Brug

Sæt `--dry-run` før kommandonavnet for at se kaldene uden at sende dem. Skriv én slags øvelse pr. sætning, som opgaven anbefaler: "ran 5k" og "cycled for 20 minutes" er to sætninger og dermed to kommandoer.

## Kommandoerne

```bash
python -m exercise_tracker exercises "ran 5k"
python -m exercise_tracker log "ran 5k"
python -m exercise_tracker --dry-run log "cycled for 20 minutes"
```

| Kommando | Kræver | Hvad den gør |
| --- | --- | --- |
| `exercises "<sætning>"` | `APP_ID`, `API_KEY` | Spørger Nutritionix og udskriver hver øvelse med varighed og kalorier; arket røres ikke |
| `log "<sætning>"` | `APP_ID`, `API_KEY`, `SHEET_ENDPOINT`, `TOKEN` (eller `USERNAME` og `PASSWORD`) | Spørger Nutritionix og sender derefter én række pr. øvelse til arket med dags dato (`dd/mm/YYYY`) og klokkeslæt (`HH:MM:SS`) |

Hver række, der sendes til Sheety, ser sådan ud (nøglerne er camelCase, og øvelsens navn har stort begyndelsesbogstav):

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

![Kommandoen log i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

I dry-run-tilstand er Nutritionix' svar et indbygget eksempel (én løbeøvelse), så du kan se begge kald uden en konto.

## Exitkoder

| Kode | Betydning |
| --- | --- |
| 0 | Alle kald blev accepteret (eller dry run blev gennemført) |
| 1 | Et API afviste kaldet eller svarede noget, der ikke kan forstås |
| 2 | Ugyldigt input eller en manglende miljøvariabel; intet blev sendt |
| 3 | Et API kunne ikke nås |

## Fra Python

Opgavens funktioner tager en gateway og data. Dette eksempel udskriver kaldene i stedet for at sende dem:

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

`get_exercises` og `add_workout_row` kan kaldes hver for sig. En afvisning fra et API udløser `ApiError`, en server, der ikke kan nås, udløser `GatewayUnreachableError`, og en værdi, der bryder en regel, udløser `InvalidInputError`, før noget kald sendes.
