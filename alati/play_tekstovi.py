# Tekstovi za Google Play listing (8 jezika): play/<jezik>/title.txt, short_description.txt,
# full_description.txt. Pokretanje:  python play_tekstovi.py <izlazni folder>
# Proverava ograničenja Play konzole: naziv ≤ 30, kratak opis ≤ 80, pun opis ≤ 4000 znakova.
import io
import os
import sys

TEKSTOVI = {
"en-US": ("Formulix – Formulas & Units",
"Math, physics and chemistry formulas with calculators and a unit converter.",
"""Formulix is a clear and colourful handbook of formulas for school, university and everyday life. Pick a topic, find the formula you need and calculate the result straight away.

WHAT'S INSIDE
• Mathematics – arithmetic, algebra, plane and solid geometry, trigonometry, calculus, analytic geometry and combinatorics
• Physics – motion, forces, energy, fluids, rotation, heat, electricity, magnetism, waves, modern physics and physical constants
• Chemistry – interactive periodic table with all 118 elements
• Units – converter between metric and imperial units: length, area, volume, temperature, mass, speed, pressure, energy, power, current, voltage, resistance, charge, magnetic field, fuel economy, angles and data

FEATURES
• Formulas written clearly, with drawings of shapes and solids
• Built-in calculator: enter the known values and choose what to find
• Fast search across all topics (e.g. "cone volume", "integral")
• Unit converter shows the result in all units at once
• Works offline, no account needed
• Soft pastel design that is easy on the eyes
• Available in English, Serbian, German, Spanish, French, Italian, Portuguese and Russian

Ideal for students, teachers, engineers and anyone who wants the right formula at hand."""),

"sr": ("Formulix – formule i jedinice",
"Formule iz matematike, fizike i hemije sa kalkulatorom i konverterom jedinica.",
"""Formulix je pregledan i šaren priručnik formula za školu, fakultet i svakodnevni život. Izaberi oblast, pronađi formulu koja ti treba i odmah izračunaj rezultat.

ŠTA SADRŽI
• Matematika – aritmetika, algebra, planimetrija, stereometrija, trigonometrija, analiza, analitička geometrija i kombinatorika
• Fizika – kretanje, sile, energija, fluidi, rotacija, toplota, elektricitet, magnetizam, talasi, moderna fizika i fizičke konstante
• Hemija – interaktivni periodni sistem sa svih 118 elemenata
• Jedinice – konverter metričkih i anglosaksonskih mera: dužina, površina, zapremina, temperatura, masa, brzina, pritisak, energija, snaga, struja, napon, otpor, naelektrisanje, magnetno polje, potrošnja goriva, uglovi i podaci

MOGUĆNOSTI
• Jasno napisane formule, sa crtežima figura i tela
• Ugrađeni kalkulator: upiši poznate vrednosti i izaberi šta tražiš
• Brza pretraga kroz sve oblasti (npr. „zapremina kupe“, „integral“)
• Konverter prikazuje rezultat u svim jedinicama odjednom
• Radi bez interneta, bez naloga
• Blag pastelni dizajn koji ne zamara oči
• Na srpskom, engleskom, nemačkom, španskom, francuskom, italijanskom, portugalskom i ruskom

Idealno za učenike, studente, nastavnike, inženjere i sve kojima treba prava formula pri ruci."""),

"de-DE": ("Formulix – Formeln & Einheiten",
"Formeln für Mathe, Physik und Chemie – mit Rechner und Einheitenumrechner.",
"""Formulix ist eine übersichtliche und farbenfrohe Formelsammlung für Schule, Studium und Alltag. Wähle ein Thema, finde die passende Formel und berechne das Ergebnis sofort.

INHALT
• Mathematik – Arithmetik, Algebra, ebene Geometrie, Stereometrie, Trigonometrie, Analysis, analytische Geometrie und Kombinatorik
• Physik – Bewegung, Kräfte, Energie, Fluide, Rotation, Wärme, Elektrizität, Magnetismus, Wellen, moderne Physik und Naturkonstanten
• Chemie – interaktives Periodensystem mit allen 118 Elementen
• Einheiten – Umrechner zwischen metrischen und imperialen Einheiten: Länge, Fläche, Volumen, Temperatur, Masse, Geschwindigkeit, Druck, Energie, Leistung, Stromstärke, Spannung, Widerstand, Ladung, Magnetfeld, Verbrauch, Winkel und Daten

FUNKTIONEN
• Klar dargestellte Formeln mit Zeichnungen von Figuren und Körpern
• Integrierter Rechner: bekannte Werte eingeben und die gesuchte Größe wählen
• Schnelle Suche in allen Themen (z. B. „Kegel Volumen“, „Integral“)
• Der Umrechner zeigt das Ergebnis in allen Einheiten gleichzeitig
• Funktioniert offline, ohne Konto
• Sanftes Pastell-Design, angenehm für die Augen
• Auf Deutsch, Englisch, Serbisch, Spanisch, Französisch, Italienisch, Portugiesisch und Russisch

Ideal für Schüler, Studierende, Lehrkräfte, Ingenieure und alle, die die richtige Formel schnell zur Hand haben möchten."""),

"es-ES": ("Formulix: fórmulas y unidades",
"Fórmulas de matemáticas, física y química con calculadora y conversor.",
"""Formulix es un formulario claro y colorido para el colegio, la universidad y el día a día. Elige un tema, encuentra la fórmula que necesitas y calcula el resultado al instante.

CONTENIDO
• Matemáticas – aritmética, álgebra, geometría plana y del espacio, trigonometría, cálculo, geometría analítica y combinatoria
• Física – movimiento, fuerzas, energía, fluidos, rotación, calor, electricidad, magnetismo, ondas, física moderna y constantes físicas
• Química – tabla periódica interactiva con los 118 elementos
• Unidades – conversor entre unidades métricas e imperiales: longitud, área, volumen, temperatura, masa, velocidad, presión, energía, potencia, corriente, tensión, resistencia, carga, campo magnético, consumo de combustible, ángulos y datos

FUNCIONES
• Fórmulas escritas con claridad, con dibujos de figuras y cuerpos
• Calculadora integrada: introduce los valores conocidos y elige qué calcular
• Búsqueda rápida en todos los temas (p. ej. «volumen del cono», «integral»)
• El conversor muestra el resultado en todas las unidades a la vez
• Funciona sin conexión y sin cuenta
• Diseño en suaves tonos pastel, agradable para la vista
• En español, inglés, serbio, alemán, francés, italiano, portugués y ruso

Ideal para estudiantes, profesores, ingenieros y cualquiera que quiera tener la fórmula correcta a mano."""),

"fr-FR": ("Formulix – formules et unités",
"Formules de maths, physique et chimie avec calculatrice et convertisseur.",
"""Formulix est un formulaire clair et coloré pour le collège, le lycée, les études et la vie de tous les jours. Choisis un domaine, trouve la formule dont tu as besoin et calcule le résultat tout de suite.

CONTENU
• Mathématiques – arithmétique, algèbre, géométrie plane et dans l'espace, trigonométrie, analyse, géométrie analytique et dénombrement
• Physique – mouvement, forces, énergie, fluides, rotation, chaleur, électricité, magnétisme, ondes, physique moderne et constantes physiques
• Chimie – tableau périodique interactif avec les 118 éléments
• Unités – convertisseur entre unités métriques et impériales : longueur, surface, volume, température, masse, vitesse, pression, énergie, puissance, courant, tension, résistance, charge, champ magnétique, consommation, angles et données

FONCTIONS
• Formules claires, avec des dessins de figures et de solides
• Calculatrice intégrée : saisis les valeurs connues et choisis ce que tu cherches
• Recherche rapide dans tous les domaines (ex. « volume du cône », « intégrale »)
• Le convertisseur affiche le résultat dans toutes les unités à la fois
• Fonctionne hors ligne, sans compte
• Design pastel doux, agréable pour les yeux
• En français, anglais, serbe, allemand, espagnol, italien, portugais et russe

Idéal pour les élèves, les étudiants, les enseignants, les ingénieurs et tous ceux qui veulent la bonne formule sous la main."""),

"it-IT": ("Formulix – formule e unità",
"Formule di matematica, fisica e chimica con calcolatrice e convertitore.",
"""Formulix è un formulario chiaro e colorato per la scuola, l'università e la vita di tutti i giorni. Scegli un argomento, trova la formula che ti serve e calcola subito il risultato.

CONTENUTI
• Matematica – aritmetica, algebra, geometria piana e solida, trigonometria, analisi, geometria analitica e calcolo combinatorio
• Fisica – moto, forze, energia, fluidi, rotazione, calore, elettricità, magnetismo, onde, fisica moderna e costanti fisiche
• Chimica – tavola periodica interattiva con tutti i 118 elementi
• Unità – convertitore tra unità metriche e imperiali: lunghezza, area, volume, temperatura, massa, velocità, pressione, energia, potenza, corrente, tensione, resistenza, carica, campo magnetico, consumo di carburante, angoli e dati

FUNZIONI
• Formule scritte in modo chiaro, con disegni di figure e solidi
• Calcolatrice integrata: inserisci i valori noti e scegli cosa calcolare
• Ricerca veloce in tutti gli argomenti (es. «volume del cono», «integrale»)
• Il convertitore mostra il risultato in tutte le unità contemporaneamente
• Funziona offline, senza account
• Design pastello delicato, riposante per gli occhi
• In italiano, inglese, serbo, tedesco, spagnolo, francese, portoghese e russo

Ideale per studenti, insegnanti, ingegneri e per chiunque voglia avere la formula giusta a portata di mano."""),

"pt-PT": ("Formulix – fórmulas e unidades",
"Fórmulas de matemática, física e química com calculadora e conversor.",
"""O Formulix é um formulário claro e colorido para a escola, a universidade e o dia a dia. Escolha um tema, encontre a fórmula de que precisa e calcule o resultado de imediato.

CONTEÚDO
• Matemática – aritmética, álgebra, geometria plana e espacial, trigonometria, análise, geometria analítica e combinatória
• Física – movimento, forças, energia, fluidos, rotação, calor, eletricidade, magnetismo, ondas, física moderna e constantes físicas
• Química – tabela periódica interativa com os 118 elementos
• Unidades – conversor entre unidades métricas e imperiais: comprimento, área, volume, temperatura, massa, velocidade, pressão, energia, potência, corrente, tensão, resistência, carga, campo magnético, consumo de combustível, ângulos e dados

FUNCIONALIDADES
• Fórmulas escritas com clareza, com desenhos de figuras e sólidos
• Calculadora integrada: introduza os valores conhecidos e escolha o que calcular
• Pesquisa rápida em todos os temas (ex.: «volume do cone», «integral»)
• O conversor mostra o resultado em todas as unidades ao mesmo tempo
• Funciona offline, sem conta
• Design suave em tons pastel, agradável para os olhos
• Em português, inglês, sérvio, alemão, espanhol, francês, italiano e russo

Ideal para estudantes, professores, engenheiros e para quem quer ter a fórmula certa à mão."""),

"ru-RU": ("Formulix – формулы и единицы",
"Формулы по математике, физике и химии с калькулятором и конвертером единиц.",
"""Formulix — понятный и красочный справочник формул для школы, университета и повседневной жизни. Выберите раздел, найдите нужную формулу и сразу рассчитайте результат.

СОДЕРЖАНИЕ
• Математика — арифметика, алгебра, планиметрия, стереометрия, тригонометрия, математический анализ, аналитическая геометрия и комбинаторика
• Физика — движение, силы, энергия, жидкости и газы, вращение, теплота, электричество, магнетизм, волны, современная физика и физические константы
• Химия — интерактивная периодическая таблица со всеми 118 элементами
• Единицы — конвертер метрических и британских единиц: длина, площадь, объём, температура, масса, скорость, давление, энергия, мощность, ток, напряжение, сопротивление, заряд, магнитное поле, расход топлива, углы и данные

ВОЗМОЖНОСТИ
• Чётко записанные формулы с чертежами фигур и тел
• Встроенный калькулятор: введите известные значения и выберите, что найти
• Быстрый поиск по всем разделам (например, «объём конуса», «интеграл»)
• Конвертер сразу показывает результат во всех единицах
• Работает без интернета и без регистрации
• Мягкий пастельный дизайн, не утомляющий глаза
• На русском, английском, сербском, немецком, испанском, французском, итальянском и португальском

Идеально для школьников, студентов, учителей, инженеров и всех, кому нужна правильная формула под рукой."""),
}


def main(izlaz):
    for jezik, (naziv, kratak, pun) in TEKSTOVI.items():
        assert len(naziv) <= 30, (jezik, "naziv", len(naziv))
        assert len(kratak) <= 80, (jezik, "kratak opis", len(kratak))
        assert len(pun) <= 4000, (jezik, "pun opis", len(pun))
        folder = os.path.join(izlaz, jezik)
        os.makedirs(folder, exist_ok=True)
        for ime, tekst in (("title.txt", naziv), ("short_description.txt", kratak),
                           ("full_description.txt", pun)):
            with io.open(os.path.join(folder, ime), "w", encoding="utf-8", newline="\n") as f:
                f.write(tekst + "\n")
        print("%-6s naziv %2d  kratak %2d  pun %4d" % (jezik, len(naziv), len(kratak), len(pun)))


if __name__ == "__main__":
    main(sys.argv[1])
