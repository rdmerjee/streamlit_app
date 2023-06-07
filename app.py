import streamlit as st


st.title('Rik Mukherjee Application')
st.markdown('this is **the special application for Stats 21**')
st.markdown('this is *The thing you need*')

st.sidebar.title('More')
st.sidebar.markdown('This project was done in Spring 2023 for Stats 21')


agree = st.checkbox('I agree')

if agree:
    st.write('Great')
    st.markdown('You have agreed')

agree_sidebar = st.sidebar.checkbox('This app is cool')

if agree_sidebar:
    st.sidebar.write('You have agreed')
