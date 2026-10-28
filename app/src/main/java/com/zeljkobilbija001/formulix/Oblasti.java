package com.zeljkobilbija001.formulix;

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
                    "n!", 0, R.color.kombinatorika)
    ));

    /** Oblast po id-u, ili null. */
    public static Oblast poId(String id) {
        for (Oblast o : SVE) if (o.id.equals(id)) return o;
        return null;
    }
}
