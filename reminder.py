import pandas as pd
from plyer import notification
import webbrowser
from datetime import datetime, time
import pytz
import pywhatkit



def send_notification(name, message,phone_number):
    notification.notify(
        title="Birthday Reminder",
        message=f"It's {name}'s birthday! {message} + Click Her to Wish in ChatApp -{phone_number} ",
        timeout=10,
    )

def send_message(phone_number, custom_message):
    # syntax: phone number with country code, message, hour and minutes

     pywhatkit.sendwhatmsg('+91{phone_number}','{custom_message}', 16, 38),
    


def read_birthday_data(file_path):
    df = pd.read_excel(file_path)
    today = datetime.now(pytz.timezone('Asia/Kolkata')).date()
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
    notification_time = time(12, )  # Set the desired notification time here

    for _, row in df.iterrows():
        birthday = row["Date of Birth"].date()
        if today.month == birthday.month and today.day == birthday.day and current_time >= notification_time:
            name = row["Name"]
            phone_number = row["Phone Number"]
            chat_app = row["Chat App"]
            custom_message = row["Custom Message"]  # Assuming there is a "Custom Message" column in the Excel file
            # chatapplink = row["Chat App Link"]

            send_notification(name,custom_message,phone_number)
            send_message(phone_number, custom_message)

            # send_gift_or_task(name)


if __name__ == "__main__":
    file_path = "C:\\Users\\AK Style\\OneDrive\\Desktop\\Birthday Reminder Python Project\\Birthday-Task Reminder.xlsx"
    read_birthday_data(file_path)


# def send_gift_or_task(name):
#     # Implement your code to send gifts or assign tasks based on the person's birthday
#     print(f"Sending gift or task to {name}...")



