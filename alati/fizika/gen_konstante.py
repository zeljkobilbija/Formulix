# Generiše assets/oblasti/konstante.json (fizičke konstante, CODATA 2022 / SI)
import json, re, sys

J = ['sr', 'en', 'it', 'fr', 'es', 'de', 'pt', 'ru']
def T(*a):
    assert len(a) == 8, a
    return dict(zip(J, a))

RU = {'m': 'м', 's': 'с', 'kg': 'кг', 'N': 'Н', 'J': 'Дж', 'K': 'К', 'mol': 'моль', 'C': 'Кл', 'F': 'Ф',
      'A': 'А', 'W': 'Вт', 'eV': 'эВ', 'MeV': 'МэВ', 'km': 'км', 'Pa': 'Па', 'kPa': 'кПа', 'g': 'г',
      'u': 'а.е.м.', 'H': 'Гн', 'c': 'c'}

def jedinica(u, jez):
    """'N·m^2/kg^2' → LaTeX; za ruski ćirilične oznake."""
    if not u: return ''
    def tok(m):
        t = m.group(0)
        if t == 'c': return 'c'  # brzina svetlosti u MeV/c²
        if jez == 'ru' and t in RU: return r'\text{' + RU[t] + '}'
        return r'\mathrm{' + t + '}'
    s = re.sub(r'[A-Za-zμ]+', tok, u)
    s = s.replace('·', r'\cdot ')
    s = re.sub(r'\^(-?\d+)', r'^{\1}', s)
    return r'\,' + s

def broj(b, jez):
    """'6.62607015e-34' → 6,626 070 15 · 10⁻³⁴ (razmaci u grupama po 3)."""
    m, _, e = b.partition('e')
    ceo, _, dec = m.partition('.')
    if len(ceo) > 4: ceo = re.sub(r'(?<=\d)(?=(\d{3})+$)', r'\\,', ceo)
    if dec: dec = re.sub(r'(\d{3})(?=\d)', r'\1\\,', dec)
    sep = '.' if jez == 'en' else '{,}'
    s = ceo + (sep + dec if dec else '')
    if e: s += r' \cdot 10^{' + str(int(e)) + '}'
    return s

TACNO = T("Tačna vrednost, po definiciji SI.", "Exact value, by definition of the SI.", "Valore esatto, per definizione del SI.",
          "Valeur exacte, par définition du SI.", "Valor exacto, por definición del SI.", "Exakter Wert, per Definition des SI.",
          "Valor exato, por definição do SI.", "Точное значение по определению СИ.")

def K(naziv, oznaka, vrednosti, objasnjenje=None, tacno=False):
    """vrednosti: lista (broj, jedinica[, '≈']) – više zapisa iste veličine."""
    latex = {}
    for j in J:
        oz = oznaka[j] if isinstance(oznaka, dict) else oznaka
        delovi = []
        for v in vrednosti:
            znak = v[2] if len(v) > 2 else '='
            znak = r'\approx' if znak == '≈' else '='
            delovi.append(znak + ' ' + broj(v[0], j) + jedinica(v[1], j))
        latex[j] = oz + ' ' + r', \quad '.join(delovi)
    obj = None
    if tacno and objasnjenje:
        obj = {j: TACNO[j] + ' ' + objasnjenje[j] for j in J}
    elif tacno:
        obj = TACNO
    elif objasnjenje:
        obj = objasnjenje
    d = {'naslov': naziv, 'latex': latex}
    if obj: d['objasnjenje'] = obj
    return d

grupe = []

grupe.append(('mehanika', 'g',
 T("Mehanika i astronomija", "Mechanics and astronomy", "Meccanica e astronomia", "Mécanique et astronomie", "Mecánica y astronomía", "Mechanik und Astronomie", "Mecânica e astronomia", "Механика и астрономия"),
 T("g, G, Zemlja, Sunce, Mesec", "g, G, Earth, Sun, Moon", "g, G, Terra, Sole, Luna", "g, G, Terre, Soleil, Lune", "g, G, Tierra, Sol, Luna", "g, G, Erde, Sonne, Mond", "g, G, Terra, Sol, Lua", "g, G, Земля, Солнце, Луна"),
 [
  K(T("Ubrzanje Zemljine teže", "Gravitational acceleration", "Accelerazione di gravità", "Intensité de la pesanteur", "Aceleración de la gravedad", "Fallbeschleunigung", "Aceleração da gravidade", "Ускорение свободного падения"),
    'g_n', [('9.80665', 'm/s^2')],
    T("Standardna vrednost; u proračunima se obično uzima g ≈ 9,81 m/s².", "Standard value; calculations usually use g ≈ 9.81 m/s².", "Valore standard; nei calcoli si usa di solito g ≈ 9,81 m/s².", "Valeur normale ; dans les calculs on prend souvent g ≈ 9,81 m/s².", "Valor estándar; en los cálculos se suele usar g ≈ 9,81 m/s².", "Normwert; in Rechnungen meist g ≈ 9,81 m/s².", "Valor padrão; nos cálculos usa-se em geral g ≈ 9,81 m/s².", "Нормальное значение; в расчётах обычно g ≈ 9,81 м/с²."), tacno=True),
  K(T("Gravitaciona konstanta", "Gravitational constant", "Costante di gravitazione universale", "Constante gravitationnelle", "Constante de gravitación universal", "Gravitationskonstante", "Constante gravitacional", "Гравитационная постоянная"),
    'G', [('6.67430e-11', 'N·m^2/kg^2')]),
  K(T("Poluprečnik Zemlje (srednji)", "Earth's radius (mean)", "Raggio terrestre (medio)", "Rayon de la Terre (moyen)", "Radio de la Tierra (medio)", "Erdradius (mittlerer)", "Raio da Terra (médio)", "Радиус Земли (средний)"),
    'R_Z', [('6371', 'km')]),
  K(T("Masa Zemlje", "Mass of the Earth", "Massa della Terra", "Masse de la Terre", "Masa de la Tierra", "Masse der Erde", "Massa da Terra", "Масса Земли"),
    'M_Z', [('5.972e24', 'kg')]),
  K(T("Masa Sunca", "Mass of the Sun", "Massa del Sole", "Masse du Soleil", "Masa del Sol", "Masse der Sonne", "Massa do Sol", "Масса Солнца"),
    'M_S', [('1.989e30', 'kg')]),
  K(T("Masa Meseca", "Mass of the Moon", "Massa della Luna", "Masse de la Lune", "Masa de la Luna", "Masse des Mondes", "Massa da Lua", "Масса Луны"),
    'M_M', [('7.342e22', 'kg')]),
  K(T("Udaljenost Zemlja – Sunce (astronomska jedinica)", "Earth – Sun distance (astronomical unit)", "Distanza Terra – Sole (unità astronomica)", "Distance Terre – Soleil (unité astronomique)", "Distancia Tierra – Sol (unidad astronómica)", "Abstand Erde – Sonne (Astronomische Einheit)", "Distância Terra – Sol (unidade astronômica)", "Расстояние Земля – Солнце (астрономическая единица)"),
    {**{j: r'1\,\mathrm{AU}' for j in J}, 'sr': r'1\,\mathrm{AJ}', 'it': r'1\,\mathrm{UA}', 'fr': r'1\,\mathrm{UA}', 'es': r'1\,\mathrm{UA}', 'de': r'1\,\mathrm{AE}', 'pt': r'1\,\mathrm{UA}', 'ru': r'1\,\text{а.е.}'}, [('1.495978707e8', 'km')]),
  K(T("Udaljenost Zemlja – Mesec (srednja)", "Earth – Moon distance (mean)", "Distanza Terra – Luna (media)", "Distance Terre – Lune (moyenne)", "Distancia Tierra – Luna (media)", "Abstand Erde – Mond (mittlerer)", "Distância Terra – Lua (média)", "Расстояние Земля – Луна (среднее)"),
    'd', [('384400', 'km')]),
 ]))

grupe.append(('supstance', 'ρ',
 T("Supstance i gasovi", "Substances and gases", "Sostanze e gas", "Substances et gaz", "Sustancias y gases", "Stoffe und Gase", "Substâncias e gases", "Вещества и газы"),
 T("Voda, vazduh, R, Nₐ, k", "Water, air, R, Nₐ, k", "Acqua, aria, R, Nₐ, k", "Eau, air, R, Nₐ, k", "Agua, aire, R, Nₐ, k", "Wasser, Luft, R, Nₐ, k", "Água, ar, R, Nₐ, k", "Вода, воздух, R, Nₐ, k"),
 [
  K(T("Gustina vode", "Density of water", "Densità dell’acqua", "Masse volumique de l’eau", "Densidad del agua", "Dichte von Wasser", "Massa específica da água", "Плотность воды"),
    r'\rho_{\mathrm{H_2O}}', [('1000', 'kg/m^3', '≈')],
    T("Na 4 °C; 1 g/cm³ = 1 kg/L.", "At 4 °C; 1 g/cm³ = 1 kg/L.", "A 4 °C; 1 g/cm³ = 1 kg/L.", "À 4 °C ; 1 g/cm³ = 1 kg/L.", "A 4 °C; 1 g/cm³ = 1 kg/L.", "Bei 4 °C; 1 g/cm³ = 1 kg/L.", "A 4 °C; 1 g/cm³ = 1 kg/L.", "При 4 °C; 1 г/см³ = 1 кг/л.")),
  K(T("Normalni atmosferski pritisak", "Standard atmospheric pressure", "Pressione atmosferica normale", "Pression atmosphérique normale", "Presión atmosférica normal", "Normaler Luftdruck", "Pressão atmosférica normal", "Нормальное атмосферное давление"),
    'p_0', [('101325', 'Pa'), ('101.325', 'kPa')],
    T("Na nivou mora; često se zaokružuje na 100 kPa.", "At sea level; often rounded to 100 kPa.", "Al livello del mare; spesso arrotondata a 100 kPa.", "Au niveau de la mer ; souvent arrondie à 100 kPa.", "Al nivel del mar; a menudo se redondea a 100 kPa.", "Auf Meereshöhe; oft auf 100 kPa gerundet.", "Ao nível do mar; muitas vezes arredondada para 100 kPa.", "На уровне моря; часто округляют до 100 кПа."), tacno=True),
  K(T("Specifični toplotni kapacitet vode", "Specific heat capacity of water", "Calore specifico dell’acqua", "Capacité thermique massique de l’eau", "Calor específico del agua", "Spezifische Wärmekapazität von Wasser", "Calor específico da água", "Удельная теплоёмкость воды"),
    r'c_{\mathrm{H_2O}}', [('4186', 'J/(kg·K)', '≈')]),
  K(T("Indeks prelamanja vode", "Refractive index of water", "Indice di rifrazione dell’acqua", "Indice de réfraction de l’eau", "Índice de refracción del agua", "Brechungsindex von Wasser", "Índice de refração da água", "Показатель преломления воды"),
    'n', [('1.33', '', '≈')]),
  K(T("Univerzalna gasna konstanta", "Molar gas constant", "Costante universale dei gas", "Constante des gaz parfaits", "Constante universal de los gases", "Universelle Gaskonstante", "Constante universal dos gases", "Универсальная газовая постоянная"),
    'R', [('8.314462618', 'J/(mol·K)')],
    T("R = Nₐ·k. U kilomolovima: 8314 J/(kmol·K).", "R = Nₐ·k. Per kilomole: 8314 J/(kmol·K).", "R = Nₐ·k. Per kilomole: 8314 J/(kmol·K).", "R = Nₐ·k. Par kilomole : 8314 J/(kmol·K).", "R = Nₐ·k. Por kilomol: 8314 J/(kmol·K).", "R = Nₐ·k. Pro Kilomol: 8314 J/(kmol·K).", "R = Nₐ·k. Por quilomol: 8314 J/(kmol·K).", "R = Nₐ·k. На киломоль: 8314 Дж/(кмоль·К)."), tacno=True),
  K(T("Avogadrova konstanta", "Avogadro constant", "Costante di Avogadro", "Constante d’Avogadro", "Constante de Avogadro", "Avogadro-Konstante", "Constante de Avogadro", "Постоянная Авогадро"),
    'N_A', [('6.02214076e23', 'mol^-1')], tacno=True),
  K(T("Bolcmanova konstanta", "Boltzmann constant", "Costante di Boltzmann", "Constante de Boltzmann", "Constante de Boltzmann", "Boltzmann-Konstante", "Constante de Boltzmann", "Постоянная Больцмана"),
    'k', [('1.380649e-23', 'J/K')], tacno=True),
  K(T("Molarna masa vazduha", "Molar mass of air", "Massa molare dell’aria", "Masse molaire de l’air", "Masa molar del aire", "Molare Masse der Luft", "Massa molar do ar", "Молярная масса воздуха"),
    'M', [('0.02897', 'kg/mol'), ('28.97', 'g/mol')]),
  K(T("Odnos specifičnih toplota gasa", "Heat capacity ratio of a gas", "Rapporto dei calori specifici", "Indice adiabatique d’un gaz", "Coeficiente adiabático de un gas", "Isentropenexponent eines Gases", "Coeficiente de Poisson de um gás", "Показатель адиабаты газа"),
    {j: r'\kappa = \dfrac{5}{3}\ (\text{%s}), \quad \kappa = \dfrac{7}{5}\ (\text{%s})' for j in J} if False else r'\kappa', [], None),
 ]))

# κ ima poseban zapis (razlomci, jednoatomni / dvoatomni)
KAPA = {
 'sr': ('jednoatomni', 'dvoatomni'), 'en': ('monatomic', 'diatomic'), 'it': ('monoatomico', 'biatomico'),
 'fr': ('monoatomique', 'diatomique'), 'es': ('monoatómico', 'diatómico'), 'de': ('einatomig', 'zweiatomig'),
 'pt': ('monoatômico', 'diatômico'), 'ru': ('одноатомный', 'двухатомный')}
kapa = grupe[-1][4][-1]
kapa['latex'] = {j: r'\kappa = \frac{5}{3} \;\text{(%s)}, \quad \kappa = \frac{7}{5} \;\text{(%s)}' % KAPA[j] for j in J}
kapa['objasnjenje'] = T("κ = cₚ / cᵥ; koristi se za adijabatske procese.", "κ = cₚ / cᵥ; used for adiabatic processes.", "κ = cₚ / cᵥ; si usa nelle trasformazioni adiabatiche.", "κ = cₚ / cᵥ ; utilisé pour les transformations adiabatiques.", "κ = cₚ / cᵥ; se usa en procesos adiabáticos.", "κ = cₚ / cᵥ; für adiabatische Prozesse.", "κ = cₚ / cᵥ; usado em processos adiabáticos.", "κ = cₚ / cᵥ; используется для адиабатных процессов.")

grupe.append(('elektromagnetizam', 'e',
 T("Elektricitet i magnetizam", "Electricity and magnetism", "Elettricità e magnetismo", "Électricité et magnétisme", "Electricidad y magnetismo", "Elektrizität und Magnetismus", "Eletricidade e magnetismo", "Электричество и магнетизм"),
 T("e, ε₀, μ₀, Kulonova konstanta", "e, ε₀, μ₀, Coulomb constant", "e, ε₀, μ₀, costante di Coulomb", "e, ε₀, μ₀, constante de Coulomb", "e, ε₀, μ₀, constante de Coulomb", "e, ε₀, μ₀, Coulomb-Konstante", "e, ε₀, μ₀, constante de Coulomb", "e, ε₀, μ₀, постоянная Кулона"),
 [
  K(T("Elementarno naelektrisanje", "Elementary charge", "Carica elementare", "Charge élémentaire", "Carga elemental", "Elementarladung", "Carga elementar", "Элементарный заряд"),
    'e', [('1.602176634e-19', 'C')], tacno=True),
  K(T("Električna konstanta (permitivnost vakuuma)", "Electric constant (vacuum permittivity)", "Costante dielettrica del vuoto", "Permittivité du vide", "Permitividad del vacío", "Elektrische Feldkonstante", "Permissividade do vácuo", "Электрическая постоянная"),
    r'\varepsilon_0', [('8.8541878188e-12', 'F/m')],
    T("F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "F/m = A·s/(V·m) = C²/(N·m²).", "Ф/м = А·с/(В·м) = Кл²/(Н·м²).")),
  K(T("Magnetna konstanta (permeabilnost vakuuma)", "Magnetic constant (vacuum permeability)", "Permeabilità magnetica del vuoto", "Perméabilité du vide", "Permeabilidad del vacío", "Magnetische Feldkonstante", "Permeabilidade do vácuo", "Магнитная постоянная"),
    r'\mu_0', [('1.25663706127e-6', 'N/A^2')],
    T("Približno 4π · 10⁻⁷ V·s/(A·m).", "Approximately 4π · 10⁻⁷ V·s/(A·m).", "Circa 4π · 10⁻⁷ V·s/(A·m).", "Environ 4π · 10⁻⁷ V·s/(A·m).", "Aproximadamente 4π · 10⁻⁷ V·s/(A·m).", "Etwa 4π · 10⁻⁷ V·s/(A·m).", "Aproximadamente 4π · 10⁻⁷ V·s/(A·m).", "Приблизительно 4π · 10⁻⁷ В·с/(А·м).")),
  K(T("Kulonova konstanta", "Coulomb constant", "Costante di Coulomb", "Constante de Coulomb", "Constante de Coulomb", "Coulomb-Konstante", "Constante de Coulomb", "Постоянная Кулона"),
    r'\dfrac{1}{4\pi\varepsilon_0}', [('8.9875517862e9', 'N·m^2/C^2')],
    T("Iz Kulonovog zakona F = e₁e₂/(4πε₀r²).", "From Coulomb's law F = e₁e₂/(4πε₀r²).", "Dalla legge di Coulomb F = e₁e₂/(4πε₀r²).", "De la loi de Coulomb F = e₁e₂/(4πε₀r²).", "De la ley de Coulomb F = e₁e₂/(4πε₀r²).", "Aus dem Coulombschen Gesetz F = e₁e₂/(4πε₀r²).", "Da lei de Coulomb F = e₁e₂/(4πε₀r²).", "Из закона Кулона F = e₁e₂/(4πε₀r²).")),
 ]))

grupe.append(('atomi', 'h',
 T("Svetlost, atomi i čestice", "Light, atoms and particles", "Luce, atomi e particelle", "Lumière, atomes et particules", "Luz, átomos y partículas", "Licht, Atome und Teilchen", "Luz, átomos e partículas", "Свет, атомы и частицы"),
 T("c, h, mase čestica", "c, h, particle masses", "c, h, masse delle particelle", "c, h, masses des particules", "c, h, masas de partículas", "c, h, Teilchenmassen", "c, h, massas das partículas", "c, h, массы частиц"),
 [
  K(T("Brzina svetlosti u vakuumu", "Speed of light in vacuum", "Velocità della luce nel vuoto", "Vitesse de la lumière dans le vide", "Velocidad de la luz en el vacío", "Lichtgeschwindigkeit im Vakuum", "Velocidade da luz no vácuo", "Скорость света в вакууме"),
    'c_0', [('299792458', 'm/s')],
    T("Približno 3,0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "About 3.0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "Circa 3,0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "Environ 3,0 · 10⁸ m/s ; c₀ = 1/√(ε₀μ₀).", "Unos 3,0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "Etwa 3,0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "Cerca de 3,0 · 10⁸ m/s; c₀ = 1/√(ε₀μ₀).", "Около 3,0 · 10⁸ м/с; c₀ = 1/√(ε₀μ₀)."), tacno=True),
  K(T("Plankova konstanta", "Planck constant", "Costante di Planck", "Constante de Planck", "Constante de Planck", "Plancksches Wirkungsquantum", "Constante de Planck", "Постоянная Планка"),
    'h', [('6.62607015e-34', 'J·s'), ('4.135667696e-15', 'eV·s')], tacno=True),
  K(T("Redukovana Plankova konstanta", "Reduced Planck constant", "Costante di Planck ridotta", "Constante de Planck réduite", "Constante de Planck reducida", "Reduziertes Plancksches Wirkungsquantum", "Constante de Planck reduzida", "Приведённая постоянная Планка"),
    r'\hbar = \dfrac{h}{2\pi}', [('1.054571817e-34', 'J·s')]),
  K(T("Štefan-Bolcmanova konstanta", "Stefan–Boltzmann constant", "Costante di Stefan-Boltzmann", "Constante de Stefan-Boltzmann", "Constante de Stefan-Boltzmann", "Stefan-Boltzmann-Konstante", "Constante de Stefan-Boltzmann", "Постоянная Стефана — Больцмана"),
    r'\sigma', [('5.670374419e-8', 'W/(m^2·K^4)')]),
  K(T("Vinova konstanta", "Wien's displacement constant", "Costante di Wien", "Constante de Wien", "Constante de Wien", "Wiensche Konstante", "Constante de Wien", "Постоянная Вина"),
    'k_W', [('2.897771955e-3', 'm·K')],
    T("λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.", "λₘₐₓ · T = const.")),
  K(T("Atomska jedinica mase", "Atomic mass unit", "Unità di massa atomica", "Unité de masse atomique", "Unidad de masa atómica", "Atomare Masseneinheit", "Unidade de massa atômica", "Атомная единица массы"),
    'u', [('1.66053906892e-27', 'kg'), ('931.49410372', 'MeV/c^2')]),
  K(T("Masa elektrona", "Electron mass", "Massa dell’elettrone", "Masse de l’électron", "Masa del electrón", "Elektronenmasse", "Massa do elétron", "Масса электрона"),
    'm_e', [('9.1093837139e-31', 'kg'), ('0.51099895069', 'MeV/c^2')]),
  K(T("Masa protona", "Proton mass", "Massa del protone", "Masse du proton", "Masa del protón", "Protonenmasse", "Massa do próton", "Масса протона"),
    'm_p', [('1.67262192595e-27', 'kg'), ('1.00727646688', 'u'), ('938.27208943', 'MeV/c^2')]),
  K(T("Masa neutrona", "Neutron mass", "Massa del neutrone", "Masse du neutron", "Masa del neutrón", "Neutronenmasse", "Massa do nêutron", "Масса нейтрона"),
    'm_n', [('1.67492750056e-27', 'kg'), ('1.00866491606', 'u'), ('939.56542194', 'MeV/c^2')]),
 ]))

teme = []
for gid, simbol, naziv, opis, konst in grupe:
    kljucne = {j: ' '.join(k['naslov'][j].lower() for k in konst) + ' konstanta constant' for j in J}
    teme.append({'id': gid, 'simbol': simbol, 'naziv': naziv, 'opis': opis, 'kljucne_reci': kljucne, 'formule': konst})

# Više zapisa iste veličine: svaki u svom redu (tema.js deli na ", \quad ")
for t in teme:
    for k in t['formule']:
        for j in J:
            k['latex'][j] = k['latex'][j].replace(r' \\[2pt] ', ' ')
            # "= a = b" → "x = a, \quad = b" ne izgleda dobro; ostavljamo u jednom redu,
            # a tema.js će ga smanjiti ako je preširok.

out = {'oblast': 'konstante', 'teme': teme}
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('teme:', len(teme), 'konstanti:', sum(len(t['formule']) for t in teme))
