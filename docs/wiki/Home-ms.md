[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Exercise Tracker

Projek Python kecil yang menukar ayat Inggeris biasa seperti "ran 5k" kepada baris dalam Google Sheet. [Nutritionix](https://docx.syndigo.com/developers/docs/natural-language-for-exercise) mencari senaman, tempoh dan kalorinya, dan [Sheety](https://sheety.co/docs) menulis satu baris bagi setiap senaman. Ia ialah tugasan hari ke-38 kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp", ditulis untuk peserta kursus yang mahukan kod yang mudah dibaca dan boleh dijalankan, dan untuk pelawat yang mencari idea.

Projek ini mengikut langkah tugasan:

1. **Tanya Nutritionix** dengan `get_exercises` (permintaan POST dengan header `x-app-id` dan `x-app-key`).
2. **Tambah satu baris bagi setiap senaman** dengan `add_workout_row` (badan `workout` dalam camelCase dengan tarikh, masa, senaman dalam huruf besar pada awal perkataan, tempoh dan kalori).
3. **Sahkan diri kepada Sheety** dengan token bearer atau dengan basic authentication.
4. **Jauhkan rahsia daripada kod**: setiap kunci, token dan endpoint ialah pemboleh ubah persekitaran.

![Arahan log dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

## Halaman

- [Mula di sini](Getting-Started-ms): keperluan, `.venv`, pemboleh ubah persekitaran.
- [Penggunaan](Usage-ms): arahan, kod keluar dan fungsi Python.
- [Seni bina](Architecture-ms): lapisan dan keputusan di sebaliknya.
- [Pembangunan](Development-ms): ujian, semakan kualiti, Doxygen dan workflow.

## Perlu diketahui

- Kunci dan token anda tidak pernah berada dalam kod sumber. Ia dibaca daripada persekitaran, dan projek tidak membaca fail `.env`.
- `--dry-run` mencetak permintaan dengan rahsia disembunyikan dan tidak menghantar apa-apa.
- Tiada kebergantungan runtime: panggilan HTTP menggunakan pustaka standard Python.
- Repositori berada di https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix.
