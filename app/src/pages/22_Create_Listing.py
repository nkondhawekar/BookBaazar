import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Page configuration
st.set_page_config(
    page_title="TextbookBazar - Create Listing",
    page_icon="📚",
    layout="wide"
)

# Initialize session state if not already done
if 'user_id' not in st.session_state:
    st.switch_page("00_Home.py")

# Add sidebar navigation
try:
    SideBarLinks()
except:
    # Simple sidebar navigation if module not available
    with st.sidebar:
        st.title("TextbookBazar")
        st.markdown(f"### Seller: {st.session_state['name']}")
        
        st.markdown("### Navigation")
        if st.button("Home", use_container_width=True):
            st.switch_page("pages/06_Seller_Home.py")
        if st.button("My Listings", use_container_width=True):
            st.switch_page("pages/07_Seller_Listings.py")
        if st.button("Messages", use_container_width=True):
            st.switch_page("pages/09_Seller_Messages.py")
        
        if st.button("Logout", use_container_width=True):
            # Clear session state and return to home
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.switch_page("00_Home.py")

# Main content
st.title("Create New Listing")
st.write("List your textbook for sale on the marketplace.")

# Check if we're relisting a similar book
relist_data = st.session_state.get('relist_book', {})

# Create a form for the listing
with st.form("listing_form"):
    # Two columns for form layout
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("Book Title", value=relist_data.get('title', ''))
        author = st.text_input("Author(s)", value=relist_data.get('author', ''))
        isbn = st.text_input("ISBN", value=relist_data.get('isbn', ''))
        class_code = st.text_input("Course Code (e.g., CS3200)", value=relist_data.get('class_code', ''))
    
    with col2:
        condition = st.selectbox("Condition", 
                               options=["new", "like new", "good", "fair", "poor"],
                               format_func=lambda x: {
                                   "new": "New - Never used",
                                   "like new": "Like New - No marks or damage",
                                   "good": "Good - Minor wear, no writing",
                                   "fair": "Fair - Some wear, may have highlighting",
                                   "poor": "Poor - Significant wear, usable"
                               }.get(x, x))
        price = st.number_input("Price ($)", min_value=1.0, max_value=500.0, value=30.0, step=0.50)
        description = st.text_area("Description", 
                                 placeholder="Describe the condition, any highlights or notes, and why this book would be useful for the course...")
        upload_image = st.file_uploader("Upload Book Image (optional)", type=["jpg", "jpeg", "png"])
    
    # Additional settings
    st.markdown("### Listing Settings")
    
    col3, col4 = st.columns(2)
    with col3:
        bulk_discount = st.checkbox("Offer bulk discount")
        if bulk_discount:
            discount_quantity = st.number_input("Minimum quantity for discount", min_value=2, value=3)
            discount_percentage = st.number_input("Discount percentage", min_value=5, max_value=50, value=10)
    
    with col4:
        promote_listing = st.checkbox("Promote listing (additional fee applies)")
        if promote_listing:
            promotion_days = st.number_input("Number of days to promote", min_value=1, max_value=30, value=7)
            promotion_cost = promotion_days * 0.50  # $0.50 per day
            st.write(f"Promotion cost: ${promotion_cost:.2f}")
    
    # Submit button
    submitted = st.form_submit_button("Create Listing", type="primary", use_container_width=True)
    
    if submitted:
        # Validate form data
        if not title or not author or not price:
            st.error("Please fill in all required fields: title, author, and price.")
        else:
            # In a real app, we would call the API to create the listing
            try:
                # In production:
                # data = {
                #     "sellerId": st.session_state["user_id"],
                #     "title": title,
                #     "author": author,
                #     "isbn": isbn,
                #     "class_code": class_code,
                #     "condition": condition,
                #     "price": price,
                #     "description": description,
                #     "bulk_discount": bulk_discount,
                #     "discount_quantity": discount_quantity if bulk_discount else None,
                #     "discount_percentage": discount_percentage if bulk_discount else None,
                #     "promote": promote_listing,
                #     "promotion_days": promotion_days if promote_listing else None
                # }
                # response = requests.post('http://api:4000/seller/listings', json=data)
                
                # For demo purposes, just show success
                st.success(f"Your listing for '{title}' has been created successfully!")
                
                # Clear the relist data if it was used
                if 'relist_book' in st.session_state:
                    del st.session_state['relist_book']
                
                # Add a button to view all listings
                if st.button("View My Listings", use_container_width=True):
                    st.switch_page("pages/07_Seller_Listings.py")
            except Exception as e:
                st.error(f"Error creating listing: {str(e)}")
                st.write("Please try again later or contact support if the problem persists.")

# Bulk upload section
st.divider()
st.markdown("### Bulk Upload Listings")
st.write("Have multiple books to sell? Upload them all at once.")

with st.expander("Bulk Upload"):
    st.markdown("""
    1. Download our template CSV file
    2. Fill in the details for each book
    3. Upload the completed file
    """)
    
    # Download template button
    st.download_button(
        label="Download Template CSV",
        data="Title,Author,ISBN,Course Code,Condition,Price,Description\n,,,,,,",
        file_name="textbook_listing_template.csv",
        mime="text/csv"
    )
    
    # Upload CSV file
    bulk_file = st.file_uploader("Upload Completed CSV", type=["csv"])
    
    if bulk_file:
        try:
            # Read the CSV file
            df = pd.read_csv(bulk_file)
            st.write("Preview of your listings:")
            st.dataframe(df)
            
            if st.button("Submit Bulk Listings", type="primary", use_container_width=True):
                # In production:
                # listings = df.to_dict('records')
                # response = requests.post('http://api:4000/seller/listings/bulk-upload', 
                #                         json={"listings": listings, "sellerId": st.session_state["user_id"]})
                
                # For demo purposes, just show success
                st.success(f"Successfully uploaded {len(df)} listings!")
                
                # Add a button to view all listings
                if st.button("View My Listings", key="view_after_bulk", use_container_width=True):
                    st.switch_page("pages/07_Seller_Listings.py")
        except Exception as e:
            st.error(f"Error processing CSV: {str(e)}")
            st.write("Please check your CSV format and try again.")

# Price recommendation
st.divider()
st.markdown("### Get Price Recommendations")
st.write("Not sure how to price your textbook? Get data-driven recommendations based on recent sales.")

isbn_for_recommendation = st.text_input("Enter ISBN for Price Recommendation")
if st.button("Get Recommendation", use_container_width=True):
    if not isbn_for_recommendation:
        st.warning("Please enter an ISBN to get a price recommendation.")
    else:
        # In production:
        # response = requests.get(f'http://api:4000/seller/price-recommendation?isbn={isbn_for_recommendation}')
        # recommendation = response.json()
        
        # For demo purposes, use mock data
        mock_recommendation = {
            "isbn": isbn_for_recommendation,
            "recommended_price": 42.50,
            "market_low": 32.99,
            "market_high": 55.00,
            "avg_time_to_sell": "4 days"
        }
        
        # Display recommendation
        st.info(f"Recommended price: ${mock_recommendation['recommended_price']:.2f}")
        st.write(f"Market range: ${mock_recommendation['market_low']:.2f} - ${mock_recommendation['market_high']:.2f}")
        st.write(f"Average time to sell: {mock_recommendation['avg_time_to_sell']}")

# Footer
st.markdown("---")
st.markdown("© 2025 TextbookBazar - The Smart Way to Buy and Sell Textbooks")

# Add logo to the top of the page