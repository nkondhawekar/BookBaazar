# # Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# # This file has function to add certain functionality to the left side bar of the app

# import streamlit as st


# # #### ------------------------ General ------------------------
# def HomeNav():
#     st.sidebar.page_link("Home.py", label="Home", icon="🏠")


# def AboutPageNav():
#     st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


# # #### ------------------------ Examples for Role of pol_strat_advisor ------------------------
# def PolStratAdvHomeNav():
#     st.sidebar.page_link(
#         "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
#     )


# def WorldBankVizNav():
#     st.sidebar.page_link(
#         "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
#     )


# def MapDemoNav():
#     st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


# # ## ------------------------ Examples for Role of usaid_worker ------------------------
# def ApiTestNav():
#     st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


# def PredictionNav():
#     st.sidebar.page_link(
#         "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
#     )


# def ClassificationNav():
#     st.sidebar.page_link(
#         "pages/13_Classification.py", label="Classification Demo", icon="🌺"
#     )


# # #### ------------------------ System Admin Role ------------------------
# def AdminPageNav():
#     st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
#     st.sidebar.page_link(
#         "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
#     )


# # # --------------------------------Links Function -----------------------------------------------
# def SideBarLinks(show_home=False):
#     """
#     This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
#     """

#     # add a logo to the sidebar always
#     st.sidebar.image("assets/logo.png", width=150)

#     # If there is no logged in user, redirect to the Home (Landing) page
#     if "authenticated" not in st.session_state:
#         st.session_state.authenticated = False
#         st.switch_page("Home.py")

#     if show_home:
#         # Show the Home page link (the landing page)
#         HomeNav()

#     # Show the other page navigators depending on the users' role.
#     if st.session_state["authenticated"]:

#         # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
#         if st.session_state["role"] == "pol_strat_advisor":
#             PolStratAdvHomeNav()
#             WorldBankVizNav()
#             MapDemoNav()

#         # If the user role is usaid worker, show the Api Testing page
#         if st.session_state["role"] == "usaid_worker":
#             PredictionNav()
#             ApiTestNav()
#             ClassificationNav()

#         # If the user is an administrator, give them access to the administrator pages
#         if st.session_state["role"] == "administrator":
#             AdminPageNav()

#     # Always show the About page at the bottom of the list of links
#     AboutPageNav()

#     if st.session_state["authenticated"]:
#         # Always show a logout button if there is a logged in user
#         if st.sidebar.button("Logout"):
#             del st.session_state["role"]
#             del st.session_state["authenticated"]
#             st.switch_page("Home.py")



# -------------------- BookBazaar --------------------

# nav.py
# Navigation configuration for Book Bazar Streamlit UI

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("BookBazaar_Home.py", label="Home", icon="🏠")

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
    st.sidebar.image("assets/bookbazar_logo.png", width=150)

    # Redirect to Home if not authenticated
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        st.session_state["authenticated"] = False
        st.switch_page("BookBazaar_Home.py")

    # Optionally show Home link
    if show_home:
        HomeNav()

    # Show links based on role
    role = st.session_state.get("role", None)
    if st.session_state["authenticated"] and role:
        if role == "buyer":
            BuyerHomeNav()
            TextbookSearchNav()
            PriceAlertsNav()
            WishlistNav()

        elif role == "seller":
            SellerHomeNav()
            MyListingsNav()
            PriceRecommendationNav()
            UpdateListingNav()

        elif role == "administrator":
            AdminHomeNav()
            ReportedUsersNav()
            FlaggedListingsNav()
            SystemLogsNav()

        elif role == "bookstore_manager":
            BookstoreHomeNav()
            TrendingBooksNav()
            PriceTrendsNav()
            SeasonalDemandNav()

    # Always show About link at bottom
    AboutPageNav()

    # Logout button
    if st.session_state.get("authenticated"):
        if st.sidebar.button("Logout"):
            for key in ("authenticated", "role"):
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page("BookBazaar_Home.py")

