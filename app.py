import streamlit as st
import base64
from datetime import datetime
from config.settings import configure_page
from services.gemini_service import initialize_gemini, get_session_id, langfuse, langfuse_enabled
from services.analytics_service import inject_analytics_script, track_event
from styles.css_styles import apply_custom_css
from components.navigation import render_navigation
from components.hero import render_hero_section
from components.features import render_features_section
from components.footer import render_footer
from components.worksheet_form import render_worksheet_form
from dotenv import load_dotenv
load_dotenv()

# Initialize
configure_page()
initialize_gemini()
apply_custom_css()

# Inject Analytics Script
inject_analytics_script()

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_generator" not in st.session_state:
    st.session_state.show_generator = False
if "show_admin" not in st.session_state:
    st.session_state.show_admin = False
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Helper function for Langfuse event logging (compatible with v2 and v3)
def log_langfuse_event(event_name, metadata):
    """Log event to Langfuse with version compatibility"""
    if not langfuse_enabled or not langfuse:
        return
    
    try:
        # Try Langfuse v3 API
        trace = langfuse.trace(
            name=event_name,
            user_id=get_session_id(),
            metadata=metadata
        )
        print(f"✅ Langfuse v3: {event_name} tracked")
    except (AttributeError, TypeError):
        # Fallback to Langfuse v2 API
        try:
            langfuse.log(
                name=event_name,
                user_id=get_session_id(),
                properties=metadata
            )
            print(f"✅ Langfuse v2: {event_name} tracked")
        except Exception as e:
            print(f"⚠️ Langfuse logging failed: {e}")

# Helper function to load logo
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        return None

# Load logo
LOGO_PATH = "assets/images/logo.png"
logo_base64 = get_base64_image(LOGO_PATH)

# Check admin URL
query_params = st.query_params
if "admin" in query_params:
    st.session_state.show_admin = True

# Render Navigation
render_navigation()

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
    
    # Main CTA button with Langfuse tracking
    st.markdown("<div class='button-center'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Generate Worksheets", key="start_btn"):
            # LANGFUSE EVENT: Landing page button clicked
            log_langfuse_event("click_generate_worksheet_landing_page", {
                "button": "landing_page_cta",
                "timestamp": datetime.now().isoformat(),
                "source": "hero_section",
                "page": "landing"
            })
            
            # Analytics tracking
            track_event("generate_main_clicked", {
                "source": "hero_section",
                "page": "landing"
            })
            
            st.session_state.show_generator = True
            st.session_state.button_clicked = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    render_features_section()
    render_footer()

# Footer note for admin access
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; opacity: 0.3; font-size: 0.7rem;'>
        <a href='?admin=true' style='color: #6b7280; text-decoration: none;'>Admin</a>
    </div>
    """,
    unsafe_allow_html=True
)