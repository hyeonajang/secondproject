import streamlit as st
import random

# 세션 상태 초기화
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None

# 앱 제목
st.title("가위바위보 게임")

# 게임 설명
st.markdown("컴퓨터와 함께 가위바위보를 즐겨보세요!")

# 게임 시작 버튼
if not st.session_state.game_started:
    if st.button("게임 시작"):
        st.session_state.game_started = True
        st.experimental_rerun()

# 게임 진행 중
if st.session_state.game_started:
    # 사용자 선택
    user_choice = st.radio("무엇을 낼까요?", ('가위', '바위', '보'))
    st.session_state.user_choice = user_choice

    # 컴퓨터의 선택
    choices = ['가위', '바위', '보']
    st.session_state.computer_choice = random.choice(choices)

    # 게임 결과 계산
    def determine_winner(user, computer):
        if user == computer:
            return "무승부"
        elif (user == '가위' and computer == '보') or \
             (user == '바위' and computer == '가위') or \
             (user == '보' and computer == '바위'):
            return "승리!"
        else:
            return "패배"

    # 결과 표시
    if st.session_state.user_choice:
        st.write(f"당신의 선택: {st.session_state.user_choice}")
        st.write(f"컴퓨터의 선택: {st.session_state.computer_choice}")
        result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)
        st.write(f"결과: {result}")

    # 게임 초기화 버튼
    if st.button("게임 초기화"):
        st.session_state.game_started = False
        st.session_state.user_choice = None
        st.session_state.computer_choice = None
        st.session_state.result = None
        st.experimental_rerun()
