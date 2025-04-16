import streamlit as st
import requests

st.set_page_config(page_title="Update Listing Status", layout="wide")
st.title("Update Listing Status")
st.write("Update the status of one of your listings (e.g., mark as sold).")

with st.form("update_listing_form"):
    listing_id = st.text_input("Listing ID")
    new_status = st.selectbox("New Status", ["sold", "removed", "available"])
    submit_update = st.form_submit_button("Update Listing")
    if submit_update:
        payload = {"status": new_status}
        r = requests.put(f"http://localhost:4000/s/listings/{listing_id}", json=payload)
        if r.status_code == 200:
            st.success("Listing status updated!")
        else:
            st.error("Failed to update listing status.")

st.markdown("[Back to Seller Home](?page=Seller_Home)")
