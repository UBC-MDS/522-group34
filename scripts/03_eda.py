# eda.py
# author: Jenson Chang
# date: 2024-12-24

import click
import os
import altair as alt
import numpy as np
import pandas as pd
from eda_plots import plot_categorical_features
from eda_plots import plot_numerical_features

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

    

    plot_numerical_features(df, numeric_features, figure_path)
    # Call the function for categorical plot
    plot_categorical_features(df, categorical_features, figure_path)

if __name__ == "__main__":
    main()
