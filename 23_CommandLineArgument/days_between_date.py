import sys
from datetime import datetime

args = sys.argv
# print(args)

if len(args) != 3:
    print(f"Usage: python scriptname.py DD-MM-YYYY DD-MM-YYYY")
else:
    start_date = args[1]
    end_date = args[2]
    try:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')

        difference = start_date - end_date
        # print(difference)

        days = difference.days
        print(f"The difference in days is {days}")
    except ValueError:
        print(f"Invalid date format.Please use DD-MM-YYYY.")
