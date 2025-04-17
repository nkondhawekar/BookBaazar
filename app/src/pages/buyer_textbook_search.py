import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="Textbook Search", layout="wide")
st.title("Textbook Search")
st.write("Search for textbooks by course code, maximum price, and condition.")

# Add sidebar
SideBarLinks(show_home=True)

# Expanded debug section (collapsible)
with st.expander("Debug Information", expanded=False):
    st.info("This section helps debug API connection issues")
    
    # Test API reachability
    try:
        health_check = requests.get("http://api:4000/", timeout=2)
        st.success(f"API base endpoint is reachable: Status {health_check.status_code}")
    except Exception as e:
        st.error(f"Cannot reach API base endpoint: {str(e)}")

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
                st.info("The API endpoint 'b/textbooks' might not be implemented yet.")
                
                # Show mock data for demonstration
                st.write("Showing sample data for demonstration:")
                mock_data = [
                    {"book_id": 1, "title": "Introduction to Computer Science", "author": "John Smith", "price": 45.99, "condition": "Used"},
                    {"book_id": 2, "title": "Advanced Mathematics", "author": "Jane Doe", "price": 65.00, "condition": "New"},
                    {"book_id": 3, "title": "Biology 101", "author": "Robert Johnson", "price": 35.50, "condition": "Good"}
                ]
                st.dataframe(mock_data)
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
            # Show mock data
            st.write("Showing sample data for demonstration:")
            mock_data = [
                {"book_id": 1, "title": "Introduction to Computer Science", "author": "John Smith", "price": 45.99, "condition": "Used"},
                {"book_id": 2, "title": "Advanced Mathematics", "author": "Jane Doe", "price": 65.00, "condition": "New"},
                {"book_id": 3, "title": "Biology 101", "author": "Robert Johnson", "price": 35.50, "condition": "Good"}
            ]
            st.dataframe(mock_data)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            # Show mock data
            st.write("Showing sample data for demonstration:")
            mock_data = [
                {"book_id": 1, "title": "Introduction to Computer Science", "author": "John Smith", "price": 45.99, "condition": "Used"},
                {"book_id": 2, "title": "Advanced Mathematics", "author": "Jane Doe", "price": 65.00, "condition": "New"},
                {"book_id": 3, "title": "Biology 101", "author": "Robert Johnson", "price": 35.50, "condition": "Good"}
            ]
            st.dataframe(mock_data)

if st.button("Back to Buyer Home"):
    st.switch_page("pages/buyer_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")