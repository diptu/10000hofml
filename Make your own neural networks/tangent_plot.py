import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output, State


# Function and derivative
def f(x):
    return x**2


def df(x):
    return 2 * x


x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("Click or Enter x-value to show tangent on f(x) = x²"),
        html.Div(
            [
                html.Label("Enter x-value:"),
                dcc.Input(
                    id="x-input",
                    type="number",
                    debounce=True,
                    placeholder="e.g. 2.5",
                    value=0,  # initial value synced with initial tangent
                ),
            ],
            style={"marginBottom": "20px"},
        ),
        dcc.Graph(
            id="function-plot", config={"scrollZoom": True}, style={"height": "600px"}
        ),
    ]
)


# Update graph when input or click changes
@app.callback(
    Output("function-plot", "figure"),
    Input("x-input", "value"),
)
def update_graph(x0):
    # Defensive: if None or out of bounds, default to 0
    if x0 is None:
        x0 = 0

    slope = df(x0)
    y0 = f(x0)
    tangent_y = y0 + slope * (x_vals - x0)

    color = "green" if slope > 0 else "red" if slope < 0 else "gray"

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x_vals, y=y_vals, mode="lines", name="f(x) = x²", line=dict(color="blue")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x_vals,
            y=tangent_y,
            mode="lines",
            name=f"Tangent at x={x0:.2f}",
            line=dict(color=color, width=3, dash="dash"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[x0],
            y=[y0],
            mode="markers+text",
            marker=dict(size=10, color=color),
            text=[f"Slope: {slope:.2f}"],
            textposition="top center",
            name="Tangent Point",
        )
    )

    fig.update_layout(
        title="f(x) = x² and its Tangent Line",
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True,
    )
    return fig


# Update input box when clicking on the graph
@app.callback(
    Output("x-input", "value"),
    Input("function-plot", "clickData"),
    State("x-input", "value"),
)
def update_input_on_click(clickData, current_value):
    if clickData:
        clicked_x = clickData["points"][0]["x"]
        # Return clicked x to update input box
        return clicked_x
    # No click, keep current value
    return current_value


if __name__ == "__main__":
    app.run(debug=True)
