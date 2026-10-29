# Generiše assets/oblasti/elektricitet.json za Formulix
import json, math, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))
def LJ(f):
    v = {j: f(j) for j in J}
    return v if len(set(v.values())) > 1 else v['sr']

RAD = dict(sr='A', en='W', it='L', fr='W', es='W', de='W', pt='W', ru='A')
POT = dict(sr=r'\varphi', en='V', it='V', fr='V', es='V', de=r'\varphi', pt='V', ru=r'\varphi')
def S(f):
    return LJ(lambda j: f.replace('{A}', RAD[j]).replace('{V}', POT[j]))
E0 = 8.8541878188e-12

N = {
 'I': T("jačina struje","current","intensità di corrente","intensité du courant","intensidad de corriente","Stromstärke","corrente elétrica","сила тока"),
 'q': T("naelektrisanje","charge","carica","charge","carga","Ladung","carga","заряд"),
 't': T("vreme","time","tempo","temps","tiempo","Zeit","tempo","время"),
 'U': T("napon","voltage","tensione","tension","tensión","Spannung","tensão","напряжение"),
 'R': T("otpor","resistance","resistenza","résistance","resistencia","Widerstand","resistência","сопротивление"),
 'rho': T("specifični otpor","resistivity","resistività","résistivité","resistividad","spezifischer Widerstand","resistividade","удельное сопротивление"),
 'l': T("dužina provodnika","length of the conductor","lunghezza del conduttore","longueur du conducteur","longitud del conductor","Leiterlänge","comprimento do condutor","длина проводника"),
 'S': T("površina preseka","cross-sectional area","sezione","section","sección","Querschnitt","área da seção","площадь сечения"),
 'R0': T("otpor na početnoj temperaturi","resistance at the initial temperature","resistenza alla temperatura iniziale","résistance à la température initiale","resistencia a la temperatura inicial","Widerstand bei Anfangstemperatur","resistência na temperatura inicial","сопротивление при начальной температуре"),
 'RT': T("otpor na novoj temperaturi","resistance at the new temperature","resistenza alla nuova temperatura","résistance à la nouvelle température","resistencia a la nueva temperatura","Widerstand bei neuer Temperatur","resistência na nova temperatura","сопротивление при новой температуре"),
 'alfa': T("temperaturni koeficijent otpora","temperature coefficient of resistance","coefficiente di temperatura","coefficient de température","coeficiente de temperatura","Temperaturkoeffizient","coeficiente de temperatura","температурный коэффициент сопротивления"),
 'dT': T("promena temperature","change in temperature","variazione di temperatura","variation de température","variación de temperatura","Temperaturänderung","variação de temperatura","изменение температуры"),
 'Ru': T("ukupni (ekvivalentni) otpor","total (equivalent) resistance","resistenza equivalente","résistance équivalente","resistencia equivalente","Ersatzwiderstand","resistência equivalente","общее сопротивление"),
 'R1': T("prvi otpornik","resistor 1","resistore 1","résistance 1","resistencia 1","Widerstand 1","resistor 1","первый резистор"),
 'R2': T("drugi otpornik","resistor 2","resistore 2","résistance 2","resistencia 2","Widerstand 2","resistor 2","второй резистор"),
 'R3': T("treći otpornik","resistor 3","resistore 3","résistance 3","resistencia 3","Widerstand 3","resistor 3","третий резистор"),
 'P': T("snaga","power","potenza","puissance","potencia","Leistung","potência","мощность"),
 'A': T("električni rad (utrošena energija)","electrical energy used","energia elettrica consumata","énergie électrique consommée","energía eléctrica consumida","elektrische Arbeit (Energie)","energia elétrica consumida","работа тока (израсходованная энергия)"),
 'U0': T("amplituda (vršna vrednost) napona","peak voltage","tensione di picco","tension crête","tensión de pico","Scheitelspannung","tensão de pico","амплитуда напряжения"),
 'Uef': T("efektivni napon","rms voltage","tensione efficace","tension efficace","tensión eficaz","Effektivspannung","tensão eficaz","действующее напряжение"),
 'I0': T("amplituda struje","peak current","corrente di picco","courant crête","corriente de pico","Scheitelstrom","corrente de pico","амплитуда тока"),
 'Ief': T("efektivna struja","rms current","corrente efficace","courant efficace","corriente eficaz","Effektivstrom","corrente eficaz","действующее значение тока"),
 'Psr': T("srednja snaga","average power","potenza media","puissance moyenne","potencia media","mittlere Leistung","potência média","средняя мощность"),
 'F': T("električna sila","electric force","forza elettrica","force électrique","fuerza eléctrica","elektrische Kraft","força elétrica","электрическая сила"),
 'q1': T("prvo naelektrisanje","charge 1","carica 1","charge 1","carga 1","Ladung 1","carga 1","первый заряд"),
 'q2': T("drugo naelektrisanje","charge 2","carica 2","charge 2","carga 2","Ladung 2","carga 2","второй заряд"),
 'r': T("rastojanje","distance","distanza","distance","distancia","Abstand","distância","расстояние"),
 'e0': T("električna konstanta","electric constant","costante dielettrica del vuoto","permittivité du vide","permitividad del vacío","elektrische Feldkonstante","permissividade do vácuo","электрическая постоянная"),
 'E': T("jačina električnog polja","electric field strength","intensità del campo elettrico","champ électrique","intensidad del campo eléctrico","elektrische Feldstärke","intensidade do campo elétrico","напряжённость электрического поля"),
 'V': T("potencijal","potential","potenziale","potentiel","potencial","Potential","potencial","потенциал"),
 'W': T("rad električnog polja","work of the electric field","lavoro del campo elettrico","travail du champ électrique","trabajo del campo eléctrico","Arbeit des elektrischen Feldes","trabalho do campo elétrico","работа электрического поля"),
 'd': T("rastojanje između ploča","plate separation","distanza tra le armature","distance entre les armatures","distancia entre placas","Plattenabstand","distância entre as placas","расстояние между пластинами"),
 'C': T("kapacitet","capacitance","capacità","capacité","capacidad","Kapazität","capacitância","электроёмкость"),
 'er': T("relativna dielektrična konstanta","relative permittivity","costante dielettrica relativa","permittivité relative","permitividad relativa","Dielektrizitätszahl","permissividade relativa","диэлектрическая проницаемость"),
 'Sp': T("površina ploče","plate area","area delle armature","aire des armatures","área de las placas","Plattenfläche","área das placas","площадь пластины"),
 'WC': T("energija kondenzatora","energy of the capacitor","energia del condensatore","énergie du condensateur","energía del condensador","Energie des Kondensators","energia do capacitor","энергия конденсатора"),
 'Cu': T("ukupni kapacitet","total capacitance","capacità equivalente","capacité équivalente","capacidad equivalente","Gesamtkapazität","capacitância equivalente","общая ёмкость"),
 'C1': T("prvi kondenzator","capacitor 1","condensatore 1","condensateur 1","condensador 1","Kondensator 1","capacitor 1","первый конденсатор"),
 'C2': T("drugi kondenzator","capacitor 2","condensatore 2","condensateur 2","condensador 2","Kondensator 2","capacitor 2","второй конденсатор"),
}
OZ = {'I': 'I', 'q': 'q', 't': 't', 'U': 'U', 'R': 'R', 'rho': r'\rho', 'l': 'l', 'S': 'S', 'R0': 'R_0', 'RT': 'R', 'alfa': r'\alpha',
      'dT': r'\Delta T', 'Ru': 'R', 'R1': 'R_1', 'R2': 'R_2', 'R3': 'R_3', 'P': 'P', 'A': S('{A}'), 'U0': 'U_0',
      'Uef': r'U_{\mathrm{ef}}', 'I0': 'I_0', 'Ief': r'I_{\mathrm{ef}}', 'Psr': r'\bar P', 'F': 'F', 'q1': 'q_1', 'q2': 'q_2',
      'r': 'r', 'e0': r'\varepsilon_0', 'E': 'E', 'V': S('{V}'), 'W': S('{A}'), 'd': 'd', 'C': 'C', 'er': r'\varepsilon_r',
      'Sp': 'S', 'WC': 'W', 'Cu': 'C', 'C1': 'C_1', 'C2': 'C_2'}
EF = dict(sr='ef', en='rms', it='eff', fr='eff', es='ef', de='eff', pt='ef', ru='д')
OZ['Uef'] = LJ(lambda j: r'U_{\text{%s}}' % EF[j]); OZ['Ief'] = LJ(lambda j: r'I_{\text{%s}}' % EF[j])
VRSTA = {'I': 'struja', 'q': 'naboj', 't': 'vreme', 'U': 'napon', 'R': 'otpor', 'rho': 'specOtpor', 'l': 'duzina', 'S': 'povrsina',
         'R0': 'otpor', 'RT': 'otpor', 'alfa': 'tempKoef', 'dT': 'tempRazlika', 'Ru': 'otpor', 'R1': 'otpor', 'R2': 'otpor',
         'R3': 'otpor', 'P': 'snaga', 'A': 'energija', 'U0': 'napon', 'Uef': 'napon', 'I0': 'struja', 'Ief': 'struja',
         'Psr': 'snaga', 'F': 'sila', 'q1': 'naboj', 'q2': 'naboj', 'r': 'duzina', 'e0': 'permitivnost', 'E': 'elPolje',
         'V': 'napon', 'W': 'energija', 'd': 'duzina', 'C': 'kapacitet', 'er': 'bez', 'Sp': 'povrsina', 'WC': 'energija',
         'Cu': 'kapacitet', 'C1': 'kapacitet', 'C2': 'kapacitet'}
POZ = {'t', 'R', 'rho', 'l', 'S', 'R0', 'RT', 'Ru', 'R1', 'R2', 'R3', 'r', 'e0', 'd', 'C', 'er', 'Sp', 'Cu', 'C1', 'C2', 'U0', 'Uef', 'I0', 'Ief'}
NENEG = {'WC', 'P', 'Psr'}

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

def crtez_veze():
    """Redna i paralelna veza dva otpornika."""
    def otpornik(x, y, oz):
        return f'<rect class="lik" x="{x}" y="{y-9}" width="44" height="18" rx="3"/><text x="{x+14}" y="{y-16}">R<tspan class="sub" dy="5">{oz}</tspan></text>'
    s = '<svg viewBox="0 0 320 170" xmlns="http://www.w3.org/2000/svg" role="img">'
    # redna
    s += '<line class="ivica" x1="14" y1="44" x2="54" y2="44"/>' + otpornik(54, 44, '1')
    s += '<line class="ivica" x1="98" y1="44" x2="118" y2="44"/>' + otpornik(118, 44, '2') + '<line class="ivica" x1="162" y1="44" x2="196" y2="44"/>'
    s += '<circle class="tac" cx="14" cy="44" r="4"/><circle class="tac" cx="196" cy="44" r="4"/>'
    s += '<text class="fun" x="210" y="50">R₁ + R₂</text>'
    # paralelna
    s += '<path class="ivica" d="M14,124 L54,124 M54,100 L54,148 M54,100 L74,100 M118,100 L138,100 M54,148 L74,148 M118,148 L138,148 M138,100 L138,148 M138,124 L178,124"/>'
    s += otpornik(74, 100, '1') + otpornik(74, 148, '2')
    s += '<circle class="tac" cx="14" cy="124" r="4"/><circle class="tac" cx="178" cy="124" r="4"/>'
    s += '<text class="fun" x="196" y="130">R₁R₂ / (R₁ + R₂)</text>'
    s += '</svg>'
    return s

def crtez_kondenzator():
    s = '<svg viewBox="0 0 300 170" xmlns="http://www.w3.org/2000/svg" role="img">'
    s += '<rect class="lik" x="90" y="20" width="10" height="120"/><rect class="lik" x="200" y="20" width="10" height="120"/>'
    for y in (36, 60, 84, 108, 128):
        s += f'<line class="pom" x1="102" y1="{y}" x2="196" y2="{y}"/><path class="tac" d="M198,{y} l-8,-4 v8 Z"/>'
    s += '<text class="fun" x="72" y="84">+q</text><text class="fun" x="216" y="84">−q</text>'
    s += '<line class="osa" x1="95" y1="156" x2="205" y2="156"/><line class="osa" x1="95" y1="150" x2="95" y2="162"/><line class="osa" x1="205" y1="150" x2="205" y2="162"/>'
    s += '<text x="146" y="152">d</text><text x="142" y="16">E</text>'
    s += '</svg>'
    return s

teme = []

teme.append({
 'id': 'omov_zakon', 'simbol': 'I',
 'naziv': T("Struja i Omov zakon","Current and Ohm’s law","Corrente e legge di Ohm","Courant et loi d’Ohm","Corriente y ley de Ohm","Strom und ohmsches Gesetz","Corrente e lei de Ohm","Ток и закон Ома"),
 'opis': T("I = q/t, I = U/R","I = q/t, I = U/R","I = q/t, I = U/R","I = q/t, I = U/R","I = q/t, I = U/R","I = Q/t, I = U/R","I = q/t, I = U/R","I = q/t, I = U/R"),
 'kljucne_reci': T("elektricna struja jacina struje omov zakon napon otpor amper volt om","electric current ohm law voltage resistance ampere volt ohm","corrente elettrica legge di ohm tensione resistenza ampere volt","courant electrique loi d ohm tension resistance ampere volt","corriente electrica ley de ohm tension resistencia amperio voltio","elektrischer strom ohmsches gesetz spannung widerstand ampere volt","corrente eletrica lei de ohm tensao resistencia ampere volt","электрический ток закон ома напряжение сопротивление ампер вольт"),
 'formule': [
  F(T("Jačina struje","Electric current","Intensità di corrente","Intensité du courant","Intensidad de corriente","Stromstärke","Corrente elétrica","Сила тока"),
    r"I = \frac{\Delta q}{\Delta t}",
    T("Naelektrisanje koje u sekundi prođe kroz presek provodnika; 1 A = 1 C/s.","Charge passing through a cross-section per second; 1 A = 1 C/s.","Carica che attraversa una sezione al secondo; 1 A = 1 C/s.","Charge traversant une section par seconde ; 1 A = 1 C/s.","Carga que atraviesa una sección por segundo; 1 A = 1 C/s.","Ladung, die pro Sekunde durch einen Querschnitt fließt; 1 A = 1 C/s.","Carga que atravessa uma seção por segundo; 1 A = 1 C/s.","Заряд, проходящий через сечение за секунду; 1 А = 1 Кл/с.")),
  F(T("Omov zakon","Ohm’s law","Legge di Ohm","Loi d’Ohm","Ley de Ohm","Ohmsches Gesetz","Lei de Ohm","Закон Ома"),
    r"I = \frac{U}{R}",
    T("Struja kroz provodnik srazmerna je naponu na njegovim krajevima; 1 Ω = 1 V/A.","Current through a conductor is proportional to the voltage across it; 1 Ω = 1 V/A.","La corrente è proporzionale alla tensione ai capi del conduttore; 1 Ω = 1 V/A.","Le courant est proportionnel à la tension aux bornes ; 1 Ω = 1 V/A.","La corriente es proporcional a la tensión en los extremos; 1 Ω = 1 V/A.","Der Strom ist proportional zur anliegenden Spannung; 1 Ω = 1 V/A.","A corrente é proporcional à tensão nos terminais; 1 Ω = 1 V/A.","Сила тока пропорциональна напряжению; 1 Ом = 1 В/А.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'I': None, 'q': 10, 't': 5, 'U': 230, 'R': 1000}, {'I': 'A', 'R': 'kΩ'}),
  'jednacine': [
   {'latex': r"I = \dfrac{U}{R}", 'trazi': 'I', 'resenja': {'I': 'U/R', 'U': 'I*R', 'R': 'U/I'}},
   {'latex': r"I = \dfrac{q}{t}", 'trazi': 'I', 'resenja': {'I': 'q/t', 'q': 'I*t', 't': 'q/I'}},
  ]}
})

teme.append({
 'id': 'otpor', 'simbol': 'R',
 'naziv': T("Otpor provodnika","Resistance of a conductor","Resistenza di un conduttore","Résistance d’un conducteur","Resistencia de un conductor","Widerstand eines Leiters","Resistência de um condutor","Сопротивление проводника"),
 'opis': T("Specifični otpor, temperatura","Resistivity, temperature","Resistività, temperatura","Résistivité, température","Resistividad, temperatura","Spezifischer Widerstand, Temperatur","Resistividade, temperatura","Удельное сопротивление, температура"),
 'kljucne_reci': T("otpor provodnika specificni otpor zica bakar temperaturni koeficijent","resistance resistivity wire copper temperature coefficient","resistenza resistivita filo rame coefficiente di temperatura","resistance resistivite fil cuivre coefficient de temperature","resistencia resistividad cable cobre coeficiente de temperatura","widerstand spezifischer widerstand draht kupfer temperaturkoeffizient","resistencia resistividade fio cobre coeficiente de temperatura","сопротивление удельное провод медь температурный коэффициент"),
 'formule': [
  F(T("Otpor žice","Resistance of a wire","Resistenza di un filo","Résistance d’un fil","Resistencia de un cable","Widerstand eines Drahtes","Resistência de um fio","Сопротивление провода"),
    r"R = \rho\,\frac{l}{S}",
    T("Bakar: ρ ≈ 0,017 Ω·mm²/m, aluminijum ≈ 0,028 Ω·mm²/m.","Copper: ρ ≈ 0.017 Ω·mm²/m, aluminium ≈ 0.028 Ω·mm²/m.","Rame: ρ ≈ 0,017 Ω·mm²/m, alluminio ≈ 0,028 Ω·mm²/m.","Cuivre : ρ ≈ 0,017 Ω·mm²/m, aluminium ≈ 0,028 Ω·mm²/m.","Cobre: ρ ≈ 0,017 Ω·mm²/m, aluminio ≈ 0,028 Ω·mm²/m.","Kupfer: ρ ≈ 0,017 Ω·mm²/m, Aluminium ≈ 0,028 Ω·mm²/m.","Cobre: ρ ≈ 0,017 Ω·mm²/m, alumínio ≈ 0,028 Ω·mm²/m.","Медь: ρ ≈ 0,017 Ом·мм²/м, алюминий ≈ 0,028 Ом·мм²/м.")),
  F(T("Zavisnost od temperature","Temperature dependence","Dipendenza dalla temperatura","Variation avec la température","Dependencia de la temperatura","Temperaturabhängigkeit","Dependência da temperatura","Зависимость от температуры"),
    r"\Delta R = \alpha\, R\, \Delta T, \quad R = R_0\,(1 + \alpha\,\Delta T)",
    T("Kod metala otpor raste sa temperaturom; za bakar α ≈ 0,0039 K⁻¹.","For metals resistance rises with temperature; for copper α ≈ 0.0039 K⁻¹.","Nei metalli la resistenza aumenta con la temperatura; rame α ≈ 0,0039 K⁻¹.","Pour les métaux la résistance augmente avec la température ; cuivre α ≈ 0,0039 K⁻¹.","En los metales la resistencia aumenta con la temperatura; cobre α ≈ 0,0039 K⁻¹.","Bei Metallen steigt der Widerstand mit der Temperatur; Kupfer α ≈ 0,0039 K⁻¹.","Nos metais a resistência aumenta com a temperatura; cobre α ≈ 0,0039 K⁻¹.","У металлов сопротивление растёт с температурой; медь α ≈ 0,0039 К⁻¹.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'R': None, 'rho': 1.7e-8, 'l': 100, 'S': 1.5e-6, 'RT': None, 'R0': 10, 'alfa': 0.0039, 'dT': 80},
                       {'rho': 'Ω·mm²/m', 'S': 'mm²', 'dT': '°C'}),
  'jednacine': [
   {'latex': r"R = \rho \dfrac{l}{S}", 'trazi': 'R', 'resenja': {'R': 'rho*l/S', 'rho': 'R*S/l', 'l': 'R*S/rho', 'S': 'rho*l/R'}},
   {'latex': r"R = R_0 (1 + \alpha \Delta T)", 'trazi': 'RT', 'resenja': {'RT': 'R0*(1 + alfa*dT)', 'R0': 'RT/(1 + alfa*dT)', 'alfa': '(RT/R0 - 1)/dT', 'dT': '(RT/R0 - 1)/alfa'}},
  ]}
})

teme.append({
 'id': 'veze_otpornika', 'simbol': 'Ω',
 'naziv': T("Redna i paralelna veza","Series and parallel","Serie e parallelo","Série et parallèle","Serie y paralelo","Reihen- und Parallelschaltung","Série e paralelo","Последовательное и параллельное соединение"),
 'opis': T("Ukupni otpor","Equivalent resistance","Resistenza equivalente","Résistance équivalente","Resistencia equivalente","Ersatzwiderstand","Resistência equivalente","Общее сопротивление"),
 'kljucne_reci': T("redna veza paralelna veza otpornici ukupni otpor ekvivalentni","series parallel resistors equivalent resistance","resistori in serie in parallelo resistenza equivalente","resistances en serie en parallele resistance equivalente","resistencias en serie en paralelo resistencia equivalente","reihenschaltung parallelschaltung widerstande ersatzwiderstand","resistores em serie em paralelo resistencia equivalente","последовательное параллельное соединение резисторов общее сопротивление"),
 'crtez': crtez_veze(),
 'formule': [
  F(T("Redna veza","Series connection","Collegamento in serie","Montage en série","Conexión en serie","Reihenschaltung","Ligação em série","Последовательное соединение"),
    r"R = R_1 + R_2 + \cdots",
    T("Kroz sve otpornike teče ista struja; naponi se sabiraju.","The same current flows through all resistors; the voltages add up.","La stessa corrente attraversa tutti i resistori; le tensioni si sommano.","Le même courant traverse toutes les résistances ; les tensions s’additionnent.","La misma corriente pasa por todas; las tensiones se suman.","Durch alle Widerstände fließt derselbe Strom; die Spannungen addieren sich.","A mesma corrente passa por todos; as tensões se somam.","Через все резисторы течёт один ток; напряжения складываются.")),
  F(T("Paralelna veza","Parallel connection","Collegamento in parallelo","Montage en parallèle","Conexión en paralelo","Parallelschaltung","Ligação em paralelo","Параллельное соединение"),
    r"\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots",
    T("Na svim otpornicima je isti napon; struje se sabiraju. Ukupni otpor je manji od najmanjeg.","All resistors have the same voltage; the currents add up. The total is smaller than the smallest resistor.","Tutti i resistori hanno la stessa tensione; le correnti si sommano. Il totale è minore del resistore più piccolo.","Toutes les résistances ont la même tension ; les courants s’additionnent. Le total est inférieur à la plus petite.","Todas tienen la misma tensión; las corrientes se suman. El total es menor que la menor.","Alle haben dieselbe Spannung; die Ströme addieren sich. Der Gesamtwert ist kleiner als der kleinste Widerstand.","Todos têm a mesma tensão; as correntes se somam. O total é menor que o menor resistor.","Напряжение на всех одинаково; токи складываются. Общее сопротивление меньше наименьшего.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Ru': None, 'R1': 100, 'R2': 220, 'R3': 330}),
  'jednacine': [
   {'latex': r"R = R_1 + R_2", 'trazi': 'Ru', 'resenja': {'Ru': 'R1 + R2', 'R1': 'Ru - R2', 'R2': 'Ru - R1'}},
   {'latex': r"R = R_1 + R_2 + R_3", 'trazi': 'Ru', 'resenja': {'Ru': 'R1 + R2 + R3', 'R1': 'Ru - R2 - R3', 'R2': 'Ru - R1 - R3', 'R3': 'Ru - R1 - R2'}},
   {'latex': r"\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2}", 'trazi': 'Ru', 'resenja': {'Ru': 'R1*R2/(R1 + R2)', 'R1': '1/(1/Ru - 1/R2)', 'R2': '1/(1/Ru - 1/R1)'}},
   {'latex': r"\dfrac{1}{R} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3}", 'trazi': 'Ru',
    'resenja': {'Ru': '1/(1/R1 + 1/R2 + 1/R3)', 'R1': '1/(1/Ru - 1/R2 - 1/R3)', 'R2': '1/(1/Ru - 1/R1 - 1/R3)', 'R3': '1/(1/Ru - 1/R1 - 1/R2)'}},
  ]}
})

teme.append({
 'id': 'snaga_struje', 'simbol': 'P',
 'naziv': T("Rad i snaga struje","Electrical energy and power","Energia e potenza elettrica","Énergie et puissance électriques","Energía y potencia eléctrica","Elektrische Arbeit und Leistung","Energia e potência elétrica","Работа и мощность тока"),
 'opis': T("P = UI, kilovat-sati","P = UI, kilowatt-hours","P = UI, kilowattora","P = UI, kilowattheures","P = UI, kilovatios-hora","P = UI, Kilowattstunden","P = UI, quilowatts-hora","P = UI, киловатт-часы"),
 'kljucne_reci': T("snaga struje rad struje dzulov zakon potrosnja struje kilovat sat racun za struju","electric power electrical energy joule heating consumption kilowatt hour electricity bill","potenza elettrica energia effetto joule consumo kilowattora bolletta","puissance electrique energie effet joule consommation kilowattheure facture","potencia electrica energia efecto joule consumo kilovatio hora factura","elektrische leistung arbeit joulesche warme verbrauch kilowattstunde stromrechnung","potencia eletrica energia efeito joule consumo quilowatt hora conta de luz","мощность тока работа тока закон джоуля ленца расход киловатт час"),
 'formule': [
  F(T("Snaga","Power","Potenza","Puissance","Potencia","Leistung","Potência","Мощность"),
    r"P = U I = R I^2 = \frac{U^2}{R}",
    T("Druga dva oblika slede iz Omovog zakona; RI² je toplota koja se oslobađa u otporniku (Džulov zakon).","The other two forms follow from Ohm’s law; RI² is the heat released in the resistor (Joule heating).","Le altre due forme seguono dalla legge di Ohm; RI² è il calore dissipato (effetto Joule).","Les deux autres formes découlent de la loi d’Ohm ; RI² est la chaleur dégagée (effet Joule).","Las otras dos formas salen de la ley de Ohm; RI² es el calor disipado (efecto Joule).","Die anderen Formen folgen aus dem ohmschen Gesetz; RI² ist die erzeugte Wärme (Joule).","As outras duas formas vêm da lei de Ohm; RI² é o calor dissipado (efeito Joule).","Две другие формы следуют из закона Ома; RI² — выделяющаяся теплота (закон Джоуля — Ленца).")),
  F(T("Rad struje","Electrical energy","Energia elettrica","Énergie électrique","Energía eléctrica","Elektrische Arbeit","Energia elétrica","Работа тока"),
    S(r"{A} = P\,t = U\,q = U I t"),
    T("Utrošena električna energija; na računu za struju izražava se u kWh (1 kWh = 3,6 MJ).","Electrical energy used; on the electricity bill it is given in kWh (1 kWh = 3.6 MJ).","Energia consumata; in bolletta è in kWh (1 kWh = 3,6 MJ).","Énergie consommée ; sur la facture en kWh (1 kWh = 3,6 MJ).","Energía consumida; en la factura en kWh (1 kWh = 3,6 MJ).","Verbrauchte Energie; auf der Stromrechnung in kWh (1 kWh = 3,6 MJ).","Energia consumida; na conta de luz em kWh (1 kWh = 3,6 MJ).","Израсходованная энергия; в счёте — в кВт·ч (1 кВт·ч = 3,6 МДж).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'P': None, 'U': 230, 'I': 10, 'R': 23, 'A': None, 't': 3600}, {'A': 'kWh', 't': 'h', 'P': 'kW'}),
  'jednacine': [
   {'latex': r"P = U I", 'trazi': 'P', 'resenja': {'P': 'U*I', 'U': 'P/I', 'I': 'P/U'}},
   {'latex': r"P = R I^2", 'trazi': 'P', 'resenja': {'P': 'R*I*I', 'R': 'P/(I*I)', 'I': 'sqrt(P/R)'}},
   {'latex': r"P = \dfrac{U^2}{R}", 'trazi': 'P', 'resenja': {'P': 'U*U/R', 'U': 'sqrt(P*R)', 'R': 'U*U/P'}},
   {'latex': S(r"{A} = P t"), 'trazi': 'A', 'resenja': {'A': 'P*t', 'P': 'A/t', 't': 'A/P'}},
  ]}
})

teme.append({
 'id': 'naizmenicna', 'simbol': '~',
 'naziv': T("Naizmenična struja","Alternating current","Corrente alternata","Courant alternatif","Corriente alterna","Wechselstrom","Corrente alternada","Переменный ток"),
 'opis': T("Efektivne vrednosti","RMS values","Valori efficaci","Valeurs efficaces","Valores eficaces","Effektivwerte","Valores eficazes","Действующие значения"),
 'kljucne_reci': T("naizmenicna struja efektivni napon vrsna vrednost amplituda 230 V mreza","alternating current ac rms voltage peak amplitude mains 230 V","corrente alternata tensione efficace valore di picco rete","courant alternatif tension efficace valeur crete secteur","corriente alterna tension eficaz valor de pico red","wechselstrom effektivwert scheitelwert netzspannung","corrente alternada tensao eficaz valor de pico rede","переменный ток действующее значение амплитуда сеть 230 В"),
 'formule': [
  F(T("Efektivne vrednosti","RMS values","Valori efficaci","Valeurs efficaces","Valores eficaces","Effektivwerte","Valores eficazes","Действующие значения"),
    LJ(lambda j: r"U_{\text{%s}} = \frac{U_0}{\sqrt{2}}, \quad I_{\text{%s}} = \frac{I_0}{\sqrt{2}}" % (EF[j], EF[j])),
    T("Za sinusni napon. Mreža od 230 V ima vršnu vrednost oko 325 V.","For a sinusoidal voltage. 230 V mains has a peak of about 325 V.","Per una tensione sinusoidale. La rete a 230 V ha un picco di circa 325 V.","Pour une tension sinusoïdale. Le secteur 230 V a une crête d’environ 325 V.","Para una tensión sinusoidal. La red de 230 V tiene un pico de unos 325 V.","Für sinusförmige Spannung. Das 230-V-Netz hat einen Scheitelwert von etwa 325 V.","Para tensão senoidal. A rede de 230 V tem pico de cerca de 325 V.","Для синусоидального напряжения. В сети 230 В амплитуда около 325 В.")),
  F(T("Srednja snaga","Average power","Potenza media","Puissance moyenne","Potencia media","Mittlere Leistung","Potência média","Средняя мощность"),
    LJ(lambda j: r"\bar P = U_{\text{%s}}\, I_{\text{%s}}" % (EF[j], EF[j])),
    T("Za otpornik (bez faznog pomaka).","For a resistor (no phase shift).","Per un resistore (senza sfasamento).","Pour une résistance (sans déphasage).","Para una resistencia (sin desfase).","Für einen ohmschen Widerstand (ohne Phasenverschiebung).","Para um resistor (sem defasagem).","Для активного сопротивления (без сдвига фаз).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'Uef': 230, 'U0': None, 'Ief': None, 'I0': 14.14, 'Psr': None}),
  'jednacine': [
   {'latex': LJ(lambda j: r"U_{\text{%s}} = \dfrac{U_0}{\sqrt{2}}" % EF[j]), 'trazi': 'U0', 'resenja': {'Uef': 'U0/sqrt(2)', 'U0': 'Uef*sqrt(2)'}},
   {'latex': LJ(lambda j: r"I_{\text{%s}} = \dfrac{I_0}{\sqrt{2}}" % EF[j]), 'trazi': 'Ief', 'resenja': {'Ief': 'I0/sqrt(2)', 'I0': 'Ief*sqrt(2)'}},
   {'latex': LJ(lambda j: r"\bar P = U_{\text{%s}} I_{\text{%s}}" % (EF[j], EF[j])), 'trazi': 'Psr', 'resenja': {'Psr': 'Uef*Ief', 'Uef': 'Psr/Ief', 'Ief': 'Psr/Uef'}},
  ]}
})

teme.append({
 'id': 'kulon', 'simbol': 'E',
 'naziv': T("Kulonov zakon i električno polje","Coulomb’s law and electric field","Legge di Coulomb e campo elettrico","Loi de Coulomb et champ électrique","Ley de Coulomb y campo eléctrico","Coulombsches Gesetz und elektrisches Feld","Lei de Coulomb e campo elétrico","Закон Кулона и электрическое поле"),
 'opis': T("Sila između naelektrisanja","Force between charges","Forza tra cariche","Force entre charges","Fuerza entre cargas","Kraft zwischen Ladungen","Força entre cargas","Сила между зарядами"),
 'kljucne_reci': T("kulonov zakon elektricna sila naelektrisanje elektricno polje jacina polja gausov zakon fluks","coulomb law electric force charge electric field strength gauss law flux","legge di coulomb forza elettrica carica campo elettrico gauss flusso","loi de coulomb force electrique charge champ electrique gauss flux","ley de coulomb fuerza electrica carga campo electrico gauss flujo","coulombsches gesetz elektrische kraft ladung elektrisches feld gauss fluss","lei de coulomb forca eletrica carga campo eletrico gauss fluxo","закон кулона электрическая сила заряд напряжённость поля гаусс поток"),
 'formule': [
  F(T("Kulonov zakon","Coulomb’s law","Legge di Coulomb","Loi de Coulomb","Ley de Coulomb","Coulombsches Gesetz","Lei de Coulomb","Закон Кулона"),
    r"F = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}",
    T("Istoimena naelektrisanja se odbijaju, raznoimena privlače; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Like charges repel, unlike charges attract; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Cariche dello stesso segno si respingono, di segno opposto si attraggono; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Des charges de même signe se repoussent, de signes opposés s’attirent ; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Cargas del mismo signo se repelen, de signo opuesto se atraen; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Gleichnamige Ladungen stoßen sich ab, ungleichnamige ziehen sich an; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Cargas de mesmo sinal se repelem, de sinais opostos se atraem; 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C².","Одноимённые заряды отталкиваются, разноимённые притягиваются; 1/(4πε₀) ≈ 9 · 10⁹ Н·м²/Кл².")),
  F(T("Električno polje","Electric field","Campo elettrico","Champ électrique","Campo eléctrico","Elektrisches Feld","Campo elétrico","Электрическое поле"),
    r"\vec F = q\,\vec E, \quad E = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r^2}",
    T("Drugi izraz: polje tačkastog naelektrisanja q na rastojanju r; 1 V/m = 1 N/C.","Second formula: field of a point charge q at distance r; 1 V/m = 1 N/C.","Seconda formula: campo di una carica puntiforme q a distanza r; 1 V/m = 1 N/C.","Seconde formule : champ d’une charge ponctuelle q à la distance r ; 1 V/m = 1 N/C.","Segunda fórmula: campo de una carga puntual q a distancia r; 1 V/m = 1 N/C.","Zweite Formel: Feld einer Punktladung q im Abstand r; 1 V/m = 1 N/C.","Segunda fórmula: campo de uma carga pontual q à distância r; 1 V/m = 1 N/C.","Вторая формула — поле точечного заряда q на расстоянии r; 1 В/м = 1 Н/Кл.")),
  F(T("Gausov zakon","Gauss’s law","Legge di Gauss","Théorème de Gauss","Ley de Gauss","Gaußsches Gesetz","Lei de Gauss","Теорема Гаусса"),
    r"\Phi_e = \varepsilon_0\,\vec E \cdot \vec S = \varepsilon_0 E S \cos\varphi = q",
    T("Električni fluks kroz zatvorenu površ jednak je naelektrisanju unutar nje.","The electric flux through a closed surface equals the enclosed charge.","Il flusso elettrico attraverso una superficie chiusa è uguale alla carica racchiusa.","Le flux électrique à travers une surface fermée est égal à la charge intérieure.","El flujo eléctrico a través de una superficie cerrada es igual a la carga encerrada.","Der elektrische Fluss durch eine geschlossene Fläche ist gleich der eingeschlossenen Ladung.","O fluxo elétrico através de uma superfície fechada é igual à carga interna.","Поток через замкнутую поверхность равен заряду внутри неё.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'F': None, 'q1': 1e-6, 'q2': 2e-6, 'r': 0.1, 'e0': E0, 'E': None, 'q': 1e-9},
                       {'q1': 'µC', 'q2': 'µC', 'q': 'nC', 'r': 'cm', 'E': 'V/m'}),
  'jednacine': [
   {'latex': r"F = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q_1 q_2}{r^2}", 'trazi': 'F', 'promenljive': ['F', 'q1', 'q2', 'r', 'e0'],
    'resenja': {'F': 'q1*q2/(4*PI*e0*r*r)', 'q1': 'F*4*PI*e0*r*r/q2', 'q2': 'F*4*PI*e0*r*r/q1', 'r': 'sqrt(q1*q2/(4*PI*e0*F))'}},
   {'latex': r"E = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q}{r^2}", 'trazi': 'E', 'promenljive': ['E', 'q', 'r', 'e0'],
    'resenja': {'E': 'q/(4*PI*e0*r*r)', 'q': 'E*4*PI*e0*r*r', 'r': 'sqrt(q/(4*PI*e0*E))'}},
   {'latex': r"F = q E", 'trazi': 'F', 'resenja': {'F': 'q*E', 'q': 'F/E', 'E': 'F/q'}},
  ]}
})

teme.append({
 'id': 'potencijal', 'simbol': 'U',
 'naziv': T("Napon i potencijal","Voltage and potential","Tensione e potenziale","Tension et potentiel","Tensión y potencial","Spannung und Potential","Tensão e potencial","Напряжение и потенциал"),
 'opis': T("Rad polja, homogeno polje","Work of the field, uniform field","Lavoro del campo, campo uniforme","Travail du champ, champ uniforme","Trabajo del campo, campo uniforme","Feldarbeit, homogenes Feld","Trabalho do campo, campo uniforme","Работа поля, однородное поле"),
 'kljucne_reci': T("napon potencijal rad elektricnog polja homogeno polje elektronvolt potencijalna energija","voltage potential work electric field uniform field electronvolt potential energy","tensione potenziale lavoro campo uniforme elettronvolt","tension potentiel travail champ uniforme electronvolt","tension potencial trabajo campo uniforme electronvoltio","spannung potential arbeit homogenes feld elektronenvolt","tensao potencial trabalho campo uniforme eletronvolt","напряжение потенциал работа поля однородное поле электронвольт"),
 'formule': [
  F(T("Napon i rad polja","Voltage and work of the field","Tensione e lavoro del campo","Tension et travail du champ","Tensión y trabajo del campo","Spannung und Feldarbeit","Tensão e trabalho do campo","Напряжение и работа поля"),
    S(r"U = \frac{{A}}{q}, \quad {A} = q\,U = \Delta W_{el}"),
    T("Elektron koji pređe napon od 1 V dobije energiju 1 eV = 1,6 · 10⁻¹⁹ J.","An electron crossing 1 V gains 1 eV = 1.6 · 10⁻¹⁹ J.","Un elettrone che attraversa 1 V acquista 1 eV = 1,6 · 10⁻¹⁹ J.","Un électron qui traverse 1 V gagne 1 eV = 1,6 · 10⁻¹⁹ J.","Un electrón que atraviesa 1 V gana 1 eV = 1,6 · 10⁻¹⁹ J.","Ein Elektron, das 1 V durchläuft, gewinnt 1 eV = 1,6 · 10⁻¹⁹ J.","Um elétron que atravessa 1 V ganha 1 eV = 1,6 · 10⁻¹⁹ J.","Электрон, прошедший 1 В, получает 1 эВ = 1,6 · 10⁻¹⁹ Дж.")),
  F(T("Potencijal tačkastog naelektrisanja","Potential of a point charge","Potenziale di una carica puntiforme","Potentiel d’une charge ponctuelle","Potencial de una carga puntual","Potential einer Punktladung","Potencial de uma carga pontual","Потенциал точечного заряда"),
    S(r"{V} = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r}"),
    T("Napon između dve tačke je razlika njihovih potencijala.","The voltage between two points is the difference of their potentials.","La tensione tra due punti è la differenza dei loro potenziali.","La tension entre deux points est la différence de leurs potentiels.","La tensión entre dos puntos es la diferencia de sus potenciales.","Die Spannung zwischen zwei Punkten ist die Differenz ihrer Potentiale.","A tensão entre dois pontos é a diferença dos seus potenciais.","Напряжение между точками — разность их потенциалов.")),
  F(T("Homogeno polje (između ploča)","Uniform field (between plates)","Campo uniforme (tra le armature)","Champ uniforme (entre armatures)","Campo uniforme (entre placas)","Homogenes Feld (zwischen Platten)","Campo uniforme (entre placas)","Однородное поле (между пластинами)"),
    r"E = \frac{U}{d}, \quad E = \frac{\sigma}{\varepsilon_0}, \quad \sigma = \frac{q}{S}",
    T("σ je površinska gustina naelektrisanja na pločama. Jedna velika ploča stvara polje σ/(2ε₀).","σ is the surface charge density on the plates. A single large plate makes a field σ/(2ε₀).","σ è la densità superficiale di carica. Una sola grande lastra crea un campo σ/(2ε₀).","σ est la densité surfacique de charge. Une seule grande plaque crée un champ σ/(2ε₀).","σ es la densidad superficial de carga. Una sola placa grande crea un campo σ/(2ε₀).","σ ist die Flächenladungsdichte. Eine einzelne große Platte erzeugt σ/(2ε₀).","σ é a densidade superficial de carga. Uma única placa grande cria um campo σ/(2ε₀).","σ — поверхностная плотность заряда. Одна большая пластина создаёт поле σ/(2ε₀).")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'W': None, 'q': 1.602176634e-19, 'U': 1000, 'V': None, 'r': 0.1, 'e0': E0, 'E': None, 'd': 0.01},
                       {'W': 'eV', 'd': 'cm', 'r': 'cm', 'E': 'kV/m'}),
  'jednacine': [
   {'latex': S(r"{A} = q U"), 'trazi': 'W', 'resenja': {'W': 'q*U', 'q': 'W/U', 'U': 'W/q'}},
   {'latex': S(r"{V} = \dfrac{1}{4\pi\varepsilon_0} \dfrac{q}{r}"), 'trazi': 'V', 'promenljive': ['V', 'q', 'r', 'e0'],
    'resenja': {'V': 'q/(4*PI*e0*r)', 'q': 'V*4*PI*e0*r', 'r': 'q/(4*PI*e0*V)'}},
   {'latex': r"E = \dfrac{U}{d}", 'trazi': 'E', 'resenja': {'E': 'U/d', 'U': 'E*d', 'd': 'U/E'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']
v['q']['naziv'] = T("naelektrisanje (podrazumevano: elektron)","charge (default: electron)","carica (predefinita: elettrone)","charge (par défaut : électron)","carga (por defecto: electrón)","Ladung (Voreinstellung: Elektron)","carga (padrão: elétron)","заряд (по умолчанию: электрон)")

teme.append({
 'id': 'kondenzator', 'simbol': 'C',
 'naziv': T("Kondenzator","Capacitor","Condensatore","Condensateur","Condensador","Kondensator","Capacitor","Конденсатор"),
 'opis': T("Kapacitet, energija, vezivanje","Capacitance, energy, combinations","Capacità, energia, collegamenti","Capacité, énergie, associations","Capacidad, energía, asociaciones","Kapazität, Energie, Schaltungen","Capacitância, energia, associações","Ёмкость, энергия, соединения"),
 'kljucne_reci': T("kondenzator kapacitet plocasti kondenzator farad energija kondenzatora redna paralelna veza dielektrik","capacitor capacitance parallel plate farad energy series parallel dielectric","condensatore capacita piano farad energia serie parallelo dielettrico","condensateur capacite plan farad energie serie parallele dielectrique","condensador capacidad placas paralelas faradio energia serie paralelo dielectrico","kondensator kapazitat plattenkondensator farad energie reihe parallel dielektrikum","capacitor capacitancia placas paralelas farad energia serie paralelo dieletrico","конденсатор электроёмкость плоский фарад энергия последовательно параллельно диэлектрик"),
 'crtez': crtez_kondenzator(),
 'formule': [
  F(T("Kapacitet","Capacitance","Capacità","Capacité","Capacidad","Kapazität","Capacitância","Электроёмкость"),
    r"q = C\,U",
    T("1 F = 1 C/V; uobičajeni kondenzatori imaju µF, nF i pF.","1 F = 1 C/V; common capacitors are in µF, nF and pF.","1 F = 1 C/V; i condensatori comuni sono in µF, nF e pF.","1 F = 1 C/V ; les condensateurs courants sont en µF, nF et pF.","1 F = 1 C/V; los condensadores comunes están en µF, nF y pF.","1 F = 1 C/V; übliche Kondensatoren haben µF, nF und pF.","1 F = 1 C/V; capacitores comuns têm µF, nF e pF.","1 Ф = 1 Кл/В; обычные конденсаторы — мкФ, нФ и пФ.")),
  F(T("Pločasti kondenzator","Parallel-plate capacitor","Condensatore piano","Condensateur plan","Condensador de placas paralelas","Plattenkondensator","Capacitor de placas paralelas","Плоский конденсатор"),
    r"C = \varepsilon_r\,\varepsilon_0\,\frac{S}{d}, \quad E = \frac{U}{d}",
    T("S je površina ploča, d rastojanje; za vazduh ε_r ≈ 1.","S is the plate area, d the separation; for air ε_r ≈ 1.","S è l’area delle armature, d la distanza; per l’aria ε_r ≈ 1.","S est l’aire des armatures, d leur distance ; pour l’air ε_r ≈ 1.","S es el área de las placas, d la distancia; para el aire ε_r ≈ 1.","S ist die Plattenfläche, d der Abstand; für Luft ε_r ≈ 1.","S é a área das placas, d a distância; para o ar ε_r ≈ 1.","S — площадь пластин, d — расстояние; для воздуха ε ≈ 1.")),
  F(T("Energija","Energy","Energia","Énergie","Energía","Energie","Energia","Энергия"),
    r"W = \frac{C U^2}{2} = \frac{q^2}{2C}, \quad w_e = \frac{\varepsilon_0 E^2}{2}",
    T("w_e je gustina energije električnog polja (energija po jedinici zapremine).","w_e is the energy density of the electric field (energy per unit volume).","w_e è la densità di energia del campo elettrico.","w_e est la densité d’énergie du champ électrique.","w_e es la densidad de energía del campo eléctrico.","w_e ist die Energiedichte des elektrischen Feldes.","w_e é a densidade de energia do campo elétrico.","w_e — объёмная плотность энергии электрического поля.")),
  F(T("Paralelna i redna veza","Parallel and series","Parallelo e serie","Parallèle et série","Paralelo y serie","Parallel- und Reihenschaltung","Paralelo e série","Параллельное и последовательное соединение"),
    r"C = C_1 + C_2 + \cdots, \quad \frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots",
    T("Obrnuto nego kod otpornika: paralelno se kapaciteti sabiraju.","Opposite of resistors: in parallel the capacitances add.","Al contrario dei resistori: in parallelo le capacità si sommano.","À l’inverse des résistances : en parallèle les capacités s’additionnent.","Al revés que las resistencias: en paralelo las capacidades se suman.","Umgekehrt wie bei Widerständen: parallel addieren sich die Kapazitäten.","Ao contrário dos resistores: em paralelo as capacitâncias se somam.","В отличие от резисторов, при параллельном соединении ёмкости складываются.")),
 ],
 'kalkulator': {'tip': 'resi',
  'velicine': velicine({'q': None, 'C': 1e-6, 'U': 12, 'er': 1, 'e0': E0, 'Sp': 0.01, 'd': 0.001, 'WC': None, 'Cu': None, 'C1': 1e-6, 'C2': 2.2e-6},
                       {'q': 'µC', 'C': 'µF', 'Sp': 'cm²', 'd': 'mm', 'WC': 'J', 'Cu': 'µF', 'C1': 'µF', 'C2': 'µF'}),
  'jednacine': [
   {'latex': r"q = C U", 'trazi': 'q', 'resenja': {'q': 'C*U', 'C': 'q/U', 'U': 'q/C'}},
   {'latex': r"C = \varepsilon_r \varepsilon_0 \dfrac{S}{d}", 'trazi': 'C', 'promenljive': ['C', 'er', 'e0', 'Sp', 'd'],
    'resenja': {'C': 'er*e0*Sp/d', 'er': 'C*d/(e0*Sp)', 'Sp': 'C*d/(er*e0)', 'd': 'er*e0*Sp/C'}},
   {'latex': r"W = \dfrac{C U^2}{2}", 'trazi': 'WC', 'resenja': {'WC': 'C*U*U/2', 'C': '2*WC/(U*U)', 'U': 'sqrt(2*WC/C)'}},
   {'latex': r"C = C_1 + C_2", 'trazi': 'Cu', 'resenja': {'Cu': 'C1 + C2', 'C1': 'Cu - C2', 'C2': 'Cu - C1'}},
   {'latex': r"\dfrac{1}{C} = \dfrac{1}{C_1} + \dfrac{1}{C_2}", 'trazi': 'Cu', 'resenja': {'Cu': 'C1*C2/(C1 + C2)', 'C1': '1/(1/Cu - 1/C2)', 'C2': '1/(1/Cu - 1/C1)'}},
  ]}
})
v = teme[-1]['kalkulator']['velicine']; v['C']['jed'] = 'µF'
v['Sp']['pocetna'] = 0.01; v['WC']['jed'] = 'J'
v['d']['naziv'] = N['d']

for t in teme:
    for j in t['kalkulator']['jednacine']:
        for k in (j.get('promenljive') or j['resenja']):
            assert k in t['kalkulator']['velicine'], (t['id'], k)
    for f in t['formule']:
        o = f.get('objasnjenje')
        if isinstance(o, dict):
            for jj in J: o[jj] = o[jj].replace('ε_r', 'εᵣ').replace('w_e', 'wₑ')

out = {'oblast': 'elektricitet', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme))
