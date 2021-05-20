import dash_bootstrap_components as dbc
import dash_html_components as html

def card(nome, id):
    return dbc.Col(
        dbc.Card([
            dbc.CardBody([
                html.H4(nome, className='card-title'),
                html.P(id=id, children=['0'], className='card-content'),
            ])
        ]),
        md=4
    )