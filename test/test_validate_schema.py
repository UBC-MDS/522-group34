import pytest
import pandera as pa
import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validate_schema import validate_schema 

def test_valid_data():
    # Test case where dataframe conforms to the schema
    data = {
        "Marital status": [1, 2],
        "Application mode": [1, 2],
        "Application order": [0, 1],
        "Course": [33, 171],
        "Daytime/evening attendance": [1, 0],
        "Previous qualification": [1, 2],
        "Previous qualification (grade)": [100.5, 180],
        "Nacionality": [1, 2],
        "Mother qualification": [1, 2],
        "Father qualification": [3, 4],
        "Mother occupation": [0, 1],
        "Father occupation": [0, 1],
        "Admission grade": [180.5, 190.0],
        "Displaced": [0, 1],
        "Educational special needs": [0, 1],
        "Debtor": [0, 1],
        "Tuition fees up to date": [1, 0],
        "Gender": [0, 1],
        "Scholarship holder": [0, 1],
        "Age at enrollment": [20, 25],
        "International": [0, 1],
        "Curricular units 1st sem (credited)": [10, 12],
        "Curricular units 1st sem (enrolled)": [10, 12],
        "Curricular units 1st sem (evaluations)": [10, 12],
        "Curricular units 1st sem (approved)": [8, 10],
        "Curricular units 1st sem (grade)": [18.5, 19.0],
        "Curricular units 1st sem (without evaluations)": [0, 0],
        "Curricular units 2nd sem (credited)": [10, 12],
        "Curricular units 2nd sem (enrolled)": [10, 12],
        "Curricular units 2nd sem (evaluations)": [10, 12],
        "Curricular units 2nd sem (approved)": [8, 10],
        "Curricular units 2nd sem (grade)": [18.5, 19.0],
        "Curricular units 2nd sem (without evaluations)": [0, 0],
        "Unemployment rate": [5.5, 6.2],
        "Inflation rate": [2.3, 2.4],
        "GDP": [50000.3, 51000.2],
        "Target": ["Dropout", "Graduate"]
    }
    
    df = pd.DataFrame(data)
    
    # Call the validation function
    try:
        validate_schema(df)
    except Exception as e:
        pytest.fail(f"Validation failed with error: {e}")
        

def test_invalid_data_out_of_range():
    # Test case with data outside the allowed range (e.g., Application mode 99 which is invalid)
    data = {
        "Marital status": [1],
        "Application mode": [99],  # Invalid
        "Application order": [0],
        "Course": [33],
        "Daytime/evening attendance": [1],
        "Previous qualification": [1],
        "Previous qualification (grade)": [150],
        "Nacionality": [1],
        "Mother qualification": [1],
        "Father qualification": [3],
        "Mother occupation": [0],
        "Father occupation": [0],
        "Admission grade": [180],
        "Displaced": [0],
        "Educational special needs": [0],
        "Debtor": [0],
        "Tuition fees up to date": [1],
        "Gender": [0],
        "Scholarship holder": [0],
        "Age at enrollment": [20],
        "International": [0],
        "Curricular units 1st sem (credited)": [10],
        "Curricular units 1st sem (enrolled)": [10],
        "Curricular units 1st sem (evaluations)": [10],
        "Curricular units 1st sem (approved)": [8],
        "Curricular units 1st sem (grade)": [18.5],
        "Curricular units 1st sem (without evaluations)": [0],
        "Curricular units 2nd sem (credited)": [10],
        "Curricular units 2nd sem (enrolled)": [10],
        "Curricular units 2nd sem (evaluations)": [10],
        "Curricular units 2nd sem (approved)": [8],
        "Curricular units 2nd sem (grade)": [18.5],
        "Curricular units 2nd sem (without evaluations)": [0],
        "Unemployment rate": [5.5],
        "Inflation rate": [2.3],
        "GDP": [50000],
        "Target": ["Dropout"]
    }
    
    df = pd.DataFrame(data)
    
    # Call the validation function and expect it to raise a schema validation error
    with pytest.raises(Exception) as excinfo:
        validate_schema(df)
    
    assert "Application mode" in str(excinfo.value)


def test_duplicate_data():
    # Test case where duplicate rows exist
    data = {
        "Marital status": [1, 1],
        "Application mode": [1, 1],
        "Application order": [0, 0],
        "Course": [33, 33],
        "Daytime/evening attendance": [1, 1],
        "Previous qualification": [1, 1],
        "Previous qualification (grade)": [100.5, 100.5],
        "Nacionality": [1, 1],
        "Mother qualification": [1, 1],
        "Father qualification": [3, 3],
        "Mother occupation": [0, 0],
        "Father occupation": [0, 0],
        "Admission grade": [180, 180],
        "Displaced": [0, 0],
        "Educational special needs": [0, 0],
        "Debtor": [0, 0],
        "Tuition fees up to date": [1, 1],
        "Gender": [0, 0],
        "Scholarship holder": [0, 0],
        "Age at enrollment": [20, 20],
        "International": [0, 0],
        "Curricular units 1st sem (credited)": [10, 10],
        "Curricular units 1st sem (enrolled)": [10, 10],
        "Curricular units 1st sem (evaluations)": [10, 10],
        "Curricular units 1st sem (approved)": [8, 8],
        "Curricular units 1st sem (grade)": [18.5, 18.5],
        "Curricular units 1st sem (without evaluations)": [0, 0],
        "Curricular units 2nd sem (credited)": [10, 10],
        "Curricular units 2nd sem (enrolled)": [10, 10],
        "Curricular units 2nd sem (evaluations)": [10, 10],
        "Curricular units 2nd sem (approved)": [8, 8],
        "Curricular units 2nd sem (grade)": [18.5, 18.5],
        "Curricular units 2nd sem (without evaluations)": [0, 0],
        "Unemployment rate": [5.5, 5.5],
        "Inflation rate": [2.3, 2.3],
        "GDP": [50000, 50000],
        "Target": ["Dropout", "Dropout"]
    }
    
    df = pd.DataFrame(data)
    
    # Call the validation function and expect it to raise a schema validation error due to duplicates
    with pytest.raises(Exception) as excinfo:
        validate_schema(df)
    
    assert "Duplicate rows found." in str(excinfo.value)


def test_empty_row():
    # Test case where the dataframe has an empty row
    data = {
        "Marital status": [1, None],
        "Application mode": [1, None],
        "Application order": [0, None],
        "Course": [33, None],
        "Daytime/evening attendance": [1, None],
        "Previous qualification": [1, None],
        "Previous qualification (grade)": [100.5, None],
        "Nacionality": [1, None],
        "Mother qualification": [1, None],
        "Father qualification": [3, None],
        "Mother occupation": [0, None],
        "Father occupation": [0, None],
        "Admission grade": [180, None],
        "Displaced": [0, None],
        "Educational special needs": [0, None],
        "Debtor": [0, None],
        "Tuition fees up to date": [1, None],
        "Gender": [0, None],
        "Scholarship holder": [0, None],
        "Age at enrollment": [20, None],
        "International": [0, None],
        "Curricular units 1st sem (credited)": [10, None],
        "Curricular units 1st sem (enrolled)": [10, None],
        "Curricular units 1st sem (evaluations)": [10, None],
        "Curricular units 1st sem (approved)": [8, None],
        "Curricular units 1st sem (grade)": [18.5, None],
        "Curricular units 1st sem (without evaluations)": [0, None],
        "Curricular units 2nd sem (credited)": [10, None],
        "Curricular units 2nd sem (enrolled)": [10, None],
        "Curricular units 2nd sem (evaluations)": [10, None],
        "Curricular units 2nd sem (approved)": [8, None],
        "Curricular units 2nd sem (grade)": [18.5, None],
        "Curricular units 2nd sem (without evaluations)": [0, None],
        "Unemployment rate": [5.5, None],
        "Inflation rate": [2.3, None],
        "GDP": [50000, None],
        "Target": ["Dropout", None]
    }
    
    df = pd.DataFrame(data)
    
    # Call the validation function and expect it to raise a schema validation error due to empty row
    with pytest.raises(Exception) as excinfo:
        validate_schema(df)
    
    assert "Empty rows found." in str(excinfo.value)