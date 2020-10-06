import dash_html_components as html
import pandas as pd

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def generate_card(title, subtitle, content):
    return html.Div(className = "card", children = [
        html.Div(className = "card-header", children = [
            html.H5(className = "card-title", children= [title]),
            html.P(className = "card-category" , children = [subtitle])
        ]), 
        html.Div(className = "card-body", children = [
            html.H5(className = "card-title", children= [content])
        ])
    ])