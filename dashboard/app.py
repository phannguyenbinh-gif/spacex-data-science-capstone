from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_launches.csv"
df = pd.read_csv(DATA)

app = Dash(__name__)
sites = ["ALL"] + sorted(df["LaunchSite"].unique().tolist())

app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Landing Dashboard"),
    dcc.Dropdown(sites, "ALL", id="site"),
    dcc.Graph(id="success-pie"),
    dcc.Graph(id="payload-scatter"),
])

@app.callback(
    Output("success-pie", "figure"),
    Output("payload-scatter", "figure"),
    Input("site", "value"),
)
def update(site):
    dff = df if site == "ALL" else df[df["LaunchSite"] == site]
    pie = px.pie(dff, names="Class", title="Landing Outcome Distribution")
    scatter = px.scatter(
        dff, x="PayloadMass", y="Class", color="Orbit",
        hover_data=["LaunchSite", "FlightNumber"],
        title="Payload Mass vs Landing Class"
    )
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)
