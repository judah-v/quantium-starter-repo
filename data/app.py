from dash import Dash, html, dcc, Input, Output, callback
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('quantium-starter-repo\\data\\output_file.csv')

regions = {
    'North': [df[df['region'] == 'north'], 'green'],
    'South': [df[df['region'] == 'south'], 'red'],
    'East': [df[df['region'] == 'east'], 'orange'],
    'West': [df[df['region'] == 'west'], 'purple'],
    'All': [df, 'blue'],
}

graph = dcc.Graph(
    id='line-graph',
    figure={
        'data': [
            go.Scatter(
                x = df['date'],
                y = df['sales'],
                mode = 'lines',
                name = 'Sales'
            )
        ],
        'layout':{
            'title':'Sales before and after price change'
        }
    }
)

app = Dash()
app.layout = [
    html.H1("Pink morsel Sales Data"),
    dcc.RadioItems(id='radio', options=['North', 'South', 'East', 'West', 'All'], value='All'),
    graph,
]

@callback(
    Output(component_id='line-graph', component_property='figure'),
    Input(component_id='radio', component_property='value')
)
def get_line(region):
    region_df = regions[region]
    figure={
        'data': [
            go.Scatter(
                x = region_df[0]['date'],
                y = region_df[0]['sales'],
                mode = 'lines',
                name = region + ' Region',
                line = {'color': region_df[1]}
            )
        ],
        'layout':{
            'title':'Sales before and after price change'
        }
    }
    return figure 


if __name__ == '__main__':
    app.run(debug=True)