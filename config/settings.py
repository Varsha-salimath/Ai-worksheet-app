import streamlit as st
import os
from dotenv import load_dotenv

def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Infinity Sheets",
        page_icon="🪐",
        layout="wide"
    )

def load_api_key():
    """Load and return Google API key"""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("❌ Gemini API key not found. Please add it to your .env file as GOOGLE_API_KEY.")
        st.stop()
    
    return api_key.strip()

# User location
USER_LOCATION = "Bengaluru, Karnataka, IN"