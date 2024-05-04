import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# Custom CSS to style the dashboard
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
            margin-bottom: 20px;  /* Add some space between elements */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add a shadow effect */
        }

        /* Style the main header */
        .header {
            margin-bottom: 20px;  /* Add some space below the header */
            font-size: 36px;
            color: #333;  /* Dark gray color */
        }

        /* Style the subheader */
        .subheader {
            margin-bottom: 40px;  /* Add more space below the subheader */
            font-size: 24px;
            color: #666;  /* Light gray color */
        }

        /* Style the column headers */
        .col-header {
            font-size: 24px;
            color: #333;  /* Dark gray color */
            margin-bottom: 10px;  /* Add some space below the column headers */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Bordered container for the entire dashboard
st.markdown('<div class="bordered">', unsafe_allow_html=True)

# Main header and subheader
st.markdown('<div class="center header">Global Superstore Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader">An Analysis of Sales Data</div>', unsafe_allow_html=True)

# Read the data
df = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')

# Creating three-column layout
col1, col2, col3 = st.columns(3)

# Box Plot
with col1:    
    st.markdown('<div class="col-header">Box Plot</div>', unsafe_allow_html=True)
    fig_box = px.box(df, x='Sub-Category', y='Quantity')
    st.plotly_chart(fig_box, use_container_width=True)

# Bar Chart
with col2:   
    st.markdown('<div class="col-header">Bar Chart</div>', unsafe_allow_html=True)
    fig_bar = px.bar(df, x='Ship Mode', y='Shipping Cost')
    st.plotly_chart(fig_bar, use_container_width=True)

# Donut Chart
with col3:
    st.markdown('<div class="col-header">Donut Chart</div>', unsafe_allow_html=True)
    fig_donut = px.pie(df, names='Order Priority', hole=0.5)
    st.plotly_chart(fig_donut, use_container_width=True)

# Histogram
with col1:    
    st.markdown('<div class="col-header">Histogram</div>', unsafe_allow_html=True)
    fig_hist = px.histogram(df, x='Region')
    st.plotly_chart(fig_hist, use_container_width=True)

# Area Chart
with col2:
    st.markdown('<div class="col-header">Area Chart</div>', unsafe_allow_html=True)
    fig_area = px.area(df, x='Market', y='Profit')
    st.plotly_chart(fig_area, use_container_width=True)

# Heatmap
sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()
top_5_countries = sales_by_country.nlargest(5, 'Sales')
df_top_5_countries = df[df['Country'].isin(top_5_countries['Country'])]
with col3:
    st.markdown('<div class="col-header">Heatmap of Top 5 Countries in Sales</div>', unsafe_allow_html=True)
    fig_heatmap_top_5 = px.density_heatmap(df_top_5_countries, x='Country', y='Sales')
    st.plotly_chart(fig_heatmap_top_5, use_container_width=True)

# Close the bordered container
st.markdown('</div>', unsafe_allow_html=True)
