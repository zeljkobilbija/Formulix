package com.zeljkobilbija001.formulix;

import android.app.Activity;
import android.graphics.Color;
import android.view.View;

import androidx.core.content.ContextCompat;
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

    /**
     * Zaglavlje u boji oblasti ide ispod status bara (ikonice status bara bele),
     * a donji deo ekrana (baner) iznad navigacije.
     */
    public static void obojenoZaglavlje(Activity a, View koren, View zaglavlje, int boja) {
        zaglavlje.setBackgroundColor(boja);
        WindowCompat.getInsetsController(a.getWindow(), a.getWindow().getDecorView())
                .setAppearanceLightStatusBars(false);
        final int gore = zaglavlje.getPaddingTop();
        ViewCompat.setOnApplyWindowInsetsListener(koren, (v, insets) -> {
            Insets bars = insets.getInsets(WindowInsetsCompat.Type.systemBars()
                    | WindowInsetsCompat.Type.ime());
            v.setPadding(bars.left, 0, bars.right, bars.bottom);
            zaglavlje.setPadding(zaglavlje.getPaddingLeft(), gore + bars.top,
                    zaglavlje.getPaddingRight(), zaglavlje.getPaddingBottom());
            return insets;
        });
        koren.setBackgroundColor(ContextCompat.getColor(a, R.color.pozadina));
    }
}
