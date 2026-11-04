# Grafika za Google Play: uramljeni snimci telefona (1080×1920), naslovna grafika (1024×500)
# i ikona (512×512).
#
#   python play_grafika.py <folder sa raw_<jezik>_<n>.png> <izlazni folder>
#
# Snimci se prave sa telefona (1080×2340): seče se statusna traka (89 px) i baner sa
# navigacijom (od 2008 px), pa se snimak stavlja na mint pozadinu sa naslovom.
# Ikona se crta iz app/src/main/res/drawable/ic_launcher_foreground.xml pomoću Chrome-a.
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

KOREN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FONT_B = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_R = r"C:\Windows\Fonts\segoeui.ttf"
TEKST = (43, 42, 58)
TEKST2 = (94, 91, 112)

NASLOVI = {
    "en": ["Math, physics and chemistry in your pocket",
           "Tap a circle to explore",
           "Every topic at a glance",
           "Formulas with drawings and calculators",
           "Interactive periodic table",
           "Metric and imperial unit converter"],
    "sr": ["Matematika, fizika i hemija na dlanu",
           "Dodirni krug i istraži",
           "Sve teme na jednom mestu",
           "Formule sa crtežima i kalkulatorom",
           "Interaktivni periodni sistem",
           "Konverter metričkih i anglosaksonskih mera"],
}
PODNASLOV = {
    "en": "Formulas, calculators and unit converter",
    "sr": "Formule, kalkulatori i konverter jedinica",
}

# Pastelni krugovi za ukras (boje oblasti iz aplikacije, pomešane sa belom)
BOJE = [(0x2E, 0x5B, 0xBA), (0x6B, 0x3F, 0xA0), (0x0F, 0x7A, 0x6B), (0xB5, 0x40, 0x0F),
        (0xB4, 0x23, 0x5A), (0x2F, 0x6B, 0x2F), (0xC6, 0x28, 0x28), (0x00, 0x83, 0x8F), (0xD9, 0x82, 0x2B)]


def pastel(c, udeo=0.6):
    return tuple(int(x + (255 - x) * udeo) for x in c)


def tamna(c, udeo=0.45):
    return tuple(int(x * (1 - udeo)) for x in c)


def pozadina(w, h):
    """Mint prelaz kao na početnom ekranu aplikacije."""
    im = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(im)
    gore, dole = (243, 252, 247), (201, 230, 230)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line([(0, y), (w, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(gore, dole)))
    return im


def krug(slika, cx, cy, r, boja, alfa=255, senka=True):
    """Pastelni krug sa odsjajem (kao KrugView u aplikaciji)."""
    vel = int(r * 2 + 60)
    sloj = Image.new("RGBA", (vel, vel), (0, 0, 0, 0))
    if senka:
        s = Image.new("RGBA", (vel, vel), (0, 0, 0, 0))
        ImageDraw.Draw(s).ellipse([30, 38, 30 + 2 * r, 38 + 2 * r], fill=(40, 60, 60, int(60 * alfa / 255)))
        sloj = Image.alpha_composite(sloj, s.filter(ImageFilter.GaussianBlur(10)))
    k = Image.new("RGBA", (vel, vel), (0, 0, 0, 0))
    dk = ImageDraw.Draw(k)
    p, svetla = pastel(boja, 0.6), pastel(boja, 0.82)
    koraci = 40
    for i in range(koraci):  # radijalni prelaz od odsjaja gore levo
        t = i / koraci
        rr = r * (1 - t)
        cxx = 30 + r - 0.3 * r * t
        cyy = 30 + r - 0.4 * r * t
        boja_i = tuple(int(a + (b - a) * t) for a, b in zip(p, svetla))
        dk.ellipse([cxx - rr, cyy - rr, cxx + rr, cyy + rr], fill=boja_i + (alfa,))
    maska = Image.new("L", (vel, vel), 0)
    ImageDraw.Draw(maska).ellipse([30, 30, 30 + 2 * r, 30 + 2 * r], fill=alfa)
    k.putalpha(maska)
    sloj = Image.alpha_composite(sloj, k)
    slika.paste(sloj, (int(cx - r - 30), int(cy - r - 30)), sloj)


def prelom(tekst, font, maxw, d):
    redovi, r = [], ""
    for rec in tekst.split():
        p = (r + " " + rec).strip()
        if d.textlength(p, font=font) <= maxw:
            r = p
        else:
            redovi.append(r)
            r = rec
    redovi.append(r)
    return redovi


def snimak(ulaz, izlaz, naslov):
    W, H = 1080, 1920
    s = Image.open(ulaz).convert("RGB").crop((0, 89, 1080, 2008))
    sc = 0.74
    s = s.resize((int(s.width * sc), int(s.height * sc)), Image.LANCZOS)
    can = pozadina(W, H).convert("RGBA")
    # ukrasni krugovi iza snimka
    krug(can, 70, 520, 120, BOJE[0], 150, False)
    krug(can, 1030, 760, 150, BOJE[4], 150, False)
    krug(can, 90, 1500, 140, BOJE[2], 150, False)
    krug(can, 1010, 1750, 110, BOJE[8], 150, False)
    d = ImageDraw.Draw(can)
    font = ImageFont.truetype(FONT_B, 66)
    redovi = prelom(naslov, font, W - 150, d)
    y = 110 if len(redovi) > 1 else 150
    for r in redovi:
        tw = d.textlength(r, font=font)
        d.text(((W - tw) / 2, y), r, font=font, fill=TEKST)
        y += 84
    x0, y0 = (W - s.width) // 2, H - s.height - 60
    senka = Image.new("RGBA", (s.width + 100, s.height + 100), (0, 0, 0, 0))
    ImageDraw.Draw(senka).rounded_rectangle([50, 60, s.width + 50, s.height + 60], radius=48, fill=(30, 50, 50, 110))
    senka = senka.filter(ImageFilter.GaussianBlur(24))
    can.alpha_composite(senka, (x0 - 50, y0 - 50))
    maska = Image.new("L", s.size, 0)
    ImageDraw.Draw(maska).rounded_rectangle([0, 0, s.width - 1, s.height - 1], radius=44, fill=255)
    can.paste(s, (x0, y0), maska)
    can.convert("RGB").save(izlaz)


def ikona(izlaz):
    """ic_launcher_foreground.xml → SVG (vidljivi deo 72×72 od 108) → PNG 512×512 preko Chrome-a."""
    xml = open(os.path.join(KOREN, "app/src/main/res/drawable/ic_launcher_foreground.xml"), encoding="utf-8").read()
    putanje = []
    for m in re.finditer(r"<path([^>]*)/>", xml, re.S):
        a = m.group(1)
        boja = re.search(r'fillColor="#([0-9A-Fa-f]{6,8})"', a).group(1)[-6:]
        pd = re.search(r'pathData="([^"]+)"', a).group(1)
        pravilo = "evenodd" if 'fillType="evenOdd"' in a else "nonzero"
        putanje.append('<path fill="#%s" fill-rule="%s" d="%s"/>' % (boja, pravilo, pd))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="18 18 72 72">'
           '<rect x="0" y="0" width="108" height="108" fill="#FFFFFF"/>%s</svg>' % "".join(putanje))
    html = '<html><body style="margin:0;background:#fff">%s</body></html>' % svg
    with tempfile.TemporaryDirectory() as tmp:
        f = os.path.join(tmp, "ikona.html")
        open(f, "w", encoding="utf-8").write(html)
        png = os.path.join(tmp, "ikona.png")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=512,512", "--screenshot=" + png, "file:///" + f.replace("\\", "/")],
                       check=True, capture_output=True, timeout=60)
        Image.open(png).convert("RGB").crop((0, 0, 512, 512)).save(izlaz)


def naslovna(izlaz, ikona_png, jezik):
    W, H = 1024, 500
    can = pozadina(W, H).convert("RGBA")
    # pastelni krugovi sa simbolima oblasti, desno
    simboli = [("%", 0), ("x²", 1), ("△", 2), ("∫", 5), ("sin", 4), ("⚛", 6), ("⇄", 8), ("n!", 3)]
    mesta = [(700, 110, 62), (840, 95, 54), (960, 170, 50), (620, 270, 56),
             (770, 250, 72), (920, 330, 60), (690, 420, 50), (840, 430, 46)]
    fs = ImageFont.truetype(FONT_B, 40)
    fsim = ImageFont.truetype(r"C:\Windows\Fonts\seguisym.ttf", 40)
    for (sim, b), (x, y, r) in zip(simboli, mesta):
        krug(can, x, y, r, BOJE[b])
        d = ImageDraw.Draw(can)
        f = fsim if sim in ("△", "⚛", "⇄") else fs
        f = f.font_variant(size=int(r * 0.75))
        tw = d.textlength(sim, font=f)
        bb = d.textbbox((0, 0), sim, font=f)
        d.text((x - tw / 2, y - (bb[1] + bb[3]) / 2), sim, font=f, fill=tamna(BOJE[b]))
    # ikona i naziv, levo
    ik = Image.open(ikona_png).convert("RGBA").resize((170, 170), Image.LANCZOS)
    maska = Image.new("L", ik.size, 0)
    ImageDraw.Draw(maska).rounded_rectangle([0, 0, 169, 169], radius=40, fill=255)
    senka = Image.new("RGBA", (250, 250), (0, 0, 0, 0))
    ImageDraw.Draw(senka).rounded_rectangle([40, 48, 210, 218], radius=40, fill=(30, 50, 50, 90))
    can.alpha_composite(senka.filter(ImageFilter.GaussianBlur(14)), (20, 50))
    can.paste(ik, (60, 90), maska)
    d = ImageDraw.Draw(can)
    d.text((58, 285), "Formulix", font=ImageFont.truetype(FONT_B, 76), fill=TEKST)
    fp = ImageFont.truetype(FONT_R, 30)
    y = 385
    for r in prelom(PODNASLOV[jezik], fp, 470, d):
        d.text((62, y), r, font=fp, fill=TEKST2)
        y += 38
    can.convert("RGB").save(izlaz)


def main(ulaz, izlaz):
    os.makedirs(izlaz, exist_ok=True)
    ik = os.path.join(izlaz, "ikona_512.png")
    ikona(ik)
    for jezik, naslovi in NASLOVI.items():
        naslovna(os.path.join(izlaz, "naslovna_1024x500_%s.png" % jezik), ik, jezik)
        for i, naslov in enumerate(naslovi, 1):
            src = os.path.join(ulaz, "raw_%s_%d.png" % (jezik, i))
            if not os.path.isfile(src) or os.path.getsize(src) == 0:
                print("preskačem (nema snimka):", src)
                continue
            snimak(src, os.path.join(izlaz, "snimak_%s_%d.png" % (jezik, i)), naslov)
    print("gotovo:", izlaz)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
