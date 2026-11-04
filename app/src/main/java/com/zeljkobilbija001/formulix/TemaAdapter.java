package com.zeljkobilbija001.formulix;

import android.content.res.ColorStateList;
import android.graphics.drawable.GradientDrawable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

/**
 * Teme u dva oblika: pastelni krugovi u dve kolone (ekran oblasti)
 * ili redovi liste (rezultati pretrage na početnom ekranu).
 */
public class TemaAdapter extends RecyclerView.Adapter<TemaAdapter.Drzac> {

    public interface KlikNaTemu {
        /** krug: okrugla površina stavke (za prelaz), ili cela stavka u listi. */
        void naTemu(Tema tema, View krug);
    }

    private final List<Tema> teme = new ArrayList<>();
    private final boolean kaoLista;
    private final KlikNaTemu slusalac;

    public TemaAdapter(boolean kaoLista, KlikNaTemu slusalac) {
        this.kaoLista = kaoLista;
        this.slusalac = slusalac;
    }

    public void postavi(List<Tema> nove) {
        teme.clear();
        teme.addAll(nove);
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public Drzac onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        int raspored = kaoLista ? R.layout.item_rezultat : R.layout.item_krug_mreza;
        View v = LayoutInflater.from(parent.getContext()).inflate(raspored, parent, false);
        return new Drzac(v);
    }

    @Override
    public void onBindViewHolder(@NonNull Drzac h, int position) {
        Tema t = teme.get(position);
        Oblast o = Oblasti.poId(t.oblastId);
        int boja = ContextCompat.getColor(h.itemView.getContext(),
                o != null ? o.boja : R.color.aritmetika);

        int ikona = t.ikona.isEmpty() ? 0 : h.itemView.getResources().getIdentifier(
                t.ikona, "drawable", h.itemView.getContext().getPackageName());
        if (ikona != 0) {
            // Figura (npr. kvadrat) kao vektorska ikonica u boji oblasti
            h.simbol.setVisibility(View.GONE);
            h.simbolSlika.setVisibility(View.VISIBLE);
            h.simbolSlika.setImageResource(ikona);
            h.simbolSlika.setImageTintList(ColorStateList.valueOf(kaoLista ? boja : Boje.tamna(boja)));
        } else {
            h.simbolSlika.setVisibility(View.GONE);
            h.simbol.setVisibility(View.VISIBLE);
            h.simbol.setText(t.simbol);
            h.simbol.setTextColor(kaoLista ? boja : Boje.tamna(boja));
            h.simbol.setTextSize(t.simbol.length() > 2 ? (kaoLista ? 15 : 22) : (kaoLista ? 22 : 34));
        }
        if (h.simbolPozadina instanceof KrugView) {
            ((KrugView) h.simbolPozadina).postaviBoju(boja);
        } else {
            GradientDrawable pozadina = new GradientDrawable();
            pozadina.setCornerRadius(h.itemView.getResources().getDisplayMetrics().density * 14);
            pozadina.setColor(Boje.providna(boja, 0x24));
            h.simbolPozadina.setBackground(pozadina);
        }

        h.naziv.setText(t.naziv);
        if (kaoLista && o != null) {
            h.opis.setText(h.itemView.getContext().getString(o.naziv) + " · " + t.opis);
        } else {
            h.opis.setText(t.opis);
        }
        View krug = kaoLista ? h.itemView : h.simbolPozadina;
        h.itemView.setOnClickListener(v -> slusalac.naTemu(t, krug));
        h.simbolPozadina.setOnClickListener(v -> slusalac.naTemu(t, krug));
    }

    @Override
    public int getItemCount() {
        return teme.size();
    }

    static class Drzac extends RecyclerView.ViewHolder {
        final View simbolPozadina;
        final TextView simbol;
        final ImageView simbolSlika;
        final TextView naziv;
        final TextView opis;

        Drzac(@NonNull View v) {
            super(v);
            simbolPozadina = v.findViewById(R.id.simbolPozadina);
            simbol = v.findViewById(R.id.simbol);
            simbolSlika = v.findViewById(R.id.simbolSlika);
            naziv = v.findViewById(R.id.naziv);
            opis = v.findViewById(R.id.opis);
        }
    }
}
