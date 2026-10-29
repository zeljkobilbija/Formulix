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
 * Periodni sistem elemenata (assets/hemija/sistem.html).
 * Dodir na element otvara njegovu karticu (TemaActivity, oblast "hemija").
 */
public class SistemActivity extends AppCompatActivity {

    private static final String DOMEN = "https://appassets.androidplatform.net";

    public static Intent namera(Context c) {
        return new Intent(c, SistemActivity.class);
    }

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_tema);

        Oblast oblast = Oblasti.poId(Hemija.OBLAST);
        int boja = ContextCompat.getColor(this, R.color.hemija);
        Boje.obojenoZaglavlje(this, findViewById(R.id.koren), findViewById(R.id.zaglavlje), boja);
        ((TextView) findViewById(R.id.naslov)).setText(R.string.periodni_sistem);
        ((TextView) findViewById(R.id.podnaslov)).setText(oblast != null ? oblast.naziv : R.string.oblast_hemija);
        findViewById(R.id.nazad).setOnClickListener(v -> finish());

        WebView web = findViewById(R.id.web);
        web.setBackgroundColor(ContextCompat.getColor(this, R.color.pozadina));
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true); // pamti horizontalni položaj tabele
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);

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
                String z = Hemija.atomskiBroj(request.getUrl());
                if (z != null) {
                    startActivity(TemaActivity.namera(SistemActivity.this, Hemija.OBLAST, z));
                }
                return true;
            }
        });

        boolean tamno = (getResources().getConfiguration().uiMode
                & Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES;
        Uri adresa = Uri.parse(DOMEN + "/assets/hemija/sistem.html").buildUpon()
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
