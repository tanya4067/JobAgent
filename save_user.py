import json
from database import conn, cursor

def save_user(phone, plan,duration_days):
    cursor.execute(
        "INSERT INTO users (phone, plan, duration_days) VALUES (?, ?, ?)",
        (phone, json.dumps(plan), duration_days)
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