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

        amount_str = str(amount)

        with get_connection() as conn:
            cur = conn.cursor()
            try:
                cur.execute('BEGIN')
                cur.execute("""UPDATE accounts
                            SET balance = balance - ?
                            WHERE user_id = ? AND account_id = ? AND balance >= ?
                            RETURNING *""",
                            (amount_str, user_id, from_account_id, amount_str))

                updated_from = cur.fetchone()
                if updated_from is None:
                    raise Exception(
                        "Insufficient funds or invalid source account")

                updated_from_dict = dict(updated_from)

                cur.execute("""UPDATE accounts
                            SET balance = balance + ?
                            WHERE user_id = ? AND account_id = ?
                            RETURNING *""",
                            (amount_str, to_user_id, to_account_id, amount_str))

                updated_to = cur.fetchone()
                if updated_to is None:
                    raise Exception("Invalid destination account")
                updated_to_dict = dict(updated_to)

                conn.commit()

                return updated_from_dict, updated_to_dict
            except Exception as e:
                conn.rollback()
                print(f'Transfer failed: {e}')
                return None

    @staticmethod
    def close_account(user_id, account_id):
        '''Soft-close -- keeps history, hides from list_accounts()'''

    @staticmethod
    def validate_money(amount: str) -> Decimal | None:
        '''Normalizes user input to be used by the the core banking logic'''
