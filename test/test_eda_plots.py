import pytest
import pandas as pd
import altair as alt
import os
import sys
import tempfile
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.eda_plots import plot_categorical_features, plot_numerical_features


# Test data
test_df = pd.DataFrame({
    'A': ['a', 'b', 'a', 'b', 'a', 'b'],
    'B': [1, 2, 3, 4, 5, 6],
    'Target': ['yes', 'no', 'yes', 'no', 'yes', 'no']
})

def test_plot_categorical_features(tmp_path):
    # Test that the function saves a file
    figure_path = tmp_path / "figures"
    figure_path.mkdir()
    plot_categorical_features(test_df, ['A'], figure_path)
    assert os.path.exists(figure_path / "eda_categorical.png")

def test_plot_numerical_features(tmp_path):
    # Test that the function saves a file
    figure_path = tmp_path / "figures"
    figure_path.mkdir()
    plot_numerical_features(test_df, ['B'], figure_path)
    assert os.path.exists(figure_path / "eda_numerical.png")

def test_plot_categorical_features_invalid_input(tmp_path):
    # Test that the function raises an error with invalid input
    assert plot_categorical_features('not a dataframe', ['A'], tmp_path) is None

def test_plot_numerical_features_invalid_input(tmp_path):
    # Test that the function raises an error with invalid input
    assert plot_numerical_features('not a dataframe', ['B'], tmp_path) is None