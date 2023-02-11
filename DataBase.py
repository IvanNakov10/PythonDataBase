import sqlite3

# Connect to database (creates database if it does not exist)
conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees""")