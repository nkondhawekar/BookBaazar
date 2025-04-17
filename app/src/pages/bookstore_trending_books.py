import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Trending Books Dashboard", layout="wide")
st.title("Trending Books Dashboard")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    response = requests.get("http://api:4000/m/trending-books", timeout=5)
    if response.status_code == 200:
        trending = response.json()
        st.dataframe(trending)
    else:
        st.error(f"Error fetching trending books. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

if st.button("Back to Bookstore Home"):
    st.switch_page("pages/bookstore_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")