# `pages` Folder

This folder contains all the pages that make up the Book Bazaar application. Each page represents a specific functionality available to users based on their role in the system.

## Role-Based Organization

The pages are organized by user role, with each role having access to specific features:

### Buyer Pages
- `buyer_home.py` - Landing page for buyers (Jenna the Freshman)
- `buyer_textbook_search.py` - Search interface for finding textbooks by course, price, and condition
- `buyer_price_alert.py` - Management of price alerts for textbooks
- `buyer_wishlist.py` - Interface for maintaining a wishlist of desired textbooks

### Seller Pages
- `Seller_Home.py` - Landing page for sellers (Adam the Graduating Senior)
- `Seller_MyListings.py` - View and manage current textbook listings
- `Seller_PriceRecommendation.py` - Get price suggestions based on market data
- `Seller_UpdateListing.py` - Update status of listings (e.g., mark as sold)

### Administrator Pages
- `Admin_Home.py` - Landing page for administrators (Rachel)
- `Admin_ReportedUsers.py` - Dashboard for viewing reported users
- `Admin_FlaggedListings.py` - Review and manage flagged textbook listings
- `Admin_SystemLogs.py` - View system logs for monitoring platform activity

### Bookstore Manager Pages
- `bookstore_home.py` - Landing page for bookstore managers (Alfred)
- `bookstore_trending_books.py` - View trending books data for inventory decisions
- `bookstore_price_trends.py` - Analyze pricing trends in the student marketplace
- `bookstore_seasonal_demand.py` - Examine seasonal demand patterns for textbooks

## Navigation

All pages include:
- Sidebar navigation powered by the `SideBarLinks` function from the `modules/nav.py` module
- Role-specific links based on the user's selection from the home page
- "Return to Home" button for returning to the main selection screen

## Structure

Each page follows a consistent structure:
1. Imports and page configuration
2. Title and description
3. Sidebar navigation setup
4. Main content/functionality
5. API integration with error handling
6. Navigation buttons at the bottom

The pages work together to create a seamless user experience tailored to the specific needs of each user role in the Book Bazaar ecosystem.