from dash import Dash, html, dcc
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('quantium-starter-repo\\data\\output_file.csv')


north = df[df['region'] == 'north']
south = df[df['region'] == 'south']
east = df[df['region'] == 'east']
west = df[df['region'] == 'west']

app = Dash()
graph = dcc.Graph(
    'line-graph',
    figure={
        'data': [
            go.Scatter(
                x = north['date'],
                y = north['sales'],
                mode = 'lines',
                name = 'North Region'
            ), go.Scatter(
                x = south['date'],
                y = south['sales'],
                mode = 'lines',
                name = 'South Region'
            ), go.Scatter(
                x = east['date'],
                y = east['sales'],
                mode = 'lines',
                name = 'East Region'
            ), go.Scatter(
                x = west['date'],
                y = west['sales'],
                mode = 'lines',
                name = 'West Region'
            ), 
        ],
        'layout':{
            'title':'Sales before and after price change'
        }
    }
)

app.layout = [
    graph,
]

if __name__ == '__main__':
    app.run(debug=True)