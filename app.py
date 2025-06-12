# 가상환경 (poetry env activate 로 경로 얻음)
# C:\Users\KOSA\AppData\Local\pypoetry\Cache\virtualenvs\langchain-env-FnfOIDgU-py3.11\Scripts\activate.bat
# streamlit
# streamlit run src/app.py
# 질문 : 연봉 5000만원인 직장인의 종합소득세는?

import os
import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_message


st.set_page_config(
    page_title="소득세 챗봇",
    page_icon="💰",
    # layout="wide",
    # initial_sidebar_state="expanded"
)

st.title("소득세 챗봇 💰")
st.caption("소득세 관련 질문을 해보세요!")

load_dotenv()

if "message_list" not in st.session_state:
    st.session_state.message_list = []
    
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        


if user_question := st.chat_input(placeholder="소득세에 관해 궁금한 내용을 말씀해주세요."):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})
    
    
    with st.spinner("AI가 답변을 준비하는 중입니다..."):
        ai_response = get_ai_message(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({"role": "ai", "content": ai_message})

# print(f'after == {st.session_state.message_list}')
