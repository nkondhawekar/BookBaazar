import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Textbook Search", layout="wide")
st.title("Textbook Search")
st.write("Search for textbooks by course code, maximum price, and condition.")

# Add sidebar
SideBarLinks(show_home=True)

with st.form("search_form"):
    course = st.text_input("Course Code")
    price = st.text_input("Maximum Price")
    condition = st.selectbox("Condition", ["", "Fair", "Good", "Like New"])
    submitted = st.form_submit_button("Search")
    if submitted:
        params = {}
        if course:
            params["course"] = course
        if price:
            params["price"] = price
        if condition:
            params["condition"] = condition
            
        # Use try/except to handle API errors gracefully
        try:
            # Try the correct endpoint
            response = requests.get("http://api:4000/b/textbooks", params=params, timeout=5)
            if response.status_code == 200:
                textbooks = response.json()
                st.write("Search Results:")
                st.dataframe(textbooks)
            else:
                st.error(f"Error searching textbooks. Status code: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if st.button("Back to Buyer Home"):
    st.switch_page("pages/buyer_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")