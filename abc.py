import streamlit as st
st.title('Welcome Learner')
n=st.text_input('Enter your name:')
if n=='Naveen':
    st.balloons()
    st.write(n,'Welcome to Cetpa')
x=st.number_input('Enter your age')
if x>=10 and x<=18:
    st.write('You are eligible for online course')
elif x>18 and x<=21:
    st.write('You are eligible for week end course and online course')
elif x>21 and x<=40:
    st.write('You are eligible for job oriented regular course')
a=st.radio('Are you working?',options=('yes','no'))
if a=='yes':
    st.write('You are eligible for week end course and online course')
else:
    st.write('You are eligible for job oriented regular course')
s=st.sidebar.checkbox('Are you interested in programming')
if s==True:
    t=st.sidebar.radio('You can choose language',options=('Python','Java','c'))
    if t==('Python'):
        st.sidebar.write('Welcome to python')
else:
    st.sidebar.write('You can enerol for sql')





