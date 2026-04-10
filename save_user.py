import json
from database import conn, cursor

def save_user(phone, plan):
    cursor.execute(
        "INSERT INTO users (phone, plan, current_day) VALUES (?, ?, ?)",
        (phone, json.dumps(plan), 1)
    )
    conn.commit()

def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_day(user_id, new_day):
    cursor.execute(
        "UPDATE users SET current_day=? WHERE id=?",
        (new_day, user_id)
    )
    conn.commit()