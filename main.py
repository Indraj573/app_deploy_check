import dash
import os
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div(
                "Python Multipage App with Dash",
                style={
                    'fontSize': '40px',          # Font size
                    'textAlign': 'center',       # Center alignment
                    'color': 'white',            # Text color
                    'backgroundColor': '#007BFF',# Background (box) color
                    'padding': '20px',           # Padding inside the box
                    'borderRadius': '10px',      # Rounded corners
                    'border': '2px solid black',  # Border around the box
                    'width': '50%',        # 🔹 Box width
                    #'height': '150px',       # 🔸 Box height
                    #'margin': '0 auto'       # Center the box horizontally
                }
            ),
            width=6
        ),
        dbc.Col('This is second column ',
                    style={
                        'fontSize': '40px',          # Font size
                        'textAlign': 'center',       # Center alignment
                        'color': 'white',            # Text color
                        'backgroundColor': '#007BFF',# Background (box) color
                        'padding': '20px',           # Padding inside the box
                        'borderRadius': '10px',      # Rounded corners
                        'border': '2px solid black',  # Border around the box
                        #'width': '600px',        # 🔹 Box width
                        #'height': '150px',       # 🔸 Box height
                        #'margin': '0 auto'       # Center the box horizontally
                    }, width=6
                )
    ]),
    dbc.Row(
        html.Div('This is second row , i think ')
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == "__main__":
            port = int(os.environ.get('PORT', 8050))  # Render sets this automatically
            app.run(debug=False, host='0.0.0.0', port=port)

