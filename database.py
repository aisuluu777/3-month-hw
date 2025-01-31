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
            portions INTEGER,
            photo TEXT)''')


    def save_dishes(self, data: dict):
        with sqlite3.connect (self.path) as conn:
            conn.execute('''
            INSERT INTO dishes(name, price, caption, category, portions, photo)
            VALUES(?,?,?,?,?,?)''',
                        (data['name'], data['price'], data['caption'], data['category'], data['portions'], data['photo']))

    def get_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            result = cursor.execute('SELECT * FROM dishes')
            data = result.fetchall()
            return [dict(row) for row in data]



    def sort_by_price(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT dishes
            ORDER BY price''')
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    def get_all_reviews(self):
        with sqlite3.connect(self.path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            result = cursor.execute('SELECT * FROM reviews')
            data = result.fetchall()
            return [dict(row) for row in data]
