import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
import dash

layout = html.Div(children=[
        mydbc.card(content="About us", title="About us", description="Here you can find interesting data about us", color="light", footer="footer")
    ], className="my-2")