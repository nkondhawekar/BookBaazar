
# blueprints/seller.py
from flask import Blueprint, request, jsonify, render_template_string
from db import query, execute
from datetime import datetime

bp = Blueprint('seller', __name__, url_prefix='/seller')

# === API Endpoints for Seller (Adam) ===

@bp.route('/listings/bulk-upload', methods=['POST'])
def bulk_upload_listings():
    data = request.get_json()
    listings = data.get('listings')
    if not listings or not isinstance(listings, list):
        return jsonify({'error': 'Listings data is required and must be a list.'}), 400
    sql = 'INSERT INTO listings (seller_id, title, description, price, condition, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
    try:
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
            execute(sql, [sellerId, title, description, price, condition, status, created_at])
        return jsonify({'message': 'Listings uploaded successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/price-recommendation/<int:listingId>', methods=['GET'])
def price_recommendation(listingId):
    recommendation = {
        "listingId": listingId,
        "recommended_price": 25.99,
        "message": "Based on historical data, a competitive price is around $25.99."
    }
    return jsonify(recommendation)

@bp.route('/listings/<int:listingId>', methods=['PUT'])
def update_listing_status(listingId):
    data = request.get_json()
    status = data.get('status')
    if not status:
        return jsonify({'error': 'Status is required.'}), 400
    sql = 'UPDATE listings SET status = ? WHERE id = ?'
    try:
        execute(sql, [status, listingId])
        return jsonify({'message': 'Listing updated successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/listings', methods=['GET'])
def get_seller_listings():
    sellerId = request.args.get('sellerId')
    if not sellerId:
        return jsonify({'error': 'sellerId query parameter is required.'}), 400
    sql = """
      SELECT l.*,
             (SELECT AVG(r.rating) FROM reviews r WHERE r.listing_id = l.id) AS average_rating
      FROM listings l
      WHERE l.seller_id = ?
    """
    try:
        listings = query(sql, [sellerId])
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/messages/<int:listingId>', methods=['GET'])
def get_listing_messages(listingId):
    sql = 'SELECT * FROM messages WHERE listing_id = ? ORDER BY sent_at ASC'
    try:
        messages = query(sql, [listingId])
        return jsonify(messages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/analytics', methods=['GET'])
def listing_analytics():
    analytics = {
        "total_impressions": 150,
        "total_views": 80,
        "most_viewed_listing": 123,
        "message": "Analytics data retrieved successfully."
    }
    return jsonify(analytics)

@bp.route('/promote', methods=['POST'])
def promote_listing():
    data = request.get_json()
    listingId = data.get('listingId')
    if not listingId:
        return jsonify({'error': 'Listing ID is required.'}), 400
    sql = 'UPDATE listings SET promoted = 1 WHERE id = ?'
    try:
        execute(sql, [listingId])
        return jsonify({'message': 'Listing promoted successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# === UI / Navigation Endpoints for Seller ===

@bp.route('/nav', methods=['GET'])
def seller_nav():
    nav_html = """
    <h1>Seller Navigation (Adam the Graduating Senior)</h1>
    <ul>
      <li><a href="/seller/ui/seller-listings">My Listings</a></li>
      <li><a href="/seller/ui/price-recommendation">Price Recommendation</a></li>
      <li><a href="/seller/ui/analytics">Listing Analytics</a></li>
    </ul>
    """
    return render_template_string(nav_html)

@bp.route('/ui/seller-listings', methods=['GET'])
def ui_seller_listings():
    # For demonstration, assume sellerId=1
    sellerId = 1
    sql = """
      SELECT l.*,
             (SELECT AVG(r.rating) FROM reviews r WHERE r.listing_id = l.id) AS average_rating
      FROM listings l
      WHERE l.seller_id = ?
    """
    try:
        listings = query(sql, [sellerId])
        html = "<h1>My Listings</h1><table border='1'><tr>"
        if listings:
            for key in listings[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in listings:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No listings found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/price-recommendation', methods=['GET'])
def ui_price_recommendation():
    # For demonstration, assume listingId=1
    listingId = 1
    recommendation = {
        "listingId": listingId,
        "recommended_price": 25.99,
        "message": "Based on historical data, a competitive price is around $25.99."
    }
    html = f"""
    <h1>Price Recommendation for Listing {listingId}</h1>
    <p>Recommended Price: {recommendation['recommended_price']}</p>
    <p>{recommendation['message']}</p>
    """
    return render_template_string(html)

@bp.route('/ui/analytics', methods=['GET'])
def ui_analytics():
    analytics = {
        "total_impressions": 150,
        "total_views": 80,
        "most_viewed_listing": 123,
        "message": "Analytics data retrieved successfully."
    }
    html = "<h1>Listing Analytics</h1><ul>"
    for key, value in analytics.items():
        html += f"<li>{key}: {value}</li>"
    html += "</ul>"
    return render_template_string(html)
