DROP DATABASE IF EXISTS TextbookMarketplace;
CREATE DATABASE IF NOT EXISTS TextbookMarketplace;
SHOW DATABASES;
USE TextbookMarketplace;

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    role ENUM('buyer', 'seller', 'admin', 'bookstore_manager') NOT NULL,
    total_sales INT DEFAULT 0,
    rating FLOAT DEFAULT 0.0,
    banned BOOLEAN DEFAULT 0
);

CREATE TABLE Textbooks (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    isbn VARCHAR(20) UNIQUE,
    class_code VARCHAR(20),
    `condition` ENUM('new', 'like new', 'good', 'fair', 'poor')
);

CREATE TABLE Listings (
    listing_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_id INT,
    book_id INT,
    price DECIMAL(10,2) NOT NULL,
    status ENUM('active', 'sold', 'removed') DEFAULT 'active',
    date_listed DATETIME DEFAULT CURRENT_TIMESTAMP,
    flagged BOOLEAN DEFAULT 0,
    FOREIGN KEY (seller_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);

CREATE TABLE SalesTransactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    listing_id INT,
    buyer_id INT,
    seller_id INT,
    date_purchased DATETIME DEFAULT CURRENT_TIMESTAMP,
    buyer_rating FLOAT,
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id),
    FOREIGN KEY (buyer_id) REFERENCES Users(user_id),
    FOREIGN KEY (seller_id) REFERENCES Users(user_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    buyer_id INT,
    seller_id INT,
    rating FLOAT NOT NULL,
    comment TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES Users(user_id),
    FOREIGN KEY (seller_id) REFERENCES Users(user_id)
);

CREATE TABLE Messages (
    message_id INT PRIMARY KEY AUTO_INCREMENT,
    listing_id INT,
    buyer_id INT,
    seller_id INT,
    message_content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id),
    FOREIGN KEY (buyer_id) REFERENCES Users(user_id),
    FOREIGN KEY (seller_id) REFERENCES Users(user_id)
);

CREATE TABLE Wishlist (
    wishlist_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);

CREATE TABLE PriceAlerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    target_price DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);

CREATE TABLE BulkPricing (
    bulk_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_id INT,
    discount DECIMAL(5,2),
    quantity INT,
    FOREIGN KEY (seller_id) REFERENCES Users(user_id)
);

CREATE TABLE Promotions (
    promo_id INT PRIMARY KEY AUTO_INCREMENT,
    listing_id INT,
    start_date DATETIME,
    end_date DATETIME,
    cost DECIMAL(10,2),
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id)
);

CREATE TABLE ListingAnalytics (
    analytics_id INT PRIMARY KEY AUTO_INCREMENT,
    listing_id INT,
    total_views INT DEFAULT 0,
    clicks INT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id)
);

CREATE TABLE BookstoreAnalytics (
    analytics_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    total_listings INT DEFAULT 0,
    total_sales INT DEFAULT 0,
    avg_resale_price DECIMAL(10,2),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);

CREATE TABLE SystemLogs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_type VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Reports (
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    reported_user_id INT,
    reported_by_user_id INT,
    reason TEXT,
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reported_user_id) REFERENCES Users(user_id),
    FOREIGN KEY (reported_by_user_id) REFERENCES Users(user_id)
);


CREATE TABLE Server (
    server_id INT PRIMARY KEY AUTO_INCREMENT,
    server_name VARCHAR(100),
    uptime_percentage DECIMAL(5,2),
    status ENUM('online', 'offline', 'maintenance'),
    last_downtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE CompetitorBenchmarking (
    benchmark_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    bookstore_price DECIMAL(10,2),
    student_resale_avg_price DECIMAL(10,2),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);


CREATE TABLE InventoryAlerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    stock_status ENUM('low', 'out of stock', 'in stock'),
    FOREIGN KEY (book_id) REFERENCES Textbooks(book_id)
);