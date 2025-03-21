import pandas as pd
from datetime import datetime
import random
import smtplib

# Load today's date
today = (datetime.now().month, datetime.now().day)

# Read the CSV and create a dictionary
data = pd.read_csv('birthdays.csv')
birthdays_dict = {
    (row.month, row.day): row
    for (index, row) in data.iterrows()
}

# Check if today matches a birthday
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person['name']
    email = birthday_person['email']

    # Pick a random letter
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path, 'r') as letter_file:
        content = letter_file.read()

    # Replace [NAME] with the actual name
    personalized_letter = content.replace("[NAME]", name)

    # Email configuration
    my_email = "anisruszanna08@gmail.com"
    password = "ghqbvznlilcqjigt"
    # Setup the connection
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Encrypt connection
        connection.login(user=my_email, password=password)
        # Send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
        )
