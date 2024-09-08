import sqlite3

db_file = "data.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

query = """
    SELECT * FROM albums
    WHERE Title LIKE '%Live%' AND LENGTH(Title) > 10   
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]}: {row[1]}")

cursor.close()
conn.close()
