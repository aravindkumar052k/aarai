#2_NewAnalysis
import streamlit as st
from streamlit.runtime.state import session_state

from utils.sidebar import sidemenu

from utils.auth import check_login,get_username
st.set_page_config(page_title="Aarai - New Analysis")
col1, col2 = st.columns([8,1])

check_login()
get_username()

with col1:
    st.title(":blue[New] Analysis !")
with col2:
    sidemenu()

st.divider()
st.session_state.setdefault("members",[])
st.session_state.setdefault("section_1 done",False)

st.subheader(":blue[Project] Details")
st.text_input("Project Name")
mem_col,add_col = st.columns([6,1])

#Add Members
with mem_col:
    new_member = st.text_input("Members",key="new_entry")
with add_col:
    st.write("")
    st.write("")
    if st.button("Add+"):
        if new_member.strip() == "":
            st.warning("Please add a member")
        elif new_member in st.session_state["members"]:
            st.warning("Person already exists")
        else:
            st.session_state["members"].append(new_member)


#Show members
if st.session_state["members"]:
    st.caption("Members added:")
    for i, member in enumerate(st.session_state["members"]):
        mem_list,rem_but =  st.columns([6,1])
        with mem_list:
            st.write(member)
        with rem_but:
            if st.button("x", f"remove_{i}"):
                st.session_state["members"].pop(i)
                st.rerun()

st.text_area("Project Description")

