# db.py
import sqlite3
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def query(sql, params=()):
    db = get_db()
    cur = db.execute(sql, params)
    rows = cur.fetchall()
    cur.close()
    return [dict(row) for row in rows]

def execute(sql, params=()):
    db = get_db()
    cur = db.execute(sql, params)
    db.commit()
    cur.close()
