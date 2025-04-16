import streamlit as st

st.set_page_config(page_title="Buyer Home", layout="wide")
st.title("Buyer Home - Jenna the Freshman")
st.write("Welcome, Jenna! Choose a feature to explore:")

if st.button("Textbook Search"):
    st.experimental_set_query_params(page="buyer_textbook_search")
    st.experimental_rerun()

if st.button("My Price Alerts"):
    st.experimental_set_query_params(page="buyer_price_alert")
    st.experimental_rerun()

if st.button("My Wishlist"):
    st.experimental_set_query_params(page="buyer_wishlist")
    st.experimental_rerun()
