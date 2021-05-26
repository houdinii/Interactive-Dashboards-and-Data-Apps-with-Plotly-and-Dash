# Imports
import dash
import dash_html_components as html
import dash_core_components as dcc

# App instantiatino
app = dash.Dash(__name__)

# List of HTML and/or interactive components
app.layout = html.Div([
    dcc.Dropdown()
    dcc.Graph()
])

# callback functions
@app.callback()
def example():
    pass

# Run the app
if __name__ == '__main__':
    app.run_server()
