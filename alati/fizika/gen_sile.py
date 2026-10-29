# Generiše assets/oblasti/sile.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def L(osnovni, **izuzeci):
    if not izuzeci: return osnovni
    return {j: izuzeci.get(j, osnovni) for j in J}
def LJ(f):
    """LaTeX po jeziku iz funkcije f(jezik)."""
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']

PI = math.pi

# Oznaka sile trenja po jeziku
TR = dict(sr='tr', en='f', it='a', fr='f', es='r', de='R', pt='at', ru=r'\text{тр}')
def Ftr(j): return r'F_{\mathrm{%s}}' % TR[j] if j != 'ru' else r'F_{\text{тр}}'
FTR = LJ(Ftr)

N = {
 'F': T("sila","force","forza","force","fuerza","Kraft","força","сила"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'a': T("ubrzanje","acceleration","accelerazione","accélération","aceleración","Beschleunigung","aceleração","ускорение"),
 'Fg': T("težina (sila teže)","weight","forza peso","poids","peso","Gewichtskraft","peso","сила тяжести"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'Gk': T("gravitaciona konstanta","gravitational constant","costante di gravitazione","constante gravitationnelle","constante de gravitación","Gravitationskonstante","constante gravitacional","гравитационная постоянная"),
 'm1': T("masa prvog tela","mass of body 1","massa del corpo 1","masse du corps 1","masa del cuerpo 1","Masse von Körper 1","massa do corpo 1","масса первого тела"),
 'm2': T("masa drugog tela","mass of body 2","massa del corpo 2","masse du corps 2","masa del cuerpo 2","Masse von Körper 2","massa do corpo 2","масса второго тела"),
 'M': T("masa planete","mass of the planet","massa del pianeta","masse de la planète","masa del planeta","Masse des Planeten","massa do planeta","масса планеты"),
 'r': T("rastojanje između središta","distance between centres","distanza tra i centri","distance entre les centres","distancia entre centros","Abstand der Mittelpunkte","distância entre os centros","расстояние между центрами"),
 'R': T("poluprečnik planete","radius of the planet","raggio del pianeta","rayon de la planète","radio del planeta","Radius des Planeten","raio do planeta","радиус планеты"),
 'gp': T("ubrzanje na površini","surface gravity","gravità in superficie","pesanteur à la surface","gravedad en la superficie","Fallbeschleunigung an der Oberfläche","gravidade na superfície","ускорение на поверхности"),
 'Ftr': T("sila trenja","friction force","forza d’attrito","force de frottement","fuerza de rozamiento","Reibungskraft","força de atrito","сила трения"),
 'FN': T("normalna sila (pritisak na podlogu)","normal force","forza normale","force normale","fuerza normal","Normalkraft","força normal","сила нормального давления"),
 'mu': T("koeficijent trenja","coefficient of friction","coefficiente d’attrito","coefficient de frottement","coeficiente de rozamiento","Reibungszahl","coeficiente de atrito","коэффициент трения"),
 'alfa': T("ugao nagiba","angle of incline","angolo d’inclinazione","angle d’inclinaison","ángulo de inclinación","Neigungswinkel","ângulo de inclinação","угол наклона"),
 'k': T("konstanta opruge","spring constant","costante elastica","raideur du ressort","constante del resorte","Federkonstante","constante elástica","жёсткость пружины"),
 'x': T("izduženje opruge","spring extension","allungamento della molla","allongement du ressort","alargamiento del resorte","Auslenkung der Feder","deformação da mola","удлинение пружины"),
 'k1': T("konstanta prve opruge","spring constant 1","costante della molla 1","raideur du ressort 1","constante del resorte 1","Federkonstante 1","constante da mola 1","жёсткость первой пружины"),
 'k2': T("konstanta druge opruge","spring constant 2","costante della molla 2","raideur du ressort 2","constante del resorte 2","Federkonstante 2","constante da mola 2","жёсткость второй пружины"),
 'kuk': T("ukupna konstanta","total spring constant","costante totale","raideur totale","constante total","Gesamtfederkonstante","constante total","общая жёсткость"),
 'p': T("pritisak","pressure","pressione","pression","presión","Druck","pressão","давление"),
 'S': T("površina","area","area","aire","área","Fläche","área","площадь"),
 'dl': T("izduženje","elongation","allungamento","allongement","alargamiento","Verlängerung","alongamento","удлинение"),
 'l': T("početna dužina","initial length","lunghezza iniziale","longueur initiale","longitud inicial","Anfangslänge","comprimento inicial","начальная длина"),
 'E': T("modul elastičnosti (Jangov)","Young's modulus","modulo di Young","module de Young","módulo de Young","Elastizitätsmodul","módulo de Young","модуль Юнга"),
 'Mo': T("moment sile","torque","momento della forza","moment de la force","momento de la fuerza","Drehmoment","momento da força","момент силы"),
 'rk': T("krak (rastojanje od ose)","lever arm (distance from axis)","braccio (distanza dall’asse)","bras de levier (distance à l’axe)","brazo (distancia al eje)","Hebelarm (Abstand zur Achse)","braço (distância ao eixo)","плечо (расстояние до оси)"),
 'fi': T("ugao između r i F","angle between r and F","angolo tra r e F","angle entre r et F","ángulo entre r y F","Winkel zwischen r und F","ângulo entre r e F","угол между r и F"),
 'F1': T("prva sila","force 1","forza 1","force 1","fuerza 1","Kraft 1","força 1","первая сила"),
 'r1': T("krak prve sile","lever arm 1","braccio 1","bras de levier 1","brazo 1","Hebelarm 1","braço 1","плечо первой силы"),
 'F2': T("druga sila","force 2","forza 2","force 2","fuerza 2","Kraft 2","força 2","вторая сила"),
 'r2': T("krak druge sile","lever arm 2","braccio 2","bras de levier 2","brazo 2","Hebelarm 2","braço 2","плечо второй силы"),
 'D': T("torziona konstanta","torsion constant","costante di torsione","constante de torsion","constante de torsión","Richtmoment","constante de torção","крутильная жёсткость"),
 'fiu': T("ugao uvrtanja","angle of twist","angolo di torsione","angle de torsion","ángulo de torsión","Verdrillwinkel","ângulo de torção","угол закручивания"),
 'xT': T("položaj težišta","centre of mass position","posizione del baricentro","position du centre de masse","posición del centro de masas","Lage des Schwerpunkts","posição do centro de massa","положение центра масс"),
 'x1': T("položaj prvog tela","position of body 1","posizione del corpo 1","position du corps 1","posición del cuerpo 1","Lage von Körper 1","posição do corpo 1","положение первого тела"),
 'x2': T("položaj drugog tela","position of body 2","posizione del corpo 2","position du corps 2","posición del cuerpo 2","Lage von Körper 2","posição do corpo 2","положение второго тела"),
 'Fr': T("centripetalna sila","centripetal force","forza centripeta","force centripète","fuerza centrípeta","Zentripetalkraft","força centrípeta","центростремительная сила"),
 'v': T("brzina","velocity","velocità","vitesse","velocidad","Geschwindigkeit","velocidade","скорость"),
 'om': T("ugaona brzina","angular velocity","velocità angolare","vitesse angulaire","velocidad angular","Winkelgeschwindigkeit","velocidade angular","угловая скорость"),
 'rc': T("poluprečnik kružnice","radius of the circle","raggio della circonferenza","rayon du cercle","radio de la circunferencia","Kreisradius","raio da circunferência","радиус окружности"),
 'pi': T("impuls (količina kretanja)","momentum","quantità di moto","quantité de mouvement","cantidad de movimiento","Impuls","quantidade de movimento","импульс"),
 'dt': T("trajanje dejstva","duration","durata","durée","duración","Einwirkdauer","duração","время действия"),
 'dp': T("promena impulsa","change in momentum","variazione della quantità di moto","variation de la quantité de mouvement","variación de la cantidad de movimiento","Impulsänderung","variação da quantidade de movimento","изменение импульса"),
 'fm': T("maseni protok","mass flow rate","portata massica","débit massique","caudal másico","Massenstrom","vazão mássica","массовый расход"),
 'dv': T("brzina isticanja (relativna)","exhaust velocity (relative)","velocità di efflusso (relativa)","vitesse d’éjection (relative)","velocidad de salida (relativa)","Ausströmgeschwindigkeit (relativ)","velocidade de ejeção (relativa)","скорость истечения (относительная)"),
 'v1': T("brzina prvog tela","velocity of body 1","velocità del corpo 1","vitesse du corps 1","velocidad del cuerpo 1","Geschwindigkeit von Körper 1","velocidade do corpo 1","скорость первого тела"),
 'v2': T("brzina drugog tela","velocity of body 2","velocità del corpo 2","vitesse du corps 2","velocidad del cuerpo 2","Geschwindigkeit von Körper 2","velocidade do corpo 2","скорость второго тела"),
 'vz': T("zajednička brzina posle sudara","common velocity after collision","velocità comune dopo l’urto","vitesse commune après le choc","velocidad común tras el choque","gemeinsame Geschwindigkeit nach dem Stoß","velocidade comum após a colisão","общая скорость после удара"),
}
OZ = {'F': 'F', 'm': 'm', 'a': 'a', 'Fg': L('F_g', ru=r'F_{\text{т}}'), 'g': 'g', 'Gk': 'G', 'm1': 'm_1', 'm2': 'm_2', 'M': 'M',
      'r': 'r', 'R': 'R', 'gp': 'g', 'Ftr': FTR, 'FN': L('F_N', ru='N'), 'mu': r'\mu', 'alfa': r'\alpha', 'k': 'k', 'x': 'x',
      'k1': 'k_1', 'k2': 'k_2', 'kuk': 'k', 'p': 'p', 'S': 'S', 'dl': r'\Delta l', 'l': 'l', 'E': 'E', 'Mo': 'M',
      'rk': 'r', 'fi': r'\varphi', 'F1': 'F_1', 'r1': 'r_1', 'F2': 'F_2', 'r2': 'r_2', 'D': 'D', 'fiu': r'\varphi',
      'xT': 'x_T', 'x1': 'x_1', 'x2': 'x_2', 'Fr': 'F_r', 'v': 'v', 'om': r'\omega', 'rc': 'r', 'pi': 'p',
      'dt': r'\Delta t', 'dp': r'\Delta p', 'fm': r'\Phi_m', 'dv': r'\Delta v', 'v1': 'v_1', 'v2': 'v_2', 'vz': "v'"}
VRSTA = {'F': 'sila', 'm': 'masa', 'a': 'ubrzanje', 'Fg': 'sila', 'g': 'ubrzanje', 'Gk': 'gravKonst', 'm1': 'masa',
         'm2': 'masa', 'M': 'masa', 'r': 'duzina', 'R': 'duzina', 'gp': 'ubrzanje', 'Ftr': 'sila', 'FN': 'sila',
         'mu': 'bez', 'alfa': 'ugao', 'k': 'krutost', 'x': 'duzina', 'k1': 'krutost', 'k2': 'krutost', 'kuk': 'krutost',
         'p': 'pritisak', 'S': 'povrsina', 'dl': 'duzina', 'l': 'duzina', 'E': 'pritisak', 'Mo': 'moment', 'rk': 'duzina',
         'fi': 'ugao', 'F1': 'sila', 'r1': 'duzina', 'F2': 'sila', 'r2': 'duzina', 'D': 'torzija', 'fiu': 'ugao',
         'xT': 'duzina', 'x1': 'duzina', 'x2': 'duzina', 'Fr': 'sila', 'v': 'brzina', 'om': 'ugaonaBrzina', 'rc': 'duzina',
         'pi': 'impuls', 'dt': 'vreme', 'dp': 'impuls', 'fm': 'maseniProtok', 'dv': 'brzina', 'v1': 'brzina',
         'v2': 'brzina', 'vz': 'brzina'}
POZ = {'m', 'g', 'Gk', 'm1', 'm2', 'M', 'r', 'R', 'gp', 'FN', 'k', 'k1', 'k2', 'kuk', 'S', 'l', 'E', 'rk', 'r1', 'r2',
       'D', 'rc', 'dt', 'fm', 'Fg', 'Fr'}
NENEG = {'mu', 'Ftr'}

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
def sub(x, y, glavno, indeks):
    return f'<text x="{x:.1f}" y="{y:.1f}">{glavno}<tspan class="sub" dy="5">{indeks}</tspan></text>'

def crtez_strma(jez):
    a = math.radians(30)
    x0, y0, x1 = 24, 178, 276
    y1 = y0 - (x1 - x0) * math.tan(a)
    s = '<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += f'<path class="lik" d="M{x0},{y0} L{x1},{y0} L{x1},{y1:.1f} Z"/>'
    s += f'<path class="ugao" d="M{x0+40},{y0} A40,40 0 0,0 {x0+40*math.cos(a):.1f},{y0-40*math.sin(a):.1f}"/>'
    s += f'<text x="{x0+48}" y="{y0-7}">α</text>'
    # telo na kosini
    d = 150; cx, cy = x0 + d * math.cos(a), y0 - d * math.sin(a)
    ux, uy = math.cos(a), -math.sin(a); nx, ny = -math.sin(a), -math.cos(a)  # niz kosinu je -u
    w, h = 40, 26
    pts = [(cx - ux*w/2, cy - uy*w/2), (cx + ux*w/2, cy + uy*w/2), (cx + ux*w/2 + nx*h, cy + uy*w/2 + ny*h), (cx - ux*w/2 + nx*h, cy - uy*w/2 + ny*h)]
    s += '<path class="lik2" d="M' + ' L'.join(f'{p[0]:.1f},{p[1]:.1f}' for p in pts) + ' Z"/>'
    tx, ty = cx + nx*h/2, cy + ny*h/2  # središte tela
    # mg nadole
    s += strela(tx, ty, tx, ty + 70, 'lik-l')
    s += f'<text x="{tx+6:.1f}" y="{ty+78:.1f}">mg</text>'
    # komponenta niz kosinu
    L1 = 70 * math.sin(a)
    s += strela(tx, ty, tx - ux*L1*1.4, ty - uy*L1*1.4)
    s += sub(tx - ux*L1*1.4 - 34, ty - uy*L1*1.4 + 4, 'F', '∥')
    # normalna sila
    s += strela(tx, ty, tx + nx*58, ty + ny*58)
    s += sub(tx + nx*58 + 6, ty + ny*58 + 2, 'F', 'N' if jez != 'ru' else 'N')
    s += '</svg>'
    return s

def crtez_poluga():
    s = '<svg viewBox="0 0 300 190" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<rect class="lik" x="20" y="88" width="260" height="10" rx="4"/>'
    s += '<path class="lik2" d="M110,98 L96,132 L124,132 Z"/>'
    s += '<line class="osa" x1="80" y1="133" x2="140" y2="133"/>'
    s += strela(32, 30, 32, 86)
    s += sub(40, 44, 'F', '1')
    s += strela(268, 40, 268, 86)
    s += sub(242, 54, 'F', '2')
    # krakovi
    s += '<line class="osa" x1="32" y1="156" x2="110" y2="156"/><line class="osa" x1="32" y1="150" x2="32" y2="162"/><line class="osa" x1="110" y1="150" x2="110" y2="162"/>'
    s += '<line class="osa" x1="110" y1="170" x2="268" y2="170"/><line class="osa" x1="110" y1="164" x2="110" y2="176"/><line class="osa" x1="268" y1="164" x2="268" y2="176"/>'
    s += '<line class="pom" x1="32" y1="98" x2="32" y2="150"/><line class="pom" x1="268" y1="98" x2="268" y2="164"/>'
    s += sub(64, 150, 'r', '1') + sub(182, 188, 'r', '2')
    s += '</svg>'
    return s

teme = []

# 1 Njutnovi zakoni
teme.append({
 'id': 'njutnovi_zakoni', 'simbol': 'F',
 'naziv': T("Njutnovi zakoni","Newton’s laws","Leggi di Newton","Lois de Newton","Leyes de Newton","Newtonsche Gesetze","Leis de Newton","Законы Ньютона"),
 'opis': T("Sila, masa, ubrzanje","Force, mass, acceleration","Forza, massa, accelerazione","Force, masse, accélération","Fuerza, masa, aceleración","Kraft, Masse, Beschleunigung","Força, massa, aceleração","Сила, масса, ускорение"),
 'kljucne_reci': T("njutnov zakon sila masa ubrzanje tezina inercija akcija reakcija","newton law force mass acceleration weight inertia action reaction","legge di newton forza massa accelerazione peso inerzia azione reazione","loi de newton force masse acceleration poids inertie action reaction","ley de newton fuerza masa aceleracion peso inercia accion reaccion","newtonsches gesetz kraft masse beschleunigung gewicht tragheit actio reactio","lei de newton forca massa aceleracao peso inercia acao reacao","закон ньютона сила масса ускорение вес инерция действие противодействие"),
 'formule': [
  F(T("Prvi zakon (inercija)","First law (inertia)","Primo principio (inerzia)","Première loi (inertie)","Primera ley (inercia)","Erstes Gesetz (Trägheit)","Primeira lei (inércia)","Первый закон (инерция)"),
    r"\sum \vec F = 0 \;\Rightarrow\; \vec v = \text{const.}",
    T("Ako je zbir sila nula, telo miruje ili se kreće ravnomerno pravolinijski.","If the net force is zero, a body stays at rest or moves uniformly in a straight line.","Se la forza risultante è nulla, il corpo resta fermo o si muove di moto rettilineo uniforme.","Si la somme des forces est nulle, le corps reste immobile ou a un mouvement rectiligne uniforme.","Si la fuerza neta es cero, el cuerpo sigue en reposo o con movimiento rectilíneo uniforme.","Ist die Gesamtkraft null, bleibt der Körper in Ruhe oder bewegt sich gleichförmig geradlinig.","Se a força resultante é nula, o corpo fica em repouso ou em movimento retilíneo uniforme.","Если сумма сил равна нулю, тело покоится или движется равномерно и прямолинейно.")),
  F(T("Drugi zakon","Second law","Secondo principio","Deuxième loi","Segunda ley","Zweites Gesetz","Segunda lei","Второй закон"),
    r"\vec a = \frac{\vec F}{m}, \quad F = m\,a",
    T("Ubrzanje je srazmerno ukupnoj sili, a obrnuto srazmerno masi; 1 N = 1 kg·m/s².","Acceleration is proportional to the net force and inversely proportional to mass; 1 N = 1 kg·m/s².","L’accelerazione è proporzionale alla forza risultante e inversamente proporzionale alla massa; 1 N = 1 kg·m/s².","L’accélération est proportionnelle à la force résultante et inversement proportionnelle à la masse ; 1 N = 1 kg·m/s².","La aceleración es proporcional a la fuerza neta e inversamente proporcional a la masa; 1 N = 1 kg·m/s².","Die Beschleunigung ist proportional zur Gesamtkraft und umgekehrt proportional zur Masse; 1 N = 1 kg·m/s².","A aceleração é proporcional à força resultante e inversamente proporcional à massa; 1 N = 1 kg·m/s².","Ускорение пропорционально равнодействующей силе и обратно пропорционально массе; 1 Н = 1 кг·м/с².")),
  F(T("Treći zakon (akcija i reakcija)","Third law (action and reaction)","Terzo principio (azione e reazione)","Troisième loi (action et réaction)","Tercera ley (acción y reacción)","Drittes Gesetz (actio = reactio)","Terceira lei (ação e reação)","Третий закон (действие и противодействие)"),
    r"\vec F_{12} = -\vec F_{21}",
    T("Dva tela deluju jedno na drugo silama istog intenziteta, a suprotnog smera.","Two bodies act on each other with forces of equal magnitude and opposite direction.","Due corpi si scambiano forze di uguale intensità e verso opposto.","Deux corps exercent l’un sur l’autre des forces de même intensité et de sens opposés.","Dos cuerpos se ejercen fuerzas de igual módulo y sentido contrario.","Zwei Körper üben aufeinander gleich große, entgegengesetzte Kräfte aus.","Dois corpos exercem um sobre o outro forças de mesma intensidade e sentidos opostos.","Два тела действуют друг на друга силами, равными по модулю и противоположными по направлению.")),
  F(T("Težina (sila teže)","Weight","Forza peso","Poids","Peso","Gewichtskraft","Peso","Сила тяжести"),
    L(r"F_g = m\,g", ru=r"F_{\text{т}} = m\,g"),
    T("Sila kojom Zemlja privlači telo mase m; g ≈ 9,81 m/s².","Force with which the Earth pulls a body of mass m; g ≈ 9.81 m/s².","Forza con cui la Terra attira un corpo di massa m; g ≈ 9,81 m/s².","Force avec laquelle la Terre attire un corps de masse m ; g ≈ 9,81 m/s².","Fuerza con que la Tierra atrae un cuerpo de masa m; g ≈ 9,81 m/s².","Kraft, mit der die Erde einen Körper der Masse m anzieht; g ≈ 9,81 m/s².","Força com que a Terra atrai um corpo de massa m; g ≈ 9,81 m/s².","Сила, с которой Земля притягивает тело массой m; g ≈ 9,81 м/с².")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'm': 10, 'a': 2, 'Fg': None, 'g': 9.81}),
  'jednacine': [
   {'latex': r"F = m a", 'trazi': 'F', 'resenja': {'F': 'm*a', 'm': 'F/a', 'a': 'F/m'}},
   {'latex': L(r"F_g = m g", ru=r"F_{\text{т}} = m g"), 'trazi': 'Fg', 'resenja': {'Fg': 'm*g', 'm': 'Fg/g', 'g': 'Fg/m'}},
  ]}
})

# 2 Gravitacija
teme.append({
 'id': 'gravitacija', 'simbol': 'G',
 'naziv': T("Gravitacija","Gravitation","Gravitazione","Gravitation","Gravitación","Gravitation","Gravitação","Гравитация"),
 'opis': T("Njutnov zakon gravitacije","Newton’s law of gravitation","Legge di gravitazione","Loi de la gravitation","Ley de gravitación","Gravitationsgesetz","Lei da gravitação","Закон всемирного тяготения"),
 'kljucne_reci': T("gravitacija gravitaciona sila privlacenje planeta zemlja ubrzanje na povrsini","gravitation gravity gravitational force attraction planet earth surface gravity","gravitazione forza gravitazionale attrazione pianeta terra","gravitation attraction universelle planete terre pesanteur","gravitacion fuerza gravitatoria atraccion planeta tierra","gravitation gravitationskraft anziehung planet erde","gravitacao forca gravitacional atracao planeta terra","гравитация всемирное тяготение притяжение планета земля"),
 'formule': [
  F(T("Zakon gravitacije","Law of gravitation","Legge di gravitazione universale","Loi de la gravitation universelle","Ley de gravitación universal","Gravitationsgesetz","Lei da gravitação universal","Закон всемирного тяготения"),
    r"F = G\,\frac{m_1 m_2}{r^2}",
    T("Dva tela se privlače silom srazmernom proizvodu masa, a obrnuto srazmernom kvadratu rastojanja; G = 6,674 · 10⁻¹¹ N·m²/kg².","Two bodies attract with a force proportional to the product of their masses and inversely proportional to the squared distance; G = 6.674 · 10⁻¹¹ N·m²/kg².","Due corpi si attraggono con forza proporzionale al prodotto delle masse e inversamente al quadrato della distanza; G = 6,674 · 10⁻¹¹ N·m²/kg².","Deux corps s’attirent avec une force proportionnelle au produit des masses et inversement au carré de la distance ; G = 6,674 · 10⁻¹¹ N·m²/kg².","Dos cuerpos se atraen con una fuerza proporcional al producto de las masas e inversa al cuadrado de la distancia; G = 6,674 · 10⁻¹¹ N·m²/kg².","Zwei Körper ziehen sich mit einer Kraft an, die proportional zum Produkt der Massen und umgekehrt proportional zum Abstandsquadrat ist; G = 6,674 · 10⁻¹¹ N·m²/kg².","Dois corpos se atraem com força proporcional ao produto das massas e inversa ao quadrado da distância; G = 6,674 · 10⁻¹¹ N·m²/kg².","Два тела притягиваются с силой, пропорциональной произведению масс и обратно пропорциональной квадрату расстояния; G = 6,674 · 10⁻¹¹ Н·м²/кг².")),
  F(T("Ubrzanje na površini planete","Surface gravity of a planet","Gravità sulla superficie di un pianeta","Pesanteur à la surface d’une planète","Gravedad en la superficie de un planeta","Fallbeschleunigung an der Planetenoberfläche","Gravidade na superfície de um planeta","Ускорение свободного падения на планете"),
    r"m g = G\,\frac{m M}{R^2} \;\Rightarrow\; g = \frac{G M}{R^2}",
    T("Za Zemlju: M = 5,97 · 10²⁴ kg, R = 6371 km, pa je g ≈ 9,8 m/s².","For the Earth: M = 5.97 · 10²⁴ kg, R = 6371 km, so g ≈ 9.8 m/s².","Per la Terra: M = 5,97 · 10²⁴ kg, R = 6371 km, quindi g ≈ 9,8 m/s².","Pour la Terre : M = 5,97 · 10²⁴ kg, R = 6371 km, donc g ≈ 9,8 m/s².","Para la Tierra: M = 5,97 · 10²⁴ kg, R = 6371 km, así que g ≈ 9,8 m/s².","Für die Erde: M = 5,97 · 10²⁴ kg, R = 6371 km, also g ≈ 9,8 m/s².","Para a Terra: M = 5,97 · 10²⁴ kg, R = 6371 km, logo g ≈ 9,8 m/s².","Для Земли: M = 5,97 · 10²⁴ кг, R = 6371 км, поэтому g ≈ 9,8 м/с².")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'Gk': 6.6743e-11, 'm1': 70, 'm2': 5.972e24, 'r': 6.371e6, 'M': 5.972e24, 'R': 6.371e6, 'gp': None},
                       {'r': 'km', 'R': 'km'}),
  'jednacine': [
   {'latex': r"F = G \dfrac{m_1 m_2}{r^2}", 'trazi': 'F', 'promenljive': ['F', 'Gk', 'm1', 'm2', 'r'],
    'resenja': {'F': 'Gk*m1*m2/(r*r)', 'm1': 'F*r*r/(Gk*m2)', 'm2': 'F*r*r/(Gk*m1)', 'r': 'sqrt(Gk*m1*m2/F)'}},
   {'latex': r"g = \dfrac{G M}{R^2}", 'trazi': 'gp', 'promenljive': ['gp', 'Gk', 'M', 'R'],
    'resenja': {'gp': 'Gk*M/(R*R)', 'M': 'gp*R*R/Gk', 'R': 'sqrt(Gk*M/gp)'}},
  ]}
})

# 3 Trenje
teme.append({
 'id': 'trenje', 'simbol': 'μ',
 'naziv': T("Trenje","Friction","Attrito","Frottement","Rozamiento","Reibung","Atrito","Трение"),
 'opis': T("Koeficijent trenja","Coefficient of friction","Coefficiente d’attrito","Coefficient de frottement","Coeficiente de rozamiento","Reibungszahl","Coeficiente de atrito","Коэффициент трения"),
 'kljucne_reci': T("trenje sila trenja koeficijent trenja klizanje mirovanje statičko staticko","friction force coefficient kinetic static sliding","attrito radente statico dinamico coefficiente","frottement statique dynamique glissement coefficient","rozamiento friccion estatico dinamico coeficiente","reibung haftreibung gleitreibung reibungszahl","atrito estatico cinetico coeficiente","трение скольжения покоя коэффициент трения"),
 'formule': [
  F(T("Trenje klizanja","Kinetic friction","Attrito dinamico","Frottement de glissement","Rozamiento dinámico","Gleitreibung","Atrito cinético","Трение скольжения"),
    LJ(lambda j: Ftr(j) + (r" = \mu\,N" if j == 'ru' else r" = \mu\,F_N")),
    T("Sila trenja je srazmerna sili kojom telo pritiska podlogu; na vodoravnoj podlozi F_N = mg.","Friction is proportional to the normal force; on a horizontal surface F_N = mg.","L’attrito è proporzionale alla forza normale; su un piano orizzontale F_N = mg.","Le frottement est proportionnel à la force normale ; sur un plan horizontal F_N = mg.","El rozamiento es proporcional a la fuerza normal; sobre una superficie horizontal F_N = mg.","Die Reibung ist proportional zur Normalkraft; auf waagerechter Fläche ist F_N = mg.","O atrito é proporcional à força normal; numa superfície horizontal F_N = mg.","Сила трения пропорциональна силе нормального давления; на горизонтальной поверхности N = mg.")),
  F(T("Trenje mirovanja (najveće)","Static friction (maximum)","Attrito statico (massimo)","Frottement statique (maximal)","Rozamiento estático (máximo)","Haftreibung (maximal)","Atrito estático (máximo)","Трение покоя (наибольшее)"),
    LJ(lambda j: (r"F_{\text{тр,max}} = \mu_0\,N" if j == 'ru' else Ftr(j).replace('}', r',\max}', 1) + r" = \mu_s\,F_N")),
    T("Telo ostaje u mirovanju dok spoljašnja sila ne pređe ovu vrednost; obično je μ_s > μ.","The body stays at rest until the applied force exceeds this value; usually μ_s > μ.","Il corpo resta fermo finché la forza applicata non supera questo valore; di solito μ_s > μ.","Le corps reste immobile tant que la force appliquée ne dépasse pas cette valeur ; en général μ_s > μ.","El cuerpo sigue en reposo hasta que la fuerza aplicada supera este valor; normalmente μ_s > μ.","Der Körper bleibt in Ruhe, bis die Kraft diesen Wert übersteigt; meist ist μ_s > μ.","O corpo fica em repouso até a força aplicada exceder este valor; em geral μ_s > μ.","Тело покоится, пока внешняя сила не превысит это значение; обычно μ₀ > μ.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ftr': None, 'mu': 0.3, 'FN': 100, 'm': 10, 'g': 9.81}),
  'jednacine': [
   {'latex': LJ(lambda j: Ftr(j) + (r" = \mu N" if j == 'ru' else r" = \mu F_N")), 'trazi': 'Ftr',
    'resenja': {'Ftr': 'mu*FN', 'mu': 'Ftr/FN', 'FN': 'Ftr/mu'}},
   {'latex': LJ(lambda j: Ftr(j) + r" = \mu m g"), 'trazi': 'Ftr',
    'resenja': {'Ftr': 'mu*m*g', 'mu': 'Ftr/(m*g)', 'm': 'Ftr/(mu*g)'}, 'promenljive': ['Ftr', 'mu', 'm', 'g'],
    'napomene': {'Ftr': T("Telo na vodoravnoj podlozi.","Body on a horizontal surface.","Corpo su un piano orizzontale.","Corps sur un plan horizontal.","Cuerpo sobre una superficie horizontal.","Körper auf waagerechter Fläche.","Corpo numa superfície horizontal.","Тело на горизонтальной поверхности.")}},
  ]}
})

# 4 Strma ravan
teme.append({
 'id': 'strma_ravan', 'simbol': 'α',
 'naziv': T("Strma ravan","Inclined plane","Piano inclinato","Plan incliné","Plano inclinado","Schiefe Ebene","Plano inclinado","Наклонная плоскость"),
 'opis': T("Komponente težine, ubrzanje","Weight components, acceleration","Componenti del peso, accelerazione","Composantes du poids, accélération","Componentes del peso, aceleración","Komponenten der Gewichtskraft, Beschleunigung","Componentes do peso, aceleração","Составляющие силы тяжести, ускорение"),
 'kljucne_reci': T("strma ravan kosa ravan nagib klizanje niz strmu ravan","inclined plane slope ramp sliding down","piano inclinato rampa scivolamento","plan incline pente glissement","plano inclinado rampa deslizamiento","schiefe ebene hang rampe gleiten","plano inclinado rampa deslizamento","наклонная плоскость скольжение уклон"),
 'crtez': {j: crtez_strma(j) for j in J},
 'formule': [
  F(T("Komponente težine","Components of weight","Componenti del peso","Composantes du poids","Componentes del peso","Komponenten der Gewichtskraft","Componentes do peso","Составляющие силы тяжести"),
    L(r"F_\parallel = m g \sin\alpha, \quad F_N = m g \cos\alpha", ru=r"F_\parallel = m g \sin\alpha, \quad N = m g \cos\alpha"),
    T("F∥ vuče telo niz strmu ravan, a F_N ga pritiska uz podlogu.","F∥ pulls the body down the slope; F_N presses it against the surface.","F∥ tira il corpo lungo il piano; F_N lo preme contro la superficie.","F∥ entraîne le corps le long de la pente ; F_N le presse contre le plan.","F∥ arrastra el cuerpo pendiente abajo; F_N lo presiona contra la superficie.","F∥ zieht den Körper hangabwärts, F_N drückt ihn auf die Unterlage.","F∥ puxa o corpo plano abaixo; F_N o pressiona contra a superfície.","F∥ тянет тело вниз по склону, N прижимает его к поверхности.")),
  F(T("Ubrzanje niz strmu ravan","Acceleration down the slope","Accelerazione lungo il piano","Accélération le long de la pente","Aceleración pendiente abajo","Beschleunigung hangabwärts","Aceleração plano abaixo","Ускорение вниз по склону"),
    r"a = g\,(\sin\alpha - \mu \cos\alpha)",
    T("Bez trenja (μ = 0): a = g sin α. Ako je a ≤ 0, telo miruje (ako je trenje dovoljno).","Without friction (μ = 0): a = g sin α. If a ≤ 0, the body stays at rest (if friction is sufficient).","Senza attrito (μ = 0): a = g sin α. Se a ≤ 0, il corpo resta fermo (se l’attrito basta).","Sans frottement (μ = 0) : a = g sin α. Si a ≤ 0, le corps reste immobile (si le frottement suffit).","Sin rozamiento (μ = 0): a = g sen α. Si a ≤ 0, el cuerpo queda en reposo (si el rozamiento basta).","Ohne Reibung (μ = 0): a = g sin α. Ist a ≤ 0, bleibt der Körper in Ruhe (bei ausreichender Reibung).","Sem atrito (μ = 0): a = g sen α. Se a ≤ 0, o corpo fica em repouso (se o atrito bastar).","Без трения (μ = 0): a = g sin α. Если a ≤ 0, тело покоится (при достаточном трении).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'a': None, 'g': 9.81, 'alfa': PI / 6, 'mu': 0.2, 'm': 10, 'F': None, 'FN': None}, {'alfa': '°'}),
  'jednacine': [
   {'latex': r"a = g (\sin\alpha - \mu \cos\alpha)", 'trazi': 'a', 'promenljive': ['a', 'g', 'alfa', 'mu'],
    'resenja': {'a': 'g*(sin(alfa) - mu*cos(alfa))', 'mu': '(sin(alfa) - a/g)/cos(alfa)', 'g': 'a/(sin(alfa) - mu*cos(alfa))'}},
   {'latex': r"F_\parallel = m g \sin\alpha", 'trazi': 'F', 'promenljive': ['F', 'm', 'g', 'alfa'],
    'resenja': {'F': 'm*g*sin(alfa)', 'm': 'F/(g*sin(alfa))', 'alfa': 'asin(F/(m*g))'}},
   {'latex': L(r"F_N = m g \cos\alpha", ru=r"N = m g \cos\alpha"), 'trazi': 'FN', 'promenljive': ['FN', 'm', 'g', 'alfa'],
    'resenja': {'FN': 'm*g*cos(alfa)', 'm': 'FN/(g*cos(alfa))', 'alfa': 'acos(FN/(m*g))'}},
  ]}
})
# u ovoj temi F znači F∥
teme[-1]['kalkulator']['velicine']['F']['oznaka'] = r'F_\parallel'
teme[-1]['kalkulator']['velicine']['F']['naziv'] = T("sila niz strmu ravan","force along the slope","forza lungo il piano","force le long de la pente","fuerza a lo largo del plano","Hangabtriebskraft","força ao longo do plano","скатывающая сила")

# 5 Opruga
teme.append({
 'id': 'opruga', 'simbol': 'k',
 'naziv': T("Opruga (Hukov zakon)","Spring (Hooke’s law)","Molla (legge di Hooke)","Ressort (loi de Hooke)","Resorte (ley de Hooke)","Feder (Hookesches Gesetz)","Mola (lei de Hooke)","Пружина (закон Гука)"),
 'opis': T("Elastična sila, spajanje opruga","Elastic force, springs combined","Forza elastica, molle combinate","Force de rappel, ressorts associés","Fuerza elástica, resortes combinados","Federkraft, Federschaltungen","Força elástica, associação de molas","Сила упругости, соединение пружин"),
 'kljucne_reci': T("opruga hukov zakon elasticna sila konstanta opruge izduzenje redna paralelna veza","spring hooke law elastic force spring constant extension series parallel","molla legge di hooke forza elastica costante elastica serie parallelo","ressort loi de hooke force de rappel raideur serie parallele","resorte ley de hooke fuerza elastica constante serie paralelo","feder hooke federkraft federkonstante reihe parallel","mola lei de hooke forca elastica constante serie paralelo","пружина закон гука сила упругости жесткость последовательно параллельно"),
 'formule': [
  F(T("Hukov zakon","Hooke’s law","Legge di Hooke","Loi de Hooke","Ley de Hooke","Hookesches Gesetz","Lei de Hooke","Закон Гука"),
    r"F = k\,x",
    T("Sila potrebna da se opruga izduži (ili sabije) za x; k je konstanta opruge u N/m.","Force needed to stretch (or compress) a spring by x; k is the spring constant in N/m.","Forza necessaria per allungare (o comprimere) la molla di x; k è la costante elastica in N/m.","Force nécessaire pour allonger (ou comprimer) le ressort de x ; k est la raideur en N/m.","Fuerza necesaria para estirar (o comprimir) el resorte una longitud x; k es la constante en N/m.","Kraft, um die Feder um x zu dehnen (oder zu stauchen); k ist die Federkonstante in N/m.","Força necessária para esticar (ou comprimir) a mola de x; k é a constante elástica em N/m.","Сила, необходимая, чтобы растянуть (или сжать) пружину на x; k — жёсткость в Н/м.")),
  F(T("Paralelno vezane opruge","Springs in parallel","Molle in parallelo","Ressorts en parallèle","Resortes en paralelo","Parallel geschaltete Federn","Molas em paralelo","Параллельное соединение"),
    r"k = k_1 + k_2 + \cdots",
    T("Opruge jedna pored druge zajedno nose teret: sistem je krući.","Springs side by side share the load: the system is stiffer.","Molle affiancate si dividono il carico: il sistema è più rigido.","Ressorts côte à côte se partagent la charge : le système est plus raide.","Resortes uno al lado del otro comparten la carga: el sistema es más rígido.","Nebeneinander tragen die Federn gemeinsam: das System ist steifer.","Molas lado a lado dividem a carga: o sistema fica mais rígido.","Пружины рядом делят нагрузку: система жёстче.")),
  F(T("Redno vezane opruge","Springs in series","Molle in serie","Ressorts en série","Resortes en serie","In Reihe geschaltete Federn","Molas em série","Последовательное соединение"),
    r"\frac{1}{k} = \frac{1}{k_1} + \frac{1}{k_2} + \cdots",
    T("Opruge jedna za drugom: sistem je mekši od svake pojedinačne opruge.","Springs one after another: the system is softer than each spring alone.","Molle una dopo l’altra: il sistema è più morbido di ciascuna molla.","Ressorts l’un après l’autre : le système est plus souple que chaque ressort.","Resortes uno tras otro: el sistema es más blando que cada resorte.","Federn hintereinander: das System ist weicher als jede einzelne Feder.","Molas uma após a outra: o sistema é mais macio que cada mola.","Пружины одна за другой: система мягче каждой пружины.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'k': 200, 'x': 0.05, 'kuk': None, 'k1': 100, 'k2': 300}, {'x': 'cm'}),
  'jednacine': [
   {'latex': r"F = k x", 'trazi': 'F', 'resenja': {'F': 'k*x', 'k': 'F/x', 'x': 'F/k'}},
   {'latex': r"k = k_1 + k_2", 'trazi': 'kuk', 'resenja': {'kuk': 'k1 + k2', 'k1': 'kuk - k2', 'k2': 'kuk - k1'}},
   {'latex': r"\dfrac{1}{k} = \dfrac{1}{k_1} + \dfrac{1}{k_2}", 'trazi': 'kuk',
    'resenja': {'kuk': 'k1*k2/(k1 + k2)', 'k1': '1/(1/kuk - 1/k2)', 'k2': '1/(1/kuk - 1/k1)'}},
  ]}
})

# 6 Pritisak i deformacija
teme.append({
 'id': 'naprezanje', 'simbol': 'p',
 'naziv': T("Pritisak i deformacija","Pressure and deformation","Pressione e deformazione","Pression et déformation","Presión y deformación","Druck und Verformung","Pressão e deformação","Давление и деформация"),
 'opis': T("p = F/S, Jangov modul","p = F/S, Young’s modulus","p = F/S, modulo di Young","p = F/S, module de Young","p = F/S, módulo de Young","p = F/S, Elastizitätsmodul","p = F/S, módulo de Young","p = F/S, модуль Юнга"),
 'kljucne_reci': T("pritisak sila povrsina pascal deformacija istezanje jangov modul elasticnosti napon sipka zica","pressure force area pascal deformation stretching young modulus stress strain rod wire","pressione forza area pascal deformazione modulo di young sforzo filo","pression force surface pascal deformation module de young contrainte fil","presion fuerza area pascal deformacion modulo de young tension alambre","druck kraft flache pascal verformung dehnung elastizitatsmodul spannung draht","pressao forca area pascal deformacao modulo de young tensao fio","давление сила площадь паскаль деформация модуль юнга напряжение проволока"),
 'formule': [
  F(T("Pritisak","Pressure","Pressione","Pression","Presión","Druck","Pressão","Давление"),
    r"p = \frac{F}{S}",
    T("Sila koja deluje normalno na površinu S, podeljena tom površinom; 1 Pa = 1 N/m².","Force acting perpendicular to area S divided by that area; 1 Pa = 1 N/m².","Forza perpendicolare alla superficie S divisa per S; 1 Pa = 1 N/m².","Force perpendiculaire à la surface S divisée par S ; 1 Pa = 1 N/m².","Fuerza perpendicular a la superficie S dividida por S; 1 Pa = 1 N/m².","Senkrecht auf die Fläche S wirkende Kraft geteilt durch S; 1 Pa = 1 N/m².","Força perpendicular à superfície S dividida por S; 1 Pa = 1 N/m².","Сила, перпендикулярная площади S, делённая на S; 1 Па = 1 Н/м².")),
  F(T("Istezanje šipke ili žice","Stretching a rod or wire","Allungamento di una barra o di un filo","Allongement d’une barre ou d’un fil","Alargamiento de una barra o un alambre","Dehnung eines Stabes oder Drahtes","Alongamento de uma barra ou fio","Растяжение стержня или проволоки"),
    r"\frac{\Delta l}{l} = \frac{1}{E}\,\frac{F}{S}",
    T("Relativno izduženje je srazmerno naponu F/S; E je modul elastičnosti materijala (čelik ≈ 200 GPa).","Relative elongation is proportional to stress F/S; E is the material’s Young’s modulus (steel ≈ 200 GPa).","L’allungamento relativo è proporzionale allo sforzo F/S; E è il modulo di Young (acciaio ≈ 200 GPa).","L’allongement relatif est proportionnel à la contrainte F/S ; E est le module de Young (acier ≈ 200 GPa).","El alargamiento relativo es proporcional a la tensión F/S; E es el módulo de Young (acero ≈ 200 GPa).","Die relative Dehnung ist proportional zur Spannung F/S; E ist der Elastizitätsmodul (Stahl ≈ 200 GPa).","O alongamento relativo é proporcional à tensão F/S; E é o módulo de Young (aço ≈ 200 GPa).","Относительное удлинение пропорционально напряжению F/S; E — модуль Юнга (сталь ≈ 200 ГПа).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'p': None, 'F': 500, 'S': 0.01, 'dl': None, 'l': 2, 'E': 2e11}, {'S': 'cm²', 'p': 'kPa', 'dl': 'mm', 'E': 'GPa'}),
  'jednacine': [
   {'latex': r"p = \dfrac{F}{S}", 'trazi': 'p', 'resenja': {'p': 'F/S', 'F': 'p*S', 'S': 'F/p'}},
   {'latex': r"\Delta l = \dfrac{F\, l}{E\, S}", 'trazi': 'dl',
    'resenja': {'dl': 'F*l/(E*S)', 'F': 'dl*E*S/l', 'l': 'dl*E*S/F', 'E': 'F*l/(dl*S)', 'S': 'F*l/(E*dl)'}},
  ]}
})
# u temi naprezanje S je presek žice: podrazumevano 1 mm² za drugu formulu bi bilo realnije, ali ostaje zajednička vrednost

# 7 Moment sile
teme.append({
 'id': 'moment_sile', 'simbol': 'M',
 'naziv': T("Moment sile i poluga","Torque and lever","Momento e leva","Moment et levier","Momento y palanca","Drehmoment und Hebel","Momento e alavanca","Момент силы и рычаг"),
 'opis': T("Krak, ravnoteža poluge","Lever arm, lever balance","Braccio, equilibrio della leva","Bras de levier, équilibre","Brazo, equilibrio de la palanca","Hebelarm, Hebelgesetz","Braço, equilíbrio da alavanca","Плечо, равновесие рычага"),
 'kljucne_reci': T("moment sile krak poluga ravnoteza obrtni moment torzija","torque moment of force lever arm balance equilibrium torsion","momento della forza braccio leva equilibrio torsione","moment de force bras de levier equilibre torsion","momento de fuerza par brazo palanca equilibrio torsion","drehmoment hebelarm hebelgesetz gleichgewicht torsion","momento torque braco alavanca equilibrio torcao","момент силы плечо рычаг равновесие кручение"),
 'crtez': crtez_poluga(),
 'formule': [
  F(T("Moment sile","Torque","Momento della forza","Moment de la force","Momento de la fuerza","Drehmoment","Momento da força","Момент силы"),
    r"\vec M = \vec r \times \vec F, \quad M = r F \sin\varphi = r' F",
    T("r je rastojanje od ose do napadne tačke sile, a r′ = r sin φ je krak sile (normalno rastojanje od ose do pravca sile).","r is the distance from the axis to where the force acts; r′ = r sin φ is the lever arm (perpendicular distance to the line of force).","r è la distanza dall’asse al punto di applicazione; r′ = r sin φ è il braccio della forza.","r est la distance de l’axe au point d’application ; r′ = r sin φ est le bras de levier.","r es la distancia del eje al punto de aplicación; r′ = r sen φ es el brazo de la fuerza.","r ist der Abstand von der Achse zum Angriffspunkt; r′ = r sin φ ist der Hebelarm.","r é a distância do eixo ao ponto de aplicação; r′ = r sen φ é o braço da força.","r — расстояние от оси до точки приложения силы; r′ = r sin φ — плечо силы.")),
  F(T("Ravnoteža poluge","Lever balance","Equilibrio della leva","Équilibre du levier","Equilibrio de la palanca","Hebelgesetz","Equilíbrio da alavanca","Равновесие рычага"),
    r"F_1 r_1 = F_2 r_2",
    T("Poluga je u ravnoteži kada su momenti sila sa obe strane ose jednaki.","A lever balances when the torques on both sides of the pivot are equal.","La leva è in equilibrio quando i momenti ai due lati del fulcro sono uguali.","Le levier est en équilibre quand les moments des deux côtés du pivot sont égaux.","La palanca está en equilibrio cuando los momentos a ambos lados del apoyo son iguales.","Der Hebel ist im Gleichgewicht, wenn die Drehmomente auf beiden Seiten gleich sind.","A alavanca está em equilíbrio quando os momentos dos dois lados do apoio são iguais.","Рычаг в равновесии, когда моменты сил по обе стороны оси равны.")),
  F(T("Uvrtanje (torzija)","Torsion","Torsione","Torsion","Torsión","Torsion","Torção","Кручение"),
    r"M = D\,\varphi",
    T("Moment potreban da se žica ili opruga uvrne za ugao φ; D je torziona konstanta.","Torque needed to twist a wire or spring by angle φ; D is the torsion constant.","Momento necessario per torcere un filo di un angolo φ; D è la costante di torsione.","Moment nécessaire pour tordre un fil d’un angle φ ; D est la constante de torsion.","Momento necesario para torcer un alambre un ángulo φ; D es la constante de torsión.","Drehmoment, um einen Draht um den Winkel φ zu verdrillen; D ist das Richtmoment.","Momento necessário para torcer um fio de um ângulo φ; D é a constante de torção.","Момент, необходимый для закручивания проволоки на угол φ; D — крутильная жёсткость.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Mo': None, 'rk': 0.3, 'F': 50, 'fi': PI / 2, 'F1': 200, 'r1': 0.5, 'F2': None, 'r2': 1.5, 'D': 0.02, 'fiu': PI / 6},
                       {'fi': '°', 'fiu': '°'}),
  'jednacine': [
   {'latex': r"M = r F \sin\varphi", 'trazi': 'Mo', 'promenljive': ['Mo', 'rk', 'F', 'fi'],
    'resenja': {'Mo': 'rk*F*sin(fi)', 'rk': 'Mo/(F*sin(fi))', 'F': 'Mo/(rk*sin(fi))'}},
   {'latex': r"F_1 r_1 = F_2 r_2", 'trazi': 'F2',
    'resenja': {'F2': 'F1*r1/r2', 'F1': 'F2*r2/r1', 'r1': 'F2*r2/F1', 'r2': 'F1*r1/F2'}},
   {'latex': r"M = D \varphi", 'trazi': 'Mo', 'resenja': {'Mo': 'D*fiu', 'D': 'Mo/fiu', 'fiu': 'Mo/D'}},
  ]}
})

# 8 Težište
teme.append({
 'id': 'teziste', 'simbol': 'x_T'.replace('_T', 'ₜ'),
 'naziv': T("Težište","Centre of mass","Baricentro","Centre de masse","Centro de masas","Schwerpunkt","Centro de massa","Центр масс"),
 'opis': T("Položaj težišta sistema tela","Centre of mass of several bodies","Baricentro di un sistema di corpi","Centre de masse d’un système","Centro de masas de un sistema","Schwerpunkt mehrerer Körper","Centro de massa de um sistema","Центр масс системы тел"),
 'kljucne_reci': T("teziste centar mase sistem tela ravnoteza","centre of mass center of gravity system of bodies balance","baricentro centro di massa sistema di corpi","centre de masse centre de gravite systeme","centro de masas centro de gravedad sistema","schwerpunkt massenmittelpunkt","centro de massa centro de gravidade sistema","центр масс центр тяжести система тел"),
 'formule': [
  F(T("Težište","Centre of mass","Baricentro","Centre de masse","Centro de masas","Schwerpunkt","Centro de massa","Центр масс"),
    r"x_T = \frac{m_1 x_1 + m_2 x_2 + m_3 x_3 + \cdots}{m_1 + m_2 + m_3 + \cdots}",
    T("Isto važi i za koordinate y i z. Težište je bliže težem telu.","The same holds for the y and z coordinates. The centre of mass is closer to the heavier body.","Lo stesso vale per le coordinate y e z. Il baricentro è più vicino al corpo più pesante.","Idem pour les coordonnées y et z. Le centre de masse est plus proche du corps le plus lourd.","Lo mismo vale para las coordenadas y y z. El centro de masas está más cerca del cuerpo más pesado.","Ebenso für y und z. Der Schwerpunkt liegt näher am schwereren Körper.","O mesmo vale para y e z. O centro de massa fica mais perto do corpo mais pesado.","То же для координат y и z. Центр масс ближе к более тяжёлому телу.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'xT': None, 'm1': 2, 'x1': 0, 'm2': 3, 'x2': 1}),
  'jednacine': [
   {'latex': r"x_T = \dfrac{m_1 x_1 + m_2 x_2}{m_1 + m_2}", 'trazi': 'xT',
    'resenja': {'xT': '(m1*x1 + m2*x2)/(m1 + m2)', 'x1': '(xT*(m1 + m2) - m2*x2)/m1', 'x2': '(xT*(m1 + m2) - m1*x1)/m2',
                'm1': 'm2*(x2 - xT)/(xT - x1)', 'm2': 'm1*(xT - x1)/(x2 - xT)'}},
  ]}
})
teme[-1]['simbol'] = 'T'

# 9 Centripetalna sila
teme.append({
 'id': 'centripetalna', 'simbol': 'Fᵣ',
 'naziv': T("Centripetalna sila","Centripetal force","Forza centripeta","Force centripète","Fuerza centrípeta","Zentripetalkraft","Força centrípeta","Центростремительная сила"),
 'opis': T("Sila pri kružnom kretanju","Force in circular motion","Forza nel moto circolare","Force du mouvement circulaire","Fuerza en el movimiento circular","Kraft bei der Kreisbewegung","Força no movimento circular","Сила при движении по окружности"),
 'kljucne_reci': T("centripetalna sila kruzno kretanje krivina zavoj radijalna sila","centripetal force circular motion curve turn radial force","forza centripeta moto circolare curva","force centripete mouvement circulaire virage","fuerza centripeta movimiento circular curva","zentripetalkraft kreisbewegung kurve radialkraft","forca centripeta movimento circular curva","центростремительная сила движение по окружности поворот"),
 'formule': [
  F(T("Centripetalna sila","Centripetal force","Forza centripeta","Force centripète","Fuerza centrípeta","Zentripetalkraft","Força centrípeta","Центростремительная сила"),
    r"F_r = m\,a_r = m \frac{v^2}{r} = m\,\omega^2 r",
    T("Ukupna sila usmerena ka središtu kružnice, potrebna da telo ide po krugu.","Net force pointing to the centre, needed to keep the body on the circle.","Forza risultante diretta verso il centro, necessaria per mantenere il corpo sulla circonferenza.","Force résultante dirigée vers le centre, nécessaire pour rester sur le cercle.","Fuerza neta hacia el centro, necesaria para mantener el cuerpo en la circunferencia.","Zum Mittelpunkt gerichtete Gesamtkraft, die den Körper auf der Kreisbahn hält.","Força resultante dirigida ao centro, necessária para manter o corpo na circunferência.","Равнодействующая, направленная к центру, удерживающая тело на окружности.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Fr': None, 'm': 1000, 'v': 20, 'rc': 50, 'om': 2}, {'v': 'km/h'}),
  'jednacine': [
   {'latex': r"F_r = m \dfrac{v^2}{r}", 'trazi': 'Fr', 'resenja': {'Fr': 'm*v*v/rc', 'm': 'Fr*rc/(v*v)', 'v': 'sqrt(Fr*rc/m)', 'rc': 'm*v*v/Fr'}},
   {'latex': r"F_r = m \omega^2 r", 'trazi': 'Fr', 'resenja': {'Fr': 'm*om*om*rc', 'm': 'Fr/(om*om*rc)', 'om': 'sqrt(Fr/(m*rc))', 'rc': 'Fr/(m*om*om)'}},
  ]}
})

# 10 Impuls
teme.append({
 'id': 'impuls', 'simbol': 'p',
 'naziv': T("Impuls i sudari","Momentum and collisions","Quantità di moto e urti","Quantité de mouvement et chocs","Cantidad de movimiento y choques","Impuls und Stöße","Quantidade de movimento e colisões","Импульс и удары"),
 'opis': T("p = mv, impuls sile","p = mv, impulse","p = mv, impulso","p = mv, impulsion","p = mv, impulso","p = mv, Kraftstoß","p = mv, impulso","p = mv, импульс силы"),
 'kljucne_reci': T("impuls kolicina kretanja impuls sile zakon odrzanja impulsa sudar neelastican reaktivna sila raketa","momentum impulse conservation of momentum collision inelastic thrust rocket","quantita di moto impulso conservazione urto anelastico spinta razzo","quantite de mouvement impulsion conservation choc inelastique poussee fusee","cantidad de movimiento momento lineal impulso conservacion choque inelastico empuje cohete","impuls kraftstoss impulserhaltung stoss unelastisch schub rakete","quantidade de movimento momento linear impulso conservacao colisao inelastica empuxo foguete","импульс количество движения импульс силы закон сохранения удар неупругий реактивная сила ракета"),
 'formule': [
  F(T("Impuls tela","Momentum","Quantità di moto","Quantité de mouvement","Cantidad de movimiento","Impuls","Quantidade de movimento","Импульс тела"),
    r"\vec p = m\,\vec v",
    T("Vektor istog smera kao brzina; jedinica kg·m/s.","A vector in the direction of velocity; unit kg·m/s.","Vettore con la stessa direzione della velocità; unità kg·m/s.","Vecteur de même direction que la vitesse ; unité kg·m/s.","Vector con la dirección de la velocidad; unidad kg·m/s.","Vektor in Richtung der Geschwindigkeit; Einheit kg·m/s.","Vetor na direção da velocidade; unidade kg·m/s.","Вектор, направленный как скорость; единица кг·м/с.")),
  F(T("Impuls sile","Impulse","Impulso","Impulsion","Impulso","Kraftstoß","Impulso","Импульс силы"),
    r"\vec F\,\Delta t = \Delta \vec p",
    T("Sila koja deluje vreme Δt menja impuls tela; zato vazdušni jastuk produžava Δt i smanjuje silu.","A force acting for time Δt changes the momentum; an airbag lengthens Δt and so reduces the force.","Una forza che agisce per Δt cambia la quantità di moto; l’airbag allunga Δt e riduce la forza.","Une force agissant pendant Δt modifie la quantité de mouvement ; l’airbag allonge Δt et réduit la force.","Una fuerza que actúa durante Δt cambia la cantidad de movimiento; el airbag alarga Δt y reduce la fuerza.","Eine Kraft, die Δt lang wirkt, ändert den Impuls; der Airbag verlängert Δt und verringert die Kraft.","Uma força atuando durante Δt muda a quantidade de movimento; o airbag aumenta Δt e reduz a força.","Сила, действующая время Δt, меняет импульс; подушка безопасности увеличивает Δt и уменьшает силу.")),
  F(T("Zakon održanja impulsa","Conservation of momentum","Conservazione della quantità di moto","Conservation de la quantité de mouvement","Conservación de la cantidad de movimiento","Impulserhaltung","Conservação da quantidade de movimento","Закон сохранения импульса"),
    r"m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2', \quad v' = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}",
    T("Bez spoljašnjih sila ukupni impuls se ne menja. Drugi izraz: savršeno neelastičan sudar (tela se slepe).","Without external forces the total momentum is constant. Second formula: perfectly inelastic collision (bodies stick together).","Senza forze esterne la quantità di moto totale si conserva. Seconda formula: urto perfettamente anelastico.","Sans forces extérieures la quantité de mouvement totale se conserve. Seconde formule : choc parfaitement mou.","Sin fuerzas externas la cantidad de movimiento total se conserva. Segunda fórmula: choque perfectamente inelástico.","Ohne äußere Kräfte bleibt der Gesamtimpuls erhalten. Zweite Formel: vollkommen unelastischer Stoß.","Sem forças externas a quantidade de movimento total se conserva. Segunda fórmula: colisão perfeitamente inelástica.","Без внешних сил полный импульс сохраняется. Вторая формула — абсолютно неупругий удар (тела слипаются).")),
  F(T("Reaktivna sila (raketa)","Thrust (rocket)","Spinta (razzo)","Poussée (fusée)","Empuje (cohete)","Schubkraft (Rakete)","Empuxo (foguete)","Реактивная сила (ракета)"),
    r"\vec F = -\Phi_m\,\Delta\vec v",
    T("Gas koji ističe masenim protokom Φ_m relativnom brzinom Δv gura raketu suprotno od smera isticanja.","Gas ejected at mass flow rate Φ_m with relative speed Δv pushes the rocket the opposite way.","Il gas espulso con portata Φ_m e velocità relativa Δv spinge il razzo in verso opposto.","Le gaz éjecté avec un débit Φ_m à la vitesse relative Δv pousse la fusée en sens inverse.","El gas expulsado con caudal Φ_m a velocidad relativa Δv empuja el cohete en sentido contrario.","Das mit Massenstrom Φ_m und Relativgeschwindigkeit Δv ausströmende Gas treibt die Rakete entgegengesetzt an.","O gás expelido com vazão Φ_m e velocidade relativa Δv empurra o foguete no sentido oposto.","Газ, вытекающий с массовым расходом Φ_m и относительной скоростью Δv, толкает ракету в обратную сторону.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'pi': None, 'm': 0.15, 'v': 40, 'F': None, 'dt': 0.01, 'dp': 6, 'vz': None, 'm1': 1000, 'v1': 20, 'm2': 1500, 'v2': 0, 'fm': 2, 'dv': 2500},
                       {'dt': 'ms'}),
  'jednacine': [
   {'latex': r"p = m v", 'trazi': 'pi', 'resenja': {'pi': 'm*v', 'm': 'pi/v', 'v': 'pi/m'}},
   {'latex': r"F \Delta t = \Delta p", 'trazi': 'F', 'resenja': {'F': 'dp/dt', 'dt': 'dp/F', 'dp': 'F*dt'}},
   {'latex': r"v' = \dfrac{m_1 v_1 + m_2 v_2}{m_1 + m_2}", 'trazi': 'vz',
    'resenja': {'vz': '(m1*v1 + m2*v2)/(m1 + m2)', 'v1': '(vz*(m1 + m2) - m2*v2)/m1', 'v2': '(vz*(m1 + m2) - m1*v1)/m2',
                'm1': 'm2*(v2 - vz)/(vz - v1)', 'm2': 'm1*(vz - v1)/(v2 - vz)'}},
   {'latex': r"F = \Phi_m \Delta v", 'trazi': 'F', 'resenja': {'F': 'fm*dv', 'fm': 'F/dv', 'dv': 'F/fm'},
    'napomene': {'F': T("Prikazana je jačina reaktivne sile.","Magnitude of the thrust is shown.","È mostrato il modulo della spinta.","L’intensité de la poussée est affichée.","Se muestra el módulo del empuje.","Angezeigt ist der Betrag der Schubkraft.","É mostrado o módulo do empuxo.","Показан модуль реактивной силы.")}},
  ]}
})
# u temi impuls F je sila udara/potiska
teme[-1]['kalkulator']['velicine']['F']['naziv'] = T("sila","force","forza","force","fuerza","Kraft","força","сила")

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)

ZAMENE = [('F_N', 'Fₙ'), ('μ_s', 'μₛ'), ('Φ_m', 'Φₘ')]
def ocisti(o):
    for j in J:
        if j in o:
            for a, b in ZAMENE: o[j] = o[j].replace(a, b)
for t in teme:
    for f in t['formule']:
        if isinstance(f.get('objasnjenje'), dict): ocisti(f['objasnjenje'])

out = {'oblast': 'sile', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
