import streamlit as st
import random as rd

st.title("My first APP")

st.write("\n\n")

st.write("Hello! I'm Peter!")
st.write("My E-mail adress: hdoyun9@gmail.com")

st.button("Reset", type="primary")
if st.button("Create Random Number"):
    st.write(rd.randint(0,99999999))
else:
    st.write("-Waiting-")
