# blueprints/manager.py
from flask import Blueprint, jsonify
from backend.db_connection import db
from pymysql.cursors import DictCursor

managers = Blueprint('manager', __name__, url_prefix='/manager')  # Changed to 'manager' to match your blueprint registration

# Book Dashboard
@managers.route('/trending-books', methods=['GET'])
def trending_books():
    sql = """
      SELECT book_id, COUNT(*) AS total_activity
      FROM (
          SELECT book_id FROM Listings
          UNION ALL
          SELECT book_id FROM Wishlist
      ) AS combined_data
      GROUP BY book_id
      ORDER BY total_activity DESC
      LIMIT 10
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        trending = cursor.fetchall()
        cursor.close()
        return jsonify(trending)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Price Trends 
@managers.route('/price-trends', methods=['GET'])
def price_trends():
    sql = """
      SELECT book_id, AVG(price) AS average_price
      FROM Listings
      WHERE status = 'sold'
      GROUP BY book_id
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        trends = cursor.fetchall()
        cursor.close()
        return jsonify(trends)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Demand 
@managers.route('/seasonal-demand', methods=['GET'])
def seasonal_demand():
    sql = """
      SELECT DATE_FORMAT(date_listed, '%Y-%m') as month, COUNT(*) AS demand_count
      FROM Listings
      GROUP BY month
      ORDER BY month
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        demand = cursor.fetchall()
        cursor.close()
        return jsonify(demand)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Availability 
@managers.route('/availability-metrics', methods=['GET'])
def availability_metrics():
    sql = """
      SELECT l.book_id, AVG(DATEDIFF(s.date_purchased, l.date_listed)) AS avg_days_to_sell
      FROM Listings l
      JOIN SalesTransactions s ON l.listing_id = s.listing_id
      WHERE l.status = 'sold'
      GROUP BY l.book_id
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        metrics = cursor.fetchall()
        cursor.close()
        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Competitor Benchmarking
@managers.route('/competitor-benchmark', methods=['GET'])
def competitor_benchmark():
    sql = """
      SELECT book_id, bookstore_price, student_resale_avg_price
      FROM CompetitorBenchmarking
    """
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        benchmark = cursor.fetchall()
        cursor.close()
        return jsonify(benchmark)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Low/Out-of-Stock Alerts
@managers.route('/stock-alerts', methods=['GET'])
def stock_alerts():
    sql = 'SELECT * FROM InventoryAlerts'
    try:
        cursor = db.get_db().cursor(DictCursor)
        cursor.execute(sql)
        alerts = cursor.fetchall()
        cursor.close()
        return jsonify(alerts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500