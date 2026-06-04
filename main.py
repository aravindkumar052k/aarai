#main.py
import streamlit as st


st.title("Aarai")
users = {
    "test@gmail.com":"test"
}

Email = st.text_input("Email")
Password = st.text_input("Password",type="password")

if st.button("Login"):
    if Email in users and users[Email] == Password:
        st.success("Login Successful")
        st.session_state["logged_in"] = True
        st.session_state["Email"] = Email
        st.switch_page("pages/1_HomePage.py")
    else:
        st.error("Invalid Credentials")



