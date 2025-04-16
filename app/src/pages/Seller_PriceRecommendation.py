import streamlit as st
import requests

st.set_page_config(page_title="Price Recommendation", layout="wide")
st.title("Price Recommendation")
st.write("Get a suggested price for one of your listings.")

# For demo, assume listingId = 1
response = requests.get("http://localhost:4000/s/price-recommendation/1")
if response.status_code == 200:
    recommendation = response.json()
    st.write(f"Listing ID: {recommendation['listingId']}")
    st.write(f"Recommended Price: ${recommendation['recommended_price']}")
    st.write(recommendation['message'])
else:
    st.error("Error fetching price recommendation.")

st.markdown("[Back to Seller Home](?page=Seller_Home)")
