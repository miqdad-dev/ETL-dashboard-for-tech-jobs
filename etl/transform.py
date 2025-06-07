from etl.helpers import clean_html, average_salary, normalize_title, classify_role
import numpy as np

def clean_job_data(df):
    df['Min Salary'] = df['Min Salary'].fillna(0).astype(float)
    df['Max Salary'] = df['Max Salary'].fillna(0).astype(float)

    # Apply transformations
    df['Avg Salary'] = df.apply(average_salary, axis=1)
    df['Description'] = df['Description'].apply(clean_html)
    df['Job Title'] = df['Job Title'].apply(normalize_title)
    df['Role'] = df['Job Title'].apply(classify_role)

    df['Location'] = df['Location'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)


    # Drop duplicates
    df.drop_duplicates(subset=["Job Title", "Description"], inplace=True)
    return df

def convert_salaries(df):
    """Simulate salary conversion if needed"""
    # Example logic: Convert from GBP to USD (rate = 1.25)
    if 'currency' in df.columns and 'average_salary' in df.columns:
        df['salary_usd'] = df.apply(lambda row: row['average_salary'] * 1.25 if row['currency'] == 'GBP' else row['average_salary'], axis=1)
    else:
        df['salary_usd'] = df['Avg Salary']
    return df