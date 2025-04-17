import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Update Listing Status", layout="wide")
st.title("Update Listing Status")
st.write("Update the status of one of your listings (e.g., mark as sold).")

# Add sidebar
SideBarLinks(show_home=True)

with st.form("update_listing_form"):
    listing_id = st.text_input("Listing ID")
    new_status = st.selectbox("New Status", ["sold", "removed", "available"])
    submit_update = st.form_submit_button("Update Listing")
    if submit_update:
        try:
            payload = {"status": new_status}
            r = requests.put(f"http://api:4000/s/listings/{listing_id}", json=payload, timeout=5)
            if r.status_code == 200:
                st.success("Listing status updated!")
            else:
                st.error(f"Failed to update listing status. Status code: {r.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if st.button("Back to Seller Home"):
    st.switch_page("pages/Seller_Home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")