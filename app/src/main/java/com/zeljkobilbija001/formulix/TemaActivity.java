package com.zeljkobilbija001.formulix;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.res.Configuration;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.webkit.WebViewAssetLoader;
import androidx.webkit.WebViewClientCompat;

/**
 * Ekran jedne teme: formule, objašnjenja i kalkulator.
 * Sadržaj prikazuje lokalna stranica assets/tema/tema.html (KaTeX radi bez interneta).
 */
public class TemaActivity extends AppCompatActivity {

    private static final String EXTRA_OBLAST = "oblast";
    private static final String EXTRA_TEMA = "tema";
    private static final String DOMEN = "https://appassets.androidplatform.net";

    public static Intent namera(Context c, String oblastId, String temaId) {
        return new Intent(c, TemaActivity.class)
                .putExtra(EXTRA_OBLAST, oblastId)
                .putExtra(EXTRA_TEMA, temaId);
    }

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_tema);

        String oblastId = getIntent().getStringExtra(EXTRA_OBLAST);
        String temaId = getIntent().getStringExtra(EXTRA_TEMA);
        Oblast oblast = Oblasti.poId(oblastId);
        Tema tema = null;
        if (oblast != null) {
            for (Tema t : Sadrzaj.teme(this, oblast.id)) if (t.id.equals(temaId)) tema = t;
        }
        if (tema == null) {
            finish();
            return;
        }

        int boja = ContextCompat.getColor(this, oblast.boja);
        Boje.obojenoZaglavlje(this, findViewById(R.id.koren), findViewById(R.id.zaglavlje), boja);
        ((TextView) findViewById(R.id.naslov)).setText(tema.naziv);
        ((TextView) findViewById(R.id.podnaslov)).setText(oblast.naziv);
        findViewById(R.id.nazad).setOnClickListener(v -> finish());

        WebView web = findViewById(R.id.web);
        web.setBackgroundColor(ContextCompat.getColor(this, R.color.pozadina));
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);

        // Stranica i JSON se služe iz assets/ preko lažnog https domena (preporučen način)
        WebViewAssetLoader ucitavac = new WebViewAssetLoader.Builder()
                .addPathHandler("/assets/", new WebViewAssetLoader.AssetsPathHandler(this))
                .build();
        web.setWebViewClient(new WebViewClientCompat() {
            @Override
            public WebResourceResponse shouldInterceptRequest(@NonNull WebView view,
                                                              @NonNull WebResourceRequest request) {
                return ucitavac.shouldInterceptRequest(request.getUrl());
            }

            @Override
            public boolean shouldOverrideUrlLoading(@NonNull WebView view,
                                                    @NonNull WebResourceRequest request) {
                return true; // stranica nema linkove ka spolja
            }
        });

        boolean tamno = (getResources().getConfiguration().uiMode
                & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
        Uri adresa = Uri.parse(DOMEN + "/assets/tema/tema.html").buildUpon()
                .appendQueryParameter("oblast", oblast.id)
                .appendQueryParameter("tema", tema.id)
                .appendQueryParameter("jezik", Jezik.trenutni(this))
                .appendQueryParameter("tamno", tamno ? "1" : "0")
                .appendQueryParameter("boja", Boje.hex(boja))
                .build();
        if (savedInstanceState == null) {
            web.loadUrl(adresa.toString());
        } else {
            web.restoreState(savedInstanceState);
        }

        Reklame.prikaziBaner(this, findViewById(R.id.reklamaKontejner));
    }

    @Override
    protected void onSaveInstanceState(@NonNull Bundle outState) {
        super.onSaveInstanceState(outState);
        WebView web = findViewById(R.id.web);
        if (web != null) web.saveState(outState);
    }
}
