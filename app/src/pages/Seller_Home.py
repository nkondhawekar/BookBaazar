import streamlit as st

st.set_page_config(page_title="Seller Home", layout="wide")
st.title("Seller Home - Adam the Graduating Senior")
st.write("Welcome, Adam! Manage your listings and get insights to help sell your textbooks.")

if st.button("My Listings"):
    st.experimental_set_query_params(page="Seller_MyListings")
    st.experimental_rerun()
if st.button("Price Recommendation"):
    st.experimental_set_query_params(page="Seller_PriceRecommendation")
    st.experimental_rerun()
if st.button("Update Listing Status"):
    st.experimental_set_query_params(page="Seller_UpdateListing")
    st.experimental_rerun()
