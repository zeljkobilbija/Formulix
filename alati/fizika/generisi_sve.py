"""
Pravi sve JSON fajlove fizike za Formulix i proverava formule kalkulatora.

Pokretanje (iz ovog foldera):
    python generisi_sve.py

Svaki gen_*.py pravi jedan fajl u app/src/main/assets/oblasti/.
Posle generisanja, ako je instaliran Node.js, proveri.js za svaku formulu
izračuna nepoznatu, pa iz rezultata ponovo izračuna svaku drugu veličinu
i uporedi ih (tako se hvataju greške u rešenim oblicima formula).
"""
import os
import shutil
import subprocess
import sys

OVDE = os.path.dirname(os.path.abspath(__file__))
OBLASTI = os.path.normpath(os.path.join(OVDE, '..', '..', 'app', 'src', 'main', 'assets', 'oblasti'))

# generator → ime JSON fajla
GENERATORI = [
    ('gen_kretanje.py', 'kretanje.json'),
    ('gen_sile.py', 'sile.json'),
    ('gen_energija.py', 'energija.json'),
    ('gen_fluidi.py', 'fluidi.json'),
    ('gen_rotacija.py', 'rotacija.json'),
    ('gen_toplota.py', 'toplota.json'),
    ('gen_elektricitet.py', 'elektricitet.json'),
    ('gen_magnetizam.py', 'magnetizam.json'),
    ('gen_talasi.py', 'talasi.json'),
    ('gen_moderna.py', 'moderna_fizika.json'),
    ('gen_konstante.py', 'konstante.json'),
]

def main():
    node = shutil.which('node')
    greske = 0
    for gen, izlaz in GENERATORI:
        putanja = os.path.join(OBLASTI, izlaz)
        print(f'{gen} → {izlaz}: ', end='', flush=True)
        r = subprocess.run([sys.executable, os.path.join(OVDE, gen), putanja], capture_output=True, text=True)
        if r.returncode != 0:
            greske += 1
            print('GREŠKA\n' + r.stderr)
            continue
        print(r.stdout.strip(), end='')
        if node and izlaz != 'konstante.json':
            p = subprocess.run([node, os.path.join(OVDE, 'proveri.js'), putanja], capture_output=True, text=True)
            print('  |  ' + (p.stdout.strip() or p.stderr.strip().splitlines()[-1]), end='')
            if p.returncode != 0 or 'gresaka: 0' not in p.stdout:
                greske += 1
        print()
    if not node:
        print('(Node.js nije pronađen, provera formula je preskočena.)')
    print('Gotovo.' if greske == 0 else f'Gotovo, ali ima {greske} problema.')
    sys.exit(1 if greske else 0)

if __name__ == '__main__':
    main()
