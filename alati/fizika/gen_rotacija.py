# Generiše assets/oblasti/rotacija.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']
PI = math.pi

# Oznake po jeziku: moment inercije, moment sile, ugaono ubrzanje, kinetička energija, rad
IN = dict(sr='I', en='I', it='I', fr='J', es='I', de='J', pt='I', ru='J')
MS = dict(sr='M', en=r'\tau', it=r'\tau', fr=r'\mathcal{M}', es=r'\tau', de='M', pt=r'\tau', ru='M')
AL = dict(sr=r'\alpha', en=r'\alpha', it=r'\alpha', fr=r'\alpha', es=r'\alpha', de=r'\alpha', pt=r'\alpha', ru=r'\varepsilon')
EK = dict(sr='E_k', en='E_k', it='E_c', fr='E_c', es='E_c', de=r'E_{\mathrm{rot}}', pt='E_c', ru=r'E_{\text{к}}')
RAD = dict(sr='A', en='W', it='L', fr='W', es='W', de='W', pt='W', ru='A')
def S(f):
    def zam(j):
        x = f
        for k, d in (('{I}', IN), ('{M}', MS), ('{a}', AL), ('{Ek}', EK), ('{A}', RAD)):
            x = x.replace(k, d[j])
        return x
    return LJ(zam)

N = {
 'I': T("moment inercije","moment of inertia","momento d’inerzia","moment d’inertie","momento de inercia","Trägheitsmoment","momento de inércia","момент инерции"),
 'I0': T("moment inercije oko ose kroz težište","moment of inertia about the centre-of-mass axis","momento d’inerzia rispetto al baricentro","moment d’inertie par rapport au centre de masse","momento de inercia respecto al centro de masas","Trägheitsmoment um die Schwerpunktachse","momento de inércia em relação ao centro de massa","момент инерции относительно оси через центр масс"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'r': T("poluprečnik","radius","raggio","rayon","radio","Radius","raio","радиус"),
 'l': T("dužina štapa","length of the rod","lunghezza dell’asta","longueur de la tige","longitud de la varilla","Stablänge","comprimento da barra","длина стержня"),
 'h': T("visina valjka","height of the cylinder","altezza del cilindro","hauteur du cylindre","altura del cilindro","Zylinderhöhe","altura do cilindro","высота цилиндра"),
 'd': T("rastojanje između osa","distance between the axes","distanza tra gli assi","distance entre les axes","distancia entre ejes","Abstand der Achsen","distância entre os eixos","расстояние между осями"),
 'Mo': T("moment sile","torque","momento della forza","moment de force","momento de fuerza","Drehmoment","torque","момент силы"),
 'eps': T("ugaono ubrzanje","angular acceleration","accelerazione angolare","accélération angulaire","aceleración angular","Winkelbeschleunigung","aceleração angular","угловое ускорение"),
 'Ek': T("kinetička energija obrtanja","rotational kinetic energy","energia cinetica di rotazione","énergie cinétique de rotation","energía cinética de rotación","Rotationsenergie","energia cinética de rotação","кинетическая энергия вращения"),
 'Eu': T("ukupna kinetička energija","total kinetic energy","energia cinetica totale","énergie cinétique totale","energía cinética total","gesamte kinetische Energie","energia cinética total","полная кинетическая энергия"),
 'om': T("ugaona brzina","angular velocity","velocità angolare","vitesse angulaire","velocidad angular","Winkelgeschwindigkeit","velocidade angular","угловая скорость"),
 'A': T("rad","work","lavoro","travail","trabajo","Arbeit","trabalho","работа"),
 'fi': T("ugao obrtanja","angle of rotation","angolo di rotazione","angle de rotation","ángulo girado","Drehwinkel","ângulo de rotação","угол поворота"),
 'P': T("snaga","power","potenza","puissance","potencia","Leistung","potência","мощность"),
 'v': T("brzina težišta","velocity of the centre of mass","velocità del baricentro","vitesse du centre de masse","velocidad del centro de masas","Schwerpunktgeschwindigkeit","velocidade do centro de massa","скорость центра масс"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'hv': T("visinska razlika","height difference","dislivello","dénivellation","desnivel","Höhenunterschied","desnível","разность высот"),
 'kf': T("faktor oblika (kugla 0,4; valjak 0,5; prsten 1)","shape factor (sphere 0.4; cylinder 0.5; ring 1)","fattore di forma (sfera 0,4; cilindro 0,5; anello 1)","facteur de forme (boule 0,4 ; cylindre 0,5 ; anneau 1)","factor de forma (esfera 0,4; cilindro 0,5; aro 1)","Formfaktor (Kugel 0,4; Zylinder 0,5; Ring 1)","fator de forma (esfera 0,4; cilindro 0,5; anel 1)","коэффициент формы (шар 0,4; цилиндр 0,5; кольцо 1)"),
 'Lm': T("moment impulsa","angular momentum","momento angolare","moment cinétique","momento angular","Drehimpuls","momento angular","момент импульса"),
 'rv': T("rastojanje od ose","distance from the axis","distanza dall’asse","distance à l’axe","distancia al eje","Abstand zur Achse","distância ao eixo","расстояние до оси"),
 'vv': T("brzina tela","velocity of the body","velocità del corpo","vitesse du corps","velocidad del cuerpo","Geschwindigkeit des Körpers","velocidade do corpo","скорость тела"),
 'fv': T("ugao između r i v","angle between r and v","angolo tra r e v","angle entre r et v","ángulo entre r y v","Winkel zwischen r und v","ângulo entre r e v","угол между r и v"),
 'dt': T("trajanje","duration","durata","durée","duración","Dauer","duração","время действия"),
 'dL': T("promena momenta impulsa","change in angular momentum","variazione del momento angolare","variation du moment cinétique","variación del momento angular","Drehimpulsänderung","variação do momento angular","изменение момента импульса"),
 'I1': T("moment inercije pre","moment of inertia before","momento d’inerzia prima","moment d’inertie avant","momento de inercia antes","Trägheitsmoment vorher","momento de inércia antes","момент инерции до"),
 'om1': T("ugaona brzina pre","angular velocity before","velocità angolare prima","vitesse angulaire avant","velocidad angular antes","Winkelgeschwindigkeit vorher","velocidade angular antes","угловая скорость до"),
 'I2': T("moment inercije posle","moment of inertia after","momento d’inerzia dopo","moment d’inertie après","momento de inercia después","Trägheitsmoment nachher","momento de inércia depois","момент инерции после"),
 'om2': T("ugaona brzina posle","angular velocity after","velocità angolare dopo","vitesse angulaire après","velocidad angular después","Winkelgeschwindigkeit nachher","velocidade angular depois","угловая скорость после"),
}
OZ = {'I': S('{I}'), 'I0': S('{I}_0'), 'm': 'm', 'r': 'r', 'l': 'l', 'h': 'h', 'd': 'd', 'Mo': S('{M}'), 'eps': S('{a}'),
      'Ek': S('{Ek}'), 'Eu': 'E', 'om': r'\omega', 'A': S('{A}'), 'fi': r'\varphi', 'P': 'P', 'v': 'v', 'g': 'g', 'hv': 'h',
      'kf': 'k', 'Lm': 'L', 'rv': 'r', 'vv': 'v', 'fv': r'\varphi', 'dt': r'\Delta t', 'dL': r'\Delta L',
      'I1': S('{I}_1'), 'om1': r'\omega_1', 'I2': S('{I}_2'), 'om2': r'\omega_2'}
VRSTA = {'I': 'momentInercije', 'I0': 'momentInercije', 'm': 'masa', 'r': 'duzina', 'l': 'duzina', 'h': 'duzina', 'd': 'duzina',
         'Mo': 'moment', 'eps': 'ugaonoUbrzanje', 'Ek': 'energija', 'Eu': 'energija', 'om': 'ugaonaBrzina', 'A': 'energija',
         'fi': 'ugao', 'P': 'snaga', 'v': 'brzina', 'g': 'ubrzanje', 'hv': 'duzina', 'kf': 'bez', 'Lm': 'momentImpulsa',
         'rv': 'duzina', 'vv': 'brzina', 'fv': 'ugao', 'dt': 'vreme', 'dL': 'momentImpulsa', 'I1': 'momentInercije',
         'om1': 'ugaonaBrzina', 'I2': 'momentInercije', 'om2': 'ugaonaBrzina'}
POZ = {'I', 'I0', 'm', 'r', 'l', 'h', 'g', 'kf', 'rv', 'dt', 'I1', 'I2'}
NENEG = {'Ek', 'Eu', 'v', 'om', 'd', 'hv'}

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

def crtez_tela():
    """Četiri tela sa osama: štap, valjak, kugla, prsten."""
    s = '<svg viewBox="0 0 320 150" xmlns="http://www.w3.org/2000/svg" role="img">'
    # štap
    s += '<rect class="lik" x="10" y="66" width="60" height="10" rx="3"/><line class="pom" x1="40" y1="30" x2="40" y2="112"/>'
    # valjak (os vertikalna)
    s += '<path class="lik" d="M96,48 L96,100 A22,8 0 0,0 140,100 L140,48"/><ellipse class="lik" cx="118" cy="48" rx="22" ry="8"/>'
    s += '<line class="pom" x1="118" y1="24" x2="118" y2="122"/>'
    # kugla
    s += '<circle class="lik" cx="196" cy="72" r="26"/><ellipse class="pom" cx="196" cy="72" rx="26" ry="8"/><line class="pom" x1="196" y1="30" x2="196" y2="114"/>'
    # prsten
    s += '<ellipse class="ivica" cx="276" cy="72" rx="30" ry="11" stroke-width="5"/><line class="pom" x1="276" y1="30" x2="276" y2="114"/>'
    for x, t in ((40, 'ml²/12'), (118, 'mr²/2'), (196, '2mr²/5'), (276, 'mr²')):
        s += f'<text class="fun" x="{x}" y="142" text-anchor="middle">{t}</text>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'momenti_inercije', 'simbol': 'I',
 'naziv': T("Momenti inercije","Moments of inertia","Momenti d’inerzia","Moments d’inertie","Momentos de inercia","Trägheitsmomente","Momentos de inércia","Моменты инерции"),
 'opis': T("Štap, valjak, kugla, prsten","Rod, cylinder, sphere, ring","Asta, cilindro, sfera, anello","Tige, cylindre, boule, anneau","Varilla, cilindro, esfera, aro","Stab, Zylinder, Kugel, Ring","Barra, cilindro, esfera, anel","Стержень, цилиндр, шар, кольцо"),
 'kljucne_reci': T("moment inercije stap valjak kugla prsten obruc stajnerova teorema paralelne ose","moment of inertia rod cylinder sphere ring hoop parallel axis theorem steiner","momento d inerzia asta cilindro sfera anello teorema di steiner huygens","moment d inertie tige cylindre boule anneau theoreme de huygens","momento de inercia varilla cilindro esfera aro teorema de steiner","tragheitsmoment stab zylinder kugel ring satz von steiner","momento de inercia barra cilindro esfera anel teorema de steiner","момент инерции стержень цилиндр шар кольцо теорема штейнера"),
 'crtez': crtez_tela(),
 'formule': [
  F(T("Štap (osa kroz težište)","Rod (axis through the centre)","Asta (asse per il baricentro)","Tige (axe passant par le centre)","Varilla (eje por el centro)","Stab (Achse durch den Schwerpunkt)","Barra (eixo pelo centro)","Стержень (ось через центр)"),
    S(r"{I}_0 = \frac{1}{12} m l^2"),
    T("Osa je normalna na štap. Za osu kroz kraj štapa: ml²/3.","Axis perpendicular to the rod. For an axis through one end: ml²/3.","Asse perpendicolare all’asta. Per un asse passante per un estremo: ml²/3.","Axe perpendiculaire à la tige. Pour un axe à une extrémité : ml²/3.","Eje perpendicular a la varilla. Para un eje por un extremo: ml²/3.","Achse senkrecht zum Stab. Für eine Achse durch ein Ende: ml²/3.","Eixo perpendicular à barra. Para um eixo numa extremidade: ml²/3.","Ось перпендикулярна стержню. Для оси через конец: ml²/3.")),
  F(T("Valjak (geometrijska osa)","Cylinder (symmetry axis)","Cilindro (asse di simmetria)","Cylindre (axe de symétrie)","Cilindro (eje de simetría)","Vollzylinder (Symmetrieachse)","Cilindro (eixo de simetria)","Цилиндр (ось симметрии)"),
    S(r"{I}_0 = \frac{1}{2} m r^2"),
    T("Pun valjak ili disk.","Solid cylinder or disc.","Cilindro pieno o disco.","Cylindre plein ou disque.","Cilindro macizo o disco.","Vollzylinder oder Scheibe.","Cilindro maciço ou disco.","Сплошной цилиндр или диск.")),
  F(T("Valjak (osa normalna na geometrijsku)","Cylinder (axis perpendicular to symmetry axis)","Cilindro (asse perpendicolare)","Cylindre (axe perpendiculaire)","Cilindro (eje perpendicular)","Vollzylinder (Querachse)","Cilindro (eixo perpendicular)","Цилиндр (ось, перпендикулярная оси симметрии)"),
    S(r"{I}_0 = \frac{1}{4} m r^2 + \frac{1}{12} m h^2"),
    T("Osa prolazi kroz težište; h je visina valjka.","The axis passes through the centre; h is the height of the cylinder.","L’asse passa per il baricentro; h è l’altezza del cilindro.","L’axe passe par le centre ; h est la hauteur du cylindre.","El eje pasa por el centro; h es la altura del cilindro.","Die Achse geht durch den Schwerpunkt; h ist die Zylinderhöhe.","O eixo passa pelo centro; h é a altura do cilindro.","Ось проходит через центр масс; h — высота цилиндра.")),
  F(T("Kugla (osa kroz središte)","Sphere (axis through the centre)","Sfera (asse per il centro)","Boule (axe passant par le centre)","Esfera (eje por el centro)","Kugel (Achse durch den Mittelpunkt)","Esfera (eixo pelo centro)","Шар (ось через центр)"),
    S(r"{I}_0 = \frac{2}{5} m r^2"),
    T("Puna homogena kugla. Tanka sferna ljuska: 2mr²/3.","Solid uniform sphere. Thin spherical shell: 2mr²/3.","Sfera piena omogenea. Guscio sferico sottile: 2mr²/3.","Boule pleine homogène. Sphère creuse mince : 2mr²/3.","Esfera maciza homogénea. Cáscara esférica delgada: 2mr²/3.","Homogene Vollkugel. Dünne Hohlkugel: 2mr²/3.","Esfera maciça homogênea. Casca esférica fina: 2mr²/3.","Сплошной однородный шар. Тонкая сфера: 2mr²/3.")),
  F(T("Tanak prsten (obruč)","Thin ring (hoop)","Anello sottile","Anneau mince","Aro delgado","Dünner Ring","Anel fino","Тонкое кольцо"),
    S(r"{I}_0 = m r^2, \quad {I}_0' = \frac{1}{2} m r^2"),
    T("Prvo: osa kroz središte, normalna na ravan prstena. Drugo: osa u ravni prstena (duž prečnika).","First: axis through the centre, perpendicular to the ring. Second: axis along a diameter.","Prima: asse per il centro, perpendicolare all’anello. Seconda: asse lungo un diametro.","Première : axe perpendiculaire au plan de l’anneau. Seconde : axe selon un diamètre.","Primera: eje perpendicular al aro por su centro. Segunda: eje según un diámetro.","Erstens: Achse senkrecht zur Ringebene. Zweitens: Achse entlang eines Durchmessers.","Primeira: eixo perpendicular ao anel pelo centro. Segunda: eixo ao longo de um diâmetro.","Первое — ось перпендикулярна плоскости кольца; второе — ось вдоль диаметра.")),
  F(T("Štajnerova teorema","Parallel axis theorem","Teorema di Huygens-Steiner","Théorème de Huygens","Teorema de Steiner","Satz von Steiner","Teorema dos eixos paralelos","Теорема Штейнера"),
    S(r"{I} = {I}_0 + m d^2"),
    T("Moment inercije oko ose paralelne osi kroz težište, na rastojanju d od nje.","Moment of inertia about an axis parallel to the centre-of-mass axis at distance d.","Momento d’inerzia rispetto a un asse parallelo a quello baricentrico, a distanza d.","Moment d’inertie par rapport à un axe parallèle à l’axe passant par le centre de masse, à la distance d.","Momento de inercia respecto a un eje paralelo al del centro de masas, a distancia d.","Trägheitsmoment um eine zur Schwerpunktachse parallele Achse im Abstand d.","Momento de inércia em relação a um eixo paralelo ao do centro de massa, à distância d.","Момент инерции относительно оси, параллельной оси через центр масс, на расстоянии d.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'I': None, 'I0': None, 'm': 2, 'l': 1, 'r': 0.1, 'h': 0.2, 'd': 0.5}, {'r': 'cm', 'h': 'cm'}),
  'jednacine': [
   {'latex': S(r"{I}_0 = \dfrac{m l^2}{12}"), 'trazi': 'I0', 'resenja': {'I0': 'm*l*l/12', 'm': '12*I0/(l*l)', 'l': 'sqrt(12*I0/m)'}},
   {'latex': S(r"{I}_0 = \dfrac{m r^2}{2}"), 'trazi': 'I0', 'resenja': {'I0': 'm*r*r/2', 'm': '2*I0/(r*r)', 'r': 'sqrt(2*I0/m)'}},
   {'latex': S(r"{I}_0 = \dfrac{m r^2}{4} + \dfrac{m h^2}{12}"), 'trazi': 'I0', 'resenja': {'I0': 'm*r*r/4 + m*h*h/12', 'm': 'I0/(r*r/4 + h*h/12)', 'r': 'sqrt(4*(I0/m - h*h/12))', 'h': 'sqrt(12*(I0/m - r*r/4))'}},
   {'latex': S(r"{I}_0 = \dfrac{2}{5} m r^2"), 'trazi': 'I0', 'resenja': {'I0': '2*m*r*r/5', 'm': '5*I0/(2*r*r)', 'r': 'sqrt(5*I0/(2*m))'}},
   {'latex': S(r"{I}_0 = m r^2"), 'trazi': 'I0', 'resenja': {'I0': 'm*r*r', 'm': 'I0/(r*r)', 'r': 'sqrt(I0/m)'}},
   {'latex': S(r"{I} = {I}_0 + m d^2"), 'trazi': 'I', 'resenja': {'I': 'I0 + m*d*d', 'I0': 'I - m*d*d', 'm': '(I - I0)/(d*d)', 'd': 'sqrt((I - I0)/m)'}},
  ]}
})
teme[-1]['simbol'] = 'I'

teme.append({
 'id': 'zakon_rotacije', 'simbol': 'α',
 'naziv': T("Osnovni zakon rotacije","Newton’s second law for rotation","Seconda legge della dinamica rotazionale","Principe fondamental de la rotation","Segunda ley para la rotación","Grundgesetz der Rotation","Segunda lei para a rotação","Основной закон динамики вращения"),
 'opis': T("Moment sile i ugaono ubrzanje","Torque and angular acceleration","Momento e accelerazione angolare","Moment et accélération angulaire","Momento y aceleración angular","Drehmoment und Winkelbeschleunigung","Torque e aceleração angular","Момент силы и угловое ускорение"),
 'kljucne_reci': T("zakon rotacije moment sile ugaono ubrzanje moment inercije","rotational dynamics torque angular acceleration moment of inertia","dinamica rotazionale momento accelerazione angolare","dynamique de rotation moment acceleration angulaire","dinamica de rotacion momento aceleracion angular","rotation drehmoment winkelbeschleunigung tragheitsmoment","dinamica de rotacao torque aceleracao angular","динамика вращения момент силы угловое ускорение"),
 'formule': [
  F(T("Osnovni zakon rotacije","Newton’s second law for rotation","Seconda legge per la rotazione","Principe fondamental de la rotation","Segunda ley para la rotación","Grundgesetz der Rotation","Segunda lei para a rotação","Основной закон динамики вращения"),
    S(r"{a} = \frac{{M}}{{I}}, \quad {M} = {I}\,{a}"),
    T("Analogno sa F = ma: moment sile ima ulogu sile, a moment inercije ulogu mase.","Analogous to F = ma: torque plays the role of force and moment of inertia the role of mass.","Analogo a F = ma: il momento fa da forza e il momento d’inerzia da massa.","Analogue à F = ma : le moment joue le rôle de la force et le moment d’inertie celui de la masse.","Análogo a F = ma: el momento hace de fuerza y el momento de inercia de masa.","Analog zu F = ma: Das Drehmoment entspricht der Kraft, das Trägheitsmoment der Masse.","Análogo a F = ma: o torque faz o papel da força e o momento de inércia o da massa.","Аналог F = ma: момент силы играет роль силы, а момент инерции — роль массы.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Mo': None, 'I': 0.5, 'eps': 4}),
  'jednacine': [
   {'latex': S(r"{M} = {I} {a}"), 'trazi': 'Mo', 'resenja': {'Mo': 'I*eps', 'I': 'Mo/eps', 'eps': 'Mo/I'}},
  ]}
})

teme.append({
 'id': 'energija_rotacije', 'simbol': 'Eₖ',
 'naziv': T("Energija i snaga pri obrtanju","Energy and power in rotation","Energia e potenza nella rotazione","Énergie et puissance en rotation","Energía y potencia en la rotación","Energie und Leistung bei Drehung","Energia e potência na rotação","Энергия и мощность при вращении"),
 'opis': T("Jω²/2, kotrljanje","Iω²/2, rolling","Iω²/2, rotolamento","Jω²/2, roulement","Iω²/2, rodadura","Jω²/2, Rollen","Iω²/2, rolamento","Jω²/2, качение"),
 'kljucne_reci': T("kineticka energija obrtanja rotacije kotrljanje rad snaga moment","rotational kinetic energy rolling work power torque","energia cinetica di rotazione rotolamento lavoro potenza","energie cinetique de rotation roulement travail puissance","energia cinetica de rotacion rodadura trabajo potencia","rotationsenergie rollen arbeit leistung drehmoment","energia cinetica de rotacao rolamento trabalho potencia","кинетическая энергия вращения качение работа мощность"),
 'formule': [
  F(T("Kinetička energija obrtanja","Rotational kinetic energy","Energia cinetica di rotazione","Énergie cinétique de rotation","Energía cinética de rotación","Rotationsenergie","Energia cinética de rotação","Кинетическая энергия вращения"),
    S(r"{Ek} = \frac{{I} \omega^2}{2}"),
    T("Analogno sa mv²/2.","Analogous to mv²/2.","Analogo a mv²/2.","Analogue à mv²/2.","Análogo a mv²/2.","Analog zu mv²/2.","Análogo a mv²/2.","Аналог mv²/2.")),
  F(T("Rad i snaga","Work and power","Lavoro e potenza","Travail et puissance","Trabajo y potencia","Arbeit und Leistung","Trabalho e potência","Работа и мощность"),
    S(r"{A} = {M}\,\varphi, \quad P = {M}\,\omega"),
    T("Npr. snaga motora je proizvod obrtnog momenta i ugaone brzine.","E.g. engine power is torque times angular velocity.","Es. la potenza del motore è coppia per velocità angolare.","Ex. la puissance d’un moteur est le couple multiplié par la vitesse angulaire.","P. ej., la potencia del motor es par por velocidad angular.","Z. B. ist die Motorleistung Drehmoment mal Winkelgeschwindigkeit.","Ex.: a potência do motor é torque vezes velocidade angular.","Например, мощность двигателя — момент, умноженный на угловую скорость.")),
  F(T("Kotrljanje","Rolling","Rotolamento","Roulement","Rodadura","Rollen","Rolamento","Качение"),
    S(r"E = \frac{m v^2}{2} + \frac{{I}_0 \omega^2}{2}, \quad v = \sqrt{\frac{2 g h}{1 + k}}"),
    T("Telo koje se kotrlja ima energiju kretanja težišta i energiju obrtanja. k = I₀/(mr²): niz strmu ravan kugla stiže brže od valjka, a valjak brže od prstena.","A rolling body has both translational and rotational energy. k = I₀/(mr²): down a slope a sphere beats a cylinder, and a cylinder beats a ring.","Un corpo che rotola ha energia di traslazione e di rotazione. k = I₀/(mr²): lungo un piano la sfera batte il cilindro e il cilindro l’anello.","Un corps qui roule a une énergie de translation et de rotation. k = J₀/(mr²) : sur une pente la boule devance le cylindre, et le cylindre l’anneau.","Un cuerpo que rueda tiene energía de traslación y de rotación. k = I₀/(mr²): en una pendiente la esfera gana al cilindro y el cilindro al aro.","Ein rollender Körper hat Translations- und Rotationsenergie. k = J₀/(mr²): Eine Kugel rollt schneller als ein Zylinder, dieser schneller als ein Ring.","Um corpo que rola tem energia de translação e de rotação. k = I₀/(mr²): num plano a esfera ganha do cilindro e o cilindro do anel.","Катящееся тело имеет энергию поступательного движения и вращения. k = J₀/(mr²): шар скатывается быстрее цилиндра, а цилиндр — быстрее кольца.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ek': None, 'I': 0.5, 'om': 10, 'A': None, 'Mo': 20, 'fi': 2 * PI, 'P': None, 'v': None, 'g': 9.81, 'hv': 1, 'kf': 0.4},
                       {'fi': 'obr'}),
  'jednacine': [
   {'latex': S(r"{Ek} = \dfrac{{I} \omega^2}{2}"), 'trazi': 'Ek', 'resenja': {'Ek': 'I*om*om/2', 'I': '2*Ek/(om*om)', 'om': 'sqrt(2*Ek/I)'}},
   {'latex': S(r"{A} = {M} \varphi"), 'trazi': 'A', 'resenja': {'A': 'Mo*fi', 'Mo': 'A/fi', 'fi': 'A/Mo'}},
   {'latex': S(r"P = {M} \omega"), 'trazi': 'P', 'resenja': {'P': 'Mo*om', 'Mo': 'P/om', 'om': 'P/Mo'}},
   {'latex': r"v = \sqrt{\dfrac{2 g h}{1 + k}}", 'trazi': 'v', 'resenja': {'v': 'sqrt(2*g*hv/(1 + kf))', 'hv': 'v*v*(1 + kf)/(2*g)', 'kf': '2*g*hv/(v*v) - 1', 'g': 'v*v*(1 + kf)/(2*hv)'},
    'napomene': {'v': T("Kotrljanje bez klizanja niz visinsku razliku h, iz mirovanja.","Rolling without slipping down a height h, starting from rest.","Rotolamento senza strisciare lungo un dislivello h, da fermo.","Roulement sans glissement sur une dénivellation h, depuis le repos.","Rodadura sin deslizar por un desnivel h, desde el reposo.","Rollen ohne Gleiten über die Höhe h, aus der Ruhe.","Rolamento sem deslizar por um desnível h, a partir do repouso.","Качение без проскальзывания с высоты h из состояния покоя.")}},
  ]}
})

teme.append({
 'id': 'moment_impulsa', 'simbol': 'L',
 'naziv': T("Moment impulsa","Angular momentum","Momento angolare","Moment cinétique","Momento angular","Drehimpuls","Momento angular","Момент импульса"),
 'opis': T("Lω, zakon održanja","Iω, conservation","Iω, conservazione","Jω, conservation","Iω, conservación","Jω, Erhaltung","Iω, conservação","Jω, закон сохранения"),
 'kljucne_reci': T("moment impulsa zakon odrzanja momenta impulsa piruet klizac obrtanje","angular momentum conservation pirouette skater spin","momento angolare conservazione pattinatrice piroetta","moment cinetique conservation patineuse pirouette","momento angular conservacion patinadora pirueta","drehimpuls drehimpulserhaltung pirouette eiskunstlauf","momento angular conservacao patinadora pirueta","момент импульса закон сохранения фигуристка вращение"),
 'formule': [
  F(T("Moment impulsa","Angular momentum","Momento angolare","Moment cinétique","Momento angular","Drehimpuls","Momento angular","Момент импульса"),
    S(r"L = {I}\,\omega, \quad L = r\,m\,v \sin\varphi"),
    T("Prvo za telo koje se obrće, drugo za telo (tačku) koje se kreće brzinom v na rastojanju r od ose.","First for a rotating body, second for a point mass moving with velocity v at distance r from the axis.","Prima per un corpo rotante, seconda per un punto materiale con velocità v a distanza r dall’asse.","La première pour un corps en rotation, la seconde pour un point de vitesse v à la distance r de l’axe.","La primera para un cuerpo que gira, la segunda para un punto con velocidad v a distancia r del eje.","Erstens für einen rotierenden Körper, zweitens für einen Massenpunkt mit Geschwindigkeit v im Abstand r.","A primeira para um corpo em rotação, a segunda para um ponto com velocidade v à distância r do eixo.","Первая — для вращающегося тела, вторая — для точки со скоростью v на расстоянии r от оси.")),
  F(T("Moment impulsa i moment sile","Angular momentum and torque","Momento angolare e momento della forza","Moment cinétique et moment de force","Momento angular y momento de fuerza","Drehimpuls und Drehmoment","Momento angular e torque","Момент импульса и момент силы"),
    S(r"{M}\,\Delta t = \Delta L"),
    T("Analogno sa FΔt = Δp.","Analogous to FΔt = Δp.","Analogo a FΔt = Δp.","Analogue à FΔt = Δp.","Análogo a FΔt = Δp.","Analog zu FΔt = Δp.","Análogo a FΔt = Δp.","Аналог FΔt = Δp.")),
  F(T("Zakon održanja momenta impulsa","Conservation of angular momentum","Conservazione del momento angolare","Conservation du moment cinétique","Conservación del momento angular","Drehimpulserhaltung","Conservação do momento angular","Закон сохранения момента импульса"),
    S(r"{I}_1 \omega_1 = {I}_2 \omega_2"),
    T("Bez spoljašnjeg momenta sile: kada klizačica privuče ruke, moment inercije se smanji, a obrtanje ubrza.","With no external torque: when a skater pulls in her arms, the moment of inertia drops and she spins faster.","Senza momenti esterni: quando la pattinatrice raccoglie le braccia ruota più veloce.","Sans moment extérieur : la patineuse qui ramène les bras tourne plus vite.","Sin momento externo: cuando la patinadora recoge los brazos gira más rápido.","Ohne äußeres Drehmoment: Zieht die Eiskunstläuferin die Arme an, dreht sie sich schneller.","Sem torque externo: quando a patinadora recolhe os braços, gira mais rápido.","Без внешнего момента: когда фигуристка прижимает руки, она вращается быстрее.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Lm': None, 'I': 0.5, 'om': 10, 'rv': 0.5, 'm': 2, 'vv': 3, 'fv': PI / 2, 'dL': None, 'Mo': 5, 'dt': 2,
                        'om2': None, 'I1': 3, 'om1': 2 * PI, 'I2': 1}, {'fv': '°', 'om1': 'rad/s'}),
  'jednacine': [
   {'latex': S(r"L = {I} \omega"), 'trazi': 'Lm', 'resenja': {'Lm': 'I*om', 'I': 'Lm/om', 'om': 'Lm/I'}},
   {'latex': r"L = r m v \sin\varphi", 'trazi': 'Lm', 'promenljive': ['Lm', 'rv', 'm', 'vv', 'fv'],
    'resenja': {'Lm': 'rv*m*vv*sin(fv)', 'rv': 'Lm/(m*vv*sin(fv))', 'm': 'Lm/(rv*vv*sin(fv))', 'vv': 'Lm/(rv*m*sin(fv))'}},
   {'latex': S(r"{M} \Delta t = \Delta L"), 'trazi': 'dL', 'resenja': {'dL': 'Mo*dt', 'Mo': 'dL/dt', 'dt': 'dL/Mo'}},
   {'latex': S(r"{I}_1 \omega_1 = {I}_2 \omega_2"), 'trazi': 'om2', 'resenja': {'om2': 'I1*om1/I2', 'om1': 'I2*om2/I1', 'I1': 'I2*om2/om1', 'I2': 'I1*om1/om2'}},
  ]}
})

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)

out = {'oblast': 'rotacija', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
