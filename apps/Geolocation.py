import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from scripts.utils import my_dash_components as mydbc
import dash

chart_typ_lbl = ["Heat Map", "Location Distribution"]
city_lbl = ["Cali", "Medellín"]
mfr_lbl = ["Colanta", "Alquería", "Leche la Mejor"]
prod_lbl = ["Lacteos", "Harinas", "Bebidas Gaseosas"]
str_typ_lbl = ["Tipo 1", "Tipo 2", "Tipo 3"]
intvl_lbl = ["Weekly", "Monthly", "Annual"]



# ####Geolocation
# import folium
# import json

# location = {'Bogota': [4.6097100, -74.0817500],
#             'Medellin':[6.27162785, -75.60281325266426],
#             'Cali': [3.4517923, -76.5324943]}


# with open('Models/Geolocation/geojson_data/Comunas_medellin.geojson') as json_file:
#     geoJsonData_Medellin = json.load(json_file)
    
# m = folium.Map(location=location['Medellin'], zoom_start=12)
# folium.GeoJson(geoJsonData_Medellin,
#     style_function=lambda x: {
#         'color' : "#1f1a95",
#         'weight' : 2,
#         'opacity': 0.6,
#         }).add_to(m)

# m.save("Map.html")

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
             dbc.Col(mydbc.dropdown(label="Chart type", list_options = chart_typ_lbl),
                    width = 6)
         ]),
         dbc.Row(
         [
             dbc.Col(mydbc.dropdown(label="City", list_options = city_lbl)),
             dbc.Col(mydbc.dropdown(label="Manufacturer", list_options = mfr_lbl)),
             dbc.Col(mydbc.dropdown(label="Product type", list_options = prod_lbl)),
             dbc.Col(mydbc.dropdown(label="Store type", list_options = str_typ_lbl)),
         ]),
         dbc.Row(
         [
             dbc.Col(mydbc.dropdown(label="Interval", list_options = intvl_lbl)),
             dbc.Col(mydbc.slider(label="Date", id="my-slider"))
         ]),
         dbc.Row(
         [
            html.Div(className = "embed-responsive embed-responsive-16by9 my-4",
                children = [html.Iframe(id= "map", srcDoc = open("Models/Geolocation/Maps/Map.html", "r").read())],
            )
         ])
     ]
)

layout = html.Div(children=[
        mydbc.card(content=content, title="Geolocation", description="Here you can find interesting data about Teaté's stores location", color="light", footer="footer")
    ], className="my-2")


