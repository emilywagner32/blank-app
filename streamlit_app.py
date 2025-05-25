import streamlit as st

st.title("Jobsite Work flow")
with st.form("LMP_form"):
   st.write("Jobsite End of Day Summary")
   jobsite = st.text_area('Job site location:')
   description = st.text_area('Description of work completed:', height=300)
   equipt = st.selectbox('Were any tools or equiptment broken?' ['yes', 'no'])
   description_broken = st.text_area('Describe what was broken:':', height=300)
   st.form_submit_button('Submit my picks')
