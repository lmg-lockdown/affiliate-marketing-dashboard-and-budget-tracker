import streamlit as st

st.title('project status page')
st.header('status page')

st.info('This budget is for a man who do affiliate marketing')
st.info('this project shows his:')
st.info('budget spent since he started affiliate marketing')
st.info('sales completed')
st.info('And days remaining till the sales are over')

st.metric(label='**budget spent**', value='$800', delta='-0.5%')
st.metric(label='**tasks complete**', value='5', delta='+5%')
st.metric(label='**days remaining**', value='15', delta='1%')

st.markdown('*My first streamlit project')
st.markdown('*Budget tracking')
st.markdown('*Task monitoring')
st.markdown('*Sales tracking')
st.markdown('*Campaign countdown')
st.markdown('*Dark mode UI')
st.markdown('*Easy to use')
st.markdown('*Beginner friendly')
st.markdown('*Real-time updates')
