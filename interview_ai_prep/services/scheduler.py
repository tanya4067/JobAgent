from apscheduler.schedulers.background import BackgroundScheduler
from save_user import get_all_users
import json
from datetime import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv
import time

load_dotenv()

TWILIO_ACCOUNT_SID=os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def fetch_all_data_for_day(day: int):
    users = get_all_users()
    result = []

    for user in users:
        user_id = user[0]
        phone = user[1]
        plan_json = user[2]

        plan = json.loads(plan_json)
        day_key = f'day_{day}'

        if day_key in plan:
            result.append({
                "user_id": user_id,
                "phone": phone,
                "day": day_key,
                "data": plan[day_key]
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

    i=1
    while(fetch_all_data_for_day(i)!=[]):
        result=fetch_all_data_for_day(i)
        for item in result:
            data = item["data"]
            formatted_data = format_plan(data)
            text_message = f"📅 {item['day']}:\n{formatted_data}"
            
            message = client.messages.create(
                body=text_message,
                from_='whatsapp:+14155238886',
                to='whatsapp:+917759034535'
            )
            time.sleep(86400)
        i+=1