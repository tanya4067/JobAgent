from apscheduler.schedulers.background import BackgroundScheduler
from save_user import get_all_users
import json
from datetime import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv
import time
import sqlite3

conn = sqlite3.connect("study_plans.db", check_same_thread=False)
cursor = conn.cursor()

load_dotenv()

TWILIO_ACCOUNT_SID=os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def fetch_all_data_for_day():
    users = get_all_users()
    result = []

    for user in users:
        user_id = user[0]
        phone = user[1]
        plan_json = user[2]
        duration_days = user[3]
        start_date = datetime.fromisoformat(user[4])
        last_sent_day = user[5]

        plan = json.loads(plan_json)

        current_day = (datetime.now() - start_date).days + 1

        if current_day > duration_days:
            continue

        if current_day <= last_sent_day:
            continue

        day_key = f"day_{current_day}"

        if day_key in plan:
            result.append({
                "user_id": user_id,
                "phone": phone,
                "day": day_key,
                "data": plan[day_key],
                "current_day": current_day
            })

    return result

def format_plan(data):
    message = ""

    for topic, tasks in data.items():
        message += f"📌 {topic.capitalize()}:\n"

        for i, task in enumerate(tasks, 1):
            message += f"   {i}. {task}\n"

        message += "\n"

    return message.strip()

def send_daily_data():
    result = fetch_all_data_for_day()

    for item in result:
        formatted_data = format_plan(item["data"])

        text_message = f"📅 {item['day'].upper()}:\n\n{formatted_data}"

        client.messages.create(
            body=text_message,
            from_='whatsapp:+14155238886',
            to='whatsapp:+91' + item["phone"]
        )

        cursor.execute(
            "UPDATE users SET last_sent_day = ? WHERE id = ?",
            (item["current_day"], item["user_id"])
        )
        conn.commit()