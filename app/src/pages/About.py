import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="About Book Bazar", layout="wide")
st.title("About Book Bazar")

# Add sidebar
SideBarLinks(show_home=True)

st.markdown("""
# Book Bazar: The Campus Textbook Marketplace

## Our Mission
Book Bazar is a peer-to-peer textbook marketplace designed specifically for college students. Our mission is to make textbooks more affordable and accessible by connecting buyers and sellers directly within the campus community.

## How It Works
- **For Buyers**: Find textbooks at lower prices than the campus bookstore. Set price alerts and wishlist items to be notified when books you need become available.
  
- **For Sellers**: List your used textbooks easily and get price recommendations based on market data. Earn more than bookstore buyback programs.

- **For Administrators**: Monitor the platform for appropriate use and ensure a safe marketplace for all users.

- **For Bookstore Managers**: Gain insights into student textbook needs and trends to optimize inventory and pricing strategies.

## Our Story
Book Bazar was created by a team of students who were frustrated with the high cost of textbooks and the low buyback values offered by campus bookstores. We built this platform to create a more fair and efficient marketplace for the campus community.

## Contact Us
For support or questions, please email support@bookbazar.edu

""")

if st.button("Return to Home"):
    st.switch_page("Home.py")