import streamlit as st
import requests

st.set_page_config(page_title="My Wishlist", layout="wide")
st.title("My Wishlist")
st.write("View and manage your wishlist items.")

# Fetch and display wishlist items for user 1
response = requests.get("http://localhost:4000/b/wishlist")
if response.status_code == 200:
    items = response.json()
    st.dataframe(items)
else:
    st.error("Error fetching wishlist.")

st.markdown("### Add a Book to Your Wishlist")
with st.form("wishlist_add_form"):
    book_id = st.text_input("Book ID to Add")
    add_submit = st.form_submit_button("Add to Wishlist")
    if add_submit:
        payload = {"userId": 1, "bookId": book_id}
        r = requests.post("http://localhost:4000/b/wishlist", json=payload)
        if r.status_code == 201:
            st.success("Book added!")
        else:
            st.error("Failed to add book.")

st.markdown("### Remove a Book from Your Wishlist")
with st.form("wishlist_remove_form"):
    remove_book_id = st.text_input("Book ID to Remove")
    remove_submit = st.form_submit_button("Remove from Wishlist")
    if remove_submit:
        payload = {"userId": 1}
        r = requests.delete(f"http://localhost:4000/b/wishlist/{remove_book_id}", json=payload)
        if r.status_code == 200:
            st.success("Book removed!")
        else:
            st.error("Failed to remove book.")

st.markdown("[Back to Buyer Home](?page=buyer_home)")
