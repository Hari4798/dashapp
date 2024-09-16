#1 import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

#2 incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#3 intialize the app 
app = Dash(__name__)

server = app.server


#4 app layout
app.layout = html.Div([
    html.Div(style={'background-image': 'dash-project/images/Summer-04.jpg', 'background-repeat': 'no-repeat',
'background-position': 'right top',
'background-size': '150px 100px' },children= '', id ="title"),
    dcc.Dropdown(options=['pop', 'lifeExp', 'gdpPercap'], value="lifeExp", id='drop-down', placeholder="Select a KPI", style={'width': '50%', 'margin': 'auto', 'display': 'block'}),
    dcc.Graph( id="histogram", figure={}, style={'display': 'inline-block'}), # added inline block
    dcc.Graph( id="bar", figure={}, style={'display': 'inline-block'}), # added inline block
    dcc.Graph( id="pie", figure={}, style={'display': 'inline-block'}), # added inline block

])



#5 callback function
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Output(component_id='bar', component_property='figure'),
    Output(component_id='pie', component_property='figure'),
    Output(component_id='title', component_property='children'),
    Input(component_id='drop-down', component_property='value'),
    Input(component_id='drop-down', component_property='value'),
    Input(component_id='drop-down', component_property='value'),
    

)

def update(kpi_selected, kpi_selected2, kpi_selected3):
    #print(kpi_selected)
    fig = px.histogram(df, x='continent', y=kpi_selected, title= {} )
    fig2 = px.bar(df, x='continent', y=kpi_selected2, title= {})
    fig3 = px.pie(df, values=kpi_selected3, names='continent', title={})

    return fig, fig2,fig3, kpi_selected


#6 Run app
if __name__ == '__main__':
    app.run_server(debug=True)
