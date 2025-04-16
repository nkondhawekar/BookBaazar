# app/src/Home.py

import streamlit as st
from modules.nav import SideBarLinks

# Configure the Streamlit page
st.set_page_config(page_title="Book Bazar", layout="wide")
st.title("Welcome to Book Bazar")
st.write("Select a persona to simulate login and explore the marketplace:")

# Initialize sidebar links (no Home link on the landing page)
SideBarLinks(show_home=False)

# Persona buttons in the main content area
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Buyer (Jenna the Freshman)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "buyer"
        st.experimental_set_query_params(page="00_Buyer_Home")
        st.experimental_rerun()

with col2:
    if st.button("Seller (Adam the Graduating Senior)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "seller"
        st.experimental_set_query_params(page="10_Seller_Home")
        st.experimental_rerun()

with col3:
    if st.button("Administrator (Rachel)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "administrator"
        st.experimental_set_query_params(page="20_Admin_Home")
        st.experimental_rerun()

with col4:
    if st.button("Bookstore Manager (Alfred)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "bookstore_manager"
        st.experimental_set_query_params(page="30_Bookstore_Home")
        st.experimental_rerun()

