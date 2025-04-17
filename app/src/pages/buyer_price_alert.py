import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(page_title="My Price Alerts", layout="wide")
st.title("My Price Alerts")
st.write("View your current price alerts and create new ones.")

# Add sidebar
SideBarLinks(show_home=True)

# Use try/except to handle API errors gracefully
try:
    # Display existing price alerts for a demo user (userId = 1)
    response = requests.get("http://web-api:4000/b/price-alerts", timeout=5)
    if response.status_code == 200:
        alerts = response.json()
        st.write("Existing Price Alerts:")
        st.dataframe(alerts)
    else:
        st.error(f"Error fetching price alerts. Status code: {response.status_code}")
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the API server. Please make sure the server is running.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

st.markdown("### Create a New Price Alert")
with st.form("price_alert_form"):
    book_id = st.text_input("Book ID")
    target_price = st.text_input("Target Price")
    submit_alert = st.form_submit_button("Create Price Alert")
    if submit_alert:
        try:
            payload = {"bookId": book_id, "userId": 1, "targetPrice": target_price}
            r = requests.post("http://api:4000/b/price-alert", json=payload, timeout=5)
            if r.status_code == 201:
                st.success("Price alert created!")
            else:
                st.error(f"Failed to create price alert. Status code: {r.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API server. Please make sure the server is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if st.button("Back to Buyer Home"):
    st.switch_page("pages/buyer_home.py")

if st.button("Return to Home"):
    st.switch_page("Home.py")