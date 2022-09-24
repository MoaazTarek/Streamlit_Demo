import os

os.chdir('D:/Moaaz/Programming/Epsilon_Data_Science_Diploma/17_Streamlit/Streamlit_Demo/Pages')

import About  
import pandas as pd
import streamlit as st


df = About.get_data()

st.write(df)
