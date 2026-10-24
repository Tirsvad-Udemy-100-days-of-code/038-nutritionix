[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Krav

- Python 3.13 eller nyere.
- Ingen runtime-afhængighed.
- For at sende rigtige kald: et applikations-id og en API-nøgle til kursets endpoint for naturligt sprog og øvelser (`https://app.100daysofpython.dev/v1/nutrition/natural/exercise`) samt et Google Sheet med navnet `workouts` og kolonnerne Date, Time, Exercise, Duration og Calories, udgivet gennem et Sheety-endpoint.
- Valgfrit: [Doxygen](https://www.doxygen.nl/) til at bygge kildedokumentationen.

## Opret og brug et lokalt .venv

Klon repositoriet, opret det virtuelle miljø i roden, opgradér `pip` og installér projektet med udviklingsværktøjerne.

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Forlad miljøet med `deactivate`. Mappen `.venv` ignoreres af git.

## Sæt miljøvariablerne

| Variabel | Betydning |
| --- | --- |
| `APP_ID` | Nutritionix-applikations-id |
| `API_KEY` | Nutritionix API-nøgle |
| `SHEET_ENDPOINT` | Sheety-endpoint for arket, fx `https://api.sheety.co/<id>/<project>/workouts` |
| `TOKEN` | Sheety bearer-token (bruges, når den er sat) |
| `USERNAME`, `PASSWORD` | Sheety basic authentication (bruges, når `TOKEN` ikke er sat) |

```bash
export APP_ID="your-app-id"
export API_KEY="your-api-key"
export SHEET_ENDPOINT="https://api.sheety.co/<id>/<project>/workouts"
export TOKEN="your-sheety-bearer-token"
```

PowerShell:

```powershell
$env:APP_ID = "your-app-id"
$env:API_KEY = "your-api-key"
$env:SHEET_ENDPOINT = "https://api.sheety.co/<id>/<project>/workouts"
$env:TOKEN = "your-sheety-bearer-token"
```

Gem dine egne nøgler i en personlig `.env`-fil, som git ignorerer, og læs den ind i din shell selv (i bash: `set -a; source .env; set +a`). Projektet læser den aldrig. På Windows sætter systemet allerede `USERNAME`; den bruges kun, når `PASSWORD` er sat, og `TOKEN` ikke er.

## Første kørsel

Prøv først dry run. Den sender ingenting:

```bash
python -m exercise_tracker --dry-run log "ran 5k"
```

Hvis udskriften viser Nutritionix-kaldet, Sheety-kaldet og skjulte hemmeligheder (`********`), er alt klar. Fortsæt med [Brug](Usage-da).

![Kommandoen exercises i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/exercises-dry-run.png)
