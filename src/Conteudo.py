import dash_html_components as html

from .leitura_dados import ler_dados
from .componentes import _CardsCabecalho, _Graficos

data = ler_dados()

def conteudo(app):
    cards_header = _CardsCabecalho(app, data)
    primeiro_grafico, segundo_grafico, terceiro_grafico = _Graficos(app, data)

    conteudo = html.Div(className='main-content', children=[
        html.H2('DashBoard Pokemon', className='title'),
        html.Hr(),
        cards_header,
        primeiro_grafico,
        segundo_grafico,
        terceiro_grafico
    ])

    return conteudo