import sqlite3


class HandleQuery:

    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None

    def start_up(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            employees(id INTEGER PRIMARY KEY, name TEXT,
                            monthly_salary REAL, yearly_bonus REAL, position TEXT)''')

    def close_db(self):
        self.conn.close()

    def insert_query(self, values):
        query = 'INSERT INTO employees (name, monthly_salary, yearly_bonus, position) VALUES (?, ?, ?, ?);'
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        values = (name, monthly_salary, yearly_bonus, position)
        self.insert_query(values)

    def delete_employee(self, id):
        self.cursor.execute('''DELETE FROM employees WHERE id = ? ''', (id,))
        self.conn.commit()

    def update_employee(self, id, new_name, new_monthly_salary, new_yearly_bonus, new_position):
        self.cursor.execute('''UPDATE employees SET name = ? WHERE id = ? ''', (new_name, id))
        self.cursor.execute('''UPDATE employees SET monthly_salary = ? WHERE id = ? ''', (new_monthly_salary, id))
        self.cursor.execute('''UPDATE employees SET yearly_bonus = ? WHERE id = ? ''', (new_yearly_bonus, id))
        self.cursor.execute('''UPDATE employees SET position = ? WHERE id = ? ''', (new_position, id))
        self.conn.commit()

    def list_employees(self):
        self.cursor.execute('''SELECT name, position FROM employees''')
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            print(row[0], row[1])

    def monthly_spending(self):
        self.cursor.execute('''SELECT SUM(monthly_salary) FROM employees''')
        monthly_spending = self.cursor.fetchone()
        print(monthly_spending[0])

    def yearly_spending(self):
        yearly_spending = 0
        self.cursor.execute('''SELECT SUM(monthly_salary), SUM(yearly_bonus) FROM employees''')
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            yearly_spending = row[0] + row[1]
            print(yearly_spending)


def main():
    try_db = HandleQuery("test.db")
    try_db.start_up()
    try_db.add_employee("Kashev", 2000, 100, "shef")
    try_db.delete_employee(1)
    try_db.close_db()
if __name__ == '__main__':
    main()
