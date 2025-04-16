import streamlit as st
import requests

st.set_page_config(page_title="Flagged Listings Review", layout="wide")
st.title("Flagged Listings Review")
response = requests.get("http://localhost:5000/admin/flagged-listings")
if response.status_code == 200:
    listings = response.json()
    st.dataframe(listings)
else:
    st.error("Error fetching flagged listings.")

st.markdown("[Back to Admin Home](?page=20_Admin_Home)")
