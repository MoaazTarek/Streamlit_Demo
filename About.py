import streamlit as st
import pandas as pd
import os

os.chdir('D:/Moaaz/Programming/Epsilon_Data_Science_Diploma/17_Streamlit/Streamlit_Demo/Pages')

st.title('About')

st.info('This is a Test')

st.success('This is a Test')

name = st.text_input('Enter your name')

age = st.number_input('Enter your age')

height = st.slider('Enter your height', min_value= 0, max_value= 200, value= 100, step= 10)

def get_data():
    dic = {'name': name, 'age': age, 'height': height}
    df = pd.DataFrame(dic, index= [0])
    return df