package com.zeljkobilbija001.formulix;

import androidx.annotation.ColorRes;
import androidx.annotation.DrawableRes;
import androidx.annotation.StringRes;

/** Jedna oblast (kartica): oblast matematike ili fizike, ili grupa oblasti (npr. Fizika). */
public class Oblast {

    public final String id;
    @StringRes public final int naziv;
    @StringRes public final int opis;
    /** Tekstualni simbol (npr. "∫"); prazno ako se koristi slika. */
    public final String simbol;
    /** Vektorska slika umesto simbola; 0 ako se koristi tekst. */
    @DrawableRes public final int slika;
    @ColorRes public final int boja;
    /** true: kartica otvara mrežu svojih oblasti (Oblasti.podoblasti), a ne teme. */
    public final boolean grupa;

    public Oblast(String id, @StringRes int naziv, @StringRes int opis,
                  String simbol, @DrawableRes int slika, @ColorRes int boja) {
        this(id, naziv, opis, simbol, slika, boja, false);
    }

    public Oblast(String id, @StringRes int naziv, @StringRes int opis,
                  String simbol, @DrawableRes int slika, @ColorRes int boja, boolean grupa) {
        this.id = id;
        this.naziv = naziv;
        this.opis = opis;
        this.simbol = simbol;
        this.slika = slika;
        this.boja = boja;
        this.grupa = grupa;
    }
}
