package com.zeljkobilbija001.formulix;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.activity.OnBackPressedCallback;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.splashscreen.SplashScreen;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private TemaAdapter rezultatiAdapter;
    private KrugoviLayout krugovi;
    private RecyclerView rezultati;
    private TextView naslovOblasti;
    private TextView nemaRezultata;
    private ImageButton obrisi;
    private ImageButton dugmePrivatnosti;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Splash mora pre super.onCreate()
        SplashScreen.installSplashScreen(this);
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        // Pastelna pozadina i iza status bara, pa ikonice status bara i navigacije tamne
        View koren = findViewById(R.id.main);
        koren.setBackground(new ToplaPozadina(getResources().getDisplayMetrics().density));
        WindowCompat.getInsetsController(getWindow(), getWindow().getDecorView())
                .setAppearanceLightStatusBars(true);
        WindowCompat.getInsetsController(getWindow(), getWindow().getDecorView())
                .setAppearanceLightNavigationBars(true);

        // Sadržaj ne ide ispod status bara i navigacije
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets bars = insets.getInsets(WindowInsetsCompat.Type.systemBars()
                    | WindowInsetsCompat.Type.ime());
            v.setPadding(bars.left, bars.top, bars.right, bars.bottom);
            return insets;
        });

        krugovi = findViewById(R.id.krugovi);
        rezultati = findViewById(R.id.listaRezultata);
        naslovOblasti = findViewById(R.id.naslovOblasti);
        nemaRezultata = findViewById(R.id.nemaRezultata);
        obrisi = findViewById(R.id.obrisiPretragu);
        EditText pretraga = findViewById(R.id.pretraga);

        postaviKrugove();

        rezultatiAdapter = new TemaAdapter(true,
                (t, v) -> startActivity(TemaActivity.namera(this, t.oblastId, t.id)));
        rezultati.setLayoutManager(new LinearLayoutManager(this));
        rezultati.setAdapter(rezultatiAdapter);

        pretraga.addTextChangedListener(new TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int a, int b, int c) { }
            @Override public void onTextChanged(CharSequence s, int a, int b, int c) { }
            @Override public void afterTextChanged(Editable s) {
                filtriraj(s.toString());
            }
        });
        obrisi.setOnClickListener(v -> pretraga.setText(""));

        // Privatnost (GDPR) i baner: prozor za saglasnost se prikazuje samo kad je potreban
        findViewById(R.id.dugmePodeli).setOnClickListener(v -> Deljenje.podeliAplikaciju(this));
        dugmePrivatnosti = findViewById(R.id.dugmePrivatnosti);
        dugmePrivatnosti.setOnClickListener(v ->
                Reklame.prikaziPodesavanjaPrivatnosti(this, this::posleSaglasnosti));
        Reklame.prikupiSaglasnost(this, this::posleSaglasnosti);
    }

    /**
     * Polazni raspored mehurića: id oblasti, položaj (udeo širine i visine) i veličina.
     * KrugoviLayout ih razmakne tako da se ne preklapaju.
     */
    private static final Object[][] RASPORED = {
            {"aritmetika", 0.27f, 0.10f, 1.00f},
            {"algebra", 0.74f, 0.12f, 1.05f},
            {"planimetrija", 0.16f, 0.33f, 1.00f},
            {"stereometrija", 0.56f, 0.32f, 1.10f},
            {"trigonometrija", 0.86f, 0.42f, 0.95f},
            {"analiza", 0.33f, 0.53f, 1.00f},
            {"analiticka_geometrija", 0.72f, 0.62f, 1.05f},
            {"kombinatorika", 0.18f, 0.75f, 1.00f},
            {"fizika", 0.50f, 0.85f, 1.20f},
            {Hemija.OBLAST, 0.84f, 0.88f, 1.00f},
    };

    private void postaviKrugove() {
        LayoutInflater inf = LayoutInflater.from(this);
        for (Oblast o : Oblasti.SVE) {
            float x = 0.5f, y = 0.5f, velicina = 1f;
            for (Object[] r : RASPORED) {
                if (r[0].equals(o.id)) { x = (float) r[1]; y = (float) r[2]; velicina = (float) r[3]; }
            }
            View krug = inf.inflate(R.layout.item_krug, krugovi, false);
            TextView simbol = krug.findViewById(R.id.simbol);
            ImageView slika = krug.findViewById(R.id.simbolSlika);
            if (o.slika != 0) {
                simbol.setVisibility(View.GONE);
                slika.setVisibility(View.VISIBLE);
                slika.setImageResource(o.slika);
            } else {
                simbol.setText(o.simbol);
            }
            ((TextView) krug.findViewById(R.id.naziv)).setText(o.naziv);
            ((TextView) krug.findViewById(R.id.opis)).setText(o.opis);
            krug.setContentDescription(getString(o.naziv) + ", " + getString(o.opis));
            // Prvi dodir: krug ide u centar i raste; dodir na izabrani krug otvara oblast
            krug.setOnClickListener(v -> {
                int i = krugovi.indexOfChild(v);
                if (krugovi.getFokus() == i) otvoriOblast(o);
                else krugovi.fokusiraj(i);
            });
            krugovi.dodaj(krug, x, y, velicina, ContextCompat.getColor(this, o.boja));
        }

        // Nazad dok je krug izabran: krugovi se vraćaju u mirovanje
        OnBackPressedCallback ponisti = new OnBackPressedCallback(false) {
            @Override public void handleOnBackPressed() { krugovi.fokusiraj(-1); }
        };
        getOnBackPressedDispatcher().addCallback(this, ponisti);
        krugovi.setPromenaFokusa(i -> ponisti.setEnabled(i >= 0));
    }

    private void posleSaglasnosti() {
        Reklame.prikaziBaner(this, findViewById(R.id.reklamaKontejner));
        dugmePrivatnosti.setVisibility(Reklame.trebaDugmePrivatnosti(this) ? View.VISIBLE : View.GONE);
    }

    /**
     * Prazna pretraga: kartice oblasti.
     * Inače: sve teme iz svih oblasti čiji naziv, opis ili ključne reči sadrže upit.
     */
    private void filtriraj(String upit) {
        String u = Tekst.normalizuj(upit);
        obrisi.setVisibility(u.isEmpty() ? View.GONE : View.VISIBLE);

        if (u.isEmpty()) {
            naslovOblasti.setVisibility(View.GONE);
            rezultati.setVisibility(View.GONE);
            nemaRezultata.setVisibility(View.GONE);
            krugovi.setVisibility(View.VISIBLE);
            krugovi.pokreniLebdenje();
            return;
        }

        List<Tema> nadjene = new ArrayList<>();
        for (Tema t : Sadrzaj.sveTeme(this)) {
            if (sadrziSveReci(t.zaPretragu, u)) nadjene.add(t);
        }
        rezultatiAdapter.postavi(nadjene);

        naslovOblasti.setVisibility(View.VISIBLE);
        krugovi.setVisibility(View.GONE);
        krugovi.zaustaviLebdenje();
        boolean prazno = nadjene.isEmpty();
        rezultati.setVisibility(prazno ? View.GONE : View.VISIBLE);
        nemaRezultata.setVisibility(prazno ? View.VISIBLE : View.GONE);
    }

    /** "zapremina kupe" nalazi temu koja sadrži obe reči, bilo kojim redom. */
    private static boolean sadrziSveReci(String tekst, String upit) {
        for (String rec : upit.split("\\s+")) {
            if (!rec.isEmpty() && !tekst.contains(rec)) return false;
        }
        return true;
    }

    private void otvoriOblast(Oblast o) {
        if (Hemija.OBLAST.equals(o.id)) startActivity(SistemActivity.namera(this));
        else if (o.grupa) startActivity(GrupaActivity.namera(this, o.id));
        else startActivity(OblastActivity.namera(this, o.id));
    }
}
