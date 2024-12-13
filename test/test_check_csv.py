import pytest
import pandas as pd
import os
import sys
from io import StringIO
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.check_csv import check_csv

def test_check_csv_valid_file():
    # Create a mock valid CSV content
    csv_content = "name,age\nJohn,25\nAlice,30"
    
    # Use StringIO to simulate a CSV file
    file_path = 'test_valid.csv'
    with open(file_path, 'w') as f:
        f.write(csv_content)

    # Call the check_csv function
    result = check_csv(file_path)
    
    # Assert that the function returns True for a valid CSV
    assert result == True


def test_check_csv_invalid_file():
    # Create a mock invalid file (non-CSV content)
    non_csv_content = "This is not a CSV file!"
    
    # Use StringIO to simulate a non-CSV file (simulating a .txt file)
    file_path = 'test_invalid.txt'
    with open(file_path, 'w') as f:
        f.write(non_csv_content)

    # Call the check_csv function on a non-CSV file
    result = check_csv(file_path)
    
    # Assert that the function returns False for a non-CSV file
    assert result == False