import streamlit as st
st.title('Hello')
n=st.text_input('Enter your name')
if n=='python':
    st.write('Welcome to cetpa')
x=st.number_input('Enter your marks')
if x>=75:
    st.write('you are eligible for 75% discount')
    
