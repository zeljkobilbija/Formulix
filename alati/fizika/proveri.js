// Za svaku jednačinu: izračunaj nepoznatu, pa svaku drugu promenljivu vrati iz rešenja i uporedi
const d = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
function kvPoz(A,B,C){ if(Math.abs(A)<1e-15){const x=-C/B;return x>0?x:NaN;} const D=B*B-4*A*C; if(D<0)return NaN; const k=Math.sqrt(D); const r=[(-B-k)/(2*A),(-B+k)/(2*A)].filter(x=>x>1e-12); return r.length?Math.min(...r):NaN; }
const F = {sin:Math.sin,cos:Math.cos,tan:Math.tan,asin:Math.asin,acos:Math.acos,sqrt:Math.sqrt,PI:Math.PI,kvPoz,pow:Math.pow,ln:Math.log,atan:Math.atan};
let greske = 0, provere = 0;
for (const t of d.teme) {
  const kal = t.kalkulator, vel = kal.velicine;
  for (const j of kal.jednacine) {
    const imena = j.promenljive || Object.keys(j.resenja);
    const fn = {};
    for (const n of Object.keys(j.resenja)) fn[n] = new Function(...imena, ...Object.keys(F), '"use strict";return (' + j.resenja[n] + ');');
    const call = (n, v) => fn[n](...imena.map(k => v[k]), ...Object.values(F));
    // nasumične pozitivne vrednosti (ugao 10°–40°)
    for (let pokusaj = 0; pokusaj < 20; pokusaj++) {
      const v = {};
      for (const k of imena) v[k] = vel[k].vrsta === 'ugao' ? (10 + Math.random() * 30) * Math.PI / 180 : (vel[k].vrsta === 'bez' ? 0.05 + Math.random() * 0.3 : 0.5 + Math.random() * 10);
      const nep = j.trazi; v[nep] = call(nep, v);
      if (!isFinite(v[nep])) continue;
      for (const k of Object.keys(j.resenja)) {
        if (k === nep) continue;
        const x = call(k, v); provere++;
        if (!(Math.abs(x - v[k]) < 1e-6 * (1 + Math.abs(v[k])))) { greske++; console.log('GRESKA', t.id, j.latex, k, x, v[k]); break; }
      }
    }
  }
}
console.log('provera:', provere, 'gresaka:', greske);
