
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from funcoes_pokemon import *
import plotly.express as px

import pandas as pd
from unidecode import unidecode


############ dados
data = pd.read_csv('C:\\Users\\Lucas\\Documents\\UNB\\CE2py\\pokemon.csv')

tipo = ['fire','water','grass']
radar = grafico_radar_comparacao(data, tipo)
graf2 = chart_catch_x_tot(data, tipo)
graf3 = chart_egg_x_tot(data)
graf4 = chart_egg_x_catch(data)
# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.FormGroup(
    [

        html.P('Natureza', style={
            'textAlign': 'center'
        }),
        dbc.Card([dcc.Dropdown(
    id='tipo',
    options=[
        {'label': 'Fogo', 'value': 'fire'},
        {'label': 'Água', 'value': 'water'},
        {'label': 'Planta', 'value': 'grass'},
        {'label': 'Elétrico', 'value': 'electric'},
        {'label': 'Pedra', 'value': 'rock'},
        {'label': 'Fantasma', 'value': 'ghost'},
        {'label': 'Normal', 'value': 'normal'},
        {'label': 'Lutador', 'value': 'fighting'},
        {'label': 'Voador', 'value': 'flying'},
        {'label': 'Venenoso', 'value': 'poison'},
        {'label': 'Terrestre', 'value': 'ground'},
        {'label': 'Inseto', 'value': 'bug'},
        {'label': 'Aço', 'value': 'steel'},
        {'label': 'Psíquico', 'value': 'psychic'},
        {'label': 'Gelo', 'value': 'ice'},
        {'label': 'Fada', 'value': 'fairy'},
        {'label': 'Dragão', 'value': 'dragon'},
        {'label': 'Noturno', 'value': 'dark'}
    ],
    value=['fire','water'],
    multi=True,
    
)]) ,
 
        html.Br(),
        html.P('Geração', style={
            'textAlign': 'center'
        }),
        dbc.Card([dcc.Dropdown(
    id='geracao',        
    options=[
        {'label': 'Primeira', 'value': 1},
        {'label': 'Segunda', 'value': 2},
        {'label': 'Terceira', 'value': 3},
        {'label': 'Quarta', 'value': 4},
        {'label': 'Quinta', 'value': 5},
        {'label': 'Sexta', 'value': 6},
        {'label': 'Sétima', 'value': 7}

    ],
    value=[1,7],
    multi=True
    )]),

        html.Br(),
        html.P('Lendário', 
        style={
            'textAlign': 'center'
        }),
        dbc.Card([dcc.Checklist(
    id='lendario',        
    options=[
        {'label': '  Lendário', 'value': 1},
        {'label': '  Comum', 'value': 0},

    ],
    value=[0],
    labelStyle= {'display': 'block'}
    )]),
        html.Br(),

        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)

sidebar = html.Div(
    [
        html.H2('Filtros', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Quantidade', className='card-title', style=CARD_TEXT_STYLE),
                        html.P(id='card_qtd', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Média Altura', className='card-title', style=CARD_TEXT_STYLE),
                        html.P(id='card_alt', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Média Peso', className='card-title', style=CARD_TEXT_STYLE),
                        html.P(id='card_peso', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    )
])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id = 'graph_1'), md = 6,
        ),
        dbc.Col(
            dcc.Graph(id = 'graph_2'),md = 6
,
        )
        
        
    ]
)

content_third_row = dbc.Row(
    [
        
        dbc.Col(
            dcc.Graph(id = 'graph_3'), md=12,
        )
        
        
    
        
        
    ]
)

content_fourth_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id = 'graph_4'), md=12,
        )
        
    ]
)




content = html.Div(
    [
        html.H2('DashBoard Pokemon', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row,
        
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])

    

@app.callback(
    Output('graph_1', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [
     State('tipo', 'value'),State('geracao','value'),State('lendario','value')
     ])
def update_graph_1(n_clicks, tipo_value, geracao_value,leg_value):
    dados = filtragem(data,tipo_value, geracao_value,leg_value)
    
    return chart_catch_x_tot(dados,tipo_value)


@app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [
     State('tipo', 'value'),State('geracao','value'),State('lendario','value')
     ])
def update_graph_1(n_clicks, tipo_value, geracao_value,lendario_value):
    dados = filtragem(data,tipo_value, geracao_value,lendario_value)
    
    return grafico_radar_comparacao(dados,tipo_value)

@app.callback(
    Output('graph_3', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [
     State('tipo', 'value'),State('geracao','value'),State('lendario','value')
     ])
def update_graph_1(n_clicks, tipo_value, geracao_value,lendario_value):
    dados = filtragem(data,tipo_value, geracao_value,lendario_value)
    
    return chart_egg_x_tot(dados)

@app.callback(
    Output('graph_4', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [
     State('tipo', 'value'),State('geracao','value'),State('lendario','value')
     ])
def update_graph_1(n_clicks, tipo_value, geracao_value,lendario_value):
    dados = filtragem(data,tipo_value, geracao_value,lendario_value)
    
    return chart_egg_x_catch(dados)    

if __name__ == '__main__':
    app.run_server(port='8085')