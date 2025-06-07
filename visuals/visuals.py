import pandas as pd
import matplotlib.pyplot as plt

def salary_distribution(df):
    plt.figure(figsize=(10, 6))
    df['salary_usd'].hist(bins=30)
    plt.title("Salary Distribution (USD)")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("visuals/salary_distribution.png")
    plt.close()

def job_count_by_location(df):
    plt.figure(figsize=(10, 6))
    df['Location'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 Job Counts by Location")
    plt.xlabel("Location")
    plt.ylabel("Job Postings")
    plt.tight_layout()
    plt.savefig("visuals/job_count_by_location.png")
    plt.close()

def average_salary_by_role(df):
    plt.figure(figsize=(12, 6))
    df.groupby('Job Title')['salary_usd'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
    plt.title("Top 10 Roles by Average Salary")
    plt.xlabel("Job Title")
    plt.ylabel("Average Salary (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visuals/avg_salary_by_role.png")
    plt.close()
