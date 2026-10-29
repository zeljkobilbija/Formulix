# Generiše assets/oblasti/fluidi.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']
def L(osnovni, **iz):
    return {j: iz.get(j, osnovni) for j in J} if iz else osnovni
PI = math.pi

# Oznake po jeziku
POT = dict(sr=r'F_{\mathrm{p}}', en=r'F_{\mathrm{b}}', it=r'F_{\mathrm{A}}', fr=r'F_{\mathrm{A}}', es=r'F_{\mathrm{E}}', de=r'F_{\mathrm{A}}', pt=r'F_{\mathrm{E}}', ru=r'F_{\mathrm{A}}')
CW = dict(sr='c', en=r'C_{\mathrm{d}}', it=r'C_{\mathrm{x}}', fr=r'C_{\mathrm{x}}', es=r'C_{\mathrm{D}}', de=r'c_{\mathrm{w}}', pt=r'C_{\mathrm{D}}', ru=r'C_{\mathrm{x}}')
GAM = dict(sr=r'\gamma', en=r'\gamma', it=r'\gamma', fr=r'\gamma', es=r'\gamma', de=r'\sigma', pt=r'\gamma', ru=r'\sigma')
def S(f):
    return LJ(lambda j: f.replace('{Fp}', POT[j]).replace('{c}', CW[j]).replace('{g}', GAM[j]))

N = {
 'p': T("pritisak na dubini h","pressure at depth h","pressione alla profondità h","pression à la profondeur h","presión a la profundidad h","Druck in der Tiefe h","pressão na profundidade h","давление на глубине h"),
 'ph': T("hidrostatički pritisak","hydrostatic pressure","pressione idrostatica","pression hydrostatique","presión hidrostática","hydrostatischer Druck","pressão hidrostática","гидростатическое давление"),
 'p0': T("pritisak na površini","pressure at the surface","pressione in superficie","pression à la surface","presión en la superficie","Druck an der Oberfläche","pressão na superfície","давление на поверхности"),
 'rho': T("gustina tečnosti","density of the liquid","densità del liquido","masse volumique du liquide","densidad del líquido","Dichte der Flüssigkeit","massa específica do líquido","плотность жидкости"),
 'rhot': T("gustina tela","density of the body","densità del corpo","masse volumique du corps","densidad del cuerpo","Dichte des Körpers","massa específica do corpo","плотность тела"),
 'g': T("ubrzanje Zemljine teže","gravitational acceleration","accelerazione di gravità","intensité de la pesanteur","aceleración de la gravedad","Fallbeschleunigung","aceleração da gravidade","ускорение свободного падения"),
 'h': T("dubina","depth","profondità","profondeur","profundidad","Tiefe","profundidade","глубина"),
 'Fp': T("sila potiska","buoyant force","spinta di Archimede","poussée d’Archimède","empuje","Auftriebskraft","empuxo","выталкивающая сила"),
 'V': T("zapremina uronjenog dela","submerged volume","volume immerso","volume immergé","volumen sumergido","eingetauchtes Volumen","volume submerso","объём погружённой части"),
 'ud': T("uronjeni deo zapremine","submerged fraction","frazione immersa","fraction immergée","fracción sumergida","eingetauchter Anteil","fração submersa","погружённая доля"),
 'chi': T("stišljivost","compressibility","comprimibilità","compressibilité","compresibilidad","Kompressibilität","compressibilidade","сжимаемость"),
 'V0': T("početna zapremina","initial volume","volume iniziale","volume initial","volumen inicial","Anfangsvolumen","volume inicial","начальный объём"),
 'dV': T("smanjenje zapremine","decrease in volume","diminuzione di volume","diminution de volume","disminución de volumen","Volumenabnahme","diminuição de volume","уменьшение объёма"),
 'dp': T("povećanje pritiska","increase in pressure","aumento di pressione","augmentation de pression","aumento de presión","Druckerhöhung","aumento de pressão","увеличение давления"),
 'p1': T("pritisak u preseku 1","pressure at section 1","pressione nella sezione 1","pression dans la section 1","presión en la sección 1","Druck im Querschnitt 1","pressão na seção 1","давление в сечении 1"),
 'v1': T("brzina u preseku 1","velocity at section 1","velocità nella sezione 1","vitesse dans la section 1","velocidad en la sección 1","Geschwindigkeit im Querschnitt 1","velocidade na seção 1","скорость в сечении 1"),
 'p2': T("pritisak u preseku 2","pressure at section 2","pressione nella sezione 2","pression dans la section 2","presión en la sección 2","Druck im Querschnitt 2","pressão na seção 2","давление в сечении 2"),
 'v2': T("brzina u preseku 2","velocity at section 2","velocità nella sezione 2","vitesse dans la section 2","velocidad en la sección 2","Geschwindigkeit im Querschnitt 2","velocidade na seção 2","скорость в сечении 2"),
 'v': T("brzina isticanja","outflow velocity","velocità di efflusso","vitesse d’écoulement","velocidad de salida","Ausflussgeschwindigkeit","velocidade de escoamento","скорость истечения"),
 'hv': T("dubina otvora ispod površine","depth of the hole below the surface","profondità del foro","profondeur de l’orifice","profundidad del orificio","Tiefe der Öffnung","profundidade do orifício","глубина отверстия"),
 'Fs': T("sila otpora (Stoks)","drag force (Stokes)","forza viscosa (Stokes)","force de frottement (Stokes)","fuerza viscosa (Stokes)","Reibungskraft (Stokes)","força viscosa (Stokes)","сила сопротивления (Стокс)"),
 'r': T("poluprečnik kuglice","radius of the sphere","raggio della sfera","rayon de la bille","radio de la esfera","Kugelradius","raio da esfera","радиус шарика"),
 'eta': T("viskoznost","viscosity","viscosità","viscosité","viscosidad","Viskosität","viscosidade","вязкость"),
 'vk': T("brzina kuglice","velocity of the sphere","velocità della sfera","vitesse de la bille","velocidad de la esfera","Geschwindigkeit der Kugel","velocidade da esfera","скорость шарика"),
 'Fu': T("sila otpora vazduha","air drag force","resistenza aerodinamica","traînée","resistencia aerodinámica","Luftwiderstandskraft","força de arrasto","сила лобового сопротивления"),
 'cw': T("koeficijent otpora","drag coefficient","coefficiente di resistenza","coefficient de traînée","coeficiente de arrastre","Widerstandsbeiwert","coeficiente de arrasto","коэффициент сопротивления"),
 'rhov': T("gustina vazduha","density of air","densità dell’aria","masse volumique de l’air","densidad del aire","Luftdichte","massa específica do ar","плотность воздуха"),
 'S': T("čeona površina","frontal area","area frontale","maître-couple","área frontal","Stirnfläche","área frontal","площадь сечения"),
 'vv': T("brzina","velocity","velocità","vitesse","velocidad","Geschwindigkeit","velocidade","скорость"),
 'F': T("sila površinskog napona","surface tension force","forza di tensione superficiale","force de tension superficielle","fuerza de tensión superficial","Oberflächenspannungskraft","força de tensão superficial","сила поверхностного натяжения"),
 'gam': T("površinski napon","surface tension","tensione superficiale","tension superficielle","tensión superficial","Oberflächenspannung","tensão superficial","поверхностное натяжение"),
 'l': T("dužina ivice","length of the edge","lunghezza del bordo","longueur du bord","longitud del borde","Randlänge","comprimento da borda","длина границы"),
 'dpk': T("natpritisak u kapi","excess pressure in a drop","sovrapressione nella goccia","surpression dans une goutte","sobrepresión en la gota","Überdruck im Tropfen","sobrepressão na gota","избыточное давление в капле"),
 'dpm': T("natpritisak u mehuru","excess pressure in a bubble","sovrapressione nella bolla","surpression dans une bulle","sobrepresión en la burbuja","Überdruck in der Seifenblase","sobrepressão na bolha","избыточное давление в пузыре"),
 'rk': T("poluprečnik kapi / mehura","radius of the drop / bubble","raggio della goccia / bolla","rayon de la goutte / bulle","radio de la gota / burbuja","Radius des Tropfens / der Blase","raio da gota / bolha","радиус капли / пузыря"),
}
OZ = {'p': 'p', 'ph': r'p_h', 'p0': 'p_0', 'rho': r'\rho', 'rhot': r'\rho_t', 'g': 'g', 'h': 'h', 'Fp': S('{Fp}'), 'V': 'V',
      'ud': r'V_u / V', 'chi': r'\chi', 'V0': 'V', 'dV': r'\Delta V', 'dp': r'\Delta p', 'p1': 'p_1', 'v1': 'v_1', 'p2': 'p_2',
      'v2': 'v_2', 'v': 'v', 'hv': 'h', 'Fs': 'F', 'r': 'r', 'eta': r'\eta', 'vk': 'v', 'Fu': 'F', 'cw': S('{c}'),
      'rhov': r'\rho', 'S': 'S', 'vv': 'v', 'F': 'F', 'gam': S('{g}'), 'l': 'l', 'dpk': r'\Delta p', 'dpm': r'\Delta p', 'rk': 'r'}
OZ['ud'] = LJ(lambda j: r'V_{\text{%s}} / V' % {'sr': 'u', 'en': 'sub', 'it': 'imm', 'fr': 'imm', 'es': 'sum', 'de': 'ein', 'pt': 'sub', 'ru': 'погр'}[j])
OZ['rhot'] = LJ(lambda j: r'\rho_{\text{%s}}' % {'sr': 't', 'en': 'b', 'it': 'c', 'fr': 'c', 'es': 'c', 'de': 'K', 'pt': 'c', 'ru': 'т'}[j])
VRSTA = {'p': 'pritisak', 'ph': 'pritisak', 'p0': 'pritisak', 'rho': 'gustina', 'rhot': 'gustina', 'g': 'ubrzanje', 'h': 'duzina',
         'Fp': 'sila', 'V': 'zapremina', 'ud': 'udeo', 'chi': 'stisljivost', 'V0': 'zapremina', 'dV': 'zapremina', 'dp': 'pritisak',
         'p1': 'pritisak', 'v1': 'brzina', 'p2': 'pritisak', 'v2': 'brzina', 'v': 'brzina', 'hv': 'duzina', 'Fs': 'sila',
         'r': 'duzina', 'eta': 'viskoznost', 'vk': 'brzina', 'Fu': 'sila', 'cw': 'bez', 'rhov': 'gustina', 'S': 'povrsina',
         'vv': 'brzina', 'F': 'sila', 'gam': 'povrsinskiNapon', 'l': 'duzina', 'dpk': 'pritisak', 'dpm': 'pritisak', 'rk': 'duzina'}
POZ = {'rho', 'rhot', 'g', 'V', 'chi', 'V0', 'r', 'eta', 'cw', 'rhov', 'S', 'gam', 'l', 'rk', 'p', 'p0', 'Fp', 'ud'}
NENEG = {'h', 'hv', 'v', 'p2', 'ph'}

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

def crtez_hidro():
    s = '<svg viewBox="0 0 300 190" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<rect class="lik" x="60" y="44" width="180" height="130" fill-opacity="0.8" stroke="none"/>'
    s += '<path class="ivica" d="M60,14 L60,174 L240,174 L240,14"/>'
    s += '<line class="lik-l" x1="60" y1="44" x2="240" y2="44"/>'
    s += '<circle class="tac" cx="170" cy="130" r="5"/>'
    s += '<line class="pom" x1="170" y1="44" x2="170" y2="130"/>'
    s += '<text x="178" y="94">h</text>'
    s += '<text x="178" y="148">p</text>'
    s += '<text x="248" y="48">p<tspan class="sub" dy="5">0</tspan></text>'
    s += '<text x="84" y="160">ρ</text>'
    s += '</svg>'
    return s

def crtez_potisak():
    s = '<svg viewBox="0 0 300 190" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<rect class="lik" x="40" y="60" width="220" height="116" fill-opacity="0.8" stroke="none"/>'
    s += '<path class="ivica" d="M40,20 L40,176 L260,176 L260,20"/>'
    s += '<line class="lik-l" x1="40" y1="60" x2="260" y2="60"/>'
    s += '<rect class="lik2" x="120" y="88" width="60" height="50" rx="4"/>'
    s += strela(150, 112, 150, 28)
    s += '<text x="158" y="40">F</text>'
    s += strela(150, 116, 150, 166)
    s += '<text x="158" y="162">mg</text>'
    s += '<text x="54" y="160">ρ</text>'
    s += '</svg>'
    return s

def crtez_cev():
    s = '<svg viewBox="0 0 300 170" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<path class="lik" d="M14,40 L120,40 C150,40 160,64 190,64 L286,64 L286,106 L190,106 C160,106 150,130 120,130 L14,130 Z"/>'
    s += strela(36, 85, 96, 85)
    s += strela(206, 85, 276, 85)
    s += '<text x="52" y="76">v<tspan class="sub" dy="5">1</tspan></text>'
    s += '<text x="224" y="58" >v<tspan class="sub" dy="5">2</tspan></text>'
    s += '<text x="52" y="122">p<tspan class="sub" dy="5">1</tspan></text>'
    s += '<text x="224" y="130">p<tspan class="sub" dy="5">2</tspan></text>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'hidrostatika', 'simbol': 'p',
 'naziv': T("Hidrostatički pritisak","Hydrostatic pressure","Pressione idrostatica","Pression hydrostatique","Presión hidrostática","Hydrostatischer Druck","Pressão hidrostática","Гидростатическое давление"),
 'opis': T("Pritisak na dubini, stišljivost","Pressure at depth, compressibility","Pressione in profondità, comprimibilità","Pression en profondeur, compressibilité","Presión en profundidad, compresibilidad","Druck in der Tiefe, Kompressibilität","Pressão em profundidade, compressibilidade","Давление на глубине, сжимаемость"),
 'kljucne_reci': T("hidrostaticki pritisak dubina voda ronjenje atmosferski pritisak stisljivost","hydrostatic pressure depth water diving atmospheric pressure compressibility","pressione idrostatica profondita acqua immersione stevino comprimibilita","pression hydrostatique profondeur eau plongee compressibilite","presion hidrostatica profundidad agua buceo compresibilidad","hydrostatischer druck schweredruck tiefe wasser tauchen kompressibilitat","pressao hidrostatica profundidade agua mergulho stevin compressibilidade","гидростатическое давление глубина вода сжимаемость"),
 'crtez': crtez_hidro(),
 'formule': [
  F(T("Pritisak na dubini","Pressure at depth","Pressione in profondità","Pression en profondeur","Presión en profundidad","Druck in der Tiefe","Pressão em profundidade","Давление на глубине"),
    r"p = p_0 + \rho g h",
    T("p₀ je pritisak na površini (vazduh ≈ 101 kPa); svakih 10 m vode dodaje oko 1 bar.","p₀ is the pressure at the surface (air ≈ 101 kPa); every 10 m of water adds about 1 bar.","p₀ è la pressione in superficie (aria ≈ 101 kPa); ogni 10 m d’acqua aggiungono circa 1 bar.","p₀ est la pression à la surface (air ≈ 101 kPa) ; chaque 10 m d’eau ajoutent environ 1 bar.","p₀ es la presión en la superficie (aire ≈ 101 kPa); cada 10 m de agua añaden cerca de 1 bar.","p₀ ist der Druck an der Oberfläche (Luft ≈ 101 kPa); je 10 m Wasser kommt etwa 1 bar hinzu.","p₀ é a pressão na superfície (ar ≈ 101 kPa); cada 10 m de água somam cerca de 1 bar.","p₀ — давление на поверхности (воздух ≈ 101 кПа); каждые 10 м воды добавляют около 1 бар.")),
  F(T("Stišljivost","Compressibility","Comprimibilità","Compressibilité","Compresibilidad","Kompressibilität","Compressibilidade","Сжимаемость"),
    r"\frac{\Delta V}{V} = -\chi\,\Delta p",
    T("Relativna promena zapremine pri promeni pritiska; za vodu χ ≈ 0,46 GPa⁻¹, pa je skoro nestišljiva.","Relative change of volume with pressure; for water χ ≈ 0.46 GPa⁻¹, so it is almost incompressible.","Variazione relativa di volume con la pressione; per l’acqua χ ≈ 0,46 GPa⁻¹, quasi incomprimibile.","Variation relative de volume avec la pression ; pour l’eau χ ≈ 0,46 GPa⁻¹, presque incompressible.","Variación relativa de volumen con la presión; para el agua χ ≈ 0,46 GPa⁻¹, casi incompresible.","Relative Volumenänderung bei Druckänderung; für Wasser χ ≈ 0,46 GPa⁻¹, also fast inkompressibel.","Variação relativa de volume com a pressão; para a água χ ≈ 0,46 GPa⁻¹, quase incompressível.","Относительное изменение объёма при изменении давления; для воды χ ≈ 0,46 ГПа⁻¹ — почти несжимаема.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'ph': None, 'p': None, 'p0': 101325, 'rho': 1000, 'g': 9.81, 'h': 10, 'dV': None, 'chi': 4.6e-10, 'V0': 1, 'dp': 1e7},
                       {'ph': 'kPa', 'p': 'kPa', 'p0': 'kPa', 'dV': 'L', 'V0': 'L', 'dp': 'MPa'}),
  'jednacine': [
   {'latex': r"p = p_0 + \rho g h", 'trazi': 'p', 'resenja': {'p': 'p0 + rho*g*h', 'p0': 'p - rho*g*h', 'rho': '(p - p0)/(g*h)', 'h': '(p - p0)/(rho*g)'}, 'promenljive': ['p', 'p0', 'rho', 'g', 'h']},
   {'latex': r"p_h = \rho g h", 'trazi': 'ph', 'resenja': {'ph': 'rho*g*h', 'rho': 'ph/(g*h)', 'h': 'ph/(rho*g)'}, 'promenljive': ['ph', 'rho', 'g', 'h']},
   {'latex': r"\Delta V = \chi\, V \Delta p", 'trazi': 'dV', 'resenja': {'dV': 'chi*V0*dp', 'chi': 'dV/(V0*dp)', 'V0': 'dV/(chi*dp)', 'dp': 'dV/(chi*V0)'}},
  ]}
})

teme.append({
 'id': 'potisak', 'simbol': 'A',
 'naziv': T("Potisak (Arhimedov zakon)","Buoyancy (Archimedes’ principle)","Spinta di Archimede","Poussée d’Archimède","Empuje (principio de Arquímedes)","Auftrieb (Archimedisches Prinzip)","Empuxo (princípio de Arquimedes)","Закон Архимеда"),
 'opis': T("Sila potiska, plivanje","Buoyant force, floating","Spinta, galleggiamento","Poussée, flottaison","Empuje, flotación","Auftriebskraft, Schwimmen","Empuxo, flutuação","Выталкивающая сила, плавание"),
 'kljucne_reci': T("potisak arhimedov zakon plivanje tonjenje uronjeno telo brod led","buoyancy archimedes principle floating sinking submerged ship ice","spinta archimede galleggiamento affondamento nave ghiaccio","poussee archimede flottaison immerge bateau glace","empuje arquimedes flotacion hundimiento barco hielo","auftrieb archimedes schwimmen sinken eingetaucht schiff eis","empuxo arquimedes flutuacao afundar navio gelo","архимедова сила выталкивающая плавание тел корабль лёд"),
 'crtez': crtez_potisak(),
 'formule': [
  F(T("Sila potiska","Buoyant force","Spinta di Archimede","Poussée d’Archimède","Empuje","Auftriebskraft","Empuxo","Выталкивающая сила"),
    S(r"{Fp} = \rho\, g\, V"),
    T("Jednaka je težini tečnosti koju telo istisne; ρ je gustina tečnosti, a V zapremina uronjenog dela tela.","Equal to the weight of the displaced liquid; ρ is the density of the liquid and V the submerged volume.","È uguale al peso del liquido spostato; ρ è la densità del liquido e V il volume immerso.","Égale au poids du liquide déplacé ; ρ est la masse volumique du liquide et V le volume immergé.","Es igual al peso del líquido desalojado; ρ es la densidad del líquido y V el volumen sumergido.","Gleich der Gewichtskraft der verdrängten Flüssigkeit; ρ ist ihre Dichte, V das eingetauchte Volumen.","É igual ao peso do líquido deslocado; ρ é a massa específica do líquido e V o volume submerso.","Равна весу вытесненной жидкости; ρ — плотность жидкости, V — объём погружённой части.")),
  F(T("Plivanje","Floating","Galleggiamento","Flottaison","Flotación","Schwimmen","Flutuação","Плавание тел"),
    LJ(lambda j: OZ['ud'][j] + r" = \frac{" + OZ['rhot'][j] + r"}{\rho}"),
    T("Telo pliva ako je ređe od tečnosti; uronjeni deo je odnos gustina (led u vodi ≈ 92 %).","A body floats if it is less dense than the liquid; the submerged fraction is the density ratio (ice in water ≈ 92 %).","Un corpo galleggia se è meno denso del liquido; la parte immersa è il rapporto delle densità (ghiaccio ≈ 92 %).","Un corps flotte s’il est moins dense que le liquide ; la fraction immergée est le rapport des masses volumiques (glace ≈ 92 %).","Un cuerpo flota si es menos denso que el líquido; la fracción sumergida es la razón de densidades (hielo ≈ 92 %).","Ein Körper schwimmt, wenn seine Dichte kleiner ist; der eingetauchte Anteil ist das Dichteverhältnis (Eis ≈ 92 %).","Um corpo flutua se for menos denso que o líquido; a fração submersa é a razão das densidades (gelo ≈ 92 %).","Тело плавает, если его плотность меньше плотности жидкости; погружённая доля равна отношению плотностей (лёд ≈ 92 %).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Fp': None, 'rho': 1000, 'g': 9.81, 'V': 0.002, 'ud': None, 'rhot': 917}, {'V': 'L'}),
  'jednacine': [
   {'latex': S(r"{Fp} = \rho g V"), 'trazi': 'Fp', 'resenja': {'Fp': 'rho*g*V', 'rho': 'Fp/(g*V)', 'V': 'Fp/(rho*g)'}, 'promenljive': ['Fp', 'rho', 'g', 'V']},
   {'latex': LJ(lambda j: OZ['ud'][j] + r" = \dfrac{" + OZ['rhot'][j] + r"}{\rho}"), 'trazi': 'ud', 'resenja': {'ud': 'rhot/rho', 'rhot': 'ud*rho', 'rho': 'rhot/ud'},
    'napomene': {'ud': T("Ako je rezultat veći od 100 %, telo tone.","If the result is above 100 %, the body sinks.","Se il risultato supera il 100 %, il corpo affonda.","Si le résultat dépasse 100 %, le corps coule.","Si el resultado supera el 100 %, el cuerpo se hunde.","Liegt das Ergebnis über 100 %, sinkt der Körper.","Se o resultado passar de 100 %, o corpo afunda.","Если результат больше 100 %, тело тонет.")}},
  ]}
})

teme.append({
 'id': 'bernuli', 'simbol': 'v',
 'naziv': T("Bernulijeva jednačina","Bernoulli’s equation","Equazione di Bernoulli","Équation de Bernoulli","Ecuación de Bernoulli","Bernoulli-Gleichung","Equação de Bernoulli","Уравнение Бернулли"),
 'opis': T("Strujanje, Toričelijev zakon","Flow, Torricelli’s law","Flusso, legge di Torricelli","Écoulement, loi de Torricelli","Flujo, ley de Torricelli","Strömung, Torricelli","Escoamento, lei de Torricelli","Течение, формула Торричелли"),
 'kljucne_reci': T("bernulijeva jednacina strujanje tecnosti cev pritisak brzina toricelijev zakon isticanje","bernoulli equation fluid flow pipe pressure velocity torricelli outflow","equazione di bernoulli flusso tubo pressione velocita torricelli efflusso","equation de bernoulli ecoulement tuyau pression vitesse torricelli","ecuacion de bernoulli flujo tuberia presion velocidad torricelli","bernoulli gleichung stromung rohr druck geschwindigkeit torricelli ausfluss","equacao de bernoulli escoamento cano pressao velocidade torricelli","уравнение бернулли течение труба давление скорость торричелли"),
 'crtez': crtez_cev(),
 'formule': [
  F(T("Bernulijeva jednačina","Bernoulli’s equation","Equazione di Bernoulli","Équation de Bernoulli","Ecuación de Bernoulli","Bernoulli-Gleichung","Equação de Bernoulli","Уравнение Бернулли"),
    r"p_1 + \frac{\rho v_1^2}{2} + \rho g h_1 = p_2 + \frac{\rho v_2^2}{2} + \rho g h_2",
    T("Za nestišljivu tečnost bez trenja: gde tečnost teče brže, pritisak je manji.","For an incompressible, frictionless liquid: where it flows faster, the pressure is lower.","Per un liquido incomprimibile e senza attrito: dove scorre più veloce la pressione è minore.","Pour un liquide incompressible sans frottement : là où il va plus vite, la pression est plus faible.","Para un líquido incompresible sin rozamiento: donde fluye más rápido, la presión es menor.","Für eine reibungsfreie, inkompressible Flüssigkeit: wo sie schneller strömt, ist der Druck kleiner.","Para um líquido incompressível sem atrito: onde escoa mais rápido, a pressão é menor.","Для несжимаемой жидкости без трения: где течение быстрее, давление меньше.")),
  F(T("Isticanje kroz otvor (Toričeli)","Outflow through a hole (Torricelli)","Efflusso da un foro (Torricelli)","Écoulement par un orifice (Torricelli)","Salida por un orificio (Torricelli)","Ausfluss aus einer Öffnung (Torricelli)","Escoamento por um orifício (Torricelli)","Истечение из отверстия (Торричелли)"),
    r"v = \sqrt{2 g h}",
    T("Tečnost ističe iz otvora na dubini h ispod površine brzinom kao da je slobodno pala sa visine h.","Liquid leaves a hole at depth h with the speed of a free fall from height h.","Il liquido esce da un foro a profondità h con la velocità di una caduta libera da h.","Le liquide sort d’un orifice à la profondeur h avec la vitesse d’une chute libre de hauteur h.","El líquido sale por un orificio a profundidad h con la velocidad de una caída libre desde h.","Die Flüssigkeit tritt aus einer Öffnung in der Tiefe h so schnell aus wie nach freiem Fall aus h.","O líquido sai por um orifício à profundidade h com a velocidade de uma queda livre de h.","Жидкость вытекает из отверстия на глубине h со скоростью свободного падения с высоты h.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'p2': None, 'p1': 2e5, 'rho': 1000, 'v1': 2, 'v2': 5, 'v': None, 'g': 9.81, 'hv': 2}, {'p1': 'kPa', 'p2': 'kPa'}),
  'jednacine': [
   {'latex': r"p_1 + \dfrac{\rho v_1^2}{2} = p_2 + \dfrac{\rho v_2^2}{2}", 'trazi': 'p2',
    'resenja': {'p2': 'p1 + rho*(v1*v1 - v2*v2)/2', 'p1': 'p2 - rho*(v1*v1 - v2*v2)/2', 'v2': 'sqrt(v1*v1 + 2*(p1 - p2)/rho)', 'v1': 'sqrt(v2*v2 - 2*(p1 - p2)/rho)', 'rho': '2*(p2 - p1)/(v1*v1 - v2*v2)'},
    'napomene': {'p2': T("Vodoravna cev (h₁ = h₂).","Horizontal pipe (h₁ = h₂).","Tubo orizzontale (h₁ = h₂).","Tuyau horizontal (h₁ = h₂).","Tubería horizontal (h₁ = h₂).","Waagerechtes Rohr (h₁ = h₂).","Cano horizontal (h₁ = h₂).","Горизонтальная труба (h₁ = h₂).")}},
   {'latex': r"v = \sqrt{2 g h}", 'trazi': 'v', 'resenja': {'v': 'sqrt(2*g*hv)', 'hv': 'v*v/(2*g)', 'g': 'v*v/(2*hv)'}},
  ]}
})

teme.append({
 'id': 'otpor', 'simbol': 'η',
 'naziv': T("Otpor sredine","Drag","Resistenza del mezzo","Résistance du fluide","Resistencia del fluido","Strömungswiderstand","Resistência do fluido","Сопротивление среды"),
 'opis': T("Stoksov zakon, otpor vazduha","Stokes’ law, air drag","Legge di Stokes, resistenza dell’aria","Loi de Stokes, traînée","Ley de Stokes, resistencia del aire","Stokessches Gesetz, Luftwiderstand","Lei de Stokes, arrasto do ar","Закон Стокса, сопротивление воздуха"),
 'kljucne_reci': T("otpor sredine stoksov zakon viskoznost otpor vazduha koeficijent otpora","drag stokes law viscosity air resistance drag coefficient","resistenza stokes viscosita resistenza aerodinamica","trainee loi de stokes viscosite resistance de l air","resistencia stokes viscosidad arrastre aerodinamico","stromungswiderstand stokes viskositat luftwiderstand cw wert","arrasto stokes viscosidade resistencia do ar","сопротивление стокс вязкость сопротивление воздуха"),
 'formule': [
  F(T("Stoksov zakon (sporo kretanje)","Stokes’ law (slow motion)","Legge di Stokes (moto lento)","Loi de Stokes (mouvement lent)","Ley de Stokes (movimiento lento)","Stokessches Gesetz (langsam)","Lei de Stokes (movimento lento)","Закон Стокса (медленное движение)"),
    r"F = 6 \pi r \eta v",
    T("Sila otpora na malu kuglicu koja se sporo kreće kroz viskoznu tečnost (voda: η ≈ 1 mPa·s).","Drag on a small sphere moving slowly through a viscous fluid (water: η ≈ 1 mPa·s).","Forza su una piccola sfera che si muove lentamente in un fluido viscoso (acqua: η ≈ 1 mPa·s).","Force sur une petite bille se déplaçant lentement dans un fluide visqueux (eau : η ≈ 1 mPa·s).","Fuerza sobre una pequeña esfera que se mueve lentamente en un fluido viscoso (agua: η ≈ 1 mPa·s).","Widerstand einer kleinen Kugel, die sich langsam in einer zähen Flüssigkeit bewegt (Wasser: η ≈ 1 mPa·s).","Força sobre uma pequena esfera que se move lentamente num fluido viscoso (água: η ≈ 1 mPa·s).","Сила сопротивления маленькому шарику в вязкой жидкости (вода: η ≈ 1 мПа·с).")),
  F(T("Otpor pri većim brzinama","Drag at higher speeds","Resistenza ad alta velocità","Traînée à grande vitesse","Resistencia a altas velocidades","Widerstand bei höheren Geschwindigkeiten","Arrasto em velocidades maiores","Сопротивление при больших скоростях"),
    S(r"F = \frac{1}{2}\, {c}\, \rho\, S\, v^2"),
    T("Raste sa kvadratom brzine; za automobil koeficijent je oko 0,3, a gustina vazduha 1,2 kg/m³.","Grows with the square of speed; a car has a coefficient of about 0.3; air density is 1.2 kg/m³.","Cresce con il quadrato della velocità; per un’auto il coefficiente è circa 0,3; aria 1,2 kg/m³.","Croît avec le carré de la vitesse ; une voiture a un coefficient d’environ 0,3 ; air 1,2 kg/m³.","Crece con el cuadrado de la velocidad; un coche tiene un coeficiente de unos 0,3; aire 1,2 kg/m³.","Wächst mit dem Quadrat der Geschwindigkeit; ein Auto hat einen Beiwert von etwa 0,3; Luft 1,2 kg/m³.","Cresce com o quadrado da velocidade; um carro tem coeficiente de cerca de 0,3; ar 1,2 kg/m³.","Растёт с квадратом скорости; у автомобиля коэффициент около 0,3; плотность воздуха 1,2 кг/м³.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Fs': None, 'r': 0.005, 'eta': 1.4, 'vk': 0.05, 'Fu': None, 'cw': 0.3, 'rhov': 1.2, 'S': 2.2, 'vv': 100 / 3.6},
                       {'r': 'mm', 'eta': 'Pa·s', 'vk': 'm/s', 'vv': 'km/h', 'Fs': 'mN'}),
  'jednacine': [
   {'latex': r"F = 6 \pi r \eta v", 'trazi': 'Fs', 'resenja': {'Fs': '6*PI*r*eta*vk', 'r': 'Fs/(6*PI*eta*vk)', 'eta': 'Fs/(6*PI*r*vk)', 'vk': 'Fs/(6*PI*r*eta)'}},
   {'latex': S(r"F = \dfrac{1}{2} {c} \rho S v^2"), 'trazi': 'Fu', 'promenljive': ['Fu', 'cw', 'rhov', 'S', 'vv'],
    'resenja': {'Fu': 'cw*rhov*S*vv*vv/2', 'cw': '2*Fu/(rhov*S*vv*vv)', 'S': '2*Fu/(cw*rhov*vv*vv)', 'vv': 'sqrt(2*Fu/(cw*rhov*S))'}},
  ]}
})
teme[-1]['kalkulator']['velicine']['Fs']['nenegativna'] = True

teme.append({
 'id': 'povrsinski_napon', 'simbol': 'γ',
 'naziv': T("Površinski napon","Surface tension","Tensione superficiale","Tension superficielle","Tensión superficial","Oberflächenspannung","Tensão superficial","Поверхностное натяжение"),
 'opis': T("Kapi i mehurovi","Drops and bubbles","Gocce e bolle","Gouttes et bulles","Gotas y burbujas","Tropfen und Blasen","Gotas e bolhas","Капли и пузыри"),
 'kljucne_reci': T("povrsinski napon kap mehur sapunica natpritisak tecnost","surface tension drop bubble soap excess pressure liquid","tensione superficiale goccia bolla sapone sovrapressione","tension superficielle goutte bulle savon surpression","tension superficial gota burbuja jabon sobrepresion","oberflachenspannung tropfen seifenblase uberdruck","tensao superficial gota bolha sabao sobrepressao","поверхностное натяжение капля пузырь мыльный избыточное давление"),
 'formule': [
  F(T("Sila površinskog napona","Surface tension force","Forza di tensione superficiale","Force de tension superficielle","Fuerza de tensión superficial","Kraft der Oberflächenspannung","Força de tensão superficial","Сила поверхностного натяжения"),
    S(r"F = {g}\, l"),
    T("Deluje duž ivice dužine l; za vodu iznosi oko 0,073 N/m.","Acts along an edge of length l; for water it is about 0.073 N/m.","Agisce lungo un bordo di lunghezza l; per l’acqua vale circa 0,073 N/m.","Agit le long d’un bord de longueur l ; pour l’eau elle vaut environ 0,073 N/m.","Actúa a lo largo de un borde de longitud l; para el agua vale unos 0,073 N/m.","Wirkt entlang eines Randes der Länge l; für Wasser etwa 0,073 N/m.","Atua ao longo de uma borda de comprimento l; para a água vale cerca de 0,073 N/m.","Действует вдоль границы длиной l; для воды около 0,073 Н/м.")),
  F(T("Natpritisak u kapi i mehuru","Excess pressure in a drop and a bubble","Sovrapressione in goccia e bolla","Surpression dans une goutte et une bulle","Sobrepresión en gota y burbuja","Überdruck in Tropfen und Blase","Sobrepressão em gota e bolha","Избыточное давление в капле и пузыре"),
    LJ(lambda j: (r"\Delta p_1 = \frac{2%s}{r}, \quad \Delta p_2 = \frac{4%s}{r}" % (GAM[j], GAM[j]))),
    T("Δp₁ za kap tečnosti (jedna površina), Δp₂ za mehur od sapunice (dve površine). Manja kap ima veći pritisak.","Δp₁ for a liquid drop (one surface), Δp₂ for a soap bubble (two surfaces). A smaller drop has a higher pressure.","Δp₁ per una goccia (una superficie), Δp₂ per una bolla di sapone (due superfici). Una goccia più piccola ha pressione maggiore.","Δp₁ pour une goutte (une surface), Δp₂ pour une bulle de savon (deux surfaces). Une goutte plus petite a une pression plus élevée.","Δp₁ para una gota (una superficie), Δp₂ para una pompa de jabón (dos superficies). Una gota más pequeña tiene mayor presión.","Δp₁ für einen Tropfen (eine Oberfläche), Δp₂ für eine Seifenblase (zwei Oberflächen). Kleinere Tropfen haben höheren Druck.","Δp₁ para uma gota (uma superfície), Δp₂ para uma bolha de sabão (duas superfícies). Uma gota menor tem pressão maior.","Δp₁ — для капли (одна поверхность), Δp₂ — для мыльного пузыря (две поверхности). У меньшей капли давление больше.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'gam': 0.0728, 'l': 0.05, 'dpk': None, 'dpm': None, 'rk': 0.001}, {'gam': 'mN/m', 'l': 'cm', 'rk': 'mm', 'F': 'mN'}),
  'jednacine': [
   {'latex': S(r"F = {g} l"), 'trazi': 'F', 'resenja': {'F': 'gam*l', 'gam': 'F/l', 'l': 'F/gam'}},
   {'latex': LJ(lambda j: r"\Delta p_1 = \dfrac{2%s}{r}" % GAM[j]), 'trazi': 'dpk', 'resenja': {'dpk': '2*gam/rk', 'gam': 'dpk*rk/2', 'rk': '2*gam/dpk'}},
   {'latex': LJ(lambda j: r"\Delta p_2 = \dfrac{4%s}{r}" % GAM[j]), 'trazi': 'dpm', 'resenja': {'dpm': '4*gam/rk', 'gam': 'dpm*rk/4', 'rk': '4*gam/dpm'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']
v['dpk']['oznaka'] = r'\Delta p_1'; v['dpm']['oznaka'] = r'\Delta p_2'

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)

out = {'oblast': 'fluidi', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
