# Stopki mailowe zespołu Klastra

Jedna stopka dla wszystkich: czarno-biała, po angielsku (nazwa fundacji po polsku, pod nią „Cluster of Social Innovations"), znak Klastra, cienka linia, dane osoby, adres biura w Gliwicach, linki do socjali fundacji.

## Zrób swoją stopkę
1. `python generuj.py --imie "Anna Nowak" --stanowisko "Project Coordinator" --telefon "+48 732 259 513" --email anna.nowak@klaster.org.pl`
   Opcje: `--logo en` (pełne logo angielskie zamiast znaku), `--logo pl` (pełne logo polskie), `--dzial "Silesian Migrant Career Centre"` (szara linia pod nazwą fundacji).
2. Otwórz powstały `stopka-anna.html` w przeglądarce, zaznacz wszystko (Ctrl+A) i skopiuj (Ctrl+C).
3. Gmail: koło zębate, Zobacz wszystkie ustawienia, zakładka Ogólne, sekcja Podpis, Utwórz nowy, wklej (Ctrl+V). Niżej ustaw ten podpis jako domyślny dla nowych wiadomości i odpowiedzi. Na dole strony Zapisz zmiany.

Pliki `stopka-*.html` zostają na Twoim komputerze, repo ich nie przyjmuje (`.gitignore`), bo zawierają dane kontaktowe.

## Co tu jest
- `szablon.html`: szablon z polami `{{...}}`.
- `generuj.py`: wypełnia szablon.
- `img/znak.png`: znak Klastra (kółko z sześcianem), 400 px, w stopce 88 px.
- `img/logo-en.png`, `img/logo-pl.png`: pełne logo, 800 px szerokości.
- Adresy publiczne obrazków: `https://klaster1234.github.io/stopki/img/<plik>` (GitHub Pages).

Kolory: czerń `#111111`, szary tekstu `#6f6f6f`, szare kropki `#bdbdbd`. Czcionka: Segoe UI, Helvetica, Arial.
