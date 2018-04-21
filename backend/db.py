import sqlite3

class Database():
    def __init__(self, database_location):
        try:
            conn = sqlite3.connect(database_location)
            self.cursor = conn.cursor()
        except sqlite3.Error as e:
            print("Error: {}".format(e))

    def select(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [{self.cursor.description[idx][0]: rows[row][idx] for idx in range(len(rows[row]))} for row in range(len(rows))]