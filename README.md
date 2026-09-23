# Stopki mailowe zespołu Klastra

Jedna stopka dla wszystkich, w kolorach ze strony klaster.org.pl: logo na żółtym kafelku, dane osoby, adres biura w Gliwicach, linki do socjali fundacji.

## Zrób swoją stopkę
1. `python generuj.py --imie "Anna Nowak" --stanowisko "Koordynatorka projektów" --telefon "+48 732 259 513" --email anna.nowak@klaster.org.pl`
   Opcjonalnie `--stanowisko-en "Project Coordinator"` (dopisze angielską nazwę po kropce) i `--dzial "Śląskie Centrum Kariery Migrantów"` (druga linia pod nazwą fundacji).
2. Otwórz powstały `stopka-anna.html` w przeglądarce, zaznacz wszystko (Ctrl+A) i skopiuj (Ctrl+C).
3. Gmail: koło zębate, Zobacz wszystkie ustawienia, zakładka Ogólne, sekcja Podpis, Utwórz nowy, wklej (Ctrl+V). Niżej ustaw ten podpis jako domyślny dla nowych wiadomości i odpowiedzi. Na dole strony Zapisz zmiany.

Pliki `stopka-*.html` zostają na Twoim komputerze, repo ich nie przyjmuje (`.gitignore`), bo zawierają dane kontaktowe.

## Co tu jest
- `szablon.html`: szablon z polami `{{...}}`.
- `generuj.py`: wypełnia szablon.
- `img/logo-kafelek.png`: logo na żółtym kafelku, 300x280 px, w stopce wyświetlane 150x140 (ostre na ekranach retina). Adres publiczny: https://klaster1234.github.io/stopki/img/logo-kafelek.png
- `img/logo-czarne.png`: czarne logo bez tła, 800 px.

Kolory: żółty `#ffc342`, granat `#0f2040`, fiolet `#7c3aed`, szary tekstu `#5b6474`.
