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

/** Ekran grupe oblasti: mreža obojenih kartica (npr. Fizika → Kretanje, Sile…). */
public class GrupaActivity extends AppCompatActivity {

    private static final String EXTRA_GRUPA = "grupa";

    public static Intent namera(Context c, String grupaId) {
        return new Intent(c, GrupaActivity.class).putExtra(EXTRA_GRUPA, grupaId);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_oblast);

        Oblast grupa = Oblasti.poId(getIntent().getStringExtra(EXTRA_GRUPA));
        if (grupa == null || !grupa.grupa) {
            finish();
            return;
        }
        int boja = ContextCompat.getColor(this, grupa.boja);
        Boje.obojenoZaglavlje(this, findViewById(R.id.koren), findViewById(R.id.zaglavlje), boja);

        ((TextView) findViewById(R.id.naslov)).setText(grupa.naziv);
        ((TextView) findViewById(R.id.podnaslov)).setText(grupa.opis);
        findViewById(R.id.nazad).setOnClickListener(v -> finish());

        RecyclerView lista = findViewById(R.id.listaTema);
        lista.setLayoutManager(new GridLayoutManager(this, 2));
        lista.setAdapter(new OblastAdapter(Oblasti.podoblasti(grupa.id),
                o -> startActivity(OblastActivity.namera(this, o.id))));
        findViewById(R.id.uskoro).setVisibility(View.GONE);
    }
}
