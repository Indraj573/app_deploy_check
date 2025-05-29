import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px



app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"
])
server = app.server
df = px.data.gapminder()

app.layout = html.Div([
    html.Div(
        id="sidebar",
        children=[
            html.Button([
                html.I(className="bi bi-house", style={"fontSize": "2vw"}),
                html.Span(" Home", className="btn-text")
            ], className="sidebar-btn", id="btn-home"),
            html.Button([
                html.I(className="bi bi-bar-chart", style={"fontSize": "2vw"}),
                html.Span(" Analytics", className="btn-text")
            ], className="sidebar-btn", id="btn-analytics"),
            html.Button([
                html.I(className="bi bi-gear", style={"fontSize": "2vw"}),
                html.Span(" Settings", className="btn-text")
            ], className="sidebar-btn", id="btn-settings"),
        ],
        className="sidebar"
    ),
    html.Div(
        html.Div("Resposive Design", style={
            'border': '.01vw solid black',
            'textAlign': 'center',
            'height': '5vh',
            'fontSize': '2vw'
        }),
        style={"marginLeft": "5vw"}  # Initial offset
    ),
    html.Div(
        dbc.Row([
            dbc.Col(dcc.Graph(
                            id='line-fig-1',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=10, r=10, t=30, b=30)), style = {'height':'50vh'}
                
                        ),xs=12, sm=10, md=8, lg=4, xl=4, xxl=4,style={'border': '.01vw solid black'}),
            dbc.Col(dcc.Graph(
                            id='line-fig-2',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=10, r=10, t=30, b=30)), style = {'height':'50vh'}
                        ),xs=12, sm=10, md=8, lg=4, xl=4, xxl=4,style={'border': '.01vw solid black'}),
            dbc.Col(dcc.Graph(
                            id='line-fig-3',
                            figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')
                                    .update_layout(showlegend=False, margin=dict(l=10, r=10, t=30, b=30)), style = {'height':'50vh'}
                        ),xs=12, sm=10, md=8, lg=4, xl=4, xxl=4,style={'border': '.01vw solid black'}),
        ]) ,style={"marginLeft": "5vw"}
    )
], style={"font-family": "Arial, sans-serif"})



if __name__ == "__main__":
            port = int(os.environ.get('PORT', 8050))  # Render sets this automatically
            app.run(debug=False, host='0.0.0.0', port=port)

