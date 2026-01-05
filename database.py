'''
Create database tables based on GitHub user data.
'''

import sqlite3 # Library for SQLite database operations
from config import DB_URL # Import database URL from config.py


def db_conn():
    '''
    Connect to database
    '''
    conn = sqlite3.connect(DB_URL) # conn contains the connection object
    return conn # Return the connection object

def create_tables():
    conn = db_conn()# Get database connection object
    cursor = conn.cursor() # Create a cursor object to execute SQL commands

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                   id
                   username
                   name
                   location
                   blog
                   followers
                   following
                   public_repos
                   avatar_url
                   created_at
                   updated__at
                   fetched_at)
                   ''') # Create users table if it doesn't exist
