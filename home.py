import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlite3
import streamlit as st
# import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
# def app():
# @st.cache
   
st.title("AppMela Dashboard")
cols = st.columns([.333, .333, .333])
option2 = st.selectbox(
'How many rows you would like to display',
('10', '50', '100'))
placeholder = st.empty()    
try:
    # connection = mysql.connector.connect(host='localhost',
    #                                     database='appmela',
    #                                     user='root',
    #                                     password='india@123')

    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])
    connection = init_connection()
    @st.experimental_memo(ttl=600)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(buffered = True)
        # sql = "select appmela.candidate.name, appmela.candidate.email, appmela.candidate.gender, from appmela.candidate,
        #         join
        #         "
        for record in cursor.execute('''
                                        Select add_vacency.state_name , add_vacency.district , 
                                        add_vacency.tradename ,  sum(add_vacency.vacency) as vacancy_counts, 
                                        
                                        count(company_name) as Number_of_Companies
                                        from appmela.add_vacency 
                                        group by district order by state_name;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df = pd.DataFrame(record, columns =['state', 'district', 'Trades', 
                                                    'Number of Vacancies',
                                                    'Number of Companies',
                                                    
                                            ])
        for record in cursor.execute('''
                                        SELECT count(distinct(email)) as num
                                        FROM appmela.candidate where district != '' group by district;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df['Number of Students'] = pd.DataFrame(record).reset_index(drop=True)
                
        for record in cursor.execute('''
                                        SELECT count(distinct(cemailid)) as num
                                        FROM appmela.establishment where district != '' group by district;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df['Number of Establishhment'] = pd.DataFrame(record).reset_index(drop=True)
                
        for record in cursor.execute('''
                                        SELECT count(distinct(apprenticemelacenter)) as num
                                        FROM appmela.vacancy_details1 group by DistrictName;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df['Number of ApprenticeMelacenter'] = pd.DataFrame(record).reset_index(drop=True)
                
        
        for record in cursor.execute('''
                                        SELECT count(distinct(email)) as num
                                        FROM appmela.candidate where district != '' group by district;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df['Number of Students'] = pd.DataFrame(record).reset_index(drop=True)
                
        for record in cursor.execute('''
                                        SELECT count(distinct(nEmail)) as num
                                        FROM appmela.nodal where district != '' group by district;
                                        '''
                        ,multi = True):
            if record.with_rows: 
                record = cursor.fetchall()
                df['Number of Coordinators'] = pd.DataFrame(record).reset_index(drop=True)
        # df = df.drop_duplicates(['email'])
                df.sort_values(by=['state', 'district'], ascending=True)
        # df = df.loc[(df['district'] != 'Select District')]
        # df = df.dropna(axis = 0, how = 'any')
        # df = df.loc[[df[:, 'district'] != 'Select District']]
            
    # st.dataframe(df)
    # AgGrid(df)
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_default_column(editable = True, groupable = True)
    # gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()
    # print("You're connected to database: ", record)
    states = list(df['state'].unique())
    state = st.sidebar.multiselect("State",options = states, key = 1)
    st.write('State Name selected as', state)
    with placeholder:
        if state:
            df = df[df['state'].isin(state)] 
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
        
    districts = list(df['district'].unique())
    district = st.sidebar.multiselect("District",options = districts, key = 2)
    st.write('District Name selected as', district)
    with placeholder:
        if district:
            df = df[df['district'].isin(district)]
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
                key = 2
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
                key = 2
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
                key = 2
                )  
                    
        
    tot_stud = int(df["Number of Vacancies"].sum())
    est = int(df['Number of ApprenticeMelacenter'].sum())
    tot_cord = int(df['Number of Establishhment'].sum())
    tot_vcn = int(df['Number of Students'].sum())
    tot_comp = int(df['Number of Companies'].sum())
    tot_coord = int(df['Number of Coordinators'].sum())
    with cols[0]:

        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of vacancies"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{tot_stud}"
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
        
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of Students"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{tot_vcn}"
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
            
    with cols[1]:
        
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of ApprenticeMelacenter"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{est}"
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
        
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of Companies"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{tot_comp}"
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
        
        
    with cols[2]:
        
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of Establishhment"
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
        
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Number of Coordinators"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{tot_coord}"
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
        return df.to_csv(index = False).encode('utf-8')
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
# finally:
#     if connection.is_connected():

#     cursor.close()
#     connection.close()
        
    # print("MySQL connection is closed")

# app.run()
