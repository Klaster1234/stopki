"""Generuje stopkę mailową z szablonu (po angielsku, czarno-białą). Wynik: stopka-<imie>.html, plik lokalny, nie trafia do repo.

python generuj.py --imie "Anna Nowak" --stanowisko "Project Coordinator" --telefon "+48 732 259 513" --email anna.nowak@klaster.org.pl
Opcje: --logo znak (domyślnie, sam znak) | en (pełne logo angielskie) | pl (pełne logo polskie); --dzial "..." dopisze szarą linię pod nazwą fundacji.
"""
import argparse, io, re, unicodedata
BASE = "https://klaster1234.github.io/stopki/img/"
LOGA = {"znak": ("znak.png", 88, 88), "en": ("logo-en.png", 112, 102), "pl": ("logo-pl.png", 112, 106)}
p = argparse.ArgumentParser()
for a in ("imie", "stanowisko", "telefon", "email"): p.add_argument("--" + a, required=True)
p.add_argument("--logo", choices=LOGA, default="znak"); p.add_argument("--dzial", default="")
a = p.parse_args()
plik, w, h = LOGA[a.logo]
dzial = ('      <div style="font-size:12px;color:#6f6f6f;line-height:18px;">%s</div>' % a.dzial) if a.dzial else ""
html = io.open("szablon.html", encoding="utf8").read()
for k, v in {"{{IMIE_NAZWISKO}}": a.imie, "{{STANOWISKO}}": a.stanowisko.upper(), "{{DZIAL_DIV}}": dzial, "{{TELEFON}}": a.telefon,
             "{{TELEFON_TEL}}": re.sub(r"[^\d+]", "", a.telefon), "{{EMAIL}}": a.email,
             "{{LOGO_URL}}": BASE + plik, "{{LOGO_W}}": str(w), "{{LOGO_H}}": str(h)}.items():
    html = html.replace(k, v)
slug = unicodedata.normalize("NFKD", a.imie.split()[0]).encode("ascii", "ignore").decode().lower()
out = "stopka-%s.html" % slug
io.open(out, "w", encoding="utf8").write(html); print("zapisano", out)
