package com.zeljkobilbija001.formulix;

import android.app.Activity;
import android.content.Intent;

/** Dugme "Podeli": standardni Android meni za deljenje sa linkom ka aplikaciji na Play prodavnici. */
public final class Deljenje {

    private Deljenje() { }

    public static void podeliAplikaciju(Activity a) {
        String link = "https://play.google.com/store/apps/details?id=" + a.getPackageName();
        Intent slanje = new Intent(Intent.ACTION_SEND)
                .setType("text/plain")
                .putExtra(Intent.EXTRA_SUBJECT, a.getString(R.string.app_name))
                .putExtra(Intent.EXTRA_TEXT, a.getString(R.string.podeli_poruka, link));
        a.startActivity(Intent.createChooser(slanje, a.getString(R.string.podeli_naslov)));
    }
}
