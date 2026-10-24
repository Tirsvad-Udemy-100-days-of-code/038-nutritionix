"""@file constants.py
@brief Constants of the Exercise Tracker: endpoints, field names and settings.

Every constant of the project is defined here, once.
"""

## @brief URL of the Nutritionix natural language exercise endpoint.
NUTRITIONIX_EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

## @brief Name of the HTTP header that carries the Nutritionix application id.
HEADER_APP_ID = "x-app-id"

## @brief Name of the HTTP header that carries the Nutritionix API key.
HEADER_APP_KEY = "x-app-key"

## @brief Name of the HTTP header that carries the Sheety authorization.
HEADER_AUTHORIZATION = "Authorization"

## @brief Name of the HTTP header that states the media type of the body.
HEADER_CONTENT_TYPE = "Content-Type"

## @brief Name of the HTTP header that names the client program.
HEADER_USER_AGENT = "User-Agent"

## @brief Value of the User-Agent header; the default of urllib is refused by the
#  Nutritionix firewall.
USER_AGENT = "exercise-tracker/0.1"

## @brief Media type of every request body.
CONTENT_TYPE_JSON = "application/json"

## @brief Prefix of the bearer authorization value.
BEARER_PREFIX = "Bearer"

## @brief Prefix of the basic authorization value.
BASIC_PREFIX = "Basic"

## @brief JSON field: the plain English sentence (Nutritionix request).
FIELD_QUERY = "query"

## @brief JSON field: the list of exercises (Nutritionix answer).
FIELD_EXERCISES = "exercises"

## @brief JSON field: the name of an exercise (Nutritionix answer).
FIELD_NAME = "name"

## @brief JSON field: the duration of an exercise in minutes (Nutritionix answer).
FIELD_DURATION_MIN = "duration_min"

## @brief JSON field: the calories of an exercise (Nutritionix answer).
FIELD_CALORIES_NF = "nf_calories"

## @brief JSON field: the row wrapper; Sheety names it after the sheet, singular.
FIELD_WORKOUT = "workout"

## @brief JSON field: the date column of the sheet.
FIELD_DATE = "date"

## @brief JSON field: the time column of the sheet.
FIELD_TIME = "time"

## @brief JSON field: the exercise column of the sheet.
FIELD_EXERCISE = "exercise"

## @brief JSON field: the duration column of the sheet.
FIELD_DURATION = "duration"

## @brief JSON field: the calories column of the sheet.
FIELD_CALORIES = "calories"

## @brief Name of the environment variable that holds the Nutritionix app id.
ENV_APP_ID = "APP_ID"

## @brief Name of the environment variable that holds the Nutritionix API key.
ENV_API_KEY = "API_KEY"

## @brief Name of the environment variable that holds the Sheety endpoint.
ENV_SHEET_ENDPOINT = "SHEET_ENDPOINT"

## @brief Name of the environment variable that holds the Sheety bearer token.
ENV_TOKEN = "TOKEN"

## @brief Name of the environment variable that holds the basic-auth username.
ENV_USERNAME = "USERNAME"

## @brief Name of the environment variable that holds the basic-auth password.
ENV_PASSWORD = "PASSWORD"

## @brief Format of the date column: day, month and four digit year.
DATE_FORMAT = "%d/%m/%Y"

## @brief Format of the time column: hours, minutes and seconds.
TIME_FORMAT = "%H:%M:%S"

## @brief Seconds to wait for an API before the request is given up.
REQUEST_TIMEOUT_SECONDS = 10

## @brief Text printed instead of a secret when a request is shown.
HIDDEN_SECRET = "********"

## @brief Name of the command line program.
PROGRAM_NAME = "exercise-tracker"

## @brief Exit code: every request was accepted.
EXIT_OK = 0

## @brief Exit code: an API answered and refused the request.
EXIT_REJECTED = 1

## @brief Exit code: the input or the configuration is invalid; nothing was sent.
EXIT_INVALID = 2

## @brief Exit code: an API could not be reached.
EXIT_UNREACHABLE = 3

## @brief HTTP method of every request of the program.
HTTP_METHOD_POST = "POST"

## @brief Lowest HTTP status code that is an error answer.
HTTP_ERROR_STATUS_MIN = 400

## @brief HTTP status code of a successful answer.
HTTP_STATUS_OK = 200

## @brief Header names whose values are secrets, in lower case.
SECRET_HEADER_NAMES = (HEADER_APP_ID.lower(), HEADER_APP_KEY.lower(), "authorization")

## @brief Longest API message, in characters, that an error carries.
MAX_API_MESSAGE_LENGTH = 200

## @brief JSON field: the human readable message of an API error answer.
FIELD_MESSAGE = "message"

## @brief DRY-RUN SAMPLE ONLY: the canned answer of the dry-run gateway.
#  This is not real Nutritionix data; it is returned when nothing is sent.
DRY_RUN_SAMPLE_BODY_JSON = (
    '{"exercises":[{"name":"running","duration_min":30.0,"nf_calories":300.0}]}'
)
