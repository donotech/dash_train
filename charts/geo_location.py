from dash import Dash, dcc, html
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)
geo_path = "C:\\devraj\\pyspark_training\\datasets\\ml_dataset\\Melbourne_house_price.csv"
df_full = pd.read_csv(geo_path)
df = df_full.sample(10000)

df['text'] = df['Suburb'] + ', ' + df['Regionname']

fig = go.Figure(data=go.Scattergeo(
    lon=df['Longtitude'],
    lat=df['Lattitude'],
    text=df['text'],
    mode='markers'
    # marker_color=df['Temp_C_ML']
))

fig.update_layout(
    geo_scope='world'
)

app.layout = html.Div(children=[
    html.H1(children='melbourne'),
    html.Div(children='''
        This data was provided by the USGS.
    '''),

    dcc.Graph(
        id='example-map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)