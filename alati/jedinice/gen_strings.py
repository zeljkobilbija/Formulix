# Pravi res/values*/strings_jedinice.xml (nazivi kategorija i jedinica na 8 jezika).
# Pokretanje iz ovog foldera:  python gen_strings.py ../../app/src/main/res
# Redosled jezika: en, sr, de, es, fr, it, pt, ru
import io
import os
import sys

JEZICI = ["values", "values-sr", "values-de", "values-es", "values-fr", "values-it", "values-pt", "values-ru"]

TEKSTOVI = """
oblast_jedinice|Units|Jedinice|Einheiten|Unidades|Unités|Unità|Unidades|Единицы
opis_jedinice|Metric ↔ imperial|Metričke ↔ anglosaksonske|Metrisch ↔ imperial|Métrico ↔ imperial|Métrique ↔ impérial|Metrico ↔ imperiale|Métrico ↔ imperial|Метрические ↔ британские
vrednost|Value|Vrednost|Wert|Valor|Valeur|Valore|Valor|Значение
izaberi_jedinicu|Choose unit|Izaberi jedinicu|Einheit wählen|Elegir unidad|Choisir l'unité|Scegli unità|Escolher unidade|Выберите единицу
kopirano|Copied|Kopirano|Kopiert|Copiado|Copié|Copiato|Copiado|Скопировано
k_duzina|Length|Dužina|Länge|Longitud|Longueur|Lunghezza|Comprimento|Длина
k_povrsina|Area|Površina|Fläche|Área|Surface|Area|Área|Площадь
k_zapremina|Volume|Zapremina|Volumen|Volumen|Volume|Volume|Volume|Объём
k_temperatura|Temperature|Temperatura|Temperatur|Temperatura|Température|Temperatura|Temperatura|Температура
k_masa|Mass|Masa|Masse|Masa|Masse|Massa|Massa|Масса
k_brzina|Speed|Brzina|Geschwindigkeit|Velocidad|Vitesse|Velocità|Velocidade|Скорость
k_pritisak|Pressure|Pritisak|Druck|Presión|Pression|Pressione|Pressão|Давление
k_energija|Energy|Energija|Energie|Energía|Énergie|Energia|Energia|Энергия
k_snaga|Power|Snaga|Leistung|Potencia|Puissance|Potenza|Potência|Мощность
k_struja|Current|Struja|Stromstärke|Corriente|Courant|Corrente|Corrente|Сила тока
k_napon|Voltage|Napon|Spannung|Tensión|Tension|Tensione|Tensão|Напряжение
k_otpor|Resistance|Otpor|Widerstand|Resistencia|Résistance|Resistenza|Resistência|Сопротивление
k_naelektrisanje|Charge|Naelektrisanje|Ladung|Carga|Charge|Carica|Carga|Заряд
k_mag_b|Magnetic field (B)|Magnetno polje (B)|Magnetfeld (B)|Campo magnético (B)|Champ magnétique (B)|Campo magnetico (B)|Campo magnético (B)|Магнитная индукция (B)
k_mag_h|Magnetic field (H)|Jačina magn. polja (H)|Magnetische Feldstärke (H)|Intensidad magnética (H)|Excitation magnétique (H)|Intensità campo magn. (H)|Intensidade magnética (H)|Напряжённость поля (H)
k_gorivo|Fuel economy|Potrošnja goriva|Verbrauch|Consumo|Consommation|Consumo|Consumo|Расход топлива
k_uglovi|Angle|Uglovi|Winkel|Ángulo|Angle|Angolo|Ângulo|Угол
k_podaci|Data|Podaci|Daten|Datos|Données|Dati|Dados|Данные
u_mikrometar|micrometre|mikrometar|Mikrometer|micrómetro|micromètre|micrometro|micrômetro|микрометр
u_milimetar|millimetre|milimetar|Millimeter|milímetro|millimètre|millimetro|milímetro|миллиметр
u_centimetar|centimetre|centimetar|Zentimeter|centímetro|centimètre|centimetro|centímetro|сантиметр
u_metar|metre|metar|Meter|metro|mètre|metro|metro|метр
u_kilometar|kilometre|kilometar|Kilometer|kilómetro|kilomètre|chilometro|quilómetro|километр
u_inc|inch|inč|Zoll|pulgada|pouce|pollice|polegada|дюйм
u_stopa|foot|stopa|Fuß|pie|pied|piede|pé|фут
u_jard|yard|jard|Yard|yarda|yard|iarda|jarda|ярд
u_milja|mile|milja|Meile|milla|mille|miglio|milha|миля
u_nauticka_milja|nautical mile|nautička milja|Seemeile|milla náutica|mille marin|miglio nautico|milha náutica|морская миля
u_mm2|square millimetre|kvadratni milimetar|Quadratmillimeter|milímetro cuadrado|millimètre carré|millimetro quadrato|milímetro quadrado|квадратный миллиметр
u_cm2|square centimetre|kvadratni centimetar|Quadratzentimeter|centímetro cuadrado|centimètre carré|centimetro quadrato|centímetro quadrado|квадратный сантиметр
u_m2|square metre|kvadratni metar|Quadratmeter|metro cuadrado|mètre carré|metro quadrato|metro quadrado|квадратный метр
u_ar|are|ar|Ar|área|are|ara|are|ар
u_hektar|hectare|hektar|Hektar|hectárea|hectare|ettaro|hectare|гектар
u_km2|square kilometre|kvadratni kilometar|Quadratkilometer|kilómetro cuadrado|kilomètre carré|chilometro quadrato|quilómetro quadrado|квадратный километр
u_in2|square inch|kvadratni inč|Quadratzoll|pulgada cuadrada|pouce carré|pollice quadrato|polegada quadrada|квадратный дюйм
u_ft2|square foot|kvadratna stopa|Quadratfuß|pie cuadrado|pied carré|piede quadrato|pé quadrado|квадратный фут
u_yd2|square yard|kvadratni jard|Quadratyard|yarda cuadrada|yard carré|iarda quadrata|jarda quadrada|квадратный ярд
u_akr|acre|akr|Acre|acre|acre|acro|acre|акр
u_mi2|square mile|kvadratna milja|Quadratmeile|milla cuadrada|mille carré|miglio quadrato|milha quadrada|квадратная миля
u_ml|millilitre|mililitar|Milliliter|mililitro|millilitre|millilitro|mililitro|миллилитр
u_l|litre|litar|Liter|litro|litre|litro|litro|литр
u_cm3|cubic centimetre|kubni centimetar|Kubikzentimeter|centímetro cúbico|centimètre cube|centimetro cubo|centímetro cúbico|кубический сантиметр
u_m3|cubic metre|kubni metar|Kubikmeter|metro cúbico|mètre cube|metro cubo|metro cúbico|кубический метр
u_in3|cubic inch|kubni inč|Kubikzoll|pulgada cúbica|pouce cube|pollice cubo|polegada cúbica|кубический дюйм
u_ft3|cubic foot|kubna stopa|Kubikfuß|pie cúbico|pied cube|piede cubo|pé cúbico|кубический фут
u_kasicica|teaspoon (US)|kašičica (SAD)|Teelöffel (US)|cucharadita (EE. UU.)|cuillère à café (US)|cucchiaino (USA)|colher de chá (EUA)|чайная ложка (США)
u_kasika|tablespoon (US)|kašika (SAD)|Esslöffel (US)|cucharada (EE. UU.)|cuillère à soupe (US)|cucchiaio (USA)|colher de sopa (EUA)|столовая ложка (США)
u_floz_us|fluid ounce (US)|tečna unca (SAD)|Flüssigunze (US)|onza líquida (EE. UU.)|once liquide (US)|oncia liquida (USA)|onça líquida (EUA)|жидкая унция (США)
u_solja|cup (US)|šolja (SAD)|Tasse (US)|taza (EE. UU.)|tasse (US)|tazza (USA)|xícara (EUA)|чашка (США)
u_pint_us|pint (US)|pinta (SAD)|Pint (US)|pinta (EE. UU.)|pinte (US)|pinta (USA)|pinta (EUA)|пинта (США)
u_kvart_us|quart (US)|kvart (SAD)|Quart (US)|cuarto (EE. UU.)|quart (US)|quarto (USA)|quarto (EUA)|кварта (США)
u_galon_us|gallon (US)|galon (SAD)|Gallone (US)|galón (EE. UU.)|gallon (US)|gallone (USA)|galão (EUA)|галлон (США)
u_floz_uk|fluid ounce (UK)|tečna unca (UK)|Flüssigunze (UK)|onza líquida (RU)|once liquide (UK)|oncia liquida (UK)|onça líquida (RU)|жидкая унция (брит.)
u_pint_uk|pint (UK)|pinta (UK)|Pint (UK)|pinta (RU)|pinte (UK)|pinta (UK)|pinta (RU)|пинта (брит.)
u_galon_uk|gallon (UK)|galon (UK)|Gallone (UK)|galón (RU)|gallon (UK)|gallone (UK)|galão (RU)|галлон (брит.)
u_mg|milligram|miligram|Milligramm|miligramo|milligramme|milligrammo|miligrama|миллиграмм
u_g|gram|gram|Gramm|gramo|gramme|grammo|grama|грамм
u_kg|kilogram|kilogram|Kilogramm|kilogramo|kilogramme|chilogrammo|quilograma|килограмм
u_t|tonne|tona|Tonne|tonelada|tonne|tonnellata|tonelada|тонна
u_karat|carat|karat|Karat|quilate|carat|carato|quilate|карат
u_unca|ounce|unca|Unze|onza|once|oncia|onça|унция
u_funta|pound|funta|Pfund|libra|livre|libbra|libra|фунт
u_stoun|stone|stoun|Stone|stone|stone|stone|stone|стоун
u_tona_us|short ton (US)|kratka tona (SAD)|Short Ton (US)|tonelada corta (EE. UU.)|tonne courte (US)|tonnellata corta (USA)|tonelada curta (EUA)|короткая тонна (США)
u_tona_uk|long ton (UK)|duga tona (UK)|Long Ton (UK)|tonelada larga (RU)|tonne longue (UK)|tonnellata lunga (UK)|tonelada longa (RU)|длинная тонна (брит.)
u_ms|metre per second|metar u sekundi|Meter pro Sekunde|metro por segundo|mètre par seconde|metro al secondo|metro por segundo|метр в секунду
u_kmh|kilometre per hour|kilometar na čas|Kilometer pro Stunde|kilómetro por hora|kilomètre par heure|chilometro orario|quilómetro por hora|километр в час
u_kms|kilometre per second|kilometar u sekundi|Kilometer pro Sekunde|kilómetro por segundo|kilomètre par seconde|chilometro al secondo|quilómetro por segundo|километр в секунду
u_c|speed of light|brzina svetlosti|Lichtgeschwindigkeit|velocidad de la luz|vitesse de la lumière|velocità della luce|velocidade da luz|скорость света
u_mph|mile per hour|milja na čas|Meile pro Stunde|milla por hora|mille par heure|miglio orario|milha por hora|миля в час
u_cvor|knot|čvor|Knoten|nudo|nœud|nodo|nó|узел
u_fts|foot per second|stopa u sekundi|Fuß pro Sekunde|pie por segundo|pied par seconde|piede al secondo|pé por segundo|фут в секунду
u_pa|pascal|paskal|Pascal|pascal|pascal|pascal|pascal|паскаль
u_kpa|kilopascal|kilopaskal|Kilopascal|kilopascal|kilopascal|kilopascal|quilopascal|килопаскаль
u_mpa|megapascal|megapaskal|Megapascal|megapascal|mégapascal|megapascal|megapascal|мегапаскаль
u_bar|bar|bar|Bar|bar|bar|bar|bar|бар
u_mbar|millibar|milibar|Millibar|milibar|millibar|millibar|milibar|миллибар
u_atm|atmosphere|atmosfera|Atmosphäre|atmósfera|atmosphère|atmosfera|atmosfera|атмосфера
u_psi|pound per square inch|funta po kvadratnom inču|Pfund pro Quadratzoll|libra por pulgada cuadrada|livre par pouce carré|libbra per pollice quadrato|libra por polegada quadrada|фунт на квадратный дюйм
u_mmhg|millimetre of mercury|milimetar živinog stuba|Millimeter Quecksilbersäule|milímetro de mercurio|millimètre de mercure|millimetro di mercurio|milímetro de mercúrio|миллиметр ртутного столба
u_inhg|inch of mercury|inč živinog stuba|Zoll Quecksilbersäule|pulgada de mercurio|pouce de mercure|pollice di mercurio|polegada de mercúrio|дюйм ртутного столба
u_j|joule|džul|Joule|julio|joule|joule|joule|джоуль
u_kj|kilojoule|kilodžul|Kilojoule|kilojulio|kilojoule|kilojoule|quilojoule|килоджоуль
u_mj|megajoule|megadžul|Megajoule|megajulio|mégajoule|megajoule|megajoule|мегаджоуль
u_cal|calorie|kalorija|Kalorie|caloría|calorie|caloria|caloria|калория
u_kcal|kilocalorie|kilokalorija|Kilokalorie|kilocaloría|kilocalorie|chilocaloria|quilocaloria|килокалория
u_wh|watt-hour|vat-čas|Wattstunde|vatio-hora|wattheure|wattora|watt-hora|ватт-час
u_kwh|kilowatt-hour|kilovat-čas|Kilowattstunde|kilovatio-hora|kilowattheure|chilowattora|quilowatt-hora|киловатт-час
u_btu|British thermal unit|britanska toplotna jedinica|British Thermal Unit|unidad térmica británica|unité thermique britannique|unità termica britannica|unidade térmica britânica|британская тепловая единица
u_ev|electronvolt|elektronvolt|Elektronenvolt|electronvoltio|électronvolt|elettronvolt|elétron-volt|электронвольт
u_ftlbf|foot-pound|stopa-funta|Foot-Pound|pie-libra|pied-livre|piede-libbra|pé-libra|фут-фунт
u_w|watt|vat|Watt|vatio|watt|watt|watt|ватт
u_kw|kilowatt|kilovat|Kilowatt|kilovatio|kilowatt|chilowatt|quilowatt|киловатт
u_mw|megawatt|megavat|Megawatt|megavatio|mégawatt|megawatt|megawatt|мегаватт
u_hp|horsepower (imperial)|konjska snaga (anglosaksonska)|Horsepower (imperial)|caballo de fuerza (imperial)|horsepower (impérial)|cavallo vapore britannico|cavalo-força (imperial)|лошадиная сила (брит.)
u_ks|metric horsepower|konjska snaga (metrička)|Pferdestärke|caballo de vapor|cheval-vapeur|cavallo vapore|cavalo-vapor|лошадиная сила (метр.)
u_btuh|BTU per hour|BTU na čas|BTU pro Stunde|BTU por hora|BTU par heure|BTU all'ora|BTU por hora|BTU в час
u_kcalh|kilocalorie per hour|kilokalorija na čas|Kilokalorie pro Stunde|kilocaloría por hora|kilocalorie par heure|chilocaloria all'ora|quilocaloria por hora|килокалория в час
u_ftlbfs|foot-pound per second|stopa-funta u sekundi|Foot-Pound pro Sekunde|pie-libra por segundo|pied-livre par seconde|piede-libbra al secondo|pé-libra por segundo|фут-фунт в секунду
u_mikroamper|microampere|mikroamper|Mikroampere|microamperio|microampère|microampere|microampere|микроампер
u_miliamper|milliampere|miliamper|Milliampere|miliamperio|milliampère|milliampere|miliampere|миллиампер
u_amper|ampere|amper|Ampere|amperio|ampère|ampere|ampere|ампер
u_kiloamper|kiloampere|kiloamper|Kiloampere|kiloamperio|kiloampère|kiloampere|quiloampere|килоампер
u_mikrovolt|microvolt|mikrovolt|Mikrovolt|microvoltio|microvolt|microvolt|microvolt|микровольт
u_milivolt|millivolt|milivolt|Millivolt|milivoltio|millivolt|millivolt|milivolt|милливольт
u_volt|volt|volt|Volt|voltio|volt|volt|volt|вольт
u_kilovolt|kilovolt|kilovolt|Kilovolt|kilovoltio|kilovolt|kilovolt|quilovolt|киловольт
u_megavolt|megavolt|megavolt|Megavolt|megavoltio|mégavolt|megavolt|megavolt|мегавольт
u_miliom|milliohm|miliom|Milliohm|miliohmio|milliohm|milliohm|miliohm|миллиом
u_om|ohm|om|Ohm|ohmio|ohm|ohm|ohm|ом
u_kiloom|kilohm|kiloom|Kiloohm|kiloohmio|kiloohm|kiloohm|quilohm|килоом
u_megaom|megohm|megaom|Megaohm|megaohmio|mégohm|megaohm|megaohm|мегаом
u_gigaom|gigohm|gigaom|Gigaohm|gigaohmio|gigaohm|gigaohm|gigaohm|гигаом
u_mikrokulon|microcoulomb|mikrokulon|Mikrocoulomb|microculombio|microcoulomb|microcoulomb|microcoulomb|микрокулон
u_milikulon|millicoulomb|milikulon|Millicoulomb|miliculombio|millicoulomb|millicoulomb|milicoulomb|милликулон
u_kulon|coulomb|kulon|Coulomb|culombio|coulomb|coulomb|coulomb|кулон
u_mah|milliampere-hour|miliamper-čas|Milliamperestunde|miliamperio-hora|milliampère-heure|milliampere-ora|miliampere-hora|миллиампер-час
u_ah|ampere-hour|amper-čas|Amperestunde|amperio-hora|ampère-heure|ampere-ora|ampere-hora|ампер-час
u_e|elementary charge|elementarno naelektrisanje|Elementarladung|carga elemental|charge élémentaire|carica elementare|carga elementar|элементарный заряд
u_nanotesla|nanotesla|nanotesla|Nanotesla|nanotesla|nanotesla|nanotesla|nanotesla|нанотесла
u_mikrotesla|microtesla|mikrotesla|Mikrotesla|microtesla|microtesla|microtesla|microtesla|микротесла
u_militesla|millitesla|militesla|Millitesla|militesla|millitesla|millitesla|militesla|миллитесла
u_tesla|tesla|tesla|Tesla|tesla|tesla|tesla|tesla|тесла
u_gaus|gauss|gaus|Gauß|gauss|gauss|gauss|gauss|гаусс
u_miligaus|milligauss|miligaus|Milligauß|miligauss|milligauss|milligauss|miligauss|миллигаусс
u_am|ampere per metre|amper po metru|Ampere pro Meter|amperio por metro|ampère par mètre|ampere al metro|ampere por metro|ампер на метр
u_kam|kiloampere per metre|kiloamper po metru|Kiloampere pro Meter|kiloamperio por metro|kiloampère par mètre|kiloampere al metro|quiloampere por metro|килоампер на метр
u_ersted|oersted|ersted|Oersted|oersted|œrsted|oersted|oersted|эрстед
u_l100|litres per 100 km|litara na 100 km|Liter pro 100 km|litros por 100 km|litres aux 100 km|litri per 100 km|litros por 100 km|литров на 100 км
u_kml|kilometres per litre|kilometara po litru|Kilometer pro Liter|kilómetros por litro|kilomètres par litre|chilometri per litro|quilómetros por litro|километров на литр
u_mpg_us|miles per gallon (US)|milja po galonu (SAD)|Meilen pro Gallone (US)|millas por galón (EE. UU.)|milles par gallon (US)|miglia per gallone (USA)|milhas por galão (EUA)|миль на галлон (США)
u_mpg_uk|miles per gallon (UK)|milja po galonu (UK)|Meilen pro Gallone (UK)|millas por galón (RU)|milles par gallon (UK)|miglia per gallone (UK)|milhas por galão (RU)|миль на галлон (брит.)
u_celzijus|degree Celsius|stepen Celzijusa|Grad Celsius|grado Celsius|degré Celsius|grado Celsius|grau Celsius|градус Цельсия
u_farenhajt|degree Fahrenheit|stepen Farenhajta|Grad Fahrenheit|grado Fahrenheit|degré Fahrenheit|grado Fahrenheit|grau Fahrenheit|градус Фаренгейта
u_kelvin|kelvin|kelvin|Kelvin|kelvin|kelvin|kelvin|kelvin|кельвин
u_rankin|degree Rankine|stepen Rankina|Grad Rankine|grado Rankine|degré Rankine|grado Rankine|grau Rankine|градус Ранкина
u_stepen|degree|stepen|Grad|grado|degré|grado|grau|градус
u_radijan|radian|radijan|Radiant|radián|radian|radiante|radiano|радиан
u_grad|gradian|grad|Gon|gradián|grade|gradiente centesimale|grado|град
u_minut|arcminute|ugaoni minut|Winkelminute|minuto de arco|minute d'arc|primo d'arco|minuto de arco|угловая минута
u_sekund|arcsecond|ugaoni sekund|Winkelsekunde|segundo de arco|seconde d'arc|secondo d'arco|segundo de arco|угловая секунда
u_obrtaj|turn|pun krug|Umdrehung|vuelta|tour|giro|volta|оборот
u_bit|bit|bit|Bit|bit|bit|bit|bit|бит
u_bajt|byte|bajt|Byte|byte|octet|byte|byte|байт
u_kb|kilobyte|kilobajt|Kilobyte|kilobyte|kilooctet|kilobyte|quilobyte|килобайт
u_mb|megabyte|megabajt|Megabyte|megabyte|mégaoctet|megabyte|megabyte|мегабайт
u_gb|gigabyte|gigabajt|Gigabyte|gigabyte|gigaoctet|gigabyte|gigabyte|гигабайт
u_tb|terabyte|terabajt|Terabyte|terabyte|téraoctet|terabyte|terabyte|терабайт
u_kib|kibibyte|kibibajt|Kibibyte|kibibyte|kibioctet|kibibyte|kibibyte|кибибайт
u_mib|mebibyte|mebibajt|Mebibyte|mebibyte|mébioctet|mebibyte|mebibyte|мебибайт
u_gib|gibibyte|gibibajt|Gibibyte|gibibyte|gibioctet|gibibyte|gibibyte|гибибайт
u_tib|tebibyte|tebibajt|Tebibyte|tebibyte|tébioctet|tebibyte|tebibyte|тебибайт
"""


def xml(tekst):
    return (tekst.replace("&", "&amp;").replace("<", "&lt;")
            .replace("'", "\\'").replace('"', '\\"'))


def main(res):
    redovi = [r.split("|") for r in TEKSTOVI.strip().splitlines()]
    for i, folder in enumerate(JEZICI):
        linije = ['<?xml version="1.0" encoding="utf-8"?>',
                  "<!-- Generisano: alati/jedinice/gen_strings.py (ne menjati ručno) -->",
                  "<resources>"]
        for r in redovi:
            assert len(r) == 9, r
            linije.append('    <string name="%s">%s</string>' % (r[0], xml(r[1 + i])))
        linije.append("</resources>")
        put = os.path.join(res, folder, "strings_jedinice.xml")
        with io.open(put, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(linije) + "\n")
        print(put)


if __name__ == "__main__":
    main(sys.argv[1])
