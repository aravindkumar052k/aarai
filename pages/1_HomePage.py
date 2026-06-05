#1_homepage
import streamlit as st

from utils.auth import check_login, get_username
from utils.sidebar import sidemenu

col1, col2 = st.columns([8,1])

st.set_page_config(page_title="Aarai - Home")


check_login()
username = get_username()

with col1:
    st.title(f":blue[Hello ] {username} !")
with col2:
    sidemenu()

if st.button("New Analysis +"):
    st.switch_page("pages/2_NewAnalysis.py")



