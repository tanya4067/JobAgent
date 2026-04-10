from apscheduler.schedulers.background import BackgroundScheduler
from save_user import get_all_users
import json
from datetime import datetime


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

def send_daily_data():
    today = datetime.now().day

    result = fetch_all_data_for_day(today)
    print("Result for funn",result)

    for item in result:
        phone = "7759034535"
        data = item["data"]

        message = f"📅 {item['day']}:\n{data}"

        print(f"Sending to {phone}: {message}")

        # 👉 Replace this with WhatsApp API
        # send_whatsapp(phone, message)