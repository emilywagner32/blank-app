import streamlit as st

st.title("Jobsite Work flow")
with st.form("LMP_form"):
   st.write("Jobsite End of Day Summary")
   jobsite = st.text_area('Job site location:', height=300)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')
