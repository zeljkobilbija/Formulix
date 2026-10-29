// Formulix – hemija: periodni sistem (sistem.html) i kartica elementa (u tema.html).
// Podaci: assets/oblasti/hemija.json (pravi ga alati/hemija/gen_hemija.py).
(function () {
  'use strict';

  var VRSTE = [
    ['alkalni', { sr: 'Alkalni metali', en: 'Alkali metals', it: 'Metalli alcalini', fr: 'Métaux alcalins', es: 'Metales alcalinos', de: 'Alkalimetalle', pt: 'Metais alcalinos', ru: 'Щелочные металлы' }],
    ['zemnoalkalni', { sr: 'Zemnoalkalni metali', en: 'Alkaline earth metals', it: 'Metalli alcalino-terrosi', fr: 'Métaux alcalino-terreux', es: 'Metales alcalinotérreos', de: 'Erdalkalimetalle', pt: 'Metais alcalino-terrosos', ru: 'Щёлочноземельные металлы' }],
    ['prelazni', { sr: 'Prelazni metali', en: 'Transition metals', it: 'Metalli di transizione', fr: 'Métaux de transition', es: 'Metales de transición', de: 'Übergangsmetalle', pt: 'Metais de transição', ru: 'Переходные металлы' }],
    ['ostali_metali', { sr: 'Ostali metali', en: 'Post-transition metals', it: 'Metalli post-transizionali', fr: 'Métaux pauvres', es: 'Metales del bloque p', de: 'Metalle der p-Gruppe', pt: 'Metais pós-transição', ru: 'Постпереходные металлы' }],
    ['metaloid', { sr: 'Metaloidi', en: 'Metalloids', it: 'Semimetalli', fr: 'Métalloïdes', es: 'Metaloides', de: 'Halbmetalle', pt: 'Semimetais', ru: 'Полуметаллы' }],
    ['nemetal', { sr: 'Nemetali', en: 'Nonmetals', it: 'Non metalli', fr: 'Non-métaux', es: 'No metales', de: 'Nichtmetalle', pt: 'Não metais', ru: 'Неметаллы' }],
    ['halogen', { sr: 'Halogeni elementi', en: 'Halogens', it: 'Alogeni', fr: 'Halogènes', es: 'Halógenos', de: 'Halogene', pt: 'Halogênios', ru: 'Галогены' }],
    ['plemeniti_gas', { sr: 'Plemeniti gasovi', en: 'Noble gases', it: 'Gas nobili', fr: 'Gaz nobles', es: 'Gases nobles', de: 'Edelgase', pt: 'Gases nobres', ru: 'Благородные газы' }],
    ['lantanoid', { sr: 'Lantanoidi', en: 'Lanthanides', it: 'Lantanidi', fr: 'Lanthanides', es: 'Lantánidos', de: 'Lanthanoide', pt: 'Lantanídeos', ru: 'Лантаноиды' }],
    ['aktinoid', { sr: 'Aktinoidi', en: 'Actinides', it: 'Attinidi', fr: 'Actinides', es: 'Actínidos', de: 'Actinoide', pt: 'Actinídeos', ru: 'Актиноиды' }]
  ];

  var T = {
    uputstvo: { sr: 'Dodirni element za detalje. Tabela se pomera levo-desno.', en: 'Tap an element for details. Swipe the table sideways.', it: 'Tocca un elemento per i dettagli. Scorri la tavola lateralmente.', fr: 'Touchez un élément pour les détails. Faites défiler le tableau.', es: 'Toca un elemento para ver detalles. Desliza la tabla.', de: 'Tippe auf ein Element für Details. Die Tabelle lässt sich seitlich wischen.', pt: 'Toque num elemento para ver detalhes. Deslize a tabela.', ru: 'Нажмите на элемент, чтобы увидеть подробности. Таблицу можно прокручивать.' },
    legenda: { sr: 'Dodirni vrstu da je istakneš', en: 'Tap a category to highlight it', it: 'Tocca una categoria per evidenziarla', fr: 'Touchez une famille pour la mettre en évidence', es: 'Toca una categoría para resaltarla', de: 'Tippe auf eine Kategorie zum Hervorheben', pt: 'Toque numa categoria para destacá-la', ru: 'Нажмите на категорию, чтобы выделить её' },
    osnovno: { sr: 'Osnovno', en: 'Basics', it: 'Dati di base', fr: 'Généralités', es: 'Datos básicos', de: 'Grunddaten', pt: 'Dados básicos', ru: 'Основное' },
    elektroni: { sr: 'Elektroni i veze', en: 'Electrons and bonding', it: 'Elettroni e legami', fr: 'Électrons et liaisons', es: 'Electrones y enlaces', de: 'Elektronen und Bindung', pt: 'Elétrons e ligações', ru: 'Электроны и связи' },
    fizicka: { sr: 'Fizička svojstva', en: 'Physical properties', it: 'Proprietà fisiche', fr: 'Propriétés physiques', es: 'Propiedades físicas', de: 'Physikalische Eigenschaften', pt: 'Propriedades físicas', ru: 'Физические свойства' },
    z: { sr: 'Atomski broj', en: 'Atomic number', it: 'Numero atomico', fr: 'Numéro atomique', es: 'Número atómico', de: 'Ordnungszahl', pt: 'Número atômico', ru: 'Атомный номер' },
    masa: { sr: 'Relativna atomska masa', en: 'Relative atomic mass', it: 'Massa atomica relativa', fr: 'Masse atomique relative', es: 'Masa atómica relativa', de: 'Relative Atommasse', pt: 'Massa atômica relativa', ru: 'Относительная атомная масса' },
    izotop: { sr: 'U zagradi je maseni broj najstabilnijeg izotopa.', en: 'In brackets: mass number of the most stable isotope.', it: 'Tra parentesi: numero di massa dell’isotopo più stabile.', fr: 'Entre crochets : nombre de masse de l’isotope le plus stable.', es: 'Entre corchetes: número másico del isótopo más estable.', de: 'In Klammern: Massenzahl des stabilsten Isotops.', pt: 'Entre colchetes: número de massa do isótopo mais estável.', ru: 'В скобках — массовое число самого устойчивого изотопа.' },
    grupa: { sr: 'Grupa', en: 'Group', it: 'Gruppo', fr: 'Groupe', es: 'Grupo', de: 'Gruppe', pt: 'Grupo', ru: 'Группа' },
    perioda: { sr: 'Perioda', en: 'Period', it: 'Periodo', fr: 'Période', es: 'Periodo', de: 'Periode', pt: 'Período', ru: 'Период' },
    blok: { sr: 'Blok', en: 'Block', it: 'Blocco', fr: 'Bloc', es: 'Bloque', de: 'Block', pt: 'Bloco', ru: 'Блок' },
    vrsta: { sr: 'Vrsta', en: 'Category', it: 'Categoria', fr: 'Famille', es: 'Categoría', de: 'Kategorie', pt: 'Categoria', ru: 'Категория' },
    konf: { sr: 'Elektronska konfiguracija', en: 'Electron configuration', it: 'Configurazione elettronica', fr: 'Configuration électronique', es: 'Configuración electrónica', de: 'Elektronenkonfiguration', pt: 'Configuração eletrônica', ru: 'Электронная конфигурация' },
    ox: { sr: 'Oksidaciona stanja', en: 'Oxidation states', it: 'Stati di ossidazione', fr: 'États d’oxydation', es: 'Estados de oxidación', de: 'Oxidationsstufen', pt: 'Estados de oxidação', ru: 'Степени окисления' },
    en: { sr: 'Elektronegativnost (Poling)', en: 'Electronegativity (Pauling)', it: 'Elettronegatività (Pauling)', fr: 'Électronégativité (Pauling)', es: 'Electronegatividad (Pauling)', de: 'Elektronegativität (Pauling)', pt: 'Eletronegatividade (Pauling)', ru: 'Электроотрицательность (Полинг)' },
    ie: { sr: 'Prva energija jonizacije', en: 'First ionization energy', it: 'Prima energia di ionizzazione', fr: 'Première énergie d’ionisation', es: 'Primera energía de ionización', de: 'Erste Ionisierungsenergie', pt: 'Primeira energia de ionização', ru: 'Первая энергия ионизации' },
    ea: { sr: 'Afinitet prema elektronu', en: 'Electron affinity', it: 'Affinità elettronica', fr: 'Affinité électronique', es: 'Afinidad electrónica', de: 'Elektronenaffinität', pt: 'Afinidade eletrônica', ru: 'Сродство к электрону' },
    r: { sr: 'Atomski poluprečnik (van der Valsov)', en: 'Atomic radius (van der Waals)', it: 'Raggio atomico (van der Waals)', fr: 'Rayon atomique (van der Waals)', es: 'Radio atómico (van der Waals)', de: 'Atomradius (Van-der-Waals)', pt: 'Raio atômico (van der Waals)', ru: 'Атомный радиус (ван-дер-ваальсов)' },
    stanje: { sr: 'Agregatno stanje (25 °C)', en: 'State at 25 °C', it: 'Stato a 25 °C', fr: 'État à 25 °C', es: 'Estado a 25 °C', de: 'Aggregatzustand (25 °C)', pt: 'Estado a 25 °C', ru: 'Агрегатное состояние (25 °C)' },
    s: { sr: 'čvrsto', en: 'solid', it: 'solido', fr: 'solide', es: 'sólido', de: 'fest', pt: 'sólido', ru: 'твёрдое' },
    l: { sr: 'tečno', en: 'liquid', it: 'liquido', fr: 'liquide', es: 'líquido', de: 'flüssig', pt: 'líquido', ru: 'жидкое' },
    g: { sr: 'gasovito', en: 'gas', it: 'gassoso', fr: 'gazeux', es: 'gaseoso', de: 'gasförmig', pt: 'gasoso', ru: 'газообразное' },
    predvidjeno: { sr: 'predviđeno', en: 'predicted', it: 'previsto', fr: 'prédit', es: 'previsto', de: 'vorhergesagt', pt: 'previsto', ru: 'предсказано' },
    tt: { sr: 'Tačka topljenja', en: 'Melting point', it: 'Punto di fusione', fr: 'Point de fusion', es: 'Punto de fusión', de: 'Schmelzpunkt', pt: 'Ponto de fusão', ru: 'Температура плавления' },
    tk: { sr: 'Tačka ključanja', en: 'Boiling point', it: 'Punto di ebollizione', fr: 'Point d’ébullition', es: 'Punto de ebullición', de: 'Siedepunkt', pt: 'Ponto de ebulição', ru: 'Температура кипения' },
    sublimacija: { sr: 'Na normalnom pritisku sublimira (prelazi direktno u gas); tačka topljenja važi pod povišenim pritiskom.', en: 'At normal pressure it sublimes (turns directly into gas); the melting point applies under higher pressure.', it: 'A pressione normale sublima; il punto di fusione vale a pressione più alta.', fr: 'À pression normale il se sublime ; le point de fusion vaut sous pression plus élevée.', es: 'A presión normal sublima; el punto de fusión vale a mayor presión.', de: 'Bei Normaldruck sublimiert es; der Schmelzpunkt gilt bei höherem Druck.', pt: 'À pressão normal sublima; o ponto de fusão vale sob pressão maior.', ru: 'При нормальном давлении возгоняется; температура плавления указана для повышенного давления.' },
    gustina: { sr: 'Gustina', en: 'Density', it: 'Densità', fr: 'Masse volumique', es: 'Densidad', de: 'Dichte', pt: 'Densidade', ru: 'Плотность' },
    otkriven: { sr: 'Otkriven', en: 'Discovered', it: 'Scoperto', fr: 'Découvert', es: 'Descubierto', de: 'Entdeckt', pt: 'Descoberto', ru: 'Открыт' },
    antika: { sr: 'poznat od davnina', en: 'known since antiquity', it: 'noto fin dall’antichità', fr: 'connu depuis l’Antiquité', es: 'conocido desde la Antigüedad', de: 'seit der Antike bekannt', pt: 'conhecido desde a Antiguidade', ru: 'известен с древности' },
    godina: { sr: 'godine', en: 'in', it: 'nel', fr: 'en', es: 'en', de: 'im Jahr', pt: 'em', ru: 'в' },
    izvor: { sr: 'Izvor podataka: PubChem (NIH), atomske mase: IUPAC.', en: 'Data: PubChem (NIH); atomic masses: IUPAC.', it: 'Dati: PubChem (NIH); masse atomiche: IUPAC.', fr: 'Données : PubChem (NIH) ; masses atomiques : IUPAC.', es: 'Datos: PubChem (NIH); masas atómicas: IUPAC.', de: 'Daten: PubChem (NIH); Atommassen: IUPAC.', pt: 'Dados: PubChem (NIH); massas atômicas: IUPAC.', ru: 'Данные: PubChem (NIH); атомные массы: IUPAC.' }
  };
  var JED_RU = { eV: 'эВ', pm: 'пм', 'g/cm³': 'г/см³', 'g/L': 'г/л', K: 'К' };

  function napravi(jezik) {
    function tekst(v) {
      if (v === null || v === undefined) return '';
      if (typeof v === 'string') return v;
      return v[jezik] !== undefined ? v[jezik] : (v.en || v.sr || '');
    }
    function jed(j) { return jezik === 'ru' && JED_RU[j] ? JED_RU[j] : j; }
    var LOKAL = { sr: 'sr-Latn-RS', en: 'en', it: 'it', fr: 'fr', es: 'es', de: 'de', pt: 'pt', ru: 'ru' }[jezik] || 'en';
    var fmt = new Intl.NumberFormat(LOKAL, { maximumFractionDigits: 6, useGrouping: false });
    function broj(x) { return fmt.format(x).replace('-', '−'); }
    var DEC = fmt.format(1.5).charAt(1);
    // IUPAC vrednost kao tekst, da ostanu i nule na kraju (127,60)
    function masa(e) { return e.masaIzotop ? '[' + e.masa + ']' : e.masa.replace('.', DEC); }
    function decimale(x) { var t = String(x); var i = t.indexOf('.'); return i < 0 ? 0 : t.length - i - 1; }
    function nazivVrste(k) { for (var i = 0; i < VRSTE.length; i++) if (VRSTE[i][0] === k) return tekst(VRSTE[i][1]); return k; }
    return { tekst: tekst, jed: jed, broj: broj, masa: masa, nazivVrste: nazivVrste, decimale: decimale };
  }

  function el(tag, klasa, sadrzaj) {
    var e = document.createElement(tag);
    if (klasa) e.className = klasa;
    if (sadrzaj !== undefined && sadrzaj !== null) e.textContent = sadrzaj;
    return e;
  }

  // Link ka kartici elementa; aplikacija presreće adresu /element/<Z>
  function adresaElementa(z) { return '/element/' + z; }

  // ---------- periodni sistem ----------
  function prikaziSistem(koren, teme, jezik) {
    var h = napravi(jezik);
    koren.appendChild(el('p', 'opis', h.tekst(T.uputstvo)));

    var okvir = el('div', 'ps-okvir');
    var tabela = el('div', 'ps-tabela');
    // brojevi grupa (red 1) i perioda (kolona 1)
    for (var g = 1; g <= 18; g++) {
      var bg = el('div', 'ps-oznaka', String(g));
      bg.style.gridRow = 1; bg.style.gridColumn = g + 1;
      tabela.appendChild(bg);
    }
    for (var p = 1; p <= 7; p++) {
      var bp = el('div', 'ps-oznaka', String(p));
      bp.style.gridRow = p + 1; bp.style.gridColumn = 1;
      tabela.appendChild(bp);
    }
    // mesta za lantanoide i aktinoide u glavnoj tabeli
    [[7, 'lantanoid', '57–71'], [8, 'aktinoid', '89–103']].forEach(function (m) {
      var c = el('div', 'ps-polje ps-mesto v-' + m[1], m[2]);
      c.style.gridRow = m[0]; c.style.gridColumn = 4;
      c.dataset.vrsta = m[1];
      tabela.appendChild(c);
    });
    teme.forEach(function (t) {
      var e = t.element;
      var a = el('a', 'ps-polje v-' + e.vrsta);
      a.href = adresaElementa(e.z);
      a.dataset.vrsta = e.vrsta;
      // red 1 su brojevi grupa; f-blok (redovi 9 i 10) ide ispod, red 9 mreže ostaje prazan kao razmak
      a.style.gridRow = e.red + 1;
      a.style.gridColumn = e.kolona + 1;
      a.setAttribute('aria-label', h.tekst(t.naziv));
      a.appendChild(el('span', 'ps-z', String(e.z)));
      a.appendChild(el('span', 'ps-s', e.simbol));
      a.appendChild(el('span', 'ps-m', h.masa(e)));
      tabela.appendChild(a);
    });
    okvir.appendChild(tabela);
    koren.appendChild(okvir);

    // legenda: dodir ističe jednu vrstu
    var leg = el('section', 'kartica ps-legenda');
    leg.appendChild(el('div', 'naslov', h.tekst(T.legenda)));
    var cipovi = el('div', 'ps-cipovi');
    var aktivna = null;
    VRSTE.forEach(function (v) {
      var b = el('button', 'ps-cip v-' + v[0], h.tekst(v[1]));
      b.type = 'button';
      b.addEventListener('click', function () {
        aktivna = aktivna === v[0] ? null : v[0];
        tabela.classList.toggle('istaknuto', !!aktivna);
        [].forEach.call(tabela.querySelectorAll('.ps-polje'), function (c) {
          c.classList.toggle('ugaseno', !!aktivna && c.dataset.vrsta !== aktivna);
        });
        [].forEach.call(cipovi.children, function (c) { c.classList.toggle('aktivan', c === b && !!aktivna); });
      });
      cipovi.appendChild(b);
    });
    leg.appendChild(cipovi);
    koren.appendChild(leg);
    koren.appendChild(el('p', 'izvor', h.tekst(T.izvor)));
  }

  // ---------- kartica elementa ----------
  var SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  // "[Ar] 3d6 4s2" → "[Ar] 3d⁶ 4s²"
  function konfiguracija(s) {
    return s.split(' ').map(function (o) {
      if (o.charAt(0) === '[') return o;
      return o.slice(0, 2) + o.slice(2).replace(/\d/g, function (c) { return SUP[c]; });
    }).join(' ');
  }

  function prikaziElement(koren, tema, sve, jezik, dodaj) {
    var h = napravi(jezik);
    var e = tema.element;

    // glavna kartica: polje sa simbolom i osnovni podaci
    var glava = el('section', 'kartica el-glava');
    var polje = el('div', 'el-polje v-' + e.vrsta);
    polje.appendChild(el('span', 'el-z', String(e.z)));
    polje.appendChild(el('span', 'el-s', e.simbol));
    polje.appendChild(el('span', 'el-m', h.masa(e)));
    glava.appendChild(polje);
    var info = el('div', 'el-info');
    info.appendChild(el('div', 'el-ime', h.tekst(tema.naziv)));
    info.appendChild(el('div', 'el-vrsta v-' + e.vrsta, h.nazivVrste(e.vrsta)));
    var poz = [];
    if (e.grupa) poz.push(h.tekst(T.grupa) + ' ' + e.grupa);
    poz.push(h.tekst(T.perioda) + ' ' + e.perioda);
    poz.push(h.tekst(T.blok) + ' ' + e.blok);
    info.appendChild(el('div', 'el-poz', poz.join(' · ')));
    glava.appendChild(info);
    dodaj(glava);

    function sekcija(naslov, redovi) {
      redovi = redovi.filter(function (r) { return r && r[1] !== null && r[1] !== undefined && r[1] !== ''; });
      if (!redovi.length) return;
      var k = el('section', 'kartica');
      k.appendChild(el('div', 'naslov', h.tekst(naslov)));
      var dl = el('dl', 'el-podaci');
      redovi.forEach(function (r) {
        var red = el('div', 'el-red');
        red.appendChild(el('dt', null, h.tekst(r[0])));
        red.appendChild(el('dd', null, r[1]));
        dl.appendChild(red);
        if (r[2]) dl.appendChild(el('p', 'el-napomena', h.tekst(r[2])));
      });
      k.appendChild(dl);
      dodaj(k);
    }
    function predvidjeno(s, da) { return da ? s + ' (' + h.tekst(T.predvidjeno) + ')' : s; }
    function temp(k) {
      if (k === null || k === undefined) return null;
      // °C sa istim brojem decimala kao izvorni podatak u K (1811 K → 1538 °C)
      var d = Math.min(h.decimale(k), 2), f = Math.pow(10, d);
      var c = Math.round((k - 273.15) * f) / f;
      return h.broj(c) + ' °C (' + h.broj(k) + ' ' + h.jed('K') + ')';
    }
    function sa(x, j) { return x === null || x === undefined ? null : h.broj(x) + ' ' + h.jed(j); }

    sekcija(T.osnovno, [
      [T.z, String(e.z)],
      [T.masa, h.masa(e), e.masaIzotop ? T.izotop : null],
      [T.grupa, e.grupa ? String(e.grupa) : null],
      [T.perioda, String(e.perioda)],
      [T.blok, e.blok],
      [T.vrsta, h.nazivVrste(e.vrsta)]
    ]);
    sekcija(T.elektroni, [
      [T.konf, predvidjeno(konfiguracija(e.konfiguracija), e.konfPredvidjena)],
      [T.ox, e.oksidaciona.length ? e.oksidaciona.join(', ') : null],
      [T.en, e.elektronegativnost === null ? null : h.broj(e.elektronegativnost)],
      [T.ie, sa(e.jonizacija, 'eV')],
      [T.ea, sa(e.afinitet, 'eV')],
      [T.r, sa(e.poluprecnik, 'pm')]
    ]);
    var sublimira = e.topljenje && e.kljucanje && e.topljenje > e.kljucanje;
    var gustina = e.gustina === null ? null :
      (e.stanje === 'g' ? sa(Number((e.gustina * 1000).toPrecision(4)), 'g/L') : sa(e.gustina, 'g/cm³'));
    sekcija(T.fizicka, [
      [T.stanje, predvidjeno(h.tekst(T[e.stanje]), e.stanjePredvidjeno)],
      [T.tt, temp(e.topljenje), sublimira ? T.sublimacija : null],
      [T.tk, temp(e.kljucanje)],
      [T.gustina, gustina],
      [T.otkriven, e.otkriven ? h.tekst(T.godina) + ' ' + e.otkriven : h.tekst(T.antika)]
    ]);

    // prethodni i sledeći element
    var nav = el('nav', 'el-nav');
    [e.z - 1, e.z + 1].forEach(function (z, i) {
      var t = sve.filter(function (x) { return x.element.z === z; })[0];
      if (!t) { nav.appendChild(el('span', 'el-nav-prazno')); return; }
      var a = el('a', 'el-nav-dugme' + (i ? ' desno' : ''));
      a.href = adresaElementa(z);
      a.appendChild(el('span', 'el-nav-strela', i ? '→' : '←'));
      var tx = el('span', 'el-nav-tekst');
      tx.appendChild(el('b', null, t.element.simbol));
      tx.appendChild(el('span', null, h.tekst(t.naziv)));
      if (i) { a.insertBefore(tx, a.firstChild); } else { a.appendChild(tx); }
      nav.appendChild(a);
    });
    dodaj(nav);
    dodaj(el('p', 'izvor', h.tekst(T.izvor)));
  }

  window.Hemija = { prikaziSistem: prikaziSistem, prikaziElement: prikaziElement };
})();
