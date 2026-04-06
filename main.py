import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_chat_response

st.title("💬克隆ChatGPT")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入deepseek API密钥：", type="password")
    st.markdown("[获取deepseek API密钥](https://deepseek.ai/deepseek-api)")

    # 添加清除对话按钮
    if st.button("🔄 清除对话历史", type="primary"):
        # 清空会话状态中的消息和记忆
        st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = [{"role": "ai",
                                         "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]
        st.success("对话历史已清除！")
        st.rerun()  # 重新运行应用以刷新界面

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not deepseek_api_key:
        st.info("请输入你的API key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     deepseek_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
