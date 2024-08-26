import streamlit as st
from datetime import datetime, time 

st.header("Slider")
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")


st.header("Range slider")
values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

st.header("Time slider")
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.header("Datetime slider")

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
