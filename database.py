import sqlite3
from datetime import datetime
import hashlib

class Database:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (username TEXT PRIMARY KEY, 
                    password TEXT,
                    email TEXT,
                    created_at TIMESTAMP)''')
        conn.commit()
        conn.close()
    
    def make_hash(self, password):
        return hashlib.sha256(str.encode(password)).hexdigest()
    
    def check_login(self, username, password):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?',
                  (username, self.make_hash(password)))
        result = c.fetchone()
        conn.close()
        return result is not None
    
    def add_user(self, username, password, email):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users VALUES (?,?,?,?)',
                     (username, self.make_hash(password), email, datetime.now()))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
