import hashlib
from datetime import datetime, timedelta
from database import get_connection


class UserManager:
    @staticmethod
    def create(username: str, last_name: str, first_name: str, password: str, email: str) -> dict:
        """Create new user, returns user info"""
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        created_at = datetime.now().isoformat()
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users (username, last_name, first_name, password, email, created_at)
                        VALUES (?, ?, ?, ?, ?, ?)""", (username, last_name, first_name, password_hash, email, created_at))
            user_id = cur.lastrowid

            return {
                'user_id': user_id,
                'username': username,
                'last_name': last_name,
                'first_name': first_name,
                'email': email
            }

    @staticmethod
    def authenticate(username: str, password: str) -> dict | None:
        # Hash the incoming password
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # query db for user with matching username
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cur.fetchone()
            # Check 1 -- does user exist?
            if user is None:
                return None

            # check 2 -- is user active?
            if user['status'] != 'active':
                return None

            # Check 3 -- do passwords match?
            password_hash = hashlib.sha256(
                password.encode('utf-8')).hexdigest()
            if password_hash == user['password']:
                return {
                    'user_id': user['user_id'],
                    'username': user['username'],
                    'last_name': user['last_name'],
                    'first_name': user['first_name'],
                    'email': user['email']
                }
            # if hashes don't match return None
            return None

    @staticmethod
    def get_by_id(user_id: int) -> dict | None:
        """Look up user info by user_id"""
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user = cur.fetchone()
            if user is None:
                return None

            return {
                'user_id': user['user_id'],
                'username': user['username'],
                'last_name': user['last_name'],
                'first_name': user['first_name'],
                'email': user['email']
            }

    @staticmethod
    def get_by_username(username: str) -> dict | None:
        """Look up user info by username"""
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cur.fetchone()
            if user is None:
                return None

            return {
                'user_id': user['user_id'],
                'username': user['username'],
                'last_name': user['last_name'],
                'first_name': user['first_name'],
                'email': user['email']
            }

    @staticmethod
    def update_email(user_id: int, new_email: str) -> dict | None:
        '''Update email with user_id'''
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            user = cur.fetchone()
            if user is None:
                return None

            cur.execute(
                'UPDATE users SET email = ? WHERE user_id = ?', (new_email, user_id))

            cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            return dict(cur.fetchone())

    @staticmethod
    def update_password(user_id: int, new_password: str) -> dict | None:
        '''Update user password with user_id'''
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            user = cur.fetchone()
            password_hash = hashlib.sha256(
                new_password.encode('utf-8')).hexdigest()
            if user is None:
                return None

            cur.execute(
                'UPDATE users SET password = ? WHERE user_id = ?', (password_hash, user_id))

            cur.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            return dict(cur.fetchone())

    @staticmethod
    def close_account(user_id: int) -> bool:
        """Close account on success and return true, False if error message is needed -- user_id doesn't exist or anything else"""
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("UPDATE users SET status = ?, closed_at = ? WHERE user_id = ?",
                        ('closed', datetime.now().isoformat(), user_id))
            return cur.rowcount > 0

    @staticmethod
    def username_exists(username: str) -> bool:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""SELECT *
                        FROM users
                        WHERE LOWER(username) = LOWER(?)""",
                        (username,))
            result = cur.fetchone()
            if result is None:
                return False
            return True

    @staticmethod
    def email_exists(email: str) -> bool:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""SELECT *
                        FROM users
                        WHERE LOWER(email) = LOWER(?)""",
                        (email,))
            result = cur.fetchone()
            if result:
                return True
            return False
