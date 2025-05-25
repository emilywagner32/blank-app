import streamlit as st

st.title("Daily Job Site Form")
with st.form("LMP_form"):
   st.write("Jobsite End of Day Summary")
   jobsite = st.text_area('Job site location:')
   description = st.text_area('Description of work completed:', height=300)
   brk = st.selectbox('Was any Equiptment broken?', ['yes', 'no'])
   brkn_desc = st.text_area('Describe what was broken:', height=300)
   st.form_submit_button('Submit')
