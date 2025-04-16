import streamlit as st
import requests

st.set_page_config(page_title="System Logs", layout="wide")
st.title("System Logs")
response = requests.get("http://localhost:4000/a/logs")
if response.status_code == 200:
    logs = response.json()
    st.dataframe(logs)
else:
    st.error("Error fetching system logs.")

st.markdown("[Back to Admin Home](?page=Admin_Home)")
