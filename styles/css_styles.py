import streamlit as st

def apply_custom_css():
    """Apply all custom CSS styling with clean inputs and sticky buttons"""
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
            
            * {
                font-family: 'Inter', sans-serif;
                box-sizing: border-box;
            }
            
            .stApp {
                background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
                color: #ffffff;
            }
            
            /* CRITICAL: Hide Streamlit default elements */
            #MainMenu {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            header {visibility: hidden !important;}
            .stDeployButton {display: none !important;}
            
            /* CRITICAL: Main container fixes */
            .main .block-container {
                padding-top: 6rem !important;
                padding-bottom: 8rem !important;
                max-width: 100% !important;
            }
            
            /* Top Navigation - Fixed */
            .top-nav {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: 80px;
                background: rgba(10, 14, 39, 0.98);
                backdrop-filter: blur(20px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 4rem;
                z-index: 1000;
            }
            
            .nav-logo-section {
                display: flex;
                align-items: center;
                gap: 1rem;
            }
            
            .nav-logo-img {
                height: 50px;
                width: auto;
                object-fit: contain;
            }
            
            .nav-tagline {
                font-size: 0.85rem;
                color: #6b7280;
                font-weight: 500;
            }
            
            .contact-info {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                color: #00d9ff;
                font-weight: 600;
                font-size: 0.95rem;
            }
            
            /* Hero Section */
            .hero-container {
                margin-top: 100px;
                min-height: 70vh;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 3rem 4rem;
            }
            
            .hero-left {
                flex: 1;
                max-width: 700px;
            }
            
            .hero-title {
                font-size: 4.5rem;
                font-weight: 900;
                line-height: 1.1;
                margin-bottom: 1.5rem;
                color: #ffffff;
            }
            
            .hero-title .gradient-text {
                background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .hero-subtitle {
                font-size: 1.3rem;
                color: #9ca3af;
                margin-bottom: 1.5rem;
                line-height: 1.6;
            }
            
            .hero-description {
                font-size: 1.05rem;
                color: #6b7280;
                margin-bottom: 2rem;
                line-height: 1.7;
            }
            
            .hero-right {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .ai-avatar {
                width: 450px;
                height: 450px;
                border-radius: 50%;
                background: linear-gradient(135deg, rgba(0, 217, 255, 0.15), rgba(168, 85, 247, 0.15));
                border: 3px solid rgba(0, 217, 255, 0.3);
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 0 80px rgba(0, 217, 255, 0.3);
                overflow: hidden;
                animation: float 3s ease-in-out infinite;
            }
            
            .ai-avatar img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 50%;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
            
            .button-center {
                display: flex;
                justify-content: center;
                margin: 2rem 0;
            }
            
            .button-center .stButton > button {
                max-width: 400px !important;
                min-width: 280px !important;
            }
            
            /* Features Section */
            .features-section {
                padding: 5rem 4rem;
                background: rgba(255, 255, 255, 0.02);
            }
            
            .section-title {
                font-size: 2.5rem;
                font-weight: 800;
                text-align: center;
                margin-bottom: 1rem;
                background: linear-gradient(135deg, #ffffff 0%, #00d9ff 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .section-subtitle {
                text-align: center;
                color: #8b92b0;
                font-size: 1.1rem;
                margin-bottom: 4rem;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 2rem;
                max-width: 1400px;
                margin: 0 auto;
            }
            
            .feature-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 2.5rem;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            
            .feature-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #00d9ff, #a855f7);
                transform: scaleX(0);
                transition: transform 0.3s ease;
            }
            
            .feature-card:hover::before {
                transform: scaleX(1);
            }
            
            .feature-card:hover {
                background: rgba(255, 255, 255, 0.05);
                border-color: rgba(0, 217, 255, 0.3);
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0, 217, 255, 0.2);
            }
            
            .feature-icon {
                font-size: 3rem;
                margin-bottom: 1.5rem;
            }
            
            .feature-title {
                font-size: 1.3rem;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 1rem;
            }
            
            .feature-text {
                font-size: 1rem;
                color: #8b92b0;
                line-height: 1.6;
            }
            
            /* Form Title */
            .form-title {
                font-size: 2.5rem;
                font-weight: 800;
                text-align: center;
                margin-bottom: 2rem;
                background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            /* ========================================
               BUTTONS - VISIBLE & STYLED
               ======================================== */
            
            /* Regular buttons - SOLID BLUE WITH WHITE TEXT */
            .stButton > button,
            .stDownloadButton > button {
                background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 50px !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                padding: 1rem 3rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 10px 30px rgba(37, 99, 235, 0.4) !important;
                width: 100% !important;
                max-width: 500px !important;
                display: block !important;
                margin: 2rem auto !important;
                cursor: pointer !important;
            }
            
            .stButton > button:hover,
            .stDownloadButton > button:hover {
                background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%) !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 40px rgba(37, 99, 235, 0.6) !important;
                color: #ffffff !important;
            }
            
            /* Make sure button is visible */
            .stButton,
            .stDownloadButton {
                display: block !important;
                text-align: center !important;
                margin: 2rem 0 !important;
                padding-bottom: 2rem !important;
            }
            
            /* Loading Animation Container */
            .loading-animation {
                text-align: center;
                padding: 2rem;
                margin: 2rem 0;
            }
            
            .sparkle-container {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 1rem;
                margin: 2rem 0;
            }
            
            .sparkle-text {
                color: #2563eb;
                font-size: 1.3rem;
                font-weight: 700;
                animation: pulse 1.5s ease-in-out infinite;
            }
            
            .sparkle {
                display: inline-block;
                font-size: 2rem;
                animation: sparkle 1.5s ease-in-out infinite;
            }
            
            @keyframes sparkle {
                0%, 100% {
                    transform: scale(1) rotate(0deg);
                    opacity: 1;
                }
                50% {
                    transform: scale(1.3) rotate(180deg);
                    opacity: 0.7;
                }
            }
            
            @keyframes pulse {
                0%, 100% {
                    opacity: 1;
                }
                50% {
                    opacity: 0.6;
                }
            }
            
            /* Falling Stars Animation */
            .falling-stars {
                position: relative;
                width: 100%;
                height: 100px;
                overflow: hidden;
            }
            
            .star {
                position: absolute;
                width: 20px;
                height: 20px;
                font-size: 1.5rem;
                animation: fall 2s linear infinite;
            }
            
            .star:nth-child(1) { left: 10%; animation-delay: 0s; }
            .star:nth-child(2) { left: 30%; animation-delay: 0.5s; }
            .star:nth-child(3) { left: 50%; animation-delay: 1s; }
            .star:nth-child(4) { left: 70%; animation-delay: 1.5s; }
            .star:nth-child(5) { left: 90%; animation-delay: 0.8s; }
            
            @keyframes fall {
                0% {
                    top: -20px;
                    opacity: 1;
                }
                100% {
                    top: 100px;
                    opacity: 0;
                }
            }
            
            /* Sticky button container */
            .sticky-button-container {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: rgba(10, 14, 39, 0.98);
                backdrop-filter: blur(20px);
                border-top: 1px solid rgba(255, 255, 255, 0.08);
                padding: 1.5rem 4rem;
                z-index: 999;
                box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.3);
            }
            
            .sticky-button-container .stButton > button {
                max-width: 400px;
                margin: 0 auto;
                display: block;
            }
            
            /* ========================================
               INPUT FIELDS - WHITE BG, BLACK TEXT
               ======================================== */
            
            /* LABELS → White, Bold */
            .stTextInput label,
            .stNumberInput label,
            .stSelectbox label,
            .stTextArea label,
            .stCheckbox label {
                color: #ffffff !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                display: block !important;
                margin-bottom: 0.75rem !important;
            }
            
            /* TEXT & NUMBER INPUTS → White background + Black text */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input,
            .stTextArea > div > div > textarea {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                border-radius: 12px !important;
                color: #000000 !important;
                font-size: 1.05rem !important;
                font-weight: 600 !important;
                padding: 1.2rem 1.5rem !important;
                min-height: 60px !important;
                transition: all 0.3s ease !important;
            }
            
            /* Placeholder text → Grey */
            .stTextInput > div > div > input::placeholder,
            .stTextArea > div > div > textarea::placeholder {
                color: #6b7280 !important;
                font-weight: 500 !important;
            }
            
            /* FOCUS → Blue glow */
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            .stTextArea > div > div > textarea:focus {
                border-color: #00d9ff !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.25) !important;
                outline: none !important;
            }
            
            /* SELECTBOX → White background + Black text - SMALLER SIZE */
            div[data-baseweb="select"] > div {
                background: #ffffff !important;
                border-radius: 10px !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                color: #000000 !important;
                padding: 0.85rem 1.2rem !important;
                min-height: 48px !important;
                font-size: 0.95rem !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
                display: flex !important;
                align-items: center !important;
            }
            
            /* Selectbox selected value text - ALL variations */
            div[data-baseweb="select"] span,
            div[data-baseweb="select"] div,
            div[data-baseweb="select"] > div > div {
                color: #000000 !important;
                font-weight: 600 !important;
            }
            
            /* Selectbox dropdown arrow - make it visible */
            div[data-baseweb="select"] svg,
            div[data-baseweb="select"] svg path {
                fill: #000000 !important;
                color: #000000 !important;
                stroke: #000000 !important;
            }
            
            /* Selectbox placeholder */
            div[data-baseweb="select"] [aria-selected="false"] {
                color: #6b7280 !important;
            }
            
            /* Selectbox focus */
            div[data-baseweb="select"]:focus-within > div {
                border-color: #00d9ff !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.25) !important;
            }
            
            /* Dropdown menu */
            div[data-baseweb="popover"] {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                border-radius: 12px !important;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
            }
            
            /* Dropdown options */
            div[role="option"] {
                color: #000000 !important;
                padding: 0.75rem 1rem !important;
                font-weight: 600 !important;
                background: #ffffff !important;
            }
            
            div[role="option"]:hover {
                background: rgba(0, 217, 255, 0.1) !important;
                color: #000000 !important;
            }
            
            /* Selected option in dropdown */
            div[role="option"][aria-selected="true"] {
                background: rgba(0, 217, 255, 0.2) !important;
                color: #000000 !important;
            }
            
            /* CHECKBOX → White background + visible label */
            .stCheckbox > label {
                display: flex !important;
                align-items: center !important;
                gap: 0.75rem !important;
            }
            
            .stCheckbox > label > div:first-child {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                border-radius: 6px !important;
                width: 24px !important;
                height: 24px !important;
            }
            
            .stCheckbox > label > div:last-child {
                color: #ffffff !important;
                font-weight: 600 !important;
                font-size: 1.05rem !important;
            }
            
            /* Checkbox checked state */
            .stCheckbox input:checked + div {
                background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%) !important;
                border-color: #00d9ff !important;
            }
            
            /* ========================================
               MOBILE RESPONSIVE
               ======================================== */
            
            @media (max-width: 768px) {
                .top-nav {
                    padding: 0 1.5rem;
                    height: 70px;
                    flex-wrap: wrap;
                    gap: 0.5rem;
                }
                
                .nav-logo-img {
                    height: 40px;
                }
                
                .nav-tagline {
                    font-size: 0.7rem;
                    display: none;
                }
                
                .contact-info {
                    font-size: 0.8rem;
                    width: 100%;
                    justify-content: center;
                    margin-top: 0.5rem;
                }
                
                .hero-container {
                    flex-direction: column;
                    padding: 2rem 1.5rem;
                    margin-top: 80px;
                    min-height: auto;
                }
                
                .hero-left {
                    max-width: 100%;
                    text-align: center;
                    margin-bottom: 2rem;
                }
                
                .hero-title {
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }
                
                .hero-subtitle {
                    font-size: 1.1rem;
                    margin-bottom: 1rem;
                }
                
                .hero-description {
                    font-size: 0.95rem;
                    margin-bottom: 1.5rem;
                }
                
                .hero-right {
                    margin-top: 1rem;
                }
                
                .ai-avatar {
                    width: 280px;
                    height: 280px;
                }
                
                .button-center {
                    margin: 1.5rem 0;
                }
                
                .features-section {
                    padding: 3rem 1.5rem;
                }
                
                .section-title {
                    font-size: 2rem;
                    margin-bottom: 0.5rem;
                }
                
                .section-subtitle {
                    font-size: 1rem;
                    margin-bottom: 3rem;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                    gap: 1.5rem;
                }
                
                .feature-card {
                    padding: 2rem 1.5rem;
                }
                
                .feature-icon {
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }
                
                .feature-title {
                    font-size: 1.2rem;
                }
                
                .feature-text {
                    font-size: 0.95rem;
                }
                
                .form-title {
                    font-size: 2rem;
                    margin-bottom: 1.5rem;
                }
                
                .sticky-button-container {
                    padding: 1rem 1.5rem;
                }
                
                .stButton > button {
                    font-size: 1rem !important;
                    padding: 0.9rem 2rem !important;
                }
                
                .stTextInput > div > div > input,
                .stNumberInput > div > div > input,
                .stTextArea > div > div > textarea {
                    font-size: 0.95rem !important;
                    padding: 0.9rem 1.1rem !important;
                    min-height: 48px !important;
                }
                
                div[data-baseweb="select"] > div {
                    font-size: 0.9rem !important;
                    padding: 0.75rem 1rem !important;
                    min-height: 46px !important;
                }
                
                .stTextInput label,
                .stNumberInput label,
                .stSelectbox label,
                .stTextArea label,
                .stCheckbox label {
                    font-size: 0.95rem !important;
                }
                
                .footer {
                    padding: 2rem 1.5rem;
                    margin-top: 3rem;
                }
                
                .footer-warning {
                    padding: 1rem 1.5rem;
                    font-size: 0.85rem;
                    margin: 1.5rem 1rem;
                }
            }
            
            /* ========================================
               FOOTER - CENTERED & STYLED
               ======================================== */
            
            .footer {
                background: rgba(255, 255, 255, 0.02);
                border-top: 1px solid rgba(255, 255, 255, 0.08);
                padding: 3rem 2rem;
                text-align: center;
                margin-top: 5rem;
            }
            
            .footer p {
                margin: 0.5rem 0;
                line-height: 1.6;
            }
            
            .footer-warning {
                background: rgba(255, 193, 7, 0.1);
                border: 1px solid rgba(255, 193, 7, 0.3);
                border-radius: 12px;
                padding: 1.2rem 2rem;
                margin: 2rem auto;
                max-width: 900px;
                color: #ffc107;
                font-size: 0.95rem;
                font-weight: 600;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.75rem;
            }
            
            .footer-warning-icon {
                font-size: 1.5rem;
            }
                .hero-title {
                    font-size: 2rem;
                }
                
                .ai-avatar {
                    width: 250px;
                    height: 250px;
                }
                
                .section-title {
                    font-size: 1.75rem;
                }
                
                .form-title {
                    font-size: 1.75rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )