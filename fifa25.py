import streamlit as st
import numpy as np
import pandas as pd

fifa=pd.read_csv('fifa_eda.csv')
st.title("fifa exploratory data analysis")
st.write(""" this app performs simple eda on fifa 2019 data
         *** python libraries:pandas,streamlit,numoy,matplotlib,seaborn*data source:[Kaggle] https://www.kaggle.com/""")

st.subheader("top 5 valued players")
st.write(fifa.nlargest(5,'Value')[['Name','Value']])
top_players_dict= fifa.nlargest(5,'Value')[['Name','Value']].set_index("Name").to_dict()
for name,value in top_players_dict['Value'].items():
          st.markdown(f"+{name}:{value}")