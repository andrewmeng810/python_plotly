#! usr/bin/env python 3


import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()
colors = {'background':'#111111', 'text': '#7FDBFF'}
# Creating Data

np.random.seed(100)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([dcc.Graph(id = 'scatter_plot',
                        figure ={'data': [
                                go.Scatter(
                                x= random_x,
                                y= random_y,
                                mode= 'markers',
                                marker = {
                                'size': 12,
                                'color': 'rgb(51,204,153)',
                                'line':{'width': 2}
                                }
                                )],
                        'layout':go.Layout(title= 'My Scatter Plot',
                                            xaxis= {'title': 'random x title'})}
                        ),
                        dcc.Graph(id = 'scatter_plot2',
                                                figure ={'data': [
                                                        go.Scatter(
                                                        x= random_x,
                                                        y= random_y,
                                                        mode= 'markers',
                                                        marker = {
                                                        'size': 12,
                                                        'color': 'rgb(200,204,153)',
                                                        'line':{'width': 2}
                                                        }
                                                        )],
                                                'layout':go.Layout(title= 'My Scatter Plot',
                                                                    xaxis= {'title': 'random x title'})}
                                                )

                        ])
if __name__ == '__main__':
    app.run_server()
