import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
from scripts.geoplot import heatmap, citylocation, point_map
from dash.dependencies import Input, Output

import pandas as pd
import geopandas
from data import run_query, engine

from datetime import date
from dateutil.relativedelta import relativedelta

import dash
import sys
sys.path.append('../')

from app import app

chart_typ_lbl = ["Sales Heat Map", "Stores Heat Map", "Stores Location"]
city_lbl = ["Cali", "Medellin"]

prod_type_lbl = run_query('select distinct initcap(nombre_cat) as nombre_cat from categorias c\
                         inner join forecast_results r on c.material=r.product ', engine)['nombre_cat']\
                        .values.tolist()

intvl_lbl = ["Weekly", "Monthly", "Annual"]


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
             dbc.Col(mydbc.dropdown(label="Chart type", id="Chart", list_options = chart_typ_lbl),
                    width = 6)
         ]),
         dbc.Row(
         [
             dbc.Col(mydbc.dropdown(label="City", id="City", list_options = city_lbl, value="",searchable=False, clearable=False)),
             dbc.Col(mydbc.dropdown(label="Product Category", id="Product_type", list_options = prod_type_lbl, value="",searchable=False, clearable=True)),
             dbc.Col(mydbc.dropdown(label="manu", id="manu", list_options = [], value="",searchable=False, clearable=True)),
             dbc.Col(mydbc.dropdown(label="Product", id="Product_sub", list_options = [], searchable=False, clearable=True)),
         ]),
         dbc.Row(
         [
              dbc.Col(dcc.DatePickerRange(id="my-date-picker-range",
                                            start_date=date.today() - relativedelta(months=6),
                                            end_date=date.today(),
                                            end_date_placeholder_text='Select a date!'
                                            ), style={'padding': 10, 'font-size': "50%"}),
                dbc.Col(html.P("Date on format Month/Day/Year"), style={"padding": 25}), dbc.Col(), dbc.Col()
         ]),
         dbc.Row(
         [
            html.Div(className = "embed-responsive embed-responsive-16by9 my-4",
                children = [html.Iframe(id= "map")
            ])
         ])
     ]
)

layout = html.Div(children=[
        mydbc.card(content=content, title="Geolocation", description="Here you can find interesting data about Teaté's stores location", color="light", footer="")
    ], className="my-2")


@app.callback(
    [dash.dependencies.Output('map', 'srcDoc')],
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('City', 'value'),
     Input('manu', 'value'),
     Input('Product_type', 'value'),
     Input('Product_sub', 'value'), 
     Input('Chart', 'value')])
def update_graph(start_date, end_date, city, manu, cat, sub_cat, Chart):
    #try:
        file = ""
        fields = []
        aliases = []
        caption = ""
        series = pd.DataFrame()
        if Chart is None or city is None or city == "":
            print("Chart Type is not selected")
            #raise Exception("Chart Type is not selected")
        else:        
            # start_date = '{:%x}'.format(date.fromisoformat(start_date.replace("/", "-")))
            # end_date = '{:%x}'.format(date.fromisoformat(end_date.replace("/", "-")))

            location = citylocation[city]
            geodata  = geopandas.read_file(f"models/Geolocation/geojson_data/Comunas_{city}.geojson", driver = "GeoJSON")
            if Chart=='Stores Location':
                query = f"""SELECT SUM(cantidad_pedido) as cantidad, T.tienda, SUM(h.valor_totalfactura) as ventas,
                        T.latitud, T.longitud, T.nombre_tienda, T.fecha_creacion, T.direccion_tienda,
                        T.telefono_1, t.nombre_tendero
                        from historicopedidos h 
                        left join tiendas t on h.tienda = t.tienda
                        left join categorias c on h.Material = c.Material
                        WHERE Valor_TotalFactura > 0
                        -- AND Fecha_Pedido >= DATE '{start_date}' 
                        -- AND Fecha_Pedido < DATE '{end_date}'
                        AND T.ciudad_tienda= '{city}'"""

                if manu is not None and not manu=="":
                    query = query + f" AND h.fabricante='{manu}'"

                if cat is not None and not cat=="":
                    query = query + f" AND c.nombre_cat =upper('{cat}')"

                if sub_cat is not None and not sub_cat=="":
                    query = query + f" AND c.material ={sub_cat}"
                        
                query = query + """ GROUP BY T.tienda, T.latitud, T.longitud, T.nombre_tienda, T.fecha_creacion,
                T.direccion_tienda, T.telefono_1, t.nombre_tendero
                order by ventas DESC limit 50"""
                series = run_query(query, engine)
                series = series.dropna(subset=['latitud', 'longitud'])
                series['fecha_creacion']  = series['fecha_creacion'].apply(lambda x: x.strftime('%Y-%m-%d'))
                fields = ['index', 'nombre_tienda', 'tienda', 'fecha_creacion', 'direccion_tienda', 'cantidad', 'ventas']
                aliases = ['Posición', 'Nombre de Tienda', 'Código', "Fecha de Creación", 'Dirección', 'Cantidad', 'Valor de Ventas $']
                caption= "Best  Teate Stores"
                m = point_map(series, location, fields, aliases, caption)
                m.save("models/Geolocation/Maps/Map.html")
                file = open("models/Geolocation/Maps/Map.html", "r").read()
            else:
                query = f"""SELECT SUM(cantidad_pedido) as cantidad, COUNT(DISTINCT T.tienda) as stores_count, T.COMUNA, SUM(h.valor_totalfactura) as total 
                        from historicopedidos h 
                        left join tiendas t on h.tienda = t.tienda
                        left join categorias c on h.Material = c.Material
                        WHERE Valor_TotalFactura > 0
                        AND Fecha_Pedido >= DATE '{start_date}' 
                        AND Fecha_Pedido < DATE '{end_date}'
                        AND T.ciudad_tienda= '{city}'"""
                                    
                if manu is not None and not manu=="":
                    query = query + f" AND h.fabricante='{manu}'"

                if cat is not None and not cat=="":
                    query = query + f" AND c.nombre_cat =upper('{cat}')"

                if sub_cat is not None and not sub_cat=="":
                    query = query + f" AND c.material ={sub_cat}"

                query = query + " GROUP BY T.COMUNA"
                series = run_query(query, engine)
                series["comuna"]=series["comuna"].str.upper()

                if Chart=='Stores Heat Map':
                    fields   = ["stores_count", "cantidad", "total"]
                    aliases  = ["Total Stores", "Total Sales Units", "Total invoice value $"]
                    caption  = f"Total Number of Stores by location"
                else:
                    fields   = ["cantidad", "stores_count", "total"]
                    aliases  = ["Total Sales Units", "Total Stores", "Total invoice value $"]
                    caption  = f"Total Number of Sales by location"
                m = heatmap(series, geodata, location, fields, aliases, caption)
                m.save("models/Geolocation/Maps/Map.html")
                file = open("models/Geolocation/Maps/Map.html", "r").read()

    #except:
    #    print("Chart Type is not selected")
    #    file = ""
        return [file]
  
@app.callback(Output('manu', 'options'), [Input('Product_type','value')])
def update_manufact_list(product_type):
    options = []
    try:
        new_list=run_query("select distinct fabricante, nombre_fabricante from historicopedidos h\
                            left join categorias c on h.material=c.material\
                            inner join (select distinct product from forecast_results) r on r.product=h.material   \
                            where c.nombre_cat = upper('"+product_type+"')", engine).to_dict(orient='records')
        options=[]
        for option in new_list:
            options.append({"label": option['nombre_fabricante'], "value": option['fabricante']})
    except:
        print('Error updating list')
    return options

@app.callback(Output('Product_sub', 'options'), [Input('Product_type','value'),Input('manu','value')])
def update_product_list(product_type, manu):
    options = []
    try:
        new_list=run_query("select distinct r.product as material,c.texto_breve_de_material \
            from forecast_results r \
            inner join categorias c on c.material=r.product \
            left join (select distinct material, fabricante from historicopedidos) h on r.product = h.material\
            where c.nombre_cat = upper('"+product_type+"')\
            and h.fabricante = "+ str(manu) , engine).to_dict(orient='records')
        for option in new_list:
            options.append({"label": option['texto_breve_de_material'], "value": option['material']})
        
    except:
        print('Error updating list')
    return options
