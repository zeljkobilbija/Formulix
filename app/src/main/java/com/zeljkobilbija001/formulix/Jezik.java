package com.zeljkobilbija001.formulix;

import android.content.Context;

import java.util.Arrays;
import java.util.List;
import java.util.Locale;

/** Jezik aplikacije: jedan od 8 podržanih, inače engleski. */
public final class Jezik {

    private Jezik() { }

    public static final List<String> PODRZANI =
            Arrays.asList("sr", "en", "it", "fr", "es", "de", "pt", "ru");

    public static String trenutni(Context c) {
        Locale l = c.getResources().getConfiguration().getLocales().get(0);
        String j = l.getLanguage();
        return PODRZANI.contains(j) ? j : "en";
    }
}
