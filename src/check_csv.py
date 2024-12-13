import pandas as pd

# Check the file format
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
        pd.read_csv(file_path)
        return True
    except Exception:
        return False