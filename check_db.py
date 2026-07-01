import sqlite3

db = sqlite3.connect('app.db')
c = db.cursor()

# List all tables
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")

# Check login_logs table
try:
    c.execute("SELECT COUNT(*) FROM login_logs")
    count = c.fetchone()[0]
    print(f"\nLogin logs count: {count}")
except Exception as e:
    print(f"Error querying login_logs: {e}")

db.close()
