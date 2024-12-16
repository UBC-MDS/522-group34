import pandas as pd
import numpy as np

def validate_distribution(df):
    """
    Validates the distribution of numerical columns in a DataFrame by comparing their 
    mean values to reference means and standard deviations.

    This function checks if the mean of each numerical column in the given DataFrame 
    is within two standard deviations of the predefined reference mean for that column.
    If a column's mean deviates more than two standard deviations from the reference mean, 
    it raises an exception.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be validated. 
                            The DataFrame should have multiple columns with numerical values.

    Raises:
        Exception: If any column's mean deviates by more than two standard deviations 
                  from the reference mean, an exception is raised with a message specifying
                  the column name, its mean, and the reference mean.
    """

    ref_mean = pd.DataFrame({
        "Marital status": 1.178571429,
        "Application mode": 18.66907776,
        "Application order": 1.727848101,
        "Course": 8856.642631,
        "Daytime/evening attendance": 0.890822785,
        "Previous qualification": 4.577757685,
        "Previous qualification (grade)": 132.6133137,
        "Nacionality": 1.873191682,
        "Mother qualification": 19.5619349,
        "Father qualification": 22.27531646,
        "Mother occupation": 10.96089512,
        "Father occupation": 11.03232369,
        "Admission grade": 126.9781193,
        "Displaced": 0.548372514,
        "Educational special needs": 0.011528029,
        "Debtor": 0.113698011,
        "Tuition fees up to date": 0.880650995,
        "Gender": 0.351717902,
        "Scholarship holder": 0.248417722,
        "Age at enrollment": 23.26514467,
        "International": 0.024864376,
        "Curricular units 1st sem (credited)": 0.709990958,
        "Curricular units 1st sem (enrolled)": 6.27056962,
        "Curricular units 1st sem (evaluations)": 8.299050633,
        "Curricular units 1st sem (approved)": 4.706600362,
        "Curricular units 1st sem (grade)": 10.64082158,
        "Curricular units 1st sem (without evaluations)": 0.137658228,
        "Curricular units 2nd sem (credited)": 0.54181736,
        "Curricular units 2nd sem (enrolled)": 6.232142857,
        "Curricular units 2nd sem (evaluations)": 8.063291139,
        "Curricular units 2nd sem (approved)": 4.435804702,
        "Curricular units 2nd sem (grade)": 10.23020572,
        "Curricular units 2nd sem (without evaluations)": 0.150316456,
        "Unemployment rate": 11.56613924,
        "Inflation rate": 1.228028933,
        "GDP": 0.001968807
    }, index=[0])

    ref_std = pd.DataFrame({
        "Marital status": 0.605746946,
        "Application mode": 17.48468229,
        "Application order": 1.313793078,
        "Course": 2063.566416,
        "Daytime/evening attendance": 0.311896681,
        "Previous qualification": 10.21659234,
        "Previous qualification (grade)": 13.18833169,
        "Nacionality": 6.914514032,
        "Mother qualification": 15.60318632,
        "Father qualification": 15.34310781,
        "Mother occupation": 26.41825291,
        "Father occupation": 25.26304024,
        "Admission grade": 14.48200082,
        "Displaced": 0.497710853,
        "Educational special needs": 0.106760057,
        "Debtor": 0.31748001,
        "Tuition fees up to date": 0.324235383,
        "Gender": 0.477560437,
        "Scholarship holder": 0.432144154,
        "Age at enrollment": 7.587815615,
        "International": 0.155729319,
        "Curricular units 1st sem (credited)": 2.360506619,
        "Curricular units 1st sem (enrolled)": 2.480178175,
        "Curricular units 1st sem (evaluations)": 4.179105569,
        "Curricular units 1st sem (approved)": 3.09423798,
        "Curricular units 1st sem (grade)": 4.843663381,
        "Curricular units 1st sem (without evaluations)": 0.690880184,
        "Curricular units 2nd sem (credited)": 1.918546144,
        "Curricular units 2nd sem (enrolled)": 2.195950751,
        "Curricular units 2nd sem (evaluations)": 3.947950941,
        "Curricular units 2nd sem (approved)": 3.014763902,
        "Curricular units 2nd sem (grade)": 5.210807955,
        "Curricular units 2nd sem (without evaluations)": 0.753774069,
        "Unemployment rate": 2.663850484,
        "Inflation rate": 1.382710692,
        "GDP": 2.269935441
    }, index=[0])

    ref_prop = {
        'prop': {'Graduate': 0.5, 'Enrolled': 0.18, 'Dropout': 0.32},
        'std': 0.10
    }

    # Check distribution for all numeric columns by checking if the mean is 2 standard deviation away from the reference mean
    for column in df.columns:

        if column == 'Target':
            # Calculate the proportions of the categorical column
            proportions = df[column].value_counts(normalize=True, dropna=True).to_dict()

            # Check proportions
            for cat in ref_prop['prop']:
                expected_prop = ref_prop['prop'][cat]
                prop = proportions.get(cat, 0)
                std = ref_prop['std']
                
                if abs(prop - expected_prop) > 2*std:
                    raise Exception(f"Proportion for category {cat} in {column} is more than 2 standard deviation away from reference proportion:"
                                    f"Expected={expected_prop}, Calculated={prop}")

        else:
            col = df[column].dropna()

            # Calculate mean and standard deviation for data
            expected_mean = ref_mean.loc[0, column]
            expected_std = ref_std.loc[0, column]
            mean = col.mean()

            # Check if mean is 2*std away from reference mean
            if abs(mean - expected_mean) > 2*expected_std:
                raise Exception(f"Column {col} mean {mean} is 2 standard deviation away from reference mean {expected_mean}.")