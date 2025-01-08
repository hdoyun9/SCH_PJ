import streamlit as st
import random as rd
import time as ts

st.title("My first APP")

st.write("\n\n")

st.markdown("**This is my Prototype App**")

st.write("\n")

st.markdown(''':ranbow[Imaginary]''')

if st.button("Reset", type="primary"):
    st.write("AHahah! nothiing! you really wanna reset?")
if st.button("What's in the box?"):
    st.write("Nothing in the box!")
    ts.sleep(2)
    st.write("ok press 'Reset'botton.")
    
else:
    st.write("-Waiting-")
