# # blueprints/seller.py
# from flask import Blueprint, request, jsonify
# from backend.db_connection import db
# from db import query, execute
# from datetime import datetime

# sellers = Blueprint('seller', __name__, url_prefix='/seller')

# # 1. Bulk upload multiple listings for sale
# @sellers.route('/listings/bulk-upload', methods=['POST'])
# def bulk_upload_listings():
#     data = request.get_json()
#     listings = data.get('listings')  # Expect a list of listing dicts
#     if not listings or not isinstance(listings, list):
#         return jsonify({'error': 'Listings data is required and must be a list.'}), 400
#     sql = 'INSERT INTO listings (seller_id, title, description, price, condition, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
#     try:
#         for listing in listings:
#             sellerId = listing.get('sellerId')
#             title = listing.get('title')
#             description = listing.get('description')
#             price = listing.get('price')
#             condition = listing.get('condition')
#             status = listing.get('status', 'available')
#             created_at = datetime.now()
#             if not all([sellerId, title, description, price, condition]):
#                 return jsonify({'error': 'Missing fields in one of the listings.'}), 400
#             execute(sql, [sellerId, title, description, price, condition, status, created_at])
#         return jsonify({'message': 'Listings uploaded successfully.'}), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # 2. Get price recommendation for a listing based on sales data
# @sellers.route('/price-recommendation/<int:listingId>', methods=['GET'])
# def price_recommendation(listingId):
#     # In a real implementation, you would query historical data to provide a recommendation.
#     # Here, we return a dummy value.
#     recommendation = {
#         "listingId": listingId,
#         "recommended_price": 25.99,
#         "message": "Based on historical data, a competitive price is around $25.99."
#     }
#     return jsonify(recommendation)

# # 3. Update a listing status (e.g., mark as sold or removed)
# @sellers.route('/listings/<int:listingId>', methods=['PUT'])
# def update_listing_status(listingId):
#     data = request.get_json()
#     status = data.get('status')
#     if not status:
#         return jsonify({'error': 'Status is required.'}), 400
#     sql = 'UPDATE listings SET status = ? WHERE id = ?'
#     try:
#         execute(sql, [status, listingId])
#         return jsonify({'message': 'Listing updated successfully.'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # 4. Retrieve all listings for the seller (with average ratings, etc.)
# @sellers.route('/listings', methods=['GET'])
# def get_seller_listings():
#     sellerId = request.args.get('sellerId')
#     if not sellerId:
#         return jsonify({'error': 'sellerId query parameter is required.'}), 400
#     sql = """
#       SELECT l.*,
#              (SELECT AVG(r.rating) FROM reviews r WHERE r.listing_id = l.id) AS average_rating
#       FROM listings l
#       WHERE l.seller_id = ?
#     """
#     try:
#         listings = query(sql, [sellerId])
#         return jsonify(listings)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # 5. Retrieve messages for a seller’s listing
# @sellers.route('/messages/<int:listingId>', methods=['GET'])
# def get_listing_messages(listingId):
#     sql = 'SELECT * FROM messages WHERE listing_id = ? ORDER BY sent_at ASC'
#     try:
#         messages = query(sql, [listingId])
#         return jsonify(messages)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # 6. Retrieve listing analytics (e.g., impressions, views)
# @sellers.route('/analytics', methods=['GET'])
# def listing_analytics():
#     # Return dummy analytics data; in a real app, query your analytics/statistics table
#     analytics = {
#         "total_impressions": 150,
#         "total_views": 80,
#         "most_viewed_listing": 123,
#         "message": "Analytics data retrieved successfully."
#     }
#     return jsonify(analytics)

# # 7. Promote a listing by paying a fee for higher visibility
# @sellers.route('/promote', methods=['POST'])
# def promote_listing():
#     data = request.get_json()
#     listingId = data.get('listingId')
#     if not listingId:
#         return jsonify({'error': 'Listing ID is required.'}), 400
#     # In a real implementation, update the listing to mark it for promotion and process payment.
#     sql = 'UPDATE listings SET promoted = 1 WHERE id = ?'
#     try:
#         execute(sql, [listingId])
#         return jsonify({'message': 'Listing promoted successfully.'})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# blueprints/seller.py
from flask import Blueprint, request, jsonify
from backend.db_connection import db
from datetime import datetime

sellers = Blueprint('seller', __name__, url_prefix='/seller')

# 1. Bulk upload multiple listings for sale
@sellers.route('/listings/bulk-upload', methods=['POST'])
def bulk_upload_listings():
    data = request.get_json()
    listings = data.get('listings')  # Expect a list of listing dicts
    if not listings or not isinstance(listings, list):
        return jsonify({'error': 'Listings data is required and must be a list.'}), 400
    sql = 'INSERT INTO listings (seller_id, title, description, price, condition, status, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    try:
        cursor = db.get_db().cursor()
        for listing in listings:
            sellerId = listing.get('sellerId')
            title = listing.get('title')
            description = listing.get('description')
            price = listing.get('price')
            condition = listing.get('condition')
            status = listing.get('status', 'available')
            created_at = datetime.now()
            if not all([sellerId, title, description, price, condition]):
                return jsonify({'error': 'Missing fields in one of the listings.'}), 400
            cursor.execute(sql, [sellerId, title, description, price, condition, status, created_at])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Listings uploaded successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. Get price recommendation for a listing based on sales data
@sellers.route('/price-recommendation/<int:listingId>', methods=['GET'])
def price_recommendation(listingId):
    # In a real implementation, you would query historical data to provide a recommendation.
    # Here, we return a dummy value.
    recommendation = {
        "listingId": listingId,
        "recommended_price": 25.99,
        "message": "Based on historical data, a competitive price is around $25.99."
    }
    return jsonify(recommendation)

# 3. Update a listing status (e.g., mark as sold or removed)
@sellers.route('/listings/<int:listingId>', methods=['PUT'])
def update_listing_status(listingId):
    data = request.get_json()
    status = data.get('status')
    if not status:
        return jsonify({'error': 'Status is required.'}), 400
    sql = 'UPDATE listings SET status = %s WHERE id = %s'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [status, listingId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Listing updated successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4. Retrieve all listings for the seller (with average ratings, etc.)
@sellers.route('/listings', methods=['GET'])
def get_seller_listings():
    sellerId = request.args.get('sellerId')
    if not sellerId:
        return jsonify({'error': 'sellerId query parameter is required.'}), 400
    sql = """
      SELECT l.*,
             (SELECT AVG(r.rating) FROM reviews r WHERE r.listing_id = l.id) AS average_rating
      FROM listings l
      WHERE l.seller_id = %s
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
        cursor.execute(sql, [sellerId])
        listings = cursor.fetchall()
        cursor.close()
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5. Retrieve messages for a seller's listing
@sellers.route('/messages/<int:listingId>', methods=['GET'])
def get_listing_messages(listingId):
    sql = 'SELECT * FROM messages WHERE listing_id = %s ORDER BY sent_at ASC'
    try:
        cursor = db.get_db().cursor(dictionary=True)
        cursor.execute(sql, [listingId])
        messages = cursor.fetchall()
        cursor.close()
        return jsonify(messages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Retrieve listing analytics (e.g., impressions, views)
@sellers.route('/analytics', methods=['GET'])
def listing_analytics():
    # Return dummy analytics data; in a real app, query your analytics/statistics table
    analytics = {
        "total_impressions": 150,
        "total_views": 80,
        "most_viewed_listing": 123,
        "message": "Analytics data retrieved successfully."
    }
    return jsonify(analytics)

# 7. Promote a listing by paying a fee for higher visibility
@sellers.route('/promote', methods=['POST'])
def promote_listing():
    data = request.get_json()
    listingId = data.get('listingId')
    if not listingId:
        return jsonify({'error': 'Listing ID is required.'}), 400
    # In a real implementation, update the listing to mark it for promotion and process payment.
    sql = 'UPDATE listings SET promoted = %s WHERE id = %s'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [1, listingId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Listing promoted successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500