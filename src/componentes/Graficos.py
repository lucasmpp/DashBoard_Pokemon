from re import template
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc

import plotly.express as px
import plotly.graph_objs as go

from .funcoes_gerais import filtragem

CORES_TIPOS = {
    'normal': '#A8A77A',
    'fire': '#EE8130',
    'water': '#6390F0',
    'electric': '#F7D02C',
    'grass': '#7AC74C',
    'ice': '#96D9D6',
    'fighting': '#C22E28',
    'poison': '#A33EA1',
    'ground': '#E2BF65',
    'flying': '#A98FF3',
    'psychic': '#F95587',
    'bug': '#A6B91A',
    'rock': '#B6A136',
    'ghost': '#735797',
    'dragon': '#6F35FC',
    'dark': '#705746',
    'steel': '#B7B7CE',
    'fairy': '#D685AD',
}

def grafico_radar_comparacao(dados, tipos):
    maximo_grafico = 0

    def layer_do_tipo(tipo):
        nonlocal maximo_grafico

        filtrado = dados.query('(type1 == @tipo) or (type2 == @tipo)')
        dict_medidas_resumo = (
            filtrado
            .loc[:, ['attack','defense','sp_attack','sp_defense','speed','hp']]
            .mean()
            .to_dict()
        )

        maximo_grafico = max(maximo_grafico, *dict_medidas_resumo.values())
        return go.Scatterpolar(
            name=tipo.capitalize(),
            r = [
                dict_medidas_resumo['hp'],
                dict_medidas_resumo['attack'],
                dict_medidas_resumo['defense'],
                dict_medidas_resumo['sp_attack'],
                dict_medidas_resumo['sp_defense'],
                dict_medidas_resumo['speed'],
                dict_medidas_resumo["hp"]
            ],
            theta = ['Vida', 'Ataque', 'Defesa', 'Ataque Especial',
                     'Defesa Especial', 'Velocidade', 'Vida'],
            fill = 'toself',
            line =  dict(color = CORES_TIPOS[tipo])
        )

    dados = [layer_do_tipo(tipo) for tipo in tipos]
    
    layout = go.Layout(
        polar = dict(
            radialaxis = dict(
            visible = True,
            range = [10, maximo_grafico*1.2]
            )
        ),
        showlegend = True,
        paper_bgcolor= "rgba(0,0,0,0)",
        template="plotly_dark"
    )

    fig = go.Figure(data=dados, layout=layout)
    return fig

def chart_catch_x_tot(df,tipos):
    def parse_dados(df, __tipo__):
        df = df.query('type1 == @__tipo__ | type2 == @__tipo__')
        df = df.loc[:, ['name', 'capture_rate', 'base_total']]
        
        return df

    layout = go.Layout(
        paper_bgcolor= "rgba(0,0,0,0)",
        template="plotly_dark"
    )
    fig = go.Figure(layout=layout)
    for tipo in tipos:
        df1 = parse_dados(df, tipo)
        fig.add_trace(go.Scatter(
            x=df1.capture_rate.astype(int),
            y=df1.base_total,
            hovertext=df1.name,
            name=tipo,
            marker_color=CORES_TIPOS[tipo]
        ))
    fig.update_traces(mode = 'markers')
    fig.update_xaxes(title_text='Facilidade de captura', 
                     categoryorder='category ascending')
    fig.update_yaxes(title_text='Atributos totais')
    return fig

def chart_egg_x_tot(df):
    x = df.base_egg_steps
    y = df.base_total
    fig = px.box(df, x=x, y=y, hover_name=df.name, template='plotly_dark', 
                 category_orders={
                     "base_egg_steps":["1280","2560","3840","5120","6400",
                                       "7680","8960","10240","20480","30720"]
                 })
    fig.update_xaxes(title_text='Número de passos para chocar o ovo', 
                     type='category')
    fig.update_yaxes(title_text='Atributos totais')
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
    return fig

def chart_egg_x_catch(df):
    y = df.capture_rate.astype(int)
    x = df.base_egg_steps
    fig = px.box(df, x=x, y=y, hover_name=df.name,template='plotly_dark', 
                 category_orders={
                     "base_egg_steps":["1280","2560","3840","5120","6400",
                                       "7680","8960","10240","20480","30720"]
                 })
    fig.update_xaxes(title_text='Número de passos para chocar o ovo', 
                     type='category')
    fig.update_yaxes(title_text='Facilidade de captura')
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
    return fig

def _Graficos(app, data):
    @app.callback(
        Output('graph_1', 'figure'),
        [Input('submit_button', 'n_clicks')],
        [
        State('tipo', 'value'),State('geracao','value'),State('lendario','value')
        ])
    def update_graph_1(_: str('n_clicks'), tipo_value, geracao_value,leg_value):
        dados, tipo = filtragem(data,tipo_value, geracao_value,leg_value)
        
        return chart_catch_x_tot(dados,tipo)


    @app.callback(
        Output('graph_2', 'figure'),
        [Input('submit_button', 'n_clicks')],
        [
        State('tipo', 'value'),State('geracao','value'),State('lendario','value')
        ])
    def update_graph_1(_: str('n_clicks'), tipo_value, geracao_value,lendario_value):
        dados,tipo = filtragem(data,tipo_value, geracao_value,lendario_value)
        
        return grafico_radar_comparacao(dados,tipo)

    @app.callback(
        Output('graph_3', 'figure'),
        [Input('submit_button', 'n_clicks')],
        [
        State('tipo', 'value'),State('geracao','value'),State('lendario','value')
        ])
    def update_graph_1(_: str('n_clicks'), tipo_value, geracao_value,lendario_value):
        dados, _ = filtragem(data,tipo_value, geracao_value,lendario_value)
        
        return chart_egg_x_tot(dados)

    @app.callback(
        Output('graph_4', 'figure'),
        [Input('submit_button', 'n_clicks')],
        [
        State('tipo', 'value'),State('geracao','value'),State('lendario','value')
        ])
    def update_graph_1(_: str('n_clicks'), tipo_value, geracao_value,lendario_value):
        dados, _ = filtragem(data,tipo_value, geracao_value,lendario_value)
        
        return chart_egg_x_catch(dados)

    content_second_row = dbc.Row([
        dbc.Col(dcc.Graph(id = 'graph_1'), md = 6),
        dbc.Col(dcc.Graph(id = 'graph_2'),md = 6)
    ])

    content_third_row = dbc.Row([
        dbc.Col(dcc.Graph(id = 'graph_3'), md=12)
    ])

    content_fourth_row = dbc.Row([
        dbc.Col(dcc.Graph(id = 'graph_4'), md=12)
    ])

    return content_second_row, content_third_row, content_fourth_row