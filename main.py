import streamlit as st
from helperSqlite import *

if st.button('submit'):
    select = '''
    select * from appmela.student_registration;
    ''' 
    
    crud(select, 'appmela.db')