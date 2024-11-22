# Academic Success Prediction
- author: Jenson Chang, Jingyuan Wang, Catherine Meng, Siddarth Subrahmanian

Demo of a data analysis project for DSCI 522 (Data Science Workflows); a course in the Master of Data Science program at the University of British Columbia.

## About
Here we attempt to build a classification model using the k-nearest neighbours algorithm which can use the information known at the time of student enrollment (academic path, demographics, and social-economic factors) to predict students' dropout and academic sucess. Our final classifier performed consistently on unseen test data, achieving a cross-validation training score of 0.71, with a similar test score. Although the model's accuracy is moderate, it performs consistently. Given that the data was collected from a single institution, a larger dataset may be necessary to generalize predictions to other institutions or countries. We believe this model is close to supporting dropout prediction for the institution from which the data was collected, though further research to improve performance and better understand characteristics of incorrectly predicted students would still be beneficial.

The data set is created by Mónica Vieira Martins, Jorge Machado, Luís Baptista and Valentim Realinho at the Instituto Politécnico de Portalegre (M.V.Martins, D. Tolledo, J. Machado, L. M.T. Baptista, V.Realinho. 2021). It is sourced from UC Irvine's Machine Learning Repository and can be found here. The data contains demographic, enrollment and academic (1st and 2nd semesters) information on the students. Each row in the data set represents a student record. Using these data, a model would be built to predict the academic outcome of the student. There are 36 columns in total.

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
