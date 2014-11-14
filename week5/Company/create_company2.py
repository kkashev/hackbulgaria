import sqlite3


class Company:

    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None

    def create_table(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            employees(id INTEGER PRIMARY KEY, name TEXT,
                            monthly_salary REAL, yearly_bonus REAL, position TEXT)''')

        name1 = "Ivan Ivanov"
        monthly_salary1 = 5000
        yearly_bonus1 = 10000
        position1 = "Software Developer"

        self.cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
                          VALUES(?,?,?,?)''', (name1, monthly_salary1, yearly_bonus1, position1))

        self.conn.commit()

    def list_employees(self):
        self.cursor.execute('''SELECT name, position FROM company''')
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            print(row[1])


def main():
    database1 = Company("testdb.db")
    database1.create_table()
    database1.list_employees()
if __name__ == '__main__':
    main()
