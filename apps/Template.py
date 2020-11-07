import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app


def template(content, pagename):
    sidebar = Sidebar(pagename)
    topbar = Topbar()
    footer = Footer()
    return html.Div(className="wrapper", id="wrapper", children=[
            sidebar,
            html.Div(className="main-panel", children=[
                html.Div(className="header", children=[topbar]),
                html.Div(className="content", children=[content]), 
                html.Div(className="footer", children=[footer]) 
            ])
        ])

def Footer():
    return html.Div(className="container-fluid", children=[
            html.Nav(className="pull-left", children=[

            ]),
            html.Div(className="copyright pull-right", children=[
                html.Label("© 2020, made with  "),
                html.I(className="fa fa-heart heart"),
                html.Label("  by "),
                html.A(href="/about", children=[          
                    html.B("Team 68")
                ])
            ])
        ])


def Sidebar(pagename):
    pagenames = ["Home", "Store", "Geolocation", "Forecast", "Product", "About"]
    classnames = ["" for page in pagenames]
    classnames[pagenames.index(pagename)] = "active"
    return html.Div(className="sidebar", id="sidebar", children=[
            html.Div(className="logo text-center",
                children=[ 
                html.A(href="https://teate.co/", className="logo-normal ",children=[
                    html.Img(src="https://teate.co/wp-content/themes/teatetheme/images/logo.png")
                ])
                ]),
            html.Div(className="sidebar-wrapper", id="collapse", children=[
                html.Ul(className="nav", id="nav", children=[
                    html.Li(className=classnames[0], children=[
                        html.A(href="/home", children=[
                            html.I(className="fa fa-home"),
                            html.P("Home")
                        ])
                    ]),
                    html.Li(className=classnames[1], children=[
                        html.A(href="/store", children=[
                            html.I(className="fa fa-shopping-cart"),
                            html.P("Store Analysis")
                        ])
                    ]),
                    html.Li(className=classnames[4], children=[
                        html.A(href="/product", children=[
                            html.I(className="fa fa-archive"),
                            html.P("Product Analysis")
                        ])
                    ]),
                    html.Li(className=classnames[2], children=[
                        html.A(href="/geolocation", children=[
                            html.I(className="fa fa-map-marker"),
                            html.P("Geolocation")
                        ])
                    ]),
                    html.Li(className=classnames[3], children=[
                        html.A(href="/forecast", children=[
                            html.I(className="fa fa-line-chart"),
                            html.P("Forecast")
                        ])
                    ]),
                    html.Li(className=classnames[5], children=[
                        html.A(href="/about", children=[
                            html.I(className="fa fa-users"),
                            html.P("About us")
                        ])
                    ])
                ])
            ])
        ])

def Topbar():
    topbar =  html.Nav(className="navbar navbar-expand-lg navbar-absolute fixed-top navbar-transparent",
        children=[
            html.Div(className="container-fluid", children=[
                html.Div(className="navbar-wrapper", children=[
                    html.Div(className="navbar-toggle", children=[
                        html.Button(id="sidebar-toggle", className="navbar-toggler", children=[
                            html.Span(className="navbar-toggler-bar bar1"),
                            html.Span(className="navbar-toggler-bar bar2"),
                            html.Span(className="navbar-toggler-bar bar3"),
                        ])
                    ]),
                    html.A(className="navbar-brand", children=[
                        html.B("Teaté Colombia S.A.S"),
                        html.Br(),
                        html.Label("Demand Forecast per Manufacture")
                    ])
                ]),
                html.Div(className="logout text-center", children=[      
                    html.Div(className="nav", children=[                 
                        html.A(href="/logout", children=[
                            html.I(className="fa fa-power-off"),
                            html.P("Log Out", style={'color':'#E73D2A'})
                        ])
                    ])
                ])
            ])
        ])
    return topbar

@app.callback(
    Output("sidebar-toggle", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar-toggle", "className")],
)
def toggle_classname(n, classname):
    if classname == "navbar-toggler":
         return "navbar-toggler toggled"
    return "navbar-toggler"


@app.callback(
    Output("wrapper", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("wrapper", "className")],
)
def toggle_classname(n, classname):
    if classname == "wrapper":
         return "wrapper nav-open"
    return "wrapper"

