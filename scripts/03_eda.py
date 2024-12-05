# eda.py
# author: Jenson Chang
# date: 2024-12-24

import click
import os
import altair as alt
import numpy as np
import pandas as pd

# main function

@click.command()
@click.option("--data_path", type=str)
@click.option("--figure_path", type=str)

def main(data_path, figure_path):
    # Read in cleaned data
    df = pd.read_csv(data_path)

    df.rename(columns = {"Daytime/evening attendance\t" : "Daytime/evening attendance"}, inplace = True)
    df.columns = df.columns.str.replace("'s", "", regex=False)

    # Group feature types based on feature description from source data
    categorical_features = ["Application order", "Course", "Nacionality", "Gender",
                            "Marital status", "Application mode", "Daytime/evening attendance",
                            "Previous qualification", "Mother qualification",  "Mother occupation", 
                            "Father qualification", "Father occupation", "Displaced", 
                            "Educational special needs", "Debtor", "Tuition fees up to date",
                            "Scholarship holder", "International"]

    numeric_features = ["Previous qualification (grade)", "Admission grade", "Age at enrollment",
                        "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)",
                        "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)",
                        "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)",
                        "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)",
                        "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)",
                        "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)",
                        "Unemployment rate", "Inflation rate", "GDP"]

    # Plot numerical features
    numerical_figures = alt.Chart(df).mark_rect().encode(
        x = alt.X(alt.repeat()).bin(maxbins=30),
        y = alt.Y('Target:N', title=None),
        color = alt.Color('count():Q').legend(orient="top")
    ).properties(
        width = 180
    ).repeat(
        numeric_features,
        columns = 2
    )
    numerical_figures.save(f"{figure_path}/eda_numerical.png")

    # Plot categorical and boolean features
    categorical_figures = alt.Chart(df).mark_bar().encode(
        x = alt.X(alt.repeat()).type('quantitative'),
        y = 'count():Q',
        column = alt.Column('Target:N', title = None),
        color = alt.Color('Target:N', legend = None)
    ).properties(
        width = 120,
        height = 80
    ).resolve_scale(
        y = 'independent'
    ).repeat(
        categorical_features,
        columns = 1
    )
    categorical_figures.save(f"{figure_path}/eda_categorical.png")

if __name__ == "__main__":
    main()
