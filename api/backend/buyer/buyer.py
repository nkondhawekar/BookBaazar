# blueprints/buyer.py
from flask import Blueprint, request, jsonify
from backend.db_connection import db
from datetime import datetime
from pymysql.cursors import DictCursor

buyers = Blueprint('buyer', __name__, url_prefix='/buyer')

# 1. Search textbooks with optional filters (course, price, condition)
@buyers.route('/textbooks', methods=['GET'])
def search_textbooks():
    course = request.args.get('course')
    price = request.args.get('price')
    condition = request.args.get('condition')
    
    sql = 'SELECT * FROM Textbooks WHERE 1=1'
    params = []
    
    if course:
        sql += ' AND class_code = %s'  # Changed from course_code to class_code
        params.append(course)
    
    if price:
        # Join with Listings to get price
        sql = '''
            SELECT DISTINCT t.* 
            FROM Textbooks t
            JOIN Listings l ON t.book_id = l.book_id
            WHERE l.price <= %s
        '''
        params = [price]
        
        if course:
            sql += ' AND t.class_code = %s'
            params.append(course)
        
        if condition:
            sql += ' AND t.condition = %s'
            params.append(condition)
    elif condition:
        sql += ' AND `condition` = %s'  # Using backticks because condition is a reserved word
        params.append(condition)
    
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, params)
        textbooks = cursor.fetchall()
        cursor.close()
        return jsonify(textbooks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. Create a price alert for a textbook
@buyers.route('/price-alerts', methods=['GET'])
def get_price_alerts():
    # Assume user ID is 1 for demo purposes, ideally from session or query param
    userId = request.args.get('userId', 1)
    
    sql = 'SELECT * FROM PriceAlerts WHERE user_id = %s'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [userId])
        alerts = cursor.fetchall()
        cursor.close()
        return jsonify(alerts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a price alert
@buyers.route('/price-alert', methods=['POST'])
def create_price_alert():
    data = request.get_json()
    bookId = data.get('bookId')
    userId = data.get('userId')
    targetPrice = data.get('targetPrice')
    
    if not all([bookId, userId, targetPrice]):
        return jsonify({'error': 'Missing required fields.'}), 400
    
    sql = 'INSERT INTO PriceAlerts (user_id, book_id, target_price) VALUES (%s, %s, %s)'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [userId, bookId, targetPrice])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Price alert created.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. View reviews for a given seller
@buyers.route('/reviews/seller/<int:sellerId>', methods=['GET'])
def get_seller_reviews(sellerId):
    sql = 'SELECT * FROM Reviews WHERE seller_id = %s'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [sellerId])
        reviews = cursor.fetchall()
        cursor.close()
        return jsonify(reviews)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4. Submit a review for a seller
@buyers.route('/reviews', methods=['POST'])
def submit_review():
    data = request.get_json()
    sellerId = data.get('sellerId')
    buyerId = data.get('buyerId')
    rating = data.get('rating')
    comment = data.get('comment')
    
    if not all([sellerId, buyerId, rating]):
        return jsonify({'error': 'Missing required fields.'}), 400
    
    sql = 'INSERT INTO Reviews (seller_id, buyer_id, rating, comment, date) VALUES (%s, %s, %s, %s, %s)'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [sellerId, buyerId, rating, comment, datetime.now()])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Review submitted successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5. Add a textbook to the wishlist
@buyers.route('/wishlist', methods=['GET'])
def get_wishlist():
    # Assume user ID is 1 for demo purposes
    userId = request.args.get('userId', 1)
    
    sql = '''
        SELECT w.*, t.title, t.author 
        FROM Wishlist w 
        JOIN Textbooks t ON w.book_id = t.book_id 
        WHERE w.user_id = %s
    '''
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [userId])
        wishlist = cursor.fetchall()
        cursor.close()
        return jsonify(wishlist)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@buyers.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    data = request.get_json()
    userId = data.get('userId')
    bookId = data.get('bookId')
    
    if not all([userId, bookId]):
        return jsonify({'error': 'Missing userId or bookId.'}), 400
    
    sql = 'INSERT INTO Wishlist (user_id, book_id) VALUES (%s, %s)'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [userId, bookId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Book added to wishlist.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Remove a textbook from the wishlist
@buyers.route('/wishlist/<int:bookId>', methods=['DELETE'])
def remove_from_wishlist(bookId):
    data = request.get_json()
    userId = data.get('userId')
    
    if not userId:
        return jsonify({'error': 'Missing userId.'}), 400
    
    sql = 'DELETE FROM Wishlist WHERE user_id = %s AND book_id = %s'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [userId, bookId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Book removed from wishlist.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 7. Send a message to a seller
@buyers.route('/messages', methods=['POST'])
def send_message():
    data = request.get_json()
    buyerId = data.get('buyerId')
    sellerId = data.get('sellerId')
    listingId = data.get('listingId')
    message = data.get('message')
    
    if not all([buyerId, sellerId, listingId, message]):
        return jsonify({'error': 'Missing required fields.'}), 400
    
    sql = 'INSERT INTO Messages (listing_id, buyer_id, seller_id, message_content, timestamp) VALUES (%s, %s, %s, %s, %s)'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [listingId, buyerId, sellerId, message, datetime.now()])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Message sent.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 8. Retrieve messages for a specific listing
@buyers.route('/messages/<int:listingId>', methods=['GET'])
def get_messages(listingId):
    sql = 'SELECT * FROM Messages WHERE listing_id = %s ORDER BY timestamp ASC'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [listingId])
        msgs = cursor.fetchall()
        cursor.close()
        return jsonify(msgs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 9. Get bulk pricing information
@buyers.route('/bulk-pricing', methods=['GET'])
def bulk_pricing():
    sellerId = request.args.get('sellerId')
    if not sellerId:
        return jsonify({'error': 'sellerId is required'}), 400
        
    sql = 'SELECT * FROM BulkPricing WHERE seller_id = %s'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [sellerId])
        bulk_info = cursor.fetchall()
        cursor.close()
        return jsonify(bulk_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500