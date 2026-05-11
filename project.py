import streamlit as st

st.title('project status page')
st.header('status page')

st.metric(label='**budget spent**', value='$800', delta='-0.5%')
st.metric(label='**tasks complete**', value='5', delta='+5%')
st.metric(label='**days remaining**', value='15', delta='1%')

st.info('This budget for a man who do affiliate marketing')
st.markdown('*My first streamlit project')
