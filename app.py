# app.py — CORRECTED VERSION

import streamlit as st
import base64  # <-- Keep this import

from config.settings import configure_page
from services.gemini_service import initialize_gemini
from styles.css_styles import apply_custom_css
from components.navigation import render_navigation
from components.hero import render_hero_section
from components.features import render_features_section
from components.footer import render_footer
from components.worksheet_form import render_worksheet_form

# Initialize App
configure_page()
initialize_gemini()
apply_custom_css()

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_generator" not in st.session_state:
    st.session_state.show_generator = False

# --- ✅ LOAD LOGO BEFORE RENDERING NAVIGATION ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.warning(f"⚠️ Failed to load logo: {image_path} | Error: {e}")
        return None

# ✅ Use YOUR exact path
LOGO_PATH = r"C:\Users\Saraga Sundar\ai_worksheet_app\assets\images\logo (1).png"
logo_base64 = get_base64_image(LOGO_PATH)

# --- ✅ NOW RENDER NAVIGATION WITH THE LOGO ---
render_navigation(logo_base64=logo_base64)

# --- MAIN CONTENT BEGINS HERE ---
if not st.session_state.show_generator:
    render_hero_section()
    
    # Center button
    st.markdown("<div class='button-center'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Generate Worksheets", key="start_btn"):
            st.session_state.show_generator = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    render_features_section()
    render_footer()
else:
    # Worksheet Generator
    st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
    
    if st.button("Back to Home", key="back_btn"):
        st.session_state.show_generator = False
        st.rerun()
    
    render_worksheet_form()