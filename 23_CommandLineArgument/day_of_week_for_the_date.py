import sys
from datetime import datetime

args = sys.argv

if len(args) != 2:
    print(f"Usage: python scriptname.py DD-MM-YYYY")
else:
    date_input = args[1]

    try:
        date_obj = datetime.strptime(date_input, "%d-%m-%Y")

        day = date_obj.strftime('%A')
        print(f"The day of the week for {date_input} is {day}.")
    except ValueError:
        print(f"Invalid date format. Please use DD-MM-YYYY.")
