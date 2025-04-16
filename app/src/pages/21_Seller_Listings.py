import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="TextbookBazar - Seller Listings",
    page_icon="📚",
    layout="wide"
)

# Initialize session state if not already done
if 'user_id' not in st.session_state:
    st.switch_page("Home.py")

# Add sidebar navigation
SideBarLinks()

# Main content
st.title("My Listings")
st.write("Manage your book listings and track their status.")

# Create New Listing button
if st.button("➕ Create New Listing", type="primary"):
    st.switch_page("pages/08_Create_Listing.py")

# Tabs for different listing status
tab1, tab2, tab3 = st.tabs(["Active Listings", "Sold Books", "Removed Listings"])

try:
    # In production: 
    # response = requests.get(f'http://api:4000/seller/listings?sellerId={st.session_state["user_id"]}')
    # all_listings = response.json()
    # 
    # # Filter listings by status
    # active_listings = [listing for listing in all_listings if listing["status"] == "active"]
    # sold_listings = [listing for listing in all_listings if listing["status"] == "sold"]
    # removed_listings = [listing for listing in all_listings if listing["status"] == "removed"]
    
    # Active Listings Tab
    with tab1:
        # Placeholder for when no API connection
        st.info("You don't have any active listings. Click 'Create New Listing' to add one.")
        
        # Example active listing UI (for preview only)
        with st.expander("Example active listing (UI preview)"):
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.markdown("### Sample Textbook")
                st.markdown("**Author:** Sample Author")
                st.markdown("**ISBN:** 978-XXXXXXXXXX")
                st.markdown("**Course:** CS3200")
            
            with col2:
                st.markdown("**Condition:** like new")
                st.markdown("**Price:** $45.99")
                st.markdown("**Listed on:** 2025-04-01")
                st.markdown("**Views:** 24 | **Messages:** 3")
            
            with col3:
                col3_1, col3_2 = st.columns(2)
                with col3_1:
                    st.button("Mark Sold", key="sold_sample")
                
                with col3_2:
                    st.button("Remove", key="remove_sample")
                
                st.button("Edit Price", key="edit_sample")
                st.button("Promote", key="promote_sample")
    
    # Sold Books Tab
    with tab2:
        # Placeholder for when no API connection
        st.info("You haven't sold any books yet.")
        
        # Example sold listing UI (for preview only)
        with st.expander("Example sold listing (UI preview)"):
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.markdown("### Sample Sold Textbook")
                st.markdown("**Author:** Sample Author")
                st.markdown("**ISBN:** 978-XXXXXXXXXX")
                st.markdown("**Course:** CS3200")
            
            with col2:
                st.markdown("**Condition:** like new")
                st.markdown("**Price:** $45.99")
                st.markdown("**Listed on:** 2025-03-15")
                st.markdown("**Sold on:** 2025-04-02")
            
            with col3:
                st.markdown("**Buyer:** John Smith")
                st.markdown("**Views:** 32")
                st.markdown("**Messages:** 5")
                
                st.button("Relist Similar", key="relist_sample")
    
    # Removed Listings Tab
    with tab3:
        # Placeholder for when no API connection
        st.info("You don't have any removed listings.")
        
        # Example removed listing UI (for preview only)
        with st.expander("Example removed listing (UI preview)"):
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.markdown("### Sample Removed Textbook")
                st.markdown("**Author:** Sample Author")
                st.markdown("**ISBN:** 978-XXXXXXXXXX")
                st.markdown("**Course:** CS3200")
            
            with col2:
                st.markdown("**Condition:** poor")
                st.markdown("**Price:** $15.00")
                st.markdown("**Listed on:** 2025-03-10")
                st.markdown("**Removed on:** 2025-04-05")
            
            with col3:
                st.markdown("**Views:** 3")
                st.markdown("**Messages:** 0")
                
                st.button("Reactivate", key="reactivate_sample")

except Exception as e:
    st.error(f"Error retrieving listings: {str(e)}")
    st.write("Please try again later or contact support if the problem persists.")

# Footer
st.markdown("---")
st.markdown("© 2025 TextbookBazar - The Smart Way to Buy and Sell Textbooks")