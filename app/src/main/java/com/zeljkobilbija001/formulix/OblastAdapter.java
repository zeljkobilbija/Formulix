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

/** Prikazuje kartice oblasti u mreži. */
public class OblastAdapter extends RecyclerView.Adapter<OblastAdapter.Drzac> {

    public interface KlikNaOblast {
        void naOblast(Oblast oblast);
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
                .inflate(R.layout.item_oblast, parent, false);
        return new Drzac(v);
    }

    @Override
    public void onBindViewHolder(@NonNull Drzac h, int position) {
        Oblast o = oblasti.get(position);
        // Pastelna kartica sa tamnim tekstom, kao krugovi na početnom ekranu
        int boja = ContextCompat.getColor(h.itemView.getContext(), o.boja);
        int tekst = Boje.tamna(boja);
        h.kartica.setCardBackgroundColor(Boje.pastel(boja));
        h.naziv.setTextColor(tekst);
        h.opis.setTextColor(tekst);
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

        h.kartica.setOnClickListener(v -> slusalac.naOblast(o));
    }

    @Override
    public int getItemCount() {
        return oblasti.size();
    }

    static class Drzac extends RecyclerView.ViewHolder {
        final KvadratnaKartica kartica;
        final TextView simbol;
        final ImageView simbolSlika;
        final TextView naziv;
        final TextView opis;

        Drzac(@NonNull View v) {
            super(v);
            kartica = v.findViewById(R.id.kartica);
            simbol = v.findViewById(R.id.simbol);
            simbolSlika = v.findViewById(R.id.simbolSlika);
            naziv = v.findViewById(R.id.naziv);
            opis = v.findViewById(R.id.opis);
        }
    }
}
