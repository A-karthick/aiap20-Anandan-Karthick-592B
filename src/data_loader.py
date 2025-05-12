# src/data_loader.py

import pandas as pd
import sqlite3
import os

def load_data(db_path='data/bmarket.db', table_name='bank_marketing'):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at {db_path}")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()

    # Clean 'Age' column
    if df['Age'].dtype == 'object':
        df['Age'] = df['Age'].str.extract(r'(\d+)').astype(float)

    return df
