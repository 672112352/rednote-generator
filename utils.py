from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
import os
from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, openai_api_key):
    # 修改1：使用 openai_api_key 参数名
    model = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=openai_api_key,  # 关键修改：使用 openai_api_key
        base_url="https://api.deepseek.com",  # DeepSeek API地址
        timeout=30.0
    )

    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]


# 修改2：修正环境变量名拼写错误
# 原代码是 DEEPSEK_API_KEY（少了一个E），应该是 DEEPSEEK_API_KEY
#memory = ConversationBufferMemory(return_messages=True)
#api_key = os.getenv("DEEPSEEK_API_KEY")  # 注意：是 DEEPSEEK，不是 DEEPSEK

#if not api_key:
 #   print("错误: 未找到 DEEPSEEK_API_KEY 环境变量")
 #   print("请先设置环境变量:")
 #   print("在命令行执行: set DEEPSEEK_API_KEY=sk-your-api-key")
#else:
    # 修改3：使用正确的变量名
#    result1 = get_chat_response("牛顿提出过哪些知名的定律？", memory, api_key)
 #   print("回答1:", result1)

  #  result2 = get_chat_response("我上一个问题是啥？", memory, api_key)
 #   print("回答2:", result2)