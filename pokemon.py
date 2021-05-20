import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from src.Filtros import filtros
from src.Conteudo import conteudo

app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
app.layout = html.Div([filtros, conteudo(app)])

if __name__ == '__main__':
    app.run_server(port='8050', debug=False)