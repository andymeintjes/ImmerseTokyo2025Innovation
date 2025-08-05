import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
import streamlit as st

data_path = 'Global YouTube Statistics.csv'

df = pd.read_csv(data_path, on_bad_lines='skip', encoding_errors='ignore')

df_countries = df[df['Country'].isin(['United States', 'Canada', 'United Arab Emirates'])]
df_countries_views = df_countries[df_countries['video views']>0]

df_countries_views.sort_values(by='video views', ascending=False)

st.map(data=df_countries_views, size='video views', latitude='Latitude', longitude='Longitude')
