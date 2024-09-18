import os
import re

directory = 'documents'
filenames = os.listdir(directory)

all_emails = []
for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r') as file:
        content = file.read()

    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, content)
    print(emails)
    all_emails.extend(emails)

print(all_emails)
