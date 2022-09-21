import streamlit as st
import pandas as pd
st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')
col1, col2, col3 = st.columns((1,1,1))
col1.write('First column')
col2.write('Second column')
col3.write('Third column')
