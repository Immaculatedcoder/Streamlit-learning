import streamlit as st

st.title("st.multiselct")

option = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected: ', option)

for color in option:
    st.write(color)
