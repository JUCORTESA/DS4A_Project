import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import dash
import sys
from datetime import date

sys.path.append('../')

from app import app


class my_dash_components:

    def table(dataframe, max_rows=10):
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in
                    dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

    def card(title="", description="", content="", footer="", color=""):
        return dbc.Card(className="m-5 p-2", children=
        [
            dbc.CardHeader(children=[html.H4(title, className="card-title"),
                                     html.P(description,
                                            className="card-text text-muted")],
                           className="mx-2 px-5 mt-2 pt-2"),
            dbc.CardBody(
                children=[
                    content
                ],
                className="m-2 px-5 pt-2",
            ),
            dbc.CardFooter(footer),

        ], color=color
                        )

    def dropdown(label="", list_options=[], id=""):
        options = []
        for option in list_options:
            options.append({"label": option, "value": option})
        return dbc.FormGroup(
            [
                dbc.Label(label, html_for=id,
                          className="col-form-label col-sm"),
                html.Div(className="col-sm",
                         children=[
                             dcc.Dropdown(
                                 id=id,
                                 options=options,
                                 className="col-sm",
                             )
                         ]
                         ),
            ],
            # row = True
        )

    def slider(label="", id="", min=0, max=10, step=1):
        slider = dbc.FormGroup(className="align-middle", children=
        [
            dbc.Label(label, html_for=id, className="col-form-label col-sm"),
            dbc.FormGroup(className="col-sm",
                          children=[
                              dcc.Slider(id=id, min=min, max=max, step=step,
                                         value=0,
                                         className="col-sm"),
                              html.Div(id='slider-output-container-' + id,
                                       className="col-sm align-middle")
                          ],
                          row=True
                          ),

        ],
                               # row = True
                               )

        @app.callback(
            dash.dependencies.Output('slider-output-container-' + id,
                                     'children'),
            [dash.dependencies.Input(id, 'value')])
        def update_output(value):
            return dbc.Label(value, html_for="range-slider")

        return slider

    def date_picker(label="", id="", start_date = date.today() ):
        return dbc.FormGroup(
            [
                html.Label(label, className="col-sm"),
                dcc.DatePickerRange(className="col-sm",
                    id=id,
                    start_date=start_date,
                    end_date_placeholder_text='Select a date!'
                )
            ]
            )