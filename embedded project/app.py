from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public views supplied for the EV Market Analysis project.
TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/EVMarketAnalysisSalesTechnologySustainability/"
    "Story6?:language=en-US&:showVizHome=no"
)
TABLEAU_WORKSPACE_URL = "https://public.tableau.com/app/profile/swayam.bhandari/viz/EVMarketAnalysisSalesTechnologySustainability/Story6"
TABLEAU_DASHBOARD_URL = (
    "https://public.tableau.com/views/EVMarketAnalysisSalesTechnologySustainability/"
    "EVMarketAnalysisDashboard?:language=en-US&:showVizHome=no"
)

@app.route("/")
def home():
    return render_template(
        "index.html",
        story_url=TABLEAU_STORY_URL,
        dashboard_url=TABLEAU_DASHBOARD_URL,
        workspace_url=TABLEAU_WORKSPACE_URL,
    )

if __name__ == "__main__":
    app.run(debug=True)
