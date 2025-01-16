import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            conn.execute('''
            CREATE TABLE IF NOT EXISTS reviews(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number TEXT,
            rate TEXT,
            extra_comments TEXT )
            ''')


    def save_review(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            INSERT INTO reviews(name, number, rate, extra_comments)
            VALUES (?, ?, ?, ?)''',
    (data['name'], data['number'], data['rate'], data['extra_comments']))

