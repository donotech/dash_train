from dash import Dash, dcc, html
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)
geo_path = "C:\\Training\\TVS\\dataset\\CAPSTONE PROJECT\\CAPSTONE " \
           "PROJECT\\BrazilianECommerce_G1\\data\\olist_geolocation_dataset.csv"
df_full = pd.read_csv(geo_path)
df = df_full.sample(10000)

df['text'] = df['geolocation_city'] + ', ' + df['geolocation_state']

fig = go.Figure(data=go.Scattergeo(
    lon=df['geolocation_lng'],
    lat=df['geolocation_lat'],
    text=df['text'],
    mode='markers'
    # marker_color=df['Temp_C_ML']
))

fig.update_layout(
    geo_scope='south america'
)

app.layout = html.Div(children=[
    html.H1(children='Identified Geothermal Systems of the Western USA'),
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