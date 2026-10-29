package com.zeljkobilbija001.formulix;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.splashscreen.SplashScreen;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private OblastAdapter adapter;
    private TemaAdapter rezultatiAdapter;
    private RecyclerView lista;
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

        // Sadržaj ne ide ispod status bara i navigacije
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets bars = insets.getInsets(WindowInsetsCompat.Type.systemBars()
                    | WindowInsetsCompat.Type.ime());
            v.setPadding(bars.left, bars.top, bars.right, bars.bottom);
            return insets;
        });

        lista = findViewById(R.id.listaOblasti);
        rezultati = findViewById(R.id.listaRezultata);
        naslovOblasti = findViewById(R.id.naslovOblasti);
        nemaRezultata = findViewById(R.id.nemaRezultata);
        obrisi = findViewById(R.id.obrisiPretragu);
        EditText pretraga = findViewById(R.id.pretraga);

        adapter = new OblastAdapter(Oblasti.SVE, this::otvoriOblast);
        lista.setLayoutManager(new GridLayoutManager(this, 2));
        lista.setAdapter(adapter);

        rezultatiAdapter = new TemaAdapter(true,
                t -> startActivity(TemaActivity.namera(this, t.oblastId, t.id)));
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
        dugmePrivatnosti = findViewById(R.id.dugmePrivatnosti);
        dugmePrivatnosti.setOnClickListener(v ->
                Reklame.prikaziPodesavanjaPrivatnosti(this, this::posleSaglasnosti));
        Reklame.prikupiSaglasnost(this, this::posleSaglasnosti);
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
            naslovOblasti.setText(R.string.oblasti);
            rezultati.setVisibility(View.GONE);
            nemaRezultata.setVisibility(View.GONE);
            lista.setVisibility(View.VISIBLE);
            return;
        }

        List<Tema> nadjene = new ArrayList<>();
        for (Tema t : Sadrzaj.sveTeme(this)) {
            if (sadrziSveReci(t.zaPretragu, u)) nadjene.add(t);
        }
        rezultatiAdapter.postavi(nadjene);

        naslovOblasti.setText(R.string.rezultati);
        lista.setVisibility(View.GONE);
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
