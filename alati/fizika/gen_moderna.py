# Generiše assets/oblasti/moderna_fizika.json za Formulix
import json, math, re, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']

H = 6.62607015e-34; C0 = 299792458; E = 1.602176634e-19; ME = 9.1093837139e-31
U = 1.66053906892e-27; MP_U = 1.00727646688; MN_U = 1.00866491606; W0 = 13.605693122994 * E

FR = dict(sr='f', en='f', it='f', fr='f', es='f', de='f', pt='f', ru=r'\nu')
AI = dict(sr=r'A_i', en=r'\phi', it=r'W_0', fr=r'W_s', es=r'\phi', de=r'W_A', pt=r'\phi', ru=r'A_{\text{вых}}')
EK = dict(sr='E_k', en='E_k', it='E_c', fr='E_c', es='E_c', de=r'E_{\mathrm{kin}}', pt='E_c', ru=r'E_{\text{к}}')
TP = dict(sr='t_{1/2}', en='t_{1/2}', it='t_{1/2}', fr='t_{1/2}', es='t_{1/2}', de='T_{1/2}', pt='t_{1/2}', ru='T_{1/2}')
def S(f):
    def z(j):
        x = f
        for k, d in (('{f}', FR), ('{A}', AI), ('{Ek}', EK), ('{tp}', TP)):
            x = x.replace(k, d[j])
        return x
    return LJ(z)

N = {
 'Ef': T("energija fotona","photon energy","energia del fotone","énergie du photon","energía del fotón","Photonenenergie","energia do fóton","энергия фотона"),
 'h': T("Plankova konstanta","Planck constant","costante di Planck","constante de Planck","constante de Planck","Plancksches Wirkungsquantum","constante de Planck","постоянная Планка"),
 'f': T("frekvencija","frequency","frequenza","fréquence","frecuencia","Frequenz","frequência","частота"),
 'c': T("brzina svetlosti","speed of light","velocità della luce","vitesse de la lumière","velocidad de la luz","Lichtgeschwindigkeit","velocidade da luz","скорость света"),
 'lam': T("talasna dužina","wavelength","lunghezza d’onda","longueur d’onde","longitud de onda","Wellenlänge","comprimento de onda","длина волны"),
 'p': T("impuls","momentum","quantità di moto","quantité de mouvement","cantidad de movimiento","Impuls","quantidade de movimento","импульс"),
 'Ai': T("izlazni rad","work function","lavoro di estrazione","travail d’extraction","función trabajo","Austrittsarbeit","função trabalho","работа выхода"),
 'Ek': T("kinetička energija elektrona","kinetic energy of the electron","energia cinetica dell’elettrone","énergie cinétique de l’électron","energía cinética del electrón","kinetische Energie des Elektrons","energia cinética do elétron","кинетическая энергия электрона"),
 'lg': T("granična talasna dužina","threshold wavelength","lunghezza d’onda di soglia","longueur d’onde seuil","longitud de onda umbral","Grenzwellenlänge","comprimento de onda limite","красная граница"),
 'e': T("elementarno naelektrisanje","elementary charge","carica elementare","charge élémentaire","carga elemental","Elementarladung","carga elementar","элементарный заряд"),
 'Uz': T("zaustavni napon","stopping voltage","potenziale d’arresto","tension d’arrêt","potencial de frenado","Gegenspannung","potencial de corte","задерживающее напряжение"),
 'm': T("masa čestice","mass of the particle","massa della particella","masse de la particule","masa de la partícula","Masse des Teilchens","massa da partícula","масса частицы"),
 'v': T("brzina čestice","velocity of the particle","velocità della particella","vitesse de la particule","velocidad de la partícula","Geschwindigkeit des Teilchens","velocidade da partícula","скорость частицы"),
 'Ua': T("napon ubrzavanja","accelerating voltage","tensione di accelerazione","tension d’accélération","tensión de aceleración","Beschleunigungsspannung","tensão de aceleração","ускоряющее напряжение"),
 'lmin': T("najmanja talasna dužina","minimum wavelength","lunghezza d’onda minima","longueur d’onde minimale","longitud de onda mínima","Grenzwellenlänge","comprimento de onda mínimo","минимальная длина волны"),
 'n': T("glavni kvantni broj","principal quantum number","numero quantico principale","nombre quantique principal","número cuántico principal","Hauptquantenzahl","número quântico principal","главное квантовое число"),
 'n2': T("početni nivo (viši)","initial level (higher)","livello iniziale (più alto)","niveau initial (supérieur)","nivel inicial (superior)","Ausgangsniveau (höher)","nível inicial (mais alto)","начальный уровень (верхний)"),
 'n1': T("konačni nivo (niži)","final level (lower)","livello finale (più basso)","niveau final (inférieur)","nivel final (inferior)","Endniveau (tiefer)","nível final (mais baixo)","конечный уровень (нижний)"),
 'Wn': T("energija nivoa","energy of the level","energia del livello","énergie du niveau","energía del nivel","Energie des Niveaus","energia do nível","энергия уровня"),
 'W0': T("energija jonizacije vodonika","ionization energy of hydrogen","energia di ionizzazione dell’idrogeno","énergie d’ionisation de l’hydrogène","energía de ionización del hidrógeno","Ionisierungsenergie von Wasserstoff","energia de ionização do hidrogênio","энергия ионизации водорода"),
 'rn': T("poluprečnik orbite","radius of the orbit","raggio dell’orbita","rayon de l’orbite","radio de la órbita","Bahnradius","raio da órbita","радиус орбиты"),
 'rB': T("Borov poluprečnik","Bohr radius","raggio di Bohr","rayon de Bohr","radio de Bohr","Bohrscher Radius","raio de Bohr","боровский радиус"),
 'N': T("broj neraspadnutih jezgara","number of undecayed nuclei","numero di nuclei non decaduti","nombre de noyaux restants","número de núcleos sin desintegrar","Anzahl unzerfallener Kerne","número de núcleos restantes","число нераспавшихся ядер"),
 'N0': T("početni broj jezgara","initial number of nuclei","numero iniziale di nuclei","nombre initial de noyaux","número inicial de núcleos","Anfangszahl der Kerne","número inicial de núcleos","начальное число ядер"),
 't': T("proteklo vreme","elapsed time","tempo trascorso","temps écoulé","tiempo transcurrido","vergangene Zeit","tempo decorrido","прошедшее время"),
 'tp': T("vreme poluraspada","half-life","tempo di dimezzamento","demi-vie","periodo de semidesintegración","Halbwertszeit","meia-vida","период полураспада"),
 'lr': T("konstanta raspada","decay constant","costante di decadimento","constante radioactive","constante de desintegración","Zerfallskonstante","constante de decaimento","постоянная распада"),
 'A': T("aktivnost","activity","attività","activité","actividad","Aktivität","atividade","активность"),
 'udeo': T("preostali deo","remaining fraction","frazione rimanente","fraction restante","fracción restante","verbleibender Anteil","fração restante","оставшаяся доля"),
 'j': T("intenzitet posle sloja","intensity after the layer","intensità dopo lo strato","intensité après la couche","intensidad tras la capa","Intensität nach der Schicht","intensidade após a camada","интенсивность после слоя"),
 'j0': T("početni intenzitet","initial intensity","intensità iniziale","intensité initiale","intensidad inicial","Anfangsintensität","intensidade inicial","начальная интенсивность"),
 'x': T("debljina sloja","thickness of the layer","spessore dello strato","épaisseur de la couche","espesor de la capa","Schichtdicke","espessura da camada","толщина слоя"),
 'mu': T("koeficijent slabljenja","attenuation coefficient","coefficiente di attenuazione","coefficient d’atténuation","coeficiente de atenuación","Schwächungskoeffizient","coeficiente de atenuação","коэффициент ослабления"),
 'dp': T("debljina poluslabljenja","half-value thickness","spessore di dimezzamento","couche de demi-atténuation","espesor de semirreducción","Halbwertsdicke","camada semirredutora","слой половинного ослабления"),
 'Em': T("energija","energy","energia","énergie","energía","Energie","energia","энергия"),
 'dm': T("defekt mase (razlika masa)","mass defect (mass difference)","difetto di massa","défaut de masse","defecto de masa","Massendefekt","defeito de massa","дефект массы"),
 'Z': T("broj protona","number of protons","numero di protoni","nombre de protons","número de protones","Protonenzahl","número de prótons","число протонов"),
 'Nn': T("broj neutrona","number of neutrons","numero di neutroni","nombre de neutrons","número de neutrones","Neutronenzahl","número de nêutrons","число нейтронов"),
 'mj': T("masa jezgra","mass of the nucleus","massa del nucleo","masse du noyau","masa del núcleo","Kernmasse","massa do núcleo","масса ядра"),
 'mp': T("masa protona","proton mass","massa del protone","masse du proton","masa del protón","Protonenmasse","massa do próton","масса протона"),
 'mn': T("masa neutrona","neutron mass","massa del neutrone","masse du neutron","masa del neutrón","Neutronenmasse","massa do nêutron","масса нейтрона"),
 'Wv': T("energija veze","binding energy","energia di legame","énergie de liaison","energía de enlace","Bindungsenergie","energia de ligação","энергия связи"),
}
OZ = {'Ef': 'E', 'h': 'h', 'f': S('{f}'), 'c': 'c', 'lam': r'\lambda', 'p': 'p', 'Ai': S('{A}'), 'Ek': S('{Ek}'), 'lg': r'\lambda_g',
      'e': 'e', 'Uz': 'U_z', 'm': 'm', 'v': 'v', 'Ua': 'U', 'lmin': r'\lambda_{\min}', 'n': 'n', 'n2': "n'", 'n1': 'n', 'Wn': 'W_n',
      'W0': 'W_0', 'rn': 'r_n', 'rB': 'r_B', 'N': 'N', 'N0': 'N_0', 't': 't', 'tp': S('{tp}'), 'lr': r'\lambda', 'A': 'A',
      'udeo': 'N/N_0', 'j': 'j', 'j0': 'j_0', 'x': 'x', 'mu': r'\mu', 'dp': 'd_{1/2}', 'Em': 'E', 'dm': r'\Delta m', 'Z': 'Z',
      'Nn': 'N', 'mj': 'm_j', 'mp': 'm_p', 'mn': 'm_n', 'Wv': 'W_v'}
VRSTA = {'Ef': 'energija', 'h': 'plank', 'f': 'frekvencija', 'c': 'brzina', 'lam': 'talasnaDuzina', 'p': 'impuls', 'Ai': 'energija',
         'Ek': 'energija', 'lg': 'talasnaDuzina', 'e': 'naboj', 'Uz': 'napon', 'm': 'masa', 'v': 'brzina', 'Ua': 'napon',
         'lmin': 'talasnaDuzina', 'n': 'broj', 'n2': 'broj', 'n1': 'broj', 'Wn': 'energija', 'W0': 'energija', 'rn': 'talasnaDuzina',
         'rB': 'talasnaDuzina', 'N': 'broj', 'N0': 'broj', 't': 'vreme', 'tp': 'vreme', 'lr': 'konstRaspada', 'A': 'aktivnost',
         'udeo': 'udeo', 'j': 'intenzitet', 'j0': 'intenzitet', 'x': 'duzina', 'mu': 'koefSlabljenja', 'dp': 'duzina', 'Em': 'energija',
         'dm': 'masa', 'Z': 'broj', 'Nn': 'broj', 'mj': 'masa', 'mp': 'masa', 'mn': 'masa', 'Wv': 'energija'}
NENEG = {'Ek', 't', 'x', 'Z', 'Nn'}
NEPOZ = {'Wn', 'Ek', 't', 'x', 'Z', 'Nn', 'Wv', 'Em', 'dm'}

def velicine(pocetne, jed={}):
    out = {}
    for k, p in pocetne.items():
        d = {'oznaka': OZ[k], 'naziv': N[k], 'vrsta': VRSTA[k]}
        if p is not None: d['pocetna'] = p
        if k in jed: d['jed'] = jed[k]
        if k not in NEPOZ: d['poz'] = True
        if k in NENEG: d['nenegativna'] = True
        out[k] = d
    return out
def F(naslov, latex, obj):
    return {'naslov': naslov, 'latex': latex, 'objasnjenje': obj}

def crtez_nivoi():
    """Energetski nivoi vodonika (razmak nije u razmeri, da bi oznake bile čitljive)."""
    nivoi = [(1, 176), (2, 112), (3, 80), (4, 58), (5, 44)]
    s = '<svg viewBox="0 0 300 196" xmlns="http://www.w3.org/2000/svg" role="img">'
    for n, y in nivoi:
        e = ('%.2f' % (-13.6057 / n / n)).replace('.', ',').replace('-', '−')
        s += f'<line class="lik-l" x1="64" y1="{y}" x2="216" y2="{y}"/>'
        s += f'<text class="tem" x="14" y="{y + 5}">n = {n}</text>'
        s += f'<text class="tem" x="224" y="{y + 5}">{e} eV</text>'
    s += '<line class="pom" x1="64" y1="20" x2="216" y2="20"/><text class="tem" x="14" y="25">n = ∞</text><text class="tem" x="224" y="25">0 eV</text>'
    y = dict(nivoi)
    for x, a_, b_ in ((96, 2, 1), (140, 3, 2), (176, 4, 2)):
        s += f'<line class="ivica" x1="{x}" y1="{y[a_]}" x2="{x}" y2="{y[b_] - 9}"/><path class="tac" d="M{x},{y[b_]} l-4.5,-9 h9 Z"/>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'foton', 'simbol': 'hf',
 'naziv': T("Foton","Photon","Fotone","Photon","Fotón","Photon","Fóton","Фотон"),
 'opis': T("Energija i impuls fotona","Photon energy and momentum","Energia e quantità di moto","Énergie et quantité de mouvement","Energía y momento","Energie und Impuls","Energia e momento","Энергия и импульс фотона"),
 'kljucne_reci': T("foton kvant svetlosti energija fotona plankova konstanta impuls fotona","photon quantum of light photon energy planck constant photon momentum","fotone quanto di luce energia costante di planck","photon quantum energie constante de planck","foton cuanto de luz energia constante de planck","photon lichtquant energie plancksches wirkungsquantum","foton quantum de luz energia constante de planck","фотон квант света энергия фотона постоянная планка импульс"),
 'formule': [
  F(T("Energija fotona","Photon energy","Energia del fotone","Énergie du photon","Energía del fotón","Photonenenergie","Energia do fóton","Энергия фотона"),
    S(r"E = h {f} = \frac{h c}{\lambda}"),
    T("Zelena svetlost (550 nm) ima fotone od oko 2,25 eV; h = 6,626 · 10⁻³⁴ J·s.","Green light (550 nm) has photons of about 2.25 eV; h = 6.626 · 10⁻³⁴ J·s.","La luce verde (550 nm) ha fotoni di circa 2,25 eV; h = 6,626 · 10⁻³⁴ J·s.","La lumière verte (550 nm) a des photons d’environ 2,25 eV ; h = 6,626 · 10⁻³⁴ J·s.","La luz verde (550 nm) tiene fotones de unos 2,25 eV; h = 6,626 · 10⁻³⁴ J·s.","Grünes Licht (550 nm) hat Photonen von etwa 2,25 eV; h = 6,626 · 10⁻³⁴ J·s.","A luz verde (550 nm) tem fótons de cerca de 2,25 eV; h = 6,626 · 10⁻³⁴ J·s.","Зелёный свет (550 нм) — фотоны около 2,25 эВ; h = 6,626 · 10⁻³⁴ Дж·с.")),
  F(T("Impuls fotona","Photon momentum","Quantità di moto del fotone","Quantité de mouvement du photon","Momento del fotón","Impuls des Photons","Momento do fóton","Импульс фотона"),
    S(r"p = \frac{E}{c} = \frac{h {f}}{c} = \frac{h}{\lambda}"),
    T("Foton nema masu mirovanja, ali ima impuls.","A photon has no rest mass but does carry momentum.","Il fotone non ha massa a riposo ma ha quantità di moto.","Le photon n’a pas de masse au repos mais possède une quantité de mouvement.","El fotón no tiene masa en reposo pero sí momento.","Ein Photon hat keine Ruhemasse, aber einen Impuls.","O fóton não tem massa de repouso, mas tem momento.","У фотона нет массы покоя, но есть импульс.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ef': None, 'h': H, 'f': 5.45e14, 'c': C0, 'lam': 550e-9, 'p': None}, {'Ef': 'eV', 'lam': 'nm', 'f': 'THz'}),
  'jednacine': [
   {'latex': S(r"E = h {f}"), 'trazi': 'Ef', 'resenja': {'Ef': 'h*f', 'f': 'Ef/h'}},
   {'latex': r"E = \dfrac{h c}{\lambda}", 'trazi': 'Ef', 'resenja': {'Ef': 'h*c/lam', 'lam': 'h*c/Ef'}},
   {'latex': r"p = \dfrac{h}{\lambda}", 'trazi': 'p', 'resenja': {'p': 'h/lam', 'lam': 'h/p'}},
  ]}
})

teme.append({
 'id': 'fotoefekat', 'simbol': 'e⁻',
 'naziv': T("Fotoelektrični efekat","Photoelectric effect","Effetto fotoelettrico","Effet photoélectrique","Efecto fotoeléctrico","Photoelektrischer Effekt","Efeito fotoelétrico","Фотоэффект"),
 'opis': T("Ajnštajnova jednačina","Einstein’s equation","Equazione di Einstein","Équation d’Einstein","Ecuación de Einstein","Einsteinsche Gleichung","Equação de Einstein","Уравнение Эйнштейна"),
 'kljucne_reci': T("fotoelektricni efekat fotoefekat izlazni rad granicna talasna duzina zaustavni napon ajnstajn","photoelectric effect work function threshold wavelength stopping voltage einstein","effetto fotoelettrico lavoro di estrazione soglia potenziale d arresto einstein","effet photoelectrique travail d extraction seuil tension d arret einstein","efecto fotoelectrico funcion trabajo umbral potencial de frenado einstein","photoeffekt austrittsarbeit grenzwellenlange gegenspannung einstein","efeito fotoeletrico funcao trabalho limiar potencial de corte einstein","фотоэффект работа выхода красная граница задерживающее напряжение эйнштейн"),
 'formule': [
  F(T("Ajnštajnova jednačina","Einstein’s equation","Equazione di Einstein","Équation d’Einstein","Ecuación de Einstein","Einsteinsche Gleichung","Equação de Einstein","Уравнение Эйнштейна"),
    S(r"h {f} = {A} + {Ek}"),
    T("Energija fotona troši se na izlazni rad iz metala, a ostatak je kinetička energija elektrona.","The photon energy goes into the work function of the metal; the rest is the electron’s kinetic energy.","L’energia del fotone serve per il lavoro di estrazione; il resto è energia cinetica dell’elettrone.","L’énergie du photon sert au travail d’extraction ; le reste est l’énergie cinétique de l’électron.","La energía del fotón se usa en la función trabajo; el resto es energía cinética del electrón.","Die Photonenenergie deckt die Austrittsarbeit; der Rest ist kinetische Energie des Elektrons.","A energia do fóton vai para a função trabalho; o resto é energia cinética do elétron.","Энергия фотона идёт на работу выхода, остаток — кинетическая энергия электрона.")),
  F(T("Granična talasna dužina i zaustavni napon","Threshold wavelength and stopping voltage","Soglia e potenziale d’arresto","Seuil et tension d’arrêt","Umbral y potencial de frenado","Grenzwellenlänge und Gegenspannung","Limiar e potencial de corte","Красная граница и задерживающее напряжение"),
    S(r"{A} = \frac{h c}{\lambda_g}, \quad {Ek} = e\,U_z"),
    T("Svetlost duža od λ_g ne izbija elektrone, ma koliko bila jaka. Cezijum: izlazni rad ≈ 2,1 eV.","Light longer than λ_g ejects no electrons, however intense. Caesium: work function ≈ 2.1 eV.","Luce con λ maggiore di λ_g non estrae elettroni, per quanto intensa. Cesio: ≈ 2,1 eV.","Une lumière de longueur d’onde supérieure à λ_g n’arrache aucun électron. Césium : ≈ 2,1 eV.","La luz con λ mayor que λ_g no arranca electrones, por intensa que sea. Cesio: ≈ 2,1 eV.","Licht mit größerer Wellenlänge als λ_g löst keine Elektronen aus. Cäsium: ≈ 2,1 eV.","Luz com λ maior que λ_g não arranca elétrons, por mais intensa. Césio: ≈ 2,1 eV.","Свет длиннее λ_g не вырывает электроны при любой интенсивности. Цезий: ≈ 2,1 эВ.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ek': None, 'h': H, 'c': C0, 'lam': 400e-9, 'Ai': 2.1 * E, 'lg': None, 'Uz': None, 'e': E}, {'Ek': 'eV', 'Ai': 'eV', 'lam': 'nm', 'lg': 'nm'}),
  'jednacine': [
   {'latex': S(r"{Ek} = \dfrac{h c}{\lambda} - {A}"), 'trazi': 'Ek', 'resenja': {'Ek': 'h*c/lam - Ai', 'Ai': 'h*c/lam - Ek', 'lam': 'h*c/(Ek + Ai)'}},
   {'latex': S(r"{A} = \dfrac{h c}{\lambda_g}"), 'trazi': 'lg', 'resenja': {'lg': 'h*c/Ai', 'Ai': 'h*c/lg'}},
   {'latex': S(r"{Ek} = e U_z"), 'trazi': 'Uz', 'resenja': {'Uz': 'Ek/e', 'Ek': 'e*Uz'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['Ek']['nenegativna'] = True

teme.append({
 'id': 'de_brolj', 'simbol': 'λ',
 'naziv': T("Talasna priroda čestica","Wave nature of particles","Natura ondulatoria delle particelle","Nature ondulatoire des particules","Naturaleza ondulatoria de las partículas","Wellennatur von Teilchen","Natureza ondulatória das partículas","Волновые свойства частиц"),
 'opis': T("De Broljeva talasna dužina, rendgensko zračenje","De Broglie wavelength, X-rays","Lunghezza d’onda di de Broglie, raggi X","Longueur d’onde de de Broglie, rayons X","Longitud de onda de De Broglie, rayos X","De-Broglie-Wellenlänge, Röntgenstrahlung","Comprimento de onda de de Broglie, raios X","Длина волны де Бройля, рентгеновское излучение"),
 'kljucne_reci': T("de broljeva talasna duzina talasna priroda elektrona elektronski mikroskop rendgensko zracenje kocno zracenje","de broglie wavelength matter waves electron microscope x rays bremsstrahlung","lunghezza d onda di de broglie onde di materia raggi x bremsstrahlung","longueur d onde de de broglie ondes de matiere rayons x freinage","longitud de onda de de broglie ondas de materia rayos x frenado","de broglie wellenlange materiewellen rontgenstrahlung bremsstrahlung","comprimento de onda de de broglie ondas de materia raios x frenagem","длина волны де бройля волны материи рентгеновское тормозное излучение"),
 'formule': [
  F(T("De Broljeva talasna dužina","De Broglie wavelength","Lunghezza d’onda di de Broglie","Longueur d’onde de de Broglie","Longitud de onda de De Broglie","De-Broglie-Wellenlänge","Comprimento de onda de de Broglie","Длина волны де Бройля"),
    r"\lambda = \frac{h}{p} = \frac{h}{m v}",
    T("Svaka čestica ima i talasna svojstva; na tome rade elektronski mikroskopi.","Every particle also has wave properties; electron microscopes rely on this.","Ogni particella ha anche proprietà ondulatorie; su questo si basano i microscopi elettronici.","Toute particule a des propriétés ondulatoires ; c’est le principe du microscope électronique.","Toda partícula tiene propiedades ondulatorias; en ello se basan los microscopios electrónicos.","Jedes Teilchen hat auch Welleneigenschaften; darauf beruht das Elektronenmikroskop.","Toda partícula tem propriedades ondulatórias; nisso se baseia o microscópio eletrônico.","У каждой частицы есть волновые свойства; на этом основан электронный микроскоп.")),
  F(T("Elektron ubrzan naponom U","Electron accelerated through voltage U","Elettrone accelerato dalla tensione U","Électron accéléré sous la tension U","Electrón acelerado por la tensión U","Durch Spannung U beschleunigtes Elektron","Elétron acelerado pela tensão U","Электрон, ускоренный напряжением U"),
    r"\lambda = \frac{h}{\sqrt{2 m e U}}",
    T("Važi dok je brzina mnogo manja od brzine svetlosti.","Valid while the speed is much less than the speed of light.","Vale finché la velocità è molto minore di quella della luce.","Valable tant que la vitesse est très inférieure à celle de la lumière.","Válido mientras la velocidad sea mucho menor que la de la luz.","Gilt, solange die Geschwindigkeit viel kleiner als die Lichtgeschwindigkeit ist.","Válido enquanto a velocidade for muito menor que a da luz.","Верно, пока скорость много меньше скорости света.")),
  F(T("Rendgenska cev (kočeno zračenje)","X-ray tube (bremsstrahlung)","Tubo a raggi X (bremsstrahlung)","Tube à rayons X (freinage)","Tubo de rayos X (frenado)","Röntgenröhre (Bremsstrahlung)","Tubo de raios X (frenagem)","Рентгеновская трубка (тормозное излучение)"),
    r"e U = \frac{h c}{\lambda_{\min}}",
    T("Najkraća talasna dužina kada elektron svu energiju preda jednom fotonu.","Shortest wavelength, when the electron gives all its energy to one photon.","Lunghezza d’onda minima, quando l’elettrone cede tutta l’energia a un fotone.","Longueur d’onde minimale, quand l’électron cède toute son énergie à un photon.","Longitud de onda mínima, cuando el electrón cede toda su energía a un fotón.","Kürzeste Wellenlänge, wenn das Elektron seine ganze Energie an ein Photon abgibt.","Menor comprimento de onda, quando o elétron cede toda a energia a um fóton.","Минимальная длина волны, когда электрон отдаёт всю энергию одному фотону.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'lam': None, 'h': H, 'm': ME, 'v': 1e6, 'e': E, 'Ua': 100, 'lmin': None}, {'lam': 'nm', 'lmin': 'pm'}),
  'jednacine': [
   {'latex': r"\lambda = \dfrac{h}{m v}", 'trazi': 'lam', 'resenja': {'lam': 'h/(m*v)', 'm': 'h/(lam*v)', 'v': 'h/(lam*m)'}},
   {'latex': r"\lambda = \dfrac{h}{\sqrt{2 m e U}}", 'trazi': 'lam', 'resenja': {'lam': 'h/sqrt(2*m*e*Ua)', 'Ua': 'pow(h/lam, 2)/(2*m*e)', 'm': 'pow(h/lam, 2)/(2*e*Ua)'},
    'napomene': {'lam': T("Podrazumevano: elektron.","Default: electron.","Predefinito: elettrone.","Par défaut : électron.","Por defecto: electrón.","Voreinstellung: Elektron.","Padrão: elétron.","По умолчанию: электрон.")}},
   {'latex': r"\lambda_{\min} = \dfrac{h c}{e U}", 'trazi': 'lmin', 'resenja': {'lmin': 'h*299792458/(e*Ua)', 'Ua': 'h*299792458/(e*lmin)'}},
  ]}
})

teme.append({
 'id': 'bor', 'simbol': 'n',
 'naziv': T("Borov model atoma","Bohr model of the atom","Modello atomico di Bohr","Modèle de Bohr","Modelo atómico de Bohr","Bohrsches Atommodell","Modelo atômico de Bohr","Модель атома Бора"),
 'opis': T("Energetski nivoi vodonika","Energy levels of hydrogen","Livelli energetici dell’idrogeno","Niveaux d’énergie de l’hydrogène","Niveles de energía del hidrógeno","Energieniveaus von Wasserstoff","Níveis de energia do hidrogênio","Уровни энергии водорода"),
 'kljucne_reci': T("borov model atom vodonika energetski nivoi spektar prelaz balmerova serija lajmanova serija","bohr model hydrogen atom energy levels spectrum transition balmer lyman series","modello di bohr atomo di idrogeno livelli energetici spettro serie di balmer","modele de bohr atome d hydrogene niveaux spectre serie de balmer","modelo de bohr atomo de hidrogeno niveles espectro serie de balmer","bohrsches atommodell wasserstoff energieniveaus spektrum balmer serie","modelo de bohr atomo de hidrogenio niveis espectro serie de balmer","модель бора атом водорода уровни энергии спектр серия бальмера"),
 'crtez': crtez_nivoi(),
 'formule': [
  F(T("Energija nivoa","Energy of the levels","Energia dei livelli","Énergie des niveaux","Energía de los niveles","Energie der Niveaus","Energia dos níveis","Энергия уровней"),
    r"W_n = -\frac{W_0}{n^2}, \quad W_0 = \frac{m_e e^4}{8 \varepsilon_0^2 h^2} = 13{,}6\ \mathrm{eV}",
    T("n = 1 je osnovno stanje; W₀ je energija potrebna da se atom vodonika jonizuje.","n = 1 is the ground state; W₀ is the energy needed to ionize a hydrogen atom.","n = 1 è lo stato fondamentale; W₀ è l’energia di ionizzazione dell’idrogeno.","n = 1 est l’état fondamental ; W₀ est l’énergie d’ionisation de l’hydrogène.","n = 1 es el estado fundamental; W₀ es la energía de ionización del hidrógeno.","n = 1 ist der Grundzustand; W₀ ist die Ionisierungsenergie von Wasserstoff.","n = 1 é o estado fundamental; W₀ é a energia de ionização do hidrogênio.","n = 1 — основное состояние; W₀ — энергия ионизации водорода.")),
  F(T("Poluprečnik orbite","Radius of the orbit","Raggio dell’orbita","Rayon de l’orbite","Radio de la órbita","Bahnradius","Raio da órbita","Радиус орбиты"),
    r"r_n = n^2 r_B, \quad r_B = \frac{h^2 \varepsilon_0}{\pi m_e e^2} = 52{,}9\ \mathrm{pm}",
    T("r_B je Borov poluprečnik, poluprečnik osnovnog stanja.","r_B is the Bohr radius, the radius of the ground state.","r_B è il raggio di Bohr, raggio dello stato fondamentale.","r_B est le rayon de Bohr, celui de l’état fondamental.","r_B es el radio de Bohr, el del estado fundamental.","r_B ist der Bohrsche Radius des Grundzustands.","r_B é o raio de Bohr, do estado fundamental.","r_B — боровский радиус основного состояния.")),
  F(T("Prelaz između nivoa","Transition between levels","Transizione tra livelli","Transition entre niveaux","Transición entre niveles","Übergang zwischen Niveaus","Transição entre níveis","Переход между уровнями"),
    S(r"h {f} = W_0 \left(\frac{1}{n^2} - \frac{1}{n'^2}\right), \quad n' > n"),
    T("Pri prelazu na niži nivo atom emituje foton. Prelazi na n = 2 daju vidljivu Balmerovu seriju.","When dropping to a lower level the atom emits a photon. Transitions to n = 2 give the visible Balmer series.","Scendendo a un livello inferiore l’atomo emette un fotone. Le transizioni a n = 2 danno la serie di Balmer visibile.","En passant à un niveau inférieur l’atome émet un photon. Les transitions vers n = 2 donnent la série de Balmer visible.","Al bajar de nivel el átomo emite un fotón. Las transiciones a n = 2 dan la serie de Balmer visible.","Beim Übergang auf ein tieferes Niveau sendet das Atom ein Photon aus. Übergänge nach n = 2 bilden die sichtbare Balmer-Serie.","Ao descer de nível o átomo emite um fóton. Transições para n = 2 dão a série de Balmer visível.","При переходе на нижний уровень атом излучает фотон. Переходы на n = 2 дают видимую серию Бальмера.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Wn': None, 'W0': W0, 'n': 2, 'rn': None, 'rB': 5.29177210544e-11, 'lam': None, 'h': H, 'c': C0, 'n1': 2, 'n2': 3}, {'Wn': 'eV', 'W0': 'eV', 'rn': 'pm', 'rB': 'pm', 'lam': 'nm'}),
  'jednacine': [
   {'latex': r"W_n = -\dfrac{W_0}{n^2}", 'trazi': 'Wn', 'resenja': {'Wn': '-W0/(n*n)', 'n': 'sqrt(-W0/Wn)', 'W0': '-Wn*n*n'}},
   {'latex': r"r_n = n^2 r_B", 'trazi': 'rn', 'resenja': {'rn': 'n*n*rB', 'n': 'sqrt(rn/rB)'}},
   {'latex': r"\dfrac{h c}{\lambda} = W_0 \left(\dfrac{1}{n^2} - \dfrac{1}{n'^2}\right)", 'trazi': 'lam',
    'resenja': {'lam': 'h*c/(W0*(1/(n1*n1) - 1/(n2*n2)))', 'n2': '1/sqrt(1/(n1*n1) - h*c/(W0*lam))', 'n1': '1/sqrt(1/(n2*n2) + h*c/(W0*lam))'},
    'napomene': {'lam': T("Primer: prelaz 3 → 2 daje crvenu liniju vodonika (656 nm).","Example: transition 3 → 2 gives hydrogen’s red line (656 nm).","Esempio: la transizione 3 → 2 dà la riga rossa dell’idrogeno (656 nm).","Exemple : la transition 3 → 2 donne la raie rouge de l’hydrogène (656 nm).","Ejemplo: la transición 3 → 2 da la línea roja del hidrógeno (656 nm).","Beispiel: Übergang 3 → 2 ergibt die rote Wasserstofflinie (656 nm).","Exemplo: a transição 3 → 2 dá a linha vermelha do hidrogênio (656 nm).","Пример: переход 3 → 2 даёт красную линию водорода (656 нм).")}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['W0']['naziv'] = N['W0']

teme.append({
 'id': 'raspad', 'simbol': 't½',
 'naziv': T("Radioaktivni raspad","Radioactive decay","Decadimento radioattivo","Désintégration radioactive","Desintegración radiactiva","Radioaktiver Zerfall","Decaimento radioativo","Радиоактивный распад"),
 'opis': T("Vreme poluraspada, aktivnost","Half-life, activity","Tempo di dimezzamento, attività","Demi-vie, activité","Semivida, actividad","Halbwertszeit, Aktivität","Meia-vida, atividade","Период полураспада, активность"),
 'kljucne_reci': T("radioaktivni raspad vreme poluraspada aktivnost bekerel konstanta raspada ugljenik 14 datiranje","radioactive decay half life activity becquerel decay constant carbon 14 dating","decadimento radioattivo tempo di dimezzamento attivita becquerel carbonio 14 datazione","desintegration radioactive demi vie activite becquerel carbone 14 datation","desintegracion radiactiva semivida actividad becquerel carbono 14 datacion","radioaktiver zerfall halbwertszeit aktivitat becquerel c14 datierung","decaimento radioativo meia vida atividade becquerel carbono 14 datacao","радиоактивный распад период полураспада активность беккерель углерод 14 датирование"),
 'formule': [
  F(T("Zakon raspada","Decay law","Legge del decadimento","Loi de décroissance","Ley de desintegración","Zerfallsgesetz","Lei do decaimento","Закон распада"),
    S(r"N(t) = N_0\, e^{-\lambda t} = N_0 \cdot 2^{-t/{tp}}, \quad {tp} = \frac{\ln 2}{\lambda}"),
    T("Posle svakog vremena poluraspada ostane polovina jezgara. Ugljenik-14: 5730 godina.","After each half-life half of the nuclei remain. Carbon-14: 5730 years.","Dopo ogni tempo di dimezzamento resta metà dei nuclei. Carbonio-14: 5730 anni.","Après chaque demi-vie, il reste la moitié des noyaux. Carbone 14 : 5730 ans.","Tras cada semivida queda la mitad de los núcleos. Carbono-14: 5730 años.","Nach jeder Halbwertszeit ist die Hälfte der Kerne übrig. C-14: 5730 Jahre.","Após cada meia-vida resta metade dos núcleos. Carbono-14: 5730 anos.","За каждый период полураспада остаётся половина ядер. Углерод-14: 5730 лет.")),
  F(T("Aktivnost","Activity","Attività","Activité","Actividad","Aktivität","Atividade","Активность"),
    r"A(t) = -\frac{dN}{dt} = \lambda N(t)",
    T("Broj raspada u sekundi; 1 Bq = 1 raspad u sekundi.","Number of decays per second; 1 Bq = 1 decay per second.","Numero di decadimenti al secondo; 1 Bq = 1 decadimento al secondo.","Nombre de désintégrations par seconde ; 1 Bq = 1 désintégration par seconde.","Número de desintegraciones por segundo; 1 Bq = 1 por segundo.","Zerfälle pro Sekunde; 1 Bq = 1 Zerfall pro Sekunde.","Número de decaimentos por segundo; 1 Bq = 1 por segundo.","Число распадов в секунду; 1 Бк = 1 распад в секунду.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'udeo': None, 't': 11460 * 3.15576e7, 'tp': 5730 * 3.15576e7, 'lr': None, 'A': None, 'N': 1e20},
                       {'t': 'god', 'tp': 'god', 'lr': '1/god'}),
  'jednacine': [
   {'latex': S(r"\dfrac{N}{N_0} = 2^{-t/{tp}}"), 'trazi': 'udeo', 'resenja': {'udeo': 'pow(2, -t/tp)', 't': '-tp*ln(udeo)/ln(2)', 'tp': '-t*ln(2)/ln(udeo)'},
    'napomene': {'t': T("Npr. starost nalaza: koliko je ugljenika-14 preostalo u odnosu na živo biće.","E.g. age of a find: how much carbon-14 remains compared to a living organism.","Es. età di un reperto: quanto carbonio-14 resta rispetto a un organismo vivo.","Ex. âge d’un objet : quelle part de carbone 14 reste par rapport à un être vivant.","P. ej., edad de un hallazgo: cuánto carbono-14 queda respecto a un ser vivo.","Z. B. Alter eines Fundes: wie viel C-14 im Vergleich zu einem Lebewesen übrig ist.","Ex.: idade de um achado: quanto carbono-14 resta em relação a um ser vivo.","Например, возраст находки: какая доля углерода-14 осталась по сравнению с живым организмом.")}},
   {'latex': S(r"{tp} = \dfrac{\ln 2}{\lambda}"), 'trazi': 'lr', 'resenja': {'lr': 'ln(2)/tp', 'tp': 'ln(2)/lr'}},
   {'latex': r"A = \lambda N", 'trazi': 'A', 'resenja': {'A': 'lr*N', 'lr': 'A/N', 'N': 'A/lr'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['lr']['pocetna'] = math.log(2) / (5730 * 3.15576e7)

teme.append({
 'id': 'slabljenje', 'simbol': 'μ',
 'naziv': T("Slabljenje zračenja","Attenuation of radiation","Attenuazione della radiazione","Atténuation du rayonnement","Atenuación de la radiación","Schwächung von Strahlung","Atenuação da radiação","Ослабление излучения"),
 'opis': T("Zaštita olovom, betonom, vodom","Shielding with lead, concrete, water","Schermatura con piombo, calcestruzzo, acqua","Protection par plomb, béton, eau","Blindaje de plomo, hormigón, agua","Abschirmung mit Blei, Beton, Wasser","Blindagem com chumbo, concreto, água","Защита свинцом, бетоном, водой"),
 'kljucne_reci': T("slabljenje zracenja apsorpcija gama zracenje zastita olovo debljina poluslabljenja koeficijent slabljenja","attenuation absorption gamma radiation shielding lead half value layer","attenuazione assorbimento radiazione gamma schermatura piombo spessore di dimezzamento","attenuation absorption rayonnement gamma protection plomb couche de demi attenuation","atenuacion absorcion radiacion gamma blindaje plomo capa hemirreductora","schwachung absorption gammastrahlung abschirmung blei halbwertsdicke","atenuacao absorcao radiacao gama blindagem chumbo camada semirredutora","ослабление поглощение гамма излучение защита свинец слой половинного ослабления"),
 'formule': [
  F(T("Zakon slabljenja","Attenuation law","Legge di attenuazione","Loi d’atténuation","Ley de atenuación","Schwächungsgesetz","Lei de atenuação","Закон ослабления"),
    r"j(x) = j_0\, e^{-\mu x} = j_0 \cdot 2^{-x/d_{1/2}}, \quad d_{1/2} = \frac{\ln 2}{\mu}",
    T("Svaki sloj debljine d₁/₂ prepolovi intenzitet. Gama zraci (1 MeV) u olovu: d₁/₂ ≈ 0,9 cm.","Each layer of thickness d₁/₂ halves the intensity. Gamma rays (1 MeV) in lead: d₁/₂ ≈ 0.9 cm.","Ogni strato di spessore d₁/₂ dimezza l’intensità. Raggi gamma (1 MeV) nel piombo: d₁/₂ ≈ 0,9 cm.","Chaque couche d’épaisseur d₁/₂ divise l’intensité par deux. Gamma (1 MeV) dans le plomb : d₁/₂ ≈ 0,9 cm.","Cada capa de espesor d₁/₂ reduce la intensidad a la mitad. Rayos gamma (1 MeV) en plomo: d₁/₂ ≈ 0,9 cm.","Jede Schicht der Dicke d₁/₂ halbiert die Intensität. Gammastrahlung (1 MeV) in Blei: d₁/₂ ≈ 0,9 cm.","Cada camada de espessura d₁/₂ reduz a intensidade à metade. Raios gama (1 MeV) no chumbo: d₁/₂ ≈ 0,9 cm.","Каждый слой толщиной d₁/₂ вдвое ослабляет излучение. Гамма (1 МэВ) в свинце: d₁/₂ ≈ 0,9 см.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'j': None, 'j0': 100, 'x': 0.05, 'dp': 0.009, 'mu': None}, {'x': 'cm', 'dp': 'cm', 'mu': '1/cm'}),
  'jednacine': [
   {'latex': r"j = j_0 \cdot 2^{-x/d_{1/2}}", 'trazi': 'j', 'resenja': {'j': 'j0*pow(2, -x/dp)', 'j0': 'j*pow(2, x/dp)', 'x': '-dp*ln(j/j0)/ln(2)', 'dp': '-x*ln(2)/ln(j/j0)'}},
   {'latex': r"d_{1/2} = \dfrac{\ln 2}{\mu}", 'trazi': 'mu', 'resenja': {'mu': 'ln(2)/dp', 'dp': 'ln(2)/mu'}},
  ]}
})

teme.append({
 'id': 'energija_veze', 'simbol': 'mc²',
 'naziv': T("Energija veze i nuklearne reakcije","Binding energy and nuclear reactions","Energia di legame e reazioni nucleari","Énergie de liaison et réactions nucléaires","Energía de enlace y reacciones nucleares","Bindungsenergie und Kernreaktionen","Energia de ligação e reações nucleares","Энергия связи и ядерные реакции"),
 'opis': T("E = mc², defekt mase","E = mc², mass defect","E = mc², difetto di massa","E = mc², défaut de masse","E = mc², defecto de masa","E = mc², Massendefekt","E = mc², defeito de massa","E = mc², дефект массы"),
 'kljucne_reci': T("energija veze defekt mase e mc2 ajnstajn nuklearna reakcija fisija fuzija jezgro","binding energy mass defect e mc2 einstein nuclear reaction fission fusion nucleus","energia di legame difetto di massa e mc2 reazione nucleare fissione fusione","energie de liaison defaut de masse e mc2 reaction nucleaire fission fusion","energia de enlace defecto de masa e mc2 reaccion nuclear fision fusion","bindungsenergie massendefekt e mc2 kernreaktion kernspaltung kernfusion","energia de ligacao defeito de massa e mc2 reacao nuclear fissao fusao","энергия связи дефект массы e mc2 ядерная реакция деление синтез"),
 'formule': [
  F(T("Ekvivalencija mase i energije","Mass–energy equivalence","Equivalenza massa-energia","Équivalence masse-énergie","Equivalencia masa-energía","Äquivalenz von Masse und Energie","Equivalência massa-energia","Эквивалентность массы и энергии"),
    r"E = m c^2, \quad 1\ \mathrm{u} \cdot c^2 = 931{,}5\ \mathrm{MeV}",
    T("Mala razlika u masi odgovara velikoj energiji.","A small mass difference corresponds to a large energy.","Una piccola differenza di massa corrisponde a molta energia.","Une petite différence de masse correspond à une grande énergie.","Una pequeña diferencia de masa corresponde a mucha energía.","Ein kleiner Massenunterschied entspricht großer Energie.","Uma pequena diferença de massa corresponde a muita energia.","Малой разнице масс соответствует большая энергия.")),
  F(T("Energija veze jezgra","Nuclear binding energy","Energia di legame del nucleo","Énergie de liaison du noyau","Energía de enlace del núcleo","Bindungsenergie des Kerns","Energia de ligação do núcleo","Энергия связи ядра"),
    r"W_v = Z m_p c^2 + N m_n c^2 - m_j c^2",
    T("Z je broj protona, N broj neutrona, m_j masa jezgra. Helijum-4: oko 28,3 MeV.","Z is the number of protons, N of neutrons, m_j the nuclear mass. Helium-4: about 28.3 MeV.","Z protoni, N neutroni, m_j massa del nucleo. Elio-4: circa 28,3 MeV.","Z protons, N neutrons, m_j masse du noyau. Hélium 4 : environ 28,3 MeV.","Z protones, N neutrones, m_j masa del núcleo. Helio-4: unos 28,3 MeV.","Z Protonen, N Neutronen, m_j Kernmasse. Helium-4: etwa 28,3 MeV.","Z prótons, N nêutrons, m_j massa do núcleo. Hélio-4: cerca de 28,3 MeV.","Z — число протонов, N — нейтронов, m_j — масса ядра. Гелий-4: около 28,3 МэВ.")),
  F(T("Energija reakcije","Reaction energy","Energia della reazione","Énergie de réaction","Energía de la reacción","Reaktionsenergie","Energia da reação","Энергия реакции"),
    r"W_r = m_j c^2 - m_A c^2 - m_B c^2",
    T("Za raspad jezgra j na A i B; pozitivna vrednost znači da se energija oslobađa.","For a nucleus j splitting into A and B; a positive value means energy is released.","Per un nucleo j che si scinde in A e B; un valore positivo indica energia liberata.","Pour un noyau j se scindant en A et B ; une valeur positive signifie de l’énergie libérée.","Para un núcleo j que se divide en A y B; un valor positivo significa energía liberada.","Für den Zerfall eines Kerns j in A und B; ein positiver Wert bedeutet freigesetzte Energie.","Para um núcleo j que se divide em A e B; valor positivo significa energia liberada.","Для распада ядра j на A и B; положительное значение — энергия выделяется.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Em': None, 'dm': 0.0303 * U, 'c': C0, 'Wv': None, 'Z': 2, 'Nn': 2, 'mp': MP_U * U, 'mn': MN_U * U, 'mj': 4.001506179127 * U},
                       {'dm': 'u', 'Em': 'MeV', 'Wv': 'MeV', 'mp': 'u', 'mn': 'u', 'mj': 'u'}),
  'jednacine': [
   {'latex': r"E = \Delta m\, c^2", 'trazi': 'Em', 'resenja': {'Em': 'dm*c*c', 'dm': 'Em/(c*c)'}},
   {'latex': r"W_v = (Z m_p + N m_n - m_j)\, c^2", 'trazi': 'Wv',
    'resenja': {'Wv': '(Z*mp + Nn*mn - mj)*c*c', 'mj': 'Z*mp + Nn*mn - Wv/(c*c)'},
    'napomene': {'Wv': T("Podrazumevano: jezgro helijuma-4 (2 protona, 2 neutrona).","Default: helium-4 nucleus (2 protons, 2 neutrons).","Predefinito: nucleo di elio-4 (2 protoni, 2 neutroni).","Par défaut : noyau d’hélium 4 (2 protons, 2 neutrons).","Por defecto: núcleo de helio-4 (2 protones, 2 neutrones).","Voreinstellung: Helium-4-Kern (2 Protonen, 2 Neutronen).","Padrão: núcleo de hélio-4 (2 prótons, 2 nêutrons).","По умолчанию: ядро гелия-4 (2 протона, 2 нейтрона).")}},
  ]}
})

FUNK = {'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'pow', 'ln', 'PI', 'kvPoz', 'abs'}
for t in teme:
    vel = t['kalkulator']['velicine']
    for j in t['kalkulator']['jednacine']:
        koriscene = list(j['resenja'])
        for izraz in j['resenja'].values():
            for ime in re.findall(r'[A-Za-z_][A-Za-z0-9_]*', izraz):
                if ime not in FUNK and ime not in koriscene and not ime.isdigit(): koriscene.append(ime)
        if len(koriscene) > len(j['resenja']): j['promenljive'] = koriscene
        for k in (j.get('promenljive') or j['resenja']):
            assert k in vel, (t['id'], k)
    for f in t['formule']:
        o = f.get('objasnjenje')
        if isinstance(o, dict):
            for jj in J: o[jj] = o[jj].replace('λ_g', 'λg').replace('r_B', 'rʙ').replace('m_j', 'mⱼ')

out = {'oblast': 'moderna_fizika', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
