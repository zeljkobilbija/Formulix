# Generiše assets/oblasti/magnetizam.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']
PI = math.pi
MU0 = 1.25663706127e-6

# Indukovani napon i moment sile po jeziku
UI = dict(sr='U_i', en=r'\mathcal{E}', it=r'\mathcal{E}', fr='e', es=r'\mathcal{E}', de=r'U_{\mathrm{ind}}', pt=r'\mathcal{E}', ru=r'\mathcal{E}_i')
MS = dict(sr='M', en=r'\tau', it=r'\tau', fr=r'\mathcal{M}', es=r'\tau', de='M', pt=r'\tau', ru='M')
def S(f):
    return LJ(lambda j: f.replace('{U}', UI[j]).replace('{M}', MS[j]))

N = {
 'F': T("magnetna sila","magnetic force","forza magnetica","force magnétique","fuerza magnética","magnetische Kraft","força magnética","магнитная сила"),
 'I': T("jačina struje","current","corrente","intensité du courant","corriente","Stromstärke","corrente","сила тока"),
 'l': T("dužina provodnika u polju","length of wire in the field","lunghezza del filo nel campo","longueur du fil dans le champ","longitud del conductor en el campo","Leiterlänge im Feld","comprimento do fio no campo","длина проводника в поле"),
 'B': T("magnetna indukcija","magnetic flux density","campo magnetico","champ magnétique","campo magnético","magnetische Flussdichte","campo magnético","магнитная индукция"),
 'fi': T("ugao između provodnika i polja","angle between wire and field","angolo tra filo e campo","angle entre fil et champ","ángulo entre conductor y campo","Winkel zwischen Leiter und Feld","ângulo entre fio e campo","угол между проводником и полем"),
 'I1': T("struja u prvom provodniku","current in wire 1","corrente nel filo 1","courant dans le fil 1","corriente en el conductor 1","Strom in Leiter 1","corrente no fio 1","ток в первом проводнике"),
 'I2': T("struja u drugom provodniku","current in wire 2","corrente nel filo 2","courant dans le fil 2","corriente en el conductor 2","Strom in Leiter 2","corrente no fio 2","ток во втором проводнике"),
 'r': T("rastojanje od provodnika","distance from the wire","distanza dal filo","distance au fil","distancia al conductor","Abstand zum Leiter","distância ao fio","расстояние до проводника"),
 'mu0': T("magnetna konstanta","magnetic constant","permeabilità magnetica del vuoto","perméabilité du vide","permeabilidad del vacío","magnetische Feldkonstante","permeabilidade do vácuo","магнитная постоянная"),
 'q': T("naelektrisanje čestice","charge of the particle","carica della particella","charge de la particule","carga de la partícula","Ladung des Teilchens","carga da partícula","заряд частицы"),
 'v': T("brzina čestice","velocity of the particle","velocità della particella","vitesse de la particule","velocidad de la partícula","Geschwindigkeit des Teilchens","velocidade da partícula","скорость частицы"),
 'fv': T("ugao između brzine i polja","angle between velocity and field","angolo tra velocità e campo","angle entre vitesse et champ","ángulo entre velocidad y campo","Winkel zwischen Geschwindigkeit und Feld","ângulo entre velocidade e campo","угол между скоростью и полем"),
 'm': T("masa čestice","mass of the particle","massa della particella","masse de la particule","masa de la partícula","Masse des Teilchens","massa da partícula","масса частицы"),
 'rk': T("poluprečnik putanje","radius of the path","raggio della traiettoria","rayon de la trajectoire","radio de la trayectoria","Bahnradius","raio da trajetória","радиус траектории"),
 'om': T("ugaona brzina (ciklotronska)","angular frequency (cyclotron)","pulsazione di ciclotrone","pulsation cyclotron","frecuencia angular de ciclotrón","Zyklotronkreisfrequenz","frequência angular do cíclotron","циклотронная частота"),
 'Bp': T("polje u središtu petlje","field at the centre of the loop","campo al centro della spira","champ au centre de la spire","campo en el centro de la espira","Feld im Mittelpunkt der Schleife","campo no centro da espira","поле в центре витка"),
 'rp': T("poluprečnik petlje","radius of the loop","raggio della spira","rayon de la spire","radio de la espira","Radius der Schleife","raio da espira","радиус витка"),
 'Bs': T("polje u solenoidu","field inside the solenoid","campo nel solenoide","champ dans le solénoïde","campo en el solenoide","Feld in der Spule","campo no solenoide","поле внутри соленоида"),
 'Nz': T("broj navojaka","number of turns","numero di spire","nombre de spires","número de espiras","Windungszahl","número de espiras","число витков"),
 'ls': T("dužina solenoida","length of the solenoid","lunghezza del solenoide","longueur du solénoïde","longitud del solenoide","Spulenlänge","comprimento do solenoide","длина соленоида"),
 'Mo': T("moment sile na petlju","torque on the loop","momento sulla spira","moment sur la bobine","momento sobre la espira","Drehmoment auf die Spule","torque na espira","момент сил на рамку"),
 'S': T("površina petlje","area of the loop","area della spira","aire de la spire","área de la espira","Fläche der Spule","área da espira","площадь рамки"),
 'fn': T("ugao između normale petlje i polja","angle between loop normal and field","angolo tra normale e campo","angle entre normale et champ","ángulo entre la normal y el campo","Winkel zwischen Flächennormale und Feld","ângulo entre a normal e o campo","угол между нормалью и полем"),
 'Ui': T("indukovani napon","induced voltage","forza elettromotrice indotta","force électromotrice induite","fuerza electromotriz inducida","Induktionsspannung","força eletromotriz induzida","ЭДС индукции"),
 'Phi': T("magnetni fluks","magnetic flux","flusso magnetico","flux magnétique","flujo magnético","magnetischer Fluss","fluxo magnético","магнитный поток"),
 'dPhi': T("promena fluksa","change in flux","variazione di flusso","variation de flux","variación del flujo","Flussänderung","variação do fluxo","изменение потока"),
 'dt': T("vreme promene","time of change","tempo della variazione","durée de la variation","tiempo del cambio","Änderungsdauer","tempo da variação","время изменения"),
 'U0': T("najveći napon generatora","peak voltage of the generator","tensione massima del generatore","tension maximale de l’alternateur","tensión máxima del generador","Scheitelspannung des Generators","tensão máxima do gerador","максимальная ЭДС генератора"),
 'omg': T("ugaona brzina obrtanja","angular velocity of rotation","velocità angolare di rotazione","vitesse angulaire de rotation","velocidad angular de giro","Winkelgeschwindigkeit der Drehung","velocidade angular de rotação","угловая скорость вращения"),
 'L': T("induktivnost","inductance","induttanza","inductance","inductancia","Induktivität","indutância","индуктивность"),
 'dIdt': T("brzina promene struje","rate of change of current","velocità di variazione della corrente","vitesse de variation du courant","rapidez de cambio de la corriente","Stromänderungsrate","taxa de variação da corrente","скорость изменения тока"),
 'W': T("energija magnetnog polja","magnetic field energy","energia del campo magnetico","énergie magnétique","energía del campo magnético","Energie des Magnetfeldes","energia do campo magnético","энергия магнитного поля"),
 'U1': T("primarni napon","primary voltage","tensione primaria","tension primaire","tensión primaria","Primärspannung","tensão primária","первичное напряжение"),
 'U2': T("sekundarni napon","secondary voltage","tensione secondaria","tension secondaire","tensión secundaria","Sekundärspannung","tensão secundária","вторичное напряжение"),
 'N1': T("broj navojaka primara","primary turns","spire del primario","spires du primaire","espiras del primario","Primärwindungen","espiras do primário","витки первичной обмотки"),
 'N2': T("broj navojaka sekundara","secondary turns","spire del secondario","spires du secondaire","espiras del secundario","Sekundärwindungen","espiras do secundário","витки вторичной обмотки"),
 'It1': T("primarna struja","primary current","corrente primaria","courant primaire","corriente primaria","Primärstrom","corrente primária","первичный ток"),
 'It2': T("sekundarna struja","secondary current","corrente secondaria","courant secondaire","corriente secundaria","Sekundärstrom","corrente secundária","вторичный ток"),
}
OZ = {'F': 'F', 'I': 'I', 'l': 'l', 'B': 'B', 'fi': r'\varphi', 'I1': 'I_1', 'I2': 'I_2', 'r': 'r', 'mu0': r'\mu_0', 'q': 'q', 'v': 'v',
      'fv': r'\varphi', 'm': 'm', 'rk': 'r', 'om': r'\omega_c', 'Bp': 'B', 'rp': 'r', 'Bs': 'B', 'Nz': 'N', 'ls': 'l', 'Mo': S('{M}'),
      'S': 'S', 'fn': r'\varphi', 'Ui': S('{U}'), 'Phi': r'\Phi', 'dPhi': r'\Delta\Phi', 'dt': r'\Delta t', 'U0': S('{U}_0'),
      'omg': r'\omega', 'L': 'L', 'dIdt': r'\Delta I / \Delta t', 'W': 'W', 'U1': 'U_1', 'U2': 'U_2', 'N1': 'N_1', 'N2': 'N_2',
      'It1': 'I_1', 'It2': 'I_2'}
OZ['U0'] = LJ(lambda j: (UI[j] + '_0') if '_' not in UI[j] else UI[j].replace('_i', r'_{i0}').replace(r'_{\mathrm{ind}}', r'_{\mathrm{ind},0}'))
VRSTA = {'F': 'sila', 'I': 'struja', 'l': 'duzina', 'B': 'magPolje', 'fi': 'ugao', 'I1': 'struja', 'I2': 'struja', 'r': 'duzina',
         'mu0': 'permeabilnost', 'q': 'naboj', 'v': 'brzina', 'fv': 'ugao', 'm': 'masa', 'rk': 'duzina', 'om': 'ugaonaBrzina',
         'Bp': 'magPolje', 'rp': 'duzina', 'Bs': 'magPolje', 'Nz': 'bez', 'ls': 'duzina', 'Mo': 'moment', 'S': 'povrsina',
         'fn': 'ugao', 'Ui': 'napon', 'Phi': 'magFluks', 'dPhi': 'magFluks', 'dt': 'vreme', 'U0': 'napon', 'omg': 'ugaonaBrzina',
         'L': 'induktivnost', 'dIdt': 'brzinaPromene', 'W': 'energija', 'U1': 'napon', 'U2': 'napon', 'N1': 'bez', 'N2': 'bez',
         'It1': 'struja', 'It2': 'struja'}
POZ = {'l', 'B', 'r', 'mu0', 'm', 'rk', 'rp', 'Nz', 'ls', 'S', 'dt', 'L', 'N1', 'N2', 'Bp', 'Bs', 'omg', 'U0', 'U1', 'U2', 'v'}
NENEG = {'W'}

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

def crtez_lorenc():
    """Pozitivna čestica u polju koje ulazi u ravan crteža: kružna putanja."""
    s = '<svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg" role="img">'
    for x in range(30, 300, 40):
        for y in range(22, 180, 36):
            s += f'<path class="pom" style="stroke-dasharray:none" d="M{x-5},{y-5} L{x+5},{y+5} M{x+5},{y-5} L{x-5},{y+5}"/>'
    s += '<circle class="kriva" cx="150" cy="92" r="62" fill="none"/>'
    s += '<circle class="tac" cx="150" cy="30" r="7"/><text class="fun" x="146" y="16">+</text>'
    s += strela(150, 30, 218, 30)
    s += '<text x="222" y="34">v</text>'
    s += strela(150, 30, 150, 74)
    s += '<text x="158" y="66">F</text>'
    s += '<line class="pom" x1="150" y1="92" x2="150" y2="30" style="stroke-dasharray:4 4"/>'
    s += '<circle class="tac" cx="150" cy="92" r="3"/><text x="156" y="112">r</text>'
    s += '<text x="262" y="170">B</text>'
    s += '</svg>'
    return s

def crtez_solenoid():
    s = '<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" role="img">'
    for i in range(9):
        x = 50 + i * 25
        s += f'<ellipse class="ivica" cx="{x}" cy="70" rx="9" ry="34"/>'
    s += strela(30, 70, 280, 70)
    s += '<text x="268" y="60">B</text>'
    s += '<line class="osa" x1="41" y1="124" x2="259" y2="124"/><line class="osa" x1="41" y1="118" x2="41" y2="130"/><line class="osa" x1="259" y1="118" x2="259" y2="130"/>'
    s += '<text x="146" y="144">l</text><text class="fun" x="20" y="24">I</text>'
    s += '<path class="ivica" d="M41,36 C30,30 24,24 18,30"/>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'sila_na_provodnik', 'simbol': 'F',
 'naziv': T("Sila na provodnik sa strujom","Force on a current-carrying wire","Forza su un filo percorso da corrente","Force de Laplace","Fuerza sobre un conductor","Kraft auf einen stromdurchflossenen Leiter","Força sobre um condutor","Сила Ампера"),
 'opis': T("F = IlB sin φ, dva provodnika","F = IlB sin φ, two wires","F = IlB sin φ, due fili","F = IlB sin φ, deux fils","F = IlB sen φ, dos conductores","F = IlB sin φ, zwei Leiter","F = IlB sen φ, dois fios","F = IlB sin φ, два проводника"),
 'kljucne_reci': T("sila na provodnik amperova sila magnetno polje struja paralelni provodnici","force on wire ampere force magnetic field current parallel wires","forza su un filo forza di ampere campo magnetico fili paralleli","force de laplace champ magnetique fils paralleles","fuerza sobre un conductor fuerza de ampere campo magnetico conductores paralelos","lorentzkraft auf leiter magnetfeld parallele leiter","forca magnetica sobre condutor fios paralelos","сила ампера магнитное поле проводник с током параллельные проводники"),
 'formule': [
  F(T("Sila na provodnik","Force on a wire","Forza su un filo","Force sur un fil","Fuerza sobre un conductor","Kraft auf einen Leiter","Força sobre um fio","Сила на проводник"),
    r"\vec F = I\,\vec l \times \vec B, \quad F = I l B \sin\varphi",
    T("Sila je normalna i na provodnik i na polje (pravilo leve ili desne ruke); 1 T = 1 N/(A·m).","The force is perpendicular to both wire and field (right-hand rule); 1 T = 1 N/(A·m).","La forza è perpendicolare al filo e al campo (regola della mano destra); 1 T = 1 N/(A·m).","La force est perpendiculaire au fil et au champ (règle de la main droite) ; 1 T = 1 N/(A·m).","La fuerza es perpendicular al conductor y al campo (regla de la mano derecha); 1 T = 1 N/(A·m).","Die Kraft steht senkrecht auf Leiter und Feld (Drei-Finger-Regel); 1 T = 1 N/(A·m).","A força é perpendicular ao fio e ao campo (regra da mão direita); 1 T = 1 N/(A·m).","Сила перпендикулярна проводнику и полю (правило левой руки); 1 Тл = 1 Н/(А·м).")),
  F(T("Dva paralelna provodnika","Two parallel wires","Due fili paralleli","Deux fils parallèles","Dos conductores paralelos","Zwei parallele Leiter","Dois fios paralelos","Два параллельных проводника"),
    r"F = \frac{\mu_0 I_1 I_2\, l}{2\pi r}",
    T("Struje istog smera se privlače, suprotnog smera odbijaju.","Currents in the same direction attract; opposite currents repel.","Correnti concordi si attraggono, discordi si respingono.","Des courants de même sens s’attirent, de sens opposés se repoussent.","Corrientes del mismo sentido se atraen, de sentido contrario se repelen.","Gleichgerichtete Ströme ziehen sich an, entgegengesetzte stoßen sich ab.","Correntes no mesmo sentido se atraem, opostas se repelem.","Токи одного направления притягиваются, противоположного — отталкиваются.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'I': 10, 'l': 0.2, 'B': 0.5, 'fi': PI / 2, 'I1': 10, 'I2': 10, 'r': 0.01, 'mu0': MU0},
                       {'fi': '°', 'l': 'cm', 'r': 'cm'}),
  'jednacine': [
   {'latex': r"F = I l B \sin\varphi", 'trazi': 'F', 'promenljive': ['F', 'I', 'l', 'B', 'fi'],
    'resenja': {'F': 'I*l*B*sin(fi)', 'I': 'F/(l*B*sin(fi))', 'l': 'F/(I*B*sin(fi))', 'B': 'F/(I*l*sin(fi))'}},
   {'latex': r"F = \dfrac{\mu_0 I_1 I_2 l}{2\pi r}", 'trazi': 'F', 'promenljive': ['F', 'mu0', 'I1', 'I2', 'l', 'r'],
    'resenja': {'F': 'mu0*I1*I2*l/(2*PI*r)', 'I1': 'F*2*PI*r/(mu0*I2*l)', 'I2': 'F*2*PI*r/(mu0*I1*l)', 'l': 'F*2*PI*r/(mu0*I1*I2)', 'r': 'mu0*I1*I2*l/(2*PI*F)'}},
  ]}
})

teme.append({
 'id': 'lorenc', 'simbol': 'qvB',
 'naziv': T("Lorencova sila","Lorentz force","Forza di Lorentz","Force de Lorentz","Fuerza de Lorentz","Lorentzkraft","Força de Lorentz","Сила Лоренца"),
 'opis': T("Naelektrisana čestica u polju","Charged particle in a field","Particella carica nel campo","Particule chargée dans un champ","Partícula cargada en un campo","Geladenes Teilchen im Feld","Partícula carregada no campo","Заряженная частица в поле"),
 'kljucne_reci': T("lorencova sila naelektrisana cestica kruzna putanja ciklotron elektron u magnetnom polju","lorentz force charged particle circular path cyclotron electron in magnetic field","forza di lorentz particella carica ciclotrone traiettoria circolare","force de lorentz particule chargee cyclotron trajectoire circulaire","fuerza de lorentz particula cargada ciclotron trayectoria circular","lorentzkraft geladenes teilchen zyklotron kreisbahn","forca de lorentz particula carregada ciclotron trajetoria circular","сила лоренца заряженная частица циклотрон движение по окружности"),
 'crtez': crtez_lorenc(),
 'formule': [
  F(T("Sila na naelektrisanu česticu","Force on a moving charge","Forza su una carica in moto","Force sur une charge en mouvement","Fuerza sobre una carga en movimiento","Kraft auf eine bewegte Ladung","Força sobre uma carga em movimento","Сила на движущийся заряд"),
    r"\vec F = q\,\vec v \times \vec B, \quad F = q v B \sin\varphi",
    T("Sila je normalna na brzinu, pa menja samo smer kretanja, a ne i iznos brzine.","The force is perpendicular to the velocity, so it changes only the direction, not the speed.","La forza è perpendicolare alla velocità: cambia solo la direzione, non il modulo.","La force est perpendiculaire à la vitesse : elle change la direction, pas la valeur.","La fuerza es perpendicular a la velocidad: cambia solo la dirección, no el módulo.","Die Kraft steht senkrecht zur Geschwindigkeit und ändert nur die Richtung.","A força é perpendicular à velocidade: muda só a direção, não o módulo.","Сила перпендикулярна скорости и меняет только направление движения.")),
  F(T("Ukupna Lorencova sila","Full Lorentz force","Forza di Lorentz completa","Force de Lorentz complète","Fuerza de Lorentz completa","Vollständige Lorentzkraft","Força de Lorentz completa","Полная сила Лоренца"),
    r"\vec F = q\,\vec E + q\,\vec v \times \vec B",
    T("Kada postoje i električno i magnetno polje.","When both electric and magnetic fields are present.","Quando sono presenti campo elettrico e magnetico.","En présence de champs électrique et magnétique.","Cuando hay campo eléctrico y magnético.","Bei elektrischem und magnetischem Feld.","Quando há campo elétrico e magnético.","При наличии электрического и магнитного полей.")),
  F(T("Kružna putanja (ciklotron)","Circular path (cyclotron)","Traiettoria circolare (ciclotrone)","Trajectoire circulaire (cyclotron)","Trayectoria circular (ciclotrón)","Kreisbahn (Zyklotron)","Trajetória circular (cíclotron)","Движение по окружности (циклотрон)"),
    r"r = \frac{m v}{q B}, \quad \omega_c = \frac{q B}{m}",
    T("Čestica koja ulazi normalno na polje kreće se po krugu; ugaona brzina ne zavisi od brzine.","A particle entering perpendicular to the field moves on a circle; the angular frequency does not depend on speed.","Una particella che entra perpendicolare al campo percorre un cerchio; la pulsazione non dipende dalla velocità.","Une particule entrant perpendiculairement au champ décrit un cercle ; la pulsation ne dépend pas de la vitesse.","Una partícula que entra perpendicular al campo describe un círculo; la frecuencia angular no depende de la velocidad.","Ein senkrecht zum Feld eintretendes Teilchen bewegt sich auf einem Kreis; die Kreisfrequenz hängt nicht von der Geschwindigkeit ab.","Uma partícula que entra perpendicular ao campo descreve um círculo; a frequência angular não depende da velocidade.","Частица, влетевшая перпендикулярно полю, движется по окружности; частота не зависит от скорости.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'q': 1.602176634e-19, 'v': 1e6, 'B': 0.01, 'fv': PI / 2, 'rk': None, 'm': 9.1093837139e-31, 'om': None},
                       {'fv': '°', 'B': 'mT'}),
  'jednacine': [
   {'latex': r"F = q v B \sin\varphi", 'trazi': 'F', 'promenljive': ['F', 'q', 'v', 'B', 'fv'],
    'resenja': {'F': 'q*v*B*sin(fv)', 'q': 'F/(v*B*sin(fv))', 'v': 'F/(q*B*sin(fv))', 'B': 'F/(q*v*sin(fv))'}},
   {'latex': r"r = \dfrac{m v}{q B}", 'trazi': 'rk', 'resenja': {'rk': 'm*v/(q*B)', 'm': 'rk*q*B/v', 'v': 'rk*q*B/m', 'q': 'm*v/(rk*B)', 'B': 'm*v/(q*rk)'},
    'napomene': {'rk': T("Podrazumevano: elektron.","Default: electron.","Predefinito: elettrone.","Par défaut : électron.","Por defecto: electrón.","Voreinstellung: Elektron.","Padrão: elétron.","По умолчанию: электрон.")}},
   {'latex': r"\omega_c = \dfrac{q B}{m}", 'trazi': 'om', 'resenja': {'om': 'q*B/m', 'q': 'om*m/B', 'B': 'om*m/q', 'm': 'q*B/om'}},
  ]}
})

teme.append({
 'id': 'polje_struje', 'simbol': 'B',
 'naziv': T("Magnetno polje struje","Magnetic field of a current","Campo magnetico di una corrente","Champ magnétique d’un courant","Campo magnético de una corriente","Magnetfeld eines Stromes","Campo magnético de uma corrente","Магнитное поле тока"),
 'opis': T("Provodnik, petlja, solenoid","Wire, loop, solenoid","Filo, spira, solenoide","Fil, spire, solénoïde","Conductor, espira, solenoide","Leiter, Schleife, Spule","Fio, espira, solenoide","Проводник, виток, соленоид"),
 'kljucne_reci': T("magnetno polje provodnika petlje solenoida kalem zavojnica tesla","magnetic field wire loop solenoid coil tesla","campo magnetico filo spira solenoide bobina tesla","champ magnetique fil spire solenoide bobine tesla","campo magnetico conductor espira solenoide bobina tesla","magnetfeld leiter schleife spule tesla","campo magnetico fio espira solenoide bobina tesla","магнитное поле проводника витка соленоида катушки тесла"),
 'crtez': crtez_solenoid(),
 'formule': [
  F(T("Dugačak pravi provodnik","Long straight wire","Filo rettilineo","Fil rectiligne","Conductor rectilíneo","Langer gerader Leiter","Fio retilíneo longo","Длинный прямой проводник"),
    r"B = \frac{\mu_0 I}{2\pi r}",
    T("Linije polja su krugovi oko provodnika; μ₀ = 4π · 10⁻⁷ N/A².","Field lines are circles around the wire; μ₀ = 4π · 10⁻⁷ N/A².","Le linee di campo sono cerchi attorno al filo; μ₀ = 4π · 10⁻⁷ N/A².","Les lignes de champ sont des cercles autour du fil ; μ₀ = 4π · 10⁻⁷ N/A².","Las líneas de campo son círculos alrededor del conductor; μ₀ = 4π · 10⁻⁷ N/A².","Die Feldlinien sind Kreise um den Leiter; μ₀ = 4π · 10⁻⁷ N/A².","As linhas de campo são círculos ao redor do fio; μ₀ = 4π · 10⁻⁷ N/A².","Линии поля — окружности вокруг проводника; μ₀ = 4π · 10⁻⁷ Н/А².")),
  F(T("Središte kružne petlje","Centre of a circular loop","Centro di una spira circolare","Centre d’une spire circulaire","Centro de una espira circular","Mittelpunkt einer Kreisschleife","Centro de uma espira circular","Центр кругового витка"),
    r"B = \frac{\mu_0 I}{2 r}",
    T("Za N navojaka polje je N puta jače.","For N turns the field is N times stronger.","Con N spire il campo è N volte più intenso.","Pour N spires le champ est N fois plus grand.","Con N espiras el campo es N veces mayor.","Bei N Windungen ist das Feld N-mal stärker.","Com N espiras o campo é N vezes maior.","Для N витков поле в N раз сильнее.")),
  F(T("Dugačak solenoid","Long solenoid","Solenoide lungo","Solénoïde long","Solenoide largo","Lange Spule","Solenoide longo","Длинный соленоид"),
    r"B = \frac{\mu_0 N I}{l}",
    T("Polje u unutrašnjosti je homogeno; N je broj navojaka, l dužina solenoida.","The field inside is uniform; N is the number of turns, l the length.","Il campo interno è uniforme; N è il numero di spire, l la lunghezza.","Le champ intérieur est uniforme ; N est le nombre de spires, l la longueur.","El campo interior es uniforme; N es el número de espiras, l la longitud.","Das Feld im Inneren ist homogen; N ist die Windungszahl, l die Länge.","O campo interno é uniforme; N é o número de espiras, l o comprimento.","Поле внутри однородно; N — число витков, l — длина.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'B': None, 'I': 10, 'r': 0.05, 'mu0': MU0, 'Bp': None, 'rp': 0.05, 'Bs': None, 'Nz': 500, 'ls': 0.2},
                       {'r': 'cm', 'rp': 'cm', 'ls': 'cm', 'B': 'µT', 'Bp': 'µT', 'Bs': 'mT'}),
  'jednacine': [
   {'latex': r"B = \dfrac{\mu_0 I}{2\pi r}", 'trazi': 'B', 'promenljive': ['B', 'mu0', 'I', 'r'], 'resenja': {'B': 'mu0*I/(2*PI*r)', 'I': 'B*2*PI*r/mu0', 'r': 'mu0*I/(2*PI*B)'}},
   {'latex': r"B = \dfrac{\mu_0 I}{2 r}", 'trazi': 'Bp', 'promenljive': ['Bp', 'mu0', 'I', 'rp'], 'resenja': {'Bp': 'mu0*I/(2*rp)', 'I': 'Bp*2*rp/mu0', 'rp': 'mu0*I/(2*Bp)'}},
   {'latex': r"B = \dfrac{\mu_0 N I}{l}", 'trazi': 'Bs', 'promenljive': ['Bs', 'mu0', 'Nz', 'I', 'ls'], 'resenja': {'Bs': 'mu0*Nz*I/ls', 'Nz': 'Bs*ls/(mu0*I)', 'I': 'Bs*ls/(mu0*Nz)', 'ls': 'mu0*Nz*I/Bs'}},
  ]}
})

teme.append({
 'id': 'moment_petlje', 'simbol': 'M',
 'naziv': T("Strujna petlja u polju (motor)","Current loop in a field (motor)","Spira in un campo (motore)","Spire dans un champ (moteur)","Espira en un campo (motor)","Leiterschleife im Feld (Motor)","Espira num campo (motor)","Рамка с током в поле (двигатель)"),
 'opis': T("Moment sile na petlju","Torque on a loop","Momento su una spira","Moment sur une spire","Momento sobre una espira","Drehmoment auf eine Schleife","Torque sobre uma espira","Момент сил на рамку"),
 'kljucne_reci': T("strujna petlja moment sile elektromotor magnetni moment ram","current loop torque electric motor magnetic moment coil","spira momento motore elettrico momento magnetico","spire couple moteur electrique moment magnetique","espira momento motor electrico momento magnetico","leiterschleife drehmoment elektromotor magnetisches moment","espira torque motor eletrico momento magnetico","рамка с током момент сил электродвигатель магнитный момент"),
 'formule': [
  F(T("Moment sile na petlju","Torque on a loop","Momento sulla spira","Moment sur la spire","Momento sobre la espira","Drehmoment auf die Schleife","Torque na espira","Момент сил на рамку"),
    S(r"{M} = N I S B \sin\varphi, \quad p_m = N I S"),
    T("φ je ugao između normale na petlju i polja; p_m je magnetni moment petlje. Na ovome se zasniva elektromotor.","φ is the angle between the loop normal and the field; p_m is the magnetic moment. This is how an electric motor works.","φ è l’angolo tra la normale e il campo; p_m è il momento magnetico. Così funziona il motore elettrico.","φ est l’angle entre la normale et le champ ; p_m est le moment magnétique. C’est le principe du moteur électrique.","φ es el ángulo entre la normal y el campo; p_m es el momento magnético. Así funciona el motor eléctrico.","φ ist der Winkel zwischen Flächennormale und Feld; p_m ist das magnetische Moment. So funktioniert der Elektromotor.","φ é o ângulo entre a normal e o campo; p_m é o momento magnético. Assim funciona o motor elétrico.","φ — угол между нормалью и полем; p_m — магнитный момент. На этом основан электродвигатель.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Mo': None, 'Nz': 100, 'I': 2, 'S': 0.0025, 'B': 0.2, 'fn': PI / 2}, {'S': 'cm²', 'fn': '°'}),
  'jednacine': [
   {'latex': S(r"{M} = N I S B \sin\varphi"), 'trazi': 'Mo', 'promenljive': ['Mo', 'Nz', 'I', 'S', 'B', 'fn'],
    'resenja': {'Mo': 'Nz*I*S*B*sin(fn)', 'I': 'Mo/(Nz*S*B*sin(fn))', 'B': 'Mo/(Nz*I*S*sin(fn))', 'S': 'Mo/(Nz*I*B*sin(fn))', 'Nz': 'Mo/(I*S*B*sin(fn))'}},
  ]}
})

teme.append({
 'id': 'indukcija', 'simbol': 'Φ',
 'naziv': T("Elektromagnetna indukcija","Electromagnetic induction","Induzione elettromagnetica","Induction électromagnétique","Inducción electromagnética","Elektromagnetische Induktion","Indução eletromagnética","Электромагнитная индукция"),
 'opis': T("Fluks, Faradejev zakon, generator","Flux, Faraday’s law, generator","Flusso, legge di Faraday, generatore","Flux, loi de Faraday, alternateur","Flujo, ley de Faraday, generador","Fluss, Induktionsgesetz, Generator","Fluxo, lei de Faraday, gerador","Поток, закон Фарадея, генератор"),
 'kljucne_reci': T("elektromagnetna indukcija magnetni fluks faradejev zakon lencovo pravilo indukovani napon generator","electromagnetic induction magnetic flux faraday law lenz induced emf generator","induzione elettromagnetica flusso magnetico legge di faraday lenz generatore","induction electromagnetique flux magnetique loi de faraday lenz alternateur","induccion electromagnetica flujo magnetico ley de faraday lenz generador","elektromagnetische induktion magnetischer fluss induktionsgesetz lenz generator","inducao eletromagnetica fluxo magnetico lei de faraday lenz gerador","электромагнитная индукция магнитный поток закон фарадея ленца генератор"),
 'formule': [
  F(T("Magnetni fluks","Magnetic flux","Flusso magnetico","Flux magnétique","Flujo magnético","Magnetischer Fluss","Fluxo magnético","Магнитный поток"),
    r"\Phi = N\,\vec B \cdot \vec S = N B S \cos\varphi",
    T("Za kalem sa N navojaka; 1 Wb = 1 T·m².","For a coil with N turns; 1 Wb = 1 T·m².","Per una bobina di N spire; 1 Wb = 1 T·m².","Pour une bobine de N spires ; 1 Wb = 1 T·m².","Para una bobina de N espiras; 1 Wb = 1 T·m².","Für eine Spule mit N Windungen; 1 Wb = 1 T·m².","Para uma bobina de N espiras; 1 Wb = 1 T·m².","Для катушки из N витков; 1 Вб = 1 Тл·м².")),
  F(T("Faradejev zakon","Faraday’s law","Legge di Faraday","Loi de Faraday","Ley de Faraday","Induktionsgesetz","Lei de Faraday","Закон Фарадея"),
    S(r"{U} = -\frac{\Delta \Phi}{\Delta t}"),
    T("Napon se indukuje kada se fluks menja; znak minus (Lencovo pravilo) kaže da se indukovana struja suprotstavlja promeni.","A voltage is induced when the flux changes; the minus sign (Lenz’s law) means the induced current opposes the change.","Si induce una tensione quando il flusso varia; il segno meno (legge di Lenz) indica che la corrente indotta si oppone alla variazione.","Une tension est induite quand le flux varie ; le signe moins (loi de Lenz) indique que le courant induit s’oppose à la variation.","Se induce una tensión cuando el flujo cambia; el signo menos (ley de Lenz) indica que la corriente inducida se opone al cambio.","Bei Flussänderung wird Spannung induziert; das Minus (Lenzsche Regel) bedeutet, dass der Induktionsstrom der Änderung entgegenwirkt.","Uma tensão é induzida quando o fluxo varia; o sinal de menos (lei de Lenz) indica que a corrente se opõe à variação.","ЭДС возникает при изменении потока; минус (правило Ленца) означает, что индукционный ток противодействует изменению.")),
  F(T("Provodnik koji se kreće u polju","Wire moving in a field","Filo in moto nel campo","Fil en mouvement dans un champ","Conductor en movimiento en un campo","Bewegter Leiter im Feld","Fio em movimento no campo","Проводник, движущийся в поле"),
    S(r"{U} = l v B \sin\varphi"),
    T("φ je ugao između brzine i polja.","φ is the angle between the velocity and the field.","φ è l’angolo tra velocità e campo.","φ est l’angle entre la vitesse et le champ.","φ es el ángulo entre la velocidad y el campo.","φ ist der Winkel zwischen Geschwindigkeit und Feld.","φ é o ângulo entre a velocidade e o campo.","φ — угол между скоростью и полем.")),
  F(T("Generator naizmenične struje","AC generator","Generatore di corrente alternata","Alternateur","Generador de corriente alterna","Wechselstromgenerator","Gerador de corrente alternada","Генератор переменного тока"),
    S(r"{U} = N \omega S B \sin\omega t"),
    T("Kalem koji se obrće u polju daje sinusni napon sa najvećom vrednošću NωSB.","A coil rotating in a field gives a sinusoidal voltage with peak value NωSB.","Una bobina che ruota nel campo produce una tensione sinusoidale di picco NωSB.","Une bobine tournant dans un champ donne une tension sinusoïdale de crête NωSB.","Una bobina que gira en un campo da una tensión sinusoidal de pico NωSB.","Eine im Feld rotierende Spule liefert eine Sinusspannung mit Scheitelwert NωSB.","Uma bobina girando num campo dá tensão senoidal de pico NωSB.","Вращающаяся в поле катушка даёт синусоидальную ЭДС с амплитудой NωSB.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Phi': None, 'Nz': 100, 'B': 0.5, 'S': 0.01, 'fn': 0, 'Ui': None, 'dPhi': 0.5, 'dt': 0.1, 'l': 0.5, 'v': 10, 'fv': PI / 2, 'U0': None, 'omg': 2 * PI * 50},
                       {'S': 'cm²', 'fn': '°', 'fv': '°', 'l': 'cm'}),
  'jednacine': [
   {'latex': r"\Phi = N B S \cos\varphi", 'trazi': 'Phi', 'promenljive': ['Phi', 'Nz', 'B', 'S', 'fn'],
    'resenja': {'Phi': 'Nz*B*S*cos(fn)', 'B': 'Phi/(Nz*S*cos(fn))', 'S': 'Phi/(Nz*B*cos(fn))', 'Nz': 'Phi/(B*S*cos(fn))'}},
   {'latex': S(r"|{U}| = \dfrac{\Delta \Phi}{\Delta t}"), 'trazi': 'Ui', 'resenja': {'Ui': 'dPhi/dt', 'dPhi': 'Ui*dt', 'dt': 'dPhi/Ui'}},
   {'latex': S(r"{U} = l v B \sin\varphi"), 'trazi': 'Ui', 'promenljive': ['Ui', 'l', 'v', 'B', 'fv'],
    'resenja': {'Ui': 'l*v*B*sin(fv)', 'l': 'Ui/(v*B*sin(fv))', 'v': 'Ui/(l*B*sin(fv))', 'B': 'Ui/(l*v*sin(fv))'}},
   {'latex': LJ(lambda j: (OZ['U0'][j] if isinstance(OZ['U0'], dict) else OZ['U0']) + r" = N \omega S B"),
    'trazi': 'U0', 'promenljive': ['U0', 'Nz', 'omg', 'S', 'B'],
    'resenja': {'U0': 'Nz*omg*S*B', 'Nz': 'U0/(omg*S*B)', 'omg': 'U0/(Nz*S*B)', 'S': 'U0/(Nz*omg*B)', 'B': 'U0/(Nz*omg*S)'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['fn'].pop('poz', None)
v['fn']['naziv'] = N['fn']

teme.append({
 'id': 'induktivnost', 'simbol': 'L',
 'naziv': T("Induktivnost","Inductance","Induttanza","Inductance","Inductancia","Induktivität","Indutância","Индуктивность"),
 'opis': T("Samoindukcija, energija","Self-induction, energy","Autoinduzione, energia","Auto-induction, énergie","Autoinducción, energía","Selbstinduktion, Energie","Autoindução, energia","Самоиндукция, энергия"),
 'kljucne_reci': T("induktivnost samoindukcija kalem solenoid henri energija magnetnog polja","inductance self induction coil solenoid henry magnetic energy","induttanza autoinduzione bobina henry energia magnetica","inductance auto induction bobine henry energie magnetique","inductancia autoinduccion bobina henrio energia magnetica","induktivitat selbstinduktion spule henry magnetische energie","indutancia autoinducao bobina henry energia magnetica","индуктивность самоиндукция катушка генри энергия магнитного поля"),
 'formule': [
  F(T("Induktivnost i samoindukcija","Inductance and self-induction","Induttanza e autoinduzione","Inductance et auto-induction","Inductancia y autoinducción","Induktivität und Selbstinduktion","Indutância e autoindução","Индуктивность и самоиндукция"),
    S(r"\Phi = L I, \quad {U} = -L\,\frac{\Delta I}{\Delta t}"),
    T("Kalem se protivi promeni struje; 1 H = 1 V·s/A.","A coil opposes changes in current; 1 H = 1 V·s/A.","Una bobina si oppone alle variazioni di corrente; 1 H = 1 V·s/A.","Une bobine s’oppose aux variations du courant ; 1 H = 1 V·s/A.","Una bobina se opone a los cambios de corriente; 1 H = 1 V·s/A.","Eine Spule wirkt Stromänderungen entgegen; 1 H = 1 V·s/A.","Uma bobina se opõe a variações de corrente; 1 H = 1 V·s/A.","Катушка препятствует изменению тока; 1 Гн = 1 В·с/А.")),
  F(T("Induktivnost solenoida","Inductance of a solenoid","Induttanza di un solenoide","Inductance d’un solénoïde","Inductancia de un solenoide","Induktivität einer Spule","Indutância de um solenoide","Индуктивность соленоида"),
    r"L = \frac{\mu_0 N^2 S}{l}",
    T("S je površina preseka, l dužina, N broj navojaka. Gvozdeno jezgro je višestruko povećava.","S is the cross-section, l the length, N the number of turns. An iron core increases it many times.","S è la sezione, l la lunghezza, N le spire. Un nucleo di ferro la aumenta molto.","S est la section, l la longueur, N le nombre de spires. Un noyau de fer l’augmente fortement.","S es la sección, l la longitud, N las espiras. Un núcleo de hierro la aumenta mucho.","S ist der Querschnitt, l die Länge, N die Windungszahl. Ein Eisenkern vergrößert sie stark.","S é a seção, l o comprimento, N as espiras. Um núcleo de ferro a aumenta muito.","S — площадь сечения, l — длина, N — число витков. Железный сердечник сильно её увеличивает.")),
  F(T("Energija magnetnog polja","Magnetic field energy","Energia del campo magnetico","Énergie magnétique","Energía del campo magnético","Energie des Magnetfeldes","Energia do campo magnético","Энергия магнитного поля"),
    r"W = \frac{L I^2}{2}, \quad w_m = \frac{B^2}{2\mu_0}",
    T("w_m je gustina energije (energija po jedinici zapremine).","w_m is the energy density (energy per unit volume).","w_m è la densità di energia.","w_m est la densité d’énergie.","w_m es la densidad de energía.","w_m ist die Energiedichte.","w_m é a densidade de energia.","w_m — объёмная плотность энергии.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'L': None, 'mu0': MU0, 'Nz': 500, 'S': 0.0004, 'ls': 0.1, 'Ui': None, 'dIdt': 100, 'W': None, 'I': 2},
                       {'S': 'cm²', 'ls': 'cm', 'L': 'mH'}),
  'jednacine': [
   {'latex': r"L = \dfrac{\mu_0 N^2 S}{l}", 'trazi': 'L', 'promenljive': ['L', 'mu0', 'Nz', 'S', 'ls'],
    'resenja': {'L': 'mu0*Nz*Nz*S/ls', 'Nz': 'sqrt(L*ls/(mu0*S))', 'S': 'L*ls/(mu0*Nz*Nz)', 'ls': 'mu0*Nz*Nz*S/L'}},
   {'latex': S(r"|{U}| = L \dfrac{\Delta I}{\Delta t}"), 'trazi': 'Ui', 'resenja': {'Ui': 'L*dIdt', 'L': 'Ui/dIdt', 'dIdt': 'Ui/L'}},
   {'latex': r"W = \dfrac{L I^2}{2}", 'trazi': 'W', 'resenja': {'W': 'L*I*I/2', 'L': '2*W/(I*I)', 'I': 'sqrt(2*W/L)'}},
  ]}
})

teme.append({
 'id': 'transformator', 'simbol': 'N₁/N₂',
 'naziv': T("Transformator","Transformer","Trasformatore","Transformateur","Transformador","Transformator","Transformador","Трансформатор"),
 'opis': T("Odnos napona i navojaka","Voltage and turns ratio","Rapporto di trasformazione","Rapport de transformation","Relación de transformación","Übersetzungsverhältnis","Relação de transformação","Коэффициент трансформации"),
 'kljucne_reci': T("transformator primar sekundar broj navojaka napon struja","transformer primary secondary turns ratio voltage current","trasformatore primario secondario spire tensione corrente","transformateur primaire secondaire spires tension courant","transformador primario secundario espiras tension corriente","transformator primarspule sekundarspule windungen spannung strom","transformador primario secundario espiras tensao corrente","трансформатор первичная вторичная обмотка витки напряжение ток"),
 'formule': [
  F(T("Idealni transformator","Ideal transformer","Trasformatore ideale","Transformateur idéal","Transformador ideal","Idealer Transformator","Transformador ideal","Идеальный трансформатор"),
    r"\frac{U_1}{U_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}",
    T("Bez gubitaka snaga se ne menja (U₁I₁ = U₂I₂): kad se napon poveća, struja se smanji. Radi samo sa naizmeničnom strujom.","Without losses power is unchanged (U₁I₁ = U₂I₂): when voltage goes up, current goes down. Works only with alternating current.","Senza perdite la potenza non cambia (U₁I₁ = U₂I₂): se la tensione sale, la corrente scende. Funziona solo in alternata.","Sans pertes la puissance est conservée (U₁I₁ = U₂I₂) : si la tension augmente, le courant diminue. Ne fonctionne qu’en alternatif.","Sin pérdidas la potencia no cambia (U₁I₁ = U₂I₂): si la tensión sube, la corriente baja. Solo funciona con alterna.","Ohne Verluste bleibt die Leistung gleich (U₁I₁ = U₂I₂): Steigt die Spannung, sinkt der Strom. Nur für Wechselstrom.","Sem perdas a potência não muda (U₁I₁ = U₂I₂): se a tensão sobe, a corrente desce. Só funciona com corrente alternada.","Без потерь мощность сохраняется (U₁I₁ = U₂I₂): напряжение растёт — ток падает. Работает только на переменном токе.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'U2': None, 'U1': 230, 'N1': 1000, 'N2': 52, 'It1': 0.5, 'It2': None}),
  'jednacine': [
   {'latex': r"\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}", 'trazi': 'U2', 'resenja': {'U2': 'U1*N2/N1', 'U1': 'U2*N1/N2', 'N1': 'N2*U1/U2', 'N2': 'N1*U2/U1'}},
   {'latex': r"\dfrac{I_2}{I_1} = \dfrac{N_1}{N_2}", 'trazi': 'It2', 'resenja': {'It2': 'It1*N1/N2', 'It1': 'It2*N2/N1', 'N1': 'N2*It2/It1', 'N2': 'N1*It1/It2'}},
  ]}
})

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)
    for f in t['formule']:
        o = f.get('objasnjenje')
        if isinstance(o, dict):
            for jj in J: o[jj] = o[jj].replace('p_m', 'pₘ').replace('w_m', 'wₘ')

out = {'oblast': 'magnetizam', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
