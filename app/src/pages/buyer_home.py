import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Buyer Home", layout="wide")
st.title("Buyer Home - Jenna the Freshman")
st.write("Welcome, Jenna! Choose a feature to explore:")

# Add sidebar
SideBarLinks(show_home=True)

if st.button("Textbook Search"):
    st.switch_page("pages/buyer_textbook_search.py")

if st.button("My Price Alerts"):
    st.switch_page("pages/buyer_price_alert.py")

if st.button("My Wishlist"):
    st.switch_page("pages/buyer_wishlist.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")