package com.zeljkobilbija001.formulix;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import android.content.res.ColorStateList;

import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

/** Prikazuje oblasti kao pastelne krugove u mreži od dve kolone. */
public class OblastAdapter extends RecyclerView.Adapter<OblastAdapter.Drzac> {

    public interface KlikNaOblast {
        void naOblast(Oblast oblast, View krug);
    }

    private final List<Oblast> oblasti = new ArrayList<>();
    private final KlikNaOblast slusalac;

    public OblastAdapter(List<Oblast> pocetne, KlikNaOblast slusalac) {
        this.oblasti.addAll(pocetne);
        this.slusalac = slusalac;
    }

    /** Zameni prikazane oblasti (npr. posle pretrage). */
    public void postavi(List<Oblast> nove) {
        oblasti.clear();
        oblasti.addAll(nove);
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public Drzac onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_krug_mreza, parent, false);
        return new Drzac(v);
    }

    @Override
    public void onBindViewHolder(@NonNull Drzac h, int position) {
        Oblast o = oblasti.get(position);
        // Pastelni krug sa tamnim simbolom, kao krugovi na početnom ekranu
        int boja = ContextCompat.getColor(h.itemView.getContext(), o.boja);
        int tekst = Boje.tamna(boja);
        h.krug.postaviBoju(boja);
        h.simbol.setTextColor(tekst);
        h.simbolSlika.setImageTintList(ColorStateList.valueOf(tekst));
        h.naziv.setText(o.naziv);
        h.opis.setText(o.opis);

        if (o.slika != 0) {
            h.simbol.setVisibility(View.GONE);
            h.simbolSlika.setVisibility(View.VISIBLE);
            h.simbolSlika.setImageResource(o.slika);
        } else {
            h.simbolSlika.setVisibility(View.GONE);
            h.simbol.setVisibility(View.VISIBLE);
            h.simbol.setText(o.simbol);
        }

        h.itemView.setOnClickListener(v -> slusalac.naOblast(o, h.krug));
        h.krug.setOnClickListener(v -> slusalac.naOblast(o, h.krug));
    }

    @Override
    public int getItemCount() {
        return oblasti.size();
    }

    static class Drzac extends RecyclerView.ViewHolder {
        final KrugView krug;
        final TextView simbol;
        final ImageView simbolSlika;
        final TextView naziv;
        final TextView opis;

        Drzac(@NonNull View v) {
            super(v);
            krug = v.findViewById(R.id.simbolPozadina);
            simbol = v.findViewById(R.id.simbol);
            simbolSlika = v.findViewById(R.id.simbolSlika);
            naziv = v.findViewById(R.id.naziv);
            opis = v.findViewById(R.id.opis);
        }
    }
}
