# 04_model_classifier.py
# author: Jingyuan Wang
# date: 2024-12-06

import click
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.model import load_data, build_preprocessor, build_pipeline, perform_random_search, save_best_model, evaluate_model

@click.command()
@click.option("--data_path_train", type=str, help="Path to the training data")
@click.option("--data_path_test", type=str, help="Path to the test data")
@click.option("--pipeline_to", type=str, help="Path to save the best pipeline")

def main(data_path_train, data_path_test, pipeline_to):

	# Load data
	X_train, y_train, X_test, y_test = load_data(data_path_train, data_path_test)

    # Build the preprocessor
	preprocessor = build_preprocessor()

    # Build the pipeline with KNN classifier
	my_pipeline = build_pipeline(preprocessor)

    # Perform RandomizedSearchCV for hyperparameter tuning
	random_search = perform_random_search(X_train, y_train, my_pipeline)

    # Print the best parameters and score
	print(f"Best parameters: {random_search.best_params_}")
	print(f"Best cross-validation score: {random_search.best_score_}")

    # Save the best pipeline
	best_model = random_search.best_estimator_
	save_best_model(best_model, pipeline_to)

    # Evaluate the best model on the test set
	test_score = evaluate_model(best_model, X_test, y_test)
	print(f"Test set accuracy: {test_score}")

if __name__ == "__main__":
	main()

