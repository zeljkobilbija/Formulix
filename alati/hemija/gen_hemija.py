# Generiše assets/oblasti/hemija.json za Formulix: 118 elemenata periodnog sistema.
# Izvori: PubChem (pubchem_elementi.txt, javni podaci NIH) i IUPAC standardne atomske mase (skraćene).
#
#   python gen_hemija.py ../../app/src/main/assets/oblasti/hemija.json
import json, os, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
OVDE = os.path.dirname(os.path.abspath(__file__))

# ---------- IUPAC atomske mase (skraćene; u zagradi maseni broj najstabilnijeg izotopa) ----------
MASE = """1.0080 4.0026 6.94 9.0122 10.81 12.011 14.007 15.999 18.998 20.180
22.990 24.305 26.982 28.085 30.974 32.06 35.45 39.95 39.098 40.078
44.956 47.867 50.942 51.996 54.938 55.845 58.933 58.693 63.546 65.38
69.723 72.630 74.922 78.971 79.904 83.798 85.468 87.62 88.906 91.224
92.906 95.95 [98] 101.07 102.91 106.42 107.87 112.41 114.82 118.71
121.76 127.60 126.90 131.29 132.91 137.33 138.91 140.12 140.91 144.24
[145] 150.36 151.96 157.25 158.93 162.50 164.93 167.26 168.93 173.05
174.97 178.49 180.95 183.84 186.21 190.23 192.22 195.08 196.97 200.59
204.38 207.2 208.98 [209] [210] [222] [223] [226] [227] 232.04
231.04 238.03 [237] [244] [243] [247] [247] [251] [252] [257]
[258] [259] [266] [267] [268] [269] [270] [269] [278] [281]
[282] [285] [286] [289] [290] [293] [294] [294]""".split()
assert len(MASE) == 118

# ---------- nazivi ----------
def lista(s):
    x = [n.strip() for n in s.replace('\n', ' ').split(',')]
    assert len(x) == 118, (len(x), x[:3])
    return x

NAZIVI = {
 'sr': lista("""Vodonik, Helijum, Litijum, Berilijum, Bor, Ugljenik, Azot, Kiseonik, Fluor, Neon, Natrijum, Magnezijum, Aluminijum,
  Silicijum, Fosfor, Sumpor, Hlor, Argon, Kalijum, Kalcijum, Skandijum, Titan, Vanadijum, Hrom, Mangan, Gvožđe, Kobalt, Nikl, Bakar,
  Cink, Galijum, Germanijum, Arsen, Selen, Brom, Kripton, Rubidijum, Stroncijum, Itrijum, Cirkonijum, Niobijum, Molibden, Tehnecijum,
  Rutenijum, Rodijum, Paladijum, Srebro, Kadmijum, Indijum, Kalaj, Antimon, Telur, Jod, Ksenon, Cezijum, Barijum, Lantan, Cerijum,
  Prazeodijum, Neodijum, Prometijum, Samarijum, Evropijum, Gadolinijum, Terbijum, Disprozijum, Holmijum, Erbijum, Tulijum, Iterbijum,
  Lutecijum, Hafnijum, Tantal, Volfram, Renijum, Osmijum, Iridijum, Platina, Zlato, Živa, Talijum, Olovo, Bizmut, Polonijum, Astat,
  Radon, Francijum, Radijum, Aktinijum, Torijum, Protaktinijum, Uranijum, Neptunijum, Plutonijum, Americijum, Kirijum, Berklijum,
  Kalifornijum, Ajnštajnijum, Fermijum, Mendelevijum, Nobelijum, Lorencijum, Raderfordijum, Dubnijum, Siborgijum, Borijum, Hasijum,
  Majtnerijum, Darmštatijum, Rendgenijum, Kopernicijum, Nihonijum, Flerovijum, Moskovijum, Livermorijum, Tenesin, Oganeson"""),
 'en': lista("""Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon, Sodium, Magnesium, Aluminium,
  Silicon, Phosphorus, Sulfur, Chlorine, Argon, Potassium, Calcium, Scandium, Titanium, Vanadium, Chromium, Manganese, Iron, Cobalt,
  Nickel, Copper, Zinc, Gallium, Germanium, Arsenic, Selenium, Bromine, Krypton, Rubidium, Strontium, Yttrium, Zirconium, Niobium,
  Molybdenum, Technetium, Ruthenium, Rhodium, Palladium, Silver, Cadmium, Indium, Tin, Antimony, Tellurium, Iodine, Xenon, Caesium,
  Barium, Lanthanum, Cerium, Praseodymium, Neodymium, Promethium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium,
  Erbium, Thulium, Ytterbium, Lutetium, Hafnium, Tantalum, Tungsten, Rhenium, Osmium, Iridium, Platinum, Gold, Mercury, Thallium,
  Lead, Bismuth, Polonium, Astatine, Radon, Francium, Radium, Actinium, Thorium, Protactinium, Uranium, Neptunium, Plutonium,
  Americium, Curium, Berkelium, Californium, Einsteinium, Fermium, Mendelevium, Nobelium, Lawrencium, Rutherfordium, Dubnium,
  Seaborgium, Bohrium, Hassium, Meitnerium, Darmstadtium, Roentgenium, Copernicium, Nihonium, Flerovium, Moscovium, Livermorium,
  Tennessine, Oganesson"""),
 'it': lista("""Idrogeno, Elio, Litio, Berillio, Boro, Carbonio, Azoto, Ossigeno, Fluoro, Neon, Sodio, Magnesio, Alluminio, Silicio,
  Fosforo, Zolfo, Cloro, Argon, Potassio, Calcio, Scandio, Titanio, Vanadio, Cromo, Manganese, Ferro, Cobalto, Nichel, Rame, Zinco,
  Gallio, Germanio, Arsenico, Selenio, Bromo, Kripton, Rubidio, Stronzio, Ittrio, Zirconio, Niobio, Molibdeno, Tecnezio, Rutenio,
  Rodio, Palladio, Argento, Cadmio, Indio, Stagno, Antimonio, Tellurio, Iodio, Xeno, Cesio, Bario, Lantanio, Cerio, Praseodimio,
  Neodimio, Promezio, Samario, Europio, Gadolinio, Terbio, Disprosio, Olmio, Erbio, Tulio, Itterbio, Lutezio, Afnio, Tantalio,
  Tungsteno, Renio, Osmio, Iridio, Platino, Oro, Mercurio, Tallio, Piombo, Bismuto, Polonio, Astato, Radon, Francio, Radio, Attinio,
  Torio, Protoattinio, Uranio, Nettunio, Plutonio, Americio, Curio, Berkelio, Californio, Einsteinio, Fermio, Mendelevio, Nobelio,
  Laurenzio, Rutherfordio, Dubnio, Seaborgio, Bohrio, Hassio, Meitnerio, Darmstadtio, Roentgenio, Copernicio, Nihonio, Flerovio,
  Moscovio, Livermorio, Tennesso, Oganesson"""),
 'fr': lista("""Hydrogène, Hélium, Lithium, Béryllium, Bore, Carbone, Azote, Oxygène, Fluor, Néon, Sodium, Magnésium, Aluminium,
  Silicium, Phosphore, Soufre, Chlore, Argon, Potassium, Calcium, Scandium, Titane, Vanadium, Chrome, Manganèse, Fer, Cobalt, Nickel,
  Cuivre, Zinc, Gallium, Germanium, Arsenic, Sélénium, Brome, Krypton, Rubidium, Strontium, Yttrium, Zirconium, Niobium, Molybdène,
  Technétium, Ruthénium, Rhodium, Palladium, Argent, Cadmium, Indium, Étain, Antimoine, Tellure, Iode, Xénon, Césium, Baryum,
  Lanthane, Cérium, Praséodyme, Néodyme, Prométhium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Thulium,
  Ytterbium, Lutécium, Hafnium, Tantale, Tungstène, Rhénium, Osmium, Iridium, Platine, Or, Mercure, Thallium, Plomb, Bismuth,
  Polonium, Astate, Radon, Francium, Radium, Actinium, Thorium, Protactinium, Uranium, Neptunium, Plutonium, Américium, Curium,
  Berkélium, Californium, Einsteinium, Fermium, Mendélévium, Nobélium, Lawrencium, Rutherfordium, Dubnium, Seaborgium, Bohrium,
  Hassium, Meitnérium, Darmstadtium, Roentgenium, Copernicium, Nihonium, Flérovium, Moscovium, Livermorium, Tennesse, Oganesson"""),
 'es': lista("""Hidrógeno, Helio, Litio, Berilio, Boro, Carbono, Nitrógeno, Oxígeno, Flúor, Neón, Sodio, Magnesio, Aluminio, Silicio,
  Fósforo, Azufre, Cloro, Argón, Potasio, Calcio, Escandio, Titanio, Vanadio, Cromo, Manganeso, Hierro, Cobalto, Níquel, Cobre,
  Zinc, Galio, Germanio, Arsénico, Selenio, Bromo, Kriptón, Rubidio, Estroncio, Itrio, Circonio, Niobio, Molibdeno, Tecnecio,
  Rutenio, Rodio, Paladio, Plata, Cadmio, Indio, Estaño, Antimonio, Telurio, Yodo, Xenón, Cesio, Bario, Lantano, Cerio,
  Praseodimio, Neodimio, Prometio, Samario, Europio, Gadolinio, Terbio, Disprosio, Holmio, Erbio, Tulio, Iterbio, Lutecio, Hafnio,
  Tantalio, Wolframio, Renio, Osmio, Iridio, Platino, Oro, Mercurio, Talio, Plomo, Bismuto, Polonio, Astato, Radón, Francio, Radio,
  Actinio, Torio, Protactinio, Uranio, Neptunio, Plutonio, Americio, Curio, Berkelio, Californio, Einstenio, Fermio, Mendelevio,
  Nobelio, Lawrencio, Rutherfordio, Dubnio, Seaborgio, Bohrio, Hasio, Meitnerio, Darmstatio, Roentgenio, Copernicio, Nihonio,
  Flerovio, Moscovio, Livermorio, Teneso, Oganesón"""),
 'de': lista("""Wasserstoff, Helium, Lithium, Beryllium, Bor, Kohlenstoff, Stickstoff, Sauerstoff, Fluor, Neon, Natrium, Magnesium,
  Aluminium, Silicium, Phosphor, Schwefel, Chlor, Argon, Kalium, Calcium, Scandium, Titan, Vanadium, Chrom, Mangan, Eisen, Cobalt,
  Nickel, Kupfer, Zink, Gallium, Germanium, Arsen, Selen, Brom, Krypton, Rubidium, Strontium, Yttrium, Zirconium, Niob, Molybdän,
  Technetium, Ruthenium, Rhodium, Palladium, Silber, Cadmium, Indium, Zinn, Antimon, Tellur, Iod, Xenon, Caesium, Barium, Lanthan,
  Cer, Praseodym, Neodym, Promethium, Samarium, Europium, Gadolinium, Terbium, Dysprosium, Holmium, Erbium, Thulium, Ytterbium,
  Lutetium, Hafnium, Tantal, Wolfram, Rhenium, Osmium, Iridium, Platin, Gold, Quecksilber, Thallium, Blei, Bismut, Polonium, Astat,
  Radon, Francium, Radium, Actinium, Thorium, Protactinium, Uran, Neptunium, Plutonium, Americium, Curium, Berkelium, Californium,
  Einsteinium, Fermium, Mendelevium, Nobelium, Lawrencium, Rutherfordium, Dubnium, Seaborgium, Bohrium, Hassium, Meitnerium,
  Darmstadtium, Roentgenium, Copernicium, Nihonium, Flerovium, Moscovium, Livermorium, Tenness, Oganesson"""),
 'pt': lista("""Hidrogênio, Hélio, Lítio, Berílio, Boro, Carbono, Nitrogênio, Oxigênio, Flúor, Neônio, Sódio, Magnésio, Alumínio,
  Silício, Fósforo, Enxofre, Cloro, Argônio, Potássio, Cálcio, Escândio, Titânio, Vanádio, Cromo, Manganês, Ferro, Cobalto,
  Níquel, Cobre, Zinco, Gálio, Germânio, Arsênio, Selênio, Bromo, Criptônio, Rubídio, Estrôncio, Ítrio, Zircônio, Nióbio,
  Molibdênio, Tecnécio, Rutênio, Ródio, Paládio, Prata, Cádmio, Índio, Estanho, Antimônio, Telúrio, Iodo, Xenônio, Césio, Bário,
  Lantânio, Cério, Praseodímio, Neodímio, Promécio, Samário, Európio, Gadolínio, Térbio, Disprósio, Hólmio, Érbio, Túlio, Itérbio,
  Lutécio, Háfnio, Tântalo, Tungstênio, Rênio, Ósmio, Irídio, Platina, Ouro, Mercúrio, Tálio, Chumbo, Bismuto, Polônio, Astato,
  Radônio, Frâncio, Rádio, Actínio, Tório, Protactínio, Urânio, Netúnio, Plutônio, Amerício, Cúrio, Berquélio, Califórnio,
  Einstênio, Férmio, Mendelévio, Nobélio, Laurêncio, Rutherfórdio, Dúbnio, Seabórgio, Bóhrio, Hássio, Meitnério, Darmstácio,
  Roentgênio, Copernício, Nihônio, Fleróvio, Moscóvio, Livermório, Tenesso, Oganessônio"""),
 'ru': lista("""Водород, Гелий, Литий, Бериллий, Бор, Углерод, Азот, Кислород, Фтор, Неон, Натрий, Магний, Алюминий, Кремний, Фосфор,
  Сера, Хлор, Аргон, Калий, Кальций, Скандий, Титан, Ванадий, Хром, Марганец, Железо, Кобальт, Никель, Медь, Цинк, Галлий, Германий,
  Мышьяк, Селен, Бром, Криптон, Рубидий, Стронций, Иттрий, Цирконий, Ниобий, Молибден, Технеций, Рутений, Родий, Палладий, Серебро,
  Кадмий, Индий, Олово, Сурьма, Теллур, Иод, Ксенон, Цезий, Барий, Лантан, Церий, Празеодим, Неодим, Прометий, Самарий, Европий,
  Гадолиний, Тербий, Диспрозий, Гольмий, Эрбий, Тулий, Иттербий, Лютеций, Гафний, Тантал, Вольфрам, Рений, Осмий, Иридий, Платина,
  Золото, Ртуть, Таллий, Свинец, Висмут, Полоний, Астат, Радон, Франций, Радий, Актиний, Торий, Протактиний, Уран, Нептуний,
  Плутоний, Америций, Кюрий, Берклий, Калифорний, Эйнштейний, Фермий, Менделевий, Нобелий, Лоуренсий, Резерфордий, Дубний,
  Сиборгий, Борий, Хассий, Мейтнерий, Дармштадтий, Рентгений, Коперниций, Нихоний, Флеровий, Московий, Ливерморий, Теннессин,
  Оганесон"""),
}

VRSTE = {'Alkali metal': 'alkalni', 'Alkaline earth metal': 'zemnoalkalni', 'Transition metal': 'prelazni',
         'Post-transition metal': 'ostali_metali', 'Metalloid': 'metaloid', 'Nonmetal': 'nemetal', 'Halogen': 'halogen',
         'Noble gas': 'plemeniti_gas', 'Lanthanide': 'lantanoid', 'Actinide': 'aktinoid'}
STANJA = {'Gas': 'g', 'Liquid': 'l', 'Solid': 's'}

def broj(x):
    x = x.strip()
    if not x: return None
    v = float(x)
    return int(v) if v == int(v) and '.' not in x else v

def polozaj(z):
    """(perioda, grupa ili None, red u tabeli, kolona u tabeli, blok)"""
    granice = [2, 10, 18, 36, 54, 86, 118]
    perioda = next(i + 1 for i, g in enumerate(granice) if z <= g)
    pocetak = ([0] + granice)[perioda - 1]
    k = z - pocetak  # redni broj u periodi, od 1
    if perioda == 1:
        grupa = 1 if z == 1 else 18
    elif perioda in (2, 3):
        grupa = k if k <= 2 else k + 10
    elif perioda in (4, 5):
        grupa = k
    else:
        if k <= 2: grupa = k
        elif k <= 17: grupa = None          # f-blok (La…Lu, Ac…Lr)
        else: grupa = k - 14
    if grupa is None:
        red = 9 if perioda == 6 else 10
        kol = k - 3 + 3                      # La/Ac u koloni 3, Lu/Lr u koloni 17
        grupa_prikaz = 3 if k == 3 else None
        blok = 'f' if 3 < k < 17 else 'd'
        return perioda, grupa_prikaz, red, kol, blok
    if grupa <= 2 or z == 2: blok = 's'
    elif grupa >= 13: blok = 'p'
    else: blok = 'd'
    return perioda, grupa, perioda, grupa, blok

def oksidaciona(s):
    if not s.strip(): return []
    out = []
    for d in s.replace(' ', '').split(','):
        n = int(d)
        out.append(('+' if n > 0 else ('−' if n < 0 else '')) + str(abs(n)))
    return out

def konfiguracija(s):
    pred = '(predicted)' in s or '(calculated)' in s
    s = s.replace('(predicted)', '').replace('(calculated)', '').strip()
    s = s.replace('] ', ']')
    # orbitale poređane po n pa l (kao u udžbenicima): [Ar] 3d6 4s2
    jezgro, _, ostalo = s.partition(']')
    if not ostalo:
        jezgro, ostalo = '', s
    else:
        jezgro += ']'
    red = 'spdf'
    orb = sorted(ostalo.split(), key=lambda o: (int(o[0]), red.index(o[1])))
    return (jezgro + ' ' + ' '.join(orb)).strip(), pred

redovi = [l.rstrip('\n').split('|') for l in open(os.path.join(OVDE, 'pubchem_elementi.txt'), encoding='utf-8')
          if l.strip() and not l.startswith('#')]
assert len(redovi) == 118

teme = []
for r in redovi:
    z = int(r[0]); sim = r[1]
    perioda, grupa, red, kol, blok = polozaj(z)
    masa = MASE[z - 1]
    zagrada = masa.startswith('[')
    konf, konf_pred = konfiguracija(r[5])
    stanje_txt = r[11]
    el = {
        'z': z, 'simbol': sim, 'masa': masa.strip('[]'), 'masaIzotop': zagrada,
        'perioda': perioda, 'grupa': grupa, 'blok': blok, 'red': red, 'kolona': kol,
        'vrsta': VRSTE[r[15]],
        'konfiguracija': konf, 'konfPredvidjena': konf_pred,
        'elektronegativnost': broj(r[6]), 'poluprecnik': broj(r[7]),
        'jonizacija': broj(r[8]), 'afinitet': broj(r[9]),
        'oksidaciona': oksidaciona(r[10]),
        'stanje': STANJA[stanje_txt.split()[-1]], 'stanjePredvidjeno': stanje_txt.startswith('Expected'),
        'topljenje': broj(r[12]), 'kljucanje': broj(r[13]), 'gustina': broj(r[14]),
        'otkriven': None if r[16] == 'Ancient' else int(r[16]),
    }
    naziv = {j: NAZIVI[j][z - 1] for j in J}
    sep = {j: ('.' if j == 'en' else ',') for j in J}
    opis = {j: f"Z = {z} · {el['masa'].replace('.', sep[j])}" for j in J}
    if zagrada: opis = {j: f"Z = {z} · [{el['masa']}]" for j in J}
    # pretraga: naziv na svim jezicima i simbol (npr. "Eisen" ili "Fe" nalazi gvožđe)
    svi = ' '.join(sorted({NAZIVI[j][z - 1].lower() for j in J}))
    kljucne = {j: f"{sim.lower()} {svi} element" for j in J}
    teme.append({'id': str(z), 'simbol': sim, 'naziv': naziv, 'opis': opis, 'kljucne_reci': kljucne, 'element': el})

# provera položaja: svako polje tabele zauzeto najviše jednom
zauzeto = {}
for t in teme:
    k = (t['element']['red'], t['element']['kolona'])
    assert k not in zauzeto, (t['simbol'], zauzeto.get(k))
    zauzeto[k] = t['simbol']

out = {'oblast': 'hemija', 'izvor': 'PubChem (NIH); IUPAC', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('elemenata:', len(teme))
