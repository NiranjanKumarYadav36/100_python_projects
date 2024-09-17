import yagmail
import dotenv
import os


dotenv.load_dotenv()
password = os.getenv('GMAIL_PASSWORD')
sender_email = 'piyush362002@gmail.com'

yag = yagmail.SMTP(sender_email, password)

body = """
Hi,

I just wanted to say Hi!

Regards
Niranjan
"""

with open('email.txt', 'r') as file:
    to_email = file.readlines()

to_email = [email.strip() for email in to_email]


yag.send(to=to_email,
         subject="Just wanted to say hi",
         contents=body,
         attachments=['file1.txt'])

print("Email sent successfully")
