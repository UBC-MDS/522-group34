# Academic Success Prediction
- author: Jenson Chang, Jingyuan Wang, Catherine Meng, Siddarth Subrahmanian

Demo of a data analysis project for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About
Here we attempt to build a classification model using the k-nearest neighbours algorithm which can use the information known at the time of student enrollment (academic path, demographics, and social-economic factors) to predict students' dropout and academic sucess.
TODO: add model performance later

## Report
The final report can be found [here](./notebook/academic-success-prediction.ipynb).

## Usage
- First time running the project, running the following from the root of this repository:
    ```
    conda env create --name academic-success-predictor --file environment.yml
    ```
- Activate the conda environment:
    ```
    conda activate academic-success-predictor
    ```
- To run the analysis, run the following from the root of this repository:
    ```
    jupyter lab 
    ```
- Open notebooks/academic-success-prediction.ipynb in Jupyter Lab and under Switch/Select Kernel choose `Python [conda env:academic-success-predictor]`.

- Next, under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Dependencies
- conda (version 24.9.2)
- nb_conda_kernels (version 2.5.1)
- jupyterlab (version 4.2.5)
- python (version 3.12.5) and packages listed in [environment.yml](./environment.yml)

## License
The Academic Success Prediction report contained herein are licensed under the **Creative Commons Attribution 2.5 Canada License** ([CC BY 2.5 CA](https://creativecommons.org/licenses/by/2.5/ca/)). See the [license file](./LICENSE.md) for more information. . If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See the [license file](./LICENSE.md) for more information.

## Reference
