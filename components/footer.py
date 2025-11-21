import streamlit as st

def render_footer():
    """Render footer section"""
    st.markdown(
        """
        <div class='footer'>
            <p style='font-size: 1.1rem; font-weight: 600; color: #ffffff; margin-bottom: 0.5rem;'>
                2025 Infinity Sheets | Powered by Google Gemini AI
            </p>
            <p style='font-weight: 700; color: #00d9ff; margin-top: 0.5rem;'>
                Infinity Learn Sri Chaitanya Educational Institutions
            </p>
            <p style='margin-top: 1rem; font-size: 0.9rem;'>
                Exploring the universe of education, one worksheet at a time
            </p>
        </div>
        <div class='footer'>
                <span class='footer-warning-icon'>⚠️</span>
                <span>Note: Worksheets are AI-generated and may contain inaccuracies. Please review content before use.</span>
            </div>
        """,
        unsafe_allow_html=True
    )