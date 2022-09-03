import pymysql
import pandas as pd

db = pymysql.connect("localhost","root","india@123","appmela")



cur = db.cursor()

cur.execute('SELECT * FROM appmela.nodal_login')

for row in cur.fetchall():
    print(row)

db.close()
