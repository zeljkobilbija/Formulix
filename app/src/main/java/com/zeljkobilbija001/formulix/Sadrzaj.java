package com.zeljkobilbija001.formulix;

import android.content.Context;
import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Učitava teme iz assets/oblasti/&lt;oblast&gt;.json.
 * Svaki tekst u JSON-u je ili običan string ili mapa {"sr": ..., "en": ...}.
 */
public final class Sadrzaj {

    private static final String TAG = "Sadrzaj";
    private static final Map<String, List<Tema>> KES = new HashMap<>();
    private static String kesJezik = null;

    private Sadrzaj() { }

    /** Teme jedne oblasti; prazna lista ako oblast još nema sadržaj. */
    public static synchronized List<Tema> teme(Context c, String oblastId) {
        String jezik = Jezik.trenutni(c);
        if (!jezik.equals(kesJezik)) {
            KES.clear();
            kesJezik = jezik;
        }
        List<Tema> t = KES.get(oblastId);
        if (t == null) {
            t = ucitaj(c.getApplicationContext(), oblastId, jezik);
            KES.put(oblastId, t);
        }
        return t;
    }

    /** Sve teme iz svih oblasti koje imaju sadržaj (za pretragu). */
    public static List<Tema> sveTeme(Context c) {
        List<Tema> sve = new ArrayList<>();
        for (Oblast o : Oblasti.SVE) sve.addAll(teme(c, o.id));
        return sve;
    }

    private static List<Tema> ucitaj(Context c, String oblastId, String jezik) {
        try {
            String[] fajlovi = c.getAssets().list("oblasti");
            if (fajlovi == null || !Arrays.asList(fajlovi).contains(oblastId + ".json")) {
                return Collections.emptyList();
            }
            JSONObject koren = new JSONObject(procitaj(c.getAssets().open("oblasti/" + oblastId + ".json")));
            Oblast oblast = Oblasti.poId(oblastId);
            String nazivOblasti = oblast != null ? c.getString(oblast.naziv) : "";

            JSONArray niz = koren.getJSONArray("teme");
            List<Tema> lista = new ArrayList<>(niz.length());
            for (int i = 0; i < niz.length(); i++) {
                JSONObject t = niz.getJSONObject(i);
                String naziv = tekst(t.opt("naziv"), jezik);
                String opis = tekst(t.opt("opis"), jezik);
                String kljucne = tekst(t.opt("kljucne_reci"), jezik);
                String zaPretragu = Tekst.normalizuj(naziv + " " + opis + " " + kljucne + " " + nazivOblasti);
                lista.add(new Tema(oblastId, t.getString("id"), tekst(t.opt("simbol"), jezik),
                        t.optString("ikona", ""), naziv, opis, zaPretragu));
            }
            return Collections.unmodifiableList(lista);
        } catch (IOException | JSONException e) {
            Log.e(TAG, "Ne mogu da učitam oblast " + oblastId, e);
            return Collections.emptyList();
        }
    }

    /** Tekst na traženom jeziku, sa rezervom na engleski pa srpski. */
    static String tekst(Object v, String jezik) {
        if (v == null || v == JSONObject.NULL) return "";
        if (v instanceof String) return (String) v;
        if (v instanceof JSONObject) {
            JSONObject o = (JSONObject) v;
            if (o.has(jezik)) return o.optString(jezik);
            if (o.has("en")) return o.optString("en");
            return o.optString("sr");
        }
        return String.valueOf(v);
    }

    private static String procitaj(InputStream in) throws IOException {
        try (InputStream ulaz = in; ByteArrayOutputStream izlaz = new ByteArrayOutputStream()) {
            byte[] buf = new byte[8192];
            int n;
            while ((n = ulaz.read(buf)) != -1) izlaz.write(buf, 0, n);
            return izlaz.toString(StandardCharsets.UTF_8.name());
        }
    }
}
