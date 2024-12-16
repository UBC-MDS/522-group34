## Milestone 1 Feedback

-   **Feedback:** Missing text for some sections in `CONTRIBUTING.md`

-   **Resolution:** Shortened `CONTRIBUTING.md` and removed missing sections

-   **By:** Jenson Chang

-   **Evidence:** [PR #40](https://github.com/UBC-MDS/academic-success-prediction/pull/40/files)

    —

-   **Feedback:** Need to provide the code that created the data set

-   **Resolution:** Added `scripts/download_data.py` to download original data from source URL

-   **By:** Catherine Meng

-   **Evidence:** [PR #26](https://github.com/UBC-MDS/academic-success-prediction/pull/26/files)

    —

-   **Feedback:** Analysis ends abruptly and does not tie back to original problem

-   **Resolution:** Expand on the results/conclusion and tie it back to the original problem in `report/academic-success-prediction.qmd`

-   **By:** Jenson Chang

-   **Evidence:** [PR #40](https://github.com/UBC-MDS/academic-success-prediction/pull/40/files)

    —

-   **Feedback:** Environment(s) file is too specific to work cross platform

-   **Resolution:** Hand curate new `environment.yml` file

-   **By:** Catherine Meng

-   **Evidence:** [PR #7](https://github.com/UBC-MDS/academic-success-prediction/pull/7/files)

    —

-   **Feedback:** References are not referred to in the narrative

-   **Resolution:** Reference to the references added in `report/academic-success-prediction.qmd`

-   **By:** Cathering Meng

-   **Evidence:** [PR #37](https://github.com/UBC-MDS/academic-success-prediction/pull/37/files), `report/academic-success-prediction.qmd`, Line 49

## Milestone 2 Feedback

-   **Feedback:** `docker-compose.yaml` pulls from latest instead of a specific tag

-   **Resolution:** Manually updating `docker-compose.yaml` with a specific tag whenver a new image is generated

-   **By:** Jenson Chang

-   **Evidence:** [PR #58](https://github.com/UBC-MDS/academic-success-prediction/pull/58/files)

    —

-   **Feedback:** Validate Target Variable Distribution function needs more rigor

-   **Resolution:** Added `validate_distribution.py` to check that the Target classes are within an expected proportion range and throws an exception if it's 2 standard deviations away from expected. 

-   **By:** Jenson Chang

-   **Evidence:** [PR #58](https://github.com/UBC-MDS/academic-success-prediction/pull/58/files), `validate_distribution.py`, Line 110

## Peer Review Feedback

-   **Feedback:** [Abdul-Rahmann's feedback](https://github.com/UBC-MDS/data-analysis-review-2024/issues/11#issuecomment-2530167190): Numbered prefix in script names violates best practices

-   **Resolution:** Fix the name of the python scripts to follow the best naming conventions. E.g. `01_dowload_data.py` -\> `dowload_data.py`

-   **By:** Catherine Meng

-   **Evidence:** [PR #56](https://github.com/UBC-MDS/academic-success-prediction/pull/56)

    —

-   **Feedback:** [Abdul-Rahmann's feedback](https://github.com/UBC-MDS/data-analysis-review-2024/issues/11#issuecomment-2530167190): Some script of giant main functions that could be better broken up.

-   **Resolution:** `scripts/02_data_cleaning_validation.py` now calls 4 custom functions instead of running all logic in main

-   **By:** Jenson Chang

-   **Evidence:** [PR #51](https://github.com/UBC-MDS/academic-success-prediction/pull/51/files), `scripts/02_data_cleaning_validation.py`, Line 38

-   **Resolution:** `scripts/model_classifier.py` now calls 6 custom functions instead of running all logic in main

-   **By:** Jingyuan Wang

-   **Evidence:** [PR #57](https://github.com/UBC-MDS/academic-success-prediction/pull/57/files), `scripts/model_classifier.py`, Line 18

    —

-   **Feedback:** [tianjiao00's feedback](https://github.com/UBC-MDS/data-analysis-review-2024/issues/11#issuecomment-2534180728): File structure and naming could use more clarity


-   **Resolution:** Added a section to README to explain the folder structure

-   **By:** Jenson Chang

-   **Evidence:** [Commit b7a60f3](https://github.com/UBC-MDS/academic-success-prediction/commit/b7a60f3fc8af32e69fc6bf5a217455bf097c45da)
