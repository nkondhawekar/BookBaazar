import streamlit as st
import requests

st.set_page_config(page_title="Trending Books Dashboard", layout="wide")
st.title("Trending Books Dashboard")
response = requests.get("http://localhost:5000/bookstore/trending-books")
if response.status_code == 200:
    trending = response.json()
    st.dataframe(trending)
else:
    st.error("Error fetching trending books.")

st.markdown("[Back to Bookstore Home](?page=30_Bookstore_Home)")
