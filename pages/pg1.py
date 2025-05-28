import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Home') # '/' is home page

# page 1 data
df = px.data.gapminder()

layout = html.Div(
    [
        # First row: dropdown
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        options=[{'label': c, 'value': c} for c in df.continent.unique()],
                        id='cont-choice'
                    ),
                    xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                )
            ]
        ),

        # Second row: 3 graphs
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id='line-fig-1',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=10, r=10, t=30, b=30))
                        ),
                        style={'padding': '0', 'margin': '0'}
                    ),
                    xs=10,sm=10,md=8,lg=4,xl=4,xxl=4,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id='line-fig-2',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=0, r=0, t=0, b=0))
                        ),
                        style={'padding': '0', 'margin': '0'}
                    ),
                    xs=10,sm=10,md=8,lg=4,xl=4,xxl=4,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id='line-fig-3',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=0, r=0, t=0, b=0))
                        ),
                        style={'padding': '0', 'margin': '0'}
                    ),
                    xs=10,sm=10,md=8,lg=4,xl=4,xxl=4,
                )
            ],
            #gutter=0  # ⬅️ removes spacing between columns
        )
    ],
    style={'padding': '0', 'margin': '0'}
)


@callback(
    Output('line-fig', 'figure'),
    Input('cont-choice', 'value')
)
def update_graph(value):
    if value is None:
        fig = px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
        fig.update_layout(showlegend=False)
    else:
        dff = df[df.continent==value]
        fig = px.histogram(dff, x='country', y='lifeExp', histfunc='avg')
        fig.update_layout(showlegend=False)
    return fig