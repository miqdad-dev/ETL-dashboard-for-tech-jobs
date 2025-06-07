# 🌍 Global Tech Talent Dashboard

This project is a complete **ETL (Extract, Transform, Load)** pipeline and dashboard that collects global job data from the Adzuna API, processes and cleans it, stores it in both CSV and SQLite formats, and visualizes key insights using Python.

---

## 📦 Project Structure

```
your-project/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── helpers.py
│
├── visuals/
│   └── visuals.py
|   
│
├── data/
│   ├── adzuna_jobs.csv
│   ├── cleaned_jobs.csv
│   └── jobs.db
│
├── notebooks/
│   └── dashboard_walkthrough.ipynb
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 Features

- 🔍 **Extracts** data from the Adzuna API
- 🧹 **Cleans** and normalizes job data
- 💾 **Saves** data to CSV and SQLite
- 📊 **Visualizes** job trends: salary distribution, job count by country, and role-based salary
- 🧪 **Notebook** for exploration and dashboards

---

## 📂 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/miqdad-dev/Global-Tech-Talent-Dashboard.git
cd Global-Tech-Talent-Dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the ETL pipeline
python main.py

# 4. Open notebook for visual analysis
jupyter notebook notebooks/dashboard_walkthrough.ipynb
```

---

## 📈 Visual Output

- Salary Distribution Histogram ![Salary distribution](image-3.png)
- Job Count by Country Bar Chart![Job in country](image-2.png)
- Average Salary by Role Pie Chart!(image-1.png)


All visuals are saved to the `Project\Global_Tech_Talent_Dashboard\visuals/` folder.

---

## 📌 Technologies Used

- Python 🐍
- Pandas
- Matplotlib
- SQLite
- Jupyter Notebooks

---

## 🙌 Author

Built with passion by [Miqdad Issa](https://github.com/miqdad-dev) — aiming to become the best data and AI engineer in the world 🚀.