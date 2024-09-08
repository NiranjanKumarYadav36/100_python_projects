from datetime import datetime

print(f"Enter notes for today:")

notes_list = []
sr_no = 1
while True:
    note = input(f"{sr_no}: ")
    if note.lower() != 'exit':
        notes_list.append(f'{sr_no}.{note.title()}')
        sr_no += 1
    else:
        break

content = "\n".join(notes_list)

date = datetime.today().date()
filename = f"{date}.txt"

with open(filename, "w", encoding='utf-8') as file:
    file.write(f"{content}")

print(f"Your notes have been saved to {filename}")
