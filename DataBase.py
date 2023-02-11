import sqlite3
from employee import Employee
# Connect to database (creates database if it does not exist)
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

def insert_emp(emp):
    c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last':emp.last, 'pay':emp.pay})

def  get_emps_Byname(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})    
    return c.fetchall()

def update_emp(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE form employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

Employee1 = Employee('Gogo', 'Petrov', 2000)
Employee2 = Employee('Vasko', 'Petrov', 3000)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (Employee1.first, Employee1.last, Employee1.pay))
conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': Employee2.first, 'last':Employee2.last, 'pay':Employee2.pay})
conn.commit()

c.execute("SELECT * FROM employees WHERE last=?", ('Nakov',))

print(c.fetchall())

conn.commit()

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Petrov'})

print(c.fetchall())

conn.commit()

conn.close()