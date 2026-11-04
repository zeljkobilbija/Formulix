package com.zeljkobilbija001.formulix;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.animation.ValueAnimator;
import android.app.Activity;
import android.view.View;
import android.view.ViewAnimationUtils;
import android.view.ViewGroup;
import android.view.animation.AccelerateDecelerateInterpolator;
import android.view.animation.DecelerateInterpolator;

/**
 * Prelaz pri otvaranju iz kruga: krug se naduva pa vrati, zatim se njegova
 * pastelna boja za jednu sekundu raširi iz kruga preko celog ekrana,
 * i tek onda se otvara sledeći ekran (sa blagim pretapanjem).
 */
public final class KrugPrelaz {

    private static final long NADUVAVANJE = 180;
    private static final long VRACANJE = 200;
    private static final long SIRENJE = 1000;

    private KrugPrelaz() { }

    public static void otvori(Activity a, View krug, int boja, Runnable otvaranje) {
        ViewGroup dekor = (ViewGroup) a.getWindow().getDecorView();
        if (dekor.getTag(R.id.krug) != null) return; // prelaz je već u toku
        if (!ValueAnimator.areAnimatorsEnabled()) {
            otvaranje.run();
            return;
        }
        dekor.setTag(R.id.krug, true);
        float dp = a.getResources().getDisplayMetrics().density;

        krug.setTranslationZ(6 * dp);
        krug.animate().scaleX(1.22f).scaleY(1.22f).setDuration(NADUVAVANJE)
                .setInterpolator(new DecelerateInterpolator())
                .withEndAction(() -> krug.animate().scaleX(1f).scaleY(1f).setDuration(VRACANJE)
                        .setInterpolator(new AccelerateDecelerateInterpolator())
                        .withEndAction(() -> {
                            krug.setTranslationZ(0);
                            rasiri(a, dekor, krug, boja, otvaranje);
                        })
                        .start())
                .start();
    }

    private static void rasiri(Activity a, ViewGroup dekor, View krug, int boja, Runnable otvaranje) {
        if (a.isFinishing() || a.isDestroyed()) {
            dekor.setTag(R.id.krug, null);
            return;
        }
        int[] k = new int[2], d = new int[2];
        krug.getLocationInWindow(k);
        dekor.getLocationInWindow(d);
        int cx = k[0] - d[0] + krug.getWidth() / 2;
        int cy = k[1] - d[1] + krug.getHeight() / 2;

        View zavesa = new View(a);
        zavesa.setBackgroundColor(Boje.pastel(boja));
        zavesa.setElevation(100 * a.getResources().getDisplayMetrics().density);
        dekor.addView(zavesa, new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

        zavesa.post(() -> {
            float kraj = (float) Math.hypot(Math.max(cx, dekor.getWidth() - cx),
                    Math.max(cy, dekor.getHeight() - cy));
            Animator sirenje = ViewAnimationUtils.createCircularReveal(
                    zavesa, cx, cy, krug.getWidth() / 2f, kraj);
            sirenje.setDuration(SIRENJE);
            sirenje.setInterpolator(new AccelerateDecelerateInterpolator());
            sirenje.addListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animator) {
                    otvaranje.run();
                    a.overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
                    // Novi ekran je već preko; zavesa se skida da bi povratak bio čist
                    zavesa.postDelayed(() -> {
                        dekor.removeView(zavesa);
                        dekor.setTag(R.id.krug, null);
                    }, 600);
                }
            });
            sirenje.start();
        });
    }
}
