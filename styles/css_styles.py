import streamlit as st

def apply_custom_css():
    """Apply all custom CSS styling - Professional & Clean"""
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
               BUTTONS - CLEAN & PROFESSIONAL
               ======================================== */
            
            /* Landing page buttons - Keep original gradient */
            .stButton > button {
                background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 50px !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                padding: 1rem 3rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 10px 30px rgba(0, 217, 255, 0.3) !important;
                width: 100% !important;
                max-width: 500px !important;
                display: block !important;
                margin: 2rem auto !important;
                cursor: pointer !important;
            }
            
            .stButton > button:hover {
                background: linear-gradient(135deg, #00b8d4 0%, #8b3fc7 100%) !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 40px rgba(0, 217, 255, 0.5) !important;
                color: #ffffff !important;
            }
            
            /* Form Submit Button - CLEAN, NO EMOJI */
            .stFormSubmitButton > button {
                background: #2563EB !important;
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
                cursor: pointer !important;
                margin: 0 auto !important;
                display: block !important;
            }
            
            .stFormSubmitButton > button:hover {
                background: #1E3A8A !important;
                color: #ffffff !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 40px rgba(37, 99, 235, 0.6) !important;
            }
            
            .stFormSubmitButton > button:disabled {
                background: #6b7280 !important;
                cursor: not-allowed !important;
                opacity: 0.6 !important;
            }
            
            /* Download button */
            .stDownloadButton > button {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 50px !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                padding: 1rem 3rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4) !important;
                width: 100% !important;
                max-width: 500px !important;
                display: block !important;
                margin: 2rem auto !important;
                cursor: pointer !important;
            }
            
            .stDownloadButton > button:hover {
                background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 40px rgba(16, 185, 129, 0.6) !important;
                color: #ffffff !important;
            }
            
            /* ========================================
               FULL SCREEN LOADING OVERLAY
               ======================================== */
            
            .loading-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(10, 14, 39, 0.95);
                backdrop-filter: blur(10px);
                z-index: 9999;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                animation: fadeIn 0.3s ease-in;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            .loading-content {
                text-align: center;
                max-width: 500px;
                padding: 2rem;
            }
            
            .loading-spinner {
                width: 80px;
                height: 80px;
                margin: 0 auto 2rem;
                border: 4px solid rgba(37, 99, 235, 0.2);
                border-top: 4px solid #2563EB;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .loading-title {
                font-size: 1.5rem;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 1rem;
            }
            
            .loading-subtitle {
                font-size: 1rem;
                color: #9ca3af;
                margin-bottom: 2rem;
            }
            
            /* Professional Sparkle Animation */
            .sparkles {
                position: absolute;
                width: 100%;
                height: 100%;
                pointer-events: none;
            }
            
            .sparkle {
                position: absolute;
                width: 4px;
                height: 4px;
                background: #2563EB;
                border-radius: 50%;
                animation: sparkleFloat 3s ease-in-out infinite;
                box-shadow: 0 0 10px #2563EB;
            }
            
            .sparkle:nth-child(1) { left: 20%; top: 20%; animation-delay: 0s; }
            .sparkle:nth-child(2) { left: 80%; top: 30%; animation-delay: 0.5s; }
            .sparkle:nth-child(3) { left: 40%; top: 60%; animation-delay: 1s; }
            .sparkle:nth-child(4) { left: 70%; top: 70%; animation-delay: 1.5s; }
            .sparkle:nth-child(5) { left: 30%; top: 80%; animation-delay: 2s; }
            .sparkle:nth-child(6) { left: 60%; top: 40%; animation-delay: 2.5s; }
            
            @keyframes sparkleFloat {
                0%, 100% {
                    transform: translateY(0) scale(0);
                    opacity: 0;
                }
                50% {
                    transform: translateY(-30px) scale(1);
                    opacity: 1;
                }
            }
            
            /* Progress Bar */
            .loading-progress {
                width: 100%;
                height: 4px;
                background: rgba(37, 99, 235, 0.2);
                border-radius: 2px;
                overflow: hidden;
                margin-top: 1.5rem;
            }
            
            .loading-progress-bar {
                height: 100%;
                background: linear-gradient(90deg, #2563EB, #00d9ff);
                animation: progress 3s ease-in-out infinite;
            }
            
            @keyframes progress {
                0% { width: 0%; }
                50% { width: 70%; }
                100% { width: 100%; }
            }
            
            /* ========================================
               INPUT FIELDS - WHITE BG, BLACK TEXT
               ======================================== */
            
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
            
            .stTextInput > div > div > input::placeholder,
            .stTextArea > div > div > textarea::placeholder {
                color: #9ca3af !important;
                font-weight: 500 !important;
                font-style: italic !important;
            }
            
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            .stTextArea > div > div > textarea:focus {
                border-color: #00d9ff !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.25) !important;
                outline: none !important;
            }
            
            /* SELECTBOX */
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
            
            div[data-baseweb="select"] span,
            div[data-baseweb="select"] div,
            div[data-baseweb="select"] > div > div {
                color: #000000 !important;
                font-weight: 600 !important;
            }
            
            div[data-baseweb="select"] svg,
            div[data-baseweb="select"] svg path {
                fill: #000000 !important;
                color: #000000 !important;
                stroke: #000000 !important;
            }
            
            div[data-baseweb="select"] [aria-selected="false"] {
                color: #6b7280 !important;
            }
            
            div[data-baseweb="select"]:focus-within > div {
                border-color: #00d9ff !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.25) !important;
            }
            
            div[data-baseweb="popover"] {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                border-radius: 12px !important;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
            }
            
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
            
            div[role="option"][aria-selected="true"] {
                background: rgba(0, 217, 255, 0.2) !important;
                color: #000000 !important;
            }
            
            /* CHECKBOX */
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
            
            .stCheckbox input:checked + div {
                background: linear-gradient(135deg, #00d9ff 0%, #a855f7 100%) !important;
                border-color: #00d9ff !important;
            }
            
            /* ========================================
               FOOTER
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
            
            /* ========================================
               MOBILE RESPONSIVE
               ======================================== */
            
            @media (max-width: 768px) {
                .top-nav {
                    padding: 0 1.5rem;
                    height: 70px;
                }
                
                .hero-container {
                    flex-direction: column;
                    padding: 2rem 1.5rem;
                    margin-top: 80px;
                }
                
                .hero-left {
                    max-width: 100%;
                    text-align: center;
                    margin-bottom: 2rem;
                }
                
                .hero-title {
                    font-size: 2.5rem;
                }
                
                .ai-avatar {
                    width: 280px;
                    height: 280px;
                }
                
                .features-section {
                    padding: 3rem 1.5rem;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                }
                
                .form-title {
                    font-size: 2rem;
                }
                
                .loading-title {
                    font-size: 1.3rem;
                }
                
                .loading-subtitle {
                    font-size: 0.9rem;
                }
                
                .loading-spinner {
                    width: 60px;
                    height: 60px;
                }
            }
            
            @media (max-width: 480px) {
                .hero-title {
                    font-size: 2rem;
                }
                
                .ai-avatar {
                    width: 220px;
                    height: 220px;
                }
                
                .form-title {
                    font-size: 1.75rem;
                }
            }
            
        </style>
        """,
        unsafe_allow_html=True
    )