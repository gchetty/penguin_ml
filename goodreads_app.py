import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

file_url = 'https://assets4.lottiefiles.com/temp/lf20_aKAfIn.json'
lottie_book = load_lottieurl(file_url)
st_lottie(lottie_book, speed=1, height=200, key="initial")

st.title('Analyzing Your Goodreads Reading Habits')
st.subheader('A Web App by [Tyler Richards](http://www.tylerjrichards.com)')

'''
Hey there! Welcome to Tyler's Goodreads Analysis App. This app analyzes (and never stores!) 
the books you've read using the popular service Goodreads, including looking at the distribution 
of the age and length of books you've read. Give it a go by uploading your data below!
'''

goodreads_file = st.file_uploader('Please Import Your Goodreads Data')
if goodreads_file is None:
	books_df = pd.read_csv('goodreads_history.csv')
else:
	books_df = pd.read_csv(goodreads_file)
	st.write('Analyzing your Goodreads history')
st.write(books_df.head())

