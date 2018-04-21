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