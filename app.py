import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from diagram_generator import generate_methodology_diagram
import os

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Generate the methodology diagram (auto-generated when the app starts)
generate_methodology_diagram()

# Create some dummy data (This should be replaced with actual Covid-19 data source)
data = {
    'Country': ['USA', 'India', 'Brazil', 'Russia', 'Turkey'],
    'Cases': [34000000, 31000000, 22000000, 17000000, 15000000],
    'Deaths': [600000, 400000, 600000, 300000, 150000],
    'Recovered': [25000000, 28000000, 21000000, 15000000, 13000000]
}

df = pd.DataFrame(data)

# Layout of the dashboard
app.layout = html.Div([
    # Navigation Bar with icons
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink([html.Img(src="/assets/icons/home.jpg", style={'width': '20px', 'height': '20px'}), "Home"], href="#", className="nav-link")),
            dbc.NavItem(dbc.NavLink([html.Img(src="/assets/icons/data.png", style={'width': '20px', 'height': '20px'}), "Data"], href="#", className="nav-link")),
            dbc.NavItem(dbc.NavLink([html.Img(src="/assets/icons/diagram.png", style={'width': '20px', 'height': '20px'}), "Methodology"], href="#", className="nav-link")),
        ],
        brand="Covid-19 Data Analysis Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
    ),

    # Main Content Area
    html.Div([
        # Section for Dashboard Introduction
        html.Div([
            html.H2("Welcome to the Covid-19 Data Analysis Dashboard"),
            html.P("This dashboard provides real-time insights into global and country-specific Covid-19 data."),
        ], style={'padding': '20px', 'textAlign': 'center'}),

        # Section for Data Visualization
        html.Div([
            html.H3("Covid-19 Global Data", style={'textAlign': 'center'}),
            dcc.Graph(
                id="covid-bar-chart",
                figure=px.bar(df, x="Country", y=["Cases", "Deaths", "Recovered"],
                              title="Covid-19 Statistics per Country", barmode="group")
            ),
        ], style={'padding': '20px'}),

        # Section for Methodology Diagram
        html.Div([
            html.H3("Methodology Diagram", style={'textAlign': 'center'}),
            html.Img(src="/assets/methodology_diagram.png", style={'width': '50%', 'height': 'auto', 'display': 'block', 'margin': '0 auto'}),
        ], style={'padding': '20px'}),

        # Footer with Contact Info
        html.Div([
            html.P("Created by Your Name - 2024", style={'textAlign': 'center', 'color': 'gray'}),
        ], style={'padding': '20px', 'textAlign': 'center', 'backgroundColor': '#f8f9fa'}),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
