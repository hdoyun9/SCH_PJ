import streamlit as st
import random as rd
import time as ts

# 세션 상태 초기화
if "me_button_disabled" not in st.session_state:
    st.session_state.me_button_disabled = True  # 초기 상태는 비활성화

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
    st.session_state.me_button_disabled = False  # Reset 버튼 클릭 시 활성화

# What's in the box? 버튼
if st.button("What's in the box?"):
    st.write("Nothing in the box!")
    ts.sleep(2)
    st.write("OK, press 'Reset' button.")

# me! 버튼 (disable 상태를 세션 상태로 제어)
st.button("me!", type="tertiary", disabled=st.session_state.me_button_disabled)
