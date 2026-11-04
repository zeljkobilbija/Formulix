package com.zeljkobilbija001.formulix;

import android.content.Context;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.util.AttributeSet;
import android.widget.FrameLayout;

import androidx.core.graphics.ColorUtils;

/** Okrugla, uvek kvadratna površina u pastelnoj boji oblasti (sa odsjajem gore levo). */
public class KrugView extends FrameLayout {

    private final GradientDrawable pozadina = new GradientDrawable();

    public KrugView(Context c) { this(c, null); }

    public KrugView(Context c, AttributeSet a) {
        super(c, a);
        pozadina.setShape(GradientDrawable.OVAL);
        pozadina.setGradientType(GradientDrawable.RADIAL_GRADIENT);
        pozadina.setGradientCenter(0.35f, 0.30f);
        pozadina.setStroke(Math.round(getResources().getDisplayMetrics().density),
                ColorUtils.setAlphaComponent(Color.WHITE, 150));
        setBackground(pozadina);
        setElevation(2 * getResources().getDisplayMetrics().density);
        postaviBoju(Color.GRAY);
    }

    /** Boja oblasti; krug dobija njenu pastelnu verziju. */
    public void postaviBoju(int boja) {
        pozadina.setColors(new int[]{
                ColorUtils.blendARGB(boja, Color.WHITE, 0.82f), Boje.pastel(boja)});
    }

    @Override
    protected void onMeasure(int wSpec, int hSpec) {
        super.onMeasure(wSpec, wSpec);
    }

    @Override
    protected void onSizeChanged(int w, int h, int ow, int oh) {
        super.onSizeChanged(w, h, ow, oh);
        pozadina.setGradientRadius(w * 0.75f);
    }
}
