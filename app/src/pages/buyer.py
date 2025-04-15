# blueprints/buyer.py
from flask import Blueprint, request, jsonify, render_template_string
from db import query, execute
from datetime import datetime

bp = Blueprint('buyer', __name__, url_prefix='/buyer')


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

@bp.route('/reviews/seller/<int:sellerId>', methods=['GET'])
def get_seller_reviews(sellerId):
    sql = 'SELECT * FROM reviews WHERE seller_id = ?'
    try:
        reviews = query(sql, [sellerId])
        return jsonify(reviews)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

@bp.route('/wishlist/<int:bookId>', methods=['DELETE'])
def remove_from_wishlist(bookId):
    data = request.get_json()
    userId = data.get('userId')
    if not userId:
        return jsonify({'error': 'Missing userId.'}), 400
    sql = 'DELETE FROM wishlist WHERE user_id = ? AND book_id = ?'
    try:
        execute(sql, [userId, bookId])
        return jsonify({'message': 'Book removed from wishlist.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

@bp.route('/messages/<int:listingId>', methods=['GET'])
def get_messages(listingId):
    sql = 'SELECT * FROM messages WHERE listing_id = ? ORDER BY sent_at ASC'
    try:
        msgs = query(sql, [listingId])
        return jsonify(msgs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/bulk-pricing', methods=['GET'])
def bulk_pricing():
    bulk_info = {
        "bulk_threshold": 5,
        "discount_rate": 0.1,
        "message": "Buy 5 or more textbooks and save 10%!"
    }
    return jsonify(bulk_info)


@bp.route('/nav', methods=['GET'])
def buyer_nav():
    nav_html = """
    <h1>Buyer Navigation (Jenna the Freshman)</h1>
    <ul>
      <li><a href="/buyer/ui/textbook-search">Textbook Search</a></li>
      <li><a href="/buyer/ui/price-alerts">My Price Alerts</a></li>
      <li><a href="/buyer/ui/wishlist">My Wishlist</a></li>
    </ul>
    """
    return render_template_string(nav_html)

@bp.route('/ui/textbook-search', methods=['GET'])
def ui_textbook_search():
    sql = "SELECT * FROM textbooks"
    try:
        textbooks = query(sql)
        table_html = "<h1>Textbook Search Results</h1><table border='1'><tr>"
        if textbooks:
            for key in textbooks[0].keys():
                table_html += f"<th>{key}</th>"
            table_html += "</tr>"
            for row in textbooks:
                table_html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            table_html += "</table>"
        else:
            table_html = "<p>No textbooks found.</p>"
        return render_template_string(table_html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/price-alerts', methods=['GET'])
def ui_price_alerts():
    userId = 1
    sql = "SELECT * FROM price_alerts WHERE user_id = ?"
    try:
        alerts = query(sql, [userId])
        html = "<h1>My Price Alerts</h1><table border='1'><tr>"
        if alerts:
            for key in alerts[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in alerts:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No price alerts found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/wishlist', methods=['GET'])
def ui_wishlist():
    userId = 1
    sql = "SELECT * FROM wishlist WHERE user_id = ?"
    try:
        wishlist_items = query(sql, [userId])
        html = "<h1>My Wishlist</h1><table border='1'><tr>"
        if wishlist_items:
            for key in wishlist_items[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in wishlist_items:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>Your wishlist is empty.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")
