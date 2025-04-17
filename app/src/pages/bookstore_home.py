import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Bookstore Home", layout="wide")
st.title("Bookstore Home - Alfred the Campus Bookstore Manager")
st.write("Welcome, Alfred! Explore textbook trends, price analysis, and demand insights.")

# Add sidebar
SideBarLinks(show_home=True)

if st.button("Trending Books"):
    st.switch_page("pages/bookstore_trending_books.py")

if st.button("Price Trends"):
    st.switch_page("pages/bookstore_price_trends.py")

if st.button("Seasonal Demand"):
    st.switch_page("pages/bookstore_seasonal_demand.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")