[English](Development) · [Dansk](Development-da) · **Bahasa Malaysia**

# Pembangunan

## Ujian dan semakan

Dengan `.venv` aktif:

```bash
python -m pytest -q --cov
python -m ruff check .
python -m ruff format --check .
python -m mypy --strict src tests
doxygen Doxyfile
```

Ujian tidak pernah menghubungi hos luaran dan tidak pernah menggunakan kunci sebenar. Ujian integrasi dan hujung ke hujung memulakan pelayan HTTP kecil pada `127.0.0.1` dan menghantar permintaan sebenar kepadanya.

![Larian ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/tests.png)

## Dokumentasi kod sumber

Kod sumber menggunakan arahan Doxygen (`@file`, `@brief`, `@param`, `@return`, `@throws`) dalam docstring. `doxygen Doxyfile` menulis HTML ke `doxygen/html/` (diabaikan oleh git).

## Workflow

Fail dalam `.gitea/workflows/` memanggil workflow kongsi daripada `TirSystem/github-action`:

| Workflow | Bila | Fungsinya |
| --- | --- | --- |
| `ci.yml` | pull request, push ke `main` | ruff dan mypy (kongsi), pytest dengan liputan, lencana metrik kod pada `main` |
| `english-comments.yml` | pull request | gagal apabila komen baharu bukan dalam bahasa Inggeris |
| `publish-wiki.yml` | push ke `main` yang mengubah `docs/wiki/` | menerbitkan halaman ini ke wiki; memerlukan rahsia `TOKEN_FOR_GITEA_WIKI` |

## Kaedah kerja

Kerja dirancang dalam pencapaian (`docs/milestones/`), satu cabang dan satu pull request bagi setiap pencapaian, dan setiap pull request menutup isu bagi tugasnya. Halaman wiki wujud dalam bahasa Inggeris, Denmark (`-da`) dan Bahasa Malaysia (`-ms`); bahasa Inggeris ialah teks yang menjadi rujukan.
