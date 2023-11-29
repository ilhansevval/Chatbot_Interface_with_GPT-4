import streamlit as st
import openai
from api_key import openai_api_key
from about import about

openai_api_key_file = openai_api_key

with st.sidebar:
    about()
    st.write('  ') 
    st.markdown("""---""")
    openai_api_key = st.text_input("# OpenAI API Key", key="chatbot_api_key", type="password")
    col1, col2 = st.columns([1,5], gap="medium")
    with col2:
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("Chatbot Interface with GPT-4") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Write a message"):

    if not openai_api_key and not openai_api_key_file:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    if openai_api_key_file:
        openai.api_key = openai_api_key_file
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-4", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)