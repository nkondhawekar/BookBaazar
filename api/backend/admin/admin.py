
# blueprints/admin.py
from flask import Blueprint, request, jsonify, current_app
from backend.db_connection import db
import time
from pymysql.cursors import DictCursor

admins = Blueprint('admin', __name__, url_prefix='/admin')

# 1. View reported users (User Report Dashboard)
@admins.route('/reports/dashboard', methods=['GET'])
def reported_users_dashboard():
    sql = """
       SELECT user_id, COUNT(*) AS report_count
       FROM user_reports
       GROUP BY user_id
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        reports = cursor.fetchall()
        cursor.close()
        return jsonify(reports)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. View flagged listings for review
@admins.route('/flagged-listings', methods=['GET'])
def flagged_listings():
    sql = 'SELECT * FROM Listings WHERE flagged = 1'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        listings = cursor.fetchall()
        cursor.close()
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. Remove a flagged listing
@admins.route('/flagged-listings/<int:listingId>', methods=['DELETE'])
def remove_flagged_listing(listingId):
    # This might mark the listing as removed rather than deleting from DB.
    sql = 'UPDATE Listings SET status = %s WHERE id = %s'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, ["removed", listingId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Flagged listing removed.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4. Check server health (uptime and performance)
@admins.route('/server/health', methods=['GET'])
def server_health():
    uptime = time.time() - current_app.config.get('START_TIME', time.time())
    return jsonify({'status': 'Server is running', 'uptime': uptime})

# 5. Ban a user who has multiple reports
@admins.route('/users/ban', methods=['POST'])
def ban_user():
    data = request.get_json()
    userId = data.get('userId')
    if not userId:
        return jsonify({'error': 'userId is required.'}), 400
    sql = 'UPDATE users SET banned = %s WHERE id = %s'
    try:
        cursor = db.get_db().cursor()
        cursor.execute(sql, [1, userId])
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'User has been banned.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6. Detect spam or duplicate listings
@admins.route('/spam', methods=['GET'])
def detect_spam():
    sql = """
       SELECT title, COUNT(*) AS occurrence
       FROM listings
       GROUP BY title
       HAVING occurrence > 1
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        spam = cursor.fetchall()
        cursor.close()
        return jsonify(spam)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 7. View system logs for diagnostics
@admins.route('/logs', methods=['GET'])
def view_logs():
    sql = 'SELECT * FROM system_logs ORDER BY timestamp DESC'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        logs = cursor.fetchall()
        cursor.close()
        return jsonify(logs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500