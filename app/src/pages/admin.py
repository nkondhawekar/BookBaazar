
# blueprints/admin.py
from flask import Blueprint, request, jsonify, render_template_string, current_app
from db import query, execute
import time

bp = Blueprint('admin', __name__, url_prefix='/admin')

# === API Endpoints for Admin (Rachel) ===

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

@bp.route('/flagged-listings', methods=['GET'])
def flagged_listings():
    sql = 'SELECT * FROM listings WHERE flagged = 1'
    try:
        listings = query(sql)
        return jsonify(listings)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/flagged-listings/<int:listingId>', methods=['DELETE'])
def remove_flagged_listing(listingId):
    sql = 'UPDATE listings SET status = "removed" WHERE id = ?'
    try:
        execute(sql, [listingId])
        return jsonify({'message': 'Flagged listing removed.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/server/health', methods=['GET'])
def server_health():
    uptime = time.time() - current_app.config.get('START_TIME', time.time())
    return jsonify({'status': 'Server is running', 'uptime': uptime})

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

@bp.route('/logs', methods=['GET'])
def view_logs():
    sql = 'SELECT * FROM system_logs ORDER BY timestamp DESC'
    try:
        logs = query(sql)
        return jsonify(logs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# === UI / Navigation Endpoints for Admin ===

@bp.route('/nav', methods=['GET'])
def admin_nav():
    nav_html = """
    <h1>Admin Navigation (Rachel the Administrator)</h1>
    <ul>
      <li><a href="/admin/ui/reported-users">Reported Users Dashboard</a></li>
      <li><a href="/admin/ui/flagged-listings">Flagged Listings Review</a></li>
      <li><a href="/admin/ui/system-logs">System Logs</a></li>
    </ul>
    """
    return render_template_string(nav_html)

@bp.route('/ui/reported-users', methods=['GET'])
def ui_reported_users():
    sql = """
       SELECT user_id, COUNT(*) AS report_count
       FROM user_reports
       GROUP BY user_id
    """
    try:
        reports = query(sql)
        html = "<h1>Reported Users Dashboard</h1><table border='1'><tr>"
        if reports:
            for key in reports[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in reports:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No reports found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/flagged-listings', methods=['GET'])
def ui_flagged_listings():
    sql = 'SELECT * FROM listings WHERE flagged = 1'
    try:
        listings = query(sql)
        html = "<h1>Flagged Listings Review</h1><table border='1'><tr>"
        if listings:
            for key in listings[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in listings:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No flagged listings found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/system-logs', methods=['GET'])
def ui_system_logs():
    sql = 'SELECT * FROM system_logs ORDER BY timestamp DESC'
    try:
        logs = query(sql)
        html = "<h1>System Logs</h1><table border='1'><tr>"
        if logs:
            for key in logs[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in logs:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No system logs found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")
