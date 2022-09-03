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
        # sql = "select appmela.candidate.name, appmela.candidate.email, appmela.candidate.gender, from appmela.candidate,

        #         join
        #         "
        cursor.execute('''select student_registration.name, student_registration.gender, state.stateName, districts.Districts_name, student_registration.email_id,
                       establishment.name, establishment.registered from appmela.student_registration
                       left outer join establishment on student_registration.district = establishment.district
                       inner join state on state.stateName = student_registration.state
                       inner join districts on districts.Districts_name = student_registration.district
                       ''')
        record = cursor.fetchall()
        df = pd.DataFrame(record, columns =['stud_name', 'gender', 'state', 'district', 'email','company_name', 'registered',
                                            ])
        df = df.drop_duplicates(['email'])
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
                    
        
    total_stud = df["email"].nunique()
    register = df['registered'].value_counts(dropna=True)['Yes']
    # # seats_available = int(df["SeatsAvailable"].sum())
    # # total_units = int(df["TotalUnits"].sum())
    # # units_available = int(df["UnitsAvailable"].sum())
    # # admissions = int(df["Admissions"].sum())
    # # num_itis = int(df['ITI_Name'].nunique())
    # # num_trades = int(df['Trade_Name'].nunique())
    # # women_iti = int(df['ITI_Women'].nunique())
        


    with cols[0]:
        # st.subheader("Total Seats")
        # st.subheader(f"{total_seats}")
        # st.subheader("Seats Available")
        # st.subheader(f"{seats_available}")  
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Total Students"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{total_stud}"

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
        
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Seats Available"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{seats_available}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)
    # #     # card("Total Seats", f"{total_seats}")
    # #     # card("Seats Available", f"{seats_available}")
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Number of Trades"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{num_trades}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)
        
    with cols[1]:
        # st.subheader("Total Units")
        # st.subheader(f"{total_units}")
        # st.subheader("Units Available")
        # st.subheader(f"{units_available}")
        # card("Total Units", f"{total_units}")
        # card("Units Available", f"{units_available}")
        wch_colour_box = (0,204,102)
        wch_colour_font = (0,0,0)
        fontsize = 18
        valign = "left"
        iconname = "fas fa-asterisk"
        sline = "Total Establishments"
        # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = f"{register}"

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
        
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Units Available"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{units_available}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Number of Women ITI"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{women_iti}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)

        
    # # with cols[2]:
    # #     # st.subheader("Admissions")
    # #     # st.subheader(f"{admissions}")
    # #     # card("Admissions", f"{admissions}")
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Admissions"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{admissions}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)
        
    # #     wch_colour_box = (0,204,102)
    # #     wch_colour_font = (0,0,0)
    # #     fontsize = 18
    # #     valign = "left"
    # #     iconname = "fas fa-asterisk"
    # #     sline = "Number of ITI"
    # #     # lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    # #     i = f"{num_itis}"

    # #     htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
    # #                                               {wch_colour_box[1]}, 
    # #                                               {wch_colour_box[2]}, 0.75); 
    # #                         color: rgb({wch_colour_font[0]}, 
    # #                                    {wch_colour_font[1]}, 
    # #                                    {wch_colour_font[2]}, 0.75); 
    # #                         font-size: {fontsize}px; 
    # #                         border-radius: 7px; 
    # #                         padding-left: 12px; 
    # #                         padding-top: 18px; 
    # #                         padding-bottom: 18px; 
    # #                         line-height:25px;'>
    # #                         <i class='{iconname} fa-xs'></i> {i}
    # #                         </style><BR><span style='font-size: 14px; 
    # #                         margin-top: 0;'>{sline}</style></span></p>"""

    # #     st.markdown(htmlstr, unsafe_allow_html=True)

        
    

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        
