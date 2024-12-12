# eda_plots.py
# author: Siddarth
# date: 2024-12-11

import altair as alt
import pandas as pd

def plot_categorical_features(df, categorical_features, figure_path):
    """
    Plots bar charts for each categorical feature in the provided list
    and saves the figure as a PNG image.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    categorical_features (list): List of categorical column names to plot.
    figure_path (str): Path where the figure should be saved.
    """
    categorical_figures = alt.Chart(df).mark_bar().encode(
        x = alt.X(alt.repeat()).type('quantitative'),
        y = 'count():Q',
        column = alt.Column('Target:N', title=None),
        color = alt.Color('Target:N', legend=None)
    ).properties(
        width=120,
        height=80
    ).resolve_scale(
        y='independent'
    ).repeat(
        categorical_features,
        columns=1
    )

    # Save the plot to the given path
    categorical_figures.save(f"{figure_path}/eda_categorical.png")
