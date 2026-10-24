**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Exercise Tracker

A small Python project that turns a plain English sentence such as "ran 5k" into rows of a Google Sheet. [Nutritionix](https://docx.syndigo.com/developers/docs/natural-language-for-exercise) finds the exercise, its duration and the calories, and [Sheety](https://sheety.co/docs) writes one row per exercise. It is the Day 38 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants who want readable, runnable code and for visitors who want an idea.

The project follows the steps of the assignment:

1. **Ask Nutritionix** with `get_exercises` (a POST with the `x-app-id` and `x-app-key` headers).
2. **Add a row per exercise** with `add_workout_row` (a camelCase `workout` body with date, time, exercise in title case, duration and calories).
3. **Authenticate Sheety** with a bearer token or with basic authentication.
4. **Keep secrets out of the code**: every key, token and endpoint is an environment variable.

![The log command in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

## Pages

- [Getting started](Getting-Started): requirements, the `.venv`, the environment variables.
- [Usage](Usage): the commands, the exit codes and the Python functions.
- [Architecture](Architecture): the layers and the decisions behind them.
- [Development](Development): tests, quality checks, Doxygen and the workflows.

## Good to know

- Your keys and tokens are never in the source. They are read from the environment, and the project does not read a `.env` file.
- `--dry-run` prints the requests with the secrets hidden and sends nothing.
- There is no runtime dependency: HTTP calls use the Python standard library.
- The repository is at https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix.
