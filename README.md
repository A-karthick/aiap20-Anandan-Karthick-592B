# Machine Learning Pipeline Project

## Full Name & Email

* **Name**: \[ANANDAN KARTHICK]
* **Email**: \[shivakarthi41@gmail.com]

---

## Project Folder Structure

```
project-folder/
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── models.py
│   └── main.py
├── requirements.txt
├── run.sh
└── README.md
```

---

## Instructions to Run the Pipeline

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:

   ```bash
   bash run.sh
   ```

3. Output will be displayed in the terminal and saved as `model_results.csv`.

---

## Pipeline Flow

1. **Data Loading**: Load data from SQLite (`bmarket.db`).
2. **Preprocessing**:

   * Drop missing values.
   * Drop unnecessary columns (e.g., Client ID).
   * Encode categorical features.
   * Map target column `Subscription Status` (`yes`=1, `no`=0).
3. **Train-Test Split**: 80% train / 20% test, random\_state=42.
4. **Model Training**: Train multiple models.
5. **Evaluation**: Evaluate using Accuracy, Precision, Recall, F1 Score.
6. **Save Results**: Save evaluation results to `model_results.csv`.

---

## EDA Findings & Feature Engineering Summary

| Feature             | Processing Applied                     |
| ------------------- | -------------------------------------- |
| Age                 | Cleaned (extracted number from string) |
| Categorical Columns | Label Encoding                         |
| Target Variable     | Mapped 'yes' to 1, 'no' to 0           |
| Train-Test Split    | 80% Train, 20% Test, random\_state=42  |

* Based on EDA, categorical encoding and target mapping were applied.
* Data imbalance was considered when choosing evaluation metrics.

---

## Models Used

| Model                    | Reason for Choice                                              |
| ------------------------ | -------------------------------------------------------------- |
| Logistic Regression      | Simple, interpretable baseline model.                          |
| Random Forest Classifier | Handles non-linearities, good for feature importance analysis. |
| CatBoost Classifier      | Robust with categorical data, handles overfitting well.        |

---

## Evaluation Metrics

| Metric    | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| Accuracy  | Proportion of correct predictions.                                     |
| Precision | Correct positive predictions out of total positive predictions.        |
| Recall    | Ability to identify all positive cases (sensitive to imbalanced data). |
| F1 Score  | Harmonic mean of Precision and Recall.                                 |

---

## Deployment Considerations

* Can be containerized (Docker) for production.
* Supports CLI automation via `run.sh`.
* Modular codebase for easy model swaps.

---
