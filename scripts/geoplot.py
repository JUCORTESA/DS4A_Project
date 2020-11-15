import branca
import folium
import pandas as pd

def heatmap(series, geodata, location, fields, aliases, caption,
            colors=['white','yellow','orange','red','darkred']):
    if(len(series)==0):
        style_function=lambda x: {
                        'fillColor':'white',
                        'color' : "black",
                        'weight' : 2,
                        'fillOpacity': 0.6,
                        }
        m = folium.Map(location=location, zoom_start=12)
        stategeo = folium.GeoJson(geodata,
                    style_function=style_function,
                    tooltip=folium.GeoJsonTooltip(
                       fields=['NOMBRE'],
                       aliases=['Comuna'], 
                       localize=True
            )).add_to(m)
    else:
        min_cn, max_cn = series[fields[0]].quantile([0.01,0.99]).apply(round, 2)
        colormap = branca.colormap.LinearColormap(
            colors=colors,
            vmin=min_cn,
            vmax=max_cn
        )

        colormap.caption=caption

        geodata = geodata.join(series.set_index("comuna"), how = "left", on = "NOMBRE")
        geodata.fillna(0, inplace = True)

        m = folium.Map(location=location,
                                zoom_start=12,
                                tiles="OpenStreetMap")
        style_function = lambda x: {
            'fillColor': colormap(x['properties'][fields[0]]),
            'color': 'black',
            'weight':2,
            'fillOpacity':0.6
        }

        stategeo = folium.GeoJson(
            geodata,
            name='Teaté Stores',
            style_function=style_function,
            tooltip=folium.GeoJsonTooltip(
                fields=['NOMBRE']+fields,
                aliases=['Comuna']+aliases, 
                localize=True
            )
        ).add_to(m)

        colormap.add_to(m)
    return m

citylocation = {'Bogota': [4.6097100, -74.0817500],
            'Medellin':[6.27162785, -75.60281325266426],
            'Cali': [3.4517923, -76.5324943]}

def df_to_geojson(df, properties):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for index, row in df.iterrows():
        try:
            feature = {'type':'Feature',
                       'properties':{},
                       'geometry':{'type':'Point',
                                   'coordinates':[]}}
            feature['geometry']['coordinates'] = [row[lon],row[lat]]
            feature['properties']["index"] = index+1
            for prop in properties:
                feature['properties'][prop] = row[prop]
            geojson['features'].append(feature)
        except:
            pass
    return geojson

def color_marker(index, min_cn, max_cn, 
                 colors=['white', 'beige', 'orange', 'lightred', 'red', 'darkred']):
    min_cn = min_cn-1
    max_cn = max_cn+1
    for i in range(len(colors)):
        if index>=(max_cn*(i/len(colors))+min_cn) and index<(max_cn*((i+1)/len(colors))+min_cn):
            return colors[i]
    return colors[-1]

def point_map(series, location, fields, aliases, caption,
              colors=['white', 'yellow', 'orange', 'red', 'darkred']):
    min_cn= series.index.min()+1
    max_cn= series.index.max()+1
    colormap = branca.colormap.LinearColormap(
        colors=colors,
        vmin=min_cn,
        vmax=max_cn
    )

    colormap.caption=caption


    m = folium.Map(location=location,
                            zoom_start=12,
                            tiles="OpenStreetMap")
    style_function = lambda x: {
        'radius': 6,
        'fill':True, # Set fill to True
        'fillColor':color_marker(x['properties']['index'], min_cn, max_cn),
        'color' : 'black',
        'fillOpacity':0.7
    }
    lat='latitud'
    lon='longitud'
    series=series.dropna(subset=[lat, lon])
    geodata = df_to_geojson(series, fields[1:])
    m = folium.Map(location=location,
                   zoom_start=12,
                   tiles="OpenStreetMap")
    for index, row in series.iterrows():
        #try:
            html = fancy_html(index, row, fields, aliases)
            iframe = branca.element.IFrame(html=html,width=400,height=300)
            
            folium.Marker(location=[row["latitud"],row["longitud"]],
                     popup= folium.Popup(iframe,parse_html=True),
                     icon = folium.Icon(color=color_marker(index, min_cn, max_cn))
                     ).add_to(m)
    colormap.add_to(m)
    return m

def fancy_html(index, row,  fields, aliases):
    left_col_colour = "#2A799C"
    right_col_colour = "#C5DCE7"
    
    html = '''<!DOCTYPE html>
<html>

    <table style="height: 126px; width: 300px;">
<tbody> '''
    
   
    
    for i, field in enumerate(fields):
        if field=="index":
             html = html+ f'''
        <tr>
            <td style="background-color:{left_col_colour};"><span style="color: #ffffff;">{aliases[i]}</span></td>
            <td style="width: 200px;background-color:{right_col_colour};">{index+1}</td>
        </tr>
        '''
        else:
            html = html+ f'''
            <tr>
                <td style="background-color:{left_col_colour};"><span style="color: #ffffff;">{aliases[i]}</span></td>
                <td style="width: 200px;background-color:{right_col_colour};">{row[field]}</td>
            </tr>
            '''
    html = html+'''
</tbody>
</table>
</html> 
'''
    return html