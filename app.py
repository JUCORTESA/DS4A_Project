import os
import dash
import dash_bootstrap_components as dbc
#from flask_caching import Cache

external_stylesheets = [dbc.themes.BOOTSTRAP,
'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

"""cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})"""
app.config.suppress_callback_exceptions = True
app.title = 'DS4A'

server = app.server
server.config['SECRET_KEY'] = 'k1LUZ1fZShowB6opomjbkjfrjdkuhnmMgmNcDGNmgGYr'