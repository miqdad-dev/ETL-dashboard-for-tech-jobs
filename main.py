# main.py
from etl.extract import extract_adzuna_jobs
from etl.transform import clean_job_data, convert_salaries
from etl.load import save_to_csv, save_to_sqlite
from visuals.visuals import salary_distribution, job_count_by_country, average_salary_by_role


def main():
   
    # Extract
    raw_data = extract_adzuna_jobs()
    
    # Transform
    cleaned_data = clean_job_data(raw_data)
    final_data = convert_salaries(cleaned_data)
   

    # Load
    save_to_csv(final_data, file_path=r"Project\Global_Tech_Talent_Dashboard\data\cleaned_jobs.csv")
    save_to_sqlite(final_data, db_path=r"Project\Global_Tech_Talent_Dashboard\data\jobs.db", table_name="jobs")

    salary_distribution(final_data)
    job_count_by_country(final_data)
    average_salary_by_role(final_data)
   

if __name__ == "__main__":
    main()
