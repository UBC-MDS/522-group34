# data_cleaning_validation.py
# author: Catherine Meng
# date: 2024-12-04

import click
import pandas as pd
from sklearn.model_selection import train_test_split
from itertools import combinations
import pandera as pa
from scipy.stats import chi2_contingency, pearsonr
import numpy as np

chi2_validation = {
    'Admission grade': np.float64(1436.5038834914599),
    'Age at enrollment': np.float64(547.2674289070418),
    'GDP': np.float64(51.965049926087076)
}

pearson_validation = {
    'Admission grade_Age at enrollment': -0.02991535667400831,
    'Admission grade_GDP': -0.019519481896555686,
    'Age at enrollment_GDP': -0.06467811172086718
}


# check the file format
def check_csv(file_path):
    """
    Check if the given file is a CSV file by its extension.

    Args:
    file_path (str): Path to the file.

    Returns:
    bool: True if the file is a CSV file, False otherwise.
    """
    # Check if file extension is .csv
    if not file_path.endswith(".csv"):
        return False

    # Try to read the file using pandas (this will raise an error if it's not a CSV file)
    try:
        pd.read_csv("file_path")
        return True
    except Exception:
        return False

# validate data set
def validate_data(file_path):
    """
    Check if the dataset meet our expectation and requirements. Raise errors if not.

    Args:
    file_path (str): Path to the file.
    """

    # Import data
    df = pd.read_csv(file_path, delimiter = ';')

    # Remove extra '\t' from the column name
    df.rename(columns = {"Daytime/evening attendance\t" : "Daytime/evening attendance"}, inplace = True)

    # Remove ' from column name to prevent issues with Altair plots
    df.columns = df.columns.str.replace("'s", "", regex=False)

    print("Data loaded.")

    df.to_csv("data/processed/clean_data.csv")

    print("Clean data saved to data/processed/clean_data.csv.")

    print("Starting data validation.")

    # validate data before split
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

    print("Validation schema result \n", schema.validate(df, lazy=True))

    #Check Target/response variable follows expected distribution
    # Calculate observed frequencies in the 'Target' column
    observed_frequencies = df['Target'].value_counts()
    print("Observed Frequencies:\n", observed_frequencies)

    # Calculate total number of students (observations)
    total_students = len(df)
    # Define the expected frequencies for a uniform distribution
    expected_frequencies = [total_students / len(observed_frequencies)] * len(observed_frequencies)
    print("\nExpected Frequencies (Uniform Distribution):", expected_frequencies)

    from scipy.stats import chisquare

    # Perform the Chi-Square goodness-of-fit test
    chi2_stat, p_value = chisquare(observed_frequencies, expected_frequencies)

    print(f"\nChi2 Stat: {chi2_stat}")
    print(f"P-Value: {p_value}")

    # Checking for anomalous correlations between target variable and a subset of features variables
    chi2_results = {}
    features = ['Admission grade', 'Age at enrollment', 'GDP']

    # Perform chi-square test for each feature
    for feature in features:
        # Create contingency table
        contingency_table = pd.crosstab(df[feature], df['Target'])
        
        # Perform chi-square test
        chi2_results[feature] = chi2_contingency(contingency_table).statistic

    # Check if the test statistic is approximately equal to pre-calculated values
    for feature in chi2_results:
        np.testing.assert_almost_equal(chi2_results[feature], chi2_validation[feature])

    # Checking for anomalous correlations between features
    pearson_results = {}
    feature_pairs = list(combinations(features, 2))

    # Perform Pearson test on each feature pairs
    for f1, f2 in feature_pairs:
        pearson_results[f1+'_'+f2] = pearsonr(df[f1], df[f2]).statistic
        
    # Check if the test statistic is approximately equal to pre-calculated values
    for pair in pearson_results:
        np.testing.assert_almost_equal(pearson_results[pair], pearson_validation[pair])

    # split train and test data set
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)

    print("Target classes \n:", train.nunique())

    train.to_csv("data/processed/train_data.csv")
    test.to_csv("data/processed/test_data.csv")
    print("Train and test data set are saved under /data/processed/.")


@click.command()
@click.option('--file_path', type=str, help="path of datafile")
def main(file_path):
    """Downloads data zip data from the web to a local filepath and extracts it."""
    try:
        if check_csv(file_path):
            print(f"{file_path} is a CSV file.")
        else:
            print(f"{file_path} is not a CSV file.")

        validate_data(file_path)

        print("Data validation success.")
    except Exception as e:
        print("There is an error happned whiling check the file type or doing the data validation: ", e)

if __name__ == '__main__':
    main()