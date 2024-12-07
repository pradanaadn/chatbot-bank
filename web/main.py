import streamlit as st
from persona.customer_service import persona_customer_service
import time

def generator():
    for word in persona_customer_service.split(" "):
        
        yield word + " "
        time.sleep(0.02)



st.markdown("<h1 style='text-align: center; '>🏦 <span style='color:orange'>Bank</span>  Product Chatbot 🏦</h1>", unsafe_allow_html=True)
st.divider()
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

chat_input = st.chat_input("Ask your question here")


if chat_input:
   st.chat_message("assistant").write_stream(generator())

  