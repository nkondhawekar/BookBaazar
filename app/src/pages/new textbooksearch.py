import streamlit as st
import requests

st.set_page_config(page_title="Textbook Search", layout="wide")
st.title("Textbook Search")
st.write("Search for textbooks by course code, maximum price, and condition.")

with st.form("search_form"):
    course = st.text_input("Course Code")
    price = st.text_input("Maximum Price")
    condition = st.selectbox("Condition", ["", "New", "Used", "Acceptable"])
    submitted = st.form_submit_button("Search")
    if submitted:
        params = {}
        if course:
            params["course"] = course
        if price:
            params["price"] = price
        if condition:
            params["condition"] = condition
        # Call the Flask API endpoint at /textbooks
        response = requests.get("http://localhost:5000/textbooks", params=params)
        if response.status_code == 200:
            textbooks = response.json()
            st.write("Search Results:")
            st.dataframe(textbooks)
        else:
            st.error("Error searching textbooks.")

st.markdown("[Back to Buyer Home](?page=00_Buyer_Home)")
