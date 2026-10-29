package com.zeljkobilbija001.formulix;

import android.net.Uri;

import java.util.List;

/** Hemija: periodni sistem (SistemActivity) i kartice elemenata (TemaActivity, oblast "hemija"). */
public final class Hemija {

    /** Id oblasti; podaci su u assets/oblasti/hemija.json (jedna tema = jedan element). */
    public static final String OBLAST = "hemija";

    private Hemija() { }

    /**
     * Stranice periodnog sistema i kartice elementa vode na adresu /element/&lt;Z&gt;.
     * Vraća atomski broj kao tekst ako je adresa takva, inače null.
     */
    public static String atomskiBroj(Uri adresa) {
        List<String> delovi = adresa.getPathSegments();
        if (delovi.size() == 2 && "element".equals(delovi.get(0)) && delovi.get(1).matches("\\d{1,3}")) {
            return delovi.get(1);
        }
        return null;
    }
}
