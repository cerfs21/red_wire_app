# visualize v0.3:
#   Edit first axis title to mention the MW unit
#   Remove second and third axis titles

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Plot a bar graph to compare observed value and prediction
def make_figure_from_prediction(figure_df):

    # Create a new Figure
    fig = go.Figure()

    # Add a line for each value column
    fig.add_trace(go.Scatter(x=figure_df['datetime_utc'], y=figure_df['demanda'], mode='lines', name='Consommation'))
    fig.add_trace(go.Scatter(x=figure_df['datetime_utc'], y=figure_df['programada'], mode='lines', name='Planification', yaxis='y2'))
    fig.add_trace(go.Scatter(x=figure_df['datetime_utc'], y=figure_df['prevista'], mode='lines', name='Prédiction', yaxis='y3'))

    # Create layout with 3 y-axes corresponding to the 3 value columns
    fig.update_layout(
        yaxis=dict(title='Consommation en MW'),
        yaxis2=dict(overlaying='y', side='right'),
        yaxis3=dict(overlaying='y', side='right'),
        xaxis=dict(title='Date'),
        #title='Comparaison des valeurs de consommation, planification et prédiction',
    )

    return fig
