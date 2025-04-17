import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Admin Home", layout="wide")
st.title("Admin Home - Rachel the Administrator")
st.write("Welcome, Rachel! Monitor reports, review flagged listings, and check system logs.")

# Add sidebar
SideBarLinks(show_home=True)

if st.button("Reported Users Dashboard"):
    st.switch_page("pages/Admin_ReportedUsers.py")

if st.button("Flagged Listings Review"):
    st.switch_page("pages/Admin_FlaggedListings.py")

if st.button("System Logs"):
    st.switch_page("pages/Admin_SystemLogs.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")