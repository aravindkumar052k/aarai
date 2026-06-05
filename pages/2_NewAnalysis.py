#2_NewAnalysis
import streamlit as st
from utils.sidebar import sidemenu

from utils.auth import check_login,get_username
st.set_page_config(page_title="Aarai - New Analysis")
col1, col2 = st.columns([8,1])

check_login()
get_username()


with col1:
    st.title("New Analysis !")
with col2:
    sidemenu()


