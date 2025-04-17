
# -------------------- BookBazaar --------------------

# nav.py
# Navigation configuration for Book Bazar Streamlit UI

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="ℹ️")


#### ------------------------ Buyer (Jenna the Freshman) ------------------------
def BuyerHomeNav():
    st.sidebar.page_link(
        "pages/buyer_home.py", label="Buyer Home", icon="👩‍🎓"
    )

def TextbookSearchNav():
    st.sidebar.page_link(
        "pages/buyer_textbook_search.py", label="Textbook Search", icon="🔍"
    )

def PriceAlertsNav():
    st.sidebar.page_link(
        "pages/buyer_price_alert.py", label="My Price Alerts", icon="💲"
    )

def WishlistNav():
    st.sidebar.page_link(
        "pages/buyer_wishlist.py", label="My Wishlist", icon="📝"
    )


#### ------------------------ Seller (Adam the Graduating Senior) ------------------------
def SellerHomeNav():
    st.sidebar.page_link(
        "pages/Seller_Home.py", label="Seller Home", icon="🛒"
    )

def MyListingsNav():
    st.sidebar.page_link(
        "pages/Seller_MyListings.py", label="My Listings", icon="📋"
    )

def PriceRecommendationNav():
    st.sidebar.page_link(
        "pages/Seller_PriceRecommendation.py", label="Price Recommendation", icon="📈"
    )

def UpdateListingNav():
    st.sidebar.page_link(
        "pages/Seller_UpdateListing.py", label="Update Listing Status", icon="✏️"
    )


#### ------------------------ Admin (Rachel the Administrator) ------------------------
def AdminHomeNav():
    st.sidebar.page_link(
        "pages/Admin_Home.py", label="Admin Home", icon="🖥️"
    )

def ReportedUsersNav():
    st.sidebar.page_link(
        "pages/Admin_ReportedUsers.py", label="Reported Users", icon="🚩"
    )

def FlaggedListingsNav():
    st.sidebar.page_link(
        "pages/Admin_FlaggedListings.py", label="Flagged Listings", icon="⚠️"
    )

def SystemLogsNav():
    st.sidebar.page_link(
        "pages/Admin_SystemLogs.py", label="System Logs", icon="📜"
    )


#### ------------------------ Bookstore Manager (Alfred) ------------------------
def BookstoreHomeNav():
    st.sidebar.page_link(
        "pages/bookstore_home.py", label="Bookstore Home", icon="🏫"
    )

def TrendingBooksNav():
    st.sidebar.page_link(
        "pages/bookstore_trending_books.py", label="Trending Books", icon="🔥"
    )

def PriceTrendsNav():
    st.sidebar.page_link(
        "pages/bookstore_price_trends.py", label="Price Trends", icon="💹"
    )

def SeasonalDemandNav():
    st.sidebar.page_link(
        "pages/bookstore_seasonal_demand.py", label="Seasonal Demand", icon="📅"
    )


# -------------------------------- Links Function -----------------------------------------------

def SideBarLinks(show_home: bool = False):
    """
    Adds sidebar navigation links based on the logged-in user's role.
    """
    # Sidebar logo
    try:
        st.sidebar.image("assets/logo.png", width=150)
    except:
        st.sidebar.write("Book Bazar")

    # Optionally show Home link
    if show_home:
        st.sidebar.page_link("Home.py", label="Home", icon="🏠")

    # Show links based on role
    role = st.session_state.get("role", None)
    if st.session_state.get("authenticated", False) and role:
        if role == "buyer":
            st.sidebar.page_link("pages/buyer_home.py", label="Buyer Home", icon="👩‍🎓")
            st.sidebar.page_link("pages/buyer_textbook_search.py", label="Textbook Search", icon="🔍")
            st.sidebar.page_link("pages/buyer_price_alert.py", label="My Price Alerts", icon="💲")
            st.sidebar.page_link("pages/buyer_wishlist.py", label="My Wishlist", icon="📝")

        elif role == "seller":
            st.sidebar.page_link("pages/Seller_Home.py", label="Seller Home", icon="🛒")
            st.sidebar.page_link("pages/Seller_MyListings.py", label="My Listings", icon="📋")
            st.sidebar.page_link("pages/Seller_PriceRecommendation.py", label="Price Recommendation", icon="📈")
            st.sidebar.page_link("pages/Seller_UpdateListing.py", label="Update Listing Status", icon="✏️")

        elif role == "administrator":
            st.sidebar.page_link("pages/Admin_Home.py", label="Admin Home", icon="🖥️")
            st.sidebar.page_link("pages/Admin_ReportedUsers.py", label="Reported Users", icon="🚩")
            st.sidebar.page_link("pages/Admin_FlaggedListings.py", label="Flagged Listings", icon="⚠️")
            st.sidebar.page_link("pages/Admin_SystemLogs.py", label="System Logs", icon="📜")

        elif role == "bookstore_manager":
            st.sidebar.page_link("pages/bookstore_home.py", label="Bookstore Home", icon="🏫")
            st.sidebar.page_link("pages/bookstore_trending_books.py", label="Trending Books", icon="🔥")
            st.sidebar.page_link("pages/bookstore_price_trends.py", label="Price Trends", icon="💹")
            st.sidebar.page_link("pages/bookstore_seasonal_demand.py", label="Seasonal Demand", icon="📅")

    # Always show About link at bottom if it exists
    try:
        st.sidebar.page_link("pages/About.py", label="About", icon="ℹ️")
    except:
        pass

    # Logout button (only show if authenticated)
    if st.session_state.get("authenticated", False):
        if st.sidebar.button("Logout"):
            for key in ("authenticated", "role"):
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page("Home.py")