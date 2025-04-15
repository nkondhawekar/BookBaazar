
# blueprints/buyer.py
from flask import Blueprint, request, jsonify
from db import query, execute
from datetime import datetime

bp = Blueprint('buyer', __name__, url_prefix='/buyer')

# 1. Search textbooks with optional filters (course, price, condition)
@bp.route('/textbooks', methods=['GET'])
def search_textbooks():
    course = request.args.get('course')
    price = request.args.get('price')
    condition = request.args.get('condition')
    sql = 'SELECT * FROM textbooks WHERE 1=1'
    params = []
    if course:
        sql += ' AND course_code = ?'
        params.append(course)
    if price:
        sql += ' AND price <= ?'
        params.append(price)
    if condition:
        sql += ' AND condition = ?'
        params.append(condition)
    try:
        textbooks = query(sql, params)
        return jsonify(textbooks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. Create a price alert for a textbook
@bp.route('/price-alert', methods=['POST'])
def create_price_alert():
    data = request.get_json()
    bookId = data.get('bookId')
    userId = data.get('userId')
    targetPrice = data.get('targetPrice')
    if not all([bookId, userId, targetPrice]):
        return jsonify({'error': 'Missing required fields.'}), 400
    sql = 'INSERT INTO price_alerts (book_id, user_id, target_price) VALUES (?, ?, ?)'
    try:
        execute(sql, [bookId, userId, targetPrice])
        return jsonify({'message': 'Price alert created.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. View reviews for a given seller
@bp.route('/reviews/seller/<int:sellerId>', methods=['GET'])
def get_seller_reviews(sellerId):
    sql = 'SELECT * FROM reviews WHERE seller_id = ?'
    try:
        reviews = query(sql, [sellerId])
        return jsonify(reviews)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4. Submit a review for a seller
@bp.route('/reviews', methods=['POST'])
def submit_review():
    data = request.get_json()
    sellerId = data.get('sellerId')
    buyerId = data.get('buyerId')
    rating = data.get('rating')
    comment = data.get('comment')
    if not all([sellerId, buyerId, rating]):
        return jsonify({'error': 'Missing required fields.'}), 400
    sql = 'INSERT INTO reviews (seller_id, buyer_id, rating, comment, created_at) VALUES (?, ?, ?, ?, ?)'
    try:
        execute(sql, [sellerId, buyerId, rating, comment, datetime.now()])
        return jsonify({'message': 'Review submitted successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5. Add a textbook to the wishlist
@bp.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    data = request.get_json()
    userId = data.get('userId')
    bookId = data.get('bookId')
    if not all([userId, bookId]):
        return jsonify({'error': 'Missing userId or bookId.'}), 400
    sql = 'INSERT INTO wishlist (user_id, book_id) VALUES (?, ?)'
    try:
        execute(sql, [userId, bookId])
        return jsonify({'message': 'Book added to wishlist.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Remove a textbook from the wishlist
@bp.route('/wishlist/<int:bookId>', methods=['DELETE'])
def remove_from_wishlist(bookId):
    data = request.get_json()  # Alternatively, get userId from session or query param.
    userId = data.get('userId')
    if not userId:
        return jsonify({'error': 'Missing userId.'}), 400
    sql = 'DELETE FROM wishlist WHERE user_id = ? AND book_id = ?'
    try:
        execute(sql, [userId, bookId])
        return jsonify({'message': 'Book removed from wishlist.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 7. Send a message to a seller
@bp.route('/messages', methods=['POST'])
def send_message():
    data = request.get_json()
    senderId = data.get('senderId')
    listingId = data.get('listingId')
    message = data.get('message')
    if not all([senderId, listingId, message]):
        return jsonify({'error': 'Missing required fields.'}), 400
    sql = 'INSERT INTO messages (sender_id, listing_id, message, sent_at) VALUES (?, ?, ?, ?)'
    try:
        execute(sql, [senderId, listingId, message, datetime.now()])
        return jsonify({'message': 'Message sent.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 8. Retrieve messages for a specific listing
@bp.route('/messages/<int:listingId>', methods=['GET'])
def get_messages(listingId):
    sql = 'SELECT * FROM messages WHERE listing_id = ? ORDER BY sent_at ASC'
    try:
        msgs = query(sql, [listingId])
        return jsonify(msgs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 9. Get bulk pricing information (mock endpoint to show available bulk discounts)
@bp.route('/bulk-pricing', methods=['GET'])
def bulk_pricing():
    # In a real implementation, you might run a query to see if a seller offers bulk discounts.
    # Here we provide a dummy response.
    bulk_info = {
        "bulk_threshold": 5,
        "discount_rate": 0.1,
        "message": "Buy 5 or more textbooks and save 10%!"
    }
    return jsonify(bulk_info)
