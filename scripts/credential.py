import streamlit as st
from loguru import logger
from os import environ
GEMINI_API_KEY = st.secrets.LLM_CREDENTIALS.GEMINI_API_KEY


def load_llm_env_key():
    logger.info(GEMINI_API_KEY)
    if environ["GOOGLE_API_KEY"] is None:
        if GEMINI_API_KEY is not None:
            environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
            logger.success("Success add GEMINI API KEY to environment variable")
        else:
            logger.error("Can not find any Gemini API Key")