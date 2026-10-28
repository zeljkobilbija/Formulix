package com.zeljkobilbija001.formulix;

/** Jedna tema unutar oblasti (npr. Procenti u Aritmetici), tekstovi već na jeziku aplikacije. */
public class Tema {

    public final String oblastId;
    public final String id;
    public final String simbol;
    /** Ime vektorske ikonice (npr. "ic_f_kvadrat") ili prazno; tada se prikazuje simbol. */
    public final String ikona;
    public final String naziv;
    public final String opis;
    /** Normalizovan tekst za pretragu (naziv, opis, ključne reči, naziv oblasti). */
    public final String zaPretragu;

    public Tema(String oblastId, String id, String simbol, String ikona,
                String naziv, String opis, String zaPretragu) {
        this.oblastId = oblastId;
        this.id = id;
        this.simbol = simbol;
        this.ikona = ikona;
        this.naziv = naziv;
        this.opis = opis;
        this.zaPretragu = zaPretragu;
    }
}
