import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

def _Checkbox(titulo, id, opcoes, valores_iniciais):
    cabecalho = html.P(titulo, className='input-title')
    corpo = dbc.Card([
        dcc.Dropdown(
            id=id,
            options=opcoes,
            value=valores_iniciais,
            multi=True
        )
    ], className="filter-input")

    return cabecalho, corpo
        