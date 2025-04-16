import streamlit as st
import requests

st.set_page_config(page_title="My Listings", layout="wide")
st.title("My Listings")
st.write("View all your current listings.")

params = {"sellerId": 1}  # For demo, assume sellerId 1
response = requests.get("http://localhost:4000/s/listings", params=params)
if response.status_code == 200:
    listings = response.json()
    st.dataframe(listings)
else:
    st.error("Error fetching listings.")

st.markdown("[Back to Seller Home](?page=Seller_Home)")
