# Modules Folder

This folder contains functionality that needs to be accessible throughout the Book Bazaar application.

## Files

### nav.py

This module supports our custom navigation sidebar and implements Role-Based Access Control (RBAC) for the application. Key features include:

- **SideBarLinks function** - Dynamically populates the sidebar with links based on the user's role
- **Role-specific navigation functions** - Separate functions for generating navigation links for each user persona:
  - Buyer navigation links (search, wishlists, price alerts)
  - Seller navigation links (listings, price recommendations)
  - Administrator navigation links (reports, flagged listings, logs)
  - Bookstore Manager navigation links (trending books, price trends, demand)

### mock_data.py

This module provides fallback mock data when API endpoints are not yet fully implemented or are experiencing errors. It includes:

- Mock textbook listings
- Mock price alerts
- Mock user reviews
- Mock sales data
- Mock analytics information

## How RBAC Works

1. The application uses Streamlit's `session_state` to store the user's role after they select a persona on the home page.
2. The `SideBarLinks` function checks the role in the session state and displays only the navigation links appropriate for that role.
3. Each page in the application also verifies the user's role to ensure they only access features they're authorized to use.

This approach allows for a seamless and secure user experience tailored to each persona's needs.