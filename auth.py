from functools import wraps
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import session

# Authentication user and password
# change and add users inside the dictionary as required
users = {
    'ds4a': 'group68'
}

def authenticate_user(credentials):
    """
    generic authentication function

    :param credentials: dictionary with user and password
    :return: True if user is correct and False otherwise
    """
    authed = (credentials['user'] in users) and (credentials['password'] == users[credentials['user']])

    return authed

def validate_login_session(f):
    """
    checks if the user is logged in or not through the session.
    :param f: a layout function
    :return: layout objects. If not, returns an error with link to the login page
    """
    @wraps(f)
    def wrapper(*args,**kwargs):
        if session.get('authed',None)==True:
            return f(*args,**kwargs)
        return html.Div(
            dbc.Row(
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                html.H2('401 - Unauthorized',className='card-title'),
                                html.A(dcc.Link('Login',href='/login'))
                            ],
                            body=True
                        )
                    ],
                    width=5
                ),
                justify='center'
            )
        )
    return wrapper
