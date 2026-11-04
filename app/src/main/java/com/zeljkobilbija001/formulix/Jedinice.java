package com.zeljkobilbija001.formulix;

import androidx.annotation.ColorInt;
import androidx.annotation.StringRes;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Kategorije i jedinice za ekran "Jedinice" (konverzija metričkih ↔ anglosaksonskih mera).
 *
 * Svaka kategorija ima osnovnu jedinicu (npr. metar). Jedinica zna kako da pretvori
 * vrednost u osnovnu i nazad. Faktori su tačne međunarodne definicije
 * (1 in = 0,0254 m, 1 lb = 0,45359237 kg, 1 gal US = 3,785411784 L…).
 */
public final class Jedinice {

    private Jedinice() { }

    public static final class Jedinica {
        public final String simbol;
        @StringRes public final int naziv;
        private final double faktor, pomeraj;
        /** Obrnuto srazmerna jedinica (npr. mpg prema L/100 km): osnovna = faktor / v. */
        private final boolean obrnuta;

        Jedinica(String simbol, int naziv, double faktor, double pomeraj, boolean obrnuta) {
            this.simbol = simbol;
            this.naziv = naziv;
            this.faktor = faktor;
            this.pomeraj = pomeraj;
            this.obrnuta = obrnuta;
        }

        public double uOsnovnu(double v) {
            return obrnuta ? faktor / v : (v + pomeraj) * faktor;
        }

        public double izOsnovne(double o) {
            return obrnuta ? faktor / o : o / faktor - pomeraj;
        }
    }

    public static final class Kategorija {
        public final String id;
        @StringRes public final int naziv;
        public final String simbol;
        @ColorInt public final int boja;
        /** Jedinica koja se bira kada se kategorija prvi put otvori. */
        public final int podrazumevana;
        public final List<Jedinica> jedinice;

        Kategorija(String id, int naziv, String simbol, int boja, int podrazumevana, Jedinica... j) {
            this.id = id;
            this.naziv = naziv;
            this.simbol = simbol;
            this.boja = boja;
            this.podrazumevana = podrazumevana;
            this.jedinice = Collections.unmodifiableList(Arrays.asList(j));
        }
    }

    private static Jedinica j(String simbol, int naziv, double faktor) {
        return new Jedinica(simbol, naziv, faktor, 0, false);
    }

    private static Jedinica pomak(String simbol, int naziv, double faktor, double pomeraj) {
        return new Jedinica(simbol, naziv, faktor, pomeraj, false);
    }

    private static Jedinica obrnuta(String simbol, int naziv, double faktor) {
        return new Jedinica(simbol, naziv, faktor, 0, true);
    }

    private static final double PI = Math.PI;

    public static final List<Kategorija> SVE = Collections.unmodifiableList(Arrays.asList(
            // Osnovna: metar
            new Kategorija("duzina", R.string.k_duzina, "m", 0xFF1565C0, 3,
                    j("µm", R.string.u_mikrometar, 1e-6),
                    j("mm", R.string.u_milimetar, 1e-3),
                    j("cm", R.string.u_centimetar, 1e-2),
                    j("m", R.string.u_metar, 1),
                    j("km", R.string.u_kilometar, 1e3),
                    j("in", R.string.u_inc, 0.0254),
                    j("ft", R.string.u_stopa, 0.3048),
                    j("yd", R.string.u_jard, 0.9144),
                    j("mi", R.string.u_milja, 1609.344),
                    j("nmi", R.string.u_nauticka_milja, 1852)),
            // Osnovna: kvadratni metar
            new Kategorija("povrsina", R.string.k_povrsina, "m²", 0xFF2E7D32, 2,
                    j("mm²", R.string.u_mm2, 1e-6),
                    j("cm²", R.string.u_cm2, 1e-4),
                    j("m²", R.string.u_m2, 1),
                    j("a", R.string.u_ar, 100),
                    j("ha", R.string.u_hektar, 1e4),
                    j("km²", R.string.u_km2, 1e6),
                    j("in²", R.string.u_in2, 0.00064516),
                    j("ft²", R.string.u_ft2, 0.09290304),
                    j("yd²", R.string.u_yd2, 0.83612736),
                    j("ac", R.string.u_akr, 4046.8564224),
                    j("mi²", R.string.u_mi2, 2589988.110336)),
            // Osnovna: litar
            new Kategorija("zapremina", R.string.k_zapremina, "L", 0xFF00838F, 1,
                    j("mL", R.string.u_ml, 1e-3),
                    j("L", R.string.u_l, 1),
                    j("cm³", R.string.u_cm3, 1e-3),
                    j("m³", R.string.u_m3, 1e3),
                    j("in³", R.string.u_in3, 0.016387064),
                    j("ft³", R.string.u_ft3, 28.316846592),
                    j("tsp", R.string.u_kasicica, 0.00492892159375),
                    j("tbsp", R.string.u_kasika, 0.01478676478125),
                    j("fl oz", R.string.u_floz_us, 0.0295735295625),
                    j("cup", R.string.u_solja, 0.2365882365),
                    j("pt", R.string.u_pint_us, 0.473176473),
                    j("qt", R.string.u_kvart_us, 0.946352946),
                    j("gal", R.string.u_galon_us, 3.785411784),
                    j("fl oz UK", R.string.u_floz_uk, 0.0284130625),
                    j("pt UK", R.string.u_pint_uk, 0.56826125),
                    j("gal UK", R.string.u_galon_uk, 4.54609)),
            // Osnovna: kelvin
            new Kategorija("temperatura", R.string.k_temperatura, "°C", 0xFFC62828, 0,
                    pomak("°C", R.string.u_celzijus, 1, 273.15),
                    pomak("°F", R.string.u_farenhajt, 5.0 / 9, 459.67),
                    j("K", R.string.u_kelvin, 1),
                    j("°R", R.string.u_rankin, 5.0 / 9)),
            // Osnovna: kilogram
            new Kategorija("masa", R.string.k_masa, "kg", 0xFF6D4C41, 2,
                    j("mg", R.string.u_mg, 1e-6),
                    j("g", R.string.u_g, 1e-3),
                    j("kg", R.string.u_kg, 1),
                    j("t", R.string.u_t, 1e3),
                    j("ct", R.string.u_karat, 2e-4),
                    j("oz", R.string.u_unca, 0.028349523125),
                    j("lb", R.string.u_funta, 0.45359237),
                    j("st", R.string.u_stoun, 6.35029318),
                    j("ton US", R.string.u_tona_us, 907.18474),
                    j("ton UK", R.string.u_tona_uk, 1016.0469088)),
            // Osnovna: metar u sekundi
            new Kategorija("brzina", R.string.k_brzina, "km/h", 0xFFEF6C00, 1,
                    j("m/s", R.string.u_ms, 1),
                    j("km/h", R.string.u_kmh, 1 / 3.6),
                    j("mph", R.string.u_mph, 0.44704),
                    j("kn", R.string.u_cvor, 1852 / 3600.0),
                    j("ft/s", R.string.u_fts, 0.3048),
                    j("km/s", R.string.u_kms, 1e3),
                    j("c", R.string.u_c, 299792458)),
            // Osnovna: paskal
            new Kategorija("pritisak", R.string.k_pritisak, "bar", 0xFF5E35B1, 3,
                    j("Pa", R.string.u_pa, 1),
                    j("kPa", R.string.u_kpa, 1e3),
                    j("MPa", R.string.u_mpa, 1e6),
                    j("bar", R.string.u_bar, 1e5),
                    j("mbar", R.string.u_mbar, 100),
                    j("atm", R.string.u_atm, 101325),
                    j("psi", R.string.u_psi, 6894.757293168361),
                    j("mmHg", R.string.u_mmhg, 133.322387415),
                    j("inHg", R.string.u_inhg, 3386.388640341)),
            // Osnovna: džul
            new Kategorija("energija", R.string.k_energija, "J", 0xFFF9A825, 4,
                    j("J", R.string.u_j, 1),
                    j("kJ", R.string.u_kj, 1e3),
                    j("MJ", R.string.u_mj, 1e6),
                    j("cal", R.string.u_cal, 4.184),
                    j("kcal", R.string.u_kcal, 4184),
                    j("Wh", R.string.u_wh, 3600),
                    j("kWh", R.string.u_kwh, 3.6e6),
                    j("BTU", R.string.u_btu, 1055.05585262),
                    j("eV", R.string.u_ev, 1.602176634e-19),
                    j("ft·lbf", R.string.u_ftlbf, 1.3558179483314004)),
            // Osnovna: vat
            new Kategorija("snaga", R.string.k_snaga, "kW", 0xFF0277BD, 1,
                    j("W", R.string.u_w, 1),
                    j("kW", R.string.u_kw, 1e3),
                    j("MW", R.string.u_mw, 1e6),
                    j("hp", R.string.u_hp, 745.6998715822702),
                    j("PS", R.string.u_ks, 735.49875),
                    j("BTU/h", R.string.u_btuh, 0.29307107017222),
                    j("kcal/h", R.string.u_kcalh, 4184 / 3600.0),
                    j("ft·lbf/s", R.string.u_ftlbfs, 1.3558179483314004)),
            // Osnovna: amper
            new Kategorija("struja", R.string.k_struja, "A", 0xFF8E24AA, 2,
                    j("µA", R.string.u_mikroamper, 1e-6),
                    j("mA", R.string.u_miliamper, 1e-3),
                    j("A", R.string.u_amper, 1),
                    j("kA", R.string.u_kiloamper, 1e3)),
            // Osnovna: volt
            new Kategorija("napon", R.string.k_napon, "V", 0xFFD84315, 2,
                    j("µV", R.string.u_mikrovolt, 1e-6),
                    j("mV", R.string.u_milivolt, 1e-3),
                    j("V", R.string.u_volt, 1),
                    j("kV", R.string.u_kilovolt, 1e3),
                    j("MV", R.string.u_megavolt, 1e6)),
            // Osnovna: om
            new Kategorija("otpor", R.string.k_otpor, "Ω", 0xFF558B2F, 1,
                    j("mΩ", R.string.u_miliom, 1e-3),
                    j("Ω", R.string.u_om, 1),
                    j("kΩ", R.string.u_kiloom, 1e3),
                    j("MΩ", R.string.u_megaom, 1e6),
                    j("GΩ", R.string.u_gigaom, 1e9)),
            // Osnovna: kulon (1 Ah = 3600 C)
            new Kategorija("naelektrisanje", R.string.k_naelektrisanje, "mAh", 0xFF3949AB, 3,
                    j("µC", R.string.u_mikrokulon, 1e-6),
                    j("mC", R.string.u_milikulon, 1e-3),
                    j("C", R.string.u_kulon, 1),
                    j("mAh", R.string.u_mah, 3.6),
                    j("Ah", R.string.u_ah, 3600),
                    j("e", R.string.u_e, 1.602176634e-19)),
            // Osnovna: tesla (1 G = 10⁻⁴ T)
            new Kategorija("mag_b", R.string.k_mag_b, "T", 0xFF7B1FA2, 3,
                    j("nT", R.string.u_nanotesla, 1e-9),
                    j("µT", R.string.u_mikrotesla, 1e-6),
                    j("mT", R.string.u_militesla, 1e-3),
                    j("T", R.string.u_tesla, 1),
                    j("G", R.string.u_gaus, 1e-4),
                    j("mG", R.string.u_miligaus, 1e-7)),
            // Osnovna: amper po metru (1 Oe = 1000/4π A/m)
            new Kategorija("mag_h", R.string.k_mag_h, "A/m", 0xFF512DA8, 0,
                    j("A/m", R.string.u_am, 1),
                    j("kA/m", R.string.u_kam, 1e3),
                    j("Oe", R.string.u_ersted, 1000 / (4 * PI))),
            // Osnovna: litara na 100 km (ostale su obrnuto srazmerne)
            new Kategorija("gorivo", R.string.k_gorivo, "mpg", 0xFFAD1457, 0,
                    j("L/100 km", R.string.u_l100, 1),
                    obrnuta("km/L", R.string.u_kml, 100),
                    obrnuta("mpg US", R.string.u_mpg_us, 100 * 3.785411784 / 1.609344),
                    obrnuta("mpg UK", R.string.u_mpg_uk, 100 * 4.54609 / 1.609344)),
            // Osnovna: radijan
            new Kategorija("uglovi", R.string.k_uglovi, "∠", 0xFF00695C, 0,
                    j("°", R.string.u_stepen, PI / 180),
                    j("rad", R.string.u_radijan, 1),
                    j("gon", R.string.u_grad, PI / 200),
                    j("′", R.string.u_minut, PI / 10800),
                    j("″", R.string.u_sekund, PI / 648000),
                    j("tr", R.string.u_obrtaj, 2 * PI)),
            // Osnovna: bajt
            new Kategorija("podaci", R.string.k_podaci, "GB", 0xFF455A64, 4,
                    j("bit", R.string.u_bit, 0.125),
                    j("B", R.string.u_bajt, 1),
                    j("kB", R.string.u_kb, 1e3),
                    j("MB", R.string.u_mb, 1e6),
                    j("GB", R.string.u_gb, 1e9),
                    j("TB", R.string.u_tb, 1e12),
                    j("KiB", R.string.u_kib, 1024),
                    j("MiB", R.string.u_mib, 1048576),
                    j("GiB", R.string.u_gib, 1073741824),
                    j("TiB", R.string.u_tib, 1099511627776.0))
    ));
}
