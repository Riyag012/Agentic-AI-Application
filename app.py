import streamlit as st
from phi.agent import Agent 
from phi.model.google import Gemini 
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import get_file, upload_file
from google.generativeai import genai 


from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key="API_KEY")

st.set_page_config(
    page_title="Multi Modal AI Agent - Video Summarizer",
    layout="wide"
)

st.title("Phidata Video Summarizer")
st.header("Powered by Gemini 2.0 Flash Exp")

def initialize_agent():
    return Agent(
        name="AI Video Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

multimodal_agent = initialize_agent()

