# visualize v0.1:
#   Initial version for test purposes

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Plot a bar graph to compare observed value and prediction
def make_figure_from_prediction(demand, prediction):
    x=["Observation", "Prédiction"]
    y=[demand, prediction]
    fig = go.Figure([go.Bar(x=x, y=y , text=y, marker_color=['green', 'yellow'])])
    fig.update_layout(
        font_color='black',
        xaxis_tickfont_size=16,
        yaxis=dict(
            title='Consommation en MW',
            titlefont_size=16,
            tickfont_size=14),
    )
    return fig