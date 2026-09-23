# Stopki mailowe zespołu Klastra

Jedna stopka dla wszystkich: czarno-biała, po angielsku (nazwa fundacji po polsku, pod nią „Cluster of Social Innovations”), znak Klastra, dane osoby, adres biura w Gliwicach. Trzy style: A trzy linijki obok czarnego kafelka ze znakiem (domyślny), B wizytówka z kreską i adresem, C układ pionowy ze znakiem nad nazwiskiem.

## Zrób swoją stopkę
1. `python generuj.py --styl A --imie "Anna Nowak" --stanowisko "Project Coordinator" --email anna.nowak@klaster.org.pl`
   `--telefon "+48 ..."` doda numer (bez tej opcji stopka jest bez telefonu); `--styl` A, B albo C; `--dzial "Silesian Migrant Career Centre"` dopisze szarą linię pod nazwą fundacji; `--czcionka georgia` (domyślna), `segoe` albo `times`.
2. Otwórz powstały `stopka-anna.html` w przeglądarce, zaznacz wszystko (Ctrl+A) i skopiuj (Ctrl+C).
3. Gmail: koło zębate, Zobacz wszystkie ustawienia, zakładka Ogólne, sekcja Podpis, Utwórz nowy, wklej (Ctrl+V). Niżej ustaw ten podpis jako domyślny dla nowych wiadomości i odpowiedzi. Na dole strony Zapisz zmiany.

Pliki `stopka-*.html` zostają na Twoim komputerze, repo ich nie przyjmuje (`.gitignore`), bo zawierają dane kontaktowe.

## Co tu jest
- `szablon-A.html`, `szablon-B.html`, `szablon-C.html`: szablony z polami `{{...}}`.
- `generuj.py`: wypełnia szablon.
- `img/znak.png`: znak Klastra (kółko z sześcianem), 400 px. `img/znak-kafelek-czarny.png`: biały znak na czarnym kafelku, 300 px.
- `img/logo-en.png`, `img/logo-pl.png`: pełne logo, 800 px szerokości, do innych zastosowań.
- Adresy publiczne obrazków: `https://klaster1234.github.io/stopki/img/<plik>` (GitHub Pages).

Kolory: czerń `#111111`, szary tekstu `#6f6f6f`, szare kropki `#bdbdbd`. Czcionka: Georgia (systemowa, jest na Windowsie, Macu i w telefonach), opcjonalnie Segoe UI albo Times New Roman.
