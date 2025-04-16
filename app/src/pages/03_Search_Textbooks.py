import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="TextbookBazar - Search Textbooks",
    page_icon="📚",
    layout="wide"
)

# Initialize session state if not already done
if 'user_id' not in st.session_state:
    st.switch_page("Home.py")

# Add sidebar navigation
SideBarLinks()

# Main content
st.title("Search Textbooks")

# Create search filters in the sidebar
st.sidebar.markdown("### Filters")

# Example course filter - would come from database in real app
courses = ["", "CS3200", "MATH2341", "BIO1011", "PHYS1151", "ENG1102"]
class_code = st.sidebar.selectbox("Course Code", courses)

# Condition filter
conditions = ["", "new", "like new", "good", "fair", "poor"]
condition = st.sidebar.selectbox("Condition", conditions)

# Price range filter
price_range = st.sidebar.slider("Max Price ($)", 0, 200, 200)

# Apply filters button
filter_applied = st.sidebar.button("Apply Filters", type="primary", use_container_width=True)

# Search bar
search_query = st.text_input("Search by title, author, or ISBN")

# When connected to API
try:
    # In production: 
    # response = requests.get(f'http://api:4000/buyer/textbooks?course={class_code}&condition={condition}&price={price_range}&query={search_query}')
    # books = response.json()
    # 
    # Display results count
    # st.write(f"Found {len(books)} textbooks matching your criteria")
    # 
    # Display books in a nice format
    # for book in books:
    #     col1, col2 = st.columns([1, 3])
    #     
    #     with col1:
    #         # This would be an actual book cover image
    #         st.markdown("📚")
    #     
    #     with col2:
    #         st.markdown(f"### {book['title']}")
    #         st.markdown(f"**Author:** {book['author']}")
    #         st.markdown(f"**ISBN:** {book['isbn']}")
    #         st.markdown(f"**Course:** {book['class_code']}")
    #         st.markdown(f"**Condition:** {book['condition']}")
    #         st.markdown(f"**Price:** ${book['price']:.2f}")
    #         st.markdown(f"**Seller:** {book['seller_name']} (Rating: {book['seller_rating']}/5)")
    #         
    #         col2_1, col2_2, col2_3 = st.columns(3)
    #         with col2_1:
    #             st.button(f"Add to Wishlist", key=f"wish_{book['book_id']}")
    #         with col2_2:
    #             st.button(f"Message Seller", key=f"msg_{book['book_id']}")
    #         with col2_3:
    #             st.button(f"Set Price Alert", key=f"alert_{book['book_id']}")
    #         
    #     st.divider()
    
    # Placeholder for when no API connection
    st.info("Connect to the API to search for textbooks.")
    
    # Example of what a book listing would look like
    if filter_applied or search_query:
        st.markdown("### Example Book Listing")
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown("📚")
        
        with col2:
            st.markdown(f"### Sample Textbook Title")
            st.markdown(f"**Author:** Sample Author")
            st.markdown(f"**ISBN:** 978-XXXXXXXXXX")
            st.markdown(f"**Course:** CS3200")
            st.markdown(f"**Condition:** like new")
            st.markdown(f"**Price:** $45.99")
            st.markdown(f"**Seller:** Sample Seller (Rating: 4.8/5)")
            
            col2_1, col2_2, col2_3 = st.columns(3)
            with col2_1:
                st.button(f"Add to Wishlist", key=f"wish_sample")
            with col2_2:
                st.button(f"Message Seller", key=f"msg_sample")
            with col2_3:
                st.button(f"Set Price Alert", key=f"alert_sample")

except Exception as e:
    st.error(f"Error retrieving textbooks: {str(e)}")
    st.write("Please try again later or contact support if the problem persists.")

# Footer
st.markdown("---")
st.markdown("© 2025 TextbookBazar - The Smart Way to Buy and Sell Textbooks")
