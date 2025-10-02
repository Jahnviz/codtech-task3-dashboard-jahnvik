from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv("data/sample_sales.csv")

# Initialize app
app = Dash(__name__)
app.title = "Task 3 Dashboard — Jahnvi Khurana"

# Layout
app.layout = html.Div([
    html.H1("Task 3 Dashboard — Jahnvi Khurana"),
    dcc.Dropdown(
        id="category",
        options=[{"label": c, "value": c} for c in df["category"].unique()],
        value=df["category"].unique()[0],
        clearable=False
    ),
    dcc.Graph(id="bar-chart")
])

# Callback
@app.callback(
    Output("bar-chart", "figure"),
    Input("category", "value")
)
def update_chart(selected_category):
    dff = df[df["category"] == selected_category]
    fig = px.bar(
        dff,
        x="product",
        y="sales",
        title=f"Sales for {selected_category}",
        text_auto=True
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True, port=8050)
