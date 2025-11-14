import streamlit as st
import base64
import os

def load_image_base64(image_path):
    """Return base64 string of an image file."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def render_navigation():
    """Render the top navigation bar."""

    logo_path = "assets/images/logo.png"  # Update this to your renamed file

    # Load logo
    if os.path.exists(logo_path):
        logo_base64 = load_image_base64(logo_path)
        logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="nav-logo-img">'
    else:
        logo_html = "<div>Infinity Sheets</div>"

    st.markdown(
        f"""
        <div class='top-nav'>
            <div class='nav-logo-section'>
                {logo_html}
            </div>
            <div class='nav-buttons'>
                <div class='contact-info'>
                    <span>need help? talk to experts</span>
                    <span style='font-weight:800;'>7996668865</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
