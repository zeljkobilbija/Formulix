// Formulix – prikaz jedne teme: formule (KaTeX), objašnjenja i kalkulator.
// Parametri u adresi: ?oblast=aritmetika&tema=procenti&jezik=sr&tamno=0&boja=%232E5BBA
(function () {
  'use strict';

  var p = new URLSearchParams(location.search);
  var OBLAST = p.get('oblast') || 'aritmetika';
  var TEMA = p.get('tema') || '';
  var JEZIK = p.get('jezik') || 'en';
  var TAMNO = p.get('tamno') === '1';
  var BOJA = p.get('boja') || '#2E5BBA';

  var UI = {
    izracunaj: { sr: 'Izračunaj', en: 'Calculate', it: 'Calcola', fr: 'Calculer', es: 'Calcular', de: 'Berechnen', pt: 'Calcular', ru: 'Вычислить' },
    greska: { sr: 'Tema nije pronađena.', en: 'Topic not found.', it: 'Argomento non trovato.', fr: 'Sujet introuvable.', es: 'Tema no encontrado.', de: 'Thema nicht gefunden.', pt: 'Tema não encontrado.', ru: 'Тема не найдена.' },
    naOsi: { sr: 'na osi', en: 'on an axis', it: 'su un asse', fr: 'sur un axe', es: 'sobre un eje', de: 'auf einer Achse', pt: 'sobre um eixo', ru: 'на оси' },
    nema: { sr: 'nema', en: 'none', it: 'nessuno', fr: 'aucun', es: 'ninguno', de: 'keine', pt: 'nenhum', ru: 'нет' },
    formula: { sr: 'Formula', en: 'Formula', it: 'Formula', fr: 'Formule', es: 'Fórmula', de: 'Formel', pt: 'Fórmula', ru: 'Формула' },
    trazi: { sr: 'Šta se traži', en: 'Solve for', it: 'Incognita', fr: 'Inconnue', es: 'Incógnita', de: 'Gesucht', pt: 'Incógnita', ru: 'Найти' },
    nemaResenja: { sr: 'Za ove vrednosti nema rešenja.', en: 'No solution for these values.', it: 'Nessuna soluzione per questi valori.', fr: 'Pas de solution pour ces valeurs.', es: 'No hay solución para estos valores.', de: 'Für diese Werte gibt es keine Lösung.', pt: 'Sem solução para estes valores.', ru: 'Для этих значений нет решения.' },
    nijedan: { sr: 'nijedan od navedenih', en: 'none of these', it: 'nessuno di questi', fr: 'aucun de ces nombres', es: 'ninguno de estos', de: 'keiner davon', pt: 'nenhum destes', ru: 'ни на одно из них' }
  };

  // ---------- pomoćne funkcije ----------
  function tekst(v) {
    if (v === null || v === undefined) return '';
    if (typeof v === 'string') return v;
    if (v[JEZIK] !== undefined) return v[JEZIK];
    return v.en !== undefined ? v.en : (v.sr || '');
  }
  function el(tag, klasa, sadrzaj) {
    var e = document.createElement(tag);
    if (klasa) e.className = klasa;
    if (sadrzaj !== undefined) e.textContent = sadrzaj;
    return e;
  }
  function latex(cilj, izraz, blok) {
    try {
      katex.render(izraz, cilj, { displayMode: !!blok, throwOnError: false, strict: 'ignore' });
    } catch (e) {
      cilj.textContent = izraz;
    }
  }
  var LOKAL = { sr: 'sr-Latn-RS', en: 'en', it: 'it', fr: 'fr', es: 'es', de: 'de', pt: 'pt', ru: 'ru' }[JEZIK] || 'en';
  var fmt = new Intl.NumberFormat(LOKAL, { maximumFractionDigits: 6 });
  var fmtNauc = new Intl.NumberFormat(LOKAL, { notation: 'scientific', maximumFractionDigits: 6 });
  var DEC = fmt.format(1.5).charAt(1); // decimalni separator jezika: "," ili "."
  function broj(x) {
    if (typeof x !== 'number' || !isFinite(x)) return '–';
    if (x === 0) x = 0; // bez "-0"
    if (Math.abs(x) >= 1e15 || (x !== 0 && Math.abs(x) < 1e-6)) return fmtNauc.format(x);
    return fmt.format(x);
  }
  // Prihvata i zarez i tačku kao decimalni separator
  function procitaj(s) {
    s = String(s).trim().replace(/\s/g, '').replace(',', '.');
    if (s === '' || s === '-' || s === '.') return NaN;
    return Number(s);
  }

  // ---------- matematičke funkcije dostupne u izrazima ----------
  function nzd(a, b) {
    if (!Number.isInteger(a) || !Number.isInteger(b)) return NaN;
    a = Math.abs(a); b = Math.abs(b);
    while (b) { var t = a % b; a = b; b = t; }
    return a;
  }
  function nzs(a, b) {
    var g = nzd(a, b);
    return g ? Math.abs(a * b) / g : (g === 0 ? 0 : NaN);
  }
  function koren(a, n) {
    if (n === 0) return NaN;
    if (a < 0 && Number.isInteger(n) && Math.abs(n) % 2 === 1) return -Math.pow(-a, 1 / n);
    return Math.pow(a, 1 / n);
  }
  function deljivost(n) {
    if (!Number.isInteger(n)) return '–';
    var d = [2, 3, 4, 5, 6, 9, 10, 11].filter(function (k) { return n % k === 0; });
    return d.length ? d.join(', ') : tekst(UI.nijedan);
  }
  // Rešenja kvadratne jednačine ax² + bx + c = 0 kao tekst (i kompleksna)
  function kvadratna(a, b, c) {
    if (![a, b, c].every(isFinite)) return '–';
    if (a === 0) return b === 0 ? '–' : 'x = ' + broj(-c / b);
    var d = b * b - 4 * a * c;
    if (d > 0) {
      var k = Math.sqrt(d);
      return 'x₁ = ' + broj((-b + k) / (2 * a)) + ',  x₂ = ' + broj((-b - k) / (2 * a));
    }
    if (d === 0) return 'x₁ = x₂ = ' + broj(-b / (2 * a));
    var re = -b / (2 * a), im = Math.abs(Math.sqrt(-d) / (2 * a));
    return 'x₁,₂ = ' + (re === 0 ? '' : broj(re) + ' ± ') + (re === 0 ? '±' : '') + broj(im) + 'i';
  }
  // Heronov obrazac; NaN ako stranice ne mogu da čine trougao
  function heron(a, b, c) {
    var s = (a + b + c) / 2, p = s * (s - a) * (s - b) * (s - c);
    return a > 0 && b > 0 && c > 0 && p > 0 ? Math.sqrt(p) : NaN;
  }
  // Trigonometrija u stepenima; vrednosti bliske nuli zaokružujemo na 0
  function cist(x) { return Math.abs(x) < 1e-12 ? 0 : x; }
  function sinS(x) { return cist(Math.sin(x * Math.PI / 180)); }
  function cosS(x) { return cist(Math.cos(x * Math.PI / 180)); }
  function tgS(x) { var c = cosS(x); return c === 0 ? NaN : cist(sinS(x) / c); }
  function ctgS(x) { var s = sinS(x); return s === 0 ? NaN : cist(cosS(x) / s); }
  function stepeni(rad) { return rad * 180 / Math.PI; }
  function kvadrant(x) {
    if (!isFinite(x)) return '–';
    var u = ((x % 360) + 360) % 360;
    if (u % 90 === 0) return tekst(UI.naOsi);
    return ['I', 'II', 'III', 'IV'][Math.floor(u / 90)];
  }
  // Polinom f(x) = ax³ + bx² + cx + d: tangenta u x0 i stacionarne tačke (f′ = 0)
  function clan(k, x, prvi) {
    if (k === 0) return '';
    var z = k < 0 ? '−' : '+', v = Math.abs(k);
    var t = (x && v === 1) ? '' : broj(v);
    if (prvi) return (k < 0 ? '−' : '') + t + x;
    return ' ' + z + ' ' + t + x;
  }
  function tangenta(a, b, c, d, x0) {
    if (![a, b, c, d, x0].every(isFinite)) return '–';
    var k = 3 * a * x0 * x0 + 2 * b * x0 + c;
    var y0 = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d;
    var n = y0 - k * x0;
    if (k === 0) return 'y = ' + broj(n);
    return 'y = ' + clan(k, 'x', true) + clan(n, '', false);
  }
  function stacionarne(a, b, c) {
    if (![a, b, c].every(isFinite)) return '–';
    var A = 3 * a, B = 2 * b;
    if (A === 0) return B === 0 ? tekst(UI.nema) : 'x = ' + broj(-c / B);
    var D = B * B - 4 * A * c;
    if (D < 0) return tekst(UI.nema);
    if (D === 0) return 'x = ' + broj(-B / (2 * A));
    var k = Math.sqrt(D), x1 = (-B - k) / (2 * A), x2 = (-B + k) / (2 * A);
    return 'x₁ = ' + broj(Math.min(x1, x2)) + ',  x₂ = ' + broj(Math.max(x1, x2));
  }
  // Kombinatorika: n!, varijacije, kombinacije, red Paskalovog trougla
  function prirodan(n) { return Number.isInteger(n) && n >= 0; }
  function fakt(n) {
    if (!prirodan(n) || n > 170) return NaN;
    var r = 1;
    for (var i = 2; i <= n; i++) r *= i;
    return r;
  }
  function varij(n, k) {
    if (!prirodan(n) || !prirodan(k) || k > n) return k > n && prirodan(n) && prirodan(k) ? 0 : NaN;
    var r = 1;
    for (var i = 0; i < k; i++) r *= (n - i);
    return r;
  }
  function komb(n, k) {
    if (!prirodan(n) || !prirodan(k)) return NaN;
    if (k > n) return 0;
    k = Math.min(k, n - k);
    var r = 1;
    for (var i = 1; i <= k; i++) r = r * (n - k + i) / i;
    return Math.round(r);
  }
  function paskal(n) {
    if (!prirodan(n) || n > 30) return '–';
    var red = [];
    for (var k = 0; k <= n; k++) red.push(fmt.format(komb(n, k)));
    return red.join('  ');
  }
  var FUNKCIJE = { fakt: fakt, varij: varij, komb: komb, paskal: paskal, tangenta: tangenta, stacionarne: stacionarne, sinS: sinS, cosS: cosS, tgS: tgS, ctgS: ctgS, stepeni: stepeni, kvadrant: kvadrant, heron: heron, pow: Math.pow, sqrt: Math.sqrt, abs: Math.abs, PI: Math.PI, nzd: nzd, nzs: nzs, koren: koren,
    deljivost: deljivost, kvadratna: kvadratna };

  // Izrazi dolaze iz naših JSON fajlova (assets), ne od korisnika.
  function prevedi(izraz, promenljive, funkcije) {
    funkcije = funkcije || FUNKCIJE;
    // Funkcija istog imena kao promenljiva se preskače (promenljiva ima prednost)
    var fimena = Object.keys(funkcije).filter(function (k) { return promenljive.indexOf(k) < 0; });
    var imena = promenljive.concat(fimena);
    /* eslint-disable no-new-func */
    var f = new Function(imena.join(','), '"use strict"; return (' + izraz + ');');
    return function (vrednosti) {
      var args = promenljive.map(function (k) { return vrednosti[k]; })
        .concat(fimena.map(function (k) { return funkcije[k]; }));
      try { return f.apply(null, args); } catch (e) { return NaN; }
    };
  }

  // ---------- fizika: funkcije, jedinice ----------
  // Najmanji pozitivan koren od A·x² + B·x + C = 0 (npr. vreme iz s = v₀t + at²/2)
  function kvPoz(A, B, C) {
    if (![A, B, C].every(isFinite)) return NaN;
    if (Math.abs(A) < 1e-15) { var x0 = -C / B; return x0 > 0 ? x0 : NaN; }
    var D = B * B - 4 * A * C;
    if (D < 0) return NaN;
    var k = Math.sqrt(D), r = [(-B - k) / (2 * A), (-B + k) / (2 * A)]
      .filter(function (x) { return x > 1e-12; });
    return r.length ? Math.min.apply(null, r) : NaN;
  }
  var FIZ = Object.assign({}, FUNKCIJE, {
    sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos,
    atan: Math.atan, atan2: Math.atan2, exp: Math.exp, ln: Math.log, log10: Math.log10,
    cbrt: Math.cbrt, kvPoz: kvPoz
  });

  // Jedinice: [id, faktor do SI, pomak]; SI = x·faktor + pomak. Prva je osnovna.
  var PI = Math.PI;
  var JED = {
    bez: [['', 1]],
    duzina: [['m', 1], ['km', 1e3], ['cm', 1e-2], ['mm', 1e-3]],
    vreme: [['s', 1], ['min', 60], ['h', 3600], ['ms', 1e-3], ['µs', 1e-6], ['dan', 86400], ['god', 3.15576e7]],
    brzina: [['m/s', 1], ['cm/s', 1e-2], ['km/h', 1 / 3.6]],
    ubrzanje: [['m/s²', 1], ['cm/s²', 1e-2]],
    ugao: [['°', PI / 180], ['rad', 1], ['obr', 2 * PI]],
    ugaonaBrzina: [['rad/s', 1], ['°/s', PI / 180], ['obr/min', 2 * PI / 60]],
    ugaonoUbrzanje: [['rad/s²', 1], ['°/s²', PI / 180]],
    frekvencija: [['Hz', 1], ['obr/min', 1 / 60], ['kHz', 1e3], ['MHz', 1e6], ['GHz', 1e9], ['THz', 1e12]],
    povrsina: [['m²', 1], ['dm²', 1e-2], ['cm²', 1e-4], ['mm²', 1e-6]],
    zapremina: [['m³', 1], ['L', 1e-3], ['cm³', 1e-6], ['mL', 1e-6]],
    zapreminskiProtok: [['m³/s', 1], ['L/s', 1e-3], ['L/min', 1e-3 / 60], ['m³/h', 1 / 3600]],
    maseniProtok: [['kg/s', 1], ['g/s', 1e-3], ['kg/h', 1 / 3600], ['t/h', 1 / 3.6]],
    masa: [['kg', 1], ['g', 1e-3], ['t', 1e3], ['u', 1.66053906892e-27]],
    gustina: [['kg/m³', 1], ['g/cm³', 1e3], ['kg/L', 1e3]],
    temperatura: [['K', 1, 0], ['°C', 1, 273.15]],
    sila: [['N', 1], ['kN', 1e3], ['mN', 1e-3], ['µN', 1e-6]],
    krutost: [['N/m', 1], ['N/cm', 100], ['kN/m', 1e3]],
    pritisak: [['Pa', 1], ['kPa', 1e3], ['MPa', 1e6], ['GPa', 1e9], ['bar', 1e5]],
    moment: [['N·m', 1], ['kN·m', 1e3]],
    torzija: [['N·m/rad', 1]],
    impuls: [['kg·m/s', 1], ['N·s', 1]],
    gravKonst: [['N·m²/kg²', 1]],
    energija: [['J', 1], ['mJ', 1e-3], ['kJ', 1e3], ['MJ', 1e6], ['Wh', 3600], ['kWh', 3.6e6], ['cal', 4.184], ['kcal', 4184], ['eV', 1.602176634e-19], ['keV', 1.602176634e-16], ['MeV', 1.602176634e-13]],
    snaga: [['W', 1], ['kW', 1e3], ['MW', 1e6]],
    udeo: [['%', 0.01]],
    viskoznost: [['Pa·s', 1], ['mPa·s', 1e-3]],
    povrsinskiNapon: [['N/m', 1], ['mN/m', 1e-3]],
    stisljivost: [['1/GPa', 1e-9], ['1/Pa', 1], ['1/bar', 1e-5]],
    momentInercije: [['kg·m²', 1], ['g·cm²', 1e-7]],
    momentImpulsa: [['kg·m²/s', 1], ['J·s', 1]],
    tempRazlika: [['K', 1], ['°C', 1]],
    koefSirenja: [['1/K', 1], ['10⁻⁶/K', 1e-6]],
    specToplota: [['J/(kg·K)', 1], ['kJ/(kg·K)', 1e3]],
    specLatentna: [['J/kg', 1], ['kJ/kg', 1e3], ['MJ/kg', 1e6]],
    molarnaMasa: [['g/mol', 1e-3], ['kg/mol', 1]],
    gasKonst: [['J/(mol·K)', 1]],
    boltzmann: [['J/K', 1]],
    toplProvodljivost: [['W/(m·K)', 1]],
    koncentracija: [['1/m³', 1], ['1/cm³', 1e6]],
    naboj: [['C', 1], ['mC', 1e-3], ['µC', 1e-6], ['nC', 1e-9]],
    struja: [['A', 1], ['mA', 1e-3], ['kA', 1e3]],
    napon: [['V', 1], ['mV', 1e-3], ['kV', 1e3]],
    otpor: [['Ω', 1], ['kΩ', 1e3], ['MΩ', 1e6]],
    specOtpor: [['Ω·m', 1], ['Ω·mm²/m', 1e-6]],
    tempKoef: [['1/K', 1]],
    elPolje: [['V/m', 1], ['kV/m', 1e3]],
    kapacitet: [['F', 1], ['mF', 1e-3], ['µF', 1e-6], ['nF', 1e-9], ['pF', 1e-12]],
    permitivnost: [['F/m', 1]],
    magPolje: [['T', 1], ['mT', 1e-3], ['µT', 1e-6], ['G', 1e-4]],
    magFluks: [['Wb', 1], ['mWb', 1e-3], ['µWb', 1e-6]],
    induktivnost: [['H', 1], ['mH', 1e-3], ['µH', 1e-6]],
    permeabilnost: [['N/A²', 1]],
    povrsinaPetlje: [['m²', 1], ['cm²', 1e-4]],
    brzinaPromene: [['A/s', 1]],
    talasnaDuzina: [['nm', 1e-9], ['pm', 1e-12], ['µm', 1e-6], ['mm', 1e-3], ['cm', 1e-2], ['m', 1], ['km', 1e3]],
    intenzitet: [['W/m²', 1], ['kW/m²', 1e3], ['mW/cm²', 10]],
    optickaJacina: [['dpt', 1]],
    stefan: [['W/(m²·K⁴)', 1]],
    wien: [['m·K', 1]],
    plank: [['J·s', 1], ['eV·s', 1.602176634e-19]],
    aktivnost: [['Bq', 1], ['kBq', 1e3], ['MBq', 1e6], ['GBq', 1e9], ['Ci', 3.7e10]],
    konstRaspada: [['1/s', 1], ['1/h', 1 / 3600], ['1/dan', 1 / 86400], ['1/god', 1 / 3.15576e7]],
    koefSlabljenja: [['1/m', 1], ['1/cm', 100], ['1/mm', 1000]],
    broj: [['', 1]]
  };
  var JED_NATPIS = {
    obr: { sr: 'obr', en: 'rev', it: 'giri', fr: 'tr', es: 'rev', de: 'U', pt: 'rot', ru: 'об' },
    dan: { sr: 'dan', en: 'd', it: 'g', fr: 'j', es: 'd', de: 'd', pt: 'd', ru: 'сут' },
    god: { sr: 'god', en: 'yr', it: 'anni', fr: 'an', es: 'años', de: 'a', pt: 'anos', ru: 'лет' },
    '1/dan': { sr: '1/dan', en: '1/d', it: '1/g', fr: '1/j', es: '1/d', de: '1/d', pt: '1/d', ru: '1/сут' },
    '1/god': { sr: '1/god', en: '1/yr', it: '1/anno', fr: '1/an', es: '1/año', de: '1/a', pt: '1/ano', ru: '1/год' },
    'obr/min': { sr: 'obr/min', en: 'rpm', it: 'giri/min', fr: 'tr/min', es: 'rpm', de: 'U/min', pt: 'rpm', ru: 'об/мин' }
  };
  var JED_RU = { m: 'м', km: 'км', cm: 'см', mm: 'мм', s: 'с', min: 'мин', h: 'ч', ms: 'мс', 'µs': 'мкс', 'cm/s': 'см/с',
    'm/s': 'м/с', 'km/h': 'км/ч', 'm/s²': 'м/с²', 'cm/s²': 'см/с²', rad: 'рад', 'rad/s': 'рад/с',
    '°/s': '°/с', 'rad/s²': 'рад/с²', '°/s²': '°/с²', Hz: 'Гц', kHz: 'кГц', 'm²': 'м²', 'dm²': 'дм²',
    'cm²': 'см²', 'mm²': 'мм²', 'm³': 'м³', L: 'л', 'cm³': 'см³', mL: 'мл', 'm³/s': 'м³/с',
    'L/s': 'л/с', 'L/min': 'л/мин', 'm³/h': 'м³/ч', 'kg/s': 'кг/с', 'g/s': 'г/с', 'kg/h': 'кг/ч',
    't/h': 'т/ч', kg: 'кг', g: 'г', t: 'т', 'kg/m³': 'кг/м³', 'g/cm³': 'г/см³', 'kg/L': 'кг/л', K: 'К',
    N: 'Н', kN: 'кН', mN: 'мН', 'µN': 'мкН', 'N/m': 'Н/м', 'N/cm': 'Н/см', 'kN/m': 'кН/м', Pa: 'Па', kPa: 'кПа',
    MPa: 'МПа', GPa: 'ГПа', bar: 'бар', 'N·m': 'Н·м', 'kN·m': 'кН·м', 'N·m/rad': 'Н·м/рад',
    'kg·m/s': 'кг·м/с', 'N·s': 'Н·с', 'N·m²/kg²': 'Н·м²/кг²',
    J: 'Дж', mJ: 'мДж', kJ: 'кДж', MJ: 'МДж', Wh: 'Вт·ч', kWh: 'кВт·ч', cal: 'кал', kcal: 'ккал', eV: 'эВ',
    W: 'Вт', kW: 'кВт', MW: 'МВт', 'Pa·s': 'Па·с', 'mPa·s': 'мПа·с', 'mN/m': 'мН/м',
    '1/GPa': '1/ГПа', '1/Pa': '1/Па', '1/bar': '1/бар', 'kg·m²': 'кг·м²', 'g·cm²': 'г·см²', 'kg·m²/s': 'кг·м²/с', 'J·s': 'Дж·с',
    '1/K': '1/К', '10⁻⁶/K': '10⁻⁶/К', 'J/(kg·K)': 'Дж/(кг·К)', 'kJ/(kg·K)': 'кДж/(кг·К)', 'J/kg': 'Дж/кг',
    'kJ/kg': 'кДж/кг', 'MJ/kg': 'МДж/кг', 'g/mol': 'г/моль', 'kg/mol': 'кг/моль', 'J/(mol·K)': 'Дж/(моль·К)',
    'J/K': 'Дж/К', 'W/(m·K)': 'Вт/(м·К)', '1/m³': '1/м³', '1/cm³': '1/см³',
    C: 'Кл', mC: 'мКл', 'µC': 'мкКл', nC: 'нКл', A: 'А', mA: 'мА', kA: 'кА', V: 'В', mV: 'мВ', kV: 'кВ',
    'Ω': 'Ом', 'kΩ': 'кОм', 'MΩ': 'МОм', 'Ω·m': 'Ом·м', 'Ω·mm²/m': 'Ом·мм²/м', 'V/m': 'В/м', 'kV/m': 'кВ/м',
    F: 'Ф', mF: 'мФ', 'µF': 'мкФ', nF: 'нФ', pF: 'пФ', 'F/m': 'Ф/м',
    T: 'Тл', mT: 'мТл', 'µT': 'мкТл', G: 'Гс', Wb: 'Вб', mWb: 'мВб', 'µWb': 'мкВб', H: 'Гн', mH: 'мГн', 'µH': 'мкГн',
    'N/A²': 'Н/А²', 'A/s': 'А/с',
    MHz: 'МГц', GHz: 'ГГц', nm: 'нм', 'µm': 'мкм', 'W/m²': 'Вт/м²', 'kW/m²': 'кВт/м²', 'mW/cm²': 'мВт/см²',
    dpt: 'дптр', THz: 'ТГц', pm: 'пм', keV: 'кэВ', MeV: 'МэВ', u: 'а.е.м.', 'eV·s': 'эВ·с',
    Bq: 'Бк', kBq: 'кБк', MBq: 'МБк', GBq: 'ГБк', Ci: 'Ки', '1/s': '1/с', '1/h': '1/ч', '1/m': '1/м', '1/cm': '1/см', '1/mm': '1/мм', 'W/(m²·K⁴)': 'Вт/(м²·К⁴)', 'm·K': 'м·К' };
  function natpisJed(id) {
    if (JED_NATPIS[id]) return tekst(JED_NATPIS[id]);
    if (JEZIK === 'ru' && JED_RU[id]) return JED_RU[id];
    return id;
  }
  function uSI(x, j) { return x * j[1] + (j[2] || 0); }
  function izSI(x, j) { return (x - (j[2] || 0)) / j[1]; }
  // Broj za polje za unos: bez razdvajanja hiljada, decimalni separator jezika
  function zaPolje(x) {
    if (typeof x !== 'number' || !isFinite(x)) return '';
    var t = String(Number(x.toPrecision(8)));
    return t.replace('.', DEC);
  }

  // ---------- boje ----------
  function svetlije(hex, udeo) {
    var n = parseInt(hex.replace('#', ''), 16);
    var r = (n >> 16) & 255, g = (n >> 8) & 255, b = n & 255;
    r = Math.round(r + (255 - r) * udeo); g = Math.round(g + (255 - g) * udeo); b = Math.round(b + (255 - b) * udeo);
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }
  var koren_el = document.documentElement;
  koren_el.lang = JEZIK;
  if (TAMNO) koren_el.classList.add('tamno');
  koren_el.style.setProperty('--akcenat', BOJA);
  // Pozadina u blagoj nijansi boje oblasti (šalje je aplikacija)
  if (p.get('pozadina')) koren_el.style.setProperty('--pozadina', p.get('pozadina'));
  if (TAMNO) koren_el.style.setProperty('--akcenat-tekst', svetlije(BOJA, 0.5));
  // Svetla ispuna figura na crtežima (u tamnoj temi providna boja oblasti)
  koren_el.style.setProperty('--lik-ispuna', TAMNO ? BOJA + '40' : svetlije(BOJA, 0.86));
  koren_el.style.setProperty('--lik-linija', TAMNO ? svetlije(BOJA, 0.35) : BOJA);

  // ---------- prikaz ----------
  var main = document.getElementById('sadrzaj');
  var kasnjenje = 0;
  function dodaj(e) {
    e.classList.add('blok');
    e.style.animationDelay = kasnjenje + 'ms';
    kasnjenje += 60;
    main.appendChild(e);
    return e;
  }

  function prikaziFormule(tema) {
    if (tema.opis) dodaj(el('p', 'opis', tekst(tema.opis)));
    if (tema.crtez) {
      // Crtež figure sa oznakama (SVG iz naših assets fajlova)
      var c = el('section', 'kartica crtez');
      c.innerHTML = tekst(tema.crtez); // isti crtež ili poseban za svaki jezik
      dodaj(c);
    }
    tema.formule.forEach(function (f) {
      var k = el('section', 'kartica');
      k.appendChild(el('div', 'naslov', tekst(f.naslov)));
      // Formule sa više delova ("..., \quad ...") prikazujemo jednu ispod druge da stanu na uzak ekran
      tekst(f.latex).split(/,\s*\\quad\s*/).forEach(function (deo) {
        var fo = el('div', 'formula');
        latex(fo, deo, true);
        k.appendChild(fo);
        sabijene.push(fo);
      });
      if (f.objasnjenje) k.appendChild(el('p', 'objasnjenje', tekst(f.objasnjenje)));
      dodaj(k);
    });
  }

  // Ako je formula šira od ekrana, smanji joj slova (najviše do 60%)
  var sabijene = [];
  function uklopi() {
    sabijene.forEach(function (fo) {
      var kx = fo.querySelector('.katex');
      if (!kx) return;
      kx.style.fontSize = '';
      var visak = fo.scrollWidth / fo.clientWidth;
      if (visak > 1.001) kx.style.fontSize = (1.32 / visak > 0.8 ? 1.32 / visak : 0.8).toFixed(3) + 'em';
    });
  }
  window.addEventListener('resize', uklopi);

  function prikaziKalkulator(kal) {
    var ulazi = kal.ulazi || [];
    var imena = ulazi.map(function (u) { return u.id; });
    var izlazi = (kal.izlazi || []).map(function (iz) {
      var o = { def: iz, tip: iz.tip || (iz.brojilac ? 'razlomak' : 'broj') };
      if (o.tip === 'razlomak') {
        o.br = prevedi(iz.brojilac, imena);
        o.im = prevedi(iz.imenilac, imena);
      } else {
        o.f = prevedi(iz.izraz, imena);
      }
      return o;
    });

    var k = el('section', 'kalkulator');
    k.appendChild(el('h2', null, tekst(UI.izracunaj)));
    if (kal.legenda) {
      var lg = el('div', 'legenda');
      latex(lg, tekst(kal.legenda), false);
      k.appendChild(lg);
    }

    var polja = {};
    ulazi.forEach(function (u) {
      var red = el('div', 'ulaz');
      var lab = el('label');
      var id = 'u_' + u.id;
      lab.htmlFor = id;
      var oz = tekst(u.oznaka);
      if (oz) { var s = el('span', 'oznaka'); latex(s, oz + ' =', false); lab.appendChild(s); }
      var ime = tekst(u.naziv);
      if (ime) lab.appendChild(el('span', 'ime', ime));
      var inp = el('input');
      inp.id = id;
      inp.type = 'text';
      inp.inputMode = u.ceo ? 'numeric' : 'decimal';
      inp.autocomplete = 'off';
      inp.value = String(u.pocetna).replace('.', DEC);
      inp.addEventListener('input', izracunaj);
      polja[u.id] = inp;
      red.appendChild(lab);
      red.appendChild(inp);
      k.appendChild(red);
    });

    var grid = el('div', 'rezultati');
    var prikazi = izlazi.map(function (o) {
      var r = el('div', 'rezultat');
      if (izlazi.length === 1 || o.tip === 'tekst') r.classList.add('siroko');
      r.appendChild(el('span', 'ime', tekst(o.def.naziv)));
      var v = el('span', 'vrednost');
      r.appendChild(v);
      var pr = null;
      if (o.tip === 'razlomak') { pr = el('span', 'priblizno'); r.appendChild(pr); }
      grid.appendChild(r);
      return { v: v, pr: pr };
    });
    k.appendChild(grid);
    // Ako u nekom redu ostane jedan uzak rezultat, raširi ga preko cele širine
    var uski = [].filter.call(grid.children, function (c) { return !c.classList.contains('siroko'); });
    if (uski.length % 2 === 1) uski[uski.length - 1].classList.add('siroko');
    dodaj(k);

    function izracunaj() {
      var vr = {}, ok = true;
      ulazi.forEach(function (u) {
        var x = procitaj(polja[u.id].value);
        if (!isFinite(x) || (u.ceo && !Number.isInteger(x))) ok = false;
        vr[u.id] = x;
      });
      izlazi.forEach(function (o, i) {
        var mesto = prikazi[i];
        if (!ok) { mesto.v.textContent = '–'; if (mesto.pr) mesto.pr.textContent = ''; return; }
        if (o.tip === 'razlomak') {
          var a = o.br(vr), b = o.im(vr);
          if (!isFinite(a) || !isFinite(b) || b === 0) { mesto.v.textContent = '–'; mesto.pr.textContent = ''; return; }
          if (Number.isInteger(a) && Number.isInteger(b)) {
            var g = nzd(a, b) || 1;
            a /= g; b /= g;
            if (b < 0) { a = -a; b = -b; }
            var znak = a < 0 ? '-' : '';
            if (b === 1) latex(mesto.v, znak + Math.abs(a), false);
            else latex(mesto.v, znak + '\\dfrac{' + Math.abs(a) + '}{' + b + '}', false);
            mesto.pr.textContent = b === 1 ? '' : '≈ ' + broj(a / b);
          } else {
            mesto.v.textContent = broj(a / b);
            mesto.pr.textContent = '';
          }
        } else if (o.tip === 'tekst') {
          mesto.v.textContent = String(o.f(vr));
        } else if (o.tip === 'stepen') {
          var st = o.f(vr);
          mesto.v.textContent = isFinite(st) ? broj(st) + '°' : '–';
        } else if (o.tip === 'pi') {
          // Ugao kao razlomak od π, npr. 45° → π/4
          var q = o.f(vr), nadjen = false;
          if (isFinite(q)) {
            for (var im = 1; im <= 360 && !nadjen; im++) {
              var br = Math.round(q * im);
              if (Math.abs(q - br / im) < 1e-9) {
                nadjen = true;
                var znakPi = br < 0 ? '-' : '', bb = Math.abs(br);
                var brojilac = bb === 0 ? '0' : (bb === 1 ? '\\pi' : bb + '\\pi');
                latex(mesto.v, bb === 0 ? '0' : znakPi + (im === 1 ? brojilac : '\\dfrac{' + brojilac + '}{' + im + '}'), false);
              }
            }
          }
          if (!nadjen) mesto.v.textContent = isFinite(q) ? broj(q) + 'π' : '–';
        } else if (o.def.decimale !== undefined) {
          var x = o.f(vr);
          mesto.v.textContent = isFinite(x) ? new Intl.NumberFormat(LOKAL, {
            minimumFractionDigits: o.def.decimale, maximumFractionDigits: o.def.decimale }).format(x) : '–';
        } else {
          mesto.v.textContent = broj(o.f(vr));
        }
      });
    }
    izracunaj();
  }

  // Kalkulator za fiziku: korisnik bira formulu i nepoznatu, uz svaku veličinu bira jedinicu.
  // Računa se u SI; vrednosti ostaju zapamćene pri promeni formule ili nepoznate.
  function prikaziResavac(kal) {
    var vel = kal.velicine || {};
    var vr = {}, jedIdx = {};
    Object.keys(vel).forEach(function (id) {
      var v = vel[id], lista = JED[v.vrsta] || JED.bez;
      vr[id] = v.pocetna !== undefined ? v.pocetna : NaN;
      jedIdx[id] = 0;
      if (v.jed) lista.forEach(function (j, i) { if (j[0] === v.jed) jedIdx[id] = i; });
    });
    var rucnaJed = {}; // jedinica rezultata koju je korisnik sam izabrao
    var autoJed = {};  // jedinica koju je kalkulator izabrao za prikaz rezultata
    function jedinice(id) { return JED[(vel[id] || {}).vrsta] || JED.bez; }
    // Za rezultat bira jedinicu u kojoj je broj čitljiv (1 ≤ |x| < 1000), osim ako je korisnik izabrao svoju.
    // Polja za unos zadržavaju svoje jedinice.
    function izaberiJedRez(id, x) {
      var lista = jedinice(id);
      autoJed[id] = jedIdx[id];
      if (rucnaJed[id] || !isFinite(x) || x === 0 || lista.length < 2) return;
      if (lista.some(function (j) { return j[2]; })) return; // temperatura
      var dobra = function (i) { var a = Math.abs(izSI(x, lista[i])) * (1 + 1e-9); return a >= 1 && a < 1000; };
      if (dobra(jedIdx[id])) return;
      for (var i = 0; i < lista.length; i++) if (dobra(i)) { autoJed[id] = i; return; }
    }
    function jed(id) { return jedinice(id)[jedIdx[id]]; }

    var jednacine = (kal.jednacine || []).map(function (j) {
      var imena = j.promenljive || Object.keys(j.resenja);
      var f = {};
      Object.keys(j.resenja).forEach(function (n) { f[n] = prevedi(j.resenja[n], imena, FIZ); });
      return { def: j, imena: imena, f: f, nep: j.trazi || Object.keys(j.resenja)[0] };
    });
    if (!jednacine.length) return;
    var tekuca = 0;

    var k = el('section', 'kalkulator resavac');
    k.appendChild(el('h2', null, tekst(UI.izracunaj)));
    var telo = el('div', 'telo');
    k.appendChild(telo);
    dodaj(k);

    function izborJedinica(id, naPromenu) {
      var lista = jedinice(id);
      if (lista.length < 2) {
        var natpis = natpisJed(lista[0][0]);
        // Neimenovana veličina (npr. koeficijent trenja): bez oznake jedinice
        return el('span', natpis ? 'jedinica' : 'jedinica prazna', natpis);
      }
      var sel = el('select', 'jedinica');
      lista.forEach(function (j, i) {
        var o = el('option', null, natpisJed(j[0]));
        o.value = i;
        sel.appendChild(o);
      });
      sel.value = jedIdx[id];
      sel.addEventListener('change', function () { jedIdx[id] = Number(sel.value); naPromenu(); });
      return sel;
    }

    function cipovi(naslov, stavke) {
      telo.appendChild(el('div', 'grupa-naslov', tekst(naslov)));
      var red = el('div', 'cipovi');
      stavke.forEach(function (st) {
        var b = el('button', 'cip' + (st.aktivan ? ' aktivan' : ''));
        b.type = 'button';
        latex(b, st.latex, false);
        b.addEventListener('click', st.klik);
        red.appendChild(b);
      });
      telo.appendChild(red);
    }

    function crtaj() {
      telo.innerHTML = '';
      var e = jednacine[tekuca];
      if (jednacine.length > 1) {
        cipovi(UI.formula, jednacine.map(function (j, i) {
          return { latex: tekst(j.def.latex), aktivan: i === tekuca, klik: function () { tekuca = i; crtaj(); } };
        }));
      }
      cipovi(UI.trazi, Object.keys(e.def.resenja).map(function (id) {
        return { latex: tekst(vel[id].oznaka), aktivan: id === e.nep, klik: function () { e.nep = id; crtaj(); } };
      }));

      var polja = {};
      e.imena.filter(function (id) { return id !== e.nep; }).forEach(function (id) {
        var v = vel[id];
        var red = el('div', 'ulaz');
        var lab = el('label');
        lab.htmlFor = 'f_' + id;
        var s = el('span', 'oznaka'); latex(s, tekst(v.oznaka) + ' =', false); lab.appendChild(s);
        lab.appendChild(el('span', 'ime', tekst(v.naziv)));
        var inp = el('input');
        inp.id = 'f_' + id;
        inp.type = 'text';
        inp.inputMode = 'decimal';
        inp.autocomplete = 'off';
        inp.value = zaPolje(izSI(vr[id], jed(id)));
        function procitajPolje() {
          var x = procitaj(inp.value);
          vr[id] = isFinite(x) ? uSI(x, jed(id)) : NaN;
          racunaj();
        }
        inp.addEventListener('input', procitajPolje);
        polja[id] = inp;
        red.appendChild(lab);
        red.appendChild(inp);
        // Promena jedinice: uneti broj ostaje, menja se njegovo značenje (72 → 72 km/h)
        red.appendChild(izborJedinica(id, procitajPolje));
        telo.appendChild(red);
      });

      var nv = vel[e.nep];
      var rez = el('div', 'rezultat siroko fizrez');
      rez.appendChild(el('span', 'ime', tekst(nv.naziv)));
      var red = el('div', 'red');
      var oz = el('span', 'oznaka'); latex(oz, tekst(nv.oznaka) + ' =', false);
      var vrednost = el('span', 'vrednost');
      red.appendChild(oz);
      red.appendChild(vrednost);
      var izborRez = izborJedinica(e.nep, function () { rucnaJed[e.nep] = true; prikaziRezultat(); });
      if (izborRez.tagName === 'SELECT') {
        // izbor jedinice rezultata je zaseban od jedinice polja za unos
        izborRez.addEventListener('change', function () { autoJed[e.nep] = jedIdx[e.nep]; });
      }
      red.appendChild(izborRez);
      rez.appendChild(red);
      telo.appendChild(rez);
      var poruka = el('p', 'napomena');
      telo.appendChild(poruka);

      var rezultat = NaN;
      function prikaziRezultat() {
        izaberiJedRez(e.nep, rezultat);
        if (izborRez.tagName === 'SELECT') izborRez.value = autoJed[e.nep];
        vrednost.textContent = isFinite(rezultat) ? broj(izSI(rezultat, jedinice(e.nep)[autoJed[e.nep]])) : '–';
      }
      function racunaj() {
        var ok = e.imena.every(function (id) { return id === e.nep || isFinite(vr[id]); });
        var x = ok ? e.f[e.nep](vr) : NaN;
        if (typeof x !== 'number' || (nv.poz && !(x > 0)) || (nv.nenegativna && !(x >= 0))) x = NaN;
        rezultat = x;
        if (isFinite(x)) vr[e.nep] = x;
        prikaziRezultat();
        var nap = e.def.napomene && e.def.napomene[e.nep];
        poruka.textContent = ok && !isFinite(x) ? tekst(UI.nemaResenja) : (nap ? tekst(nap) : '');
        poruka.style.display = poruka.textContent ? '' : 'none';
      }
      racunaj();
    }
    crtaj();
  }

  function greska() {
    main.appendChild(el('p', 'opis', tekst(UI.greska)));
  }

  fetch('../oblasti/' + encodeURIComponent(OBLAST) + '.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      var tema = (d.teme || []).filter(function (t) { return t.id === TEMA; })[0];
      if (!tema) return greska();
      document.title = tekst(tema.naziv);
      if (tema.element && window.Hemija) {
        // Hemija: kartica elementa periodnog sistema
        Hemija.prikaziElement(main, tema, d.teme, JEZIK, dodaj);
        return;
      }
      prikaziFormule(tema);
      uklopi();
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(uklopi);
      if (tema.kalkulator) {
        if (tema.kalkulator.tip === 'resi') prikaziResavac(tema.kalkulator);
        else prikaziKalkulator(tema.kalkulator);
      }
    })
    .catch(greska);
})();
