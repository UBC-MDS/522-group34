import sys
import os
import pandas as pd
import pytest
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from unittest.mock import patch
from scipy.stats import randint

# Add project path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.model import load_data, build_preprocessor, build_pipeline, perform_random_search, save_best_model, evaluate_model

@pytest.fixture
def data():
    # Dummy data for testing
    data_train = {
	    "Target": [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
	    "Previous qualification (grade)": [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7],
	    "Admission grade": [70, 80, 90, 85, 75, 82, 78, 88, 77, 82, 91, 84, 79, 86, 80],
	    "Age at enrollment": [20, 21, 22, 23, 19, 24, 22, 23, 21, 20, 24, 25, 19, 23, 22]
    }
    
    data_test = {
        "Target": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
	    "Previous qualification (grade)": [5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7],
	    "Admission grade": [72, 81, 88, 84, 77, 85, 90, 80, 87, 82, 91, 84, 78, 86, 79],
	    "Age at enrollment": [21, 22, 23, 24, 20, 25, 21, 22, 23, 24, 20, 21, 22, 23, 24]
    }
    
    train_df = pd.DataFrame(data_train)
    test_df = pd.DataFrame(data_test)
    
    train_path = "train.csv"
    test_path = "test.csv"
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    yield train_path, test_path
    
    os.remove(train_path)
    os.remove(test_path)

def test_load_data(data):
    train_path, test_path = data
    X_train, y_train, X_test, y_test = load_data(train_path, test_path)
    
    assert len(X_train) == 15
    assert len(y_train) == 15
    assert len(X_test) == 15
    assert len(y_test) == 15

def test_build_preprocessor():
    preprocessor = build_preprocessor()
    assert preprocessor is not None

def test_build_pipeline():
    preprocessor = build_preprocessor()
    pipeline = build_pipeline(preprocessor)
    assert pipeline is not None





