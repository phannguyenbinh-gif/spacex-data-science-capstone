from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

DATA = Path(__file__).resolve().parent / "data" / "spacex_launch_dash.csv"
df = pd.read_csv(DATA)
app = Dash(__name__)

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={"textAlign":"center"}),
    html.Label("Launch Site"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label":"All Sites","value":"ALL"}] +
                [{"label":s,"value":s} for s in sorted(df.LaunchSite.unique())],
        value="ALL", clearable=False),
    html.Label("Payload Range"),
    dcc.RangeSlider(id="payload-slider",
        min=float(df.PayloadMass.min()), max=float(df.PayloadMass.max()),
        value=[float(df.PayloadMass.min()),float(df.PayloadMass.max())]),
    dcc.Graph(id="success-pie-chart"),
    dcc.Graph(id="success-payload-scatter-chart")
])

@app.callback(
    Output("success-pie-chart","figure"),
    Output("success-payload-scatter-chart","figure"),
    Input("site-dropdown","value"),
    Input("payload-slider","value")
)
def update_dashboard(site, payload_range):
    dff=df[df.PayloadMass.between(payload_range[0],payload_range[1])]
    if site!="ALL":
        dff=dff[dff.LaunchSite==site]
    pie=px.pie(dff,names="Class",title=f"Landing Outcomes - {site}")
    scatter=px.scatter(dff,x="PayloadMass",y="Class",color="Orbit",
                       hover_data=["LaunchSite","FlightNumber"],
                       title=f"Payload Mass vs Landing Outcome - {site}")
    return pie,scatter

if __name__ == "__main__":
    app.run(debug=True)
