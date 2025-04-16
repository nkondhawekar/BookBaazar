# ##################################################
# # This is the main/entry-point file for the 
# # sample application for your project
# ##################################################

# # Set up basic logging infrastructure
# import logging
# logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # import the main streamlit library as well
# # as SideBarLinks function from src/modules folder
# import streamlit as st
# from modules.nav import SideBarLinks

# # streamlit supports reguarl and wide layout (how the controls
# # are organized/displayed on the screen).
# st.set_page_config(layout = 'wide')

# # If a user is at this page, we assume they are not 
# # authenticated.  So we change the 'authenticated' value
# # in the streamlit session_state to false. 
# st.session_state['authenticated'] = False

# # Use the SideBarLinks function from src/modules/nav.py to control
# # the links displayed on the left-side panel. 
# # IMPORTANT: ensure src/.streamlit/config.toml sets
# # showSidebarNavigation = false in the [client] section
# SideBarLinks(show_home=True)

# # ***************************************************
# #    The major content of this page
# # ***************************************************

# # set the title of the page and provide a simple prompt. 
# logger.info("Loading the Home page of the app")
# st.title('CS 3200 Sample Semester Project App')
# st.write('\n\n')
# st.write('### HI! As which user would you like to log in?')

# # For each of the user personas for which we are implementing
# # functionality, we put a button on the screen that the user 
# # can click to MIMIC logging in as that mock user. 

# if st.button("Act as John, a Political Strategy Advisor", 
#             type = 'primary', 
#             use_container_width=True):
#     # when user clicks the button, they are now considered authenticated
#     st.session_state['authenticated'] = True
#     # we set the role of the current user
#     st.session_state['role'] = 'pol_strat_advisor'
#     # we add the first name of the user (so it can be displayed on 
#     # subsequent pages). 
#     st.session_state['first_name'] = 'John'
#     # finally, we ask streamlit to switch to another page, in this case, the 
#     # landing page for this particular user type
#     logger.info("Logging in as Political Strategy Advisor Persona")
#     st.switch_page('pages/00_Pol_Strat_Home.py')

# if st.button('Act as Mohammad, an USAID worker', 
#             type = 'primary', 
#             use_container_width=True):
#     st.session_state['authenticated'] = True
#     st.session_state['role'] = 'usaid_worker'
#     st.session_state['first_name'] = 'Mohammad'
#     st.switch_page('pages/10_USAID_Worker_Home.py')

# if st.button('Act as System Administrator', 
#             type = 'primary', 
#             use_container_width=True):
#     st.session_state['authenticated'] = True
#     st.session_state['role'] = 'administrator'
#     st.session_state['first_name'] = 'SysAdmin'
#     st.switch_page('pages/20_Admin_Home.py')



#------------------------ Book Bazaar Home Page ------------------------

# app/src/Home.py

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False


# Configure the Streamlit page
st.set_page_config(page_title="Book Bazar", layout="wide")
st.title("Welcome to Book Bazar")
st.write("Select a persona to simulate login and explore the marketplace:")

# Initialize sidebar links (no Home link on the landing page)
SideBarLinks(show_home=False)

# Persona buttons in the main content area
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Buyer (Jenna the Freshman)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "buyer"
        st.experimental_set_query_params(page="00_Buyer_Home")
        st.experimental_rerun()

with col2:
    if st.button("Seller (Adam the Graduating Senior)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "seller"
        st.experimental_set_query_params(page="10_Seller_Home")
        st.experimental_rerun()

with col3:
    if st.button("Administrator (Rachel)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "administrator"
        st.experimental_set_query_params(page="20_Admin_Home")
        st.experimental_rerun()

with col4:
    if st.button("Bookstore Manager (Alfred)"):
        st.session_state["authenticated"] = True
        st.session_state["role"] = "bookstore_manager"
        st.experimental_set_query_params(page="30_Bookstore_Home")
        st.experimental_rerun()

