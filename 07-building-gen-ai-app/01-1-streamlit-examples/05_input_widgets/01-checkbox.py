import streamlit as st

agree = st.checkbox("I agree")

print("agree:", agree)

if agree:
    st.write("Great!")