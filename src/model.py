import os
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from scipy.stats import randint

def load_data(train_path, test_path):
	"""
	Loads training and testing data from specified CSV file paths and separates features and target.

	Parameters:
	train_path (str): Path to the CSV file containing training data.
	test_path (str): Path to the CSV file containing testing data.

	Returns:
	tuple: A tuple containing:
        - X_train (pandas.DataFrame): Features of the training data.
        - y_train (pandas.Series): Target column of the training data.
        - X_test (pandas.DataFrame): Features of the testing data.
        - y_test (pandas.Series): Target column of the testing data.
	"""
    
	train_df = pd.read_csv(train_path)
	test_df = pd.read_csv(test_path)
    
	X_train = train_df.drop(columns=['Target'])
	y_train = train_df['Target']
	X_test = test_df.drop(columns=['Target'])
	y_test = test_df['Target']
    
	return X_train, y_train, X_test, y_test

def build_preprocessor():
	"""
	Builds and returns a column transformer for preprocessing data, which scales numeric features 
	and drops specified non-numeric or irrelevant features.

	Numeric features are standardized using StandardScaler, while certain categorical or redundant 
	features are dropped.

	Returns:
	sklearn.compose.ColumnTransformer: A preprocessor configured with:
        - StandardScaler for specified numeric features.
        - 'drop' for specified features that are not needed.
	"""
	numeric_features = [
        "Previous qualification (grade)", "Admission grade", "Age at enrollment",
        "Curricular units 1st sem (credited)", "Curricular units 1st sem (enrolled)",
        "Curricular units 1st sem (evaluations)", "Curricular units 1st sem (approved)",
        "Curricular units 1st sem (grade)", "Curricular units 1st sem (without evaluations)",
        "Curricular units 2nd sem (credited)", "Curricular units 2nd sem (enrolled)",
        "Curricular units 2nd sem (evaluations)", "Curricular units 2nd sem (approved)",
        "Curricular units 2nd sem (grade)", "Curricular units 2nd sem (without evaluations)",
        "Unemployment rate", "Inflation rate", "GDP"
    ]
    
	drop_features = [
        "Course", "Nacionality", "Gender", "Unemployment rate", 
        "Inflation rate", "GDP", "Previous qualification", "Mother qualification", 
        "Mother occupation", "Father qualification", "Father occupation"
    ]
    
	preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        ('drop', drop_features)
    )
    
	return preprocessor

def build_pipeline(preprocessor):
    """
    Build and return a machine learning pipeline for a KNN classifier.
    
    Parameters:
    preprocessor : sklearn.compose.ColumnTransformer or similar
        A preprocessor object that will be applied to the data before the KNN classifier. 
    
    Returns:
    pipeline : sklearn.pipeline.Pipeline
        A pipeline object that first applies the preprocessing step(s) and then fits the KNN classifier 
    
    Example:
    >>> from sklearn.preprocessing import StandardScaler
    >>> preprocessor = StandardScaler()
    >>> p
    """
    return make_pipeline(
        preprocessor,
        KNeighborsClassifier()
    )

def perform_random_search(X_train, y_train, pipeline):
    """
    Perform RandomizedSearchCV to tune hyperparameters for a KNN classifier pipeline.

    Parameters:
    X_train : array-like, shape (n_samples, n_features)
        The training data used to fit the model.
        
    y_train : array-like, shape (n_samples,)
        The target labels corresponding to the training data.
        
    pipeline : sklearn.pipeline.Pipeline
        The machine learning pipeline that includes preprocessing steps and a KNeighborsClassifier.
    
    Returns:
    random_search : sklearn.model_selection.RandomizedSearchCV
        The RandomizedSearchCV object fitted to the data, containing the best hyperparameters and model.

    Example:
    >>> from sklearn.preprocessing import StandardScaler
    >>> from sklearn.pipeline import make_pipeline
    >>> from sklearn.neighbors import KNeighborsClassifier
    >>> preprocessor = StandardScaler()
    >>> pipeline = make_pipeline(preprocessor, KNeighborsClassifier())
    >>> random_search = perform_random_search(X_train, y_train, pipeline)
    >>> print(random_search.best_params_)
    """
    param_distributions = {
        'kneighborsclassifier__n_neighbors': randint(1, 30)
    }

    random_search = RandomizedSearchCV(
        estimator=pipeline,
        param_distributions=param_distributions,
        n_iter=50,
        cv=5,
        scoring='accuracy',
        random_state=42,
        n_jobs=-1
    )
    
    random_search.fit(X_train, y_train)
    
    return random_search

def save_best_model(best_model, pipeline_to):

    """
    Save the best model pipeline to the specified path.
    
    This function serializes and saves the given `best_model` (e.g., the best model 
    obtained from RandomizedSearchCV) to a file in the specified directory. The 
    model is saved in a pickle file format.

    Parameters:
    best_model : sklearn.pipeline.Pipeline or similar
        The trained pipeline model (including preprocessing steps and the estimator) to be saved.
        
    pipeline_to : str
        The directory path where the model will be saved. The model will be stored as 
        'best_knn_pipeline.pickle' in this directory.
    
    Returns:
    None
    
    Example:
    >>> save_best_model(random_search.best_estimator_, './models')
    """
    with open(os.path.join(pipeline_to, 'best_knn_pipeline.pickle'), 'wb') as f:
        pickle.dump(best_model, f)

def evaluate_model(best_model, X_test, y_test):
    """
    Evaluate the model on the test data.
    
    This function evaluates the performance of the provided model on the test dataset 
    by calculating the accuracy score, which is the proportion of correctly predicted labels.

    Parameters:
    best_model : sklearn.pipeline.Pipeline or estimator
        The trained model (e.g., the best model obtained from RandomizedSearchCV) to be evaluated.
        
    X_test : array-like, shape (n_samples, n_features)
        The test data used to evaluate the model's performance.
        
    y_test : array-like, shape (n_samples,)
        The true labels for the test data.

    Returns:
    float
        The accuracy score of the model on the test data.

    Example:
    >>> accuracy = evaluate_model(best_model, X_test, y_test)
    >>> print(f"Model Accuracy: {accuracy}")
    """
    return best_model.score(X_test, y_test)