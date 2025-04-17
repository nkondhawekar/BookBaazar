
import streamlit as st
from modules.nav import SideBarLinks

# Configure the Streamlit page
st.set_page_config(page_title="Book Bazar", layout="wide")
st.title("Welcome to Book Bazar")
st.write("Select a persona to simulate login and explore the marketplace:")

# Initialize session state if not exists
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Call SideBarLinks - this will show appropriate links if user is authenticated
SideBarLinks(show_home=False)

# Only show persona buttons if not authenticated
if not st.session_state.get('authenticated', False):
    if st.button("Buyer (Jenna the Freshman)", use_container_width=True):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "buyer"
        st.switch_page("pages/buyer_home.py")

    if st.button("Seller (Adam the Graduating Senior)", use_container_width=True):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "seller"
        st.switch_page("pages/Seller_Home.py")

    if st.button("Administrator (Rachel)", use_container_width=True):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "administrator"
        st.switch_page("pages/Admin_Home.py")

    if st.button("Bookstore Manager (Alfred)", use_container_width=True):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "bookstore_manager"
        st.switch_page("pages/bookstore_home.py")
else:
    # If already authenticated, show welcome back message and relevant links
    role = st.session_state.get("role", "")
    if role == "buyer":
        st.write("Welcome back, Jenna! Continue to your dashboard:")
        if st.button("Go to Buyer Home", use_container_width=True):
            st.switch_page("pages/buyer_home.py")
    elif role == "seller":
        st.write("Welcome back, Adam! Continue to your dashboard:")
        if st.button("Go to Seller Home", use_container_width=True):
            st.switch_page("pages/Seller_Home.py")
    elif role == "administrator":
        st.write("Welcome back, Rachel! Continue to your dashboard:")
        if st.button("Go to Admin Home", use_container_width=True):
            st.switch_page("pages/Admin_Home.py")
    elif role == "bookstore_manager":
        st.write("Welcome back, Alfred! Continue to your dashboard:")
        if st.button("Go to Bookstore Home", use_container_width=True):
            st.switch_page("pages/bookstore_home.py")
    
    # Add a logout button in the main content area
    if st.button("Logout", use_container_width=True):
        for key in ("authenticated", "role"):
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()