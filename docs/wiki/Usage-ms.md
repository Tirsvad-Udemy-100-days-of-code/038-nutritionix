[English](Usage) · [Dansk](Usage-da) · **Bahasa Malaysia**

# Penggunaan

Letakkan `--dry-run` sebelum nama arahan untuk melihat permintaan tanpa menghantarnya. Beri satu jenis senaman bagi setiap ayat, seperti yang disarankan oleh tugasan: "ran 5k" dan "cycled for 20 minutes" ialah dua ayat, maka dua arahan.

## Arahan

```bash
python -m exercise_tracker exercises "ran 5k"
python -m exercise_tracker log "ran 5k"
python -m exercise_tracker --dry-run log "cycled for 20 minutes"
```

| Arahan | Memerlukan | Fungsinya |
| --- | --- | --- |
| `exercises "<ayat>"` | `APP_ID`, `API_KEY` | Bertanya kepada Nutritionix dan mencetak setiap senaman dengan tempoh dan kalorinya; helaian tidak disentuh |
| `log "<ayat>"` | `APP_ID`, `API_KEY`, `SHEET_ENDPOINT`, `TOKEN` (atau `USERNAME` dan `PASSWORD`) | Bertanya kepada Nutritionix, kemudian menghantar satu baris bagi setiap senaman ke helaian dengan tarikh semasa (`dd/mm/YYYY`) dan masa (`HH:MM:SS`) |

Setiap baris yang dihantar kepada Sheety kelihatan seperti ini (kuncinya camelCase dan nama senaman dalam huruf besar pada awal perkataan):

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

![Arahan log dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

Dalam mod dry-run, jawapan Nutritionix ialah sampel terbina dalam (satu senaman berlari), supaya anda dapat melihat kedua-dua permintaan tanpa akaun.

## Kod keluar

| Kod | Maksud |
| --- | --- |
| 0 | Semua permintaan diterima (atau dry run selesai) |
| 1 | Sebuah API menolak permintaan atau menjawab sesuatu yang tidak dapat difahami |
| 2 | Input tidak sah atau pemboleh ubah persekitaran tiada; tiada apa-apa dihantar |
| 3 | Sebuah API tidak dapat dihubungi |

## Daripada Python

Fungsi tugasan mengambil gateway dan data. Contoh ini mencetak permintaan dan tidak menghantarnya:

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

`get_exercises` dan `add_workout_row` boleh dipanggil satu demi satu. Penolakan oleh sebuah API menimbulkan `ApiError`, pelayan yang tidak dapat dihubungi menimbulkan `GatewayUnreachableError`, dan nilai yang melanggar peraturan menimbulkan `InvalidInputError` sebelum sebarang permintaan dihantar.
