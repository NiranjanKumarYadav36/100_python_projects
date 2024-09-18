import smtplib
import dotenv, os
from email.mine.multipart import MIMEMultipart
from email.mine.text import MIMEText

dotenv.load_dotenv()

# Step 1: Define the credentials
sender_email = ""
password = os.getenv("GMAIL_PASSWORD")

# Step 2: Initialize the smtp server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)


# Step 3: Construct the Email Object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = sender_email
msg['Subject'] = ""

message_body = """

"""

msg.attach(MIMEText(message_body, 'plain'))

# Step 4: Sent out the email
server.send_message(msg)
server.quit()