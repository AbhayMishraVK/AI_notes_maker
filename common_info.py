import os
import time
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from openai import OpenAI

load_dotenv()

time_to_stop = 30
model_name = "llama3-70b-8192"


def model_load(open_ai_api_key, temperature=1):
    model_open_ui = ChatGroq(
        model_name=model_name,
        groq_api_key=open_ai_api_key,
        temperature=temperature
    )
    return model_open_ui


