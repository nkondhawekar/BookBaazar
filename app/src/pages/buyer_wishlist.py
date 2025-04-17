import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="My Wishlist", layout="wide")
st.title("My Wishlist")
st.write("View and manage your wishlist items.")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    # Fetch and display wishlist items for user 1
    response = requests.get("http://web-api:4000/b/wishlist", timeout=5)
    if response.status_code == 200:
        items = response.json()
        st.dataframe(items)
    else:
        st.error(f"Error fetching wishlist. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

st.markdown("### Add a Book to Your Wishlist")
with st.form("wishlist_add_form"):
    book_id = st.text_input("Book ID to Add")
    add_submit = st.form_submit_button("Add to Wishlist")
    if add_submit:
        try:
            payload = {"userId": 1, "bookId": book_id}
            r = requests.post("http://web-api:4000/b/wishlist", json=payload, timeout=5)
            if r.status_code == 201:
                st.success("Book added!")
            else:
                st.error(f"Failed to add book. Status code: {r.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown("### Remove a Book from Your Wishlist")
with st.form("wishlist_remove_form"):
    remove_book_id = st.text_input("Book ID to Remove")
    remove_submit = st.form_submit_button("Remove from Wishlist")
    if remove_submit:
        try:
            payload = {"userId": 1}
            r = requests.delete(f"http://api:4000/b/wishlist/{remove_book_id}", json=payload, timeout=5)
            if r.status_code == 200:
                st.success("Book removed!")
            else:
                st.error(f"Failed to remove book. Status code: {r.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if st.button("Back to Buyer Home"):
    st.switch_page("pages/buyer_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")