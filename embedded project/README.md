# EV Market Analysis — Tableau + Flask

A small Flask website that embeds the EV Market Analysis Tableau Public dashboard and story.

## Folder structure

```text
EV_Market_Tableau_Flask/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally

1. Install Python 3.10 or newer.
2. Open this folder in Visual Studio Code.
3. Open the terminal in VS Code.
4. Create and activate a virtual environment (optional but recommended):

   **Windows**
   ```powershell
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

5. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

6. Start the website:
   ```powershell
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Tableau views

- Story: https://public.tableau.com/views/EVMarketAnalysisSalesTechnologySustainability/Story6
- Dashboard: https://public.tableau.com/views/EVMarketAnalysisSalesTechnologySustainability/EVMarketAnalysisDashboard

The Tableau views must be published and accessible to the public. If they do not appear embedded, verify the view's permissions and open the direct Tableau Public link.

## Technologies

- Python and Flask
- HTML
- CSS
- Tableau Public Embedding API v3
- Visual Studio Code (development environment)

- Tableau Public project workspace: https://public.tableau.com/app/profile/swayam.bhandari/viz/EVMarketAnalysisSalesTechnologySustainability/Story6
