#!/usr/bin/env python3
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

app = Dash(__name__, external_stylesheets=[dbc.themes.DARK])
fig = go.Figure(data=[go.Scatter3d(x=[], y=[], z=[], mode='lines+markers')])
fig.update_layout(
    scene=dict(xaxis_title='X Stretch', yaxis_title='Y Entropy', zaxis_title='Z V-Connectivity'),
    template='plotly_dark', title='RSRP Phase 1A — Live Telemetry'
)

app.layout = html.Div([
    html.H1("RSRP Phase 1A — Local Demo", style={'color':'#00ff88'}),
    dcc.Graph(figure=fig),
    dcc.Interval(interval=3000),
    html.Div("Demo mode — no participants yet", style={'color':'white','fontSize':24})
], style={'backgroundColor':'#000'})

if __name__ == '__main__':
    print("Dashboard live → http://127.0.0.1:8050")
    app.run_server(debug=False)
