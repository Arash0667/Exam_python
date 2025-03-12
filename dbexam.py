import sqlite3

class Database:
    def __init__(self,db):
        self.con= sqlite3.connect(db)
        self.cur= self.con.cursor()
        self.cur.execute( """        
                            CREATE TABLE IF NOT EXISTS Contacts (id integer PRIMARY KEY,
                            fname text, lname text , email real , password integer)
                            """)
        self.con.commit()

    def insert(self,fname,lname,email,password):
        self.cur.execute('INSERT INTO Contacts VALUES (null,?,?,?,?)',(fname,lname,email,password))
        self.con.commit()

    def select_records(self,email,password):
        self.cur.execute('SELECT * FROM Contacts WHERE email=? and password=? ',(email,password) )
        rows=self.cur.fetchall()
        return rows
        
db1=Database("C:/test/db_exam.db")
