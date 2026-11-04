package com.zeljkobilbija001.formulix;

import android.app.Activity;
import android.content.Context;
import android.content.res.ColorStateList;
import android.content.res.Configuration;
import android.graphics.Color;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.core.content.ContextCompat;
import androidx.core.graphics.ColorUtils;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;

/** Pomoćne funkcije za boje i obojeno zaglavlje ekrana. */
public final class Boje {

    private Boje() { }

    /** Boja sa zadatom providnošću (0–255). */
    public static int providna(int boja, int alfa) {
        return Color.argb(alfa, Color.red(boja), Color.green(boja), Color.blue(boja));
    }

    /** "#RRGGBB" za prosleđivanje stranici teme. */
    public static String hex(int boja) {
        return String.format("#%06X", 0xFFFFFF & boja);
    }

    /** Pastelna verzija boje oblasti (kao krugovi na početnom ekranu). */
    public static int pastel(int boja) {
        return ColorUtils.blendARGB(boja, Color.WHITE, 0.60f);
    }

    /** Tamna nijansa boje oblasti, za tekst i ikonice na pastelnoj podlozi. */
    public static int tamna(int boja) {
        return ColorUtils.blendARGB(boja, Color.BLACK, 0.45f);
    }

    public static boolean tamnaTema(Context c) {
        return (c.getResources().getConfiguration().uiMode
                & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
    }

    /** Pozadina ekrana oblasti: vrlo blaga nijansa boje oblasti (u tamnoj temi obična tamna). */
    public static int pozadinaEkrana(Context c, int boja) {
        return tamnaTema(c) ? ContextCompat.getColor(c, R.color.pozadina)
                : ColorUtils.blendARGB(boja, Color.WHITE, 0.92f);
    }

    /**
     * Zaglavlje u pastelnoj boji oblasti sa tamnim tekstom i ikonicama ide ispod status bara (ikonice status bara tamne),
     * a donji deo ekrana (baner) iznad navigacije.
     */
    public static void obojenoZaglavlje(Activity a, View koren, View zaglavlje, int boja) {
        oboji(koren, zaglavlje, boja);
        View podeli = zaglavlje.findViewById(R.id.dugmePodeli);
        if (podeli != null) podeli.setOnClickListener(v -> Deljenje.podeliAplikaciju(a));
        WindowCompat.getInsetsController(a.getWindow(), a.getWindow().getDecorView())
                .setAppearanceLightStatusBars(true); // tamne ikonice na pastelnoj boji
        final int gore = zaglavlje.getPaddingTop();
        ViewCompat.setOnApplyWindowInsetsListener(koren, (v, insets) -> {
            Insets bars = insets.getInsets(WindowInsetsCompat.Type.systemBars()
                    | WindowInsetsCompat.Type.ime());
            v.setPadding(bars.left, 0, bars.right, bars.bottom);
            zaglavlje.setPadding(zaglavlje.getPaddingLeft(), gore + bars.top,
                    zaglavlje.getPaddingRight(), zaglavlje.getPaddingBottom());
            return insets;
        });
    }

    /** Samo boje zaglavlja i pozadine (npr. kada ekran promeni kategoriju). */
    public static void oboji(View koren, View zaglavlje, int boja) {
        zaglavlje.setBackgroundColor(pastel(boja));
        int tekst = tamna(boja);
        ((TextView) zaglavlje.findViewById(R.id.naslov)).setTextColor(tekst);
        ((TextView) zaglavlje.findViewById(R.id.podnaslov)).setTextColor(tekst);
        ColorStateList ikonice = ColorStateList.valueOf(tekst);
        ((ImageView) zaglavlje.findViewById(R.id.nazad)).setImageTintList(ikonice);
        ((ImageView) zaglavlje.findViewById(R.id.dugmePodeli)).setImageTintList(ikonice);
        koren.setBackgroundColor(pozadinaEkrana(koren.getContext(), boja));
    }
}
