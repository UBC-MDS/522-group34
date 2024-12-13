import pandera as pa
import pandas as pd
import numpy as np

def validate_schema(df):
    """
    Validates the schema of a DataFrame by checking if it contains all the required columns.

    This function compares the columns in the given DataFrame to a list of required columns 
    and raises an exception if any required columns are missing. It checks for exact matches 
    in column names, ensuring that all expected columns are present.

    Args:
        df (pd.DataFrame): The DataFrame whose schema is to be validated.
        required_columns (list): A list of column names that must be present in the DataFrame.

    Raises:
        Exception: If any of the required columns are missing from the DataFrame, an exception is raised
                  with a message specifying the missing columns.
    """
    
    schema = pa.DataFrameSchema(
        {
            "Marital status": pa.Column(int, pa.Check.isin([1, 2, 3, 4, 5, 6]), 
                                        nullable=True),
            "Application mode": pa.Column(int, pa.Check.isin(
                [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 
                27, 39, 42, 43, 44, 51, 53, 57])),
            "Application order": pa.Column(int, pa.Check.isin(
                [0, 1, 2, 3, 4, 5, 6, 9])),
            "Course": pa.Column(int, pa.Check.isin(
                [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 
                9254, 9500, 9556, 9670, 9773, 9853, 9991]), nullable=True), 
            "Daytime/evening attendance": pa.Column(int, pa.Check.isin(
                [0, 1]), nullable=True),
            "Previous qualification": pa.Column(int, pa.Check.isin(
                [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43])),
            "Previous qualification (grade)": pa.Column(float, pa.Check.between(
                0, 200)),
            "Nacionality": pa.Column(int, pa.Check.isin(
                [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 
                100, 101, 103, 105, 108, 109]), nullable=True),
            "Mother qualification": pa.Column(int, pa.Check.isin(
                [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 
                34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), nullable=True),
            "Father qualification": pa.Column(int, pa.Check.isin(
                [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 22, 25, 
                26, 27,29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
                43, 44]), nullable=True),
            "Mother occupation": pa.Column(int, pa.Check.isin(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131,
             132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 
             192, 193, 194]), nullable=True),
            "Father occupation": pa.Column(int, pa.Check.isin(
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 
                112, 114, 121, 122, 123, 124, 131, 132, 134, 135, 141, 143, 
                144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 
                181, 182, 183, 192, 193, 194, 195]), nullable=True),
            "Admission grade": pa.Column(float, pa.Check.between(0, 200), 
                                        nullable=True),
            "Displaced": pa.Column(int, pa.Check.isin([0, 1]), nullable=True), 
            "Educational special needs": pa.Column(int, pa.Check.isin([0, 1]), 
                                                nullable=True),
            "Debtor": pa.Column(int, pa.Check.isin([0, 1]), nullable=True),
            "Tuition fees up to date": pa.Column(int, pa.Check.isin([0, 1]), 
                                                nullable=True),
            "Gender": pa.Column(int, pa.Check.isin([0, 1]), nullable=True),
            "Scholarship holder": pa.Column(int, pa.Check.isin([0, 1]), 
                                            nullable=True),
            "Age at enrollment": pa.Column(int, pa.Check.between(15, 100), 
                                        nullable=True),
            "International": pa.Column(int, pa.Check.isin([0, 1]), 
                                    nullable=True),
            "Curricular units 1st sem (credited)": pa.Column(int, 
                                                            nullable=True),
            "Curricular units 1st sem (enrolled)": pa.Column(int, 
                                                            nullable=True),
            "Curricular units 1st sem (evaluations)": pa.Column(int, 
                                                                nullable=True), 
            "Curricular units 1st sem (approved)": pa.Column(int, 
                                                            nullable=True),
            "Curricular units 1st sem (grade)": pa.Column(
                float, pa.Check.between(0, 20), nullable=True),
            "Curricular units 1st sem (without evaluations)": pa.Column(
                int, nullable=True),
            "Curricular units 2nd sem (credited)": pa.Column(
                int, nullable=True),
            "Curricular units 2nd sem (enrolled)": pa.Column(
                int, nullable=True),
            "Curricular units 2nd sem (evaluations)": pa.Column(
                int, nullable=True),
            "Curricular units 2nd sem (approved)": pa.Column(int, nullable=True),
            "Curricular units 2nd sem (grade)": pa.Column(
                float, pa.Check.between(0, 20), nullable=True),
            "Curricular units 2nd sem (without evaluations)": pa.Column(
                int, nullable=True),
            "Unemployment rate": pa.Column(float, nullable=True),
            "Inflation rate": pa.Column(float, nullable=True),
            "GDP": pa.Column(float, nullable=True),
            "Target": pa.Column(str, pa.Check.isin(
                ['Dropout', 'Enrolled', 'Graduate']))
        },
        checks=[
            pa.Check(lambda df: ~df.duplicated().any(), 
                    error="Duplicate rows found."),
            pa.Check(lambda df: ~(df.isna().all(axis=1)).any(), 
                    error="Empty rows found.")
        ]
    )

    schema.validate(df, lazy=True)