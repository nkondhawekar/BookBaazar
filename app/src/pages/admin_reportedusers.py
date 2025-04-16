import streamlit as st
import requests

st.set_page_config(page_title="Reported Users Dashboard", layout="wide")
st.title("Reported Users Dashboard")
response = requests.get("http://localhost:4000/a/reports/dashboard")
if response.status_code == 200:
    reports = response.json()
    st.dataframe(reports)
else:
    st.error("Error fetching reported users.")

st.markdown("[Back to Admin Home](?page=Admin_Home)")
