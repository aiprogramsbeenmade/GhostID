# 🕵️‍♂️ GhostID: Professional Identity Framework

**GhostID** è un framework avanzato in Python progettato per la generazione di identità sintetiche ultra-realistiche. A differenza dei comuni generatori di dati casuali, GhostID garantisce la coerenza algoritmica, geografica e digitale di ogni profilo, rendendolo indistinguibile da un'identità reale in contesti di test e simulazione.

---

## 🚀 Caratteristiche Principali

* **Identità Multilivello**: Generazione di profili completi (Anagrafica, Istruzione, Carriera, Finanze).
* **Codice Fiscale Reale**: Algoritmo proprietario per il calcolo del CF italiano (omocodia esclusa) con validazione di genere e data.
* **Geolocalizzazione OSM**: Integrazione con **OpenStreetMap** per fornire indirizzi reali e coordinate GPS precise.
* **Ecosistema Social**: Generazione di handle e URL coerenti per LinkedIn, Instagram, Facebook e X.
* **Digital Fingerprint**: Simulazione tecnica di User-Agent, IP locali e chiavi SSH RSA.
* **Dossier Reporting**: Esportazione automatica in formato `.txt` formattato stile agenzia governativa.
* **Validazione Pydantic**: Architettura basata su modelli rigorosi per garantire l'integrità del dato.

---

## 📂 Struttura del Progetto

```text
GhostID/
├── data/
│   └── dossiers/          # Archivio dei dossier generati (.txt)
├── src/
│   ├── providers/         # Client API (OSMClient)
│   ├── generator.py       # Motore logico di generazione
│   ├── models.py          # Modelli Pydantic (Data Schema)
│   └── utils.py           # Utility di formattazione
├── main.py                # Entry point per generazione locale
└── requirements.txt       # Dipendenze del progetto
```

---

## 🛠️ Installazione
1. **Clona il repository:**
   ```bash
   git clone https://github.com/aiprogramsbeenmade/GhostID.git
   cd GhostID
2. **Crea un ambiente virtuale:**
    ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. **Installa le dipendenze:**
    ```bash
   pip install -r requirements.txt

---
## 🖥️ Utilizzo
**Per generare un singolo dossier e archiviarlo:**
```bash
python main.py
```

**Esempio di Output:**
```bash
[ANAGRAFICA]
Nome: Rita Cagnotto             Genere: F
Data di Nascita: 1986-06-02     Luogo: Fabiano
Codice Fiscale: CGNRTI86H42H501Z Documento: ND24823HG

[DIGITAL FINGERPRINT]
Local IP: 192.168.1.167         Lang: it-IT
User-Agent: Mozilla/5.0 (X11; Linux x86_64)...
```

---

## ⚖️ Disclaimer
Questo progetto è creato a scopo educativo e di test. L'autore non è responsabile per l'uso improprio delle informazioni generate. I dati prodotti sono sintetici e non appartengono a persone reali.
