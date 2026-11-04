package com.zeljkobilbija001.formulix;

import android.graphics.Canvas;
import android.graphics.ColorFilter;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.PixelFormat;
import android.graphics.RadialGradient;
import android.graphics.Rect;
import android.graphics.Shader;
import android.graphics.drawable.Drawable;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

/**
 * Topla pozadina početnog ekrana (dizajn "Topli stakleni"): eliptični sjaj
 * ispod sredine ekrana koji prelazi u tamno braon, i mekana svetla mrlja gore levo.
 */
public class ToplaPozadina extends Drawable {

    private static final int[] BOJE = {0xFFE8913A, 0xFF9A5A2C, 0xFF5A3A2A, 0xFF2F2019};
    private static final float[] POLOZAJI = {0f, 0.38f, 0.70f, 1f};

    private final float gustina;
    private final Paint sjaj = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint mrlja = new Paint(Paint.ANTI_ALIAS_FLAG);
    private float mrljaX, mrljaY, mrljaR;

    public ToplaPozadina(float gustina) {
        this.gustina = gustina;
    }

    @Override
    protected void onBoundsChange(@NonNull Rect b) {
        float w = b.width(), h = b.height();
        if (w <= 0 || h <= 0) return;

        // Krug poluprečnika 1, razvučen u elipsu (120% širine × 70% visine) sa centrom na 50% / 72%
        RadialGradient g = new RadialGradient(0, 0, 1, BOJE, POLOZAJI, Shader.TileMode.CLAMP);
        Matrix m = new Matrix();
        m.setScale(1.2f * w, 0.7f * h);
        m.postTranslate(b.left + 0.5f * w, b.top + 0.72f * h);
        g.setLocalMatrix(m);
        sjaj.setShader(g);

        mrljaX = b.left + 50 * gustina;
        mrljaY = b.top + 70 * gustina;
        mrljaR = 170 * gustina;
        mrlja.setShader(new RadialGradient(mrljaX, mrljaY, mrljaR,
                new int[]{0x2EFFD6AA, 0x00FFD6AA}, null, Shader.TileMode.CLAMP));
    }

    @Override
    public void draw(@NonNull Canvas c) {
        c.drawRect(getBounds(), sjaj);
        c.drawCircle(mrljaX, mrljaY, mrljaR, mrlja);
    }

    @Override public void setAlpha(int alpha) { }
    @Override public void setColorFilter(@Nullable ColorFilter cf) { }
    @Override public int getOpacity() { return PixelFormat.OPAQUE; }
}
