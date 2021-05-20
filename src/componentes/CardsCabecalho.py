import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from .Card import card
from .funcoes_gerais import filtragem

def plural(valor):
    return 's' if valor > 1 else ''

def quantidade(dados): 
    qtd = dados.shape[0]
    return f"{qtd} Pokemon{plural(qtd)} encontrado{plural(qtd)}"

def alt_media(dados):
    alt = dados['height_m'].mean()   
    return f"{round(alt,2)} metro{plural(alt)}"

def peso_media(dados):
    peso = dados['weight_kg'].mean()
    return f"{round(peso,2)} kg{plural(peso)}"

def _CardsCabecalho(app, data):
    @app.callback(
        Output('card_qtd', 'children'),
        [Input('submit_button', 'n_clicks')],
        [State('tipo', 'value'),State('geracao','value'),State('lendario','value')]
    )
    def update_card_qtd(_: str('n_clicks'), tipo_value, geracao_value,leg_value):
        dados, _ = filtragem(data,tipo_value, geracao_value,leg_value)
        return quantidade(dados)


    @app.callback(
        Output('card_alt', 'children'),
        [Input('submit_button', 'n_clicks')],
        [State('tipo', 'value'),State('geracao','value'),State('lendario','value')]
    )
    def update_card_alt(_: str('n_clicks'), tipo_value, geracao_value,leg_value):
        dados, _ = filtragem(data,tipo_value, geracao_value,leg_value)
        return alt_media(dados)


    @app.callback(
        Output('card_peso', 'children'),
        [Input('submit_button', 'n_clicks')],
        [State('tipo', 'value'),State('geracao','value'),State('lendario','value')]
    )
    def update_card_peso(_: str('n_clicks'), tipo_value, geracao_value,leg_value):
        dados, _ = filtragem(data,tipo_value, geracao_value,leg_value)
        return peso_media(dados)
    
    return dbc.Row([
        card('Quantidade', 'card_qtd'),
        card('Altura Média', 'card_alt'),
        card('Peso Médio', 'card_peso')
    ])