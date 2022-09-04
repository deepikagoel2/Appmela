import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlite3
import streamlit as st
# import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

# @st.cache
st.set_page_config(
    page_title="Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("AppMela Dashboard")


cols = st.columns([.333, .333, .333])

option2 = st.selectbox(
    'How many rows you would like to display',
    ('10', '50', '100'))


placeholder = st.empty()


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='appmela',
                                         user='root',
                                         password='india@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        operation = 'SELECT count(id) from student_registration; SELECT count(id) from establishment; SELECT stateName from stateName; SELECT Districts_name from districts;'

        for result in cursor.execute(operation, multi=True):
            if result.with_rows:
                record = cursor.fetchall()
            df = pd.DataFrame(record, columns=['tot_stud', 'tot_est', 'state', 'district'
                                           ])
        # df = df.drop_duplicates(['email'])
            df.sort_values(by=['state', 'district'], ascending=True)

        print(df)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():

        cursor.close()
        connection.close()
        print("MySQL connection is closed")
