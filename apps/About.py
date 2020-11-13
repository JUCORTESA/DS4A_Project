# Basics Requirements
import pathlib
import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

# Dash Bootstrap Components
import dash_bootstrap_components as dbc
from app import app



layout = html.Div(
    [
        dbc.Alert(
            [
                html.H1("About Us", style={"color": "#E73D2A"}),

            ],
            style={
                "background-color": "#F4F3EF",
                "border": "0px",
            },
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/ariana.jpg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px", "max-width":"50%"}
                                ),
                                html.H3(
                                    "Ariana Rojas",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Industrial Engineer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:arianalrg@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="",
                                ),
                            ], style={"text-align": "center"}
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/daza.jpeg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px"}
                                ),
                                html.H3(
                                    "Daniel Daza",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "MSc Business Analytics | Industrial Engineer | Data Science",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:dafedaza@hotmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/daniel-felipe-daza-flechas-180010122/",
                                ),
                            ], style={"text-align": "center"}
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/lopez.jpeg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px"}
                                ),
                                html.H3(
                                    "Daniel Lopez",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Economist | Industrial Engineer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:daniel.lopez.81@hotmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/daniel-l%C3%B3pez-9982b51aa/",
                                ),
                            ], style={"text-align": "center"}
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/javier.jpeg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px"}
                                ),
                                html.H3(
                                    "Jávier Alexis Cárdenas Bohorquez",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Electronic Engineer Student",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:javiercardenas@usantotomas.edu.co",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/javier-cardenas-581637169/",
                                ),
                            ], style={"text-align": "center"}
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/jcarlos.jpg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px", "width":"max-content", "max-width":"50%"}
                                ),
                                html.H3(
                                    "Juan Carlos Cortés Aguas",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Business Administrator | Software Developer",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:juan1015@gmail.com",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/juan-carlos-cortes-aguas/",
                                ),
                            ], style={"text-align": "center"}
                        ),
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/jmario.jpeg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px"}
                                ),
                                html.H3(
                                    "Juan Mario Castro Quintana",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Actuary",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:jmcastroq@unal.edu.co",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="https://www.linkedin.com/in/juan-mario-castro-quintana-528128b2/",
                                ),
                            ], style={"text-align": "center"}
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(
                                    src=app.get_asset_url("img/paola.jpg"),
                                    height="250px",
                                    className="img_marg",
                                    style={"border-radius": "600px"}
                                ),
                                html.H3(
                                    "Paola A. Ureña P.",
                                    className="H5_margin",
                                ),
                                html.H5(
                                    "Economist",
                                    className="P_margin",
                                ),
                                dbc.Button(
                                    "@",
                                    size="lg",
                                    color="danger",
                                    className="correo",
                                    href="mailto:pauruenap@unal.edu.co",
                                ),
                                dbc.Button(
                                    "in",
                                    size="lg",
                                    color="primary",
                                    className="In_marg",
                                    href="",
                                ),
                            ], style={"text-align": "center"}
                        ),
                    dbc.Col([]),
                    ]
                ),
            ]
        ),
    ]
)