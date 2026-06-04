#1_homepage
import streamlit as st


email = st.session_state.get("Email")
res = email.split('@')[0]
st.title(f":blue[Hello ] {res} !")

if st.button("New Analysis +"):
    st.session_state["New_Analysis"] = True
    st.switch_page("pages/2_NewAnalysis.py")
#st.header("_Streamlit_ is :blue[cool] :sunglasses:")
#st.markdown("*Streamlit* is **really** ***cool***.")
#st.header("This is a header with a divider", divider="gray")
#st.header("One", divider=True)


