import pytest
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validate_distribution import validate_distribution

def test_validate_distribution_within_range():
    # Create a DataFrame with values close to the reference values
    data = {
        "Marital status": [1.2, 1.1, 1.3, 1.2, 1.1],
        "Application mode": [18.6, 18.7, 19, 18.5, 18.8],
        "Application order": [1.7, 1.8, 1.7, 1.6, 1.8],
        "Course": [8856, 8857, 8855, 8856, 8857],
        "Target": ["Enrolled", "Dropout", "Graduate", "Enrolled", "Dropout"]
    }
    df = pd.DataFrame(data)
    
    # Test that no exception is raised when values are within 2 standard deviations of the reference mean
    try:
        validate_distribution(df)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_validate_distribution_outside_range():
    # Create a DataFrame with values significantly different from the reference means
    data = {
        "Marital status": [10, 11, 12, 13, 14],  # Much higher than expected mean
        "Application mode": [100, 105, 110, 120, 130],  # Much higher than expected mean
        "Application order": [10, 10, 10, 10, 10],  # High constant value
        "Course": [9000, 9100, 9200, 9300, 9400],  # Much higher than expected mean
        "Target": ["Enrolled", "Dropout", "Graduate", "Enrolled", "Dropout"]
    }
    df = pd.DataFrame(data)
    
    # Capture print statements or exceptions
    with pytest.raises(Exception):
        validate_distribution(df)

def test_validate_distribution_with_missing_data():
    # Create a DataFrame with missing values (NaN) in some columns
    data = {
        "Marital status": [1.2, np.nan, 1.3, 1.2, 1.1],
        "Application mode": [18.5, 18.7, np.nan, 18.6, 18.8],
        "Application order": [1.6, 1.7, 1.6, np.nan, 1.8],
        "Course": [8856, 8857, 8855, np.nan, 8857],
        "Target": ["Enrolled", "Dropout", "Graduate", "Enrolled", "Dropout"]
    }
    df = pd.DataFrame(data)
    
    # Test that no exception is raised despite the missing data (NaN values should be handled)
    try:
        validate_distribution(df)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")