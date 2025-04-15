# blueprints/admin.py
from flask import Blueprint, request, jsonify, current_app
from db import query, execute
import time

bp = Blueprint('admin', __name__, url_prefix='/admin')

# 1. View reported users (User Report Dashboard)
@bp.route('/reports/dashboard', methods=['GET'])
def reported_users_dashboard():
    sql = """
       SELECT user_id, COUNT(*) AS report_count
       FROM user_reports
       GROUP BY user_id
    """
    try:
        reports = query(sql)
        return jsonify(reports)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. View flagged listings for review
@bp.route('/flagged-listings', methods=['GET'])
def flagged_listings():
    sql = 'SELECT * FROM listings WHERE flagged = 1'
    try:
        listings = query(sql)
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. Remove a flagged listing
@bp.route('/flagged-listings/<int:listingId>', methods=['DELETE'])
def remove_flagged_listing(listingId):
    # This might mark the listing as removed rather than deleting from DB.
    sql = 'UPDATE listings SET status = "removed" WHERE id = ?'
    try:
        execute(sql, [listingId])
        return jsonify({'message': 'Flagged listing removed.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4. Check server health (uptime and performance)
@bp.route('/server/health', methods=['GET'])
def server_health():
    uptime = time.time() - current_app.config.get('START_TIME', time.time())
    return jsonify({'status': 'Server is running', 'uptime': uptime})

# 5. Ban a user who has multiple reports
@bp.route('/users/ban', methods=['POST'])
def ban_user():
    data = request.get_json()
    userId = data.get('userId')
    if not userId:
        return jsonify({'error': 'userId is required.'}), 400
    sql = 'UPDATE users SET banned = 1 WHERE id = ?'
    try:
        execute(sql, [userId])
        return jsonify({'message': 'User has been banned.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Detect spam or duplicate listings
@bp.route('/spam', methods=['GET'])
def detect_spam():
    sql = """
       SELECT title, COUNT(*) AS occurrence
       FROM listings
       GROUP BY title
       HAVING occurrence > 1
    """
    try:
        spam = query(sql)
        return jsonify(spam)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 7. View system logs for diagnostics
@bp.route('/logs', methods=['GET'])
def view_logs():
    sql = 'SELECT * FROM system_logs ORDER BY timestamp DESC'
    try:
        logs = query(sql)
        return jsonify(logs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
