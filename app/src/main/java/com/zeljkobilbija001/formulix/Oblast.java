package com.zeljkobilbija001.formulix;

import androidx.annotation.ColorRes;
import androidx.annotation.DrawableRes;
import androidx.annotation.StringRes;

/** Jedna oblast matematike (kartica na početnom ekranu). */
public class Oblast {

    public final String id;
    @StringRes public final int naziv;
    @StringRes public final int opis;
    /** Tekstualni simbol (npr. "∫"); prazno ako se koristi slika. */
    public final String simbol;
    /** Vektorska slika umesto simbola; 0 ako se koristi tekst. */
    @DrawableRes public final int slika;
    @ColorRes public final int boja;

    public Oblast(String id, @StringRes int naziv, @StringRes int opis,
                  String simbol, @DrawableRes int slika, @ColorRes int boja) {
        this.id = id;
        this.naziv = naziv;
        this.opis = opis;
        this.simbol = simbol;
        this.slika = slika;
        this.boja = boja;
    }
}
