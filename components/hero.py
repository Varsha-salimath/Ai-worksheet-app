import streamlit as st
from utils.helpers import get_base64_image

def render_hero_section():
    """Render hero section with avatar"""
    
    # Update this path to your actual avatar image location
    aina_avatar_base64 = get_base64_image(r"C:\Users\Saraga Sundar\Downloads\20250910113600.jpg")
    
    avatar_html = ""
    if aina_avatar_base64:
        avatar_html = f'<img src="data:image/jpeg;base64,{aina_avatar_base64}" alt="AINA Avatar">'
    else:
        avatar_html = '<div style="font-size: 12rem;">🤖</div>'
    
    st.markdown(
        f"""
        <div class='hero-container'>
            <div class='hero-left'>
                <h1 class='hero-title'>
                    Meet <span class='gradient-text'>Infinity Sheets</span><br>
                    AI-Powered Worksheet Generator
                </h1>
                <p class='hero-subtitle'>
                    Instant worksheets, personalized support, and exam mastery - powered by AI, built for educators.
                </p>
                <p class='hero-description'>
                    Instantly create subject-specific, grade-aligned, and difficulty-based worksheets 
                    powered by Google Gemini — built for educators by Infinity Learn.
                </p>
            </div>
            <div class='hero-right'>
                <div class='ai-avatar'>
                    {avatar_html}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )