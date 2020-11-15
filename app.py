import dash
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.BOOTSTRAP,
'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.config.suppress_callback_exceptions = True
app.title = 'DS4A'

# create a server and apply a random secret key
# change key to security reasons when implementing
server = app.server
server.config['SECRET_KEY'] = 'k1LUZ1fZShowB6opomjbkjfrjdkuhnmMgmNcDGNmgGYr'