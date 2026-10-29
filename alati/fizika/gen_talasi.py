# Generiše assets/oblasti/talasi.json za Formulix (oscilacije, talasi, optika, zračenje)
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']
PI = math.pi
K0 = 273.15

FR = dict(sr='f', en='f', it='f', fr='f', es='f', de='f', pt='f', ru=r'\nu')
IN = dict(sr='I', en='I', it='I', fr='J', es='I', de='J', pt='I', ru='J')
# sočivo: predmet, lik, žižna daljina, uvećanje
PR = dict(sr='p', en='d_o', it='p', fr='p', es='s', de='g', pt='p', ru='d')
LK = dict(sr='l', en='d_i', it='q', fr="p'", es="s'", de='b', pt="p'", ru='f')
FF = dict(sr='f', en='f', it='f', fr='f', es='f', de='f', pt='f', ru='F')
UV = dict(sr='u', en='m', it='G', fr=r'\gamma', es='M', de=r'\beta', pt='A', ru=r'\Gamma')
def S(f):
    def z(j):
        x = f
        for k, d in (('{f}', FR), ('{I}', IN), ('{p}', PR), ('{l}', LK), ('{F}', FF), ('{u}', UV)):
            x = x.replace(k, d[j])
        return x
    return LJ(z)

N = {
 's0': T("amplituda","amplitude","ampiezza","amplitude","amplitud","Amplitude","amplitude","амплитуда"),
 'om': T("kružna frekvencija","angular frequency","pulsazione","pulsation","frecuencia angular","Kreisfrequenz","frequência angular","циклическая частота"),
 'v0': T("najveća brzina","maximum velocity","velocità massima","vitesse maximale","velocidad máxima","Maximalgeschwindigkeit","velocidade máxima","максимальная скорость"),
 'a0': T("najveće ubrzanje","maximum acceleration","accelerazione massima","accélération maximale","aceleración máxima","Maximalbeschleunigung","aceleração máxima","максимальное ускорение"),
 'T': T("period","period","periodo","période","período","Periode","período","период"),
 'f': T("frekvencija","frequency","frequenza","fréquence","frecuencia","Frequenz","frequência","частота"),
 'k': T("konstanta opruge","spring constant","costante elastica","raideur","constante del resorte","Federkonstante","constante elástica","жёсткость пружины"),
 'W': T("energija oscilovanja","energy of oscillation","energia dell’oscillazione","énergie de l’oscillation","energía de la oscilación","Schwingungsenergie","energia da oscilação","энергия колебаний"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'l': T("dužina klatna","length of the pendulum","lunghezza del pendolo","longueur du pendule","longitud del péndulo","Pendellänge","comprimento do pêndulo","длина маятника"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'I': T("moment inercije","moment of inertia","momento d’inerzia","moment d’inertie","momento de inercia","Trägheitsmoment","momento de inércia","момент инерции"),
 'd': T("rastojanje ose od težišta","distance from axis to centre of mass","distanza asse–baricentro","distance axe–centre de masse","distancia eje–centro de masas","Abstand Achse–Schwerpunkt","distância eixo–centro de massa","расстояние от оси до центра масс"),
 'D': T("torziona konstanta","torsion constant","costante di torsione","constante de torsion","constante de torsión","Richtmoment","constante de torção","крутильная жёсткость"),
 'L': T("induktivnost","inductance","induttanza","inductance","inductancia","Induktivität","indutância","индуктивность"),
 'C': T("kapacitet","capacitance","capacità","capacité","capacidad","Kapazität","capacitância","ёмкость"),
 'c': T("brzina talasa","wave speed","velocità dell’onda","célérité de l’onde","velocidad de la onda","Wellengeschwindigkeit","velocidade da onda","скорость волны"),
 'lam': T("talasna dužina","wavelength","lunghezza d’onda","longueur d’onde","longitud de onda","Wellenlänge","comprimento de onda","длина волны"),
 'F': T("sila zatezanja žice","tension of the string","tensione della corda","tension de la corde","tensión de la cuerda","Spannkraft der Saite","tração na corda","сила натяжения струны"),
 'ls': T("dužina žice","length of the string","lunghezza della corda","longueur de la corde","longitud de la cuerda","Saitenlänge","comprimento da corda","длина струны"),
 'ms': T("masa žice","mass of the string","massa della corda","masse de la corde","masa de la cuerda","Masse der Saite","massa da corda","масса струны"),
 'E': T("modul elastičnosti","Young’s modulus","modulo di Young","module de Young","módulo de Young","Elastizitätsmodul","módulo de Young","модуль Юнга"),
 'rho': T("gustina","density","densità","masse volumique","densidad","Dichte","massa específica","плотность"),
 'kapa': T("odnos specifičnih toplota","heat capacity ratio","rapporto dei calori specifici","indice adiabatique","coeficiente adiabático","Isentropenexponent","coeficiente de Poisson","показатель адиабаты"),
 'R': T("univerzalna gasna konstanta","molar gas constant","costante dei gas","constante des gaz parfaits","constante de los gases","universelle Gaskonstante","constante dos gases","газовая постоянная"),
 'Tt': T("temperatura gasa","temperature of the gas","temperatura del gas","température du gaz","temperatura del gas","Temperatur des Gases","temperatura do gás","температура газа"),
 'M': T("molarna masa","molar mass","massa molare","masse molaire","masa molar","molare Masse","massa molar","молярная масса"),
 'Nn': T("redni broj (0, 1, 2, …)","harmonic number (0, 1, 2, …)","numero d’ordine (0, 1, 2, …)","rang (0, 1, 2, …)","número de orden (0, 1, 2, …)","Ordnung (0, 1, 2, …)","número de ordem (0, 1, 2, …)","номер (0, 1, 2, …)"),
 'fN': T("frekvencija N-tog tona","frequency of the N-th mode","frequenza del modo N","fréquence du mode N","frecuencia del modo N","Frequenz der N-ten Eigenschwingung","frequência do modo N","частота N-й гармоники"),
 'lc': T("dužina žice ili cevi","length of string or pipe","lunghezza della corda o del tubo","longueur de la corde ou du tuyau","longitud de la cuerda o del tubo","Länge der Saite oder Pfeife","comprimento da corda ou tubo","длина струны или трубы"),
 'f0': T("frekvencija izvora","source frequency","frequenza della sorgente","fréquence de la source","frecuencia de la fuente","Frequenz der Quelle","frequência da fonte","частота источника"),
 'fp': T("primljena frekvencija","observed frequency","frequenza percepita","fréquence perçue","frecuencia percibida","wahrgenommene Frequenz","frequência percebida","воспринимаемая частота"),
 'vd': T("brzina izvora ili posmatrača","speed of source or observer","velocità della sorgente o dell’osservatore","vitesse de la source ou de l’observateur","velocidad de la fuente o del observador","Geschwindigkeit von Quelle oder Beobachter","velocidade da fonte ou do observador","скорость источника или наблюдателя"),
 'cz': T("brzina zvuka","speed of sound","velocità del suono","vitesse du son","velocidad del sonido","Schallgeschwindigkeit","velocidade do som","скорость звука"),
 'a': T("konstanta rešetke","grating spacing","passo del reticolo","pas du réseau","constante de la red","Gitterkonstante","constante da rede","период решётки"),
 'beta': T("ugao maksimuma","angle of the maximum","angolo del massimo","angle du maximum","ángulo del máximo","Winkel des Maximums","ângulo do máximo","угол максимума"),
 'Nr': T("red maksimuma","order of the maximum","ordine del massimo","ordre du maximum","orden del máximo","Ordnung des Maximums","ordem do máximo","порядок максимума"),
 'n': T("indeks prelamanja","refractive index","indice di rifrazione","indice de réfraction","índice de refracción","Brechungsindex","índice de refração","показатель преломления"),
 'c0': T("brzina svetlosti u vakuumu","speed of light in vacuum","velocità della luce nel vuoto","vitesse de la lumière dans le vide","velocidad de la luz en el vacío","Lichtgeschwindigkeit im Vakuum","velocidade da luz no vácuo","скорость света в вакууме"),
 'cs': T("brzina svetlosti u sredini","speed of light in the medium","velocità della luce nel mezzo","vitesse de la lumière dans le milieu","velocidad de la luz en el medio","Lichtgeschwindigkeit im Medium","velocidade da luz no meio","скорость света в среде"),
 'n1': T("indeks prve sredine","index of medium 1","indice del mezzo 1","indice du milieu 1","índice del medio 1","Brechungsindex Medium 1","índice do meio 1","показатель первой среды"),
 'n2': T("indeks druge sredine","index of medium 2","indice del mezzo 2","indice du milieu 2","índice del medio 2","Brechungsindex Medium 2","índice do meio 2","показатель второй среды"),
 'al': T("upadni ugao","angle of incidence","angolo di incidenza","angle d’incidence","ángulo de incidencia","Einfallswinkel","ângulo de incidência","угол падения"),
 'be': T("prelomni ugao","angle of refraction","angolo di rifrazione","angle de réfraction","ángulo de refracción","Brechungswinkel","ângulo de refração","угол преломления"),
 'ng1': T("indeks gušće sredine","index of the denser medium","indice del mezzo più denso","indice du milieu le plus réfringent","índice del medio más denso","Brechungsindex des dichteren Mediums","índice do meio mais denso","показатель более плотной среды"),
 'ng2': T("indeks ređe sredine","index of the less dense medium","indice del mezzo meno denso","indice du milieu le moins réfringent","índice del medio menos denso","Brechungsindex des dünneren Mediums","índice do meio menos denso","показатель менее плотной среды"),
 'ag': T("granični ugao totalne refleksije","critical angle","angolo limite","angle limite","ángulo límite","Grenzwinkel der Totalreflexion","ângulo limite","предельный угол"),
 'ab': T("Brusterov ugao","Brewster’s angle","angolo di Brewster","angle de Brewster","ángulo de Brewster","Brewster-Winkel","ângulo de Brewster","угол Брюстера"),
 'ff': T("žižna daljina","focal length","distanza focale","distance focale","distancia focal","Brennweite","distância focal","фокусное расстояние"),
 'pp': T("udaljenost predmeta","object distance","distanza dell’oggetto","distance de l’objet","distancia del objeto","Gegenstandsweite","distância do objeto","расстояние до предмета"),
 'll': T("udaljenost lika","image distance","distanza dell’immagine","distance de l’image","distancia de la imagen","Bildweite","distância da imagem","расстояние до изображения"),
 'uu': T("uvećanje","magnification","ingrandimento","grandissement","aumento","Abbildungsmaßstab","aumento","увеличение"),
 'yp': T("veličina predmeta","object size","altezza dell’oggetto","taille de l’objet","tamaño del objeto","Gegenstandsgröße","tamanho do objeto","размер предмета"),
 'yl': T("veličina lika","image size","altezza dell’immagine","taille de l’image","tamaño de la imagen","Bildgröße","tamanho da imagem","размер изображения"),
 'nl': T("indeks prelamanja sočiva","refractive index of the lens","indice della lente","indice de la lentille","índice de la lente","Brechungsindex der Linse","índice da lente","показатель преломления линзы"),
 'no': T("indeks okoline","refractive index of surroundings","indice del mezzo circostante","indice du milieu extérieur","índice del medio","Brechungsindex der Umgebung","índice do meio","показатель среды"),
 'r1': T("poluprečnik prve površi","radius of surface 1","raggio della superficie 1","rayon de la face 1","radio de la cara 1","Krümmungsradius 1","raio da face 1","радиус первой поверхности"),
 'r2': T("poluprečnik druge površi","radius of surface 2","raggio della superficie 2","rayon de la face 2","radio de la cara 2","Krümmungsradius 2","raio da face 2","радиус второй поверхности"),
 'Dj': T("jačina sočiva","optical power","potere diottrico","vergence","potencia óptica","Brechkraft","vergência","оптическая сила"),
 'j': T("gustina svetlosnog toka (intenzitet)","intensity","intensità","éclairement énergétique","intensidad","Bestrahlungsstärke (Intensität)","intensidade","интенсивность"),
 'P': T("snaga izvora","power of the source","potenza della sorgente","puissance de la source","potencia de la fuente","Leistung der Quelle","potência da fonte","мощность источника"),
 'r': T("rastojanje od izvora","distance from the source","distanza dalla sorgente","distance à la source","distancia a la fuente","Abstand zur Quelle","distância da fonte","расстояние до источника"),
 'lmax': T("talasna dužina najjačeg zračenja","peak wavelength","lunghezza d’onda del massimo","longueur d’onde du maximum","longitud de onda del máximo","Wellenlänge des Maximums","comprimento de onda do máximo","длина волны максимума"),
 'kW': T("Vinova konstanta","Wien’s constant","costante di Wien","constante de Wien","constante de Wien","Wiensche Konstante","constante de Wien","постоянная Вина"),
 'sig': T("Štefan-Bolcmanova konstanta","Stefan–Boltzmann constant","costante di Stefan-Boltzmann","constante de Stefan-Boltzmann","constante de Stefan-Boltzmann","Stefan-Boltzmann-Konstante","constante de Stefan-Boltzmann","постоянная Стефана — Больцмана"),
 'Tz': T("temperatura tela","temperature of the body","temperatura del corpo","température du corps","temperatura del cuerpo","Temperatur des Körpers","temperatura do corpo","температура тела"),
 'jc': T("izračena snaga po jedinici površine","radiated power per unit area","potenza irradiata per unità di superficie","puissance rayonnée par unité de surface","potencia radiada por unidad de área","abgestrahlte Leistung pro Fläche","potência irradiada por unidade de área","излучаемая мощность с единицы площади"),
}
OZ = {'s0': 's_0', 'om': r'\omega', 'v0': 'v_0', 'a0': 'a_0', 'T': 'T', 'f': S('{f}'), 'k': 'k', 'W': 'W', 'm': 'm', 'l': 'l', 'g': 'g',
      'I': S('{I}'), 'd': 'd', 'D': 'D', 'L': 'L', 'C': 'C', 'c': 'c', 'lam': r'\lambda', 'F': 'F', 'ls': 'l', 'ms': 'm', 'E': 'E',
      'rho': r'\rho', 'kapa': r'\kappa', 'R': 'R', 'Tt': 'T', 'M': 'M', 'Nn': 'N', 'fN': S('{f}_N'), 'lc': 'l', 'f0': S('{f}_0'),
      'fp': S('{f}'), 'vd': 'v', 'cz': 'c', 'a': 'a', 'beta': r'\beta', 'Nr': 'N', 'n': 'n', 'c0': 'c_0', 'cs': 'c', 'n1': 'n_1',
      'n2': 'n_2', 'ng1': 'n_1', 'ng2': 'n_2', 'al': r'\alpha', 'be': r'\beta', 'ag': r'\alpha_g', 'ab': r'\alpha_B', 'ff': S('{F}'), 'pp': S('{p}'),
      'll': S('{l}'), 'uu': S('{u}'), 'yp': 'y', 'yl': "y'", 'nl': 'n', 'no': 'n_0', 'r1': 'r_1', 'r2': 'r_2', 'Dj': 'D',
      'j': 'j', 'P': 'P', 'r': 'r', 'lmax': r'\lambda_{\max}', 'kW': 'k_W', 'sig': r'\sigma', 'Tz': 'T', 'jc': r'j^{*}'}
VRSTA = {'s0': 'duzina', 'om': 'ugaonaBrzina', 'v0': 'brzina', 'a0': 'ubrzanje', 'T': 'vreme', 'f': 'frekvencija', 'k': 'krutost',
         'W': 'energija', 'm': 'masa', 'l': 'duzina', 'g': 'ubrzanje', 'I': 'momentInercije', 'd': 'duzina', 'D': 'torzija',
         'L': 'induktivnost', 'C': 'kapacitet', 'c': 'brzina', 'lam': 'talasnaDuzina', 'F': 'sila', 'ls': 'duzina', 'ms': 'masa',
         'E': 'pritisak', 'rho': 'gustina', 'kapa': 'bez', 'R': 'gasKonst', 'Tt': 'temperatura', 'M': 'molarnaMasa', 'Nn': 'bez',
         'fN': 'frekvencija', 'lc': 'duzina', 'f0': 'frekvencija', 'fp': 'frekvencija', 'vd': 'brzina', 'cz': 'brzina',
         'a': 'talasnaDuzina', 'beta': 'ugao', 'Nr': 'bez', 'n': 'bez', 'c0': 'brzina', 'cs': 'brzina', 'n1': 'bez', 'n2': 'bez', 'ng1': 'bez', 'ng2': 'bez',
         'al': 'ugao', 'be': 'ugao', 'ag': 'ugao', 'ab': 'ugao', 'ff': 'duzina', 'pp': 'duzina', 'll': 'duzina', 'uu': 'bez',
         'yp': 'duzina', 'yl': 'duzina', 'nl': 'bez', 'no': 'bez', 'r1': 'duzina', 'r2': 'duzina', 'Dj': 'optickaJacina',
         'j': 'intenzitet', 'P': 'snaga', 'r': 'duzina', 'lmax': 'talasnaDuzina', 'kW': 'wien', 'sig': 'stefan', 'Tz': 'temperatura',
         'jc': 'intenzitet'}
POZ = {'s0', 'om', 'v0', 'a0', 'T', 'f', 'k', 'W', 'm', 'l', 'g', 'I', 'd', 'D', 'L', 'C', 'c', 'lam', 'F', 'ls', 'ms', 'E', 'rho',
       'kapa', 'R', 'Tt', 'M', 'fN', 'lc', 'f0', 'fp', 'cz', 'a', 'n', 'c0', 'cs', 'n1', 'n2', 'ng1', 'ng2', 'nl', 'no', 'P', 'r', 'lmax',
       'kW', 'sig', 'Tz', 'jc', 'j', 'yp', 'ag', 'ab'}
NENEG = {'Nn', 'Nr'}

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

def strela(x1, y1, x2, y2, klasa='lik-l', duz=10, sir=4.5):
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    bx, by = x2 - ux * duz, y2 - uy * duz
    px, py = -uy * sir, ux * sir
    return (f'<line class="{klasa}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>'
            f'<path class="tac" d="M{x2:.1f},{y2:.1f} L{bx+px:.1f},{by+py:.1f} L{bx-px:.1f},{by-py:.1f} Z"/>')

def crtez_talas():
    s = '<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<line class="osa" x1="10" y1="75" x2="290" y2="75"/><path class="osa-s" d="M290,75 l-7,-4 v8 Z"/>'
    pts = ' '.join(f'{20 + x:.1f},{75 - 42 * math.sin(2 * PI * x / 120):.1f}' for x in range(0, 261, 3))
    s += f'<polyline class="kriva" points="{pts}"/>'
    s += '<line class="pom" x1="50" y1="33" x2="50" y2="22"/><line class="pom" x1="170" y1="33" x2="170" y2="22"/>'
    s += '<line class="osa" x1="50" y1="22" x2="170" y2="22"/>'
    s += '<text x="104" y="16">λ</text>'
    s += '<line class="pom" x1="50" y1="75" x2="50" y2="33"/><text x="56" y="58">s<tspan class="sub" dy="5">0</tspan></text>'
    s += strela(220, 128, 280, 128)
    s += '<text x="240" y="122">c</text>'
    s += '</svg>'
    return s

def crtez_prelamanje():
    s = '<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<rect class="lik" x="10" y="100" width="280" height="92" stroke="none" fill-opacity="0.7"/>'
    s += '<line class="lik-l" x1="10" y1="100" x2="290" y2="100"/>'
    s += '<line class="pom" x1="150" y1="14" x2="150" y2="190"/>'
    a, b = math.radians(50), math.radians(31)
    s += strela(150 - 95 * math.sin(a), 100 - 95 * math.cos(a), 150, 100)
    s += strela(150, 100, 150 + 95 * math.sin(b), 100 + 95 * math.cos(b))
    s += f'<path class="ugao" d="M150,62 A38,38 0 0,0 {150 - 38*math.sin(a):.1f},{100 - 38*math.cos(a):.1f}"/>'
    s += '<text x="128" y="56">α</text>'
    s += f'<path class="ugao" d="M150,138 A38,38 0 0,0 {150 + 38*math.sin(b):.1f},{100 + 38*math.cos(b):.1f}"/>'
    s += '<text x="160" y="160">β</text>'
    s += '<text x="244" y="90">n<tspan class="sub" dy="5">1</tspan></text><text x="244" y="128">n<tspan class="sub" dy="5">2</tspan></text>'
    s += '</svg>'
    return s

def crtez_socivo(j):
    p, l = PR[j].replace('_o', 'ₒ').replace('_i', 'ᵢ'), LK[j].replace('_o', 'ₒ').replace('_i', 'ᵢ')
    s = '<svg viewBox="0 0 320 170" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<line class="osa" x1="6" y1="90" x2="314" y2="90"/>'
    s += '<path class="lik" d="M160,20 Q178,90 160,160 Q142,90 160,20 Z"/>'
    s += '<circle class="tac" cx="110" cy="90" r="3"/><circle class="tac" cx="210" cy="90" r="3"/>'
    s += f'<text x="104" y="110">{FF[j]}</text><text x="204" y="110">{FF[j]}</text>'
    s += strela(45, 90, 45, 50)   # predmet visine 40 na a = 115
    # lik: b = a f/(a - f) = 115*50/65 ≈ 88.5; uvećanje 0.77 → visina 30.8 obrnut
    s += strela(248.5, 90, 248.5, 120.8)
    s += '<line class="pom" x1="45" y1="50" x2="248.5" y2="120.8"/>'
    s += '<line class="pom" x1="45" y1="50" x2="160" y2="50"/><line class="pom" x1="160" y1="50" x2="248.5" y2="120.8"/>'
    s += '<line class="osa" x1="45" y1="150" x2="160" y2="150"/><line class="osa" x1="160" y1="150" x2="248.5" y2="150"/>'
    s += '<line class="osa" x1="45" y1="144" x2="45" y2="156"/><line class="osa" x1="160" y1="144" x2="160" y2="156"/><line class="osa" x1="248.5" y1="144" x2="248.5" y2="156"/>'
    s += f'<text x="94" y="168">{p}</text><text x="198" y="168">{l}</text>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'harmonijsko', 'simbol': 's(t)',
 'naziv': T("Harmonijsko oscilovanje","Simple harmonic motion","Moto armonico","Oscillations harmoniques","Movimiento armónico simple","Harmonische Schwingung","Movimento harmônico simples","Гармонические колебания"),
 'opis': T("Elongacija, brzina, ubrzanje","Displacement, velocity, acceleration","Spostamento, velocità, accelerazione","Élongation, vitesse, accélération","Elongación, velocidad, aceleración","Auslenkung, Geschwindigkeit, Beschleunigung","Elongação, velocidade, aceleração","Смещение, скорость, ускорение"),
 'kljucne_reci': T("harmonijsko oscilovanje elongacija amplituda period frekvencija energija oscilovanja","simple harmonic motion displacement amplitude period frequency energy","moto armonico elongazione ampiezza periodo frequenza energia","oscillation harmonique elongation amplitude periode frequence energie","movimiento armonico simple elongacion amplitud periodo frecuencia energia","harmonische schwingung auslenkung amplitude periode frequenz energie","movimento harmonico simples elongacao amplitude periodo frequencia energia","гармонические колебания смещение амплитуда период частота энергия"),
 'crtez': None,
 'formule': [
  F(T("Elongacija, brzina i ubrzanje","Displacement, velocity and acceleration","Spostamento, velocità e accelerazione","Élongation, vitesse et accélération","Elongación, velocidad y aceleración","Auslenkung, Geschwindigkeit und Beschleunigung","Elongação, velocidade e aceleração","Смещение, скорость и ускорение"),
    r"s(t) = s_0 \sin\omega t, \quad v(t) = \omega s_0 \cos\omega t, \quad a(t) = -\omega^2 s(t)",
    T("Ubrzanje je uvek usmereno ka ravnotežnom položaju i srazmerno elongaciji.","The acceleration always points to the equilibrium position and is proportional to the displacement.","L’accelerazione è sempre diretta verso l’equilibrio ed è proporzionale allo spostamento.","L’accélération est toujours dirigée vers l’équilibre et proportionnelle à l’élongation.","La aceleración apunta siempre al equilibrio y es proporcional a la elongación.","Die Beschleunigung zeigt stets zur Ruhelage und ist proportional zur Auslenkung.","A aceleração aponta sempre para o equilíbrio e é proporcional à elongação.","Ускорение всегда направлено к положению равновесия и пропорционально смещению.")),
  F(T("Period i frekvencija","Period and frequency","Periodo e frequenza","Période et fréquence","Período y frecuencia","Periode und Frequenz","Período e frequência","Период и частота"),
    S(r"\omega = 2\pi {f} = \frac{2\pi}{T}"),
    T("Isto kao kod kružnog kretanja.","Same as for circular motion.","Come nel moto circolare.","Comme pour le mouvement circulaire.","Igual que en el movimiento circular.","Wie bei der Kreisbewegung.","Igual ao movimento circular.","Как при движении по окружности.")),
  F(T("Energija","Energy","Energia","Énergie","Energía","Energie","Energia","Энергия"),
    r"W = \frac{k s_0^2}{2} = \frac{m v_0^2}{2}",
    T("Ukupna energija je stalna: prelazi iz potencijalne u kinetičku i nazad.","Total energy is constant: it changes from potential to kinetic and back.","L’energia totale è costante: passa da potenziale a cinetica e viceversa.","L’énergie totale est constante : elle passe de potentielle à cinétique et inversement.","La energía total es constante: pasa de potencial a cinética y viceversa.","Die Gesamtenergie ist konstant: sie wandelt sich zwischen Spann- und Bewegungsenergie.","A energia total é constante: passa de potencial a cinética e vice-versa.","Полная энергия постоянна: переходит из потенциальной в кинетическую и обратно.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'v0': None, 's0': 0.05, 'om': 2 * PI, 'a0': None, 'T': None, 'f': 1, 'W': None, 'k': 100, 'm': 0.5}, {'s0': 'cm'}),
  'jednacine': [
   {'latex': r"v_0 = \omega s_0", 'trazi': 'v0', 'resenja': {'v0': 'om*s0', 'om': 'v0/s0', 's0': 'v0/om'}},
   {'latex': r"a_0 = \omega^2 s_0", 'trazi': 'a0', 'resenja': {'a0': 'om*om*s0', 'om': 'sqrt(a0/s0)', 's0': 'a0/(om*om)'}},
   {'latex': r"\omega = \dfrac{2\pi}{T}", 'trazi': 'T', 'resenja': {'om': '2*PI/T', 'T': '2*PI/om'}},
   {'latex': r"W = \dfrac{k s_0^2}{2}", 'trazi': 'W', 'resenja': {'W': 'k*s0*s0/2', 'k': '2*W/(s0*s0)', 's0': 'sqrt(2*W/k)'}},
  ]}
})
del teme[-1]['crtez']

teme.append({
 'id': 'klatna', 'simbol': 'T',
 'naziv': T("Opruga i klatna","Spring and pendulums","Molla e pendoli","Ressort et pendules","Resorte y péndulos","Feder und Pendel","Mola e pêndulos","Пружинный и другие маятники"),
 'opis': T("Period oscilovanja","Period of oscillation","Periodo di oscillazione","Période d’oscillation","Período de oscilación","Schwingungsdauer","Período de oscilação","Период колебаний"),
 'kljucne_reci': T("klatno matematicko fizicko torziono opruga period oscilovanja","pendulum simple physical torsion spring mass period","pendolo semplice fisico torsione molla periodo","pendule simple pesant de torsion ressort periode","pendulo simple fisico de torsion resorte periodo","pendel fadenpendel physikalisches torsionspendel federpendel schwingungsdauer","pendulo simples fisico de torcao mola periodo","маятник математический физический крутильный пружинный период"),
 'formule': [
  F(T("Telo na opruzi","Mass on a spring","Massa su una molla","Masse sur un ressort","Masa en un resorte","Federpendel","Massa numa mola","Пружинный маятник"),
    r"T = 2\pi \sqrt{\frac{m}{k}}", T("Ne zavisi od amplitude ni od g.","Independent of amplitude and of g.","Non dipende dall’ampiezza né da g.","Indépendante de l’amplitude et de g.","No depende de la amplitud ni de g.","Unabhängig von Amplitude und g.","Não depende da amplitude nem de g.","Не зависит от амплитуды и от g.")),
  F(T("Matematičko klatno","Simple pendulum","Pendolo semplice","Pendule simple","Péndulo simple","Fadenpendel","Pêndulo simples","Математический маятник"),
    r"T = 2\pi \sqrt{\frac{l}{g}}", T("Za male uglove (do oko 10°); ne zavisi od mase.","For small angles (up to about 10°); independent of mass.","Per piccoli angoli (fino a circa 10°); non dipende dalla massa.","Pour de petits angles (jusqu’à environ 10°) ; indépendante de la masse.","Para ángulos pequeños (hasta unos 10°); no depende de la masa.","Für kleine Winkel (bis etwa 10°); unabhängig von der Masse.","Para ângulos pequenos (até cerca de 10°); não depende da massa.","Для малых углов (до ~10°); не зависит от массы.")),
  F(T("Fizičko klatno","Physical pendulum","Pendolo fisico","Pendule pesant","Péndulo físico","Physikalisches Pendel","Pêndulo físico","Физический маятник"),
    S(r"T = 2\pi \sqrt{\frac{{I}}{m g d}}"), T("Kruto telo koje se njiše oko ose na rastojanju d od težišta.","A rigid body swinging about an axis at distance d from its centre of mass.","Corpo rigido che oscilla attorno a un asse a distanza d dal baricentro.","Solide oscillant autour d’un axe à la distance d du centre de masse.","Sólido que oscila en torno a un eje a distancia d del centro de masas.","Starrer Körper, der um eine Achse im Abstand d vom Schwerpunkt schwingt.","Corpo rígido oscilando em torno de um eixo à distância d do centro de massa.","Твёрдое тело, качающееся вокруг оси на расстоянии d от центра масс.")),
  F(T("Torziono klatno","Torsion pendulum","Pendolo di torsione","Pendule de torsion","Péndulo de torsión","Torsionspendel","Pêndulo de torção","Крутильный маятник"),
    S(r"T = 2\pi \sqrt{\frac{{I}}{D}}"), T("D je torziona konstanta žice.","D is the torsion constant of the wire.","D è la costante di torsione del filo.","D est la constante de torsion du fil.","D es la constante de torsión del hilo.","D ist das Richtmoment des Drahtes.","D é a constante de torção do fio.","D — крутильная жёсткость нити.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'T': None, 'm': 0.5, 'k': 50, 'l': 1, 'g': 9.81, 'I': 0.1, 'd': 0.2, 'D': 0.5}),
  'jednacine': [
   {'latex': r"T = 2\pi \sqrt{\dfrac{m}{k}}", 'trazi': 'T', 'resenja': {'T': '2*PI*sqrt(m/k)', 'm': 'k*pow(T/(2*PI), 2)', 'k': 'm/pow(T/(2*PI), 2)'}},
   {'latex': r"T = 2\pi \sqrt{\dfrac{l}{g}}", 'trazi': 'T', 'resenja': {'T': '2*PI*sqrt(l/g)', 'l': 'g*pow(T/(2*PI), 2)', 'g': 'l/pow(T/(2*PI), 2)'}},
   {'latex': S(r"T = 2\pi \sqrt{\dfrac{{I}}{m g d}}"), 'trazi': 'T', 'resenja': {'T': '2*PI*sqrt(I/(m*g*d))', 'I': 'm*g*d*pow(T/(2*PI), 2)', 'd': 'I/(m*g*pow(T/(2*PI), 2))', 'm': 'I/(g*d*pow(T/(2*PI), 2))'}, 'promenljive': ['T', 'I', 'm', 'g', 'd']},
   {'latex': S(r"T = 2\pi \sqrt{\dfrac{{I}}{D}}"), 'trazi': 'T', 'resenja': {'T': '2*PI*sqrt(I/D)', 'I': 'D*pow(T/(2*PI), 2)', 'D': 'I/pow(T/(2*PI), 2)'}},
  ]}
})

teme.append({
 'id': 'lc_kolo', 'simbol': 'LC',
 'naziv': T("Električno oscilatorno kolo","LC circuit","Circuito LC","Circuit LC","Circuito LC","LC-Schwingkreis","Circuito LC","Колебательный контур"),
 'opis': T("Tomsonova formula","Thomson’s formula","Formula di Thomson","Formule de Thomson","Fórmula de Thomson","Thomsonsche Formel","Fórmula de Thomson","Формула Томсона"),
 'kljucne_reci': T("oscilatorno kolo lc kolo tomsonova formula rezonantna frekvencija kondenzator kalem radio","lc circuit oscillator resonant frequency thomson capacitor inductor radio","circuito lc oscillante frequenza di risonanza thomson","circuit lc oscillant frequence propre thomson","circuito lc oscilante frecuencia de resonancia thomson","lc schwingkreis resonanzfrequenz thomson","circuito lc oscilador frequencia de ressonancia thomson","колебательный контур формула томсона резонансная частота"),
 'formule': [
  F(T("Period oscilovanja","Period of oscillation","Periodo di oscillazione","Période propre","Período de oscilación","Schwingungsdauer","Período de oscilação","Период колебаний"),
    S(r"T = 2\pi \sqrt{L C}, \quad {f} = \frac{1}{2\pi\sqrt{L C}}"),
    T("Energija prelazi iz električnog polja kondenzatora u magnetno polje kalema i nazad.","Energy passes from the capacitor’s electric field to the coil’s magnetic field and back.","L’energia passa dal campo elettrico del condensatore al campo magnetico della bobina e ritorno.","L’énergie passe du champ électrique du condensateur au champ magnétique de la bobine et inversement.","La energía pasa del campo eléctrico del condensador al magnético de la bobina y viceversa.","Die Energie pendelt zwischen dem elektrischen Feld des Kondensators und dem Magnetfeld der Spule.","A energia passa do campo elétrico do capacitor ao campo magnético da bobina e volta.","Энергия переходит из электрического поля конденсатора в магнитное поле катушки и обратно.")),
  F(T("Energija kola","Energy of the circuit","Energia del circuito","Énergie du circuit","Energía del circuito","Energie des Schwingkreises","Energia do circuito","Энергия контура"),
    r"W = \frac{C U_0^2}{2} = \frac{L I_0^2}{2}",
    T("U_0 i I_0 su najveći napon i najveća struja.","U_0 and I_0 are the peak voltage and current.","U_0 e I_0 sono tensione e corrente massime.","U_0 et I_0 sont la tension et le courant maximaux.","U_0 e I_0 son la tensión y corriente máximas.","U_0 und I_0 sind Scheitelspannung und -strom.","U_0 e I_0 são a tensão e corrente máximas.","U_0 и I_0 — амплитуды напряжения и тока.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'f': None, 'L': 1e-3, 'C': 1e-9, 'T': None}, {'L': 'mH', 'C': 'nF', 'f': 'kHz'}),
  'jednacine': [
   {'latex': S(r"{f} = \dfrac{1}{2\pi\sqrt{L C}}"), 'trazi': 'f', 'resenja': {'f': '1/(2*PI*sqrt(L*C))', 'L': '1/(C*pow(2*PI*f, 2))', 'C': '1/(L*pow(2*PI*f, 2))'}},
   {'latex': r"T = 2\pi \sqrt{L C}", 'trazi': 'T', 'resenja': {'T': '2*PI*sqrt(L*C)', 'L': 'pow(T/(2*PI), 2)/C', 'C': 'pow(T/(2*PI), 2)/L'}},
  ]}
})

teme.append({
 'id': 'talasi', 'simbol': 'λ',
 'naziv': T("Talasi","Waves","Onde","Ondes","Ondas","Wellen","Ondas","Волны"),
 'opis': T("Talasna dužina, brzina talasa","Wavelength, wave speed","Lunghezza d’onda, velocità","Longueur d’onde, célérité","Longitud de onda, velocidad","Wellenlänge, Ausbreitungsgeschwindigkeit","Comprimento de onda, velocidade","Длина волны, скорость волны"),
 'kljucne_reci': T("talas talasna duzina frekvencija brzina talasa brzina zvuka zica talasni broj faza","wave wavelength frequency wave speed speed of sound string wavenumber phase","onda lunghezza d onda frequenza velocita del suono corda","onde longueur d onde frequence celerite vitesse du son corde","onda longitud de onda frecuencia velocidad del sonido cuerda","welle wellenlange frequenz schallgeschwindigkeit saite wellenzahl","onda comprimento de onda frequencia velocidade do som corda","волна длина волны частота скорость звука струна волновое число"),
 'crtez': crtez_talas(),
 'formule': [
  F(T("Osnovna jednačina talasa","Basic wave equation","Relazione fondamentale","Relation fondamentale","Ecuación fundamental","Grundgleichung der Welle","Equação fundamental","Основное соотношение"),
    S(r"c = \lambda {f} = \frac{\omega}{k}, \quad k = \frac{2\pi}{\lambda}"),
    T("k je talasni broj. Zvuk u vazduhu ≈ 343 m/s, svetlost ≈ 3 · 10⁸ m/s.","k is the wavenumber. Sound in air ≈ 343 m/s, light ≈ 3 · 10⁸ m/s.","k è il numero d’onda. Suono in aria ≈ 343 m/s, luce ≈ 3 · 10⁸ m/s.","k est le nombre d’onde. Son dans l’air ≈ 343 m/s, lumière ≈ 3 · 10⁸ m/s.","k es el número de onda. Sonido en el aire ≈ 343 m/s, luz ≈ 3 · 10⁸ m/s.","k ist die Wellenzahl. Schall in Luft ≈ 343 m/s, Licht ≈ 3 · 10⁸ m/s.","k é o número de onda. Som no ar ≈ 343 m/s, luz ≈ 3 · 10⁸ m/s.","k — волновое число. Звук в воздухе ≈ 343 м/с, свет ≈ 3 · 10⁸ м/с.")),
  F(T("Jednačina talasa","Wave function","Funzione d’onda","Équation de l’onde","Función de onda","Wellenfunktion","Função de onda","Уравнение волны"),
    r"s(x, t) = s_0 \sin(\omega t - k x), \quad \delta = 2\pi \frac{\Delta x}{\lambda} = k\,\Delta x",
    T("δ je fazna razlika između dve tačke na rastojanju Δx.","δ is the phase difference between two points Δx apart.","δ è la differenza di fase tra due punti a distanza Δx.","δ est le déphasage entre deux points distants de Δx.","δ es la diferencia de fase entre dos puntos separados Δx.","δ ist die Phasendifferenz zweier Punkte im Abstand Δx.","δ é a diferença de fase entre dois pontos a Δx.","δ — разность фаз точек на расстоянии Δx.")),
  F(T("Brzina talasa u sredinama","Wave speed in media","Velocità nei mezzi","Célérité dans les milieux","Velocidad en los medios","Ausbreitungsgeschwindigkeit in Medien","Velocidade nos meios","Скорость волн в средах"),
    r"c = \sqrt{\frac{F l}{m}}, \quad c = \sqrt{\frac{E}{\rho}}, \quad c = \sqrt{\frac{\kappa R T}{M}}",
    T("Redom: žica (sila zatezanja F, dužina l, masa m), čvrsto telo, gas.","In order: string (tension F, length l, mass m), solid, gas.","Nell’ordine: corda (tensione F, lunghezza l, massa m), solido, gas.","Dans l’ordre : corde (tension F, longueur l, masse m), solide, gaz.","En orden: cuerda (tensión F, longitud l, masa m), sólido, gas.","Der Reihe nach: Saite (Spannkraft F, Länge l, Masse m), Festkörper, Gas.","Na ordem: corda (tração F, comprimento l, massa m), sólido, gás.","По порядку: струна (натяжение F, длина l, масса m), твёрдое тело, газ.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'c': None, 'lam': 0.78, 'f': 440, 'F': 70, 'ls': 0.65, 'ms': 0.003, 'E': 2e11, 'rho': 7850, 'kapa': 1.4, 'R': 8.314462618, 'Tt': K0 + 20, 'M': 0.029},
                       {'lam': 'cm', 'ms': 'g', 'E': 'GPa', 'Tt': '°C'}),
  'jednacine': [
   {'latex': S(r"c = \lambda {f}"), 'trazi': 'c', 'resenja': {'c': 'lam*f', 'lam': 'c/f', 'f': 'c/lam'}},
   {'latex': r"c = \sqrt{\dfrac{F l}{m}}", 'trazi': 'c', 'resenja': {'c': 'sqrt(F*ls/ms)', 'F': 'c*c*ms/ls', 'ls': 'c*c*ms/F', 'ms': 'F*ls/(c*c)'}},
   {'latex': r"c = \sqrt{\dfrac{E}{\rho}}", 'trazi': 'c', 'resenja': {'c': 'sqrt(E/rho)', 'E': 'c*c*rho', 'rho': 'E/(c*c)'}},
   {'latex': r"c = \sqrt{\dfrac{\kappa R T}{M}}", 'trazi': 'c', 'promenljive': ['c', 'kapa', 'R', 'Tt', 'M'],
    'resenja': {'c': 'sqrt(kapa*R*Tt/M)', 'Tt': 'c*c*M/(kapa*R)', 'M': 'kapa*R*Tt/(c*c)', 'kapa': 'c*c*M/(R*Tt)'}},
  ]}
})

teme.append({
 'id': 'stojeci_talasi', 'simbol': 'fₙ',
 'naziv': T("Stojeći talasi i zvuk","Standing waves and sound","Onde stazionarie e suono","Ondes stationnaires et son","Ondas estacionarias y sonido","Stehende Wellen und Schall","Ondas estacionárias e som","Стоячие волны и звук"),
 'opis': T("Žice i cevi muzičkih instrumenata","Strings and pipes of instruments","Corde e canne degli strumenti","Cordes et tuyaux d’instruments","Cuerdas y tubos de instrumentos","Saiten und Pfeifen","Cordas e tubos de instrumentos","Струны и трубы инструментов"),
 'kljucne_reci': T("stojeci talas zica cev osnovni ton harmonici muzicki instrument","standing wave string pipe fundamental harmonics musical instrument","onda stazionaria corda canna armoniche strumento","onde stationnaire corde tuyau fondamental harmoniques instrument","onda estacionaria cuerda tubo armonicos instrumento","stehende welle saite pfeife grundton oberton instrument","onda estacionaria corda tubo harmonicos instrumento","стоячая волна струна труба основной тон гармоники инструмент"),
 'formule': [
  F(T("Oba kraja ista (žica, otvorena cev)","Both ends alike (string, open pipe)","Estremi uguali (corda, canna aperta)","Extrémités identiques (corde, tuyau ouvert)","Extremos iguales (cuerda, tubo abierto)","Beide Enden gleich (Saite, offene Pfeife)","Extremidades iguais (corda, tubo aberto)","Одинаковые концы (струна, открытая труба)"),
    S(r"{f}_N = (N + 1)\,\frac{c}{2 l} = (N + 1)\,{f}_0, \quad N = 0, 1, 2, \ldots"),
    T("N = 0 je osnovni ton, ostali su njegovi celobrojni umnošci.","N = 0 is the fundamental; the others are its integer multiples.","N = 0 è la fondamentale, le altre sono multipli interi.","N = 0 est le fondamental, les autres sont ses multiples entiers.","N = 0 es el fundamental, los demás son múltiplos enteros.","N = 0 ist der Grundton, die anderen sind ganzzahlige Vielfache.","N = 0 é a fundamental, as outras são múltiplos inteiros.","N = 0 — основной тон, остальные — его целые кратные.")),
  F(T("Jedan kraj otvoren, drugi zatvoren","One end open, one closed","Un estremo aperto e uno chiuso","Une extrémité ouverte, l’autre fermée","Un extremo abierto y otro cerrado","Ein Ende offen, eines geschlossen","Uma extremidade aberta e outra fechada","Один конец открыт, другой закрыт"),
    S(r"{f}_N = (2N + 1)\,\frac{c}{4 l} = (2N + 1)\,{f}_0"),
    T("Javljaju se samo neparni harmonici.","Only odd harmonics occur.","Ci sono solo armoniche dispari.","Seuls les harmoniques impairs existent.","Solo aparecen armónicos impares.","Es treten nur ungerade Harmonische auf.","Só aparecem harmônicos ímpares.","Возникают только нечётные гармоники.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'fN': None, 'Nn': 0, 'c': 343, 'lc': 0.5}),
  'jednacine': [
   {'latex': S(r"{f}_N = (N + 1) \dfrac{c}{2 l}"), 'trazi': 'fN', 'resenja': {'fN': '(Nn + 1)*c/(2*lc)', 'c': 'fN*2*lc/(Nn + 1)', 'lc': '(Nn + 1)*c/(2*fN)', 'Nn': 'fN*2*lc/c - 1'}},
   {'latex': S(r"{f}_N = (2N + 1) \dfrac{c}{4 l}"), 'trazi': 'fN', 'resenja': {'fN': '(2*Nn + 1)*c/(4*lc)', 'c': 'fN*4*lc/(2*Nn + 1)', 'lc': '(2*Nn + 1)*c/(4*fN)', 'Nn': '(fN*4*lc/c - 1)/2'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['c']['naziv'] = T("brzina talasa (zvuk u vazduhu ≈ 343 m/s)","wave speed (sound in air ≈ 343 m/s)","velocità dell’onda (suono in aria ≈ 343 m/s)","célérité (son dans l’air ≈ 343 m/s)","velocidad de la onda (sonido ≈ 343 m/s)","Wellengeschwindigkeit (Schall ≈ 343 m/s)","velocidade da onda (som ≈ 343 m/s)","скорость волны (звук ≈ 343 м/с)")

teme.append({
 'id': 'dopler', 'simbol': 'v',
 'naziv': T("Doplerov efekat","Doppler effect","Effetto Doppler","Effet Doppler","Efecto Doppler","Doppler-Effekt","Efeito Doppler","Эффект Доплера"),
 'opis': T("Promena frekvencije pri kretanju","Frequency shift with motion","Variazione di frequenza col moto","Décalage de fréquence","Cambio de frecuencia por movimiento","Frequenzänderung bei Bewegung","Variação da frequência com o movimento","Изменение частоты при движении"),
 'kljucne_reci': T("doplerov efekat sirena ambulantna kola izvor posmatrac priblizavanje udaljavanje","doppler effect siren ambulance source observer approaching receding","effetto doppler sirena ambulanza sorgente osservatore","effet doppler sirene ambulance source observateur","efecto doppler sirena ambulancia fuente observador","doppler effekt sirene krankenwagen quelle beobachter","efeito doppler sirene ambulancia fonte observador","эффект доплера сирена источник наблюдатель приближение удаление"),
 'formule': [
  F(T("Posmatrač se kreće","Moving observer","Osservatore in moto","Observateur en mouvement","Observador en movimiento","Bewegter Beobachter","Observador em movimento","Движется наблюдатель"),
    S(r"{f} = {f}_0 \left(1 \pm \frac{v}{c}\right)"),
    T("Znak + kada se posmatrač približava izvoru, − kada se udaljava.","Plus sign when the observer approaches, minus when receding.","Segno + se l’osservatore si avvicina, − se si allontana.","Signe + si l’observateur s’approche, − s’il s’éloigne.","Signo + si el observador se acerca, − si se aleja.","Plus, wenn sich der Beobachter nähert, minus beim Entfernen.","Sinal + quando o observador se aproxima, − quando se afasta.","«+» при приближении наблюдателя, «−» при удалении.")),
  F(T("Izvor se kreće","Moving source","Sorgente in moto","Source en mouvement","Fuente en movimiento","Bewegte Quelle","Fonte em movimento","Движется источник"),
    S(r"{f} = \frac{{f}_0}{1 \mp \dfrac{v}{c}}"),
    T("Gornji znak (−) kada se izvor približava: ton je viši; c je brzina zvuka.","Upper sign (−) when the source approaches: the pitch is higher; c is the speed of sound.","Segno superiore (−) se la sorgente si avvicina: il suono è più acuto; c è la velocità del suono.","Signe du haut (−) si la source s’approche : le son est plus aigu ; c est la vitesse du son.","Signo superior (−) si la fuente se acerca: el tono es más agudo; c es la velocidad del sonido.","Oberes Zeichen (−), wenn sich die Quelle nähert: der Ton ist höher; c ist die Schallgeschwindigkeit.","Sinal de cima (−) quando a fonte se aproxima: o som é mais agudo; c é a velocidade do som.","Верхний знак (−) при приближении источника: тон выше; c — скорость звука.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'fp': None, 'f0': 700, 'vd': 25, 'cz': 343}, {'vd': 'km/h'}),
  'jednacine': [
   {'latex': S(r"{f} = {f}_0 \left(1 + \dfrac{v}{c}\right)"), 'trazi': 'fp', 'resenja': {'fp': 'f0*(1 + vd/cz)', 'f0': 'fp/(1 + vd/cz)', 'vd': 'cz*(fp/f0 - 1)'},
    'napomene': {'fp': T("Posmatrač se približava izvoru; za udaljavanje unesi negativnu brzinu.","Observer approaching; for receding enter a negative speed.","Osservatore che si avvicina; per l’allontanamento inserisci una velocità negativa.","Observateur qui s’approche ; pour l’éloignement, entrez une vitesse négative.","Observador que se acerca; para alejarse introduce velocidad negativa.","Beobachter nähert sich; beim Entfernen negative Geschwindigkeit eingeben.","Observador se aproximando; para afastamento use velocidade negativa.","Наблюдатель приближается; для удаления введите отрицательную скорость.")}},
   {'latex': S(r"{f} = \dfrac{{f}_0}{1 - \dfrac{v}{c}}"), 'trazi': 'fp', 'resenja': {'fp': 'f0/(1 - vd/cz)', 'f0': 'fp*(1 - vd/cz)', 'vd': 'cz*(1 - f0/fp)'},
    'napomene': {'fp': T("Izvor se približava; za udaljavanje unesi negativnu brzinu.","Source approaching; for receding enter a negative speed.","Sorgente che si avvicina; per l’allontanamento inserisci una velocità negativa.","Source qui s’approche ; pour l’éloignement, entrez une vitesse négative.","Fuente que se acerca; para alejarse introduce velocidad negativa.","Quelle nähert sich; beim Entfernen negative Geschwindigkeit eingeben.","Fonte se aproximando; para afastamento use velocidade negativa.","Источник приближается; для удаления введите отрицательную скорость.")}},
  ]}
})
teme[-1]['kalkulator']['velicine']['cz']['naziv'] = N['cz']

teme.append({
 'id': 'resetka', 'simbol': 'N',
 'naziv': T("Optička rešetka","Diffraction grating","Reticolo di diffrazione","Réseau de diffraction","Red de difracción","Optisches Gitter","Rede de difração","Дифракционная решётка"),
 'opis': T("Ogib svetlosti","Diffraction of light","Diffrazione della luce","Diffraction de la lumière","Difracción de la luz","Beugung des Lichts","Difração da luz","Дифракция света"),
 'kljucne_reci': T("opticka resetka ogib difrakcija interferencija maksimum talasna duzina svetlosti laser","diffraction grating interference maximum wavelength of light laser","reticolo di diffrazione interferenza massimo laser","reseau de diffraction interference maximum laser","red de difraccion interferencia maximo laser","optisches gitter beugung interferenz maximum laser","rede de difracao interferencia maximo laser","дифракционная решётка интерференция максимум длина волны лазер"),
 'formule': [
  F(T("Uslov za maksimume","Condition for maxima","Condizione dei massimi","Condition des maxima","Condición de máximos","Bedingung für Maxima","Condição dos máximos","Условие максимумов"),
    r"a \sin\beta = N \lambda, \quad N = 0, \pm 1, \pm 2, \ldots, \quad N_{\max} \le \frac{a}{\lambda}",
    T("a je rastojanje između susednih proreza (konstanta rešetke).","a is the distance between neighbouring slits (grating spacing).","a è la distanza tra fenditure vicine (passo del reticolo).","a est la distance entre fentes voisines (pas du réseau).","a es la distancia entre rendijas vecinas (constante de la red).","a ist der Abstand benachbarter Spalte (Gitterkonstante).","a é a distância entre fendas vizinhas (constante da rede).","a — расстояние между соседними щелями (период решётки).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'beta': None, 'a': 2e-6, 'Nr': 1, 'lam': 633e-9}, {'a': 'µm', 'lam': 'nm', 'beta': '°'}),
  'jednacine': [
   {'latex': r"a \sin\beta = N \lambda", 'trazi': 'beta', 'resenja': {'beta': 'asin(Nr*lam/a)', 'lam': 'a*sin(beta)/Nr', 'a': 'Nr*lam/sin(beta)', 'Nr': 'a*sin(beta)/lam'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['beta'].pop('poz', None)

teme.append({
 'id': 'prelamanje', 'simbol': 'n',
 'naziv': T("Prelamanje svetlosti","Refraction of light","Rifrazione della luce","Réfraction de la lumière","Refracción de la luz","Brechung des Lichts","Refração da luz","Преломление света"),
 'opis': T("Snelov zakon, totalna refleksija","Snell’s law, total reflection","Legge di Snell, riflessione totale","Loi de Snell-Descartes, réflexion totale","Ley de Snell, reflexión total","Brechungsgesetz, Totalreflexion","Lei de Snell, reflexão total","Закон Снеллиуса, полное отражение"),
 'kljucne_reci': T("prelamanje svetlosti indeks prelamanja snelov zakon totalna refleksija granicni ugao brusterov ugao polarizacija","refraction refractive index snell law total internal reflection critical angle brewster polarization","rifrazione indice di rifrazione legge di snell riflessione totale angolo limite brewster","refraction indice snell descartes reflexion totale angle limite brewster","refraccion indice snell reflexion total angulo limite brewster","brechung brechungsindex snellius totalreflexion grenzwinkel brewster","refracao indice snell reflexao total angulo limite brewster","преломление показатель снеллиус полное отражение предельный угол брюстер"),
 'crtez': crtez_prelamanje(),
 'formule': [
  F(T("Indeks prelamanja","Refractive index","Indice di rifrazione","Indice de réfraction","Índice de refracción","Brechungsindex","Índice de refração","Показатель преломления"),
    r"n = \frac{c_0}{c}, \quad c_0 = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}",
    T("Voda n ≈ 1,33, staklo ≈ 1,5, dijamant ≈ 2,42.","Water n ≈ 1.33, glass ≈ 1.5, diamond ≈ 2.42.","Acqua n ≈ 1,33, vetro ≈ 1,5, diamante ≈ 2,42.","Eau n ≈ 1,33, verre ≈ 1,5, diamant ≈ 2,42.","Agua n ≈ 1,33, vidrio ≈ 1,5, diamante ≈ 2,42.","Wasser n ≈ 1,33, Glas ≈ 1,5, Diamant ≈ 2,42.","Água n ≈ 1,33, vidro ≈ 1,5, diamante ≈ 2,42.","Вода n ≈ 1,33, стекло ≈ 1,5, алмаз ≈ 2,42.")),
  F(T("Snelov zakon","Snell’s law","Legge di Snell","Loi de Snell-Descartes","Ley de Snell","Snelliussches Brechungsgesetz","Lei de Snell","Закон Снеллиуса"),
    r"\frac{\sin\alpha}{\sin\beta} = \frac{c_1}{c_2} = \frac{n_2}{n_1}",
    T("α je upadni, β prelomni ugao, oba mereni od normale.","α is the angle of incidence, β of refraction, both from the normal.","α è l’angolo di incidenza, β di rifrazione, entrambi dalla normale.","α est l’angle d’incidence, β de réfraction, mesurés depuis la normale.","α es el ángulo de incidencia, β el de refracción, desde la normal.","α ist der Einfalls-, β der Brechungswinkel, beide zum Lot.","α é o ângulo de incidência, β o de refração, ambos a partir da normal.","α — угол падения, β — угол преломления, от нормали.")),
  F(T("Totalna refleksija i Brusterov ugao","Total reflection and Brewster’s angle","Riflessione totale e angolo di Brewster","Réflexion totale et angle de Brewster","Reflexión total y ángulo de Brewster","Totalreflexion und Brewster-Winkel","Reflexão total e ângulo de Brewster","Полное отражение и угол Брюстера"),
    r"\sin\alpha_g = \frac{n_2}{n_1}\ (n_2 < n_1), \quad \tan\alpha_B = n",
    T("Iznad graničnog ugla svetlost se potpuno odbija (optička vlakna). Pod Brusterovim uglom odbijena svetlost je polarizovana.","Above the critical angle light is totally reflected (optical fibres). At Brewster’s angle reflected light is polarized.","Oltre l’angolo limite la luce è riflessa totalmente (fibre ottiche). All’angolo di Brewster la luce riflessa è polarizzata.","Au-delà de l’angle limite la lumière est totalement réfléchie (fibres optiques). À l’angle de Brewster la lumière réfléchie est polarisée.","Por encima del ángulo límite la luz se refleja totalmente (fibra óptica). En el ángulo de Brewster la luz reflejada está polarizada.","Oberhalb des Grenzwinkels wird Licht total reflektiert (Glasfaser). Beim Brewster-Winkel ist das reflektierte Licht polarisiert.","Acima do ângulo limite a luz é totalmente refletida (fibra óptica). No ângulo de Brewster a luz refletida é polarizada.","Выше предельного угла свет полностью отражается (оптоволокно). Под углом Брюстера отражённый свет поляризован.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'n': None, 'c0': 299792458, 'cs': 2.25e8, 'be': None, 'n1': 1, 'al': PI / 4, 'n2': 1.33, 'ng1': 1.33, 'ng2': 1, 'ag': None, 'ab': None}, {'al': '°', 'be': '°', 'ag': '°', 'ab': '°', 'cs': 'm/s'}),
  'jednacine': [
   {'latex': r"n = \dfrac{c_0}{c}", 'trazi': 'n', 'resenja': {'n': 'c0/cs', 'cs': 'c0/n', 'c0': 'n*cs'}},
   {'latex': r"n_1 \sin\alpha = n_2 \sin\beta", 'trazi': 'be', 'resenja': {'be': 'asin(n1*sin(al)/n2)', 'al': 'asin(n2*sin(be)/n1)', 'n1': 'n2*sin(be)/sin(al)', 'n2': 'n1*sin(al)/sin(be)'}},
   {'latex': r"\sin\alpha_g = \dfrac{n_2}{n_1}", 'trazi': 'ag', 'resenja': {'ag': 'asin(ng2/ng1)', 'ng2': 'ng1*sin(ag)', 'ng1': 'ng2/sin(ag)'},
    'napomene': {'ag': T("Iz gušće u ređu sredinu, npr. n₁ = 1,33 (voda) i n₂ = 1 (vazduh).","From denser to less dense medium, e.g. n₁ = 1.33 (water), n₂ = 1 (air).","Dal mezzo più denso al meno denso, es. n₁ = 1,33 (acqua), n₂ = 1 (aria).","Du milieu plus réfringent vers le moins réfringent, ex. n₁ = 1,33 (eau), n₂ = 1 (air).","Del medio más denso al menos denso, p. ej. n₁ = 1,33 (agua), n₂ = 1 (aire).","Vom optisch dichteren ins dünnere Medium, z. B. n₁ = 1,33 (Wasser), n₂ = 1 (Luft).","Do meio mais denso para o menos denso, ex. n₁ = 1,33 (água), n₂ = 1 (ar).","Из оптически более плотной среды в менее плотную, напр. n₁ = 1,33 (вода), n₂ = 1 (воздух).")}},
   {'latex': r"\tan\alpha_B = n", 'trazi': 'ab', 'resenja': {'ab': 'atan(n)', 'n': 'tan(ab)'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['cs']['jed'] = 'm/s'
v['n']['pocetna'] = 1.5

teme.append({
 'id': 'socivo', 'simbol': 'f',
 'naziv': T("Sočiva i ogledala","Lenses and mirrors","Lenti e specchi","Lentilles et miroirs","Lentes y espejos","Linsen und Spiegel","Lentes e espelhos","Линзы и зеркала"),
 'opis': T("Jednačina sočiva, uvećanje","Lens equation, magnification","Equazione delle lenti, ingrandimento","Relation de conjugaison, grandissement","Ecuación de las lentes, aumento","Linsengleichung, Abbildungsmaßstab","Equação das lentes, aumento","Формула линзы, увеличение"),
 'kljucne_reci': T("socivo ogledalo zizna daljina jednacina sociva uvecanje dioptrija naocare lupa","lens mirror focal length lens equation magnification diopter glasses magnifier","lente specchio distanza focale equazione ingrandimento diottria occhiali","lentille miroir distance focale conjugaison grandissement dioptrie lunettes loupe","lente espejo distancia focal ecuacion aumento dioptria gafas lupa","linse spiegel brennweite linsengleichung vergrosserung dioptrie brille lupe","lente espelho distancia focal equacao aumento dioptria oculos lupa","линза зеркало фокусное расстояние формула линзы увеличение диоптрия очки лупа"),
 'crtez': {j: crtez_socivo(j) for j in J},
 'formule': [
  F(T("Jednačina sočiva","Lens equation","Equazione delle lenti","Relation de conjugaison","Ecuación de las lentes","Linsengleichung","Equação das lentes","Формула тонкой линзы"),
    S(r"\frac{1}{{F}} = \frac{1}{{p}} + \frac{1}{{l}}"),
    T("Važi i za sferna ogledala (f = r/2). Za rasipno sočivo f je negativno, a za imaginarni lik udaljenost lika.","Also valid for spherical mirrors (f = r/2). For a diverging lens f is negative, as is the distance of a virtual image.","Vale anche per gli specchi sferici (f = r/2). Per una lente divergente f è negativa, come la distanza di un’immagine virtuale.","Vaut aussi pour les miroirs sphériques (f = r/2). Pour une lentille divergente f est négative, ainsi que la distance d’une image virtuelle.","Vale también para espejos esféricos (f = r/2). Para una lente divergente f es negativa, igual que la distancia de una imagen virtual.","Gilt auch für Kugelspiegel (f = r/2). Bei Zerstreuungslinsen ist f negativ, ebenso die Bildweite eines virtuellen Bildes.","Vale também para espelhos esféricos (f = r/2). Para lente divergente f é negativa, assim como a distância de imagem virtual.","Верна и для сферических зеркал (F = R/2). Для рассеивающей линзы F отрицательно, как и расстояние до мнимого изображения.")),
  F(T("Uvećanje","Magnification","Ingrandimento","Grandissement","Aumento","Abbildungsmaßstab","Aumento","Увеличение"),
    S(r"{u} = \frac{y'}{y} = \frac{{l}}{{p}}"),
    T("y je veličina predmeta, y′ veličina lika.","y is the object size, y′ the image size.","y è l’altezza dell’oggetto, y′ quella dell’immagine.","y est la taille de l’objet, y′ celle de l’image.","y es el tamaño del objeto, y′ el de la imagen.","y ist die Gegenstands-, y′ die Bildgröße.","y é o tamanho do objeto, y′ o da imagem.","y — размер предмета, y′ — размер изображения.")),
  F(T("Žižna daljina sočiva","Lensmaker’s equation","Formula del costruttore di lenti","Formule des opticiens","Ecuación del fabricante de lentes","Linsenschleiferformel","Equação dos fabricantes de lentes","Формула оптической силы линзы"),
    S(r"\frac{1}{{F}} = \left(\frac{n}{n_0} - 1\right)\left(\frac{1}{r_1} + \frac{1}{r_2}\right), \quad D = \frac{1}{{F}}"),
    T("r₁ i r₂ su poluprečnici krivina (pozitivni za ispupčene površi). D je jačina sočiva u dioptrijama (1 dpt = 1/m).","r₁, r₂ are the radii of curvature (positive for convex surfaces). D is the optical power in dioptres (1 dpt = 1/m).","r₁, r₂ sono i raggi di curvatura (positivi se convessi). D è il potere diottrico (1 dpt = 1/m).","r₁, r₂ sont les rayons de courbure (positifs si convexes). D est la vergence en dioptries (1 δ = 1/m).","r₁, r₂ son los radios de curvatura (positivos si convexos). D es la potencia en dioptrías (1 dpt = 1/m).","r₁, r₂ sind die Krümmungsradien (positiv bei konvex). D ist die Brechkraft in Dioptrien (1 dpt = 1/m).","r₁, r₂ são os raios de curvatura (positivos se convexos). D é a vergência em dioptrias (1 di = 1/m).","r₁, r₂ — радиусы кривизны (положительны для выпуклых). D — оптическая сила в диоптриях (1 дптр = 1/м).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'ll': None, 'ff': 0.1, 'pp': 0.3, 'uu': None, 'yl': None, 'yp': 0.02, 'nl': 1.5, 'no': 1, 'r1': 0.2, 'r2': 0.2, 'Dj': None},
                       {'ff': 'cm', 'pp': 'cm', 'll': 'cm', 'yp': 'cm', 'yl': 'cm', 'r1': 'cm', 'r2': 'cm'}),
  'jednacine': [
   {'latex': S(r"\dfrac{1}{{F}} = \dfrac{1}{{p}} + \dfrac{1}{{l}}"), 'trazi': 'll', 'resenja': {'ll': '1/(1/ff - 1/pp)', 'pp': '1/(1/ff - 1/ll)', 'ff': '1/(1/pp + 1/ll)'}},
   {'latex': S(r"{u} = \dfrac{{l}}{{p}}"), 'trazi': 'uu', 'resenja': {'uu': 'll/pp', 'll': 'uu*pp', 'pp': 'll/uu'}},
   {'latex': S(r"y' = y\,\dfrac{{l}}{{p}}"), 'trazi': 'yl', 'resenja': {'yl': 'yp*ll/pp', 'yp': 'yl*pp/ll', 'll': 'yl*pp/yp', 'pp': 'yp*ll/yl'}},
   {'latex': S(r"\dfrac{1}{{F}} = \left(\dfrac{n}{n_0} - 1\right)\left(\dfrac{1}{r_1} + \dfrac{1}{r_2}\right)"), 'trazi': 'ff',
    'resenja': {'ff': '1/((nl/no - 1)*(1/r1 + 1/r2))', 'nl': 'no*(1 + 1/(ff*(1/r1 + 1/r2)))', 'r1': '1/(1/(ff*(nl/no - 1)) - 1/r2)', 'r2': '1/(1/(ff*(nl/no - 1)) - 1/r1)'}},
   {'latex': S(r"D = \dfrac{1}{{F}}"), 'trazi': 'Dj', 'resenja': {'Dj': '1/ff', 'ff': '1/Dj'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']
for k in ('ff', 'll', 'r1', 'r2', 'Dj', 'uu', 'yl'): v[k].pop('poz', None)

teme.append({
 'id': 'zracenje', 'simbol': 'σT⁴',
 'naziv': T("Svetlost i toplotno zračenje","Light and thermal radiation","Luce e irraggiamento termico","Lumière et rayonnement thermique","Luz y radiación térmica","Licht und Wärmestrahlung","Luz e radiação térmica","Свет и тепловое излучение"),
 'opis': T("Intenzitet, Vinov i Štefanov zakon","Intensity, Wien’s and Stefan’s laws","Intensità, leggi di Wien e Stefan","Éclairement, lois de Wien et Stefan","Intensidad, leyes de Wien y Stefan","Intensität, Wien und Stefan-Boltzmann","Intensidade, leis de Wien e Stefan","Интенсивность, законы Вина и Стефана"),
 'kljucne_reci': T("intenzitet zracenja crno telo vinov zakon stefan bolcmanov zakon temperatura zvezde sunce albedo","intensity radiation black body wien law stefan boltzmann law star temperature sun albedo","intensita radiazione corpo nero legge di wien stefan boltzmann stella sole albedo","eclairement rayonnement corps noir loi de wien stefan boltzmann etoile soleil albedo","intensidad radiacion cuerpo negro ley de wien stefan boltzmann estrella sol albedo","intensitat strahlung schwarzer korper wiensches gesetz stefan boltzmann stern sonne albedo","intensidade radiacao corpo negro lei de wien stefan boltzmann estrela sol albedo","интенсивность излучения абсолютно чёрное тело закон вина стефана больцмана звезда солнце альбедо"),
 'formule': [
  F(T("Intenzitet","Intensity","Intensità","Éclairement","Intensidad","Intensität","Intensidade","Интенсивность"),
    r"j = \frac{P}{S}, \quad j(r) = \frac{P}{4\pi r^2}, \quad j' = j \cos\alpha",
    T("Tačkasti izvor zrači podjednako na sve strane, pa intenzitet opada sa kvadratom rastojanja. α je ugao između zraka i normale na površinu.","A point source radiates equally in all directions, so intensity falls with the square of distance. α is the angle between the rays and the surface normal.","Una sorgente puntiforme irradia ugualmente in tutte le direzioni: l’intensità cala col quadrato della distanza. α è l’angolo con la normale.","Une source ponctuelle rayonne dans toutes les directions : l’éclairement décroît comme le carré de la distance. α est l’angle avec la normale.","Una fuente puntual emite igual en todas direcciones: la intensidad cae con el cuadrado de la distancia. α es el ángulo con la normal.","Eine Punktquelle strahlt in alle Richtungen gleich, die Intensität fällt mit dem Abstandsquadrat. α ist der Winkel zum Lot.","Uma fonte pontual irradia igualmente em todas as direções: a intensidade cai com o quadrado da distância. α é o ângulo com a normal.","Точечный источник излучает во все стороны, интенсивность убывает как квадрат расстояния. α — угол с нормалью.")),
  F(T("Vinov zakon","Wien’s law","Legge di Wien","Loi de Wien","Ley de Wien","Wiensches Verschiebungsgesetz","Lei de Wien","Закон Вина"),
    r"\lambda_{\max} = \frac{k_W}{T}",
    T("Toplija tela najjače zrače na kraćim talasnim dužinama. Sunce (5800 K): oko 500 nm.","Hotter bodies radiate most strongly at shorter wavelengths. The Sun (5800 K): about 500 nm.","I corpi più caldi irradiano di più a lunghezze d’onda minori. Sole (5800 K): circa 500 nm.","Les corps plus chauds rayonnent surtout aux courtes longueurs d’onde. Soleil (5800 K) : environ 500 nm.","Los cuerpos más calientes emiten más en longitudes de onda cortas. Sol (5800 K): unos 500 nm.","Heißere Körper strahlen am stärksten bei kürzeren Wellenlängen. Sonne (5800 K): etwa 500 nm.","Corpos mais quentes irradiam mais em comprimentos de onda menores. Sol (5800 K): cerca de 500 nm.","Более горячие тела сильнее излучают на коротких волнах. Солнце (5800 К): около 500 нм.")),
  F(T("Štefan-Bolcmanov zakon","Stefan–Boltzmann law","Legge di Stefan-Boltzmann","Loi de Stefan-Boltzmann","Ley de Stefan-Boltzmann","Stefan-Boltzmann-Gesetz","Lei de Stefan-Boltzmann","Закон Стефана — Больцмана"),
    r"j^{*} = \frac{P^{*}}{S} = \sigma T^4, \quad j^{*}_{\text{siv}} = (1 - a)\,\sigma T^4",
    T("Prvo za crno telo; drugo za sivo telo, gde je a deo upadnog zračenja koji se odbije (albedo).","First for a black body; second for a grey body, where a is the reflected fraction of incident radiation (albedo).","La prima per il corpo nero; la seconda per un corpo grigio, con a frazione riflessa (albedo).","La première pour le corps noir ; la seconde pour un corps gris, a étant la fraction réfléchie (albédo).","La primera para el cuerpo negro; la segunda para un cuerpo gris, con a la fracción reflejada (albedo).","Erstens für den schwarzen Körper; zweitens für den grauen Körper mit dem reflektierten Anteil a (Albedo).","A primeira para o corpo negro; a segunda para um corpo cinzento, com a a fração refletida (albedo).","Первая — для абсолютно чёрного тела; вторая — для серого, где a — доля отражённого излучения (альбедо).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'j': None, 'P': 100, 'r': 2, 'lmax': None, 'kW': 2.897771955e-3, 'Tz': 5800, 'jc': None, 'sig': 5.670374419e-8},
                       {'lmax': 'nm'}),
  'jednacine': [
   {'latex': r"j = \dfrac{P}{4\pi r^2}", 'trazi': 'j', 'resenja': {'j': 'P/(4*PI*r*r)', 'P': 'j*4*PI*r*r', 'r': 'sqrt(P/(4*PI*j))'}},
   {'latex': r"\lambda_{\max} = \dfrac{k_W}{T}", 'trazi': 'lmax', 'promenljive': ['lmax', 'kW', 'Tz'], 'resenja': {'lmax': 'kW/Tz', 'Tz': 'kW/lmax'}},
   {'latex': r"j^{*} = \sigma T^4", 'trazi': 'jc', 'promenljive': ['jc', 'sig', 'Tz'], 'resenja': {'jc': 'sig*pow(Tz, 4)', 'Tz': 'pow(jc/sig, 0.25)'}},
  ]}
})

import re
FUNK = {'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'pow', 'ln', 'PI', 'kvPoz', 'abs'}
for t in teme:
    vel = t['kalkulator']['velicine']
    for j in t['kalkulator']['jednacine']:
        # sve veličine koje se pojavljuju u izrazima moraju biti polja za unos
        koriscene = list(j['resenja'])
        for izraz in j['resenja'].values():
            for ime in re.findall(r'[A-Za-z_][A-Za-z0-9_]*', izraz):
                if ime not in FUNK and ime not in koriscene: koriscene.append(ime)
        if j.get('promenljive'):
            for ime in koriscene:
                if ime not in j['promenljive']: j['promenljive'].append(ime)
        elif len(koriscene) > len(j['resenja']):
            j['promenljive'] = koriscene
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)
    for f in t['formule']:
        o = f.get('objasnjenje')
        if isinstance(o, dict):
            for jj in J: o[jj] = o[jj].replace('U_0', 'U₀').replace('I_0', 'I₀').replace('t_p', 'tₚ')

out = {'oblast': 'talasi', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
