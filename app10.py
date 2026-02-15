import streamlit as st
import pandas as pd
import numpy as np

st.title("🎁 st.selectbox")

df = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

selected_column = st.selectbox(
    "Select a Dataframe column",
    df.columns
)
st.write(selected_column)
st.line_chart(df, x=None, y=selected_column)
# option = st.selectbox(
#     'What is your favorite color?',
#     ('Blue', 'Red', 'Green')
# )

# st.write(f'Your favortite color is: {option}')