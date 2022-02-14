import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, smth varchar(100))')
        self.connection.commit()

    def fetch(self):
        self.cursor.execute('select * from items')
        rows = self.cursor.fetchall()
        return rows

    def insert(self, smth):
        self.cursor.execute("INSERT INTO items VALUES (NULL, ?)", (smth,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()


# db = Database('simple_db.db')
# db.insert('drugie cos')
db = Database('simple_db.db')
# print(db.fetch())
