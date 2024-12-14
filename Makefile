# Makefile
# Jenson Chang, Jingyuan Wang, Catherine Meng, Siddarth Subrahmanian, Dec 2024

# This script takes no arguments.

# example usage:
# make all
# make clean

all : report/academic-success-prediction.pdf report/academic-success-prediction.html

# Download the data and extract and save as csv file
data/raw/data.csv : scripts/download_data.py
	python scripts/download_data.py \
		--url="http://archive.ics.uci.edu/static/public/697/predict+students+dropout+and+academic+success.zip" \
		--write_to=data/raw

# Check file type, do data cleaning and data validation
data/processed/clean_data.csv data/processed/test_data.csv data/processed/train_data.csv : data/raw/data.csv scripts/data_cleaning_validation.py
	python scripts/data_cleaning_validation.py \
		--file_path="data/raw/data.csv"

# Perform exploratory data analysis and save figures
results/figures/eda_categorical.png results/figures/eda_numerical.png : data/processed/train_data.csv scripts/eda.py
	python scripts/eda.py \
		--data_path="data/processed/train_data.csv" \
		--figure_path="results/figures"

# Run the knn model and export the best one
results/models/best_knn_pipeline.pickle : data/processed/train_data.csv data/processed/test_data.csv scripts/model_classifier.py
	python scripts/model_classifier.py \
		--data_path_train="data/processed/train_data.csv" \
		--data_path_test="data/processed/test_data.csv" \
		--pipeline_to="results/models"

# Write the pdf report
report/academic-success-prediction.pdf: report/academic-success-prediction.qmd results/figures/eda_categorical.png results/figures/eda_numerical.png results/models/best_knn_pipeline.pickle
	quarto render report/academic-success-prediction.qmd --to pdf
# Write the pdf report
report/academic-success-prediction.html : report/academic-success-prediction.qmd results/figures/eda_categorical.png results/figures/eda_numerical.png results/models/best_knn_pipeline.pickle
	quarto render report/academic-success-prediction.qmd --to html

clean :
	rm -f data/raw/data.csv \
		data/processed/clean_data.csv \
		data/processed/test_data.csv \
		data/processed/train_data.csv
	rm -f results/figures/eda_categorical.png \
		results/figures/eda_numerical.png 
	rm -f results/models/best_knn_pipeline.pickle
	rm -f report/academic-success-prediction.pdf
	rm -f report/academic-success-prediction.html