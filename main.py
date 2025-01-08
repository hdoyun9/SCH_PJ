import streamlit as st

st.title("My first APP")

st.write("\n\n")

st.write("Hello! I'm Peter!")
st.write("My E-mail adress: hdoyun9@gmail.com")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
