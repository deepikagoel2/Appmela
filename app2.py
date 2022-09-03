import mysql.connector
import pandas as pd 
import sqlalchemy

#establishing the connection
conn = mysql.connector.connect(user='root', password='india@123', host='127.0.0.1', database='appmela')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
# cursor.execute("SELECT DATABASE()")

cursor.execute('SELECT * FROM appmela.nodal_login;')

# connection.commit()

# query = 'SELECT * FROM appmela.nodal_login;'

# Fetch a single row using fetchone() method.

# df = pd.read_sql_query(query, connection)   



for row in cursor:
    data = cursor.fetchall()
    # df = pd.DataFrame(data)
# print(row)
print("Connection established to: ",data)

# df = pd.DataFrame(data)
# print(df)

# data.to_csv('nodal_login.csv', index = False)

# df = pd.read_table(data)

# df = pd.read_sql('SELECT * FROM appmela.nodal_login;', data)

#Closing the connection
conn.close()