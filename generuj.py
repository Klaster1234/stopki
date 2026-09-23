"""Generuje stopkę mailową z szablonu. Wynik: stopka-<imie>.html (plik lokalny, nie trafia do repo).

python generuj.py --imie "Anna Nowak" --stanowisko "Koordynatorka projektów" --telefon "+48 732 259 513" --email anna.nowak@klaster.org.pl
Opcjonalnie: --dzial "Śląskie Centrum Kariery Migrantów" (druga linia pod nazwą fundacji), --stanowisko-en "Project Coordinator".
"""
import argparse, io, re, unicodedata
LOGO_URL = "https://klaster1234.github.io/stopki/img/logo-kafelek.png"
p = argparse.ArgumentParser()
for a in ("imie", "stanowisko", "telefon", "email"): p.add_argument("--" + a, required=True)
p.add_argument("--stanowisko-en", default=""); p.add_argument("--dzial", default=""); p.add_argument("--logo", default=LOGO_URL)
a = p.parse_args()
stan = a.stanowisko + (" &nbsp;·&nbsp; " + a.stanowisko_en if a.stanowisko_en else "")
dzial = ('      <div style="font-size:13px;color:#5b6474;line-height:18px;">%s</div>' % a.dzial) if a.dzial else ""
html = io.open("szablon.html", encoding="utf8").read()
for k, v in {"{{IMIE_NAZWISKO}}": a.imie, "{{STANOWISKO}}": stan, "{{DZIAL_DIV}}": dzial, "{{TELEFON}}": a.telefon,
             "{{TELEFON_TEL}}": re.sub(r"[^\d+]", "", a.telefon), "{{EMAIL}}": a.email, "{{LOGO_URL}}": a.logo}.items():
    html = html.replace(k, v)
slug = unicodedata.normalize("NFKD", a.imie.split()[0]).encode("ascii", "ignore").decode().lower()
out = "stopka-%s.html" % slug
io.open(out, "w", encoding="utf8").write(html); print("zapisano", out)
