import streamlit as st

st.title("🎁 st.selectbox")

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green')
)

st.write(f'Your favortite color is: {option}')