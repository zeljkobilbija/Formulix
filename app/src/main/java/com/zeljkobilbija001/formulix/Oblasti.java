package com.zeljkobilbija001.formulix;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/** Spisak svih oblasti, redom kako se prikazuju na početnom ekranu. */
public final class Oblasti {

    private Oblasti() { }

    public static final List<Oblast> SVE = Collections.unmodifiableList(Arrays.asList(
            new Oblast("aritmetika", R.string.oblast_aritmetika, R.string.opis_aritmetika,
                    "%", 0, R.color.aritmetika),
            new Oblast("algebra", R.string.oblast_algebra, R.string.opis_algebra,
                    "x²", 0, R.color.algebra),
            new Oblast("planimetrija", R.string.oblast_planimetrija, R.string.opis_planimetrija,
                    "", R.drawable.ic_oblast_trougao, R.color.planimetrija),
            new Oblast("stereometrija", R.string.oblast_stereometrija, R.string.opis_stereometrija,
                    "", R.drawable.ic_oblast_kocka, R.color.stereometrija),
            new Oblast("trigonometrija", R.string.oblast_trigonometrija, R.string.opis_trigonometrija,
                    "sin", 0, R.color.trigonometrija),
            new Oblast("analiza", R.string.oblast_analiza, R.string.opis_analiza,
                    "∫", 0, R.color.analiza),
            new Oblast("analiticka_geometrija", R.string.oblast_analiticka_geometrija,
                    R.string.opis_analiticka_geometrija,
                    "", R.drawable.ic_oblast_elipsa, R.color.analiticka_geometrija),
            new Oblast("kombinatorika", R.string.oblast_kombinatorika, R.string.opis_kombinatorika,
                    "n!", 0, R.color.kombinatorika),
            new Oblast("fizika", R.string.oblast_fizika, R.string.opis_fizika,
                    "", R.drawable.ic_oblast_atom, R.color.fizika, true),
            new Oblast(Hemija.OBLAST, R.string.oblast_hemija, R.string.opis_hemija,
                    "", R.drawable.ic_oblast_hemija, R.color.hemija)
    ));

    /** Oblasti fizike (ekran koji otvara kartica "Fizika"). Sadržaj: assets/oblasti/<id>.json */
    public static final List<Oblast> FIZIKA = Collections.unmodifiableList(Arrays.asList(
            new Oblast("kretanje", R.string.oblast_kretanje, R.string.opis_kretanje,
                    "v", 0, R.color.f_kretanje),
            new Oblast("sile", R.string.oblast_sile, R.string.opis_sile,
                    "F", 0, R.color.f_sile),
            new Oblast("energija", R.string.oblast_energija, R.string.opis_energija,
                    "E", 0, R.color.f_energija),
            new Oblast("fluidi", R.string.oblast_fluidi, R.string.opis_fluidi,
                    "ρ", 0, R.color.f_fluidi),
            new Oblast("rotacija", R.string.oblast_rotacija, R.string.opis_rotacija,
                    "ω", 0, R.color.f_rotacija),
            new Oblast("toplota", R.string.oblast_toplota, R.string.opis_toplota,
                    "°C", 0, R.color.f_toplota),
            new Oblast("elektricitet", R.string.oblast_elektricitet, R.string.opis_elektricitet,
                    "Ω", 0, R.color.f_elektricitet),
            new Oblast("magnetizam", R.string.oblast_magnetizam, R.string.opis_magnetizam,
                    "B", 0, R.color.f_magnetizam),
            new Oblast("talasi", R.string.oblast_talasi, R.string.opis_talasi,
                    "λ", 0, R.color.f_talasi),
            new Oblast("moderna_fizika", R.string.oblast_moderna_fizika, R.string.opis_moderna_fizika,
                    "hν", 0, R.color.f_moderna_fizika),
            new Oblast("konstante", R.string.oblast_konstante, R.string.opis_konstante,
                    "c₀", 0, R.color.f_konstante)
    ));

    /** Oblasti unutar grupe (npr. "fizika"); prazno za običnu oblast. */
    public static List<Oblast> podoblasti(String grupaId) {
        return "fizika".equals(grupaId) ? FIZIKA : Collections.<Oblast>emptyList();
    }

    /** Sve oblasti koje mogu imati teme (bez grupa), za pretragu. */
    public static List<Oblast> saTemama() {
        List<Oblast> sve = new ArrayList<>();
        for (Oblast o : SVE) {
            if (o.grupa) sve.addAll(podoblasti(o.id));
            else sve.add(o);
        }
        return sve;
    }

    /** Oblast po id-u (i oblasti fizike), ili null. */
    public static Oblast poId(String id) {
        for (Oblast o : SVE) if (o.id.equals(id)) return o;
        for (Oblast o : FIZIKA) if (o.id.equals(id)) return o;
        return null;
    }
}
