# # blueprints/bookstore.py
# from flask import Blueprint, jsonify
# from backend.db_connection import db
# from db import query, execute

# managers = Blueprint('bookstore', __name__, url_prefix='/bookstore')

# # Book Dashboard
# @managers.route('/trending-books', methods=['GET'])
# def trending_books():
#     sql = """
#       SELECT book_id, COUNT(*) AS total_activity
#       FROM (
#           SELECT book_id FROM listings
#           UNION ALL
#           SELECT book_id FROM wishlist
#       )
#       GROUP BY book_id
#       ORDER BY total_activity DESC
#       LIMIT 10
#     """
#     try:
#         trending = query(sql)
#         return jsonify(trending)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Price Trends 
# @managers.route('/price-trends', methods=['GET'])
# def price_trends():
#     sql = """
#       SELECT book_id, AVG(price) AS average_price
#       FROM listings
#       WHERE status = 'sold'
#       GROUP BY book_id
#     """
#     try:
#         trends = query(sql)
#         return jsonify(trends)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Demand 
# @managers.route('/seasonal-demand', methods=['GET'])
# def seasonal_demand():
#     sql = """
#       SELECT strftime('%Y-%m', created_at) as month, COUNT(*) AS demand_count
#       FROM listings
#       GROUP BY month
#       ORDER BY month
#     """
#     try:
#         demand = query(sql)
#         return jsonify(demand)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# #Availability 
# @managers.route('/availability-metrics', methods=['GET'])
# def availability_metrics():
#     sql = """
#       SELECT book_id, AVG(JULIANDAY(sold_date) - JULIANDAY(created_at)) AS avg_days_to_sell
#       FROM listings
#       WHERE status = 'sold'
#       GROUP BY book_id
#     """
#     try:
#         metrics = query(sql)
#         return jsonify(metrics)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Competitor Benchmarking
# @managers.route('/competitor-benchmark', methods=['GET'])
# def competitor_benchmark():
#     sql = """
#       SELECT 
#         (SELECT COUNT(*) FROM listings WHERE seller_type = 'bookstore') AS bookstore_count,
#         (SELECT COUNT(*) FROM listings WHERE seller_type = 'student') AS student_count
#     """
#     try:
#         benchmark = query(sql)
#         return jsonify(benchmark)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Low/Out-of-Stock Alerts
# @managers.route('/stock-alerts', methods=['GET'])
# def stock_alerts():
#     sql = 'SELECT * FROM inventory_alerts'
#     try:
#         alerts = query(sql)
#         return jsonify(alerts)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# blueprints/manager.py
from flask import Blueprint, jsonify
from backend.db_connection import db

managers = Blueprint('bookstore', __name__, url_prefix='/bookstore')

# Book Dashboard
@managers.route('/trending-books', methods=['GET'])
def trending_books():
    sql = """
      SELECT book_id, COUNT(*) AS total_activity
      FROM (
          SELECT book_id FROM listings
          UNION ALL
          SELECT book_id FROM wishlist
      ) AS combined_data
      GROUP BY book_id
      ORDER BY total_activity DESC
      LIMIT 10
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
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
      FROM listings
      WHERE status = 'sold'
      GROUP BY book_id
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
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
      SELECT DATE_FORMAT(created_at, '%Y-%m') as month, COUNT(*) AS demand_count
      FROM listings
      GROUP BY month
      ORDER BY month
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
        cursor.execute(sql)
        demand = cursor.fetchall()
        cursor.close()
        return jsonify(demand)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Availability 
@managers.route('/availability-metrics', methods=['GET'])
def availability_metrics():
    sql = """
      SELECT book_id, AVG(DATEDIFF(sold_date, created_at)) AS avg_days_to_sell
      FROM listings
      WHERE status = 'sold'
      GROUP BY book_id
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
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
      SELECT 
        (SELECT COUNT(*) FROM listings WHERE seller_type = 'bookstore') AS bookstore_count,
        (SELECT COUNT(*) FROM listings WHERE seller_type = 'student') AS student_count
    """
    try:
        cursor = db.get_db().cursor(dictionary=True)
        cursor.execute(sql)
        benchmark = cursor.fetchall()
        cursor.close()
        return jsonify(benchmark)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Low/Out-of-Stock Alerts
@managers.route('/stock-alerts', methods=['GET'])
def stock_alerts():
    sql = 'SELECT * FROM inventory_alerts'
    try:
        cursor = db.get_db().cursor(dictionary=True)
        cursor.execute(sql)
        alerts = cursor.fetchall()
        cursor.close()
        return jsonify(alerts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500