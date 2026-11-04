package com.zeljkobilbija001.formulix;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

/** Ekran jedne oblasti: mreža tema (npr. Aritmetika → Razlomci, Procenti…). */
public class OblastActivity extends AppCompatActivity {

    private static final String EXTRA_OBLAST = "oblast";

    public static Intent namera(Context c, String oblastId) {
        return new Intent(c, OblastActivity.class).putExtra(EXTRA_OBLAST, oblastId);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_oblast);

        Oblast oblast = Oblasti.poId(getIntent().getStringExtra(EXTRA_OBLAST));
        if (oblast == null) {
            finish();
            return;
        }
        int boja = ContextCompat.getColor(this, oblast.boja);
        Boje.obojenoZaglavlje(this, findViewById(R.id.koren), findViewById(R.id.zaglavlje), boja);

        ((TextView) findViewById(R.id.naslov)).setText(oblast.naziv);
        ((TextView) findViewById(R.id.podnaslov)).setText(oblast.opis);
        findViewById(R.id.nazad).setOnClickListener(v -> finish());

        List<Tema> teme = Sadrzaj.teme(this, oblast.id);
        RecyclerView lista = findViewById(R.id.listaTema);
        TemaAdapter adapter = new TemaAdapter(false,
                (t, krug) -> KrugPrelaz.otvori(this, krug, boja,
                        () -> startActivity(TemaActivity.namera(this, t.oblastId, t.id))));
        lista.setLayoutManager(new GridLayoutManager(this, 2));
        lista.setAdapter(adapter);
        adapter.postavi(teme);

        findViewById(R.id.uskoro).setVisibility(teme.isEmpty() ? View.VISIBLE : View.GONE);
        lista.setVisibility(teme.isEmpty() ? View.GONE : View.VISIBLE);

        Reklame.prikaziBaner(this, findViewById(R.id.reklamaKontejner));
    }
}
