package com.zeljkobilbija001.formulix;

import android.animation.TimeAnimator;
import android.animation.ValueAnimator;
import android.content.Context;
import android.graphics.Color;
import android.graphics.PorterDuff;
import android.graphics.drawable.GradientDrawable;
import android.util.AttributeSet;
import android.util.TypedValue;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.OvershootInterpolator;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.core.graphics.ColorUtils;
import androidx.core.widget.TextViewCompat;

import java.util.ArrayList;
import java.util.List;

/**
 * Mehurići (dizajn "Topli stakleni"): krugovi različitih veličina slobodno
 * raspoređeni po površini, bez preklapanja, i lagano lebde.
 *
 * Izabrani krug ({@link #fokusiraj}) klizi u centar i naraste, a ostali se
 * razmaknu i malo smanje. Prelaz se animira: krug se postavi na novo mesto i
 * novu veličinu, a pomeraj i razmera ga vode od starog izgleda do novog.
 */
public class KrugoviLayout extends ViewGroup {

    public interface PromenaFokusa {
        void naFokus(int indeks);
    }

    /** Polazni položaj (udeo širine i visine, 0–1) i relativna veličina kruga. */
    private static final class Mesto {
        final float x, y, velicina;
        final int boja;
        float cx, cy, r;             // cilj (raspored)
        float odX0, odY0, s0 = 1f;   // pomeraj i razmera na početku prelaza
        float odX, odY, s = 1f;      // trenutni pomeraj i razmera
        boolean fiksno;
        Mesto(float x, float y, float velicina, int boja) {
            this.x = x; this.y = y; this.velicina = velicina; this.boja = boja;
        }
    }

    private static final long TRAJANJE_PRELAZA = 700;
    private static final float UVECANJE = 1.6f;
    private static final float UMANJENJE = 0.86f;

    private final List<Mesto> mesta = new ArrayList<>();
    private final float dp;
    private final OvershootInterpolator opruga = new OvershootInterpolator(1.4f);
    private TimeAnimator sat;
    private long pocetakPrelaza = -1;
    private int zadnjaSirina, zadnjaVisina;
    private int fokus = -1;
    private PromenaFokusa slusalac;

    public KrugoviLayout(Context c) { this(c, null); }

    public KrugoviLayout(Context c, AttributeSet a) {
        super(c, a);
        dp = getResources().getDisplayMetrics().density;
        setClipChildren(false);
    }

    /**
     * Dodaje krug; x, y su udeo površine (0–1), velicina je relativna (1 = obična),
     * boja je boja oblasti (krug dobija njenu pastelnu verziju).
     */
    public void dodaj(View krug, float x, float y, float velicina, int boja) {
        mesta.add(new Mesto(x, y, velicina, boja));
        addView(krug);
        oznaci(krug, false);
        zadnjaSirina = 0; // ponovo izračunaj raspored
    }

    public void setPromenaFokusa(PromenaFokusa s) { slusalac = s; }

    public int getFokus() { return fokus; }

    /** Izabrani krug ide u centar i raste; -1 vraća sve u mirovanje. */
    public void fokusiraj(int indeks) {
        if (indeks == fokus) return;
        if (fokus >= 0 && fokus < getChildCount()) oznaci(getChildAt(fokus), false);
        fokus = indeks;
        if (fokus >= 0) oznaci(getChildAt(fokus), true);
        if (slusalac != null) slusalac.naFokus(fokus);

        int w = getWidth(), h = getHeight();
        if (w == 0 || h == 0) return;

        // Gde je svaki krug sada na ekranu (centar i poluprečnik)
        int n = mesta.size();
        float[] vx = new float[n], vy = new float[n], vr = new float[n];
        for (int i = 0; i < n; i++) {
            Mesto m = mesta.get(i);
            vx[i] = m.cx + m.odX;
            vy[i] = m.cy + m.odY;
            vr[i] = m.r * m.s;
        }
        rasporedi(w, h);
        boolean animacije = ValueAnimator.areAnimatorsEnabled();
        for (int i = 0; i < n; i++) {
            Mesto m = mesta.get(i);
            m.odX0 = animacije ? vx[i] - m.cx : 0;
            m.odY0 = animacije ? vy[i] - m.cy : 0;
            m.s0 = animacije && m.r > 0 ? vr[i] / m.r : 1f;
        }
        pocetakPrelaza = animacije ? -2 : -1; // -2: prelaz počinje u sledećem kadru
        if (!animacije) primeni(0);
        requestLayout();
    }

    @Override
    protected void onMeasure(int wSpec, int hSpec) {
        int w = MeasureSpec.getSize(wSpec);
        int h = MeasureSpec.getSize(hSpec);
        setMeasuredDimension(w, h);
        if (w == 0 || h == 0) return;

        if (w != zadnjaSirina || h != zadnjaVisina) {
            rasporedi(w, h);
            zadnjaSirina = w;
            zadnjaVisina = h;
        }
        for (int i = 0; i < getChildCount(); i++) {
            View krug = getChildAt(i);
            int d = Math.round(mesta.get(i).r * 2);
            podesiSadrzaj(krug, d);
            int s = MeasureSpec.makeMeasureSpec(d, MeasureSpec.EXACTLY);
            krug.measure(s, s);
        }
    }

    @Override
    protected void onLayout(boolean changed, int l, int t, int r, int b) {
        for (int i = 0; i < getChildCount(); i++) {
            Mesto m = mesta.get(i);
            View krug = getChildAt(i);
            int x = Math.round(m.cx - m.r), y = Math.round(m.cy - m.r);
            krug.layout(x, y, x + krug.getMeasuredWidth(), y + krug.getMeasuredHeight());
        }
        if (pocetakPrelaza == -1 && sat == null) primeni(0);
    }

    /** Dodir praznog prostora vraća krugove u mirovanje. */
    @Override
    public boolean onTouchEvent(MotionEvent e) {
        if (fokus < 0) return false;
        if (e.getAction() == MotionEvent.ACTION_UP) fokusiraj(-1);
        return true;
    }

    /** Veličine i položaji krugova za površinu w × h (uzima u obzir izabrani krug). */
    private void rasporedi(int w, int h) {
        int n = mesta.size();
        if (n == 0) return;
        float zbir = 0, najveci = 0;
        for (int i = 0; i < n; i++) {
            float v = faktor(i) * mesta.get(i).velicina;
            zbir += v * v;
            najveci = Math.max(najveci, v);
        }

        float rub = 6 * dp;      // mesto za lebdenje
        float razmak = 8 * dp;
        float cxs = w / 2f, cys = h / 2f;
        // Krugovi zauzimaju oko 58% površine; nijedan nije veći od 60% kraće stranice
        float d0 = (float) Math.sqrt(0.58f * w * h * 4 / (Math.PI * zbir));
        d0 = Math.min(d0, 0.60f * Math.min(w, h) / najveci);
        // Obični krugovi ostaju iste veličine kao bez izbora (ako ima mesta)
        float bezIzbora = 0, najveciBez = 0;
        for (Mesto m : mesta) { bezIzbora += m.velicina * m.velicina; najveciBez = Math.max(najveciBez, m.velicina); }
        float d0Bez = (float) Math.sqrt(0.58f * w * h * 4 / (Math.PI * bezIzbora));
        d0Bez = Math.min(d0Bez, 0.44f * w / najveciBez);
        d0 = Math.min(d0, d0Bez);

        for (int pokusaj = 0; pokusaj < 25; pokusaj++) {
            for (int i = 0; i < n; i++) {
                Mesto m = mesta.get(i);
                m.r = d0 * faktor(i) * m.velicina / 2;
                m.fiksno = i == fokus;
                m.cx = m.x * w;
                m.cy = m.y * h;
                if (m.fiksno) { m.cx = cxs; m.cy = cys; }
                else if (fokus >= 0) {
                    // odgurni od centra da napravi mesta
                    float dx = m.cx - cxs, dy = m.cy - cys;
                    float d = (float) Math.sqrt(dx * dx + dy * dy);
                    if (d < 1) { dx = 1; d = 1; }
                    m.cx += dx / d * 40 * dp;
                    m.cy += dy / d * 40 * dp;
                }
            }
            for (int k = 0; k < 300; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = i + 1; j < n; j++) {
                        Mesto a = mesta.get(i), b = mesta.get(j);
                        float dx = b.cx - a.cx, dy = b.cy - a.cy;
                        float d = (float) Math.sqrt(dx * dx + dy * dy);
                        if (d < 0.01f) { dx = 0.01f; d = 0.01f; }
                        float min = a.r + b.r + razmak;
                        if (d < min) {
                            float pomak = min - d, ux = dx / d, uy = dy / d;
                            if (a.fiksno) { b.cx += ux * pomak; b.cy += uy * pomak; }
                            else if (b.fiksno) { a.cx -= ux * pomak; a.cy -= uy * pomak; }
                            else {
                                a.cx -= ux * pomak / 2; a.cy -= uy * pomak / 2;
                                b.cx += ux * pomak / 2; b.cy += uy * pomak / 2;
                            }
                        }
                    }
                }
                for (Mesto m : mesta) {
                    if (m.fiksno) continue;
                    m.cx = Math.max(m.r + rub, Math.min(w - m.r - rub, m.cx));
                    m.cy = Math.max(m.r + rub, Math.min(h - m.r - rub, m.cy));
                }
            }
            if (bezPreklapanja(razmak * 0.5f)) return;
            d0 *= 0.95f; // ne staje: malo manji krugovi
        }
    }

    private float faktor(int i) {
        if (fokus < 0) return 1f;
        return i == fokus ? UVECANJE : UMANJENJE;
    }

    private boolean bezPreklapanja(float tolerancija) {
        for (int i = 0; i < mesta.size(); i++) {
            for (int j = i + 1; j < mesta.size(); j++) {
                Mesto a = mesta.get(i), b = mesta.get(j);
                float dx = b.cx - a.cx, dy = b.cy - a.cy;
                if (Math.sqrt(dx * dx + dy * dy) < a.r + b.r + tolerancija) return false;
            }
        }
        return true;
    }

    /** Simbol, naziv i opis rastu sa krugom. */
    private void podesiSadrzaj(View krug, int d) {
        Object tag = krug.getTag(R.id.krug);
        if (tag instanceof Integer && (Integer) tag == d) return;
        krug.setTag(R.id.krug, d);
        if (krug.getBackground() instanceof GradientDrawable) {
            ((GradientDrawable) krug.getBackground()).setGradientRadius(d * 0.75f);
        }

        TextView simbol = krug.findViewById(R.id.simbol);
        ImageView slika = krug.findViewById(R.id.simbolSlika);
        TextView naziv = krug.findViewById(R.id.naziv);
        TextView opis = krug.findViewById(R.id.opis);
        ImageView strelica = krug.findViewById(R.id.strelica);

        simbol.setTextSize(TypedValue.COMPLEX_UNIT_PX, d * 0.22f);
        LayoutParams ps = slika.getLayoutParams();
        ps.width = ps.height = Math.round(d * 0.26f);
        slika.setLayoutParams(ps);

        LayoutParams pn = naziv.getLayoutParams();
        pn.width = Math.round(d * 0.80f);
        pn.height = Math.round(d * 0.24f);
        naziv.setLayoutParams(pn);
        int najvise = Math.max(10, Math.round(Math.min(d * 0.11f, 22 * dp)));
        int najmanje = Math.min(najvise - 1, Math.round(8 * dp));
        TextViewCompat.setAutoSizeTextTypeUniformWithConfiguration(
                naziv, najmanje, najvise, 1, TypedValue.COMPLEX_UNIT_PX);

        LayoutParams po = opis.getLayoutParams();
        po.width = Math.round(d * 0.72f);
        opis.setLayoutParams(po);
        opis.setTextSize(TypedValue.COMPLEX_UNIT_PX, Math.max(9 * dp, Math.min(d * 0.065f, 14 * dp)));

        LayoutParams pa = strelica.getLayoutParams();
        pa.width = pa.height = Math.round(Math.max(20 * dp, d * 0.13f));
        strelica.setLayoutParams(pa);
    }

    /**
     * Pastelni krug u boji oblasti: boja pomešana sa belom, sa odsjajem gore levo
     * i svetlom ivicom. Tekst i ikonica su tamna nijansa iste boje.
     * Izabrani krug je svetliji, ima senku, opis i strelicu "otvori".
     */
    private void oznaci(View krug, boolean izabran) {
        int boja = mesta.get(indexOfChild(krug)).boja;
        int pastel = ColorUtils.blendARGB(boja, Color.WHITE, izabran ? 0.72f : 0.60f);
        int odsjaj = ColorUtils.blendARGB(boja, Color.WHITE, izabran ? 0.92f : 0.80f);
        int tekst = ColorUtils.blendARGB(boja, Color.BLACK, 0.45f);

        GradientDrawable g = new GradientDrawable();
        g.setShape(GradientDrawable.OVAL);
        g.setGradientType(GradientDrawable.RADIAL_GRADIENT);
        g.setGradientCenter(0.35f, 0.30f);
        g.setColors(new int[]{odsjaj, pastel});
        Object d = krug.getTag(R.id.krug);
        g.setGradientRadius((d instanceof Integer ? (Integer) d : 120 * dp) * 0.75f);
        g.setAlpha(izabran ? 255 : 235);
        g.setStroke(Math.round(dp), ColorUtils.setAlphaComponent(Color.WHITE, izabran ? 200 : 110));
        krug.setBackground(g);

        krug.setElevation(izabran ? 14 * dp : 2 * dp);
        ((TextView) krug.findViewById(R.id.simbol)).setTextColor(tekst);
        ((TextView) krug.findViewById(R.id.naziv)).setTextColor(tekst);
        ((TextView) krug.findViewById(R.id.opis)).setTextColor(tekst);
        ((ImageView) krug.findViewById(R.id.simbolSlika)).setColorFilter(tekst, PorterDuff.Mode.SRC_IN);
        ImageView strelica = krug.findViewById(R.id.strelica);
        strelica.setColorFilter(tekst, PorterDuff.Mode.SRC_IN);
        krug.findViewById(R.id.opis).setVisibility(izabran ? VISIBLE : GONE);
        strelica.setVisibility(izabran ? VISIBLE : GONE);
    }

    @Override
    protected void onAttachedToWindow() {
        super.onAttachedToWindow();
        pokreniLebdenje();
    }

    @Override
    protected void onDetachedFromWindow() {
        zaustaviLebdenje();
        super.onDetachedFromWindow();
    }

    /** Jedan sat pokreće i lebdenje i prelaze; isključen ako je korisnik ugasio animacije. */
    public void pokreniLebdenje() {
        zaustaviLebdenje();
        if (!ValueAnimator.areAnimatorsEnabled()) { primeni(0); return; }
        sat = new TimeAnimator();
        sat.setTimeListener((anim, ukupno, delta) -> primeni(ukupno));
        sat.start();
    }

    public void zaustaviLebdenje() {
        if (sat != null) sat.cancel();
        sat = null;
    }

    /** Postavlja pomeraj, razmeru i lebdenje svakog kruga za trenutak t (ms). */
    private void primeni(long t) {
        if (pocetakPrelaza == -2) pocetakPrelaza = t;
        float e = 1f;
        if (pocetakPrelaza >= 0) {
            float p = Math.min(1f, (t - pocetakPrelaza) / (float) TRAJANJE_PRELAZA);
            e = opruga.getInterpolation(p);
            if (p >= 1f) pocetakPrelaza = -1;
        }
        boolean lebdi = sat != null;
        for (int i = 0; i < getChildCount() && i < mesta.size(); i++) {
            Mesto m = mesta.get(i);
            View krug = getChildAt(i);
            float k = 1f - e;
            m.odX = m.odX0 * k;
            m.odY = m.odY0 * k;
            m.s = m.s0 + (1f - m.s0) * e;
            if (pocetakPrelaza == -1) { m.odX0 = m.odY0 = 0; m.s0 = 1f; }
            float lebdenje = 0;
            if (lebdi) {
                float period = 3600 + (i % 4) * 700;
                lebdenje = (float) Math.sin(2 * Math.PI * (t + i * 370) / period) * 3.5f * dp;
            }
            krug.setTranslationX(m.odX);
            krug.setTranslationY(m.odY + lebdenje);
            krug.setScaleX(m.s);
            krug.setScaleY(m.s);
        }
    }
}
