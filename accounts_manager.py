from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from database import get_connection


class AccountsManager():
    @staticmethod
    def list_account(user_id: int) -> list[dict]:
        """Return all active accounts belonging to user_id"""

        # retrive accounts by user_id in descending ORDER
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                'SELECT * FROM accounts WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
            accounts = cur.fetchall()
        # use a for loop to list all account in dicts
            accounts_list = [dict(row) for row in accounts]
            return accounts_list

    @staticmethod
    def create_account(user_id: int, account_type: str) -> dict:
        """Create one new account (checking, savings, etc.) one method infinitly extensible"""
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO accounts (user_id, account_type, created_at) VALUES (?, ?, ?)",
                        (user_id, account_type, datetime.now().isoformat()))
            account_id = cur.lastrowid

            return {
                'account_id': account_id,
                'user_id': user_id,
                'account_type': account_type
            }

    @staticmethod
    def get_account(user_id: int, account_id: int) -> dict | None:
        """Single source of truth -- used by everything else"""
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM accounts WHERE user_id = ? AND account_id = ?", (user_id, account_id))
            account = cur.fetchone()
            if account is None:
                return None
            return dict(account)

    @staticmethod
    def show_balance(user_id: int, account_id: int) -> Decimal:
        """Show balance of a single account"""
        account = AccountsManager.get_account(user_id, account_id)
        return Decimal(account['balance'])

    @staticmethod
    def deposit(user_id: int, account_id: int, amount: Decimal) -> dict | None:
        """Deposits money into users account"""
        account = AccountsManager.get_account(user_id, account_id)
        curr_balance = Decimal(account['balance'])
        updated_balance = curr_balance + amount
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE accounts 
                        SET balance = ? 
                        WHERE user_id = ? AND account_id = ? 
                        RETURNING *
                        ''', (str(updated_balance), user_id, account_id))
            row = cur.fetchone()

        return dict(row) if row else None

    @staticmethod
    def withdraw(user_id, account_id, amount):
        '''Withdraw money from user account'''
        account = AccountsManager.get_account(user_id, account_id)
        curr_balance = Decimal(account['balance'])
        updated_balance = curr_balance - amount
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE accounts 
                        SET balance = ? 
                        WHERE user_id = ? AND account_id = ? 
                        RETURNING *
                        ''', (str(updated_balance), user_id, account_id))
            row = cur.fetchone()

        return dict(row) if row else None

    @staticmethod
    def transfer(user_id, from_account_id, to_account_id, to_user_id, amount):
        from_account = AccountsManager.get_account(user_id, from_account_id)
        to_account = AccountsManager.get_account(to_user_id, to_account_id)
        from_account_balance = Decimal(from_account['balance'])
        to_account_balance = Decimal(to_account['balance'])
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""UPDATE
                        SET balance = ?
                        WHERE user_id = ? AND account_id = ?
                        RETURNING *""",
                        (str(from_account_balance - amount), user_id, from_account_id))
            sent_from = dict(cur.fetchone())
            cur.execute("""UPDATE
                        SET balance = ?
                        WHERE user_id = ? AND account_id = ?
                        RETURNING *""",
                        (str(to_account_balance + amount), to_user_id, to_account_id))
            reciever = dict(cur.fetchone())

        return sent_from, reciever

    @staticmethod
    def close_account(user_id, account_id):
        '''Soft-close -- keeps history, hides from list_accounts()'''

    @staticmethod
    def validate_money(amount: str) -> Decimal | None:
        '''Normalizes user input to be used by the the core banking logic'''
