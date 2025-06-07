import json
import requests
import pandas as pd

def extract_adzuna_jobs():
    base_url = "https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=9f8ff6a0&app_key=7aee07938ea0b38724250a96115df9b2&what=software%20engineer&results_per_page=20&content-type=application/json"

    response = requests.get(base_url)
    if response.status_code == 200:
        results = response.json()["results"]
        df = pd.json_normalize(results)
        # Select only the columns you want
        columns_to_keep = ['title', 'salary_min', 'salary_max', 'location.area','description']
        df = df[columns_to_keep].copy()

        # Rename for clarity
        df.rename(columns={
            'title': 'Job Title',
            'salary_min': 'Min Salary',
            'salary_max': 'Max Salary',
            'location.area': 'Location',
            'description': 'Description'
        }, inplace=True)

        # Save and preview
        df.to_csv(r"C:\Users\issam\Desktop\Python\Project\Global_Tech_Talent_Dashboard\data\adzuna_jobs.csv", index=False)
        print("Columns are:", df.columns)
        print("Preview:")
        print(df.head(1).T)
        return df

    else:
        print(f"Error: {response.status_code}")

extract_adzuna_jobs()