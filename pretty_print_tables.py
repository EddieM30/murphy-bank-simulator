# pretty_print_db.py
import sqlite3
from tabulate import tabulate

DB_NAME = "bank.db"


def print_all_tables():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Get list of all tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    if not tables:
        print("No tables found in the database.")
        return

    for table_row in tables:
        table_name = table_row[0]
        print(f"\n{'='*20} {table_name.upper()} {'='*20}")

        # Get all rows from this table
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()

        if rows:
            # Convert rows to list of dicts for tabulate
            headers = rows[0].keys()
            table_data = [dict(row) for row in rows]
            print(tabulate(table_data, headers="keys", tablefmt="pretty"))
        else:
            print("   (empty table)")

    conn.close()


if __name__ == "__main__":
    print_all_tables()
