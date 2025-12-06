#!/usr/bin/env python3
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import threading, time, json

app = dash.Dash(__name__, title="spiralcore — live telemetry")
fig = go.Figure(data=[go.Scatter3d(x=[], y=[], z=[], mode='lines+markers')])
fig.update_layout(scene=dict(xaxis_title='X Stretch', yaxis_title='Y Entropy', zaxis_title='Z V-Connectivity'),
                  template='plotly_dark')

app.layout = html.Div([
    html.H1("spiralcore — Phase 1A Live Telemetry", style={'color':'#00ff88','textAlign':'center'}),
    dcc.Graph(figure=fig, style={'height':'80vh'}),
    dcc.Interval(id='interval', interval=2000, n_intervals=0),
    html.Div(id='metrics', style={'color':'white','fontSize':24,'textAlign':'center'})
])

@app.callback([Output('metrics','children'), Output('figure','data')],
              Input('interval','n_intervals'))
def update(n):
    # placeholder — real metrics will be injected by measurement scripts
    data = json.loads(open("participants/metrics.json","r").read()) if open("participants/metrics.json","a+").tell() else {}
    text = f"ΔV: {data.get('delta_v',0):.2f} | λ₁: {data.get('lyapunov',0):.4f} | Diversity: {data.get('variance',1):.3f}"
    return text, [go.Scatter3d(x=[4.2], y=[1.8], z=[5.9], mode='markers', marker=dict(size=10,color='red'))]

if __name__ == '__main__':
    print("Dashboard → http://127.0.0.1:8050")
    app.run_server(debug=False)
