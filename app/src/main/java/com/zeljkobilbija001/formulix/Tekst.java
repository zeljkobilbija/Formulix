package com.zeljkobilbija001.formulix;

import java.text.Normalizer;
import java.util.Locale;

/** Pomoćne funkcije za pretragu teksta. */
public final class Tekst {

    private Tekst() { }

    /**
     * Mala slova, bez kvačica i akcenata: "Površina" → "povrsina", "Fläche" → "flache".
     * Tako pretraga radi i kad korisnik kuca bez kvačica.
     */
    public static String normalizuj(String s) {
        if (s == null) return "";
        String t = s.toLowerCase(Locale.ROOT)
                .replace("đ", "dj")
                .replace("ß", "ss")
                .replace("ё", "е");
        t = Normalizer.normalize(t, Normalizer.Form.NFD);
        return t.replaceAll("\\p{M}", "").trim();
    }
}
