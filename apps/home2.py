import streamlit as st
import mysql.connector
from mysql.connector import errorcode

config = {
'user': 'username',
'password':'password',
'host': 'localhost',
'database':'database',
'raise_on_warnings': True
}

class mySQL:
        def init(self):
                # self.st = st
                try:
                        self.cnx = mysql.connector.connect(**config)
                        self.cursor = self.cnx.cursor()

                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                self.st.text("Something is wrong with your user name or password")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                self.st.text("Database does not exist")
                        else:
                                self.st.text('Unknown error')
        
        def mysql_select(self, sql) :
                try :
                        self.cursor.execute(sql)
                        result = self.cursor.fetchall()
                        if not result :
                                return False, "Record not found"
                        else :
                                return True, result
                        
                except mysql.connector.Error as err:
                        return False, str(err.errno) + " : " + sql

query_to_execute = '''select 
                                count(student_registration.id), count(establishment.id),
                                state.stateName, districts.Districts_name
                                from appmela.student_registration
                                left outer join establishment on student_registration.district = establishment.district
                                inner join state on state.stateName = student_registration.state
                                inner join districts on districts.Districts_name = student_registration.district
                                group by districts.Districts_name;'''
mysql = mySQL()
mysql. mysql_select(query_to_execute)
