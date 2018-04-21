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

class Students():
    def __init__(self, students=[]):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def add_students(self, students):
        for student in students:
            self.add_student(student)

    def get_all_students(self, db):
        return db.select("select * from students;")

    def search(self, db, what=None, location=None, availability=None, payment=None, education=None):
        params = {}
        if what != None:
            params['what'] = what
        if location != None:
            params['location'] = location
        if availability != None:
            params['availability'] = availability
        if payment != None:
            params['payment'] = payment
        if education != None:
            params['education'] = education

        whereParam = "and ".join(["{}='{}'".format(n, params[n]) for n in params.keys()])
        if len(whereParam) == 0:
            paramString = ""
        else:
            paramString = "where " + whereParam
        return db.select('select * from students {};'.format(paramString))

db = Database('D:\sqlite\hackathon.db')

students = Students()
search_result = students.get_all_students(db)

for student in search_result:
    print(student.values())