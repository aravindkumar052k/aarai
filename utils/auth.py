#auth.py
import streamlit as st



def check_login():
    if not st.session_state.get("logged_in") :
        st.warning("Please login to continue")
        st.page_link("main.py", label="Go to Login")
        st.stop()

def get_username():
    email = st.session_state.get("email_id", "")
    return email.split("@")[0] if email else "User"