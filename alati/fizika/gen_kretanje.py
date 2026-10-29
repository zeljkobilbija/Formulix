# Generiše assets/oblasti/kretanje.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def L(osnovni, **izuzeci):
    """LaTeX: isti za sve jezike osim navedenih izuzetaka."""
    if not izuzeci: return osnovni
    return {j: izuzeci.get(j, osnovni) for j in J}

PI = math.pi

# ---------- veličine ----------
N = {
 'pos': T("položaj","position","posizione","position","posición","Position","posição","положение"),
 's0': T("početni položaj","initial position","posizione iniziale","position initiale","posición inicial","Anfangsposition","posição inicial","начальное положение"),
 's': T("pređeni put","distance","spazio percorso","distance parcourue","distancia recorrida","zurückgelegter Weg","distância percorrida","пройденный путь"),
 'v': T("brzina","velocity","velocità","vitesse","velocidad","Geschwindigkeit","velocidade","скорость"),
 'v0': T("početna brzina","initial velocity","velocità iniziale","vitesse initiale","velocidad inicial","Anfangsgeschwindigkeit","velocidade inicial","начальная скорость"),
 'vsr': T("srednja brzina","average velocity","velocità media","vitesse moyenne","velocidad media","Durchschnittsgeschwindigkeit","velocidade média","средняя скорость"),
 't': T("vreme","time","tempo","temps","tiempo","Zeit","tempo","время"),
 'a': T("ubrzanje","acceleration","accelerazione","accélération","aceleración","Beschleunigung","aceleração","ускорение"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'h': T("visina pada","fall height","altezza di caduta","hauteur de chute","altura de caída","Fallhöhe","altura de queda","высота падения"),
 'H': T("najveća visina","maximum height","altezza massima","hauteur maximale","altura máxima","maximale Höhe","altura máxima","максимальная высота"),
 'tp': T("vreme penjanja","rise time","tempo di salita","durée de la montée","tiempo de subida","Steigzeit","tempo de subida","время подъёма"),
 'D': T("domet","range","gittata","portée","alcance","Wurfweite","alcance","дальность полёта"),
 'tL': T("vreme leta","flight time","tempo di volo","durée du vol","tiempo de vuelo","Flugzeit","tempo de voo","время полёта"),
 'alfa': T("ugao izbačaja","launch angle","angolo di lancio","angle de tir","ángulo de lanzamiento","Abwurfwinkel","ângulo de lançamento","угол бросания"),
 'T': T("period (vreme jednog obrta)","period","periodo","période","período","Umlaufzeit (Periode)","período","период"),
 'f': T("frekvencija","frequency","frequenza","fréquence","frecuencia","Frequenz","frequência","частота"),
 'om': T("ugaona brzina","angular velocity","velocità angolare","vitesse angulaire","velocidad angular","Winkelgeschwindigkeit","velocidade angular","угловая скорость"),
 'om0': T("početna ugaona brzina","initial angular velocity","velocità angolare iniziale","vitesse angulaire initiale","velocidad angular inicial","Anfangswinkelgeschwindigkeit","velocidade angular inicial","начальная угловая скорость"),
 'r': T("poluprečnik","radius","raggio","rayon","radio","Radius","raio","радиус"),
 'ar': T("radijalno (centripetalno) ubrzanje","centripetal acceleration","accelerazione centripeta","accélération centripète","aceleración centrípeta","Zentripetalbeschleunigung","aceleração centrípeta","центростремительное ускорение"),
 'at': T("tangencijalno ubrzanje","tangential acceleration","accelerazione tangenziale","accélération tangentielle","aceleración tangencial","Tangentialbeschleunigung","aceleração tangencial","касательное ускорение"),
 'au': T("ukupno ubrzanje","total acceleration","accelerazione totale","accélération totale","aceleración total","Gesamtbeschleunigung","aceleração total","полное ускорение"),
 'fi': T("ugao obrtanja","angle of rotation","angolo di rotazione","angle de rotation","ángulo girado","Drehwinkel","ângulo de rotação","угол поворота"),
 'l': T("dužina luka","arc length","lunghezza dell’arco","longueur de l’arc","longitud del arco","Bogenlänge","comprimento do arco","длина дуги"),
 'eps': T("ugaono ubrzanje","angular acceleration","accelerazione angolare","accélération angulaire","aceleración angular","Winkelbeschleunigung","aceleração angular","угловое ускорение"),
 'fV': T("zapreminski protok","volume flow rate","portata volumetrica","débit volumique","caudal volumétrico","Volumenstrom","vazão volumétrica","объёмный расход"),
 'fm': T("maseni protok","mass flow rate","portata massica","débit massique","caudal másico","Massenstrom","vazão mássica","массовый расход"),
 'S': T("površina preseka","cross-sectional area","area della sezione","aire de la section","área de la sección","Querschnittsfläche","área da seção","площадь сечения"),
 'V': T("zapremina","volume","volume","volume","volumen","Volumen","volume","объём"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'rho': T("gustina","density","densità","masse volumique","densidad","Dichte","massa específica","плотность"),
 'S1': T("presek 1","cross-section 1","sezione 1","section 1","sección 1","Querschnitt 1","seção 1","сечение 1"),
 'v1': T("brzina u preseku 1","velocity at section 1","velocità nella sezione 1","vitesse dans la section 1","velocidad en la sección 1","Geschwindigkeit im Querschnitt 1","velocidade na seção 1","скорость в сечении 1"),
 'S2': T("presek 2","cross-section 2","sezione 2","section 2","sección 2","Querschnitt 2","seção 2","сечение 2"),
 'v2': T("brzina u preseku 2","velocity at section 2","velocità nella sezione 2","vitesse dans la section 2","velocidad en la sección 2","Geschwindigkeit im Querschnitt 2","velocidade na seção 2","скорость в сечении 2"),
}
OZ = {'pos': 's', 's0': 's_0', 's': 's', 'v': 'v', 'v0': 'v_0', 'vsr': r'\bar v', 't': 't', 'a': 'a', 'g': 'g',
      'h': 'h', 'H': 'H', 'tp': 't_p', 'D': 'D', 'tL': 't_L', 'alfa': r'\alpha', 'T': 'T',
      'f': L('f', ru=r'\nu'), 'om': r'\omega', 'om0': r'\omega_0', 'r': 'r', 'ar': 'a_r', 'at': 'a_t',
      'au': 'a', 'fi': r'\varphi', 'l': 'l', 'eps': L(r'\alpha', ru=r'\varepsilon'), 'fV': r'\Phi_V',
      'fm': r'\Phi_m', 'S': 'S', 'V': 'V', 'm': 'm', 'rho': r'\rho', 'S1': 'S_1', 'v1': 'v_1', 'S2': 'S_2', 'v2': 'v_2'}
VRSTA = {'pos': 'duzina', 's0': 'duzina', 's': 'duzina', 'v': 'brzina', 'v0': 'brzina', 'vsr': 'brzina',
         't': 'vreme', 'a': 'ubrzanje', 'g': 'ubrzanje', 'h': 'duzina', 'H': 'duzina', 'tp': 'vreme',
         'D': 'duzina', 'tL': 'vreme', 'alfa': 'ugao', 'T': 'vreme', 'f': 'frekvencija', 'om': 'ugaonaBrzina',
         'om0': 'ugaonaBrzina', 'r': 'duzina', 'ar': 'ubrzanje', 'at': 'ubrzanje', 'au': 'ubrzanje',
         'fi': 'ugao', 'l': 'duzina', 'eps': 'ugaonoUbrzanje', 'fV': 'zapreminskiProtok', 'fm': 'maseniProtok',
         'S': 'povrsina', 'V': 'zapremina', 'm': 'masa', 'rho': 'gustina', 'S1': 'povrsina', 'v1': 'brzina',
         'S2': 'povrsina', 'v2': 'brzina'}
POZ = {'t', 'g', 'h', 'H', 'tp', 'D', 'tL', 'alfa', 'T', 'f', 'r', 'S', 'V', 'm', 'rho', 'S1', 'S2', 'fV', 'fm'}

def velicine(pocetne, jed={}):
    out = {}
    for k, p in pocetne.items():
        d = {'oznaka': OZ[k], 'naziv': N[k], 'vrsta': VRSTA[k], 'pocetna': p}
        if k in jed: d['jed'] = jed[k]
        if k in POZ: d['poz'] = True
        out[k] = d
    return out

def F(naslov, latex, obj):
    return {'naslov': naslov, 'latex': latex, 'objasnjenje': obj}

# ---------- crteži ----------
def strela(x1, y1, x2, y2, klasa='lik-l', duz=11, sir=5):
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy); ux, uy = dx / n, dy / n
    bx, by = x2 - ux * duz, y2 - uy * duz
    px, py = -uy * sir, ux * sir
    return (f'<line class="{klasa}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>'
            f'<path class="tac" d="M{x2:.1f},{y2:.1f} L{bx+px:.1f},{by+py:.1f} L{bx-px:.1f},{by-py:.1f} Z"/>')

def crtez_hitac():
    # Parabola od (30,160) do (270,160), teme (150,40): kontrolna tačka (150,-80)
    s = '<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<line class="osa" x1="14" y1="160" x2="290" y2="160"/><path class="osa-s" d="M290,160 l-7,-4 v8 Z"/>'
    s += '<line class="osa" x1="30" y1="172" x2="30" y2="14"/><path class="osa-s" d="M30,14 l-4,7 h8 Z"/>'
    s += '<text class="tem" x="280" y="178">x</text><text class="tem" x="38" y="22">y</text>'
    s += '<path class="kriva" d="M30,160 Q150,-80 270,160"/>'
    s += '<line class="pom" x1="150" y1="40" x2="150" y2="160"/>'
    s += strela(30, 160, 30 + 0.447 * 78, 160 - 0.894 * 78)
    s += '<path class="ugao" d="M60,160 A30,30 0 0,0 43.4,133.2"/>'
    s += '<text x="64" y="151">α</text>'
    s += '<text x="74" y="96">v<tspan class="sub" dy="5">0</tspan></text>'
    s += '<text x="158" y="106">H</text>'
    s += '<line class="osa" x1="30" y1="182" x2="270" y2="182"/><line class="osa" x1="30" y1="176" x2="30" y2="188"/><line class="osa" x1="270" y1="176" x2="270" y2="188"/>'
    s += '<text x="143" y="198">D</text>'
    s += '<circle class="tac" cx="150" cy="40" r="4"/>'
    s += '</svg>'
    return s

def crtez_kruzno():
    cx, cy, R = 118, 112, 82
    a = math.radians(55)
    px, py = cx + R * math.cos(a), cy - R * math.sin(a)
    tx, ty = -math.sin(a), -math.cos(a)  # smer kretanja suprotno kazaljci
    s = '<svg viewBox="0 0 300 205" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += f'<circle class="lik" cx="{cx}" cy="{cy}" r="{R}"/>'
    # poluprečnik r vodoravno
    s += f'<line class="lik-l" x1="{cx}" y1="{cy}" x2="{cx+R}" y2="{cy}"/>'
    s += f'<text x="{cx+R/2-5:.1f}" y="{cy+22}">r</text>'
    s += f'<line class="pom" x1="{cx}" y1="{cy}" x2="{px:.1f}" y2="{py:.1f}"/>'
    # ugao φ
    s += f'<path class="ugao" d="M{cx+24},{cy} A24,24 0 0,0 {cx+24*math.cos(a):.1f},{cy-24*math.sin(a):.1f}"/>'
    s += f'<text x="{cx+36*math.cos(a/2)-2:.1f}" y="{cy-36*math.sin(a/2)+7:.1f}">φ</text>'
    # a_r ka središtu
    mx, my = px + (cx - px) * 0.5, py + (cy - py) * 0.5
    s += strela(px, py, mx, my)
    s += f'<text x="{mx+14:.1f}" y="{my+4:.1f}">a<tspan class="sub" dy="5">r</tspan></text>'
    # brzina po tangenti
    s += strela(px, py, px + tx * 70, py + ty * 70)
    s += f'<text x="{px + tx*70 - 18:.1f}" y="{py + ty*70 + 4:.1f}">v</text>'
    s += f'<circle class="tac" cx="{px:.1f}" cy="{py:.1f}" r="5"/>'
    s += f'<circle class="tac" cx="{cx}" cy="{cy}" r="3.5"/>'
    s += f'<text x="{cx-18}" y="{cy+20}" class="tem">O</text>'
    # smer obrtanja ω
    s += '<path class="ugao" d="M254,96 A40,40 0 0,0 236,52"/><path class="tac" d="M236,52 l0.5,11 l8,-7 Z"/>'
    s += '<text x="258" y="70">ω</text>'
    s += '</svg>'
    return s

# ---------- teme ----------
teme = []

teme.append({
 'id': 'ravnomerno', 'simbol': 'v',
 'naziv': T("Ravnomerno kretanje","Uniform motion","Moto rettilineo uniforme","Mouvement uniforme","Movimiento uniforme","Gleichförmige Bewegung","Movimento uniforme","Равномерное движение"),
 'opis': T("Stalna brzina","Constant velocity","Velocità costante","Vitesse constante","Velocidad constante","Konstante Geschwindigkeit","Velocidade constante","Постоянная скорость"),
 'kljucne_reci': T("ravnomerno pravolinijsko kretanje brzina put vreme srednja brzina","uniform motion constant speed velocity distance time average speed","moto uniforme velocita spazio tempo velocita media","mouvement rectiligne uniforme vitesse distance temps vitesse moyenne","movimiento rectilineo uniforme mru velocidad distancia tiempo velocidad media","gleichformige bewegung geschwindigkeit weg zeit durchschnittsgeschwindigkeit","movimento uniforme mu velocidade distancia tempo velocidade media","равномерное прямолинейное движение скорость путь время средняя скорость"),
 'formule': [
  F(T("Zakon puta","Position–time law","Legge oraria","Équation horaire","Ecuación de posición","Weg-Zeit-Gesetz","Função horária","Закон движения"),
    r"s = s_0 + v\,t",
    T("Položaj tela posle vremena t, kada se kreće stalnom brzinom v; s₀ je početni položaj.","Position after time t when moving at constant velocity v; s₀ is the initial position.","Posizione dopo il tempo t a velocità costante v; s₀ è la posizione iniziale.","Position après un temps t à vitesse constante v ; s₀ est la position initiale.","Posición tras un tiempo t a velocidad constante v; s₀ es la posición inicial.","Position nach der Zeit t bei konstanter Geschwindigkeit v; s₀ ist die Anfangsposition.","Posição após o tempo t com velocidade constante v; s₀ é a posição inicial.","Положение тела через время t при постоянной скорости v; s₀ — начальное положение.")),
  F(T("Srednja brzina","Average velocity","Velocità media","Vitesse moyenne","Velocidad media","Durchschnittsgeschwindigkeit","Velocidade média","Средняя скорость"),
    r"\bar v = \frac{\Delta s}{\Delta t}, \quad s = s_0 + \bar v\,t",
    T("Ukupni pređeni put podeljen ukupnim vremenom; važi i kada brzina nije stalna.","Total distance divided by total time; valid even when the velocity changes.","Spazio totale diviso il tempo totale; vale anche se la velocità varia.","Distance totale divisée par la durée totale ; valable même si la vitesse varie.","Distancia total dividida entre el tiempo total; vale aunque la velocidad cambie.","Gesamtweg geteilt durch Gesamtzeit; gilt auch bei veränderlicher Geschwindigkeit.","Distância total dividida pelo tempo total; vale mesmo com velocidade variável.","Весь путь, делённый на всё время; верно и при переменной скорости.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'pos': None, 's0': 0, 'v': 20, 't': 10, 's': 1000, 'vsr': None}, {'v': 'km/h', 'vsr': 'km/h', 's': 'km'}),
  'jednacine': [
   {'latex': r"s = s_0 + v t", 'trazi': 'pos', 'resenja': {'pos': 's0 + v*t', 's0': 'pos - v*t', 'v': '(pos - s0)/t', 't': '(pos - s0)/v'}},
   {'latex': r"\bar v = \dfrac{s}{t}", 'trazi': 'vsr', 'resenja': {'vsr': 's/t', 's': 'vsr*t', 't': 's/vsr'}},
  ]}
})

teme.append({
 'id': 'ubrzano', 'simbol': 'a',
 'naziv': T("Ravnomerno ubrzano kretanje","Uniformly accelerated motion","Moto uniformemente accelerato","Mouvement uniformément accéléré","Movimiento uniformemente acelerado","Gleichmäßig beschleunigte Bewegung","Movimento uniformemente variado","Равноускоренное движение"),
 'opis': T("Stalno ubrzanje","Constant acceleration","Accelerazione costante","Accélération constante","Aceleración constante","Konstante Beschleunigung","Aceleração constante","Постоянное ускорение"),
 'kljucne_reci': T("ubrzano usporeno kretanje ubrzanje kocenje brzina put zaustavni put","accelerated motion acceleration braking deceleration suvat stopping distance","moto accelerato accelerazione frenata decelerazione","mouvement accelere acceleration freinage deceleration","movimiento acelerado mrua aceleracion frenado desaceleracion","beschleunigte bewegung beschleunigung bremsen bremsweg","movimento acelerado muv aceleracao frenagem torricelli","равноускоренное движение ускорение торможение тормозной путь"),
 'formule': [
  F(T("Brzina","Velocity","Velocità","Vitesse","Velocidad","Geschwindigkeit","Velocidade","Скорость"),
    r"v = v_0 + a\,t",
    T("Brzina posle vremena t; za usporavanje (kočenje) a je negativno.","Velocity after time t; a is negative when slowing down.","Velocità dopo il tempo t; in frenata a è negativa.","Vitesse après un temps t ; a est négative lors d’un freinage.","Velocidad tras un tiempo t; al frenar a es negativa.","Geschwindigkeit nach der Zeit t; beim Bremsen ist a negativ.","Velocidade após o tempo t; na frenagem a é negativa.","Скорость через время t; при торможении a отрицательно.")),
  F(T("Zakon puta","Position–time law","Legge oraria","Équation horaire","Ecuación de posición","Weg-Zeit-Gesetz","Função horária","Закон движения"),
    r"s = s_0 + v_0 t + \frac{a t^2}{2}",
    T("Položaj tela posle vremena t pri stalnom ubrzanju a.","Position after time t at constant acceleration a.","Posizione dopo il tempo t con accelerazione costante a.","Position après un temps t avec une accélération constante a.","Posición tras un tiempo t con aceleración constante a.","Position nach der Zeit t bei konstanter Beschleunigung a.","Posição após o tempo t com aceleração constante a.","Положение тела через время t при постоянном ускорении a.")),
  F(T("Brzina i put (bez vremena)","Velocity and distance (no time)","Velocità e spazio (senza tempo)","Vitesse et distance (sans le temps)","Velocidad y distancia (sin tiempo)","Geschwindigkeit und Weg (ohne Zeit)","Equação de Torricelli","Скорость и путь (без времени)"),
    r"v^2 = v_0^2 + 2 a s",
    T("Korisno za zaustavni put: kada se telo zaustavi, v = 0.","Useful for stopping distance: when the body stops, v = 0.","Utile per lo spazio di frenata: quando il corpo si ferma, v = 0.","Utile pour la distance d’arrêt : à l’arrêt, v = 0.","Útil para la distancia de frenado: al detenerse, v = 0.","Nützlich für den Bremsweg: beim Stillstand ist v = 0.","Útil para a distância de frenagem: ao parar, v = 0.","Удобно для тормозного пути: при остановке v = 0.")),
  F(T("Ubrzanje","Acceleration","Accelerazione","Accélération","Aceleración","Beschleunigung","Aceleração","Ускорение"),
    r"a = \frac{\Delta v}{\Delta t}",
    T("Promena brzine u jedinici vremena.","Change of velocity per unit time.","Variazione di velocità nell’unità di tempo.","Variation de la vitesse par unité de temps.","Cambio de velocidad por unidad de tiempo.","Geschwindigkeitsänderung pro Zeiteinheit.","Variação da velocidade por unidade de tempo.","Изменение скорости за единицу времени.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'v': None, 'v0': 0, 'a': 2, 't': 5, 's': None}, {'v': 'km/h', 'v0': 'km/h'}),
  'jednacine': [
   {'latex': r"v = v_0 + a t", 'trazi': 'v', 'resenja': {'v': 'v0 + a*t', 'v0': 'v - a*t', 'a': '(v - v0)/t', 't': '(v - v0)/a'}},
   {'latex': r"s = v_0 t + \dfrac{a t^2}{2}", 'trazi': 's',
    'resenja': {'s': 'v0*t + a*t*t/2', 'v0': '(s - a*t*t/2)/t', 'a': '2*(s - v0*t)/(t*t)', 't': 'kvPoz(a/2, v0, -s)'},
    'napomene': {'s': T("s je put od početnog položaja (s₀ = 0).","s is measured from the starting point (s₀ = 0).","s è misurato dal punto di partenza (s₀ = 0).","s est mesuré depuis le point de départ (s₀ = 0).","s se mide desde el punto de partida (s₀ = 0).","s wird vom Startpunkt gemessen (s₀ = 0).","s é medido a partir do ponto de partida (s₀ = 0).","s отсчитывается от начальной точки (s₀ = 0).")}},
   {'latex': r"v^2 = v_0^2 + 2 a s", 'trazi': 's',
    'resenja': {'v': 'sqrt(v0*v0 + 2*a*s)', 'v0': 'sqrt(v*v - 2*a*s)', 'a': '(v*v - v0*v0)/(2*s)', 's': '(v*v - v0*v0)/(2*a)'}},
  ]}
})

teme.append({
 'id': 'slobodni_pad', 'simbol': 'g',
 'naziv': T("Slobodan pad i vertikalni hitac","Free fall and vertical throw","Caduta libera e lancio verticale","Chute libre et lancer vertical","Caída libre y tiro vertical","Freier Fall und senkrechter Wurf","Queda livre e lançamento vertical","Свободное падение и бросок вверх"),
 'opis': T("Kretanje sa ubrzanjem g","Motion with acceleration g","Moto con accelerazione g","Mouvement d’accélération g","Movimiento con aceleración g","Bewegung mit Beschleunigung g","Movimento com aceleração g","Движение с ускорением g"),
 'kljucne_reci': T("slobodan pad vertikalni hitac navise visina gravitacija g 9.81","free fall vertical throw upward height gravity g 9.81","caduta libera lancio verticale altezza gravita","chute libre lancer vertical hauteur pesanteur","caida libre tiro vertical lanzamiento altura gravedad","freier fall senkrechter wurf hohe schwerkraft","queda livre lancamento vertical altura gravidade","свободное падение бросок вверх высота гравитация"),
 'formule': [
  F(T("Slobodan pad","Free fall","Caduta libera","Chute libre","Caída libre","Freier Fall","Queda livre","Свободное падение"),
    r"v = g\,t, \quad h = \frac{g t^2}{2}, \quad v = \sqrt{2 g h}",
    T("Telo pušteno iz mirovanja, bez otpora vazduha; g ≈ 9,81 m/s².","Body released from rest, no air resistance; g ≈ 9.81 m/s².","Corpo lasciato da fermo, senza attrito dell’aria; g ≈ 9,81 m/s².","Corps lâché sans vitesse initiale, sans frottement de l’air ; g ≈ 9,81 m/s².","Cuerpo soltado desde el reposo, sin rozamiento del aire; g ≈ 9,81 m/s².","Körper aus der Ruhe losgelassen, ohne Luftwiderstand; g ≈ 9,81 m/s².","Corpo solto do repouso, sem resistência do ar; g ≈ 9,81 m/s².","Тело отпущено без начальной скорости, без сопротивления воздуха; g ≈ 9,81 м/с².")),
  F(T("Vertikalni hitac naviše","Upward vertical throw","Lancio verticale verso l’alto","Lancer vertical vers le haut","Tiro vertical hacia arriba","Senkrechter Wurf nach oben","Lançamento vertical para cima","Бросок вертикально вверх"),
    r"v = v_0 - g\,t, \quad h = v_0 t - \frac{g t^2}{2}",
    T("Telo izbačeno naviše početnom brzinom v₀; h je visina iznad tačke izbačaja.","Body thrown upward with initial velocity v₀; h is the height above the launch point.","Corpo lanciato verso l’alto con velocità v₀; h è l’altezza sopra il punto di lancio.","Corps lancé vers le haut à la vitesse v₀ ; h est la hauteur au-dessus du point de lancement.","Cuerpo lanzado hacia arriba con velocidad v₀; h es la altura sobre el punto de lanzamiento.","Körper mit v₀ nach oben geworfen; h ist die Höhe über dem Abwurfpunkt.","Corpo lançado para cima com velocidade v₀; h é a altura acima do ponto de lançamento.","Тело брошено вверх со скоростью v₀; h — высота над точкой броска.")),
  F(T("Najveća visina i vreme penjanja","Maximum height and rise time","Altezza massima e tempo di salita","Hauteur maximale et durée de montée","Altura máxima y tiempo de subida","Maximale Höhe und Steigzeit","Altura máxima e tempo de subida","Максимальная высота и время подъёма"),
    r"H = \frac{v_0^2}{2g}, \quad t_p = \frac{v_0}{g}",
    T("U najvišoj tački brzina je nula; ukupno vreme leta je 2tₚ.","At the highest point the velocity is zero; total flight time is 2tₚ.","Nel punto più alto la velocità è nulla; il tempo di volo totale è 2tₚ.","Au point le plus haut la vitesse est nulle ; la durée totale du vol est 2tₚ.","En el punto más alto la velocidad es cero; el tiempo total de vuelo es 2tₚ.","Im höchsten Punkt ist die Geschwindigkeit null; die gesamte Flugzeit ist 2tₚ.","No ponto mais alto a velocidade é zero; o tempo total de voo é 2tₚ.","В верхней точке скорость равна нулю; полное время полёта 2tₚ.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'g': 9.81, 't': 2, 'h': 20, 'v': None, 'v0': 15, 'H': None, 'tp': None}),
  'jednacine': [
   {'latex': r"h = \dfrac{g t^2}{2}", 'trazi': 'h', 'resenja': {'h': 'g*t*t/2', 't': 'sqrt(2*h/g)', 'g': '2*h/(t*t)'}},
   {'latex': r"v = g t", 'trazi': 'v', 'resenja': {'v': 'g*t', 't': 'v/g', 'g': 'v/t'}},
   {'latex': r"v = \sqrt{2 g h}", 'trazi': 'v', 'resenja': {'v': 'sqrt(2*g*h)', 'h': 'v*v/(2*g)', 'g': 'v*v/(2*h)'}},
   {'latex': r"H = \dfrac{v_0^2}{2g}", 'trazi': 'H', 'resenja': {'H': 'v0*v0/(2*g)', 'v0': 'sqrt(2*g*H)', 'g': 'v0*v0/(2*H)'}},
   {'latex': r"t_p = \dfrac{v_0}{g}", 'trazi': 'tp', 'resenja': {'tp': 'v0/g', 'v0': 'g*tp', 'g': 'v0/tp'}},
  ]}
})

TG = dict(sr=r"\operatorname{tg}", ru=r"\operatorname{tg}")
teme.append({
 'id': 'kosi_hitac', 'simbol': 'α',
 'naziv': T("Kosi hitac","Projectile motion","Moto del proiettile","Mouvement d’un projectile","Tiro oblicuo","Schräger Wurf","Lançamento oblíquo","Бросок под углом"),
 'opis': T("Domet, visina, vreme leta","Range, height, flight time","Gittata, altezza, tempo di volo","Portée, hauteur, durée du vol","Alcance, altura, tiempo de vuelo","Wurfweite, Höhe, Flugzeit","Alcance, altura, tempo de voo","Дальность, высота, время полёта"),
 'kljucne_reci': T("kosi hitac horizontalni hitac domet putanja parabola ugao izbacaja","projectile motion horizontal throw range trajectory parabola launch angle","moto parabolico proiettile lancio orizzontale gittata traiettoria","mouvement parabolique projectile tir horizontal portee trajectoire","tiro parabolico oblicuo horizontal alcance trayectoria","schrager wurf waagerechter wurf wurfweite flugbahn parabel","lancamento obliquo horizontal alcance trajetoria parabola","бросок под углом горизонтальный бросок дальность траектория парабола"),
 'crtez': crtez_hitac(),
 'formule': [
  F(T("Koordinate","Coordinates","Coordinate","Coordonnées","Coordenadas","Koordinaten","Coordenadas","Координаты"),
    r"x = v_0 \cos\alpha \; t, \quad y = v_0 \sin\alpha \; t - \frac{g t^2}{2}",
    T("Vodoravno se telo kreće ravnomerno, a vertikalno kao vertikalni hitac.","Horizontally the motion is uniform; vertically it is a vertical throw.","In orizzontale il moto è uniforme, in verticale è un lancio verticale.","Horizontalement le mouvement est uniforme, verticalement c’est un lancer vertical.","En horizontal el movimiento es uniforme y en vertical es un tiro vertical.","Waagerecht gleichförmig, senkrecht wie ein senkrechter Wurf.","Na horizontal o movimento é uniforme; na vertical é um lançamento vertical.","По горизонтали движение равномерное, по вертикали — как бросок вверх.")),
  F(T("Putanja (parabola)","Trajectory (parabola)","Traiettoria (parabola)","Trajectoire (parabole)","Trayectoria (parábola)","Flugbahn (Parabel)","Trajetória (parábola)","Траектория (парабола)"),
    L(r"y = x \tan\alpha - \frac{g\,x^2}{2 v_0^2 \cos^2\alpha}", **{k: rf"y = x {v}\alpha - \frac{{g\,x^2}}{{2 v_0^2 \cos^2\alpha}}" for k, v in TG.items()}),
    T("Visina tela u zavisnosti od vodoravnog rastojanja x.","Height of the body as a function of horizontal distance x.","Altezza del corpo in funzione della distanza orizzontale x.","Hauteur du corps en fonction de la distance horizontale x.","Altura del cuerpo en función de la distancia horizontal x.","Höhe des Körpers in Abhängigkeit von der waagerechten Entfernung x.","Altura do corpo em função da distância horizontal x.","Высота тела в зависимости от горизонтального расстояния x.")),
  F(T("Domet, najveća visina, vreme leta","Range, maximum height, flight time","Gittata, altezza massima, tempo di volo","Portée, hauteur maximale, durée du vol","Alcance, altura máxima, tiempo de vuelo","Wurfweite, maximale Höhe, Flugzeit","Alcance, altura máxima, tempo de voo","Дальность, наибольшая высота, время полёта"),
    r"D = \frac{v_0^2 \sin 2\alpha}{g}, \quad H = \frac{v_0^2 \sin^2\alpha}{2g}, \quad t_L = \frac{2 v_0 \sin\alpha}{g}",
    T("Za izbačaj i pad na istoj visini. Najveći domet je za α = 45°; uglovi α i 90° − α daju isti domet.","For launch and landing at the same height. Maximum range at α = 45°; angles α and 90° − α give the same range.","Per lancio e arrivo alla stessa quota. Gittata massima per α = 45°; α e 90° − α danno la stessa gittata.","Départ et arrivée à la même hauteur. Portée maximale pour α = 45° ; α et 90° − α donnent la même portée.","Lanzamiento y caída a la misma altura. Alcance máximo con α = 45°; α y 90° − α dan el mismo alcance.","Abwurf und Landung auf gleicher Höhe. Größte Wurfweite bei α = 45°; α und 90° − α ergeben dieselbe Weite.","Lançamento e queda na mesma altura. Alcance máximo para α = 45°; α e 90° − α dão o mesmo alcance.","Старт и падение на одной высоте. Наибольшая дальность при α = 45°; углы α и 90° − α дают одинаковую дальность.")),
  F(T("Horizontalni hitac","Horizontal throw","Lancio orizzontale","Lancer horizontal","Tiro horizontal","Waagerechter Wurf","Lançamento horizontal","Горизонтальный бросок"),
    r"x = v_0 t, \quad y = h - \frac{g t^2}{2}, \quad D = v_0 \sqrt{\frac{2h}{g}}",
    T("Telo bačeno vodoravno sa visine h (α = 0).","Body thrown horizontally from height h (α = 0).","Corpo lanciato orizzontalmente dall’altezza h (α = 0).","Corps lancé horizontalement depuis la hauteur h (α = 0).","Cuerpo lanzado horizontalmente desde la altura h (α = 0).","Körper waagerecht aus der Höhe h geworfen (α = 0).","Corpo lançado horizontalmente da altura h (α = 0).","Тело брошено горизонтально с высоты h (α = 0).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'v0': 20, 'alfa': PI / 4, 'g': 9.81, 'D': None, 'H': None, 'tL': None, 'h': 20}, {'alfa': '°'}),
  'jednacine': [
   {'latex': r"D = \dfrac{v_0^2 \sin 2\alpha}{g}", 'trazi': 'D',
    'resenja': {'D': 'v0*v0*sin(2*alfa)/g', 'v0': 'sqrt(D*g/sin(2*alfa))', 'alfa': 'asin(D*g/(v0*v0))/2', 'g': 'v0*v0*sin(2*alfa)/D'},
    'napomene': {'alfa': T("Prikazan je manji ugao; isti domet daje i 90° − α.","The smaller angle is shown; 90° − α gives the same range.","È mostrato l’angolo minore; anche 90° − α dà la stessa gittata.","L’angle le plus petit est affiché ; 90° − α donne la même portée.","Se muestra el ángulo menor; 90° − α da el mismo alcance.","Angezeigt ist der kleinere Winkel; 90° − α ergibt dieselbe Weite.","É mostrado o ângulo menor; 90° − α dá o mesmo alcance.","Показан меньший угол; та же дальность и при 90° − α.")}},
   {'latex': r"H = \dfrac{v_0^2 \sin^2\alpha}{2g}", 'trazi': 'H',
    'resenja': {'H': 'v0*v0*sin(alfa)*sin(alfa)/(2*g)', 'v0': 'sqrt(2*g*H)/sin(alfa)', 'alfa': 'asin(sqrt(2*g*H)/v0)', 'g': 'v0*v0*sin(alfa)*sin(alfa)/(2*H)'}},
   {'latex': r"t_L = \dfrac{2 v_0 \sin\alpha}{g}", 'trazi': 'tL',
    'resenja': {'tL': '2*v0*sin(alfa)/g', 'v0': 'g*tL/(2*sin(alfa))', 'alfa': 'asin(g*tL/(2*v0))', 'g': '2*v0*sin(alfa)/tL'}},
   {'latex': r"D = v_0 \sqrt{\dfrac{2h}{g}}", 'trazi': 'D',
    'resenja': {'D': 'v0*sqrt(2*h/g)', 'v0': 'D/sqrt(2*h/g)', 'h': 'g*D*D/(2*v0*v0)', 'g': '2*h*v0*v0/(D*D)'},
    'napomene': {'D': T("Horizontalni hitac sa visine h.","Horizontal throw from height h.","Lancio orizzontale dall’altezza h.","Lancer horizontal depuis la hauteur h.","Tiro horizontal desde la altura h.","Waagerechter Wurf aus der Höhe h.","Lançamento horizontal da altura h.","Горизонтальный бросок с высоты h.")}},
  ]}
})

teme.append({
 'id': 'kruzno', 'simbol': 'ω',
 'naziv': T("Kružno kretanje","Circular motion","Moto circolare","Mouvement circulaire","Movimiento circular","Kreisbewegung","Movimento circular","Движение по окружности"),
 'opis': T("Period, ugaona brzina","Period, angular velocity","Periodo, velocità angolare","Période, vitesse angulaire","Período, velocidad angular","Periode, Winkelgeschwindigkeit","Período, velocidade angular","Период, угловая скорость"),
 'kljucne_reci': T("kruzno kretanje period frekvencija ugaona brzina obodna brzina centripetalno radijalno ubrzanje obrtaji","circular motion period frequency angular velocity speed centripetal acceleration rpm","moto circolare uniforme periodo frequenza velocita angolare accelerazione centripeta","mouvement circulaire uniforme periode frequence vitesse angulaire acceleration centripete","movimiento circular uniforme mcu periodo frecuencia velocidad angular aceleracion centripeta","kreisbewegung umlaufzeit frequenz winkelgeschwindigkeit zentripetalbeschleunigung drehzahl","movimento circular uniforme mcu periodo frequencia velocidade angular aceleracao centripeta","движение по окружности период частота угловая скорость центростремительное ускорение"),
 'crtez': crtez_kruzno(),
 'formule': [
  F(T("Period i frekvencija","Period and frequency","Periodo e frequenza","Période et fréquence","Período y frecuencia","Periode und Frequenz","Período e frequência","Период и частота"),
    L(r"f = \frac{1}{T}, \quad \omega = 2\pi f = \frac{2\pi}{T}", ru=r"\nu = \frac{1}{T}, \quad \omega = 2\pi \nu = \frac{2\pi}{T}"),
    T("T je vreme jednog obrta, f broj obrta u sekundi, ω ugaona brzina u rad/s.","T is the time of one revolution, f the revolutions per second, ω the angular velocity in rad/s.","T è il tempo di un giro, f i giri al secondo, ω la velocità angolare in rad/s.","T est la durée d’un tour, f le nombre de tours par seconde, ω la vitesse angulaire en rad/s.","T es el tiempo de una vuelta, f las vueltas por segundo, ω la velocidad angular en rad/s.","T ist die Dauer eines Umlaufs, f die Umläufe pro Sekunde, ω die Winkelgeschwindigkeit in rad/s.","T é o tempo de uma volta, f as voltas por segundo, ω a velocidade angular em rad/s.","T — время одного оборота, ν — число оборотов в секунду, ω — угловая скорость в рад/с.")),
  F(T("Obodna brzina","Linear speed","Velocità tangenziale","Vitesse linéaire","Velocidad lineal","Bahngeschwindigkeit","Velocidade linear","Линейная скорость"),
    r"v = \omega r = \frac{2\pi r}{T}",
    T("Brzina tačke na kružnici poluprečnika r; usmerena je po tangenti.","Speed of a point on a circle of radius r; it points along the tangent.","Velocità di un punto sulla circonferenza di raggio r; è diretta lungo la tangente.","Vitesse d’un point du cercle de rayon r ; elle est tangente au cercle.","Velocidad de un punto de la circunferencia de radio r; es tangente.","Geschwindigkeit eines Punktes auf dem Kreis mit Radius r; sie zeigt tangential.","Velocidade de um ponto na circunferência de raio r; é tangente.","Скорость точки на окружности радиуса r; направлена по касательной.")),
  F(T("Radijalno (centripetalno) ubrzanje","Centripetal acceleration","Accelerazione centripeta","Accélération centripète","Aceleración centrípeta","Zentripetalbeschleunigung","Aceleração centrípeta","Центростремительное ускорение"),
    r"a_r = \frac{v^2}{r} = \omega^2 r = \omega v",
    T("Usmereno je ka središtu kružnice.","It points toward the centre of the circle.","È diretta verso il centro della circonferenza.","Elle est dirigée vers le centre du cercle.","Está dirigida hacia el centro de la circunferencia.","Sie zeigt zum Kreismittelpunkt.","É dirigida para o centro da circunferência.","Направлено к центру окружности.")),
  F(T("Tangencijalno i ukupno ubrzanje","Tangential and total acceleration","Accelerazione tangenziale e totale","Accélération tangentielle et totale","Aceleración tangencial y total","Tangential- und Gesamtbeschleunigung","Aceleração tangencial e total","Касательное и полное ускорение"),
    L(r"a_t = r\,\alpha, \quad a = \sqrt{a_r^2 + a_t^2}", ru=r"a_t = r\,\varepsilon, \quad a = \sqrt{a_r^2 + a_t^2}"),
    T("Kada se brzina obrtanja menja; α je ugaono ubrzanje.","When the rotation speed changes; α is the angular acceleration.","Quando la velocità di rotazione varia; α è l’accelerazione angolare.","Quand la vitesse de rotation varie ; α est l’accélération angulaire.","Cuando cambia la velocidad de giro; α es la aceleración angular.","Wenn sich die Drehgeschwindigkeit ändert; α ist die Winkelbeschleunigung.","Quando a velocidade de rotação varia; α é a aceleração angular.","Когда скорость вращения меняется; ε — угловое ускорение.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'T': 2, 'f': None, 'om': None, 'r': 0.5, 'v': None, 'ar': None, 'at': 1, 'au': None}),
  'jednacine': [
   {'latex': r"\omega = \dfrac{2\pi}{T}", 'trazi': 'om', 'resenja': {'om': '2*PI/T', 'T': '2*PI/om'}},
   {'latex': L(r"f = \dfrac{1}{T}", ru=r"\nu = \dfrac{1}{T}"), 'trazi': 'f', 'resenja': {'f': '1/T', 'T': '1/f'}},
   {'latex': r"v = \omega r", 'trazi': 'v', 'resenja': {'v': 'om*r', 'om': 'v/r', 'r': 'v/om'}},
   {'latex': r"a_r = \dfrac{v^2}{r}", 'trazi': 'ar', 'resenja': {'ar': 'v*v/r', 'v': 'sqrt(ar*r)', 'r': 'v*v/ar'}},
   {'latex': r"a_r = \omega^2 r", 'trazi': 'ar', 'resenja': {'ar': 'om*om*r', 'om': 'sqrt(ar/r)', 'r': 'ar/(om*om)'}},
   {'latex': r"a = \sqrt{a_r^2 + a_t^2}", 'trazi': 'au', 'resenja': {'au': 'sqrt(ar*ar + at*at)', 'ar': 'sqrt(au*au - at*at)', 'at': 'sqrt(au*au - ar*ar)'}},
  ]}
})

teme.append({
 'id': 'ugaono', 'simbol': 'φ',
 'naziv': T("Ubrzano obrtanje","Accelerated rotation","Rotazione accelerata","Rotation accélérée","Rotación acelerada","Beschleunigte Drehung","Rotação acelerada","Равноускоренное вращение"),
 'opis': T("Ugao, ugaono ubrzanje","Angle, angular acceleration","Angolo, accelerazione angolare","Angle, accélération angulaire","Ángulo, aceleración angular","Winkel, Winkelbeschleunigung","Ângulo, aceleração angular","Угол, угловое ускорение"),
 'kljucne_reci': T("ugaono ubrzanje ugao obrtanja radijan luk obrtanje tocak","angular acceleration angle of rotation radian arc wheel","accelerazione angolare angolo radiante arco ruota","acceleration angulaire angle radian arc roue","aceleracion angular angulo radian arco rueda","winkelbeschleunigung drehwinkel bogenmass bogen rad","aceleracao angular angulo radiano arco roda","угловое ускорение угол поворота радиан дуга колесо"),
 'formule': [
  F(T("Ugao i luk","Angle and arc","Angolo e arco","Angle et arc","Ángulo y arco","Winkel und Bogen","Ângulo e arco","Угол и дуга"),
    r"\varphi = \frac{l}{r}",
    T("Ugao u radijanima je dužina luka podeljena poluprečnikom; jedan obrt je 2π rad.","Angle in radians is arc length divided by radius; one turn is 2π rad.","L’angolo in radianti è l’arco diviso il raggio; un giro vale 2π rad.","L’angle en radians est l’arc divisé par le rayon ; un tour vaut 2π rad.","El ángulo en radianes es el arco dividido por el radio; una vuelta son 2π rad.","Winkel im Bogenmaß ist Bogenlänge durch Radius; eine Umdrehung sind 2π rad.","O ângulo em radianos é o arco dividido pelo raio; uma volta são 2π rad.","Угол в радианах — длина дуги, делённая на радиус; один оборот — 2π рад.")),
  F(T("Stalna ugaona brzina","Constant angular velocity","Velocità angolare costante","Vitesse angulaire constante","Velocidad angular constante","Konstante Winkelgeschwindigkeit","Velocidade angular constante","Постоянная угловая скорость"),
    r"\varphi = \omega\,t",
    T("Ugao za koji se telo obrne za vreme t.","Angle turned in time t.","Angolo percorso nel tempo t.","Angle parcouru pendant le temps t.","Ángulo girado en el tiempo t.","In der Zeit t überstrichener Winkel.","Ângulo percorrido no tempo t.","Угол поворота за время t.")),
  F(T("Stalno ugaono ubrzanje","Constant angular acceleration","Accelerazione angolare costante","Accélération angulaire constante","Aceleración angular constante","Konstante Winkelbeschleunigung","Aceleração angular constante","Постоянное угловое ускорение"),
    L(r"\omega = \omega_0 + \alpha t, \quad \varphi = \omega_0 t + \frac{\alpha t^2}{2}, \quad \omega^2 = \omega_0^2 + 2 \alpha \varphi",
      ru=r"\omega = \omega_0 + \varepsilon t, \quad \varphi = \omega_0 t + \frac{\varepsilon t^2}{2}, \quad \omega^2 = \omega_0^2 + 2 \varepsilon \varphi"),
    T("Iste formule kao za ravnomerno ubrzano kretanje, sa ugaonim veličinama.","Same formulas as for uniformly accelerated motion, with angular quantities.","Stesse formule del moto uniformemente accelerato, con grandezze angolari.","Mêmes formules que pour le mouvement uniformément accéléré, avec des grandeurs angulaires.","Mismas fórmulas que el movimiento uniformemente acelerado, con magnitudes angulares.","Dieselben Formeln wie bei der beschleunigten Bewegung, mit Winkelgrößen.","Mesmas fórmulas do movimento uniformemente variado, com grandezas angulares.","Те же формулы, что и для равноускоренного движения, с угловыми величинами.")),
  F(T("Ugaono ubrzanje","Angular acceleration","Accelerazione angolare","Accélération angulaire","Aceleración angular","Winkelbeschleunigung","Aceleração angular","Угловое ускорение"),
    L(r"\alpha = \frac{\Delta\omega}{\Delta t}, \quad aₜ = r\,\alpha", ru=r"\varepsilon = \frac{\Delta\omega}{\Delta t}, \quad aₜ = r\,\varepsilon"),
    T("Promena ugaone brzine u jedinici vremena; aₜ je tangencijalno ubrzanje tačke na poluprečniku r.","Change of angular velocity per unit time; aₜ is the tangential acceleration of a point at radius r.","Variazione della velocità angolare nell’unità di tempo; aₜ è l’accelerazione tangenziale a distanza r.","Variation de la vitesse angulaire par unité de temps ; aₜ est l’accélération tangentielle au rayon r.","Cambio de la velocidad angular por unidad de tiempo; aₜ es la aceleración tangencial a la distancia r.","Änderung der Winkelgeschwindigkeit pro Zeit; aₜ ist die Tangentialbeschleunigung im Abstand r.","Variação da velocidade angular por unidade de tempo; aₜ é a aceleração tangencial no raio r.","Изменение угловой скорости за единицу времени; aₜ — касательное ускорение точки на радиусе r.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'r': 0.3, 'fi': None, 'l': 1, 'om': None, 'om0': 0, 'eps': 2, 't': 3, 'at': None}, {'fi': 'rad'}),
  'jednacine': [
   {'latex': r"l = r \varphi", 'trazi': 'fi', 'resenja': {'fi': 'l/r', 'l': 'r*fi', 'r': 'l/fi'}},
   {'latex': L(r"\omega = \omega_0 + \alpha t", ru=r"\omega = \omega_0 + \varepsilon t"), 'trazi': 'om',
    'resenja': {'om': 'om0 + eps*t', 'om0': 'om - eps*t', 'eps': '(om - om0)/t', 't': '(om - om0)/eps'}},
   {'latex': L(r"\varphi = \omega_0 t + \dfrac{\alpha t^2}{2}", ru=r"\varphi = \omega_0 t + \dfrac{\varepsilon t^2}{2}"), 'trazi': 'fi',
    'resenja': {'fi': 'om0*t + eps*t*t/2', 'om0': '(fi - eps*t*t/2)/t', 'eps': '2*(fi - om0*t)/(t*t)', 't': 'kvPoz(eps/2, om0, -fi)'}},
   {'latex': L(r"\omega^2 = \omega_0^2 + 2 \alpha \varphi", ru=r"\omega^2 = \omega_0^2 + 2 \varepsilon \varphi"), 'trazi': 'om',
    'resenja': {'om': 'sqrt(om0*om0 + 2*eps*fi)', 'om0': 'sqrt(om*om - 2*eps*fi)', 'eps': '(om*om - om0*om0)/(2*fi)', 'fi': '(om*om - om0*om0)/(2*eps)'}},
   {'latex': L(r"a_t = r \alpha", ru=r"a_t = r \varepsilon"), 'trazi': 'at', 'resenja': {'at': 'r*eps', 'r': 'at/eps', 'eps': 'at/r'}},
  ]}
})

teme.append({
 'id': 'protok', 'simbol': 'Φ',
 'naziv': T("Protok","Flow rate","Portata","Débit","Caudal","Durchfluss","Vazão","Расход"),
 'opis': T("Zapreminski i maseni, gustina","Volume and mass, density","Volumetrica e massica, densità","Volumique et massique, masse volumique","Volumétrico y másico, densidad","Volumen- und Massenstrom, Dichte","Volumétrica e mássica, densidade","Объёмный и массовый, плотность"),
 'kljucne_reci': T("protok zapreminski maseni gustina cev jednacina kontinuiteta tecnost","flow rate volume mass density pipe continuity equation liquid","portata volumetrica massica densita tubo equazione di continuita","debit volumique massique masse volumique tuyau equation de continuite","caudal volumetrico masico densidad tuberia ecuacion de continuidad","durchfluss volumenstrom massenstrom dichte rohr kontinuitatsgleichung","vazao volumetrica massica densidade cano equacao da continuidade","расход объёмный массовый плотность труба уравнение неразрывности"),
 'formule': [
  F(T("Zapreminski protok","Volume flow rate","Portata volumetrica","Débit volumique","Caudal volumétrico","Volumenstrom","Vazão volumétrica","Объёмный расход"),
    r"\Phi_V = \frac{\Delta V}{\Delta t} = S\,v",
    T("Zapremina tečnosti koja prođe kroz presek S za jedinicu vremena, pri brzini v.","Volume passing through cross-section S per unit time at velocity v.","Volume che attraversa la sezione S nell’unità di tempo, alla velocità v.","Volume traversant la section S par unité de temps, à la vitesse v.","Volumen que atraviesa la sección S por unidad de tiempo, a la velocidad v.","Volumen, das pro Zeit bei der Geschwindigkeit v durch den Querschnitt S fließt.","Volume que atravessa a seção S por unidade de tempo, à velocidade v.","Объём, проходящий через сечение S за единицу времени при скорости v.")),
  F(T("Maseni protok","Mass flow rate","Portata massica","Débit massique","Caudal másico","Massenstrom","Vazão mássica","Массовый расход"),
    r"\Phi_m = \frac{\Delta m}{\Delta t} = \rho\,\Phi_V",
    T("Masa koja prođe kroz presek za jedinicu vremena.","Mass passing through the cross-section per unit time.","Massa che attraversa la sezione nell’unità di tempo.","Masse traversant la section par unité de temps.","Masa que atraviesa la sección por unidad de tiempo.","Masse, die pro Zeit durch den Querschnitt fließt.","Massa que atravessa a seção por unidade de tempo.","Масса, проходящая через сечение за единицу времени.")),
  F(T("Gustina","Density","Densità","Masse volumique","Densidad","Dichte","Massa específica","Плотность"),
    r"\rho = \frac{m}{V}",
    T("Voda ima gustinu oko 1000 kg/m³ (1 g/cm³).","Water has a density of about 1000 kg/m³ (1 g/cm³).","L’acqua ha densità di circa 1000 kg/m³ (1 g/cm³).","L’eau a une masse volumique d’environ 1000 kg/m³ (1 g/cm³).","El agua tiene una densidad de unos 1000 kg/m³ (1 g/cm³).","Wasser hat eine Dichte von etwa 1000 kg/m³ (1 g/cm³).","A água tem massa específica de cerca de 1000 kg/m³ (1 g/cm³).","Плотность воды около 1000 кг/м³ (1 г/см³).")),
  F(T("Jednačina kontinuiteta","Continuity equation","Equazione di continuità","Équation de continuité","Ecuación de continuidad","Kontinuitätsgleichung","Equação da continuidade","Уравнение неразрывности"),
    r"S_1 v_1 = S_2 v_2",
    T("Kod nestišljive tečnosti protok je isti u svakom preseku cevi: gde je cev uža, tečnost teče brže.","For an incompressible liquid the flow rate is the same in every cross-section: where the pipe is narrower, the liquid flows faster.","Per un liquido incomprimibile la portata è uguale in ogni sezione: dove il tubo è più stretto il liquido scorre più veloce.","Pour un liquide incompressible le débit est le même dans chaque section : là où le tuyau est plus étroit, le liquide va plus vite.","En un líquido incompresible el caudal es igual en cada sección: donde el tubo es más estrecho, el líquido va más rápido.","Bei einer inkompressiblen Flüssigkeit ist der Durchfluss in jedem Querschnitt gleich: Wo das Rohr enger ist, fließt sie schneller.","Num líquido incompressível a vazão é igual em cada seção: onde o cano é mais estreito, o líquido flui mais rápido.","Для несжимаемой жидкости расход одинаков в любом сечении: где труба уже, жидкость течёт быстрее.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'fV': None, 'V': 0.01, 't': 5, 'S': 0.0005, 'v': 2, 'fm': None, 'rho': 1000, 'm': 2,
                        'S1': 0.0005, 'v1': 2, 'S2': 0.0002, 'v2': None},
                       {'fV': 'L/s', 'V': 'L', 'S': 'cm²', 'S1': 'cm²', 'S2': 'cm²', 'm': 'kg'}),
  'jednacine': [
   {'latex': r"\Phi_V = \dfrac{V}{t}", 'trazi': 'fV', 'resenja': {'fV': 'V/t', 'V': 'fV*t', 't': 'V/fV'}},
   {'latex': r"\Phi_V = S v", 'trazi': 'fV', 'resenja': {'fV': 'S*v', 'S': 'fV/v', 'v': 'fV/S'}},
   {'latex': r"\Phi_m = \rho\, \Phi_V", 'trazi': 'fm', 'resenja': {'fm': 'rho*fV', 'rho': 'fm/fV', 'fV': 'fm/rho'}},
   {'latex': r"\rho = \dfrac{m}{V}", 'trazi': 'rho', 'resenja': {'rho': 'm/V', 'm': 'rho*V', 'V': 'm/rho'}},
   {'latex': r"S_1 v_1 = S_2 v_2", 'trazi': 'v2', 'resenja': {'v2': 'S1*v1/S2', 'S2': 'S1*v1/v2', 'v1': 'S2*v2/S1', 'S1': 'S2*v2/v1'}},
  ]}
})

# vrednosti None -> izostavi pocetna (računa se)
for t in teme:
    for v in t['kalkulator']['velicine'].values():
        if v['pocetna'] is None: del v['pocetna']
        elif isinstance(v['pocetna'], float): v['pocetna'] = round(v['pocetna'], 12)
    # svaka promenljiva iz rešenja mora da postoji
    for j in t['kalkulator']['jednacine']:
        for k in j['resenja']:
            assert k in t['kalkulator']['velicine'], (t['id'], k)

out = {'oblast': 'kretanje', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
