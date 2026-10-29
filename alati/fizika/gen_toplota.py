# Generiše assets/oblasti/toplota.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']

# Oznake po jeziku
RAD = dict(sr='A', en='W', it='L', fr='W', es='W', de='W', pt='W', ru='A')
LAT = dict(sr='q', en='L', it=r'\lambda', fr='L', es='L', de='q', pt='L', ru=r'\lambda')
LAM = dict(sr=r'\lambda', en='k', it=r'\lambda', fr=r'\lambda', es='k', de=r'\lambda', pt='k', ru=r'\lambda')
Q1 = dict(sr='Q_1', en='Q_H', it='Q_1', fr='Q_1', es='Q_1', de=r'Q_{\mathrm{zu}}', pt='Q_1', ru='Q_1')
Q2 = dict(sr='Q_2', en='Q_C', it='Q_2', fr='Q_2', es='Q_2', de=r'Q_{\mathrm{ab}}', pt='Q_2', ru='Q_2')
T1 = dict(sr='T_1', en='T_H', it='T_1', fr='T_1', es='T_1', de='T_1', pt='T_1', ru='T_1')
T2 = dict(sr='T_2', en='T_C', it='T_2', fr='T_2', es='T_2', de='T_2', pt='T_2', ru='T_2')
def S(f):
    def z(j):
        x = f
        for k, d in (('{A}', RAD), ('{q}', LAT), ('{lam}', LAM), ('{Q1}', Q1), ('{Q2}', Q2), ('{T1}', T1), ('{T2}', T2)):
            x = x.replace(k, d[j])
        return x
    return LJ(z)

N = {
 'dl': T("produženje","change in length","allungamento","allongement","dilatación lineal","Längenänderung","dilatação linear","удлинение"),
 'l': T("početna dužina","initial length","lunghezza iniziale","longueur initiale","longitud inicial","Anfangslänge","comprimento inicial","начальная длина"),
 'alfa': T("koeficijent linearnog širenja","coefficient of linear expansion","coefficiente di dilatazione lineare","coefficient de dilatation linéaire","coeficiente de dilatación lineal","Längenausdehnungskoeffizient","coeficiente de dilatação linear","коэффициент линейного расширения"),
 'dT': T("promena temperature","change in temperature","variazione di temperatura","variation de température","variación de temperatura","Temperaturänderung","variação de temperatura","изменение температуры"),
 'dV': T("povećanje zapremine","change in volume","variazione di volume","variation de volume","variación de volumen","Volumenänderung","variação de volume","изменение объёма"),
 'V': T("zapremina","volume","volume","volume","volumen","Volumen","volume","объём"),
 'beta': T("koeficijent zapreminskog širenja","coefficient of volume expansion","coefficiente di dilatazione cubica","coefficient de dilatation volumique","coeficiente de dilatación volumétrica","Volumenausdehnungskoeffizient","coeficiente de dilatação volumétrica","коэффициент объёмного расширения"),
 'Q': T("količina toplote","heat","calore","chaleur","calor","Wärme","calor","количество теплоты"),
 'm': T("masa","mass","massa","masse","masa","Masse","massa","масса"),
 'c': T("specifični toplotni kapacitet","specific heat capacity","calore specifico","capacité thermique massique","calor específico","spezifische Wärmekapazität","calor específico","удельная теплоёмкость"),
 'q': T("specifična toplota (topljenja, isparavanja, sagorevanja)","specific latent heat (or heat of combustion)","calore latente specifico (o potere calorifico)","chaleur latente massique (ou pouvoir calorifique)","calor latente específico (o poder calorífico)","spezifische Umwandlungswärme (oder Heizwert)","calor latente específico (ou poder calorífico)","удельная теплота (плавления, парообразования, сгорания)"),
 'P': T("snaga grejača","heater power","potenza del riscaldatore","puissance du chauffage","potencia del calentador","Heizleistung","potência do aquecedor","мощность нагревателя"),
 't': T("vreme","time","tempo","temps","tiempo","Zeit","tempo","время"),
 'p': T("pritisak","pressure","pressione","pression","presión","Druck","pressão","давление"),
 'M': T("molarna masa","molar mass","massa molare","masse molaire","masa molar","molare Masse","massa molar","молярная масса"),
 'R': T("univerzalna gasna konstanta","molar gas constant","costante dei gas","constante des gaz parfaits","constante de los gases","universelle Gaskonstante","constante dos gases","универсальная газовая постоянная"),
 'Tt': T("temperatura","temperature","temperatura","température","temperatura","Temperatur","temperatura","температура"),
 'p1': T("pritisak u stanju 1","pressure in state 1","pressione nello stato 1","pression dans l’état 1","presión en el estado 1","Druck im Zustand 1","pressão no estado 1","давление в состоянии 1"),
 'V1': T("zapremina u stanju 1","volume in state 1","volume nello stato 1","volume dans l’état 1","volumen en el estado 1","Volumen im Zustand 1","volume no estado 1","объём в состоянии 1"),
 'T1': T("temperatura u stanju 1","temperature in state 1","temperatura nello stato 1","température dans l’état 1","temperatura en el estado 1","Temperatur im Zustand 1","temperatura no estado 1","температура в состоянии 1"),
 'p2': T("pritisak u stanju 2","pressure in state 2","pressione nello stato 2","pression dans l’état 2","presión en el estado 2","Druck im Zustand 2","pressão no estado 2","давление в состоянии 2"),
 'V2': T("zapremina u stanju 2","volume in state 2","volume nello stato 2","volume dans l’état 2","volumen en el estado 2","Volumen im Zustand 2","volume no estado 2","объём в состоянии 2"),
 'T2': T("temperatura u stanju 2","temperature in state 2","temperatura nello stato 2","température dans l’état 2","temperatura en el estado 2","Temperatur im Zustand 2","temperatura no estado 2","температура в состоянии 2"),
 'dU': T("promena unutrašnje energije","change in internal energy","variazione di energia interna","variation d’énergie interne","variación de energía interna","Änderung der inneren Energie","variação da energia interna","изменение внутренней энергии"),
 'A': T("rad izvršen nad gasom","work done on the gas","lavoro compiuto sul gas","travail reçu par le gaz","trabajo realizado sobre el gas","am Gas verrichtete Arbeit","trabalho realizado sobre o gás","работа внешних сил над газом"),
 'Qd': T("dovedena toplota","heat added","calore fornito","chaleur reçue","calor suministrado","zugeführte Wärme","calor fornecido","подведённое тепло"),
 'cv': T("specifična toplota pri stalnoj zapremini","specific heat at constant volume","calore specifico a volume costante","capacité thermique massique à volume constant","calor específico a volumen constante","spezifische Wärme bei konstantem Volumen","calor específico a volume constante","удельная теплоёмкость при постоянном объёме"),
 'kapa': T("odnos specifičnih toplota","heat capacity ratio","rapporto dei calori specifici","indice adiabatique","coeficiente adiabático","Isentropenexponent","coeficiente de Poisson","показатель адиабаты"),
 'eta': T("stepen korisnog dejstva","efficiency","rendimento","rendement","rendimiento","Wirkungsgrad","rendimento","КПД"),
 'Wr': T("koristan rad","useful work","lavoro utile","travail utile","trabajo útil","Nutzarbeit","trabalho útil","полезная работа"),
 'Q1': T("toplota od toplijeg tela","heat from the hot reservoir","calore dalla sorgente calda","chaleur reçue de la source chaude","calor del foco caliente","vom warmen Reservoir aufgenommene Wärme","calor da fonte quente","теплота от нагревателя"),
 'Q2': T("toplota predata hladnijem telu","heat to the cold reservoir","calore ceduto alla sorgente fredda","chaleur cédée à la source froide","calor cedido al foco frío","an das kalte Reservoir abgegebene Wärme","calor cedido à fonte fria","теплота, отданная холодильнику"),
 'Tv': T("temperatura toplijeg tela","temperature of the hot reservoir","temperatura della sorgente calda","température de la source chaude","temperatura del foco caliente","Temperatur des warmen Reservoirs","temperatura da fonte quente","температура нагревателя"),
 'Tn': T("temperatura hladnijeg tela","temperature of the cold reservoir","temperatura della sorgente fredda","température de la source froide","temperatura del foco frío","Temperatur des kalten Reservoirs","temperatura da fonte fria","температура холодильника"),
 'Pt': T("toplotna snaga (protok toplote)","heat flow rate","flusso di calore","flux thermique","flujo de calor","Wärmestrom","fluxo de calor","тепловой поток"),
 'lam': T("toplotna provodljivost","thermal conductivity","conducibilità termica","conductivité thermique","conductividad térmica","Wärmeleitfähigkeit","condutividade térmica","теплопроводность"),
 'S': T("površina","area","area","aire","área","Fläche","área","площадь"),
 'dx': T("debljina","thickness","spessore","épaisseur","espesor","Dicke","espessura","толщина"),
 'n': T("broj molekula u jedinici zapremine","number density","densità numerica","densité particulaire","densidad de partículas","Teilchenzahldichte","densidade de partículas","концентрация молекул"),
 'k': T("Bolcmanova konstanta","Boltzmann constant","costante di Boltzmann","constante de Boltzmann","constante de Boltzmann","Boltzmann-Konstante","constante de Boltzmann","постоянная Больцмана"),
 'Ek': T("srednja kinetička energija molekula","mean kinetic energy of a molecule","energia cinetica media di una molecola","énergie cinétique moyenne d’une molécule","energía cinética media de una molécula","mittlere kinetische Energie eines Moleküls","energia cinética média de uma molécula","средняя кинетическая энергия молекулы"),
 'v': T("srednja kvadratna brzina molekula","root-mean-square speed","velocità quadratica media","vitesse quadratique moyenne","velocidad cuadrática media","mittlere quadratische Geschwindigkeit","velocidade quadrática média","среднеквадратичная скорость"),
}
OZ = {'dl': r'\Delta l', 'l': 'l', 'alfa': r'\alpha', 'dT': r'\Delta T', 'dV': r'\Delta V', 'V': 'V', 'beta': r'\beta', 'Q': 'Q',
      'm': 'm', 'c': 'c', 'q': S('{q}'), 'P': 'P', 't': 't', 'p': 'p', 'M': 'M', 'R': 'R', 'Tt': 'T', 'p1': 'p_1', 'V1': 'V_1',
      'T1': 'T_1', 'p2': 'p_2', 'V2': 'V_2', 'T2': 'T_2', 'dU': r'\Delta U', 'A': S('{A}'), 'Qd': 'Q', 'cv': 'c_v',
      'kapa': r'\kappa', 'eta': r'\eta', 'Wr': S('{A}'), 'Q1': S('{Q1}'), 'Q2': S('{Q2}'), 'Tv': S('{T1}'), 'Tn': S('{T2}'),
      'Pt': 'P', 'lam': S('{lam}'), 'S': 'S', 'dx': r'\Delta x', 'n': 'n', 'k': 'k', 'Ek': r'\bar E_k', 'v': r'\bar v'}
OZ['Ek'] = LJ(lambda j: r'\overline{E}_{\text{к}}' if j == 'ru' else r'\overline{E}_k')
OZ['v'] = r'v_{\mathrm{rms}}'
VRSTA = {'dl': 'duzina', 'l': 'duzina', 'alfa': 'koefSirenja', 'dT': 'tempRazlika', 'dV': 'zapremina', 'V': 'zapremina',
         'beta': 'koefSirenja', 'Q': 'energija', 'm': 'masa', 'c': 'specToplota', 'q': 'specLatentna', 'P': 'snaga', 't': 'vreme',
         'p': 'pritisak', 'M': 'molarnaMasa', 'R': 'gasKonst', 'Tt': 'temperatura', 'p1': 'pritisak', 'V1': 'zapremina',
         'T1': 'temperatura', 'p2': 'pritisak', 'V2': 'zapremina', 'T2': 'temperatura', 'dU': 'energija', 'A': 'energija',
         'Qd': 'energija', 'cv': 'specToplota', 'kapa': 'bez', 'eta': 'udeo', 'Wr': 'energija', 'Q1': 'energija', 'Q2': 'energija',
         'Tv': 'temperatura', 'Tn': 'temperatura', 'Pt': 'snaga', 'lam': 'toplProvodljivost', 'S': 'povrsina', 'dx': 'duzina',
         'n': 'koncentracija', 'k': 'boltzmann', 'Ek': 'energija', 'v': 'brzina'}
POZ = {'l', 'alfa', 'V', 'beta', 'm', 'c', 'q', 'P', 't', 'p', 'M', 'R', 'Tt', 'p1', 'V1', 'T1', 'p2', 'V2', 'T2', 'cv', 'kapa',
       'Q1', 'Tv', 'Tn', 'lam', 'S', 'dx', 'n', 'k', 'Ek', 'v'}
NENEG = {'Q2'}

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
K0 = 273.15

teme = []

teme.append({
 'id': 'sirenje', 'simbol': 'α',
 'naziv': T("Toplotno širenje","Thermal expansion","Dilatazione termica","Dilatation thermique","Dilatación térmica","Wärmeausdehnung","Dilatação térmica","Тепловое расширение"),
 'opis': T("Linearno i zapreminsko","Linear and volume","Lineare e cubica","Linéaire et volumique","Lineal y volumétrica","Längen- und Volumenausdehnung","Linear e volumétrica","Линейное и объёмное"),
 'kljucne_reci': T("toplotno sirenje linearno zapreminsko sina most koeficijent sirenja","thermal expansion linear volume rail bridge expansion coefficient","dilatazione termica lineare cubica binario ponte","dilatation thermique lineaire volumique rail pont","dilatacion termica lineal volumetrica riel puente","warmeausdehnung langenausdehnung volumenausdehnung schiene brucke","dilatacao termica linear volumetrica trilho ponte","тепловое расширение линейное объёмное рельс мост"),
 'formule': [
  F(T("Linearno širenje","Linear expansion","Dilatazione lineare","Dilatation linéaire","Dilatación lineal","Längenausdehnung","Dilatação linear","Линейное расширение"),
    r"\Delta l = \alpha\, l\, \Delta T",
    T("Za čelik α ≈ 12 · 10⁻⁶ K⁻¹: šina od 30 m se na 40 °C razlike produži oko 1,4 cm.","For steel α ≈ 12 · 10⁻⁶ K⁻¹: a 30 m rail lengthens by about 1.4 cm over 40 °C.","Per l’acciaio α ≈ 12 · 10⁻⁶ K⁻¹: un binario di 30 m si allunga di circa 1,4 cm per 40 °C.","Pour l’acier α ≈ 12 · 10⁻⁶ K⁻¹ : un rail de 30 m s’allonge d’environ 1,4 cm pour 40 °C.","Para el acero α ≈ 12 · 10⁻⁶ K⁻¹: un riel de 30 m se alarga unos 1,4 cm con 40 °C.","Für Stahl α ≈ 12 · 10⁻⁶ K⁻¹: eine 30-m-Schiene wird bei 40 °C etwa 1,4 cm länger.","Para o aço α ≈ 12 · 10⁻⁶ K⁻¹: um trilho de 30 m alonga cerca de 1,4 cm com 40 °C.","Для стали α ≈ 12 · 10⁻⁶ К⁻¹: рельс длиной 30 м удлиняется на 1,4 см при 40 °C.")),
  F(T("Zapreminsko širenje","Volume expansion","Dilatazione cubica","Dilatation volumique","Dilatación volumétrica","Volumenausdehnung","Dilatação volumétrica","Объёмное расширение"),
    r"\Delta V = \beta\, V\, \Delta T, \quad \beta = 3\alpha",
    T("β = 3α važi za čvrsta tela; tečnosti imaju sopstveni β.","β = 3α holds for solids; liquids have their own β.","β = 3α vale per i solidi; i liquidi hanno un proprio β.","β = 3α vaut pour les solides ; les liquides ont leur propre β.","β = 3α vale para sólidos; los líquidos tienen su propio β.","β = 3α gilt für Festkörper; Flüssigkeiten haben ein eigenes β.","β = 3α vale para sólidos; os líquidos têm seu próprio β.","β = 3α для твёрдых тел; у жидкостей свой β.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'dl': None, 'alfa': 12e-6, 'l': 30, 'dT': 40, 'dV': None, 'beta': 210e-6, 'V': 0.001},
                       {'alfa': '10⁻⁶/K', 'beta': '10⁻⁶/K', 'dl': 'mm', 'V': 'L', 'dV': 'mL', 'dT': '°C'}),
  'jednacine': [
   {'latex': r"\Delta l = \alpha l \Delta T", 'trazi': 'dl', 'resenja': {'dl': 'alfa*l*dT', 'alfa': 'dl/(l*dT)', 'l': 'dl/(alfa*dT)', 'dT': 'dl/(alfa*l)'}},
   {'latex': r"\Delta V = \beta V \Delta T", 'trazi': 'dV', 'resenja': {'dV': 'beta*V*dT', 'beta': 'dV/(V*dT)', 'V': 'dV/(beta*dT)', 'dT': 'dV/(beta*V)'},
    'napomene': {'dV': T("Podrazumevano: voda (β ≈ 210 · 10⁻⁶ K⁻¹).","Default: water (β ≈ 210 · 10⁻⁶ K⁻¹).","Predefinito: acqua (β ≈ 210 · 10⁻⁶ K⁻¹).","Par défaut : eau (β ≈ 210 · 10⁻⁶ K⁻¹).","Por defecto: agua (β ≈ 210 · 10⁻⁶ K⁻¹).","Voreinstellung: Wasser (β ≈ 210 · 10⁻⁶ K⁻¹).","Padrão: água (β ≈ 210 · 10⁻⁶ K⁻¹).","По умолчанию: вода (β ≈ 210 · 10⁻⁶ К⁻¹).")}},
  ]}
})

teme.append({
 'id': 'kolicina_toplote', 'simbol': 'Q',
 'naziv': T("Količina toplote","Heat","Quantità di calore","Quantité de chaleur","Cantidad de calor","Wärmemenge","Quantidade de calor","Количество теплоты"),
 'opis': T("Zagrevanje, topljenje, sagorevanje","Heating, melting, combustion","Riscaldamento, fusione, combustione","Chauffage, fusion, combustion","Calentamiento, fusión, combustión","Erwärmen, Schmelzen, Verbrennen","Aquecimento, fusão, combustão","Нагревание, плавление, сгорание"),
 'kljucne_reci': T("kolicina toplote specificni toplotni kapacitet zagrevanje vode topljenje leda isparavanje sagorevanje grejac bojler","heat specific heat capacity heating water melting ice vaporization combustion heater kettle","calore specifico riscaldamento acqua fusione ghiaccio evaporazione combustione","chaleur capacite thermique chauffage eau fusion glace vaporisation combustion","calor especifico calentamiento agua fusion hielo vaporizacion combustion","warme spezifische warmekapazitat erwarmen wasser schmelzen eis verdampfen verbrennen heizwert","calor especifico aquecimento agua fusao gelo vaporizacao combustao","количество теплоты удельная теплоёмкость нагревание плавление льда парообразование сгорание"),
 'formule': [
  F(T("Zagrevanje","Heating","Riscaldamento","Chauffage","Calentamiento","Erwärmen","Aquecimento","Нагревание"),
    r"Q = m\, c\, \Delta T",
    T("Za vodu c ≈ 4186 J/(kg·K): za 1 L vode i 1 °C treba oko 4,2 kJ. Za gas razlikujemo c_p (stalan pritisak) i c_v (stalna zapremina).","For water c ≈ 4186 J/(kg·K): 1 L of water needs about 4.2 kJ per 1 °C. For gases c_p (constant pressure) and c_v (constant volume) differ.","Per l’acqua c ≈ 4186 J/(kg·K): 1 L d’acqua richiede circa 4,2 kJ per 1 °C. Per i gas si distinguono c_p e c_v.","Pour l’eau c ≈ 4186 J/(kg·K) : 1 L d’eau demande environ 4,2 kJ par °C. Pour les gaz on distingue c_p et c_v.","Para el agua c ≈ 4186 J/(kg·K): 1 L de agua necesita unos 4,2 kJ por °C. En gases se distinguen c_p y c_v.","Für Wasser c ≈ 4186 J/(kg·K): 1 L Wasser braucht pro °C etwa 4,2 kJ. Bei Gasen unterscheidet man c_p und c_v.","Para a água c ≈ 4186 J/(kg·K): 1 L de água precisa de cerca de 4,2 kJ por °C. Em gases distinguem-se c_p e c_v.","Для воды c ≈ 4186 Дж/(кг·К): для 1 л воды на 1 °C нужно около 4,2 кДж. Для газов различают c_p и c_v.")),
  F(T("Promena agregatnog stanja i sagorevanje","Change of state and combustion","Cambiamento di stato e combustione","Changement d’état et combustion","Cambio de estado y combustión","Phasenübergang und Verbrennung","Mudança de estado e combustão","Фазовые переходы и сгорание"),
    S(r"Q = {q}\, m"),
    T("Topljenje leda: 334 kJ/kg; isparavanje vode: 2260 kJ/kg; sagorevanje benzina ≈ 46 MJ/kg.","Melting ice: 334 kJ/kg; boiling water: 2260 kJ/kg; burning petrol ≈ 46 MJ/kg.","Fusione del ghiaccio: 334 kJ/kg; evaporazione dell’acqua: 2260 kJ/kg; benzina ≈ 46 MJ/kg.","Fusion de la glace : 334 kJ/kg ; vaporisation de l’eau : 2260 kJ/kg ; essence ≈ 46 MJ/kg.","Fusión del hielo: 334 kJ/kg; vaporización del agua: 2260 kJ/kg; gasolina ≈ 46 MJ/kg.","Schmelzen von Eis: 334 kJ/kg; Verdampfen von Wasser: 2260 kJ/kg; Benzin ≈ 46 MJ/kg.","Fusão do gelo: 334 kJ/kg; vaporização da água: 2260 kJ/kg; gasolina ≈ 46 MJ/kg.","Плавление льда: 334 кДж/кг; парообразование воды: 2260 кДж/кг; бензин ≈ 46 МДж/кг.")),
  F(T("Toplotna snaga","Heating power","Potenza termica","Puissance thermique","Potencia térmica","Wärmeleistung","Potência térmica","Тепловая мощность"),
    r"P = \frac{Q}{\Delta t}",
    T("Grejač snage P za vreme Δt preda toplotu Q (ako nema gubitaka).","A heater of power P delivers heat Q in time Δt (without losses).","Un riscaldatore di potenza P fornisce il calore Q nel tempo Δt (senza perdite).","Un chauffage de puissance P fournit la chaleur Q en Δt (sans pertes).","Un calentador de potencia P entrega el calor Q en Δt (sin pérdidas).","Ein Heizer der Leistung P gibt in Δt die Wärme Q ab (ohne Verluste).","Um aquecedor de potência P fornece o calor Q em Δt (sem perdas).","Нагреватель мощностью P за время Δt отдаёт теплоту Q (без потерь).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Q': None, 'm': 1, 'c': 4186, 'dT': 80, 'q': 334e3, 'P': 2000, 't': None},
                       {'Q': 'kJ', 'dT': '°C', 'q': 'kJ/kg', 't': 'min', 'P': 'kW'}),
  'jednacine': [
   {'latex': r"Q = m c \Delta T", 'trazi': 'Q', 'resenja': {'Q': 'm*c*dT', 'm': 'Q/(c*dT)', 'c': 'Q/(m*dT)', 'dT': 'Q/(m*c)'}},
   {'latex': S(r"Q = {q} m"), 'trazi': 'Q', 'resenja': {'Q': 'q*m', 'q': 'Q/m', 'm': 'Q/q'}},
   {'latex': r"t = \dfrac{Q}{P}", 'trazi': 't', 'resenja': {'t': 'Q/P', 'Q': 'P*t', 'P': 'Q/t'},
    'napomene': {'t': T("Npr. koliko dugo kuvalo zagreva vodu (bez gubitaka).","E.g. how long a kettle takes to heat the water (no losses).","Es. quanto tempo impiega un bollitore (senza perdite).","Ex. durée de chauffe d’une bouilloire (sans pertes).","P. ej., cuánto tarda un hervidor (sin pérdidas).","Z. B. wie lange ein Wasserkocher braucht (ohne Verluste).","Ex.: quanto tempo uma chaleira leva (sem perdas).","Например, сколько греется чайник (без потерь).")}},
  ]}
})
teme[-1]['kalkulator']['velicine']['m']['naziv'] = T("masa","mass","massa","masse","masa","Masse","massa","масса")

teme.append({
 'id': 'gasni_zakoni', 'simbol': 'pV',
 'naziv': T("Jednačina stanja gasa","Ideal gas law","Equazione di stato dei gas","Loi des gaz parfaits","Ecuación de los gases ideales","Zustandsgleichung idealer Gase","Equação dos gases ideais","Уравнение состояния газа"),
 'opis': T("pV = nRT, gasni zakoni","pV = nRT, gas laws","pV = nRT, leggi dei gas","pV = nRT, lois des gaz","pV = nRT, leyes de los gases","pV = nRT, Gasgesetze","pV = nRT, leis dos gases","pV = νRT, газовые законы"),
 'kljucne_reci': T("jednacina stanja idealan gas gasni zakoni izoterma izobara izohora boyle mariotte gej lisak sarl dalton parcijalni pritisak","ideal gas law gas laws isothermal isobaric isochoric boyle charles gay lussac dalton partial pressure","equazione di stato gas perfetto boyle charles gay lussac dalton pressione parziale","loi des gaz parfaits boyle mariotte charles gay lussac dalton pression partielle","gases ideales boyle mariotte charles gay lussac dalton presion parcial","ideales gas zustandsgleichung boyle mariotte gay lussac dalton partialdruck","gases ideais clapeyron boyle charles gay lussac dalton pressao parcial","уравнение менделеева клапейрона идеальный газ бойля мариотта гей люссака шарля дальтона парциальное давление"),
 'formule': [
  F(T("Jednačina stanja idealnog gasa","Ideal gas equation","Equazione di stato","Équation d’état","Ecuación de estado","Zustandsgleichung","Equação de estado","Уравнение Менделеева — Клапейрона"),
    r"p V = \frac{m}{M} R T",
    T("T je apsolutna temperatura u kelvinima; R = 8,314 J/(mol·K); m/M je broj molova.","T is the absolute temperature in kelvin; R = 8.314 J/(mol·K); m/M is the amount in moles.","T è la temperatura assoluta in kelvin; R = 8,314 J/(mol·K); m/M è il numero di moli.","T est la température absolue en kelvins ; R = 8,314 J/(mol·K) ; m/M est la quantité de matière.","T es la temperatura absoluta en kelvin; R = 8,314 J/(mol·K); m/M es el número de moles.","T ist die absolute Temperatur in Kelvin; R = 8,314 J/(mol·K); m/M ist die Stoffmenge.","T é a temperatura absoluta em kelvin; R = 8,314 J/(mol·K); m/M é o número de mols.","T — абсолютная температура в кельвинах; R = 8,314 Дж/(моль·К); m/M — количество вещества.")),
  F(T("Promena stanja","Change of state","Trasformazione","Transformation","Cambio de estado","Zustandsänderung","Transformação","Изменение состояния"),
    r"\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}",
    T("Za istu količinu gasa. Posebni slučajevi: T = const (Bojl-Mariot), p = const (Gej-Lisak), V = const (Šarl).","For the same amount of gas. Special cases: T = const (Boyle), p = const (Charles / Gay-Lussac), V = const (Amontons / Gay-Lussac).","Per la stessa quantità di gas. Casi particolari: T costante (Boyle), p costante (1ª Gay-Lussac), V costante (2ª Gay-Lussac).","Pour la même quantité de gaz. Cas particuliers : T constante (Boyle-Mariotte), p constante (Gay-Lussac), V constant (Charles).","Para la misma cantidad de gas. Casos: T constante (Boyle-Mariotte), p constante (Charles), V constante (Gay-Lussac).","Für dieselbe Gasmenge. Sonderfälle: T konstant (Boyle-Mariotte), p konstant (Gay-Lussac), V konstant (Amontons).","Para a mesma quantidade de gás. Casos: T constante (Boyle), p constante (Charles), V constante (Gay-Lussac).","Для одной и той же массы газа. Частные случаи: T = const (Бойль — Мариотт), p = const (Гей-Люссак), V = const (Шарль).")),
  F(T("Daltonov zakon","Dalton’s law","Legge di Dalton","Loi de Dalton","Ley de Dalton","Daltonsches Gesetz","Lei de Dalton","Закон Дальтона"),
    r"p = p_1 + p_2 + \cdots + p_n",
    T("Pritisak smeše gasova je zbir parcijalnih pritisaka.","The pressure of a gas mixture is the sum of the partial pressures.","La pressione di una miscela è la somma delle pressioni parziali.","La pression d’un mélange est la somme des pressions partielles.","La presión de una mezcla es la suma de las presiones parciales.","Der Druck eines Gasgemischs ist die Summe der Partialdrücke.","A pressão de uma mistura é a soma das pressões parciais.","Давление смеси равно сумме парциальных давлений.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'p': None, 'V': 0.0224, 'm': 0.032, 'M': 0.032, 'R': 8.314462618, 'Tt': K0,
                        'p2': None, 'p1': 101325, 'V1': 0.01, 'T1': K0 + 20, 'V2': 0.005, 'T2': K0 + 60},
                       {'p': 'kPa', 'V': 'L', 'm': 'g' if False else 'kg', 'Tt': '°C', 'p1': 'kPa', 'p2': 'kPa', 'V1': 'L', 'V2': 'L', 'T1': '°C', 'T2': '°C'}),
  'jednacine': [
   {'latex': r"p V = \dfrac{m}{M} R T", 'trazi': 'p', 'promenljive': ['p', 'V', 'm', 'M', 'R', 'Tt'],
    'resenja': {'p': 'm*R*Tt/(M*V)', 'V': 'm*R*Tt/(M*p)', 'm': 'p*V*M/(R*Tt)', 'M': 'm*R*Tt/(p*V)', 'Tt': 'p*V*M/(m*R)'}},
   {'latex': r"\dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}", 'trazi': 'p2',
    'resenja': {'p2': 'p1*V1*T2/(T1*V2)', 'V2': 'p1*V1*T2/(T1*p2)', 'T2': 'p2*V2*T1/(p1*V1)', 'p1': 'p2*V2*T1/(T2*V1)', 'V1': 'p2*V2*T1/(T2*p1)', 'T1': 'p1*V1*T2/(p2*V2)'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['m']['jed'] = 'g'

teme.append({
 'id': 'prvi_zakon', 'simbol': 'ΔU',
 'naziv': T("Prvi zakon termodinamike","First law of thermodynamics","Primo principio della termodinamica","Premier principe de la thermodynamique","Primer principio de la termodinámica","Erster Hauptsatz der Thermodynamik","Primeira lei da termodinâmica","Первый закон термодинамики"),
 'opis': T("Unutrašnja energija, c_p i c_v","Internal energy, c_p and c_v","Energia interna, c_p e c_v","Énergie interne, c_p et c_v","Energía interna, c_p y c_v","Innere Energie, c_p und c_v","Energia interna, c_p e c_v","Внутренняя энергия, c_p и c_v"),
 'kljucne_reci': T("prvi zakon termodinamike unutrasnja energija toplota rad gasa cp cv","first law of thermodynamics internal energy heat work cp cv","primo principio termodinamica energia interna calore lavoro","premier principe thermodynamique energie interne chaleur travail","primer principio termodinamica energia interna calor trabajo","erster hauptsatz innere energie warme arbeit","primeira lei termodinamica energia interna calor trabalho","первое начало термодинамики внутренняя энергия теплота работа"),
 'formule': [
  F(T("Prvi zakon termodinamike","First law","Primo principio","Premier principe","Primer principio","Erster Hauptsatz","Primeira lei","Первый закон"),
    S(r"\Delta U = {A} + Q, \quad {A} = -p\,\Delta V"),
    S(T("Unutrašnja energija gasa raste za dovedenu toplotu Q i za rad {A} koji okolina izvrši nad gasom. Kada se gas širi, {A} je negativan.","The internal energy rises by the heat Q supplied and by the work {A} done on the gas. When the gas expands, {A} is negative.","L’energia interna aumenta del calore Q fornito e del lavoro {A} compiuto sul gas. Se il gas si espande, {A} è negativo.","L’énergie interne augmente de la chaleur Q reçue et du travail {A} reçu par le gaz. Lors d’une détente, {A} est négatif.","La energía interna aumenta con el calor Q recibido y el trabajo {A} realizado sobre el gas. Si el gas se expande, {A} es negativo.","Die innere Energie steigt um die zugeführte Wärme Q und die am Gas verrichtete Arbeit {A}. Dehnt sich das Gas aus, ist {A} negativ.","A energia interna aumenta com o calor Q recebido e o trabalho {A} realizado sobre o gás. Se o gás se expande, {A} é negativo.","Внутренняя энергия растёт на подведённую теплоту Q и работу {A} внешних сил над газом. При расширении газа {A} отрицательна.")['sr'])
    if False else {j: x.replace('{A}', RAD[j].replace('\\', '')) for j, x in T("Unutrašnja energija gasa raste za dovedenu toplotu Q i za rad {A} koji okolina izvrši nad gasom. Kada se gas širi, {A} je negativan.","The internal energy rises by the heat Q supplied and by the work {A} done on the gas. When the gas expands, {A} is negative.","L’energia interna aumenta del calore Q fornito e del lavoro {A} compiuto sul gas. Se il gas si espande, {A} è negativo.","L’énergie interne augmente de la chaleur Q reçue et du travail {A} reçu par le gaz. Lors d’une détente, {A} est négatif.","La energía interna aumenta con el calor Q recibido y el trabajo {A} realizado sobre el gas. Si el gas se expande, {A} es negativo.","Die innere Energie steigt um die zugeführte Wärme Q und die am Gas verrichtete Arbeit {A}. Dehnt sich das Gas aus, ist {A} negativ.","A energia interna aumenta com o calor Q recebido e o trabalho {A} realizado sobre o gás. Se o gás se expande, {A} é negativo.","Внутренняя энергия растёт на подведённую теплоту Q и работу {A} внешних сил над газом. При расширении газа {A} отрицательна.").items()}),
  F(T("Unutrašnja energija i specifične toplote","Internal energy and specific heats","Energia interna e calori specifici","Énergie interne et capacités thermiques","Energía interna y calores específicos","Innere Energie und spezifische Wärmen","Energia interna e calores específicos","Внутренняя энергия и теплоёмкости"),
    r"\Delta U = m\, c_v\, \Delta T, \quad c_p - c_v = \frac{R}{M}, \quad \kappa = \frac{c_p}{c_v}",
    T("Za jednoatomni gas κ = 5/3, za dvoatomni (vazduh) κ = 7/5.","For a monatomic gas κ = 5/3, for a diatomic one (air) κ = 7/5.","Per un gas monoatomico κ = 5/3, per uno biatomico (aria) κ = 7/5.","Pour un gaz monoatomique κ = 5/3, pour un gaz diatomique (air) κ = 7/5.","Para un gas monoatómico κ = 5/3, para uno diatómico (aire) κ = 7/5.","Für ein einatomiges Gas κ = 5/3, für ein zweiatomiges (Luft) κ = 7/5.","Para um gás monoatômico κ = 5/3, para um diatômico (ar) κ = 7/5.","Для одноатомного газа κ = 5/3, для двухатомного (воздух) κ = 7/5.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'dU': None, 'A': -200, 'Qd': 500, 'p': 1e5, 'dV': 0.002, 'm': 0.01, 'cv': 718, 'dT': 50},
                       {'p': 'kPa', 'dV': 'L', 'dT': '°C'}),
  'jednacine': [
   {'latex': S(r"\Delta U = {A} + Q"), 'trazi': 'dU', 'resenja': {'dU': 'A + Qd', 'A': 'dU - Qd', 'Qd': 'dU - A'}},
   {'latex': S(r"{A} = -p \Delta V"), 'trazi': 'A', 'resenja': {'A': '-p*dV', 'p': '-A/dV', 'dV': '-A/p'}},
   {'latex': r"\Delta U = m c_v \Delta T", 'trazi': 'dU', 'resenja': {'dU': 'm*cv*dT', 'm': 'dU/(cv*dT)', 'cv': 'dU/(m*dT)', 'dT': 'dU/(m*cv)'},
    'napomene': {'dU': T("Podrazumevano: vazduh, c_v ≈ 718 J/(kg·K).","Default: air, c_v ≈ 718 J/(kg·K).","Predefinito: aria, c_v ≈ 718 J/(kg·K).","Par défaut : air, c_v ≈ 718 J/(kg·K).","Por defecto: aire, c_v ≈ 718 J/(kg·K).","Voreinstellung: Luft, c_v ≈ 718 J/(kg·K).","Padrão: ar, c_v ≈ 718 J/(kg·K).","По умолчанию: воздух, c_v ≈ 718 Дж/(кг·К).")}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['m']['jed'] = 'g'; v['dV']['naziv'] = T("promena zapremine","change in volume","variazione di volume","variation de volume","variación de volumen","Volumenänderung","variação de volume","изменение объёма")
del v['p']['poz']

teme.append({
 'id': 'adijabata', 'simbol': 'κ',
 'naziv': T("Adijabatski proces","Adiabatic process","Trasformazione adiabatica","Transformation adiabatique","Proceso adiabático","Adiabatische Zustandsänderung","Processo adiabático","Адиабатный процесс"),
 'opis': T("Bez razmene toplote","No heat exchange","Senza scambio di calore","Sans échange de chaleur","Sin intercambio de calor","Ohne Wärmeaustausch","Sem troca de calor","Без теплообмена"),
 'kljucne_reci': T("adijabata adijabatski proces sabijanje sirenje gasa dizel pumpa","adiabatic process compression expansion diesel pump poisson","adiabatica compressione espansione diesel poisson","adiabatique compression detente diesel laplace","adiabatico compresion expansion diesel poisson","adiabatisch kompression expansion diesel poisson","adiabatico compressao expansao diesel poisson","адиабата сжатие расширение газа дизель пуассон"),
 'formule': [
  F(T("Pritisak i zapremina","Pressure and volume","Pressione e volume","Pression et volume","Presión y volumen","Druck und Volumen","Pressão e volume","Давление и объём"),
    r"p_1 V_1^{\kappa} = p_2 V_2^{\kappa}",
    T("Gas ne razmenjuje toplotu sa okolinom (brz proces ili dobra izolacija).","The gas exchanges no heat with its surroundings (fast process or good insulation).","Il gas non scambia calore con l’esterno (processo rapido o buon isolamento).","Le gaz n’échange pas de chaleur avec l’extérieur (processus rapide ou bonne isolation).","El gas no intercambia calor con el exterior (proceso rápido o buen aislamiento).","Das Gas tauscht keine Wärme mit der Umgebung aus (schneller Vorgang oder gute Isolierung).","O gás não troca calor com o exterior (processo rápido ou bom isolamento).","Газ не обменивается теплотой с окружением (быстрый процесс или хорошая изоляция).")),
  F(T("Temperatura i zapremina","Temperature and volume","Temperatura e volume","Température et volume","Temperatura y volumen","Temperatur und Volumen","Temperatura e volume","Температура и объём"),
    r"T_1 V_1^{\kappa - 1} = T_2 V_2^{\kappa - 1}",
    T("Pri sabijanju gas se zagreva (dizel motor, pumpa za bicikl), a pri širenju hladi.","Compression heats the gas (diesel engine, bicycle pump); expansion cools it.","La compressione riscalda il gas (motore diesel, pompa), l’espansione lo raffredda.","La compression échauffe le gaz (moteur diesel, pompe), la détente le refroidit.","La compresión calienta el gas (motor diésel, bomba), la expansión lo enfría.","Beim Verdichten erwärmt sich das Gas (Dieselmotor, Luftpumpe), beim Ausdehnen kühlt es ab.","A compressão aquece o gás (motor diesel, bomba), a expansão o resfria.","При сжатии газ нагревается (дизель, насос), при расширении охлаждается.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'p2': None, 'p1': 101325, 'V1': 0.001, 'V2': 0.0001, 'kapa': 1.4, 'T2': None, 'T1': K0 + 20},
                       {'p1': 'kPa', 'p2': 'kPa', 'V1': 'L', 'V2': 'L', 'T1': '°C', 'T2': '°C'}),
  'jednacine': [
   {'latex': r"p_1 V_1^{\kappa} = p_2 V_2^{\kappa}", 'trazi': 'p2',
    'resenja': {'p2': 'p1*pow(V1/V2, kapa)', 'p1': 'p2*pow(V2/V1, kapa)', 'V2': 'V1*pow(p1/p2, 1/kapa)', 'V1': 'V2*pow(p2/p1, 1/kapa)', 'kapa': 'ln(p2/p1)/ln(V1/V2)'}},
   {'latex': r"T_1 V_1^{\kappa-1} = T_2 V_2^{\kappa-1}", 'trazi': 'T2',
    'resenja': {'T2': 'T1*pow(V1/V2, kapa - 1)', 'T1': 'T2*pow(V2/V1, kapa - 1)', 'V2': 'V1*pow(T1/T2, 1/(kapa - 1))', 'V1': 'V2*pow(T2/T1, 1/(kapa - 1))', 'kapa': '1 + ln(T2/T1)/ln(V1/V2)'},
    'napomene': {'T2': T("Primer: vazduh sabijen 10 puta (kao u dizel motoru).","Example: air compressed 10 times (as in a diesel engine).","Esempio: aria compressa 10 volte (come in un motore diesel).","Exemple : air comprimé 10 fois (comme dans un diesel).","Ejemplo: aire comprimido 10 veces (como en un diésel).","Beispiel: Luft 10-fach verdichtet (wie im Dieselmotor).","Exemplo: ar comprimido 10 vezes (como num diesel).","Пример: воздух сжат в 10 раз (как в дизеле).")}},
  ]}
})

teme.append({
 'id': 'toplotni_motori', 'simbol': 'η',
 'naziv': T("Toplotni motori i Karnoov ciklus","Heat engines and the Carnot cycle","Macchine termiche e ciclo di Carnot","Moteurs thermiques et cycle de Carnot","Máquinas térmicas y ciclo de Carnot","Wärmekraftmaschinen und Carnot-Prozess","Máquinas térmicas e ciclo de Carnot","Тепловые двигатели и цикл Карно"),
 'opis': T("Stepen korisnog dejstva","Efficiency","Rendimento","Rendement","Rendimiento","Wirkungsgrad","Rendimento","КПД"),
 'kljucne_reci': T("toplotni motor karnoov ciklus stepen korisnog dejstva drugi zakon termodinamike","heat engine carnot cycle efficiency second law thermodynamics","macchina termica ciclo di carnot rendimento secondo principio","moteur thermique cycle de carnot rendement second principe","maquina termica ciclo de carnot rendimiento segundo principio","warmekraftmaschine carnot prozess wirkungsgrad zweiter hauptsatz","maquina termica ciclo de carnot rendimento segunda lei","тепловой двигатель цикл карно кпд второй закон термодинамики"),
 'formule': [
  F(T("Stepen korisnog dejstva","Efficiency","Rendimento","Rendement","Rendimiento","Wirkungsgrad","Rendimento","КПД"),
    S(r"\eta = \frac{{A}}{{Q1}} = 1 - \frac{{Q2}}{{Q1}}"),
    T("Motor uzima toplotu od toplijeg tela, deo pretvara u rad, a ostatak predaje hladnijem telu.","The engine takes heat from the hot reservoir, turns part into work and gives the rest to the cold one.","Il motore preleva calore dalla sorgente calda, ne trasforma una parte in lavoro e cede il resto a quella fredda.","Le moteur prend de la chaleur à la source chaude, en transforme une partie en travail et cède le reste à la source froide.","La máquina toma calor del foco caliente, convierte una parte en trabajo y cede el resto al frío.","Die Maschine nimmt Wärme vom warmen Reservoir, wandelt einen Teil in Arbeit um und gibt den Rest ans kalte ab.","A máquina retira calor da fonte quente, transforma parte em trabalho e cede o resto à fria.","Двигатель берёт теплоту у нагревателя, часть превращает в работу, остальное отдаёт холодильнику.")),
  F(T("Karnoov ciklus","Carnot cycle","Ciclo di Carnot","Cycle de Carnot","Ciclo de Carnot","Carnot-Prozess","Ciclo de Carnot","Цикл Карно"),
    S(r"\frac{{Q1}}{{T1}} = \frac{{Q2}}{{T2}}, \quad \eta_C = 1 - \frac{{T2}}{{T1}}"),
    T("Najveći mogući stepen korisnog dejstva između dve temperature (u kelvinima).","The highest possible efficiency between two temperatures (in kelvin).","Il massimo rendimento possibile tra due temperature (in kelvin).","Le rendement maximal possible entre deux températures (en kelvins).","El máximo rendimiento posible entre dos temperaturas (en kelvin).","Der größtmögliche Wirkungsgrad zwischen zwei Temperaturen (in Kelvin).","O máximo rendimento possível entre duas temperaturas (em kelvin).","Наибольший возможный КПД между двумя температурами (в кельвинах).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'eta': None, 'Wr': 300, 'Q1': 1000, 'Q2': 700, 'Tv': K0 + 500, 'Tn': K0 + 20},
                       {'Tv': '°C', 'Tn': '°C', 'Wr': 'J', 'Q1': 'J', 'Q2': 'J'}),
  'jednacine': [
   {'latex': S(r"\eta = \dfrac{{A}}{{Q1}}"), 'trazi': 'eta', 'resenja': {'eta': 'Wr/Q1', 'Wr': 'eta*Q1', 'Q1': 'Wr/eta'}},
   {'latex': S(r"\eta = 1 - \dfrac{{Q2}}{{Q1}}"), 'trazi': 'eta', 'resenja': {'eta': '1 - Q2/Q1', 'Q2': '(1 - eta)*Q1', 'Q1': 'Q2/(1 - eta)'}},
   {'latex': S(r"\eta_C = 1 - \dfrac{{T2}}{{T1}}"), 'trazi': 'eta', 'resenja': {'eta': '1 - Tn/Tv', 'Tn': '(1 - eta)*Tv', 'Tv': 'Tn/(1 - eta)'}},
  ]}
})

teme.append({
 'id': 'provodjenje', 'simbol': 'λ',
 'naziv': T("Provođenje toplote","Heat conduction","Conduzione del calore","Conduction thermique","Conducción del calor","Wärmeleitung","Condução de calor","Теплопроводность"),
 'opis': T("Toplotni gubici kroz zid","Heat loss through a wall","Dispersione attraverso una parete","Pertes à travers un mur","Pérdidas a través de una pared","Wärmeverlust durch eine Wand","Perdas através de uma parede","Потери тепла через стену"),
 'kljucne_reci': T("provodjenje toplote toplotna provodljivost zid izolacija prozor gubici","heat conduction thermal conductivity wall insulation window heat loss","conduzione calore conducibilita parete isolamento finestra","conduction thermique conductivite mur isolation fenetre","conduccion calor conductividad pared aislamiento ventana","warmeleitung warmeleitfahigkeit wand dammung fenster","conducao calor condutividade parede isolamento janela","теплопроводность стена утепление окно потери тепла"),
 'formule': [
  F(T("Furijeov zakon","Fourier’s law","Legge di Fourier","Loi de Fourier","Ley de Fourier","Fouriersches Gesetz","Lei de Fourier","Закон Фурье"),
    S(r"P = \frac{Q}{\Delta t} = {lam}\, S\, \frac{\Delta T}{\Delta x}"),
    T("Toplota koja u sekundi prođe kroz zid površine S i debljine Δx. Staklo ≈ 1, cigla ≈ 0,6, stiropor ≈ 0,035 W/(m·K).","Heat per second through a wall of area S and thickness Δx. Glass ≈ 1, brick ≈ 0.6, polystyrene ≈ 0.035 W/(m·K).","Calore al secondo attraverso una parete di area S e spessore Δx. Vetro ≈ 1, mattone ≈ 0,6, polistirolo ≈ 0,035 W/(m·K).","Chaleur par seconde à travers un mur d’aire S et d’épaisseur Δx. Verre ≈ 1, brique ≈ 0,6, polystyrène ≈ 0,035 W/(m·K).","Calor por segundo a través de una pared de área S y espesor Δx. Vidrio ≈ 1, ladrillo ≈ 0,6, poliestireno ≈ 0,035 W/(m·K).","Wärme pro Sekunde durch eine Wand der Fläche S und Dicke Δx. Glas ≈ 1, Ziegel ≈ 0,6, Styropor ≈ 0,035 W/(m·K).","Calor por segundo através de uma parede de área S e espessura Δx. Vidro ≈ 1, tijolo ≈ 0,6, isopor ≈ 0,035 W/(m·K).","Теплота за секунду через стену площадью S и толщиной Δx. Стекло ≈ 1, кирпич ≈ 0,6, пенопласт ≈ 0,035 Вт/(м·К).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Pt': None, 'lam': 0.6, 'S': 10, 'dT': 20, 'dx': 0.25}, {'dx': 'cm', 'dT': '°C'}),
  'jednacine': [
   {'latex': S(r"P = {lam} S \dfrac{\Delta T}{\Delta x}"), 'trazi': 'Pt',
    'resenja': {'Pt': 'lam*S*dT/dx', 'lam': 'Pt*dx/(S*dT)', 'S': 'Pt*dx/(lam*dT)', 'dT': 'Pt*dx/(lam*S)', 'dx': 'lam*S*dT/Pt'}},
  ]}
})

teme.append({
 'id': 'kineticka_teorija', 'simbol': 'kT',
 'naziv': T("Kinetička teorija gasova","Kinetic theory of gases","Teoria cinetica dei gas","Théorie cinétique des gaz","Teoría cinética de los gases","Kinetische Gastheorie","Teoria cinética dos gases","Молекулярно-кинетическая теория"),
 'opis': T("Molekuli, pritisak, temperatura","Molecules, pressure, temperature","Molecole, pressione, temperatura","Molécules, pression, température","Moléculas, presión, temperatura","Moleküle, Druck, Temperatur","Moléculas, pressão, temperatura","Молекулы, давление, температура"),
 'kljucne_reci': T("kineticka teorija gasova molekuli brzina molekula srednja kineticka energija bolcmanova konstanta","kinetic theory gases molecules molecular speed rms mean kinetic energy boltzmann","teoria cinetica molecole velocita quadratica media boltzmann","theorie cinetique molecules vitesse quadratique boltzmann","teoria cinetica moleculas velocidad cuadratica media boltzmann","kinetische gastheorie molekule geschwindigkeit boltzmann","teoria cinetica moleculas velocidade quadratica media boltzmann","молекулярно кинетическая теория молекулы скорость средняя кинетическая энергия больцман"),
 'formule': [
  F(T("Pritisak i temperatura","Pressure and temperature","Pressione e temperatura","Pression et température","Presión y temperatura","Druck und Temperatur","Pressão e temperatura","Давление и температура"),
    r"p = n k T, \quad n = \frac{N}{V}, \quad k = \frac{R}{N_A}",
    T("n je broj molekula u jedinici zapremine; k = 1,38 · 10⁻²³ J/K.","n is the number of molecules per unit volume; k = 1.38 · 10⁻²³ J/K.","n è il numero di molecole per unità di volume; k = 1,38 · 10⁻²³ J/K.","n est le nombre de molécules par unité de volume ; k = 1,38 · 10⁻²³ J/K.","n es el número de moléculas por unidad de volumen; k = 1,38 · 10⁻²³ J/K.","n ist die Teilchenzahl pro Volumen; k = 1,38 · 10⁻²³ J/K.","n é o número de moléculas por unidade de volume; k = 1,38 · 10⁻²³ J/K.","n — число молекул в единице объёма; k = 1,38 · 10⁻²³ Дж/К.")),
  F(T("Pritisak i brzina molekula","Pressure and molecular speed","Pressione e velocità molecolare","Pression et vitesse moléculaire","Presión y velocidad molecular","Druck und Molekülgeschwindigkeit","Pressão e velocidade molecular","Давление и скорость молекул"),
    r"p = \frac{1}{3} n m_1 \overline{v^2} = \frac{1}{3} \rho\, \overline{v^2}",
    T("m₁ je masa jednog molekula, a ρ gustina gasa.","m₁ is the mass of one molecule and ρ the gas density.","m₁ è la massa di una molecola e ρ la densità del gas.","m₁ est la masse d’une molécule et ρ la masse volumique du gaz.","m₁ es la masa de una molécula y ρ la densidad del gas.","m₁ ist die Masse eines Moleküls, ρ die Gasdichte.","m₁ é a massa de uma molécula e ρ a massa específica do gás.","m₁ — масса одной молекулы, ρ — плотность газа.")),
  F(T("Energija i brzina molekula","Energy and speed of molecules","Energia e velocità delle molecole","Énergie et vitesse des molécules","Energía y velocidad de las moléculas","Energie und Geschwindigkeit der Moleküle","Energia e velocidade das moléculas","Энергия и скорость молекул"),
    LJ(lambda j: (r"\overline{E}_{\text{к}}" if j == 'ru' else r"\overline{E}_k") + r" = \frac{3}{2} k T, \quad v_{\mathrm{rms}} = \sqrt{\frac{3 R T}{M}}"),
    T("Srednja kinetička energija zavisi samo od temperature. Molekuli vazduha na sobnoj temperaturi imaju oko 500 m/s.","Mean kinetic energy depends only on temperature. Air molecules at room temperature move at about 500 m/s.","L’energia cinetica media dipende solo dalla temperatura. Le molecole d’aria a temperatura ambiente vanno a circa 500 m/s.","L’énergie cinétique moyenne ne dépend que de la température. Les molécules d’air vont à environ 500 m/s.","La energía cinética media depende solo de la temperatura. Las moléculas del aire van a unos 500 m/s.","Die mittlere kinetische Energie hängt nur von der Temperatur ab. Luftmoleküle haben etwa 500 m/s.","A energia cinética média depende só da temperatura. As moléculas do ar têm cerca de 500 m/s.","Средняя кинетическая энергия зависит только от температуры. Молекулы воздуха движутся со скоростью около 500 м/с.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ek': None, 'k': 1.380649e-23, 'Tt': K0 + 20, 'v': None, 'R': 8.314462618, 'M': 0.029, 'p': None, 'n': 2.5e25},
                       {'Tt': '°C', 'p': 'kPa'}),
  'jednacine': [
   {'latex': LJ(lambda j: (r"\overline{E}_{\text{к}}" if j == 'ru' else r"\overline{E}_k") + r" = \dfrac{3}{2} k T"), 'trazi': 'Ek', 'promenljive': ['Ek', 'k', 'Tt'],
    'resenja': {'Ek': '1.5*k*Tt', 'Tt': 'Ek/(1.5*k)'}},
   {'latex': r"v_{\mathrm{rms}} = \sqrt{\dfrac{3 R T}{M}}", 'trazi': 'v', 'promenljive': ['v', 'R', 'Tt', 'M'],
    'resenja': {'v': 'sqrt(3*R*Tt/M)', 'Tt': 'v*v*M/(3*R)', 'M': '3*R*Tt/(v*v)'}},
   {'latex': r"p = n k T", 'trazi': 'p', 'promenljive': ['p', 'n', 'k', 'Tt'],
    'resenja': {'p': 'n*k*Tt', 'n': 'p/(k*Tt)', 'Tt': 'p/(n*k)'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['M']['naziv'] = T("molarna masa gasa","molar mass of the gas","massa molare del gas","masse molaire du gaz","masa molar del gas","molare Masse des Gases","massa molar do gás","молярная масса газа")

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)
    tekstovi = [t['opis']] + [f.get('objasnjenje') for f in t['formule']]
    for j in t['kalkulator']['jednacine']:
        tekstovi += list((j.get('napomene') or {}).values())
    for o in tekstovi:
        if isinstance(o, dict):
            for jj in J: o[jj] = o[jj].replace('c_p', 'cₚ').replace('c_v', 'cᵥ')

out = {'oblast': 'toplota', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
