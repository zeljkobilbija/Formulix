# Generatori sadržaja fizike

Ovde su skripte koje prave JSON fajlove za oblasti fizike u
`app/src/main/assets/oblasti/`. Folder `alati/` ne ulazi u aplikaciju.

## Kako se koristi

1. Izmeni odgovarajući `gen_*.py` (npr. dodaj formulu, ispravi prevod).
2. Pokreni iz ovog foldera:

   ```
   python generisi_sve.py
   ```

   Treba ti Python 3. Ako imaš i Node.js, automatski se proveravaju
   sve formule u kalkulatorima.
3. U Android Studiju pokreni aplikaciju.

Jedan generator možeš pokrenuti i sam:

```
python gen_sile.py ../../app/src/main/assets/oblasti/sile.json
node proveri.js ../../app/src/main/assets/oblasti/sile.json
```

## Fajlovi

| Generator | Oblast |
|---|---|
| gen_kretanje.py | Kretanje |
| gen_sile.py | Sile |
| gen_energija.py | Rad i energija |
| gen_fluidi.py | Fluidi |
| gen_rotacija.py | Rotacija |
| gen_toplota.py | Toplota |
| gen_elektricitet.py | Elektricitet |
| gen_magnetizam.py | Magnetizam |
| gen_talasi.py | Oscilacije i talasi |
| gen_moderna.py | Moderna fizika |
| gen_konstante.py | Konstante |

`proveri.js` za svaku formulu izračuna nepoznatu, pa iz rezultata ponovo
izračuna svaku drugu veličinu i uporedi ih.

## Kako izgleda jedna formula u kalkulatoru

```python
{'latex': r"F = m a",            # prikaz na dugmetu
 'trazi': 'F',                   # šta se traži na početku
 'resenja': {'F': 'm*a',         # rešen oblik za svaku veličinu
             'm': 'F/a',
             'a': 'F/m'}}
```

Veličine (`velicine`) imaju oznaku, naziv na 8 jezika, vrstu jedinice
(`vrsta`, npr. `sila`, `duzina`) i početnu vrednost u SI jedinicama.
Spisak jedinica je u `app/src/main/assets/tema/tema.js` (objekat `JED`).

Napomena: generatori u ovom obliku prave fajlove iz početka, pa će
ručne izmene u JSON fajlovima biti prepisane. Menjaj zato generatore.
