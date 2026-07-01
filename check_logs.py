import sqlite3
from werkzeug.security import generate_password_hash

db = sqlite3.connect('app.db')
c = db.cursor()

# Create a test user in login_logs to establish that credentials work
# Actually, the app uses a simple admin username/password from config
# Let's just verify the app is working by checking recent entries

print("Recent login logs:")
c.execute("SELECT * FROM login_logs ORDER BY timestamp DESC LIMIT 5")
logs = c.fetchall()
for log in logs:
    print(f"  {log}")

db.close()
