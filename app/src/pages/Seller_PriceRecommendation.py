import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Price Recommendation", layout="wide")
st.title("Price Recommendation")
st.write("Get a suggested price for one of your listings.")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    # For demo, assume listingId = 1
    response = requests.get("http://api:4000/s/price-recommendation/1", timeout=5)
    if response.status_code == 200:
        recommendation = response.json()
        st.write(f"Listing ID: {recommendation['listingId']}")
        st.write(f"Recommended Price: ${recommendation['recommended_price']}")
        st.write(recommendation['message'])
    else:
        st.error(f"Error fetching price recommendation. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

if st.button("Back to Seller Home"):
    st.switch_page("pages/Seller_Home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")