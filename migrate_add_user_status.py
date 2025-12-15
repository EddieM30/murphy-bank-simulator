from database import get_connection


def migrate():
    """Add status and closed_at columns to user table"""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(users)")
        col_info = cur.fetchall()

        col_names = [col[1] for col in col_info]
        if 'status' not in col_names:
            cur.execute(
                "ALTER TABLE users ADD COLUMN status TEXT NOT NULL DEFAULT 'active'")
            print('Successfully added status column')
        else:
            print('Status column already exists')

        if 'closed_at' not in col_names:
            cur.execute("ALTER TABLE users ADD COLUMN closed_at TEXT")
            print('Closed_at column added to users')
        else:
            print("closed_at column already exists")


migrate()
