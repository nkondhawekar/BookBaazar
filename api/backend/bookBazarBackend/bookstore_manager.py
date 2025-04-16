from flask import Blueprint, render_template_string, jsonify
from db import query

bp = Blueprint('bookstore', __name__, url_prefix='/bookstore')


@bp.route('/trending-books', methods=['GET'])
def trending_books():
    sql = """
      SELECT book_id, COUNT(*) AS total_activity
      FROM (
          SELECT book_id FROM listings
          UNION ALL
          SELECT book_id FROM wishlist
      )
      GROUP BY book_id
      ORDER BY total_activity DESC
      LIMIT 10
    """
    try:
        trending = query(sql)
        return jsonify(trending)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/price-trends', methods=['GET'])
def price_trends():
    sql = """
      SELECT book_id, AVG(price) AS average_price
      FROM listings
      WHERE status = 'sold'
      GROUP BY book_id
    """
    try:
        trends = query(sql)
        return jsonify(trends)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/seasonal-demand', methods=['GET'])
def seasonal_demand():
    sql = """
      SELECT strftime('%Y-%m', created_at) as month, COUNT(*) AS demand_count
      FROM listings
      GROUP BY month
      ORDER BY month
    """
    try:
        demand = query(sql)
        return jsonify(demand)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/nav', methods=['GET'])
def bookstore_nav():
    nav_html = """
    <h1>Bookstore Navigation (Alfred the Campus Bookstore Manager)</h1>
    <ul>
      <li><a href="/bookstore/ui/trending-books">Trending Books Dashboard</a></li>
      <li><a href="/bookstore/ui/price-trends">Price Trends Analysis</a></li>
      <li><a href="/bookstore/ui/seasonal-demand">Seasonal Demand Insights</a></li>
    </ul>
    """
    return render_template_string(nav_html)

@bp.route('/ui/trending-books', methods=['GET'])
def ui_trending_books():
    sql = """
      SELECT book_id, COUNT(*) AS total_activity
      FROM (
          SELECT book_id FROM listings
          UNION ALL
          SELECT book_id FROM wishlist
      )
      GROUP BY book_id
      ORDER BY total_activity DESC
      LIMIT 10
    """
    try:
        trending = query(sql)
        html = "<h1>Trending Books Dashboard</h1><table border='1'><tr>"
        if trending:
            for key in trending[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in trending:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No trending data found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/price-trends', methods=['GET'])
def ui_price_trends():
    sql = """
      SELECT book_id, AVG(price) AS average_price
      FROM listings
      WHERE status = 'sold'
      GROUP BY book_id
    """
    try:
        trends = query(sql)
        html = "<h1>Price Trends Analysis</h1><table border='1'><tr>"
        if trends:
            for key in trends[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in trends:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No price trend data found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")

@bp.route('/ui/seasonal-demand', methods=['GET'])
def ui_seasonal_demand():
    sql = """
      SELECT strftime('%Y-%m', created_at) as month, COUNT(*) AS demand_count
      FROM listings
      GROUP BY month
      ORDER BY month
    """
    try:
        demand = query(sql)
        html = "<h1>Seasonal Demand Insights</h1><table border='1'><tr>"
        if demand:
            for key in demand[0].keys():
                html += f"<th>{key}</th>"
            html += "</tr>"
            for row in demand:
                html += "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
            html += "</table>"
        else:
            html = "<p>No seasonal demand data found.</p>"
        return render_template_string(html)
    except Exception as e:
        return render_template_string(f"<p>Error: {str(e)}</p>")
