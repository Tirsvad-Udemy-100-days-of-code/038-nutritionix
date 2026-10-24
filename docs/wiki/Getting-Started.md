**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Requirements

- Python 3.13 or later.
- No runtime dependency.
- To send real requests: an application id and API key for the natural language exercise endpoint of the course service (`https://app.100daysofpython.dev/v1/nutrition/natural/exercise`), and a Google Sheet named `workouts` with the columns Date, Time, Exercise, Duration and Calories, published through a Sheety endpoint.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

## Create and use a local .venv

Clone the repository, then create the virtual environment in its root, upgrade `pip` and install the project with its development tools.

Linux and macOS:

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

Leave the environment with `deactivate`. The folder `.venv` is ignored by git.

## Set the environment variables

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

PowerShell:

```powershell
$env:APP_ID = "your-app-id"
$env:API_KEY = "your-api-key"
$env:SHEET_ENDPOINT = "https://api.sheety.co/<id>/<project>/workouts"
$env:TOKEN = "your-sheety-bearer-token"
```

Keep your own keys in a personal `.env` file that git ignores, and load it into the shell yourself (in bash: `set -a; source .env; set +a`). The project never reads it. On Windows the system already sets `USERNAME`; it is used only when `PASSWORD` is set and `TOKEN` is not.

## First run

Try the dry run first. It sends nothing:

```bash
python -m exercise_tracker --dry-run log "ran 5k"
```

If the output shows the Nutritionix request, the Sheety request and hidden secrets (`********`), everything is in place. Continue with [Usage](Usage).

![The exercises command in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/exercises-dry-run.png)
