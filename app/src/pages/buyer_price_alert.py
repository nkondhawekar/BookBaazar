import streamlit as st
import requests

st.set_page_config(page_title="My Price Alerts", layout="wide")
st.title("My Price Alerts")
st.write("View your current price alerts and create new ones.")

# Display existing price alerts for a demo user (userId = 1)
response = requests.get("http://localhost:5000/buyer/price-alerts")
if response.status_code == 200:
    alerts = response.json()
    st.write("Existing Price Alerts:")
    st.dataframe(alerts)
else:
    st.error("Error fetching price alerts.")

st.markdown("### Create a New Price Alert")
with st.form("price_alert_form"):
    book_id = st.text_input("Book ID")
    target_price = st.text_input("Target Price")
    submit_alert = st.form_submit_button("Create Price Alert")
    if submit_alert:
        payload = {"bookId": book_id, "userId": 1, "targetPrice": target_price}
        r = requests.post("http://localhost:5000/buyer/price-alert", json=payload)
        if r.status_code == 201:
            st.success("Price alert created!")
        else:
            st.error("Failed to create price alert.")

st.markdown("[Back to Buyer Home](?page=00_Buyer_Home)")
