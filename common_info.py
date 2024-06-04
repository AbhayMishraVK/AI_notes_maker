import os
import time
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from openai import OpenAI

load_dotenv()

model_name = "llama3-70b-8192"


def model_load(temperature=0.7):
    open_ai_api_key = os.getenv("GRAQ_API_KEY")
    if not open_ai_api_key and 'api_key' in st.session_state:
        open_ai_api_key = st.session_state['api_key']
    time.sleep(1)
    model_open_ui = ChatGroq(
        model_name=model_name,
        groq_api_key=open_ai_api_key,
        temperature=temperature
    )
    return model_open_ui


