#2_NewAnlaysis
import streamlit as st

from utils.auth import check_login,get_username
st.set_page_config(page_title="Aarai - New Analysis")

check_login()
get_username()

st.title("New Analysis !")