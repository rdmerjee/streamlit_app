import streamlit as st


st.title('Rik Mukherjee Application')
st.markdown('This is **the special application for Stats 21**')
st.markdown('An application that gives you what you need for the project in Stats 21')

st.sidebar.title('More')
st.sidebar.markdown('This project was done in Spring 2023 for Stats 21')

st.markdown('I recently watched Spider-Man: Across the Spiderverse, and I was deeply moved by the film. The animation was beautiful, the characters were great, the main character was very vulnerable and easy to root for, and the villain was menacing but you could understand why he did what he did.')
st.markdown('Do you agree that this movie is good?')

agree = st.checkbox('I agree')

if agree:
    st.write('Great, I agree with you')

st.markdown('Was the villain cool?')

yes = st.checkbox('Yes')
no = st.checkbox ('No')

if yes:
    st.write('**Great, I agree with you!**')

if no:
    st.write('**I do not agree with you. What is the reason for this?**')
    st.text_input('Input your reasoning here.')

agree_sidebar = st.sidebar.checkbox('If this app is cool, check this box.')

if agree_sidebar:
    st.sidebar.write('You have agreed with me that this app is cool.')
