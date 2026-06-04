#2_NewAnlaysis
import streamlit as st

from utils.auth import check_login,get_username

check_login()
get_username()

st.title("New Analysis !")