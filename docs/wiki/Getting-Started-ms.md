[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

## Keperluan

- Python 3.13 atau lebih baharu.
- Tiada kebergantungan runtime.
- Untuk menghantar permintaan sebenar: id aplikasi Nutritionix percuma dan kunci API, serta Google Sheet bernama `workouts` dengan lajur Date, Time, Exercise, Duration dan Calories, diterbitkan melalui endpoint Sheety.
- Pilihan: [Doxygen](https://www.doxygen.nl/) untuk membina dokumentasi kod sumber.

## Cipta dan guna .venv setempat

Klon repositori, cipta persekitaran maya di akarnya, naik taraf `pip` dan pasang projek bersama alat pembangunan.

Linux dan macOS:

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

Keluar daripada persekitaran dengan `deactivate`. Folder `.venv` diabaikan oleh git.

## Tetapkan pemboleh ubah persekitaran

| Pemboleh ubah | Maksud |
| --- | --- |
| `APP_ID` | Id aplikasi Nutritionix |
| `API_KEY` | Kunci API Nutritionix |
| `SHEET_ENDPOINT` | Endpoint Sheety bagi helaian, contohnya `https://api.sheety.co/<id>/<project>/workouts` |
| `TOKEN` | Token bearer Sheety (digunakan jika ditetapkan) |
| `USERNAME`, `PASSWORD` | Basic authentication Sheety (digunakan jika `TOKEN` tidak ditetapkan) |

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

Simpan kunci anda sendiri dalam fail `.env` peribadi yang diabaikan oleh git, dan muatkannya ke dalam shell sendiri (dalam bash: `set -a; source .env; set +a`). Projek tidak pernah membacanya. Pada Windows, sistem sudah menetapkan `USERNAME`; ia hanya digunakan apabila `PASSWORD` ditetapkan dan `TOKEN` tidak.

## Larian pertama

Cuba dry run dahulu. Ia tidak menghantar apa-apa:

```bash
python -m exercise_tracker --dry-run log "ran 5k"
```

Jika output menunjukkan permintaan Nutritionix, permintaan Sheety dan rahsia yang disembunyikan (`********`), semuanya sudah sedia. Teruskan dengan [Penggunaan](Usage-ms).

![Arahan exercises dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/exercises-dry-run.png)
