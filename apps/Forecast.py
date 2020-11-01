import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from app import app
import pandas as pd
import dash
from data import run_query, engine

city_lbl =["Cali", "Medellin"]
mfr_lbl = ["Colanta", "Alquería", "Leche la Mejor"]
prod_type_lbl = ["Lacteos", "Harinas", "Bebidas Gaseosas"]
prod_lbl = run_query('select distinct product from forecast_results', engine)['product'].values.tolist()

styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': 'auto',
        'width': '100%'
    }
}

content = html.Div(
     [
         dbc.Row(
         [
             dbc.Col(mydbc.dropdown(id="City",label="City", list_options = city_lbl, value="Cali")),
             #dbc.Col(mydbc.dropdown(label="Manufacturer", list_options = mfr_lbl)),
             #dbc.Col(mydbc.dropdown(label="Product type", list_options = prod_type_lbl)),
             dbc.Col(mydbc.dropdown(id="Product",label="Product", list_options = prod_lbl, value="505")),
         ]),
         dbc.Row(
         children=[
             dbc.Col(dbc.Button("Run Predictor", color="primary", className="col-8"))#,
            #  dbc.Col(children=[
            #      html.Div(children=[mydbc.date_picker(label = "Date Interval", id="date-picker")], className="float-right")
            #      ],className="col-4 justify-content-start"),
            
         ]),
         dbc.Row([
              html.Div(className = "embed-responsive embed-responsive-16by9",
                children = [
                    dcc.Graph(id='Forecast',
                    figure={
                        'layout': {
                        'title': 'Forecast Visualization',
                        }
                    }, 
                    className="embed-responsive-item")
                ],
            )
         ])
     ]  
)

layout = html.Div(children=[
        mydbc.card(content=content, title="Forecast", description="Here you can find interesting data about Teaté's products forecast", color="light", footer="")
    ], className="my-2")

@app.callback(Output('Forecast','figure'),[Input('City', 'value'),Input('Product','value')])
def update_graph(city,product):
    city_code=(2000 if city=='Cali' else 3000)
    df_plot=run_query('select * from forecast_results where product= '+str(product) + ' and city= '+str(city_code) + ' order by ds desc', engine)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat_upper'],name='y' ,mode='lines',line=dict(width=0.5, color='rgb(210, 250, 255)'),showlegend=False))
    fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat_lower'],name='y' ,mode='lines',fill='tonexty',line=dict(width=0.5, color='rgb(210, 250, 255)'),fillcolor='rgba(0, 0, 255,0.1)' ,showlegend=False))
    fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat'],name='yhat' ,mode='lines',line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['y'],name='y' ,mode='markers',marker_color='black'))

    return fig
