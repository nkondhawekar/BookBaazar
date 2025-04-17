import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Price Trends Analysis", layout="wide")
st.title("Price Trends Analysis")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    response = requests.get("http://api:4000/m/price-trends", timeout=5)
    if response.status_code == 200:
        trends = response.json()
        st.dataframe(trends)
    else:
        st.error(f"Error fetching price trends. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

if st.button("Back to Bookstore Home"):
    st.switch_page("pages/bookstore_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")