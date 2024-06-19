import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector



x=st.text_input("Favourite Movie?")
st.write(f"Fav Movie is {x}")
st.write("## This is a H2 Title")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
