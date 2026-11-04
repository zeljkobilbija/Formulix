package com.zeljkobilbija001.formulix;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.ColorStateList;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.os.Build;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.os.ConfigurationCompat;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.math.BigDecimal;
import java.math.MathContext;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/**
 * Ekran "Jedinice": izbor kategorije (pastelni krugovi), unos vrednosti i jedinice,
 * i lista preračuna u sve ostale jedinice te kategorije.
 * Dodir na preračun ga uzima kao novi unos; dugi dodir kopira vrednost.
 */
public class KonverterActivity extends AppCompatActivity {

    private static final String PODESAVANJA = "konverter";

    public static Intent namera(Context c) {
        return new Intent(c, KonverterActivity.class);
    }

    private View koren, zaglavlje;
    private LinearLayout kategorijeRed;
    private EditText unos;
    private TextView jedinicaIz;
    private ImageView strelicaIzbora;
    private View izborJedinice;
    private final RezultatiAdapter adapter = new RezultatiAdapter();

    private Jedinice.Kategorija kategorija;
    private int izJedinice;
    private Locale jezik;
    private float dp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_konverter);
        dp = getResources().getDisplayMetrics().density;
        jezik = ConfigurationCompat.getLocales(getResources().getConfiguration()).get(0);

        koren = findViewById(R.id.koren);
        zaglavlje = findViewById(R.id.zaglavlje);
        kategorijeRed = findViewById(R.id.kategorije);
        unos = findViewById(R.id.vrednost);
        jedinicaIz = findViewById(R.id.jedinicaIz);
        strelicaIzbora = findViewById(R.id.strelicaIzbora);
        izborJedinice = findViewById(R.id.izborJedinice);

        Boje.obojenoZaglavlje(this, koren, zaglavlje, Jedinice.SVE.get(0).boja);
        ((TextView) findViewById(R.id.podnaslov)).setText(R.string.opis_jedinice);
        findViewById(R.id.nazad).setOnClickListener(v -> finish());

        RecyclerView lista = findViewById(R.id.rezultati);
        lista.setLayoutManager(new LinearLayoutManager(this));
        lista.setAdapter(adapter);

        postaviKategorije();
        izborJedinice.setOnClickListener(v -> izaberiJedinicu());
        unos.setSelectAllOnFocus(true); // novi unos zamenjuje stari broj

        // Dok je tastatura otvorena: bez reda kategorija i banera, da se vidi više preračuna
        View traka = findViewById(R.id.kategorijeTraka);
        View baner = findViewById(R.id.reklamaKontejner);
        ViewCompat.setOnApplyWindowInsetsListener(traka, (v, insets) -> {
            int vidljivo = insets.isVisible(WindowInsetsCompat.Type.ime()) ? View.GONE : View.VISIBLE;
            if (traka.getVisibility() != vidljivo) {
                traka.post(() -> {
                    traka.setVisibility(vidljivo);
                    baner.setVisibility(vidljivo);
                });
            }
            return insets;
        });

        unos.addTextChangedListener(new TextWatcher() {
            @Override public void beforeTextChanged(CharSequence s, int a, int b, int c) { }
            @Override public void onTextChanged(CharSequence s, int a, int b, int c) { }
            @Override public void afterTextChanged(Editable s) { preracunaj(); }
        });

        // Poslednji izbor (čuva se samo na uređaju)
        SharedPreferences p = getSharedPreferences(PODESAVANJA, MODE_PRIVATE);
        int k = Math.max(0, Math.min(Jedinice.SVE.size() - 1, p.getInt("kategorija", 0)));
        izaberiKategoriju(k, p.getInt("jedinica", -1));
        unos.setText(p.getString("vrednost", "1"));
        unos.setSelection(unos.getText().length());

        Reklame.prikaziBaner(this, findViewById(R.id.reklamaKontejner));
    }

    @Override
    protected void onPause() {
        super.onPause();
        getSharedPreferences(PODESAVANJA, MODE_PRIVATE).edit()
                .putInt("kategorija", Jedinice.SVE.indexOf(kategorija))
                .putInt("jedinica", izJedinice)
                .putString("vrednost", unos.getText().toString())
                .apply();
    }

    /** Red pastelnih krugova sa nazivom ispod, po jedan za svaku kategoriju. */
    private void postaviKategorije() {
        int krug = Math.round(58 * dp);
        for (int i = 0; i < Jedinice.SVE.size(); i++) {
            Jedinice.Kategorija k = Jedinice.SVE.get(i);
            LinearLayout stavka = new LinearLayout(this);
            stavka.setOrientation(LinearLayout.VERTICAL);
            stavka.setGravity(Gravity.CENTER_HORIZONTAL);
            stavka.setClipChildren(false);
            stavka.setClipToPadding(false);
            stavka.setPadding(Math.round(4 * dp), Math.round(4 * dp), Math.round(4 * dp), 0);
            stavka.setLayoutParams(new LinearLayout.LayoutParams(Math.round(80 * dp),
                    ViewGroup.LayoutParams.WRAP_CONTENT));

            KrugView k1 = new KrugView(this);
            k1.postaviBoju(k.boja);
            k1.setForeground(getDrawable(R.drawable.krug_talas));
            TextView simbol = new TextView(this);
            simbol.setText(k.simbol);
            simbol.setTextColor(Boje.tamna(k.boja));
            simbol.setTypeface(Typeface.create("sans-serif-medium", Typeface.BOLD));
            simbol.setTextSize(TypedValue.COMPLEX_UNIT_SP, k.simbol.length() > 3 ? 13 : 17);
            k1.addView(simbol, new android.widget.FrameLayout.LayoutParams(
                    ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT,
                    Gravity.CENTER));
            stavka.addView(k1, new LinearLayout.LayoutParams(krug, krug));

            TextView naziv = new TextView(this);
            naziv.setText(k.naziv);
            naziv.setTextSize(TypedValue.COMPLEX_UNIT_SP, 12);
            naziv.setGravity(Gravity.CENTER_HORIZONTAL);
            naziv.setMaxLines(2);
            naziv.setTextColor(getColor(R.color.tekst_sekundarni));
            LinearLayout.LayoutParams pn = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
            pn.topMargin = Math.round(6 * dp);
            stavka.addView(naziv, pn);

            final int indeks = i;
            k1.setOnClickListener(v -> izaberiKategoriju(indeks, -1));
            kategorijeRed.addView(stavka);
        }
    }

    /** Menja kategoriju: boje ekrana, izabrani krug, jedinica i preračuni. */
    private void izaberiKategoriju(int indeks, int jedinica) {
        Jedinice.Kategorija nova = Jedinice.SVE.get(indeks);
        boolean promena = nova != kategorija;
        kategorija = nova;
        izJedinice = jedinica >= 0 && jedinica < nova.jedinice.size() ? jedinica : nova.podrazumevana;

        Boje.oboji(koren, zaglavlje, nova.boja);
        ((TextView) findViewById(R.id.naslov)).setText(nova.naziv);

        for (int i = 0; i < kategorijeRed.getChildCount(); i++) {
            LinearLayout stavka = (LinearLayout) kategorijeRed.getChildAt(i);
            View krug = stavka.getChildAt(0);
            TextView naziv = (TextView) stavka.getChildAt(1);
            boolean izabrana = i == indeks;
            krug.animate().scaleX(izabrana ? 1.12f : 0.92f).scaleY(izabrana ? 1.12f : 0.92f)
                    .setDuration(220).start();
            krug.setElevation((izabrana ? 8 : 2) * dp);
            naziv.setTypeface(null, izabrana ? Typeface.BOLD : Typeface.NORMAL);
            naziv.setTextColor(izabrana ? Boje.tamna(nova.boja) : getColor(R.color.tekst_sekundarni));
        }
        if (promena) {
            View stavka = kategorijeRed.getChildAt(indeks);
            stavka.post(() -> stavka.requestRectangleOnScreen(
                    new android.graphics.Rect(0, 0, stavka.getWidth(), stavka.getHeight()), false));
        }

        // Dugme za jedinicu u pastelnoj boji kategorije
        GradientDrawable dugme = new GradientDrawable();
        dugme.setCornerRadius(22 * dp);
        dugme.setColor(Boje.pastel(nova.boja));
        izborJedinice.setBackground(dugme);
        jedinicaIz.setTextColor(Boje.tamna(nova.boja));
        strelicaIzbora.setImageTintList(ColorStateList.valueOf(Boje.tamna(nova.boja)));
        unos.setTextColor(Boje.tamna(nova.boja));
        prikaziJedinicu();
        preracunaj();
    }

    private void prikaziJedinicu() {
        Jedinice.Jedinica j = kategorija.jedinice.get(izJedinice);
        jedinicaIz.setText(j.simbol + "  ·  " + getString(j.naziv));
    }

    private void izaberiJedinicu() {
        List<Jedinice.Jedinica> sve = kategorija.jedinice;
        CharSequence[] stavke = new CharSequence[sve.size()];
        for (int i = 0; i < sve.size(); i++) {
            stavke[i] = sve.get(i).simbol + "  ·  " + getString(sve.get(i).naziv);
        }
        new AlertDialog.Builder(this)
                .setTitle(R.string.izaberi_jedinicu)
                .setSingleChoiceItems(stavke, izJedinice, (d, i) -> {
                    izJedinice = i;
                    prikaziJedinicu();
                    preracunaj();
                    d.dismiss();
                })
                .show();
    }

    /** Vrednost iz polja (prihvata i zarez i tačku); null ako nije broj. */
    private Double procitaj() {
        String s = unos.getText().toString().trim().replace(" ", "").replace(',', '.');
        if (s.isEmpty() || s.equals("-") || s.equals(".")) return null;
        try {
            return Double.parseDouble(s);
        } catch (NumberFormatException e) {
            return null;
        }
    }

    private void preracunaj() {
        Double v = procitaj();
        List<Double> iznosi = new ArrayList<>();
        Jedinice.Jedinica iz = kategorija.jedinice.get(izJedinice);
        for (Jedinice.Jedinica u : kategorija.jedinice) {
            iznosi.add(v == null ? null : u.izOsnovne(iz.uOsnovnu(v)));
        }
        adapter.postavi(kategorija, iznosi, izJedinice);
    }

    /** Broj sa najviše 10 značajnih cifara, u formatu jezika aplikacije; veoma veliki/mali eksponencijalno. */
    private String formatiraj(Double v) {
        if (v == null) return "";
        if (v.isNaN() || v.isInfinite()) return "—";
        if (v == 0) return "0";
        double a = Math.abs(v);
        BigDecimal b = new BigDecimal(v).round(new MathContext(10)).stripTrailingZeros();
        if (a >= 1e15 || a < 1e-7) {
            String e = String.format(Locale.ROOT, "%.6E", v);          // npr. 1.602177E-19
            String[] d = e.split("E");
            String mant = new BigDecimal(d[0]).stripTrailingZeros().toPlainString();
            NumberFormat nf = NumberFormat.getInstance(jezik);
            nf.setMaximumFractionDigits(6);
            mant = nf.format(Double.parseDouble(mant));
            return mant + " × 10" + superskript(Integer.parseInt(d[1]));
        }
        NumberFormat nf = NumberFormat.getInstance(jezik);
        nf.setMaximumFractionDigits(Math.max(0, b.scale()));
        nf.setGroupingUsed(true);
        return nf.format(b);
    }

    private static String superskript(int n) {
        String cifre = "⁰¹²³⁴⁵⁶⁷⁸⁹";
        StringBuilder s = new StringBuilder(n < 0 ? "⁻" : "");
        for (char c : String.valueOf(Math.abs(n)).toCharArray()) s.append(cifre.charAt(c - '0'));
        return s.toString();
    }

    /** Vrednost za ponovni unos (bez razdvajanja hiljada, sa tačkom ili zarezom jezika). */
    private String zaUnos(double v) {
        String s = new BigDecimal(v).round(new MathContext(10)).stripTrailingZeros().toPlainString();
        char zarez = java.text.DecimalFormatSymbols.getInstance(jezik).getDecimalSeparator();
        return zarez == ',' ? s.replace('.', ',') : s;
    }

    private void uzmiKaoUnos(int indeks, double v) {
        izJedinice = indeks;
        prikaziJedinicu();
        unos.setText(zaUnos(v));
        unos.setSelection(unos.getText().length());
    }

    private void kopiraj(String tekst) {
        ClipboardManager cm = (ClipboardManager) getSystemService(CLIPBOARD_SERVICE);
        cm.setPrimaryClip(ClipData.newPlainText(getString(R.string.oblast_jedinice), tekst));
        // Android 13+ sam prikazuje potvrdu kopiranja
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.TIRAMISU) {
            Toast.makeText(this, R.string.kopirano, Toast.LENGTH_SHORT).show();
        }
    }

    private class RezultatiAdapter extends RecyclerView.Adapter<RezultatiAdapter.Drzac> {
        private Jedinice.Kategorija k;
        private final List<Double> iznosi = new ArrayList<>();
        private int izabrana;

        @android.annotation.SuppressLint("NotifyDataSetChanged")
        void postavi(Jedinice.Kategorija k, List<Double> iznosi, int izabrana) {
            this.k = k;
            this.iznosi.clear();
            this.iznosi.addAll(iznosi);
            this.izabrana = izabrana;
            notifyDataSetChanged();
        }

        @NonNull
        @Override
        public Drzac onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            return new Drzac(LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.item_jedinica, parent, false));
        }

        @Override
        public void onBindViewHolder(@NonNull Drzac h, int position) {
            Jedinice.Jedinica j = k.jedinice.get(position);
            Double v = iznosi.get(position);
            String tekst = formatiraj(v);
            h.iznos.setText(tekst);
            h.simbol.setText(j.simbol);
            h.simbol.setTextColor(Boje.tamna(k.boja));
            h.naziv.setText(j.naziv);
            boolean ova = position == izabrana;
            h.kartica.setCardBackgroundColor(ova ? Boje.pastel(k.boja) : getColor(R.color.povrsina));
            h.iznos.setTextColor(ova ? Boje.tamna(k.boja) : getColor(R.color.tekst));
            h.kartica.setOnClickListener(x -> {
                if (v != null && !v.isNaN() && !v.isInfinite()) uzmiKaoUnos(position, v);
            });
            h.kartica.setOnLongClickListener(x -> {
                if (tekst.isEmpty()) return false;
                kopiraj(tekst + " " + j.simbol);
                return true;
            });
        }

        @Override
        public int getItemCount() {
            return k == null ? 0 : k.jedinice.size();
        }

        class Drzac extends RecyclerView.ViewHolder {
            final com.google.android.material.card.MaterialCardView kartica;
            final TextView iznos, simbol, naziv;

            Drzac(@NonNull View v) {
                super(v);
                kartica = v.findViewById(R.id.kartica);
                iznos = v.findViewById(R.id.iznos);
                simbol = v.findViewById(R.id.simbol);
                naziv = v.findViewById(R.id.naziv);
            }
        }
    }
}
