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
  function prevedi(izraz, promenljive) {
    var imena = promenljive.concat(Object.keys(FUNKCIJE));
    /* eslint-disable no-new-func */
    var f = new Function(imena.join(','), '"use strict"; return (' + izraz + ');');
    return function (vrednosti) {
      var args = promenljive.map(function (k) { return vrednosti[k]; })
        .concat(Object.keys(FUNKCIJE).map(function (k) { return FUNKCIJE[k]; }));
      try { return f.apply(null, args); } catch (e) { return NaN; }
    };
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

  function greska() {
    main.appendChild(el('p', 'opis', tekst(UI.greska)));
  }

  fetch('../oblasti/' + encodeURIComponent(OBLAST) + '.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      var tema = (d.teme || []).filter(function (t) { return t.id === TEMA; })[0];
      if (!tema) return greska();
      document.title = tekst(tema.naziv);
      prikaziFormule(tema);
      uklopi();
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(uklopi);
      if (tema.kalkulator) prikaziKalkulator(tema.kalkulator);
    })
    .catch(greska);
})();
