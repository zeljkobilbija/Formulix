# Generiše assets/oblasti/energija.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']
PI = math.pi

# Oznake po jeziku: rad, kinetička, potencijalna, elastična energija
RAD = dict(sr='A', en='W', it='L', fr='W', es='W', de='W', pt='W', ru='A')
EK = dict(sr='E_k', en='E_k', it='E_c', fr='E_c', es='E_c', de=r'E_{\mathrm{kin}}', pt='E_c', ru=r'E_{\text{к}}')
EP = dict(sr='E_p', en='E_p', it='E_p', fr='E_p', es='E_p', de=r'E_{\mathrm{pot}}', pt='E_p', ru=r'E_{\text{п}}')
EE = dict(sr=r'E_{\mathrm{el}}', en=r'E_{\mathrm{el}}', it=r'E_{\mathrm{el}}', fr=r'E_{\mathrm{el}}', es=r'E_{\mathrm{el}}', de=r'E_{\mathrm{Spann}}', pt=r'E_{\mathrm{el}}', ru=r'E_{\text{упр}}')
def S(f):
    """LaTeX šablon sa {A}, {Ek}, {Ep}, {Ee} → po jeziku."""
    return LJ(lambda j: f.replace('{A}', RAD[j]).replace('{Ek}', EK[j]).replace('{Ep}', EP[j]).replace('{Ee}', EE[j]))

N = {
 'A': T("rad","work","lavoro","travail","trabajo","Arbeit","trabalho","работа"),
 'F': T("sila","force","forza","force","fuerza","Kraft","força","сила"),
 's': T("pređeni put","displacement","spostamento","déplacement","desplazamiento","Weg","deslocamento","перемещение"),
 'fi': T("ugao između sile i puta","angle between force and path","angolo tra forza e spostamento","angle entre force et déplacement","ángulo entre fuerza y desplazamiento","Winkel zwischen Kraft und Weg","ângulo entre força e deslocamento","угол между силой и перемещением"),
 'p': T("pritisak","pressure","pressione","pression","presión","Druck","pressão","давление"),
 'dV': T("promena zapremine","change in volume","variazione di volume","variation de volume","variación de volumen","Volumenänderung","variação de volume","изменение объёма"),
 'Ek': T("kinetička energija","kinetic energy","energia cinetica","énergie cinétique","energía cinética","kinetische Energie","energia cinética","кинетическая энергия"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'v': T("brzina","velocity","velocità","vitesse","velocidad","Geschwindigkeit","velocidade","скорость"),
 'v0': T("početna brzina","initial velocity","velocità iniziale","vitesse initiale","velocidad inicial","Anfangsgeschwindigkeit","velocidade inicial","начальная скорость"),
 'Ep': T("potencijalna energija","potential energy","energia potenziale","énergie potentielle","energía potencial","potentielle Energie","energia potencial","потенциальная энергия"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'h': T("visina","height","altezza","hauteur","altura","Höhe","altura","высота"),
 'Ee': T("elastična energija","elastic energy","energia elastica","énergie élastique","energía elástica","Spannenergie","energia elástica","энергия упругой деформации"),
 'k': T("konstanta opruge","spring constant","costante elastica","raideur du ressort","constante del resorte","Federkonstante","constante elástica","жёсткость пружины"),
 'x': T("izduženje opruge","spring extension","allungamento della molla","allongement du ressort","alargamiento del resorte","Auslenkung der Feder","deformação da mola","удлинение пружины"),
 'Epg': T("gravitaciona potencijalna energija","gravitational potential energy","energia potenziale gravitazionale","énergie potentielle de gravitation","energía potencial gravitatoria","Gravitationsenergie","energia potencial gravitacional","гравитационная потенциальная энергия"),
 'Gk': T("gravitaciona konstanta","gravitational constant","costante di gravitazione","constante gravitationnelle","constante de gravitación","Gravitationskonstante","constante gravitacional","гравитационная постоянная"),
 'M': T("masa planete","mass of the planet","massa del pianeta","masse de la planète","masa del planeta","Masse des Planeten","massa do planeta","масса планеты"),
 'r': T("rastojanje od središta planete","distance from the planet’s centre","distanza dal centro del pianeta","distance au centre de la planète","distancia al centro del planeta","Abstand zum Planetenmittelpunkt","distância ao centro do planeta","расстояние до центра планеты"),
 'Fk': T("sila kočenja","braking force","forza frenante","force de freinage","fuerza de frenado","Bremskraft","força de frenagem","сила торможения"),
 'sz': T("zaustavni put","stopping distance","spazio di frenata","distance de freinage","distancia de frenado","Bremsweg","distância de frenagem","тормозной путь"),
 'P': T("snaga","power","potenza","puissance","potencia","Leistung","potência","мощность"),
 't': T("vreme","time","tempo","temps","tiempo","Zeit","tempo","время"),
 'eta': T("stepen korisnog dejstva","efficiency","rendimento","rendement","rendimiento","Wirkungsgrad","rendimento","коэффициент полезного действия"),
 'Pk': T("korisna snaga","useful power","potenza utile","puissance utile","potencia útil","Nutzleistung","potência útil","полезная мощность"),
 'Pu': T("uložena snaga","input power","potenza assorbita","puissance absorbée","potencia absorbida","zugeführte Leistung","potência fornecida","затраченная мощность"),
}
OZ = {'A': S('{A}'), 'F': 'F', 's': 's', 'fi': r'\varphi', 'p': 'p', 'dV': r'\Delta V', 'Ek': S('{Ek}'), 'm': 'm', 'v': 'v',
      'v0': 'v_0', 'Ep': S('{Ep}'), 'g': 'g', 'h': 'h', 'Ee': S('{Ee}'), 'k': 'k', 'x': 'x', 'Epg': S('{Ep}'), 'Gk': 'G',
      'M': 'M', 'r': 'r', 'Fk': 'F', 'sz': 's', 'P': 'P', 't': 't', 'eta': r'\eta', 'Pk': r'P_{\mathrm{k}}', 'Pu': r'P_{\mathrm{u}}'}
# Korisna/uložena: indeksi po jeziku
OZ['Pk'] = LJ(lambda j: {'sr': r'P_{\mathrm{k}}', 'en': r'P_{\mathrm{out}}', 'it': r'P_{\mathrm{u}}', 'fr': r'P_{\mathrm{u}}', 'es': r'P_{\mathrm{u}}', 'de': r'P_{\mathrm{ab}}', 'pt': r'P_{\mathrm{u}}', 'ru': r'P_{\text{пол}}'}[j])
OZ['Pu'] = LJ(lambda j: {'sr': r'P_{\mathrm{u}}', 'en': r'P_{\mathrm{in}}', 'it': r'P_{\mathrm{a}}', 'fr': r'P_{\mathrm{a}}', 'es': r'P_{\mathrm{a}}', 'de': r'P_{\mathrm{zu}}', 'pt': r'P_{\mathrm{t}}', 'ru': r'P_{\text{затр}}'}[j])
PK = {j: (OZ['Pk'][j] if isinstance(OZ['Pk'], dict) else OZ['Pk']) for j in J}
PU = {j: (OZ['Pu'][j] if isinstance(OZ['Pu'], dict) else OZ['Pu']) for j in J}

VRSTA = {'A': 'energija', 'F': 'sila', 's': 'duzina', 'fi': 'ugao', 'p': 'pritisak', 'dV': 'zapremina', 'Ek': 'energija',
         'm': 'masa', 'v': 'brzina', 'v0': 'brzina', 'Ep': 'energija', 'g': 'ubrzanje', 'h': 'duzina', 'Ee': 'energija',
         'k': 'krutost', 'x': 'duzina', 'Epg': 'energija', 'Gk': 'gravKonst', 'M': 'masa', 'r': 'duzina', 'Fk': 'sila',
         'sz': 'duzina', 'P': 'snaga', 't': 'vreme', 'eta': 'udeo', 'Pk': 'snaga', 'Pu': 'snaga'}
POZ = {'m', 'g', 'k', 'Gk', 'M', 'r', 't', 'Pu', 'Fk', 'sz', 'eta'}
NENEG = {'Ek', 'Ee', 'v'}

def velicine(pocetne, jed={}):
    out = {}
    for k, p in pocetne.items():
        d = {'oznaka': OZ[k], 'naziv': N[k], 'vrsta': VRSTA[k]}
        if p is not None: d['pocetna'] = p
        if k in jed: d['jed'] = jed[k]
        if k in POZ: d['poz'] = True
        if k in NENEG: d['nenegativna'] = True
        out[k] = d
    return out
def F(naslov, latex, obj):
    return {'naslov': naslov, 'latex': latex, 'objasnjenje': obj}

def strela(x1, y1, x2, y2, klasa='lik-l', duz=11, sir=5):
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    bx, by = x2 - ux * duz, y2 - uy * duz
    px, py = -uy * sir, ux * sir
    return (f'<line class="{klasa}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>'
            f'<path class="tac" d="M{x2:.1f},{y2:.1f} L{bx+px:.1f},{by+py:.1f} L{bx-px:.1f},{by-py:.1f} Z"/>')

def crtez_rad():
    s = '<svg viewBox="0 0 300 170" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<line class="osa" x1="10" y1="120" x2="290" y2="120"/>'
    s += '<rect class="lik2" x="40" y="80" width="60" height="40" rx="3"/>'
    s += '<rect class="lik" x="190" y="80" width="60" height="40" rx="3" stroke-dasharray="6 5" fill-opacity="0.35"/>'
    a = math.radians(35); cx, cy = 100, 100
    s += strela(cx, cy, cx + 80 * math.cos(a), cy - 80 * math.sin(a))
    s += f'<text x="{cx + 80*math.cos(a) + 4:.1f}" y="{cy - 80*math.sin(a) + 2:.1f}">F</text>'
    s += f'<line class="pom" x1="{cx}" y1="{cy}" x2="{cx+86}" y2="{cy}"/>'
    s += f'<path class="ugao" d="M{cx+34},{cy} A34,34 0 0,0 {cx+34*math.cos(a):.1f},{cy-34*math.sin(a):.1f}"/>'
    s += f'<text x="{cx+40}" y="{cy-6}">φ</text>'
    s += strela(70, 145, 220, 145)
    s += '<line class="osa" x1="70" y1="138" x2="70" y2="152"/>'
    s += '<text x="140" y="166">s</text>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'rad', 'simbol': 'A',
 'naziv': T("Mehanički rad","Work","Lavoro","Travail","Trabajo","Arbeit","Trabalho","Механическая работа"),
 'opis': T("Rad sile, rad gasa","Work of a force, work of a gas","Lavoro di una forza e di un gas","Travail d’une force, d’un gaz","Trabajo de una fuerza y de un gas","Arbeit einer Kraft, Volumenarbeit","Trabalho de uma força e de um gás","Работа силы, работа газа"),
 'kljucne_reci': T("rad sile mehanicki rad dzul ugao rad gasa","work of a force joule angle work done by gas","lavoro di una forza joule lavoro di un gas","travail d une force joule travail d un gaz","trabajo de una fuerza julio trabajo de un gas","arbeit kraft weg joule volumenarbeit","trabalho de uma forca joule trabalho de um gas","работа силы джоуль работа газа"),
 'crtez': crtez_rad(),
 'formule': [
  F(T("Rad sile","Work of a force","Lavoro di una forza","Travail d’une force","Trabajo de una fuerza","Arbeit einer Kraft","Trabalho de uma força","Работа силы"),
    S(r"{A} = \vec F \cdot \vec s = F s \cos\varphi"),
    T("Samo komponenta sile u smeru kretanja vrši rad; 1 J = 1 N·m. Za φ = 90° rad je nula, a za φ > 90° negativan (npr. trenje).","Only the force component along the motion does work; 1 J = 1 N·m. For φ = 90° the work is zero; for φ > 90° it is negative (e.g. friction).","Solo la componente della forza lungo il moto compie lavoro; 1 J = 1 N·m. Per φ = 90° il lavoro è nullo, per φ > 90° è negativo (es. attrito).","Seule la composante de la force dans le sens du mouvement travaille ; 1 J = 1 N·m. Pour φ = 90° le travail est nul, pour φ > 90° il est négatif (frottement).","Solo la componente de la fuerza en la dirección del movimiento realiza trabajo; 1 J = 1 N·m. Con φ = 90° es nulo y con φ > 90° negativo (rozamiento).","Nur die Kraftkomponente in Bewegungsrichtung verrichtet Arbeit; 1 J = 1 N·m. Bei φ = 90° ist sie null, bei φ > 90° negativ (z. B. Reibung).","Só a componente da força na direção do movimento realiza trabalho; 1 J = 1 N·m. Para φ = 90° é nulo e para φ > 90° negativo (atrito).","Работу совершает только составляющая силы вдоль перемещения; 1 Дж = 1 Н·м. При φ = 90° работа равна нулю, при φ > 90° отрицательна (трение).")),
  F(T("Rad gasa (stalan pritisak)","Work of a gas (constant pressure)","Lavoro di un gas (pressione costante)","Travail d’un gaz (pression constante)","Trabajo de un gas (presión constante)","Volumenarbeit (konstanter Druck)","Trabalho de um gás (pressão constante)","Работа газа (постоянное давление)"),
    S(r"{A} = -p\,\Delta V"),
    T("Rad koji okolina izvrši nad gasom; kada se gas širi (ΔV > 0), rad je negativan, jer gas predaje energiju okolini.","Work done on the gas by the surroundings; when the gas expands (ΔV > 0) it is negative, since the gas gives energy away.","Lavoro compiuto sul gas dall’esterno; quando il gas si espande (ΔV > 0) è negativo.","Travail reçu par le gaz ; lors d’une détente (ΔV > 0) il est négatif.","Trabajo realizado sobre el gas; cuando el gas se expande (ΔV > 0) es negativo.","Am Gas verrichtete Arbeit; dehnt sich das Gas aus (ΔV > 0), ist sie negativ.","Trabalho realizado sobre o gás; quando ele se expande (ΔV > 0) é negativo.","Работа внешних сил над газом; при расширении (ΔV > 0) она отрицательна.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'A': None, 'F': 100, 's': 10, 'fi': PI / 6, 'p': 1e5, 'dV': 0.002}, {'fi': '°', 'p': 'kPa', 'dV': 'L'}),
  'jednacine': [
   {'latex': S(r"{A} = F s \cos\varphi"), 'trazi': 'A',
    'resenja': {'A': 'F*s*cos(fi)', 'F': 'A/(s*cos(fi))', 's': 'A/(F*cos(fi))', 'fi': 'acos(A/(F*s))'}},
   {'latex': S(r"{A} = p\,\Delta V"), 'trazi': 'A', 'resenja': {'A': 'p*dV', 'p': 'A/dV', 'dV': 'A/p'},
    'napomene': {'A': T("Prikazan je rad koji gas izvrši pri širenju (bez znaka minus).","Shown is the work done by the gas as it expands (without the minus sign).","È mostrato il lavoro compiuto dal gas nell’espansione (senza segno meno).","Travail fourni par le gaz lors de la détente (sans le signe moins).","Se muestra el trabajo realizado por el gas al expandirse (sin signo menos).","Angezeigt ist die vom Gas bei der Ausdehnung verrichtete Arbeit (ohne Minuszeichen).","É mostrado o trabalho realizado pelo gás na expansão (sem sinal de menos).","Показана работа самого газа при расширении (без знака минус).")}},
  ]}
})

teme.append({
 'id': 'kineticka', 'simbol': 'Eₖ',
 'naziv': T("Kinetička energija","Kinetic energy","Energia cinetica","Énergie cinétique","Energía cinética","Kinetische Energie","Energia cinética","Кинетическая энергия"),
 'opis': T("Energija kretanja","Energy of motion","Energia del movimento","Énergie du mouvement","Energía del movimiento","Bewegungsenergie","Energia do movimento","Энергия движения"),
 'kljucne_reci': T("kineticka energija energija kretanja brzina masa","kinetic energy energy of motion speed mass","energia cinetica movimento velocita massa","energie cinetique mouvement vitesse masse","energia cinetica movimiento velocidad masa","kinetische energie bewegungsenergie geschwindigkeit masse","energia cinetica movimento velocidade massa","кинетическая энергия движения скорость масса"),
 'formule': [
  F(T("Kinetička energija","Kinetic energy","Energia cinetica","Énergie cinétique","Energía cinética","Kinetische Energie","Energia cinética","Кинетическая энергия"),
    S(r"{Ek} = \frac{m v^2}{2}"),
    T("Dvostruko veća brzina znači četiri puta veću energiju; zato zaustavni put brzo raste sa brzinom.","Doubling the speed quadruples the energy; that is why stopping distance grows fast with speed.","Velocità doppia significa energia quadrupla; per questo lo spazio di frenata cresce in fretta.","Une vitesse doublée quadruple l’énergie ; c’est pourquoi la distance de freinage croît vite.","El doble de velocidad cuadruplica la energía; por eso la distancia de frenado crece rápido.","Doppelte Geschwindigkeit bedeutet vierfache Energie; daher wächst der Bremsweg so schnell.","Velocidade dobrada quadruplica a energia; por isso a distância de frenagem cresce rápido.","Вдвое большая скорость — вчетверо большая энергия; поэтому тормозной путь быстро растёт.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ek': None, 'm': 1000, 'v': 50 / 3.6}, {'v': 'km/h', 'Ek': 'kJ'}),
  'jednacine': [
   {'latex': S(r"{Ek} = \dfrac{m v^2}{2}"), 'trazi': 'Ek', 'resenja': {'Ek': 'm*v*v/2', 'm': '2*Ek/(v*v)', 'v': 'sqrt(2*Ek/m)'}},
  ]}
})

teme.append({
 'id': 'potencijalna', 'simbol': 'Eₚ',
 'naziv': T("Potencijalna energija","Potential energy","Energia potenziale","Énergie potentielle","Energía potencial","Potentielle Energie","Energia potencial","Потенциальная энергия"),
 'opis': T("Visina, opruga, gravitacija","Height, spring, gravitation","Altezza, molla, gravitazione","Hauteur, ressort, gravitation","Altura, resorte, gravitación","Höhe, Feder, Gravitation","Altura, mola, gravitação","Высота, пружина, тяготение"),
 'kljucne_reci': T("potencijalna energija visina elasticna energija opruga gravitaciona","potential energy height elastic energy spring gravitational","energia potenziale altezza elastica molla gravitazionale","energie potentielle hauteur elastique ressort gravitation","energia potencial altura elastica resorte gravitatoria","potentielle energie lageenergie hohe spannenergie feder","energia potencial altura elastica mola gravitacional","потенциальная энергия высота упругая пружина гравитационная"),
 'formule': [
  F(T("U blizini Zemlje","Near the Earth’s surface","Vicino alla superficie terrestre","Près de la surface terrestre","Cerca de la superficie terrestre","Nahe der Erdoberfläche","Perto da superfície terrestre","Вблизи поверхности Земли"),
    S(r"{Ep} = m g h"),
    T("h je visina iznad izabranog nultog nivoa (npr. poda).","h is the height above a chosen zero level (e.g. the floor).","h è l’altezza sopra un livello zero scelto (es. il pavimento).","h est la hauteur au-dessus d’un niveau zéro choisi (le sol).","h es la altura sobre un nivel cero elegido (el suelo).","h ist die Höhe über einem gewählten Nullniveau (z. B. Boden).","h é a altura acima de um nível zero escolhido (o chão).","h — высота над выбранным нулевым уровнем (например, полом).")),
  F(T("Elastična energija opruge","Elastic energy of a spring","Energia elastica di una molla","Énergie élastique d’un ressort","Energía elástica de un resorte","Spannenergie einer Feder","Energia elástica de uma mola","Энергия сжатой пружины"),
    S(r"{Ee} = \frac{k x^2}{2}"),
    T("Energija istegnute ili sabijene opruge; x je izduženje u odnosu na neopterećenu oprugu.","Energy of a stretched or compressed spring; x is the extension from its relaxed length.","Energia di una molla allungata o compressa; x è la deformazione dalla lunghezza a riposo.","Énergie d’un ressort étiré ou comprimé ; x est l’allongement par rapport au repos.","Energía de un resorte estirado o comprimido; x es la deformación desde el reposo.","Energie einer gedehnten oder gestauchten Feder; x ist die Auslenkung.","Energia de uma mola esticada ou comprimida; x é a deformação a partir do repouso.","Энергия растянутой или сжатой пружины; x — деформация.")),
  F(T("Gravitaciona (daleko od Zemlje)","Gravitational (far from the Earth)","Gravitazionale (lontano dalla Terra)","De gravitation (loin de la Terre)","Gravitatoria (lejos de la Tierra)","Gravitation (fern der Erde)","Gravitacional (longe da Terra)","Гравитационная (вдали от Земли)"),
    S(r"{Ep} = -G\,\frac{m M}{r}"),
    T("Nula je u beskonačnosti, pa je energija negativna; koristi se za satelite i planete.","Zero at infinity, so the energy is negative; used for satellites and planets.","È nulla all’infinito, quindi negativa; si usa per satelliti e pianeti.","Nulle à l’infini, donc négative ; utilisée pour satellites et planètes.","Es cero en el infinito, por eso negativa; se usa para satélites y planetas.","Im Unendlichen null, daher negativ; für Satelliten und Planeten.","É zero no infinito, por isso negativa; usada para satélites e planetas.","Равна нулю на бесконечности, поэтому отрицательна; для спутников и планет.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ep': None, 'm': 2, 'g': 9.81, 'h': 10, 'Ee': None, 'k': 500, 'x': 0.1, 'Epg': None, 'Gk': 6.6743e-11, 'M': 5.972e24, 'r': 6.771e6},
                       {'x': 'cm', 'r': 'km'}),
  'jednacine': [
   {'latex': S(r"{Ep} = m g h"), 'trazi': 'Ep', 'resenja': {'Ep': 'm*g*h', 'm': 'Ep/(g*h)', 'h': 'Ep/(m*g)', 'g': 'Ep/(m*h)'}},
   {'latex': S(r"{Ee} = \dfrac{k x^2}{2}"), 'trazi': 'Ee', 'resenja': {'Ee': 'k*x*x/2', 'k': '2*Ee/(x*x)', 'x': 'sqrt(2*Ee/k)'}},
   {'latex': S(r"{Ep} = -G \dfrac{m M}{r}"), 'trazi': 'Epg', 'promenljive': ['Epg', 'Gk', 'm', 'M', 'r'],
    'resenja': {'Epg': '-Gk*m*M/r', 'm': '-Epg*r/(Gk*M)', 'r': '-Gk*m*M/Epg'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['Epg']['oznaka'] = S('{Ep}')

teme.append({
 'id': 'odrzanje', 'simbol': 'E',
 'naziv': T("Zakon održanja energije","Conservation of energy","Conservazione dell’energia","Conservation de l’énergie","Conservación de la energía","Energieerhaltung","Conservação da energia","Закон сохранения энергии"),
 'opis': T("Rad i promena energije","Work and change of energy","Lavoro e variazione di energia","Travail et variation d’énergie","Trabajo y variación de energía","Arbeit und Energieänderung","Trabalho e variação de energia","Работа и изменение энергии"),
 'kljucne_reci': T("zakon odrzanja energije mehanicka energija rad promena energije zaustavni put kocenje","conservation of energy mechanical energy work energy theorem stopping distance braking","conservazione energia meccanica teorema lavoro energia frenata","conservation energie mecanique theoreme energie cinetique freinage","conservacion energia mecanica teorema trabajo energia frenado","energieerhaltung mechanische energie arbeitssatz bremsweg","conservacao energia mecanica teorema trabalho energia frenagem","закон сохранения энергии механическая энергия работа торможение тормозной путь"),
 'formule': [
  F(T("Rad i promena energije","Work and change of energy","Lavoro e variazione di energia","Travail et variation d’énergie","Trabajo y variación de energía","Arbeit und Energieänderung","Trabalho e variação de energia","Работа и изменение энергии"),
    S(r"{A} = \Delta {Ek} + \Delta {Ep} + \Delta {Ee}"),
    T("Rad spoljašnjih sila (bez sile teže i opruge) jednak je promeni ukupne mehaničke energije.","Work of external forces (other than gravity and springs) equals the change in total mechanical energy.","Il lavoro delle forze esterne (esclusi peso e molle) è uguale alla variazione dell’energia meccanica.","Le travail des forces extérieures (hors poids et ressorts) égale la variation de l’énergie mécanique.","El trabajo de las fuerzas externas (sin peso ni resortes) es igual a la variación de la energía mecánica.","Die Arbeit äußerer Kräfte (außer Gewicht und Federn) ist gleich der Änderung der mechanischen Energie.","O trabalho das forças externas (exceto peso e molas) é igual à variação da energia mecânica.","Работа внешних сил (кроме силы тяжести и упругости) равна изменению механической энергии.")),
  F(T("Bez trenja","Without friction","Senza attrito","Sans frottement","Sin rozamiento","Ohne Reibung","Sem atrito","Без трения"),
    S(r"\frac{m v_0^2}{2} + m g h_0 = \frac{m v^2}{2} + m g h, \quad v = \sqrt{v_0^2 + 2 g\,(h_0 - h)}"),
    T("Mehanička energija se ne menja; brzina zavisi samo od razlike visina, a ne od oblika putanje.","Mechanical energy is constant; speed depends only on the height difference, not on the path.","L’energia meccanica si conserva; la velocità dipende solo dal dislivello, non dal percorso.","L’énergie mécanique se conserve ; la vitesse ne dépend que de la dénivellation, pas du chemin.","La energía mecánica se conserva; la velocidad depende solo del desnivel, no del camino.","Die mechanische Energie bleibt erhalten; die Geschwindigkeit hängt nur vom Höhenunterschied ab.","A energia mecânica se conserva; a velocidade depende só do desnível, não do caminho.","Механическая энергия сохраняется; скорость зависит только от разности высот, а не от пути.")),
  F(T("Zaustavni put","Stopping distance","Spazio di frenata","Distance de freinage","Distancia de frenado","Bremsweg","Distância de frenagem","Тормозной путь"),
    r"F\,s = \frac{m v^2}{2}",
    T("Sila kočenja na putu s troši celu kinetičku energiju.","The braking force over distance s removes all the kinetic energy.","La forza frenante sullo spazio s dissipa tutta l’energia cinetica.","La force de freinage sur la distance s dissipe toute l’énergie cinétique.","La fuerza de frenado a lo largo de s disipa toda la energía cinética.","Die Bremskraft auf dem Weg s baut die gesamte kinetische Energie ab.","A força de frenagem ao longo de s dissipa toda a energia cinética.","Сила торможения на пути s гасит всю кинетическую энергию.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'v': None, 'v0': 0, 'g': 9.81, 'h': 5, 'sz': None, 'Fk': 8000, 'm': 1000, 'vk': 50 / 3.6} if False else
                       {'v': None, 'v0': 0, 'g': 9.81, 'h': 5, 'sz': None, 'Fk': 8000, 'm': 1000}, {'sz': 'm'}),
  'jednacine': [
   {'latex': r"v = \sqrt{v_0^2 + 2 g h}", 'trazi': 'v',
    'resenja': {'v': 'sqrt(v0*v0 + 2*g*h)', 'v0': 'sqrt(v*v - 2*g*h)', 'h': '(v*v - v0*v0)/(2*g)', 'g': '(v*v - v0*v0)/(2*h)'},
    'napomene': {'v': T("h je visinska razlika za koju se telo spustilo (bez trenja).","h is the height the body has dropped (no friction).","h è il dislivello di cui il corpo è sceso (senza attrito).","h est la hauteur de descente (sans frottement).","h es la altura que ha descendido (sin rozamiento).","h ist der Höhenunterschied nach unten (ohne Reibung).","h é a altura que o corpo desceu (sem atrito).","h — высота, на которую тело опустилось (без трения).")}},
   {'latex': r"F s = \dfrac{m v^2}{2}", 'trazi': 'sz',
    'resenja': {'sz': 'm*v*v/(2*Fk)', 'Fk': 'm*v*v/(2*sz)', 'm': '2*Fk*sz/(v*v)', 'v': 'sqrt(2*Fk*sz/m)'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['v']['pocetna'] = 50 / 3.6
teme[-1]['kalkulator']['velicine']['v']['jed'] = 'km/h'
teme[-1]['kalkulator']['velicine']['h']['naziv'] = T("visinska razlika","height difference","dislivello","dénivellation","desnivel","Höhenunterschied","desnível","разность высот")

teme.append({
 'id': 'snaga', 'simbol': 'P',
 'naziv': T("Snaga i stepen korisnog dejstva","Power and efficiency","Potenza e rendimento","Puissance et rendement","Potencia y rendimiento","Leistung und Wirkungsgrad","Potência e rendimento","Мощность и КПД"),
 'opis': T("Vat, kilovat-sat, η","Watt, kilowatt-hour, η","Watt, kilowattora, η","Watt, kilowattheure, η","Vatio, kilovatio-hora, η","Watt, Kilowattstunde, η","Watt, quilowatt-hora, η","Ватт, киловатт-час, КПД"),
 'kljucne_reci': T("snaga vat kilovat cas stepen korisnog dejstva efikasnost motor potrosnja struje","power watt kilowatt hour efficiency engine motor energy consumption","potenza watt kilowattora rendimento efficienza motore consumo","puissance watt kilowattheure rendement moteur consommation","potencia vatio kilovatio hora rendimiento eficiencia motor consumo","leistung watt kilowattstunde wirkungsgrad motor verbrauch","potencia watt quilowatt hora rendimento eficiencia motor consumo","мощность ватт киловатт час кпд двигатель расход энергии"),
 'formule': [
  F(T("Snaga","Power","Potenza","Puissance","Potencia","Leistung","Potência","Мощность"),
    S(r"P = \frac{{A}}{\Delta t} = \vec F \cdot \vec v = F v \cos\varphi"),
    T("Rad izvršen u jedinici vremena; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Work done per unit time; 1 W = 1 J/s. 1 kWh = 3.6 MJ.","Lavoro compiuto nell’unità di tempo; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Travail effectué par unité de temps ; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Trabajo realizado por unidad de tiempo; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Arbeit pro Zeiteinheit; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Trabalho realizado por unidade de tempo; 1 W = 1 J/s. 1 kWh = 3,6 MJ.","Работа за единицу времени; 1 Вт = 1 Дж/с. 1 кВт·ч = 3,6 МДж.")),
  F(T("Stepen korisnog dejstva","Efficiency","Rendimento","Rendement","Rendimiento","Wirkungsgrad","Rendimento","Коэффициент полезного действия"),
    LJ(lambda j: r"\eta = \frac{%s}{%s}" % (PK[j], PU[j])),
    T("Koliki deo uložene snage (energije) se korisno iskoristi; uvek je manji od 1 (100 %).","Fraction of the input power (energy) that is usefully used; always less than 1 (100 %).","Frazione della potenza (energia) assorbita che viene usata utilmente; sempre minore di 1 (100 %).","Part de la puissance (énergie) absorbée qui est utile ; toujours inférieur à 1 (100 %).","Fracción de la potencia (energía) absorbida que se aprovecha; siempre menor que 1 (100 %).","Anteil der zugeführten Leistung (Energie), der genutzt wird; immer kleiner als 1 (100 %).","Fração da potência (energia) fornecida que é aproveitada; sempre menor que 1 (100 %).","Доля затраченной мощности (энергии), которая используется полезно; всегда меньше 1 (100 %).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'P': None, 'A': 3.6e6, 't': 3600, 'F': 2000, 'v': 25, 'eta': 0.8, 'Pk': None, 'Pu': 2000},
                       {'A': 'kWh', 't': 'h', 'v': 'km/h', 'P': 'kW', 'Pk': 'kW', 'Pu': 'kW'}),
  'jednacine': [
   {'latex': S(r"P = \dfrac{{A}}{t}"), 'trazi': 'P', 'resenja': {'P': 'A/t', 'A': 'P*t', 't': 'A/P'}},
   {'latex': r"P = F v", 'trazi': 'P', 'resenja': {'P': 'F*v', 'F': 'P/v', 'v': 'P/F'}},
   {'latex': LJ(lambda j: r"\eta = \dfrac{%s}{%s}" % (PK[j], PU[j])), 'trazi': 'Pk',
    'resenja': {'eta': 'Pk/Pu', 'Pk': 'eta*Pu', 'Pu': 'Pk/eta'}},
  ]}
})

ZAMENE = [('F_N', 'Fₙ')]
for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)

out = {'oblast': 'energija', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
