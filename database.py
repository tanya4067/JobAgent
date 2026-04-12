# database.py

import sqlite3

conn = sqlite3.connect("study_plans.db", check_same_thread=False)
cursor = conn.cursor()



# cursor.execute("""

# DROP TABLE IF EXISTS users
               
# """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT UNIQUE,
    plan TEXT,
    duration_days INTEGER,
    start_date TEXT,
    last_sent_day INTEGER DEFAULT 0
)
""")

conn.commit()