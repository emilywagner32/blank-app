import streamlit as st

st.title("Jobsite Work flow")
with st.form("LMP_form"):
   st.write("Jobsite End of Day Summary")
   jobsite = st.text_area('Job site location:', height=68)
   description = st.text_area('Description of work completed:', height=300)
   st.form_submit_button('Submit my picks')
