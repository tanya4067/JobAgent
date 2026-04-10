# database.py

import sqlite3

conn = sqlite3.connect("study_plans.db", check_same_thread=False)
cursor = conn.cursor()



cursor.execute("""

DROP TABLE IF EXISTS users
               
""")
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone TEXT,
    plan TEXT,
    current_day INTEGER
)
""")

conn.commit()