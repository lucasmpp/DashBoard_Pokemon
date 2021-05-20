import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from .componentes import checkbox

controles_filtros = dbc.FormGroup([
    *checkbox('Natureza', id='tipo', valores_iniciais=['fire','water'], opcoes=[
        {'label': 'Fogo',           'value': 'fire'},
        {'label': 'Água',           'value': 'water'},
        {'label': 'Planta',         'value': 'grass'},
        {'label': 'Elétrico',       'value': 'electric'},
        {'label': 'Pedra',          'value': 'rock'},
        {'label': 'Fantasma',       'value': 'ghost'},
        {'label': 'Normal',         'value': 'normal'},
        {'label': 'Lutador',        'value': 'fighting'},
        {'label': 'Voador',         'value': 'flying'},
        {'label': 'Venenoso',       'value': 'poison'},
        {'label': 'Terrestre',      'value': 'ground'},
        {'label': 'Inseto',         'value': 'bug'},
        {'label': 'Aço',            'value': 'steel'},
        {'label': 'Psíquico',       'value': 'psychic'},
        {'label': 'Gelo',           'value': 'ice'},
        {'label': 'Fada',           'value': 'fairy'},
        {'label': 'Dragão',         'value': 'dragon'},
        {'label': 'Noturno',        'value': 'dark'}
    ]),
    html.Br(),
    *checkbox('Geração', id='geracao', valores_iniciais=[1,7], opcoes=[
        {'label': 'Primeira',   'value': 1},
        {'label': 'Segunda',    'value': 2},
        {'label': 'Terceira',   'value': 3},
        {'label': 'Quarta',     'value': 4},
        {'label': 'Quinta',     'value': 5},
        {'label': 'Sexta',      'value': 6},
        {'label': 'Sétima',     'value': 7}
    ]),
    html.Br(),
    *checkbox('Lendário', id='lendario', valores_iniciais=[0], opcoes=[
        {'label': '  Lendário', 'value': 1},
        {'label': '  Comum', 'value': 0},
    ]),
    html.Br(),

    dbc.Button(
        id='submit_button',
        n_clicks=0,
        children='Filtrar',
        color='dark',
        block=True
    ),
])

filtros = html.Div(
    [
        html.H2('Filtros', className='title'),
        html.Hr(),
        controles_filtros
    ],
    className='sidebar'
)