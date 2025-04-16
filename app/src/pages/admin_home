import streamlit as st

st.set_page_config(page_title="Admin Home", layout="wide")
st.title("Admin Home - Rachel the Administrator")
st.write("Welcome, Rachel! Monitor reports, review flagged listings, and check system logs.")

if st.button("Reported Users Dashboard"):
    st.experimental_set_query_params(page="21_Admin_ReportedUsers")
    st.experimental_rerun()
if st.button("Flagged Listings Review"):
    st.experimental_set_query_params(page="22_Admin_FlaggedListings")
    st.experimental_rerun()
if st.button("System Logs"):
    st.experimental_set_query_params(page="23_Admin_SystemLogs")
    st.experimental_rerun()
