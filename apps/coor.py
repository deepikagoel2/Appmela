import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlite3
import streamlit as st
# import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

# @st.cache

def app():
        

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
                        cursor = connection.cursor(buffered = True)
                        cursor.execute('select id, apprenticemelacenter, trades, vacency from coordinator_details')
                        
                        record = cursor.fetchall()
                        df = pd.DataFrame(record, columns = ['tot_coord', 'Appmela', 'trades', 'vacancy'])
                        
                tot_cord = int((df['tot_coord'].count()).sum())
                
                gb = GridOptionsBuilder.from_dataframe(df)
                gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
                gb.configure_default_column(editable = True, groupable = True)
                # gb.configure_side_bar() #Add a sidebar
                gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
                gridOptions = gb.build()

                # print("You're connected to database: ", record)
                trades = list(df['trades'].unique())
                trade = st.sidebar.multiselect("Trades",options = trades, key = 1)
                st.write('Trades Name selected as', trade)
                with placeholder:
                        if trade:
                                df = df[df['trades'].isin(trade)] 
                                # placeholder.dataframe(df.reset_index())
                                if option2 == '10': 
                                        AgGrid(df.head(10),
                                        gridOptions=gridOptions,
                                        data_return_mode='AS_INPUT', 
                                        update_mode='SELECTION_CHANGED', 
                                        fit_columns_on_grid_load=False,
                                        theme='blue', #Add theme color to the table
                                        enable_enterprise_modules=True,
                                        height=350, 
                                        width='100%',
                                        reload_data=True,
                                        key = 1
                                        )
                                elif option2 == '50':
                                        AgGrid(df.head(50),
                                        gridOptions=gridOptions,
                                        data_return_mode='AS_INPUT', 
                                        update_mode='SELECTION_CHANGED', 
                                        fit_columns_on_grid_load=False,
                                        theme='blue', #Add theme color to the table
                                        enable_enterprise_modules=True,
                                        height=350, 
                                        width='100%',
                                        reload_data=True,
                                        key = 1
                                        )
                                elif option2 == '100':
                                        AgGrid(df.head(100),
                                        gridOptions=gridOptions,
                                        data_return_mode='AS_INPUT', 
                                        update_mode='SELECTION_CHANGED', 
                                        fit_columns_on_grid_load=False,
                                        theme='blue', #Add theme color to the table
                                        enable_enterprise_modules=True,
                                        height=350, 
                                        width='100%',
                                        reload_data=True,
                                        key = 1
                                        )
                        
                with cols[0]:
                
                        wch_colour_box = (0,204,102)
                        wch_colour_font = (0,0,0)
                        fontsize = 18
                        valign = "left"
                        iconname = "fas fa-asterisk"
                        sline = "Total Coordinators"
                        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
                        i = f"{tot_cord}"

                        htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                                {wch_colour_box[1]}, 
                                                                {wch_colour_box[2]}, 0.75); 
                                        color: rgb({wch_colour_font[0]}, 
                                                {wch_colour_font[1]}, 
                                                {wch_colour_font[2]}, 0.75); 
                                        font-size: {fontsize}px; 
                                        border-radius: 7px; 
                                        padding-left: 12px; 
                                        padding-top: 18px; 
                                        padding-bottom: 18px; 
                                        line-height:25px;'>
                                        <i class='{iconname} fa-xs'></i> {i}
                                        </style><BR><span style='font-size: 14px; 
                                        margin-top: 0;'>{sline}</style></span></p>"""

                        st.markdown(htmlstr, unsafe_allow_html=True)
                def convert_df(df):
                        return df.to_csv().encode('utf-8')

                csv = convert_df(df)

                st.download_button(
                "Press to Download",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
                )


        except Error as e:
                print("Error while connecting to MySQL", e)
        finally:
                if connection.is_connected():
                
                        cursor.close()
                        connection.close()