import smtplib
import schedule
import time
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Email details
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = SENDER_EMAIL  # You can send it to yourself
PASSWORD = os.getenv("PASSWORD")

def send_reminder():
    subject = "Budget Update Reminder 📊"
    body = """Hello,  
Don't forget to update your budget list today!💰  
Track your expenses and savings.  
Click here to update: https://docs.google.com/spreadsheets/d/14PrQKtCEQqiStS4YT-yiZ6l7K2vjM-0jFuZpxPzO18I/edit?pli=1&gid=582856110#gid=582856110 

Have a great day! 😊
    """

    # Create email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Budget reminder sent! ✅")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule the reminder (every Monday at 9 AM)
schedule.every().monday.at("09:00").do(send_reminder)

# Keep running in the background
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
