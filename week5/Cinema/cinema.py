import sqlite3


class Cinema:
    def __init__(self, database):
        self.database = database
        self.conn = None
        self.cursor = None

    def start_up(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''PRAGMA foreign_keys = ON;''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            movies(id INTEGER PRIMARY KEY, name TEXT,rating REAL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT,
                            date TEXT, time TEXT, FOREIGN KEY (movie_id) REFERENCES movies(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                            reservation(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER,
                            row INTEGER, col INTEGER, FOREIGN KEY (projection_id) REFERENCES projections(id))''')

    def close_db(self):
        self.conn.close()

    def insert_movie_query(self, values):
        query = 'INSERT INTO movies (name, rating) VALUES (?, ?);'
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_movie(self, name, rating):
        values = (name, rating)
        self.insert_movie_query(values)

    def insert_projection_query(self, values):
        query = 'INSERT INTO projections (movie_id, type, date, time) VALUES (?, ?, ?, ?);'
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_projection(self, movie_id, type, date, time):
        values = (movie_id, type, date, time)
        self.insert_projection_query(values)

    def insert_reservartion(self, values):
        query = 'INSERT INTO reservation (username, projection_id, row, col) VALUES (?, ?, ?, ?);'
        self.cursor.execute(query, values)
        self.conn.commit()

    def add_reservation(self, username, projection_id, row, col):
        values = (username, projection_id, row, col)
        self.insert_reservartion(values)

    def show_movies(self):
        self.cursor.execute('''SELECT * FROM movies ORDER BY rating''')
        all_rows = self.cursor.fetchall()
        for row in all_rows:
            print(row[0], row[1])


def main():
    test_cinema = Cinema("test_cinema.db")
    test_cinema.start_up()
    test_cinema.add_movie("Fast and Furious", 8)
    test_cinema.add_projection("3D", 2, "2014-04-01", "19:10")
    test_cinema.add_reservation("kashev", 1, 2, 2)
    test_cinema.close_db()
if __name__ == '__main__':
    main()
