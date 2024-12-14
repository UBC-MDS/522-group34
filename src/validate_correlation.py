import pandas as pd
import numpy as np

def validate_correlation(df, corr_threshold = 0.95):
    """
    Validates the correlation between features and the target column in a DataFrame.

    This function calculates the pairwise correlation between numeric columns in the 
    provided DataFrame and checks if any correlations exceed the specified threshold.
    If any pair of columns has a correlation (in absolute value) greater than the threshold, 
    an exception is raised with a message indicating the columns involved.

    The target column is expected to be named 'Target' and is mapped to numeric values 
    for correlation calculation (e.g., 'Enrolled' = 0, 'Dropout' = 1, 'Graduate' = 2).

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be validated.
        corr_threshold (float, optional): The threshold above which correlations between columns 
                                          are considered too high. Default is 0.95.

    Raises:
        Exception: If any pair of features (or feature and target) has a correlation higher than 
                   the specified threshold, an exception is raised with a message specifying 
                   the correlated columns and their correlation value.
    """
    
    # Encode the target column with numeric values so correlation test can be done
    mapping = {"Enrolled": 0, "Dropout": 1, "Graduate": 2}
    validate_df = df.copy()
    validate_df["Target"] = validate_df["Target"].map(mapping)

    # Calculate pairwise correlations for all feature/feature and feature/target pairs
    correlations = validate_df.corr(numeric_only=True)

    # Identify highly correlated pairs
    for i in range(len(correlations)):
        for j in range(i + 1, len(correlations.columns)):
            corr_value = correlations.iloc[i, j]
            if abs(corr_value) > corr_threshold:
                pair = (correlations.index[i], correlations.columns[j])
                raise Exception(f"Correlation exceeds threshold for: {pair}.")