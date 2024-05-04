import pandas as pd
import streamlit as st
import plotly.express as px
t.set_page_config(
    page_title="Global Superstore"
)
#importing the dataset
df = pd.read_excel(cleaned_dataset.xlsx,engine='openpyxl')
