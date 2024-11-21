# Academic Success Prediction
- author: Jenson Chang, Jingyuan Wang, Catherine Meng, Siddarth Subrahmanian

Demo of a data analysis project for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About
Here we attempt to build a classification model using the k-nearest neighbours algorithm which can use the information known at the time of student enrollment (academic path, demographics, and social-economic factors) to predict students' dropout and academic sucess.
TODO: add model performance later

## Report
The final report can be found [here](./notebook/academic-success-prediction.ipynb).

## Usage
First time running the project, running the following from the root of this repository:
```
conda env create --name academic-success-predictor --file environment.yml
```
To run the analysis, run the following from the root of this repository:
```
jupyter lab 
```
Open notebooks/academic-success-prediction.ipynb in Jupyter Lab and under Switch/Select Kernel choose `Python [conda env:academic-success-predictor]`.

Next, under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Dependencies
TODO

## License
TODO

## Reference
