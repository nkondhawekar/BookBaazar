# Database Files

This directory contains the SQL scripts used to initialize the Book Bazaar MySQL database.

## Files

- `BookBazarDDL.sql` - Contains the Data Definition Language (DDL) statements to create the database schema, including all tables and relationships.
- `dbproject_data.sql` - Contains INSERT statements to populate the database with sample data for development and testing.

## Database Schema

The Book Bazaar database has the following main tables:

- `Users` - Stores information about buyers, sellers, administrators, and bookstore managers
- `Textbooks` - Contains details about the textbooks being sold
- `Listings` - Represents textbooks listed for sale by sellers
- `SalesTransactions` - Records completed sales transactions
- `Reviews` - Stores buyer reviews of sellers
- `Messages` - Contains messages exchanged between buyers and sellers
- `Wishlist` - Records books that buyers are interested in
- `PriceAlerts` - Stores price thresholds set by buyers for notifications
- `SystemLogs` - Tracks system events for administrators
- `Reports` - Records user reports for administrators to review

## Restarting the Database

If you need to reset the database to its initial state, you can use the following steps:

1. Stop all containers: docker compose down
2. Restart the containers: docker compose up -d