#main.py
import streamlit as st

st.set_page_config(page_title="Aarai")

st.title("Aarai")
users = {
    "test@gmail.com":"test"
}



email_id = st.text_input("Email")
password = st.text_input("Password",type="password")

if st.button("Login"):
    if email_id in users and users[email_id] == password:
        st.success("Login Successful")
        st.session_state["logged_in"] = True
        st.session_state["email_id"] = email_id
        st.switch_page("pages/1_HomePage.py")
    else:
        st.error("Invalid Credentials")



