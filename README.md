# Book Bazaar: A Campus Textbook Marketplace

Book Bazaar is a peer-to-peer textbook marketplace designed specifically for college students by Richard Ferrentino, Pranav Thamil, Arvind Narayan, and Nikita Kondhawekar. Our mission is to make textbooks more affordable and accessible by connecting buyers and sellers directly within the campus community.

## Project Components

Book Bazaar consists of three major components, each running in its own Docker Container:

- **Streamlit App** in the `./app` directory - The user interface for different personas
- **Flask REST API** in the `./api` directory - Handles data processing and database interactions
- **MySQL Database** initialized with SQL scripts from the `./database-files` directory

## User Personas

Book Bazaar serves four distinct user types, each with their own interface and features:

1. **Buyers** (e.g., Jenna the Freshman) - Browse, search, and purchase textbooks at lower prices than the campus bookstore. Set price alerts and create wishlists.

2. **Sellers** (e.g., Adam the Graduating Senior) - List used textbooks, receive price recommendations, and manage sales.

3. **Administrators** (e.g., Rachel) - Monitor the platform for appropriate use, review flagged listings, and ensure a safe marketplace.

4. **Bookstore Managers** (e.g., Alfred) - Gain insights into student textbook needs and trends to optimize inventory and pricing strategies.

## Setup Instructions

### Prerequisites

- Git
- Docker and Docker Compose
- A code editor (VSCode recommended)
- Python 3.x

### Getting Started

1. Clone this repository to your local machine

2. Set up the environment variables
- Create a `.env` file in the `api` folder based on the `.env.template` file
- Edit the `.env` file with your database credentials:
- (change the password to whatever you want)

3. Start the Docker containers: docker compose up -d

4. Access the application
- Streamlit UI: http://localhost:8501
- Flask API: http://localhost:4000

5. To stop the containers: docker compose down

## Project Structure

- `/app` - Streamlit application
- `/src` - Source code
 - `/pages` - Interface pages for different user roles
 - `/modules` - Shared functionality
 - `/assets` - Images and other static assets

- `/api` - Flask REST API
- `/backend` - Backend code
 - `/admin` - Admin-specific endpoints
 - `/buyer` - Buyer-specific endpoints
 - `/seller` - Seller-specific endpoints
 - `/bookstore_manager` - Bookstore manager-specific endpoints
 - `/db_connection` - Database connection utilities

- `/database-files` - SQL scripts for database initialization
- `BookBazarDDL.sql` - Database schema definition
- `dbproject_data.sql` - Sample data for testing

## Role-Based Access

Book Bazaar implements a role-based access control system using Streamlit's session state. When a user selects a persona from the home page, they are directed to the appropriate interface with role-specific features and navigation options.

## Database Schema

The application uses a MySQL database with tables for Users, Textbooks, Listings, Transactions, Messages, and more. See the `BookBazarDDL.sql` file for the complete database schema.

Video Demonstration: https://northeastern-my.sharepoint.com/:v:/g/personal/thamil_p_northeastern_edu/ETQX-q1h2QdGsBibOxRGwWoBvVg_DahwM8YkoJWMyNpjHA?e=PtU2lh&nav=eyJwbGF5YmFja09wdGlvbnMiOnt9LCJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbE1vZGUiOiJtaXMiLCJyZWZlcnJhbFZpZXciOiJwb3N0cm9sbC1jb3B5bGluayIsInJlZmVycmFsUGxheWJhY2tTZXNzaW9uSWQiOiJiYzMyMjNjNC1iMjhmLTQxNzUtYTY0ZS0zODlmYmI4MDEwZmEifX0%3D
