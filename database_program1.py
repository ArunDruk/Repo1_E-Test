import sqlite3
conn=sqlite3.connect("employee.db") # this creates the database, it the db is already present it just connects it.
c=conn.cursor()
#c.execute("CREATE TABLE employees(first text, last text, pay integer)")

c.execute("INSERT INTO employees VALUES('Dhoni','kumar',30000)")
c.execute("SELECT * from employees")

print(c.fetchall())

conn.commit()
conn.close()

