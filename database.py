import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path


    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS reviews(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number TEXT, 
            rate INTEGER,
            extra_comments TEXT)''')


    def save_review(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            INSERT INTO reviews(name, number, rate, extra_comments)
            VALUES (?, ?, ?, ?)''',
                         (data['name'], data['number'], data['rate'], data['extra_comments']))

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS dishes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            caption TEXT,
            category TEXT,
            portions INTEGER)''')


    def save_dishes(self, data: dict):
        with sqlite3.connect (self.path) as conn:
            conn.execute('''
            INSERT INTO dishes(name, price, caption, category, portions)
            VALUES(?,?,?,?,?)''',
                        (data['name'], data['price'], data['caption'], data['category'], data['portions']))
