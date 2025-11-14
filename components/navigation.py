# components/navigation.py
import streamlit as st

def render_navigation(logo_base64: str = None):
    """Render top navigation bar"""
    if logo_base64:
        logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="nav-logo-img" alt="Infinity Learn Logo">'
    else:
        logo_html = '''
        <div style="
            font-size: 1.8rem; 
            font-weight: 900; 
            background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
        ">Infinity Sheets</div>
        '''
    
    st.markdown(
        f"""
        <div class='top-nav'>
            <div class='nav-logo-section'>
                {logo_html}
                <div class='nav-tagline'></div>
            </div>
            <div class='nav-buttons'>
                <div class='contact-info'>
                    <span>need help? talk to experts</span>
                    <span style='font-weight: 800;'>7996668865</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )