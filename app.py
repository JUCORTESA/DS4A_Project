import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


import codecs
from scripts.utils import *
from Views.Home import page


template=codecs.open("Views/template.html", 'r') #Load HTML FILE

app = dash.Dash(__name__)


app.title = 'DS4A'
app.index_string = template.read()

app.layout = page

if __name__ == '__main__':
    app.run_server()