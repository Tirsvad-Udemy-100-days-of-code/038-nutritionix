[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Exercise Tracker

Et lille Python-projekt, der gør en almindelig engelsk sætning som "ran 5k" til rækker i et Google Sheet. [Nutritionix](https://docx.syndigo.com/developers/docs/natural-language-for-exercise) finder øvelsen, varigheden og kalorierne, og [Sheety](https://sheety.co/docs) skriver én række pr. øvelse. Det er opgaven fra dag 38 på Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp", skrevet til kursister, der vil have læsbar kode, som kan køres, og til besøgende, der søger inspiration.

Projektet følger opgavens trin:

1. **Spørg Nutritionix** med `get_exercises` (et POST-kald med headerne `x-app-id` og `x-app-key`).
2. **Tilføj en række pr. øvelse** med `add_workout_row` (en `workout`-body i camelCase med dato, tid, øvelse med stort begyndelsesbogstav, varighed og kalorier).
3. **Godkend over for Sheety** med et bearer-token eller med basic authentication.
4. **Hold hemmeligheder ude af koden**: hver nøgle, token og endpoint er en miljøvariabel.

![Kommandoen log i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix/raw/branch/main/docs/images/log-dry-run.png)

## Sider

- [Kom i gang](Getting-Started-da): krav, `.venv`, miljøvariablerne.
- [Brug](Usage-da): kommandoerne, exitkoderne og Python-funktionerne.
- [Arkitektur](Architecture-da): lagene og beslutningerne bag dem.
- [Udvikling](Development-da): test, kvalitetstjek, Doxygen og workflows.

## Godt at vide

- Dine nøgler og tokens ligger aldrig i kilden. De læses fra miljøet, og projektet læser ingen `.env`-fil.
- `--dry-run` udskriver kaldene med hemmelighederne skjult og sender ingenting.
- Der er ingen runtime-afhængighed: HTTP-kald bruger Pythons standardbibliotek.
- Repositoriet ligger på https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/038-nutritionix.
