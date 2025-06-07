import streamlit as st
import pandas as pd
from visuals.visuals import salary_distribution, job_count_by_location, average_salary_by_role

# Streamlit page config
st.set_page_config(page_title="Global Tech Talent Dashboard", layout="wide")

# Custom style
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    h1, h2 { color: #2C3E50; }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 Global Tech Talent Dashboard")
st.caption("Built by Miqdad Issa — Powered by Python, Pandas, and Streamlit")

# Data loading
df = pd.read_csv("/data/cleaned_jobs.csv")

# Data preview toggle
with st.expander("🔍 Preview Raw Data"):
    st.dataframe(df.head(30))

# Column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Salary Distribution")
    salary_distribution(df)

with col2:
    st.subheader("🌎 Job Count by Location")
    job_count_by_location(df)

st.subheader("💼 Average Salary by Role")
average_salary_by_role(df)

st.success("Dashboard ready. Explore, learn, and grow! 🚀")
