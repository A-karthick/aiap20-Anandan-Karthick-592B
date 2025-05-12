# src/preprocess.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Drop rows with missing values (optional: you can also fillna)
    df = df.dropna()

    # Drop Client ID (not useful for prediction)
    df = df.drop(columns=['Client ID'])

    # Standardize target column
    df['Subscription Status'] = df['Subscription Status'].map({'yes': 1, 'no': 0})

    # Encode categorical columns
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Split features and target
    X = df.drop(columns=['Subscription Status'])
    y = df['Subscription Status']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
