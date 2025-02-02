import os
import streamlit as st
import pandas as pd

file_path = os.path.join(os.getcwd(), "07-building-gen-ai-app", "01-1-streamlit-examples", "03_data_display_elements", "data", "sample.csv")
df = pd.read_csv(file_path, dtype="int")

st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label="Expenses", value=900, delta=20, delta_color="inverse")