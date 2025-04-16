import logging
logger = logging.getLogger(__name__)
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TextbookBazar",
    page_icon="📚",
    layout="wide"
)

# Add logo
st.sidebar.image("assets/logo.png", width=150)

# Add home and about links to sidebar
st.sidebar.page_link("Home.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/30_About.py", label="About", icon="📚")

# Title and welcome message
st.title("📚 TextbookBazar")
st.header("CS 3200 Sample Semester Project App")

# User selection
st.markdown("## Hi! As which user would you like to log in?")

# Create buttons for each persona
if st.button("Act as Jenna, a Freshman Buyer", 
            use_container_width=True,
            type="primary"):
    # Store user info in session state
    st.session_state['user_id'] = 1
    st.session_state['name'] = "Jenna"
    st.session_state['role'] = "buyer"
    st.session_state['year'] = "Freshman"
    st.switch_page("pages/01_Buyer_Home.py")

if st.button("Act as Adam, a Graduating Senior Buyer", 
            use_container_width=True,
            type="primary"):
    # Store user info in session state
    st.session_state['user_id'] = 3
    st.session_state['name'] = "Adam"
    st.session_state['role'] = "buyer"
    st.session_state['year'] = "Senior"
    st.switch_page("pages/01_Buyer_Home.py")

if st.button("Act as Michael, a Seller", 
            use_container_width=True,
            type="primary"):
    # Store user info in session state
    st.session_state['user_id'] = 2
    st.session_state['name'] = "Michael"
    st.session_state['role'] = "seller"
    st.session_state['year'] = "Junior"
    st.switch_page("pages/06_Seller_Home.py")

if st.button("Act as System Administrator", 
            use_container_width=True,
            type="primary"):
    # Store user info in session state
    st.session_state['user_id'] = 4
    st.session_state['name'] = "Admin"
    st.session_state['role'] = "admin"
    st.switch_page("pages/09_Admin_Home.py")

if st.button("Act as Bookstore Manager", 
            use_container_width=True,
            type="primary"):
    # Store user info in session state
    st.session_state['user_id'] = 5
    st.session_state['name'] = "Manager"
    st.session_state['role'] = "bookstore_manager"
    st.switch_page("pages/13_Manager_Home.py")

# Footer
st.markdown("---")
st.markdown("© 2025 TextbookBazar - The Smart Way to Buy and Sell Textbooks")
