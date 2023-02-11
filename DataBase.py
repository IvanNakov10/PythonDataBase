import sqlite3

# Connect to database (creates database if it does not exist)
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
 #       first text,
  #      last text,
   #     pay integer
    #    )""")

# c.execute("INSERT INTO employees VALUES ('Ivan', 'Nakov', 50000)")

c.execute("SELECT * FROM employees WHERE last='Nakov'")

print(c.fetchone())

conn.commit()

conn.close()