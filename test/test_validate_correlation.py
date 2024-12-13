import pytest
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validate_correlation import validate_correlation

def test_correlation_exceeds_threshold():
    data = {
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [2, 4, 6, 8, 10],  # Perfect correlation with Feature1
        "Feature3": [5, 4, 3, 2, 1],
        "Target": ["Enrolled", "Dropout", "Graduate", "Enrolled", "Dropout"]
    }
    df = pd.DataFrame(data)
    
    # Test that an exception is raised when correlation exceeds threshold
    with pytest.raises(Exception):
        validate_correlation(df)

def test_correlation_below_threshold():
    data = {
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 6, 7, 8, 9],  # Low correlation with Feature1
        "Feature3": [5, 4, 3, 2, 1],
        "Target": ["Enrolled", "Dropout", "Graduate", "Enrolled", "Dropout"]
    }
    df = pd.DataFrame(data)
    
    # Test that no exception is raised when correlation is below the threshold
    try:
        validate_correlation(df, corr_threshold=1)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")