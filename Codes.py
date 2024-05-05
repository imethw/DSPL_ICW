import pandas as pd
import streamlit as st
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Global superstore",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)
# Customized CSS to style the dashboard
st.markdown(
    """
    <style>
        /* Center align the main header and subheader */
        .center {
            text-align: center;
        }
        
        /* Add padding to the bordered container */
        .bordered {
            border: 2px solid #ddd;  /* Add a light gray border */
            border-radius: 10px;  /* Add border radius for rounded corners */
            padding: 20px;
            margin-bottom: 10px;  /* Add some space between elements */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add a shadow effect */
            background-color: #f9f9f9; /* Light gray background color */
        }       
    </style>
    """,
    unsafe_allow_html=True
)
# Border container for the entire dashboard
st.markdown('<div class="bordered">', unsafe_allow_html=True)

# Main header and subheader
st.markdown('<div class="center header"><h1>Global Sales Dashboard<h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader"><h3>Analyze Your Sales Data<h3></div>', unsafe_allow_html=True)

# Reading the data
sales_data = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')
