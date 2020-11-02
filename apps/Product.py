import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from app import app
from dash.dependencies import Input, Output
from data import run_query, engine
import plotly.express as px

city_lbl = ["Cali", "Medellín"]
mfr_lbl = run_query("select DISTINCT ON (fabricante) fabricante, nombre_fabricante from historicopedidos", engine).dropna()
prod_cat_lbl = run_query("select MIN(jerarquia_productos), nombre_cat from categorias group by nombre_cat", engine).dropna()
prod_sub_cat_lbl = run_query("select MIN(subcategoria), nombre_sub from categorias group by nombre_sub", engine).dropna()

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
                dbc.Col(dcc.Dropdown(id="city", options=[{'label': i, 'value': i} for i in city_lbl],)),
                dbc.Col(dcc.Dropdown(id="manufacturer", options=[{'label': mfr_lbl.iloc[i]['nombre_fabricante'], 'value': mfr_lbl.iloc[i]['fabricante']} for i in range(mfr_lbl.shape[0])])),
                dbc.Col(dcc.Dropdown(id="product category", options=[{'label': prod_cat_lbl.iloc[i]['nombre_cat'], 'value': prod_cat_lbl.iloc[i]['min']} for i in range(prod_cat_lbl.shape[0])])),
                dbc.Col(dcc.Dropdown(id="product sub-category", options=[{'label': prod_sub_cat_lbl.iloc[i]['nombre_sub'], 'value': prod_sub_cat_lbl.iloc[i]['min']} for i in range(prod_sub_cat_lbl.shape[0])])),
                dbc.Col(dcc.DatePickerRange(id="my-date-picker-range",
                                    start_date="2020-01-07",
                                    end_date="2020-05-07",
                                    end_date_placeholder_text='Select a date!'
                                    ),  style ={'font-size':5})
            ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='product_graph'),),
            dbc.Col(dcc.Graph(id='productmoney_graph'),)
        ])
    ]
)

layout = html.Div(children=[
    mydbc.card(content=content, title="Product Analysis",
               description="Here you can find interesting data about Teaté's products",
               color="light", footer="footer")
], className="my-2")

@app.callback(Output('product_graph', 'figure'),
              [Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date'),
               Input('city', 'value'),
               Input('manufacturer', 'value'),
               Input('product category', 'value'),
               Input('product sub-category', 'value')])
def update_graph(start_date, end_date, city, manufacturer, cat, sub_cat):

    query = "select SUM(cantidad_pedido) as cantidad, c.Texto_breve_de_material1 from historicopedidos h left join tiendas t on h.tienda = t.tienda left join categorias c on h.Material = c.Material WHERE Valor_TotalFactura >0 AND Fecha_Pedido >= " + "\'" + start_date + "\'" + " AND Fecha_Pedido < "+ "\'" + end_date + "\'"+""
    
    if city is not None:
        if city == 'Cali':
            centro = 2000
        else:
            centro = 3000
        query = query + 'AND t.Cod_Centro ='+ str(centro)

    if manufacturer is not None:
        query = query + 'AND h.fabricante =' + str(manufacturer)

    if cat is not None:
        query = query + 'AND c.jerarquia_productos ='+str(cat)

    if sub_cat is not None:
        query = query + 'AND c.subcategoria ='+str(sub_cat)
    df = run_query(query + "group by c.material, c.Texto_breve_de_material1 order by cantidad DESC limit 10", engine)
    fig = px.bar(df, x='texto_breve_de_material1', y='cantidad')
    return fig

@app.callback(Output('productmoney_graph', 'figure'),
              [Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date'),
               Input('city', 'value'),
               Input('manufacturer', 'value'),
               Input('product category', 'value'),
               Input('product sub-category', 'value')])
def update_moneygraph(start_date, end_date, city, manufacturer, cat, sub_cat):

    query = "select SUM(Valor_TotalFactura) as ventas, c.Texto_breve_de_material1 from historicopedidos h left join tiendas t on h.tienda = t.tienda left join categorias c on h.Material = c.Material WHERE Valor_TotalFactura >0 AND Fecha_Pedido >= " + "\'" + start_date + "\'" + " AND Fecha_Pedido < "+ "\'" + end_date + "\'"+""
    
    if city is not None:
        if city == 'Cali':
            centro = 2000
        else:
            centro = 3000
        query = query + 'AND t.Cod_Centro ='+ str(centro)

    if manufacturer is not None:
        query = query + 'AND h.fabricante =' + str(manufacturer)

    if cat is not None:
        query = query + 'AND c.jerarquia_productos ='+str(cat)

    if sub_cat is not None:
        query = query + 'AND c.subcategoria ='+str(sub_cat)
    df = run_query(query + "group by c.material, c.Texto_breve_de_material1 order by ventas DESC limit 10", engine)
    fig = px.bar(df, x='texto_breve_de_material1', y='ventas')
    return fig

