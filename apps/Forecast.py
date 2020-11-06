import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from app import app
import numpy as np
import pandas as pd
import dash
from data import run_query, engine

city_lbl =["Cali", "Medellin"]
prod_type_lbl = run_query('select distinct initcap(nombre_cat) as nombre_cat from categorias c\
                         inner join forecast_results r on c.material=r.product ', engine)['nombre_cat']\
                        .values.tolist()
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

content = html.Div(className="col-sm",
        children=[
        dbc.Row(
         [
             dbc.Col(mydbc.dropdown(id="City",label="City", list_options = city_lbl, value="",searchable=False, clearable=False)),
             dbc.Col(mydbc.dropdown(id="Product_type",label="Product type", list_options = prod_type_lbl,searchable=False,clearable=False)),
             dbc.Col(mydbc.dropdown(id="Product",label="Product", list_options = [], value="",searchable=False,clearable=False)),
         ]),
        #  dbc.Row(
        #  children=[
        #      dbc.Col(dbc.Button("Run Predictor", color="primary", className="col-8"))
            
        #  ]),
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
         ]),
        dbc.Row([
             html.Div(className="col-sm",
             children=[
                dbc.Row(children=[dbc.Label('RMSE:',html_for='Label_rmse',className="col-form-label col-sm")]),
                dbc.Row(children=[dcc.Textarea(id='rmse_display',value='',contentEditable=False,disabled =True)])]
                ),
             html.Div(className="col-sm",
             children=[
                 dbc.Row(children=[dbc.Label('Yearly Seasonality:',html_for='Label_yearly_season',className="col-form-label col-sm")]),
                 dbc.Row(children=[dcc.Textarea(id='Year_seasonality',value='',contentEditable=False,disabled =True)])]
                ),
             html.Div(className="col-sm",
             children=[
                 dbc.Row(children=[dbc.Label('Monthly Seasonality:',html_for='Label_monthly_season',className="col-form-label col-sm")]),
                 dbc.Row(children=[dcc.Textarea(id='Month_seasonality',value='',contentEditable=False,disabled =True)])]
                ),
             html.Div(className="col-sm",
             children=[
                 dbc.Row(children=[dbc.Label('Last Updated:',html_for='Label_last_updated',className="col-form-label col-sm")]),
                 dbc.Row(children=[dcc.Textarea(id='Last_updated',value='',contentEditable=False,disabled =True)])]
                )             
            ]
         )
     ]  
)

layout = html.Div(children=[
        mydbc.card(content=content, title="Forecast", description="Here you can find interesting data about Teaté's products forecast", color="light", footer="")
    ], className="my-2")

@app.callback(Output('Forecast','figure'),[Input('City', 'value'),Input('Product','value')])
def update_graph(city,product):
    fig = go.Figure()
    try:
        city_code=(2000 if city=='Cali' else 3000)
        df_plot=run_query('select * from forecast_results where product= '+str(product) + ' and city= '+str(city_code) + ' order by ds desc', engine)
        
        fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat_upper'],name='y' ,mode='lines',line=dict(width=0.5, color='rgb(210, 250, 255)'),showlegend=False))
        fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat_lower'],name='y' ,mode='lines',fill='tonexty',line=dict(width=0.5, color='rgb(210, 250, 255)'),fillcolor='rgba(0, 0, 255,0.1)' ,showlegend=False))
        fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['yhat'],name='yhat' ,mode='lines',line=dict(color='blue', width=4)))
        fig.add_trace(go.Scatter(x=df_plot['ds'],y=df_plot['y'],name='y' ,mode='markers',marker_color='black'))
    except:
        pass
    return fig

@app.callback(Output('Product', 'options'), [Input('Product_type','value')])
def update_prod_list(product_type):
    options = []
    try:
        new_list=run_query("select distinct c.material,c.texto_breve_de_material \
            from forecast_results r \
            inner join categorias c on c.material=r.product \
            where c.nombre_cat = upper('"+product_type+"')" , engine).to_dict(orient='records')
        
        for option in new_list:
            options.append({"label": option['texto_breve_de_material'], "value": option['material']})
        
    except:
        print('Error updating list')
    return options

@app.callback(Output('rmse_display','value'),[Input('City', 'value'),Input('Product','value')])
def update_rmse(city,product):
    try:
        city_code=(2000 if city=='Cali' else 3000)
        sql='select * from model_metrics_log where city = '+ str(city_code) + ' and product = '+ str(product) + ' order by forecast_datetime desc limit 1'
        result=str(np.round(run_query(sql, engine)['rmse'].values.tolist()[0],2))
    except:
        result=''
        pass
    return result

@app.callback(Output('Year_seasonality','value'),[Input('City', 'value'),Input('Product','value')])
def update_year_seasonality(city,product):
    try:
        city_code=(2000 if city=='Cali' else 3000)
        sql='select * from model_metrics_log where city = '+ str(city_code) + ' and product = '+ str(product) + ' order by forecast_datetime desc limit 1'
        temp=run_query(sql, engine)['yearly_seasonality_scale'].values.tolist()[0]
        result= 'No' if temp ==0 else 'Weak'if temp ==1 else 'Strong'
        result=result+ ' Seasonality'
    except:
        result=''
        pass
    return result

@app.callback(Output('Month_seasonality','value'),[Input('City', 'value'),Input('Product','value')])
def update_month_seasonality(city,product):
    try:
        city_code=(2000 if city=='Cali' else 3000)
        sql='select * from model_metrics_log where city = '+ str(city_code) + ' and product = '+ str(product) + ' order by forecast_datetime desc limit 1'
        temp=run_query(sql, engine)['monthly_seasonality_scale'].values.tolist()[0]
        result= 'No' if temp ==0 else 'Weak'if temp ==1 else 'Strong'
        result=result+ ' Seasonality'
    except:
        result=''
        pass
    return result

@app.callback(Output('Last_updated','value'),[Input('City', 'value'),Input('Product','value')])
def update_last_updated(city,product):
    try:
        city_code=(2000 if city=='Cali' else 3000)
        sql='select * from model_metrics_log where city = '+ str(city_code) + ' and product = '+ str(product) + ' order by forecast_datetime desc limit 1'
        result=run_query(sql, engine)['forecast_datetime'].loc[0].strftime("%d/%m/%Y - %H:%M")
    except:
        result=''
        pass
    return result