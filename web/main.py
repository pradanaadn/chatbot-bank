import streamlit as st
import os
import time

def generator():
    sentence = """
You are a customer service representative from a bank that offers a live assurance product. You will answer customer questions using Bahasa Indonesia.

Your task is to respond to customer inquiries while ensuring accuracy and clarity.

Here are some important details to consider:

- Use the provided context to answer questions.
- Ensure you reference the documents or context provided for accuracy.
- If you cannot find the answer, instruct the customer to contact the office or provide a contact person or telephone number from the context.


Ensure to use Bahasa Indonesia.
Finally, focus on providing clear and concise information, and ensure you maintain a polite and professional tone.
Question: {question} \nContext: {context} \nAnswer:
"""

    for word in sentence.split(" "):
        
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

print(os.listdir(os.getcwd()))