
import streamlit as st
from multiapp import MultiApp
from apps import home, coor # import your app modules here

st.set_page_config(
        page_title="Dashboard",
        page_icon="✅",
        layout="wide",
    )

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the streamlit-multiapps framework.

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Coordinator", coor.app)

app.run()