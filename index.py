import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import no_update
from flask import session
import codecs

# local imports
from auth import authenticate_user, validate_login_session
from app import app
from apps import Home, Analytics, Geolocation, Forecast


###############################################################################
# Views
###############################################################################

# login layout content to show
def login_layout():
    """Login view"""
    return html.Div(
        [
            dcc.Location(id='login-url', pathname='/login', refresh=False),
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H4('Login', className='card-title'),
                                    dbc.Input(id='login-email',
                                              placeholder='User'),
                                    dbc.Input(id='login-password',
                                              placeholder='Assigned password',
                                              type='password'),
                                    dbc.Button('Submit', id='login-button',
                                               color='danger', block=True),
                                    html.Br(),
                                    html.Div(id='login-alert')
                                ],
                                body=True
                            ),
                            width=6
                        ),
                        justify='center'
                    )
                ]
            )
        ]
    )


# main app layout
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(
            login_layout(),
            id='page-content'
        ),
    ]
)


# home layout content
@validate_login_session
def app_layout():
    """route to home layout in Home.py"""
    template = codecs.open("apps/views/template2.html", 'r')  # Load HTML FILE
    app.title = 'DS4A'
    app.index_string = template.read()
    return Home.layout

# Analytics layout content
@validate_login_session
def app_layout_2():
    """route to Analytics layout in Analytics.py"""
    template = codecs.open("apps/views/template2.html", 'r')  # Load HTML FILE
    app.title = 'DS4A'
    app.index_string = template.read()
    return Analytics.layout

# Geolocation layout content
@validate_login_session
def app_layout_3():
    """route to Analytics layout in Analytics.py"""
    template = codecs.open("apps/views/template.html", 'r')  # Load HTML FILE
    app.title = 'DS4A'
    app.index_string = template.read()
    return Geolocation.layout

@validate_login_session
def app_layout_4():
    """route to Analytics layout in Analytics.py"""
    template = codecs.open("apps/views/template.html", 'r')  # Load HTML FILE
    app.title = 'DS4A'
    app.index_string = template.read()
    return Forecast.layout

###############################################################################
# utilities
###############################################################################

# url router
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def router(url):
    """Checks and route url to view layout"""
    if url == '/home':
        return app_layout()
    elif url == '/login':
        return login_layout()
    elif url == '/analytics':
        return app_layout_2()
    elif url == '/geolocation':
        return app_layout_3()
    elif url == '/forecast':
        return app_layout_4()
    else:
        return login_layout()


# authenticate
@app.callback(
    [Output('url', 'pathname'),
     Output('login-alert', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('login-email', 'value'),
     State('login-password', 'value')])
def login_auth(n_clicks, email, pw):
    """
    check credentials
    if correct, authenticate the session
    otherwise, authenticate the session and send user to login
    """
    if n_clicks is None or n_clicks == 0:
        return no_update, no_update
    credentials = {'user': email, "password": pw}
    if authenticate_user(credentials):
        session['authed'] = True
        return '/home', ''
    session['authed'] = False
    return no_update, dbc.Alert('Incorrect credentials.', color='danger',
                                dismissable=True)


@app.callback(
    Output('home-url', 'pathname'),
    [Input('logout-button', 'n_clicks')])
def logout_(n_clicks):
    """clear the session and send user to login"""
    if n_clicks is None or n_clicks == 0:
        return no_update
    session['authed'] = False
    return '/login'


if __name__ == "__main__":
    app.run_server(debug=True)
