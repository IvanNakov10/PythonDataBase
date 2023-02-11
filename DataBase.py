import sqlite3
from employee import Employee
# Connect to database (creates database if it does not exist)
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
 #       first text,
  #      last text,
   #     pay integer
    #    )""")

Employee1 = Employee('Gogo', 'Petrov', 2000)

Employee2 = Employee('Vasko', 'Petrov', 3000)

print(Employee1.first)
print(Employee1.last)
print(Employee1.pay)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (Employee1.first, Employee1.last, Employee1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': Employee2.first, 'last':Employee2.last, 'pay':Employee2.pay})
conn.commit()

c.execute("SELECT * FROM employees WHERE last='Nakov'")

print(c.fetchmany(2))

conn.commit()

conn.close()