#1_homepage
import streamlit as st

from utils.auth import check_login, get_username
st.set_page_config(page_title="Aarai - Home")


check_login()
username = get_username()

st.title(f":blue[Hello ] {username} !")

if st.button("New Analysis +"):
    st.switch_page("pages/2_NewAnalysis.py")



