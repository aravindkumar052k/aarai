#sidebar.py
import streamlit as st



def logout():
    st.session_state.clear()
    st.switch_page("main.py")


def sidemenu():
    if st.button("logout"):
        logout()




