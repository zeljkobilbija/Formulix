# Generator podataka za hemiju (periodni sistem)

`gen_hemija.py` pravi `app/src/main/assets/oblasti/hemija.json` sa svih 118 elemenata.

Pokretanje (iz ovog foldera):

```
python gen_hemija.py ../../app/src/main/assets/oblasti/hemija.json
```

## Izvori

- `pubchem_elementi.txt`: tabela elemenata iz PubChem-a (NIH, javni podaci):
  elektronska konfiguracija, elektronegativnost, atomski poluprečnik, energija
  jonizacije, afinitet prema elektronu, oksidaciona stanja, agregatno stanje,
  tačke topljenja i ključanja (K), gustina (g/cm³), vrsta, godina otkrića.
- Atomske mase: IUPAC standardne (skraćene) vrednosti, upisane u `gen_hemija.py`
  (`MASE`). U zagradi je maseni broj najstabilnijeg izotopa.
- Nazivi elemenata na 8 jezika su u `gen_hemija.py` (`NAZIVI`).

Položaj u tabeli (grupa, perioda, blok) generator računa iz atomskog broja.

## Prikaz

- `app/src/main/assets/hemija/sistem.html`: periodni sistem
- `app/src/main/assets/hemija/hemija.js` i `hemija.css`: tabela i kartica elementa
- Kartica elementa se otvara u istom ekranu kao formule (`TemaActivity`, oblast `hemija`).
