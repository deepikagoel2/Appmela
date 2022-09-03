# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, inspect
import pandas as pd

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'india@123'
host = '127.0.0.1'
port = 3306
database = 'appmela'


try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    con = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))
    # inspector = inspect(con)
    # inspector.get_table_names()
    print(f"Connection to the {host} for user {user} created successfully.") 
    nodal_login = pd.read_sql('SELECT * FROM appmela.nodal_login;',con)    
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)
