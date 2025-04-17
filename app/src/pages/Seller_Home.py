import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Seller Home", layout="wide")
st.title("Seller Home - Adam the Graduating Senior")
st.write("Welcome, Adam! Manage your listings and get insights to help sell your textbooks.")

# Add the sidebar navigation
SideBarLinks(show_home=True)

if st.button("My Listings"):
    st.switch_page("pages/Seller_MyListings.py")

if st.button("Price Recommendation"):
    st.switch_page("pages/Seller_PriceRecommendation.py")

if st.button("Update Listing Status"):
    st.switch_page("pages/Seller_UpdateListing.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")