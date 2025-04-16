# app/src/Home.py
import streamlit as st

st.set_page_config(page_title="Textbook Marketplace", layout="wide")

st.title("Welcome to the Textbook Marketplace")

st.markdown("### Simulate login by selecting a user:")

col1, col2, col3, col4 = st.columns(4)

if col1.button("Buyer (Jenna)"):
    st.experimental_set_query_params(page="00_Buyer_Home")
    st.experimental_rerun()

if col2.button("Seller (Adam)"):
    st.experimental_set_query_params(page="10_Seller_Home")
    st.experimental_rerun()

if col3.button("Admin (Rachel)"):
    st.experimental_set_query_params(page="20_Admin_Home")
    st.experimental_rerun()

if col4.button("Bookstore Manager (Alfred)"):
    st.experimental_set_query_params(page="30_Bookstore_Home")
    st.experimental_rerun()

st.markdown("_(You can also change the URL query parameter `page` manually if needed.)_")
