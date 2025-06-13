import streamlit as st
import random
st.title("가위바위보 게임")
st.markdown("컴퓨터와 함께 가위바위보를 즐겨보세요!")
user_choice = st.radio(
    "무엇을 낼까요?",
    ('가위', '바위', '보')
)
choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)
def determine_winner(user, computer):
    if user == computer:
        return "무승부"
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
        return "승리!"
    else:
        return "패배"
if user_choice:
    st.write(f"당신의 선택: {user_choice}")
    st.write(f"컴퓨터의 선택: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    st.write(f"결과: {result}")
if st.button("게임 시작"):
    st.experimental_rerun()
