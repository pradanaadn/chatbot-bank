import streamlit as st
import os
import sys
from loguru import logger
from scripts.credential import load_llm_env_key
from scripts.embedding_manager import EmbeddingManager
from scripts.retrieval_agent_manager import RetrievalAgentManager


load_llm_env_key()
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

@st.cache_resource()
def load_vector_db():
    return EmbeddingManager().get_vectordb()


logger.info((os.listdir(os.getcwd()), os.getcwd()))

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


vector_db = load_vector_db()
agent = RetrievalAgentManager(
    vectordb=vector_db,
)

st.markdown(
    "<h1 style='text-align: center; '>🏦 <span style='color:orange'>Bank</span>  Product Chatbot 🏦</h1>",
    unsafe_allow_html=True,
)
st.divider()


chat_input = st.chat_input("Ask your question here")


if chat_input:
    st.session_state["chat_history"].append(dict(role="user", content=chat_input))
    response = agent.generate_message(chat_input)
    st.session_state["chat_history"].append(dict(role="ai", content=response))

    
for chat in st.session_state["chat_history"]:
    st.chat_message(name=chat["role"]).write(chat["content"])
