[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

# Seni bina

Kod mengikut Clean Architecture. Kebergantungan menghala ke dalam: `presentation` mengenali `application` dan `domain`; `infrastructure` mengenali `application` dan `domain`; `domain` hanya mengenali `constants`.

```text
src/exercise_tracker/
  constants.py
  domain/            value_objects/ (Exercise, ExerciseQuery, WorkoutRow, credentials, ...), errors/
  application/       use_cases/ (get_exercises, add_workout_row, log_workout), ports/, dto/, errors/
  infrastructure/    http/ (urllib and dry-run gateways), config/ (environment), clock/
  presentation/      cli.py (composition root), commands/
tests/               unit/, integration/, e2e/
```

| Lapisan | Mengandungi |
| --- | --- |
| `domain` | Objek nilai yang menguatkuasakan peraturan (`Exercise`, `ExerciseQuery`, `WorkoutRow`, `SheetEndpoint`, `SheetAuthorization`, ...) dan `InvalidInputError` |
| `application` | Kes guna, port `HttpGateway` dan `Clock`, `HttpResponse` dan ralat `ApiError`, `GatewayUnreachableError` dan `MalformedResponseError` |
| `infrastructure` | Penyesuai: `UrllibHttpGateway`, `DryRunHttpGateway`, `SystemClock` dan pembacaan persekitaran |
| `presentation` | Baris arahan: satu arahan bagi setiap kes guna, dan `cli.py`, composition root yang membina penyesuai |

## Keputusan

- **Tiada kebergantungan runtime** (ADR-0001). HTTP menggunakan `urllib` daripada pustaka standard, hanya dalam lapisan infrastruktur dan di sebalik port `HttpGateway`, jadi lapisan lain diuji dengan gateway palsu.
- **Tiada kes guna atau rajah reka bentuk** (ADR-0002). Projek ini hanya dua permintaan POST; kriteria Go/No-Go bagi pencapaian dan komen Doxygen menerangkan tingkah lakunya.
- **Rahsia dijauhkan daripada kod.** Objek nilai kelayakan menyembunyikan teksnya dalam `str` dan `repr`, dry run menutup header rahsia, dan tiada rahsia diletakkan dalam URL.
- **Pengesahan dipilih dalam konfigurasi**, bukan dalam kes guna: token bearer jika `TOKEN` ditetapkan, jika tidak basic authentication daripada `USERNAME` dan `PASSWORD`.
- **Pemalar berada dalam `constants.py`**, sekali sahaja.

Keputusan dan pelan berada dalam `docs/` repositori.
