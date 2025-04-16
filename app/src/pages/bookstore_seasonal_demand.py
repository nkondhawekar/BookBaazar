import streamlit as st
import requests

st.set_page_config(page_title="Seasonal Demand Insights", layout="wide")
st.title("Seasonal Demand Insights")
response = requests.get("http://localhost:4000/m/seasonal-demand")
if response.status_code == 200:
    demand = response.json()
    st.dataframe(demand)
else:
    st.error("Error fetching seasonal demand data.")

st.markdown("[Back to Bookstore Home](?page=bookstore_home)")
