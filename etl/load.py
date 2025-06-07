import pandas as pd
import sqlite3
import os

def save_to_csv(df, file_path=r"Project\Global_Tech_Talent_Dashboard\data\cleaned_jobs.csv"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ Data successfully saved to {file_path}")

def save_to_sqlite(df, db_path=r"Project\Global_Tech_Talent_Dashboard\data\jobs.db", table_name="jobs"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Data successfully saved to SQLite database at {db_path}")
