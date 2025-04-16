from flask import current_app

def query(sql, params=None):
    cursor = current_app.mysql.get_db().cursor()
    cursor.execute(sql, params or ())
    result = cursor.fetchall()
    cursor.close()
    return result

def execute(sql, params=None):
    conn = current_app.mysql.get_db()
    cursor = conn.cursor()
    cursor.execute(sql, params or ())
    conn.commit()
    cursor.close()