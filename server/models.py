import sqlite3


class Db_start:
    def __init__(self):
        self.conn = sqlite3.connect("poll.db")
        self.c = self.conn.cursor()
        self.create_user_table()
        self.create_poll_table()

    def create_poll_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS poll (
            id INTEGER PRIMARY KEY,
            username TEXT,
            age INTEGER,
            city TEXT,
            country TEXT
        );
        """
        self.c.execute(query)
        self.conn.commit()

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "user" (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
        """
        self.c.execute(query)
        self.conn.commit()


class PollModel:
    def __init__(self):
        self.conn = sqlite3.connect("poll.db")
        self.c = self.conn.cursor()

    def add_record(self, username, age, city, country):
        self.c.execute(
            "INSERT INTO poll (username, age, city, country) VALUES (?, ?, ?, ?)",
            (username, age, city, country),
        )
        self.conn.commit()
        return self.c.lastrowid

    def get_records(self):
        self.c.execute("SELECT * FROM poll")
        return self.c.fetchall()

    def close(self):
        self.conn.close()


class Db_service:
    def __init__(self):
        self.model = PollModel()

    def add_record_to_poll(self, username, age, city, country):
        return self.model.add_record(username, age, city, country)

    def get_last_record_from_poll(self):
        record = self.model.get_records()[-1] if self.model.get_records() else None
        if record is None:
            return None
        else:
            return {
                "id": record[0],
                "username": record[1],
                "age": record[2],
                "city": record[3],
                "country": record[4],
            }
