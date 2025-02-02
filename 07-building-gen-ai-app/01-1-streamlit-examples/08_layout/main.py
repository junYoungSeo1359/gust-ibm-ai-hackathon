import os
import streamlit as st
import pandas as pd

# Sidebar
with st.sidebar:
    st.write("Text in the sidebar")

# Columns
col1, col2, col3 = st.columns(3)

col1.write("Text in a column")

slider = col2.slider("Choose a number", min_value=0, max_value=10)

col3.write(slider)

# Tabs
file_path = os.path.join(os.getcwd(), "07-building-gen-ai-app", "01-1-streamlit-examples", "08_layout", "data", "sample.csv")
df = pd.read_csv(file_path)

tab1, tab2 = st.tabs(["Line plot", "Bar plot"])

with tab1:
    tab1.write("A line plot")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
    tab2.write("A bar plot")
    st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Expander (collapsible element)
with st.expander("Click to expand"):
    st.write("I am text that you only see when you expand")

# Container

with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")
