import pywhatkit as kit
from datetime import datetime

import json
from database import cursor, conn

def send_message():
    cursor.execute("SELECT id, phone, plan, current_day FROM users")
    users = cursor.fetchall()

    for user in users:
        user_id, phone, plan_json, current_day = user
        plan = json.loads(plan_json)

        day_key = f"day_{current_day}"

        if day_key not in plan:
            print(f"✅ User {phone} completed plan")
            continue

        day_data = plan[day_key]

        message = f"📅 Day {current_day} Plan\n\n"

        for topic, tasks in day_data.items():
            message += f"{topic.upper()}:\n"
            for task in tasks:
                message += f" - {task}\n"
            message += "\n"

        print(f"📩 Sending to {phone}")
        print(message)

        # 👉 send WhatsApp here

        # update next day
        cursor.execute(
            "UPDATE users SET current_day=? WHERE id=?",
            (current_day + 1, user_id)
        )

    conn.commit()
