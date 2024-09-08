import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

query = """
    SELECT CustomerId FROM invoices WHERE BillingCountry = 'Germany' AND Total >= 2.0
"""

cursor.execute(query)
data = cursor.fetchall()
for d in data:
    print(d[0])
print(data)
cursor.close()
conn.close()
