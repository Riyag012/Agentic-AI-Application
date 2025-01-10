import streamlit as st
from phi.agent import Agent 
from phi.model.google import Gemini 
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptAvailable, VideoUnavailable


from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key="API_KEY")

st.set_page_config(
    page_title="Multi Modal AI Agent - YouTube Video Summarizer",
    page_icon= "🎥",
    layout="wide"
)

st.title("Phidata Video Summarizer")
st.header("Powered by Gemini 1.5 Flash")

def initialize_agent():
    return Agent(
        name="AI YouTube Video Summarizer",
        model=Gemini(id="gemini-1.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True
    )
# initialize agent
multimodal_agent = initialize_agent()

youtube_url = st.text_input(
    "Paste Youtube Video URL here: ",
    placeholder="eg., https://www.youtube.com/watch?v=example",
    help="Provide a YouTube Video URL for summarization"
)

def get_video_id(url):
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("?")[0]
    return None

if st.button("🔍 Summarize Video", key="summarize_video_button"):
    video_id = get_video_id(youtube_url)
    if not video_id:
        st.warning("Invalid yt url, try again")
    else:
        try:
            with st.spinner("Processing video's transcript and gathering insights..."):
                transcipt = YouTubeTranscriptApi.get_transcript(video_id)
                video_text = " ".join(entry['text'] for entry in transcipt)

                analysis_promt = f"""
                Summarize the following video transcript for content and context:
                {video_text}

                Provide a detailed, user-friendly, and actionable summary.
                """
                response = multimodal_agent.run(analysis_promt)

            st.subheader("Summary")
            st.markdown(response.content)
            
        except NoTranscriptAvailable:
            st.error("Transcript Not Avaialable")

        except VideoUnavailable:
            st.error("Video Unavailable")

        except Exception as error:
            st.error(f"An error occured: {error}")