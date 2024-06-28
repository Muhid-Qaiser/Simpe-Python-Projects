import smtplib
import datetime as dt
import pandas
import random

PASSWORD = 'vgrumgyfhuwjooov'
EMAIL = 'joemom7860@gmail.com'

current_date = dt.datetime.now()
month = current_date.month
day = current_date.day
today = (month, day)

birthday_dataframe = pandas.read_csv('birthdays.csv')

birthdays_dict = {(row.month, row.day): row for (index, row) in birthday_dataframe.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    to_email = birthday_person.email
    letter_number = random.randint(1, 3)

    with open(f'letter_templates/letter_{letter_number}.txt') as letter_file:
        letter = letter_file.read()
        letter = letter.replace('[NAME]', birthday_person.name)
        letter = letter.replace('Angela', 'Genji Main')

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=f'Subject: Happy Birthday \n\n{letter}')
