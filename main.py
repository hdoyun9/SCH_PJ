import streamlit as st
import random

# 세션 상태 초기화
if "box_clicked" not in st.session_state:
    st.session_state.box_clicked = False  # 'What's in the box?' 버튼 상태
if "show_me_button" not in st.session_state:
    st.session_state.show_me_button = False  # me 버튼 표시 여부
if "show_me_only" not in st.session_state:
    st.session_state.show_me_only = False  # 모든 버튼 숨기고 me만 표시 여부
if "correct_index" not in st.session_state:
    st.session_state.correct_index = random.randint(1, 20)  # 정답 버튼의 인덱스 설정

# 상태 리셋 함수
def reset_app():
    st.session_state.box_clicked = False
    st.session_state.show_me_button = False
    st.session_state.show_me_only = False
    st.session_state.correct_index = random.randint(1, 20)  # 정답 버튼 재설정

st.title("My first APP")
st.write("\n\n")
st.markdown("**This is my Prototype App**")
st.write("\n")
st.markdown(''':rainbow[Imaginary]''')

# 모든 버튼 숨기고 me 버튼만 표시 상태
if st.session_state.show_me_only:
    st.write("Choose one of the 'me!' buttons!")

    # 20개의 me 버튼 생성
    for i in range(1, 21):
        if st.button(f"me! {i}"):
            if i == st.session_state.correct_index:  # 정답 버튼 클릭
                reset_app()
                st.success("You chose the right one! It's your gift! 🎉")
                st.write("[Click here to claim your gift!](https://youtu.be/dQw4w9WgXcQ?si=uvdbW7XaQ6f84BGU)")  # 링크 표시
                  # 상태 초기화
            else:  # 오답 버튼 클릭
                st.error("Wrong choice! Try another one!")
else:
    # Reset 버튼
    if st.button("Reset", type="primary"):
        if st.session_state.box_clicked:  # 'What's in the box?' 버튼이 눌린 경우
            st.write("Aha! Nothing! You really wanna reset?")
            st.session_state.show_me_button = True
        else:
            st.write("You need to check 'What's in the box?' first!")

    # What's in the box? 버튼
    if st.button("What's in the box?"):
        st.write("Nothing in the box!")
        st.session_state.box_clicked = True

    # me 버튼
    if st.session_state.show_me_button:
        if st.button("me!", type="tertiary"):
            # 'me!' 버튼 클릭 시 다른 버튼 숨기기
            st.session_state.show_me_only = True
