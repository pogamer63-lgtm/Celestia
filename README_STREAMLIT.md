# Celestia Streamlit App

## Lokal starten
1. Terminal in den Projektordner:
   ```powershell
   cd C:\Users\001123470\pyton\Celestia
   ```
2. Abhaengigkeiten installieren:
   ```powershell
   pip install -r requirements.txt
   ```
3. App starten:
   ```powershell
   streamlit run app.py
   ```

## Wrapper Prinzip
- `app.py` ist nur der Streamlit-Wrapper.
- Deine statische Website (`index.html`, `collections.html`, ...) bleibt das eigentliche Frontend.
- Beim Start synchronisiert `app.py` die Dateien automatisch nach `static/` und rendert die Website direkt per `st.html` (ohne iframe), damit Navigation und Scrollbar sauber bleiben.
- Interne Navigation bleibt ueber Query-Parameter (`?page=...`) und nutzt Prefetch/Caching fuer schnellere Seitenwechsel.

## Deploy (Streamlit Community Cloud)
1. Projekt zu GitHub pushen.
2. In Streamlit Cloud "New app" waehlen.
3. Repository verbinden.
4. Als Main file `app.py` setzen.
5. Deploy ausfuehren.

## Logo
- Datei: `assets/celestia-logo.png`
- Wird automatisch in der Hero-Sektion angezeigt.
