# db.py

import sqlite3
from flask import g

DATABASE = 'hospital.db'

def get_db():
    """
    Get the database connection. If the connection does not exist, it will be created.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Return rows that behave like dictionaries
    return g.db

def close_db(e=None):
    """
    Close the database connection.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """
    Initialize the database. This function should be called to create the initial tables.
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Additional functions for database operations can be added here.
# For example, functions to insert, update, or query data.
