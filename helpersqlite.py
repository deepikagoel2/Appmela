import sqlite3

def ping():
    print("Working.....")
    
def getalldata(sqlstring, path):
    db = sqlite3.connect(path, uri = True)
    cur = db.cursor()
    cur.execute(sqlstring)
    return cur.fetchall()

def crud(sqlstring, path):
    db =  sqlite3.connect(path)
    c = db.cursor()
    c.excute(sqlString)
    db.commit()
    db.close()