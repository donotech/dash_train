from dash import Dash
import flask
from dash import html

server = flask.Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/ATM_Data_Anlaysis/')
app.layout = html.Div([html.H1('This Is head', style={'textAlign':'center'})])


@server.route("/dash")
def MyDashApp():
    return app.index()


if __name__ == '__main__':
    app.run_server(debug=True)