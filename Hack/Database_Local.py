import sqlite3

class Database_Local():


    db = sqlite3.connect(hackathon)
    c = db.cursor()



    c.execute(SELECT * FROM Students)