import dash
import os
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            [html.Div(
                "First Division",
                style={
                    'textAlign': 'center',       # Center alignment
                    'color': 'white',            # Text color
                    'backgroundColor': '#007BFF',
                    'borderRadius': '10px',      # Rounded corners
                    'border': '2px solid black',
                }
            ),
            html.Div(
                "Second Division",
                style={
                    'textAlign': 'center',       # Center alignment
                    'color': 'white',            # Text color
                    'backgroundColor': '#007BFF',
                    'borderRadius': '10px',      # Rounded corners
                    'border': '2px solid black',    
                }
            )],
            style={'display': 'flex'},
            xs=12, sm=8, md=6, lg=4, xl=3, xxl=3
        ),
        dbc.Col(
            html.Div(
                [
                    html.Div(
                        'This is first division of second column',
                        style={
                            'textAlign': 'center',       # Center alignment
                            'color': 'white',            # Text color
                            'backgroundColor': '#007BFF',
                            'borderRadius': '10px',      # Rounded corners
                            'border': '2px solid black',   
                        }
                    ),
                    html.Div(
                        'This is the second division of second column',
                       style={
                            'textAlign': 'center',       # Center alignment
                            'color': 'white',            # Text color
                            'backgroundColor': '#007BFF',
                            'borderRadius': '10px',      # Rounded corners
                            'border': '2px solid black',   
                        }
                    )
                ],
                style= {'display':'flex'}
            ),
            xs=12, sm=8, md=6, lg=4, xl=3, xxl=3
        )
    ]),
    

    html.Hr(),

    dbc.Row(
        [
            

            dbc.Col(
                [
                    dash.page_container
                ], width=12)
        ]
    )
], fluid=True)




if __name__ == "__main__":
            port = int(os.environ.get('PORT', 8050))  # Render sets this automatically
            app.run(debug=False, host='0.0.0.0', port=port)

