# data_cleaning_validation.py
# author: Catherine Meng
# date: 2024-12-04

import click
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.check_csv import check_csv
from src.validate_correlation import validate_correlation
from src.validate_distribution import validate_distribution
from src.validate_schema import validate_schema

@click.command()
@click.option('--file_path', type=str, help="path of datafile")
def main(file_path):

    """Downloads data zip data from the web to a local filepath and extracts it."""
    try:
        if not check_csv(file_path):
            print(f"{file_path} is not a CSV file.")
    except Exception as e:
        print("Error with data validation. Please check source data file.", e)

    df = pd.read_csv(file_path, delimiter=';')

    # Remove extra '\t' from the column name
    df.rename(columns = {"Daytime/evening attendance\t" : "Daytime/evening attendance"}, inplace = True)

    # Remove ' from column name to prevent issues with Altair plots
    df.columns = df.columns.str.replace("'s", "", regex=False)

    # Save cleanred data
    df.to_csv("data/processed/clean_data.csv")

    # Run data validation
    validate_schema(df)
    validate_distribution(df)
    validate_correlation(df)
    print("Data validation success.")

    # Split train and test data set
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)

    train.to_csv("data/processed/train_data.csv")
    test.to_csv("data/processed/test_data.csv")

if __name__ == '__main__':
    main()
