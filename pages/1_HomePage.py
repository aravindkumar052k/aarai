#1_homepage
import streamlit as st

from utils.auth import check_login, get_username

check_login()
get_username()


st.title(f":blue[Hello ] {get_username()} !")

if st.button("New Analysis +"):
    st.switch_page("pages/2_NewAnalysis.py")



