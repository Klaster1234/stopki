"""Generuje stopke mailowa (po angielsku, czarno-biala). Wynik: stopka-<imie>.html, plik lokalny, nie trafia do repo.

python generuj.py --styl A --imie "Anna Nowak" --stanowisko "Project Coordinator" --email anna.nowak@klaster.org.pl [--telefon "+48 732 259 513"]
Style: A czarny kafelek ze znakiem i tekst obok, bez linii; B kompaktowa wizytowka z kreska; C uklad pionowy, znak nad nazwiskiem.
Opcje: --czcionka georgia (domyslnie) | segoe | times; --dzial "..." dopisze szara linie (np. nazwe centrum albo projektu).
"""
import argparse, io, re, unicodedata
IMG = "https://klaster1234.github.io/stopki/img/"
p = argparse.ArgumentParser()
for a in ("imie", "stanowisko", "email"): p.add_argument("--" + a, required=True)
p.add_argument("--telefon", default="", help="opcjonalnie; bez tego stopka nie ma numeru")
p.add_argument("--styl", choices=("A", "B", "C"), default="A"); p.add_argument("--dzial", default="")
p.add_argument("--czcionka", choices=("georgia", "segoe", "times"), default="georgia")
a = p.parse_args()
CZ = {"georgia": ("Georgia,'Times New Roman',serif", "21px", "700", "25px", "12.5px"),
      "segoe": ("'Segoe UI',Helvetica,Arial,sans-serif", "19px", "600", "23px", "12px"),
      "times": ("'Times New Roman',Times,serif", "23px", "700", "26px", "13px")}
font, ns, nw, nlh, ts = CZ[a.czcionka]
dzial = ('<div style="font-size:12px;color:#6f6f6f;line-height:18px;">%s</div>' % a.dzial) if a.dzial else ""
telefon_seg = ('<a href="tel:%s" style="color:#111111;text-decoration:none;">%s</a><span style="color:#c4c4c4;">&nbsp;&nbsp;&#183;&nbsp;&nbsp;</span>'
               % (re.sub(r"[^\d+]", "", a.telefon), a.telefon)) if a.telefon else ""
html = io.open("szablon-%s.html" % a.styl, encoding="utf8").read()
for k, v in {"{{IMIE_NAZWISKO}}": a.imie, "{{STANOWISKO}}": a.stanowisko, "{{STANOWISKO_CAPS}}": a.stanowisko.upper(),
             "{{DZIAL_DIV}}": dzial, "{{TELEFON_SEG}}": telefon_seg,
             "{{EMAIL}}": a.email, "{{IMG}}": IMG, "{{FONT}}": font, "{{NAME_SIZE}}": ns,
             "{{NAME_WEIGHT}}": nw, "{{NAME_LH}}": nlh, "{{TEXT_SIZE}}": ts}.items():
    html = html.replace(k, v)
html = re.sub(r"\n\s*\n", "\n", html)
slug = unicodedata.normalize("NFKD", a.imie.split()[0]).encode("ascii", "ignore").decode().lower()
out = "stopka-%s.html" % slug
io.open(out, "w", encoding="utf8").write(html); print("zapisano", out)
