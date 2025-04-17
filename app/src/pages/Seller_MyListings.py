import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="My Listings", layout="wide")
st.title("My Listings")
st.write("View all your current listings.")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    params = {"sellerId": 1}  # For demo, assume sellerId 1
    response = requests.get("http://api:4000/s/listings", params=params, timeout=5)
    
    if response.status_code == 200:
        listings = response.json()
        st.dataframe(listings)
    else:
        st.error(f"Error fetching listings. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Add navigation buttons
if st.button("Back to Seller Home"):
    st.switch_page("pages/Seller_Home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")