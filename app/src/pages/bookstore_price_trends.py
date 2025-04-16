import streamlit as st
import requests

st.set_page_config(page_title="Price Trends Analysis", layout="wide")
st.title("Price Trends Analysis")
response = requests.get("http://localhost:5000/bookstore/price-trends")
if response.status_code == 200:
    trends = response.json()
    st.dataframe(trends)
else:
    st.error("Error fetching price trends.")

st.markdown("[Back to Bookstore Home](?page=30_Bookstore_Home)")
