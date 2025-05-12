# src/main.py

from data_loader import load_data
from preprocess import preprocess_data
from models import run_all_models
import pandas as pd

def main():
    print("Loading data...")
    df = load_data()

    print("Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("Training and evaluating models...")
    results = run_all_models(X_train, X_test, y_train, y_test)

    print("\nEvaluation Results:")
    results_df = pd.DataFrame(results)
    print(results_df)

    # Save results to CSV (optional)
    results_df.to_csv('model_results.csv', index=False)

if __name__ == '__main__':
    main()
