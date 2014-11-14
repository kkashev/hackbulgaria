import sqlite3

conn = sqlite3.connect("company.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus INTEGER , position TEXT)
''')
conn.commit()

name1 = "Ivan Ivanov"
monthly_salary1 = 5000
yearly_bonus1 = 10000
position1 = "Software Developer"

name2 = "Rado Rado"
monthly_salary2 = 500
yearly_bonus2 = 0
position2 = "Technical Support Intern"

name3 = "Ivo Ivo"
monthly_salary3 = 10000
yearly_bonus3 = 100000
position3 = "CEO"

name4 = "Petar Petrov"
monthly_salary4 = 3000
yearly_bonus4 = 1000
position4 = "Marketing Manager"

name5 = "Maria Georgieva"
monthly_salary5 = 8000
yearly_bonus5 = 10000
position5 = "COO"

cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name1, monthly_salary1, yearly_bonus1, position1))
