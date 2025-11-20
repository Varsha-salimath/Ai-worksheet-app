import streamlit as st
<<<<<<< HEAD
import base64
from config.settings import configure_page
from services.gemini_service import initialize_gemini
from services.analytics_service import inject_analytics_script, track_event, EVENT_GENERATE_MAIN
=======
from config.settings import configure_page
from services.gemini_service import initialize_gemini
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
from styles.css_styles import apply_custom_css
from components.navigation import render_navigation
from components.hero import render_hero_section
from components.features import render_features_section
from components.footer import render_footer
from components.worksheet_form import render_worksheet_form
<<<<<<< HEAD
from dotenv import load_dotenv
load_dotenv()

=======
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f

# Initialize
configure_page()
initialize_gemini()
apply_custom_css()

<<<<<<< HEAD
# Inject Analytics Script (Umami/Plausible/PostHog)
inject_analytics_script()

=======
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_generator" not in st.session_state:
    st.session_state.show_generator = False
<<<<<<< HEAD
if "show_admin" not in st.session_state:
    st.session_state.show_admin = False
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Helper function to load logo
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.warning(f"Logo not found: {e}")
        return None

# Load logo
LOGO_PATH = "assets/images/logo.png"
logo_base64 = get_base64_image(LOGO_PATH)

# Check for admin URL parameter
query_params = st.query_params
if "admin" in query_params:
    st.session_state.show_admin = True
=======
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f

# Render Navigation
render_navigation()

<<<<<<< HEAD
# ==================
# ADMIN DASHBOARD
# ==================
if st.session_state.show_admin:
    from admin.dashboard import render_admin_dashboard
    
    if st.button("🏠 Back to Home", key="admin_back_btn"):
        st.session_state.show_admin = False
        st.query_params.clear()
        st.rerun()
    
    render_admin_dashboard()

# ==================
# WORKSHEET GENERATOR
# ==================
elif st.session_state.show_generator:
    st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
    
    if st.button("🏠 Back to Home", key="back_btn"):
        st.session_state.show_generator = False
        st.rerun()
    
    render_worksheet_form()

# ==================
# LANDING PAGE
# ==================
else:
    render_hero_section()
    
    # Center button with analytics tracking
=======
# Main Content
if not st.session_state.show_generator:
    # Landing Page
    render_hero_section()
    
    # Center button
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    st.markdown("<div class='button-center'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Generate Worksheets", key="start_btn"):
<<<<<<< HEAD
            # ANALYTICS: Track Button 1 click (Landing page main CTA)
            track_event("generate_main_clicked", {
                "source": "hero_section",
                "page": "landing"
            })
            
            st.session_state.show_generator = True
            st.session_state.button_clicked = True
=======
            st.session_state.show_generator = True
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    render_features_section()
    render_footer()
<<<<<<< HEAD

# Footer note for admin access
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; opacity: 0.3; font-size: 0.7rem;'>
        <a href='?admin=true' style='color: #6b7280; text-decoration: none;'>Admin</a>
    </div>
    """,
    unsafe_allow_html=True
)
=======
else:
    # Worksheet Generator
    st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
    
    if st.button("Back to Home", key="back_btn"):
        st.session_state.show_generator = False
        st.rerun()
    
    render_worksheet_form()
    # In app.py — ADD THESE LINES

import base64

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.warning(f"THANK YOU FOR VISITING")
        return None

# Load logo — UPDATE THIS PATH TO YOUR ACTUAL FILE
LOGO_PATH = r"C:\Users\Saraga Sundar\Downloads\svgtopng\logo (1).png"
logo_base64 = get_base64_image(LOGO_PATH)
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
