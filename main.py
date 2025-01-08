import streamlit as st
import time as ts

# 세션 상태 초기화
if "show_me_button" not in st.session_state:
    st.session_state.show_me_button = False  # 처음에는 me 버튼이 표시되지 않음

st.title("My first APP")

st.write("\n\n")
st.markdown("**This is my Prototype App**")
st.write("\n")
st.markdown(''':rainbow[Imaginary]''')

# Reset 버튼 동작
if st.button("Reset", type="primary"):
    st.write("Aha! Nothing! You really wanna reset?")
    ts.sleep(1)
    st.write("Then press 'me!'. I'm not kidding this time~")
    st.session_state.show_me_button = True  # Reset 버튼 클릭 시 me 버튼 표시

# What's in the box? 버튼
if st.button("What's in the box?"):
    st.write("Nothing in the box!")
    ts.sleep(2)
    st.write("OK, press 'Reset' button.")

# me 버튼 표시 여부
if st.session_state.show_me_button:
    st.button("me!", type="tertiary")
