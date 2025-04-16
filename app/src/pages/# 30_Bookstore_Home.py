# 30_Bookstore_Home.py
#test

import streamlit as st

st.set_page_config(page_title="Bookstore Home", layout="wide")
st.title("Bookstore Home - Alfred the Campus Bookstore Manager")
st.write("Welcome, Alfred! Explore textbook trends, price analysis, and demand insights.")

if st.button("Trending Books"):
    st.experimental_set_query_params(page="31_Bookstore_TrendingBooks")
    st.experimental_rerun()
if st.button("Price Trends"):
    st.experimental_set_query_params(page="32_Bookstore_PriceTrends")
    st.experimental_rerun()
if st.button("Seasonal Demand"):
    st.experimental_set_query_params(page="33_Bookstore_SeasonalDemand")
    st.experimental_rerun()

