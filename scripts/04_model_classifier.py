# 04_model_classifier.py
# author: Jingyuan Wang
# date: 2024-12-06

import click
import os
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from scipy.stats import randint
import pickle
from joblib import dump

@click.command()
@click.option("--data_path_train", type=str, help="Path to the training data")
@click.option("--data_path_test", type=str, help="Path to the test data")
@click.option("--pipeline_to", type=str, help="Path to save the best pipeline")

def main(data_path_train, data_path_test, pipeline_to):

    # Load data
    train_df = pd.read_csv(data_path_train)
    test_df = pd.read_csv(data_path_test)

    # Prepare features and target
    X_train = train_df.drop(columns=['Target'])
    y_train = train_df['Target']
    X_test = test_df.drop(columns=['Target'])
    y_test = test_df['Target']
   
    # Define the preprocessor for scaling numerical features
    numeric_features = ["Previous qualification (grade)", "Admission grade", "Age at enrollment",
                        "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)",
                        "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)",
                        "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)",
                        "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)",
                        "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)",
                        "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)",
                        "Unemployment rate", "Inflation rate", "GDP"]
    
    drop_features = ["Course", "Nacionality", "Gender", "Unemployment rate", 
                     "Inflation rate", "GDP", "Previous qualification", "Mother qualification", 
                     "Mother occupation", "Father qualification", "Father occupation"]
    
    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        ('drop', drop_features)
    )

    # Build the pipeline with KNN classifier
    my_pipeline = make_pipeline(
        preprocessor, 
        KNeighborsClassifier() 
    )

    # Use RandomizedSearchCV to tune hyperparameters
    param_distributions = {
        'kneighborsclassifier__n_neighbors': randint(1, 30)  # Randomized search for n_neighbors
    }

    random_search = RandomizedSearchCV(
        estimator=my_pipeline,
        param_distributions=param_distributions,
        n_iter=50,  
        cv=5,  
        scoring='accuracy', 
        random_state=42, 
        n_jobs=-1  
    )

    # Fit the model with RandomizedSearchCV
    random_search.fit(X_train, y_train)

    # Print the best parameters and score
    print(f"Best parameters: {random_search.best_params_}")
    print(f"Best cross-validation score: {random_search.best_score_}")

    # Save the best pipeline
    best_model = random_search.best_estimator_
    with open(os.path.join(pipeline_to, 'best_knn_pipeline.pickle'), 'wb') as f:
        pickle.dump(best_model, f)

    # Evaluate the best model on the test set
    test_score = best_model.score(X_test, y_test)
    print(f"Test set accuracy: {test_score}")

if __name__ == "__main__":
    main()
