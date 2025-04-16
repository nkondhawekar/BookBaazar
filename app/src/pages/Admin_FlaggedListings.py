import streamlit as st
import requests

st.set_page_config(page_title="Flagged Listings Review", layout="wide")
st.title("Flagged Listings Review")
response = requests.get("http://localhost:4000/a/flagged-listings")
if response.status_code == 200:
    listings = response.json()
    st.dataframe(listings)
else:
    st.error("Error fetching flagged listings.")

st.markdown("[Back to Admin Home](?page=Admin_Home)")
