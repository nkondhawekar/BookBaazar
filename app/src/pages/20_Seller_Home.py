import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="TextbookBazar - Seller Dashboard",
    page_icon="📚",
    layout="wide"
)

# Initialize session state if not already done
if 'user_id' not in st.session_state:
    st.switch_page("Home.py")

# Add sidebar navigation
SideBarLinks()

# Main content
st.title(f"Welcome Seller, {st.session_state['name']}")

st.markdown("## What would you like to do today?")

# Create two columns for better button layout
col1, col2 = st.columns(2)

with col1:
    if st.button("Manage My Listings", 
                type="primary",
                use_container_width=True):
        st.switch_page("pages/07_Seller_Listings.py")
    
    if st.button("Check Seller Analytics", 
                type="primary",
                use_container_width=True):
        st.switch_page("pages/10_Seller_Analytics.py")

with col2:
    if st.button("Create New Listing", 
                type="primary",
                use_container_width=True):
        st.switch_page("pages/08_Create_Listing.py")
    
    if st.button("View Messages", 
                type="primary",
                use_container_width=True):
        st.switch_page("pages/09_Seller_Messages.py")

# Dashboard metrics
st.markdown("## Dashboard")

# Create metrics in a row
col1, col2, col3, col4 = st.columns(4)

try:
    # In production, these would come from API calls:
    # response = requests.get(f'http://api:4000/seller/dashboard?sellerId={st.session_state["user_id"]}')
    # dashboard = response.json()
    # 
    # with col1:
    #     st.metric(label="Active Listings", value=dashboard['active_listings'])
    # 
    # with col2:
    #     st.metric(label="Books Sold", value=dashboard['books_sold'])
    # 
    # with col3:
    #     st.metric(label="Your Rating", value=f"{dashboard['rating']}/5.0")
    # 
    # with col4:
    #     st.metric(label="Unread Messages", value=dashboard['unread_messages'])
    
    # Placeholder metrics for UI demonstration
    with col1:
        st.metric(label="Active Listings", value="0")
    
    with col2:
        st.metric(label="Books Sold", value="0")
    
    with col3:
        st.metric(label="Your Rating", value="0/5.0")
    
    with col4:
        st.metric(label="Unread Messages", value="0")
    
    # Recent activity
    st.markdown("## Recent Activity")
    
    # Placeholder for when no API connection
    st.info("Connect to the API to view your recent activity.")
    
except Exception as e:
    st.error(f"Error retrieving dashboard data: {str(e)}")
    st.write("Please try again later or contact support if the problem persists.")

# Footer
st.markdown("---")
st.markdown("© 2025 TextbookBazar - The Smart Way to Buy and Sell Textbooks")

