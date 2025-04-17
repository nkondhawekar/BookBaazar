# blueprints/seller.py
from flask import Blueprint, request, jsonify
from backend.db_connection import db
from datetime import datetime
from pymysql.cursors import DictCursor

sellers = Blueprint('seller', __name__, url_prefix='/seller')

# 1. Bulk upload multiple listings for sale
@sellers.route('/listings/bulk-upload', methods=['POST'])
def bulk_upload_listings():
    data = request.get_json()
    listings = data.get('listings')  # Expect a list of listing dicts
    
    if not listings or not isinstance(listings, list):
        return jsonify({'error': 'Listings data is required and must be a list.'}), 400
    
    sql = 'INSERT INTO Listings (seller_id, book_id, price, status, date_listed) VALUES (%s, %s, %s, %s, %s)'
    try:
        cursor = db.get_db().cursor()
        for listing in listings:
            sellerId = listing.get('sellerId')
            bookId = listing.get('bookId')
            price = listing.get('price')
            status = listing.get('status', 'active')
            
            if not all([sellerId, bookId, price]):
                return jsonify({'error': 'Missing fields in one of the listings.'}), 400
            
            cursor.execute(sql, [sellerId, bookId, price, status, datetime.now()])
        
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
    
    sql = 'UPDATE Listings SET status = %s WHERE listing_id = %s'
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
      SELECT l.*, t.title, t.author, t.isbn, t.class_code, t.`condition`
      FROM Listings l
      JOIN Textbooks t ON l.book_id = t.book_id
      WHERE l.seller_id = %s
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [sellerId])
        listings = cursor.fetchall()
        cursor.close()
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5. Retrieve messages for a seller's listing
@sellers.route('/messages/<int:listingId>', methods=['GET'])
def get_listing_messages(listingId):
    sql = 'SELECT * FROM Messages WHERE listing_id = %s ORDER BY timestamp ASC'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [listingId])
        messages = cursor.fetchall()
        cursor.close()
        return jsonify(messages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Retrieve listing analytics (e.g., impressions, views)
@sellers.route('/analytics/<int:listingId>', methods=['GET'])
def listing_analytics(listingId):
    sql = 'SELECT * FROM ListingAnalytics WHERE listing_id = %s'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql, [listingId])
        analytics = cursor.fetchone()
        cursor.close()
        
        if analytics:
            return jsonify(analytics)
        else:
            return jsonify({
                "listing_id": listingId,
                "total_views": 0,
                "clicks": 0,
                "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 7. Promote a listing by paying a fee for higher visibility
@sellers.route('/promote', methods=['POST'])
def promote_listing():
    data = request.get_json()
    listingId = data.get('listingId')
    days = data.get('days', 7)  # Default promotion period: 7 days
    cost = data.get('cost', 5.00)  # Default cost: $5.00
    
    if not listingId:
        return jsonify({'error': 'Listing ID is required.'}), 400
    
    sql = '''
        INSERT INTO Promotions (listing_id, start_date, end_date, cost) 
        VALUES (%s, %s, DATE_ADD(%s, INTERVAL %s DAY), %s)
    '''
    now = datetime.now()
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [listingId, now, now, days, cost])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Listing promoted successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500