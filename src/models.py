# src/models.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {
        'Model': model.__class__.__name__,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1 Score': f1_score(y_test, y_pred)
    }

def run_all_models(X_train, X_test, y_train, y_test):
    models = [
        LogisticRegression(max_iter=1000),
        RandomForestClassifier(),
        CatBoostClassifier(verbose=0)
    ]

    results = []
    for model in models:
        result = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)
        results.append(result)

    return results
