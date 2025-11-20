import streamlit as st

def apply_custom_css():
<<<<<<< HEAD
    """Apply all custom CSS styling with glassmorphic bubble inputs"""
=======
    """Apply all custom CSS styling"""
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
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
            
            /* Buttons */
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
            }
            
            .stButton > button:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 40px rgba(0, 217, 255, 0.5) !important;
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
            
<<<<<<< HEAD
            /* ========================================
               GLASSMORPHIC BUBBLE INPUTS - iOS STYLE
               ======================================== */
            
            /* Form labels - White and visible */
=======
            /* CRITICAL FIX: Form labels - Make them VISIBLE */
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            .stTextInput label,
            .stNumberInput label,
            .stSelectbox label,
            .stCheckbox label {
                color: #ffffff !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                display: block !important;
                margin-bottom: 0.75rem !important;
            }
            
<<<<<<< HEAD
            /* GLASSMORPHIC TEXT & NUMBER INPUTS */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input {
                background: rgba(255, 255, 255, 0.95) !important;
                backdrop-filter: blur(20px) !important;
                -webkit-backdrop-filter: blur(20px) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
                border-radius: 25px !important;
                color: #000000 !important;
                font-size: 1.1rem !important;
                font-weight: 700 !important;
                padding: 1.2rem 1.8rem !important;
                min-height: 60px !important;
                line-height: 1.5 !important;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1),
                            inset 0 1px 2px rgba(255, 255, 255, 0.1) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            
            .stTextInput > div > div > input::placeholder {
                color: rgba(0, 0, 0, 0.4) !important;
                opacity: 1 !important;
            }
            
            /* Hover effect - Glow */
            .stTextInput > div > div > input:hover,
            .stNumberInput > div > div > input:hover {
                background: rgba(255, 255, 255, 1) !important;
                border-color: rgba(0, 217, 255, 0.4) !important;
                box-shadow: 0 8px 32px rgba(0, 217, 255, 0.2),
                            inset 0 1px 2px rgba(255, 255, 255, 0.15) !important;
            }
            
            /* Focus state - Bright glow */
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus {
                background: rgba(255, 255, 255, 1) !important;
                border-color: rgba(0, 217, 255, 0.7) !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.2),
                            0 8px 32px rgba(0, 217, 255, 0.3),
                            inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
                outline: none !important;
                transform: translateY(-2px) !important;
            }
            
            /* GLASSMORPHIC SELECTBOX */
            div[data-baseweb="select"] {
                background: transparent !important;
            }
            
            div[data-baseweb="select"] > div {
                background: rgba(255, 255, 255, 0.08) !important;
                backdrop-filter: blur(20px) !important;
                -webkit-backdrop-filter: blur(20px) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
                border-radius: 25px !important;
                color: #ffffff !important;
                padding: 1.2rem 1.8rem !important;
                min-height: 60px !important;
                display: flex !important;
                align-items: center !important;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1),
                            inset 0 1px 2px rgba(255, 255, 255, 0.1) !important;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            
            div[data-baseweb="select"] span {
                color: #ffffff !important;
                font-weight: 600 !important;
                font-size: 1.1rem !important;
            }
            
            div[data-baseweb="select"] svg {
                color: rgba(255, 255, 255, 0.7) !important;
            }
            
            /* Selectbox hover */
            div[data-baseweb="select"] > div:hover {
                background: rgba(255, 255, 255, 0.12) !important;
                border-color: rgba(0, 217, 255, 0.4) !important;
                box-shadow: 0 8px 32px rgba(0, 217, 255, 0.2),
                            inset 0 1px 2px rgba(255, 255, 255, 0.15) !important;
            }
            
            /* Selectbox focus */
            div[data-baseweb="select"]:focus-within > div {
                background: rgba(255, 255, 255, 0.15) !important;
                border-color: rgba(0, 217, 255, 0.7) !important;
                box-shadow: 0 0 0 4px rgba(0, 217, 255, 0.2),
                            0 8px 32px rgba(0, 217, 255, 0.3),
                            inset 0 1px 2px rgba(255, 255, 255, 0.2) !important;
                transform: translateY(-2px) !important;
            }
            
            /* Dropdown menu - Dark glassmorphic */
            div[data-baseweb="popover"] {
                background: rgba(26, 31, 58, 0.95) !important;
                backdrop-filter: blur(20px) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 20px !important;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5) !important;
            }
            
            div[role="option"] {
                color: #ffffff !important;
                background: transparent !important;
                font-weight: 500 !important;
                padding: 0.9rem 1.2rem !important;
                border-radius: 12px !important;
                margin: 0.25rem 0.5rem !important;
                transition: all 0.2s ease !important;
            }
            
            div[role="option"]:hover {
                background: rgba(0, 217, 255, 0.15) !important;
                color: #00d9ff !important;
=======
            /* CRITICAL FIX: Text inputs - Full visibility */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.5) !important;
                border-radius: 12px !important;
                color: #000000 !important;
                font-size: 1.2rem !important;
                font-weight: 700 !important;
                padding: 1.2rem 1.5rem !important;
                min-height: 65px !important;
                line-height: 1.5 !important;
            }
            
            .stTextInput > div > div > input::placeholder {
                color: #6b7280 !important;
                opacity: 0.7 !important;
            }
            
            /* CRITICAL FIX: Selectbox - Full visibility */
            div[data-baseweb="select"] {
                background: #ffffff !important;
            }
            
            div[data-baseweb="select"] > div {
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.5) !important;
                border-radius: 12px !important;
                color: #000000 !important;
                padding: 1.2rem 1.5rem !important;
                min-height: 65px !important;
                display: flex !important;
                align-items: center !important;
            }
            
            div[data-baseweb="select"] span {
                color: #000000 !important;
                font-weight: 700 !important;
                font-size: 1.2rem !important;
            }
            
            div[data-baseweb="select"] svg {
                color: #000000 !important;
            }
            
            /* Dropdown menu */
            div[data-baseweb="popover"] {
                background: #ffffff !important;
            }
            
            div[role="option"] {
                color: #000000 !important;
                background: #ffffff !important;
                font-weight: 600 !important;
                padding: 0.75rem 1rem !important;
            }
            
            div[role="option"]:hover {
                background: rgba(0, 217, 255, 0.2) !important;
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            }
            
            div[aria-selected="true"] {
                background: rgba(0, 217, 255, 0.25) !important;
<<<<<<< HEAD
                color: #00d9ff !important;
                font-weight: 700 !important;
            }
            
            /* Checkbox - Glassmorphic */
=======
                font-weight: 800 !important;
            }
            
            /* Checkbox */
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            .stCheckbox > label {
                display: flex !important;
                align-items: center !important;
                gap: 0.75rem !important;
            }
            
            .stCheckbox > label > div:first-child {
<<<<<<< HEAD
                background: rgba(255, 255, 255, 0.08) !important;
                backdrop-filter: blur(10px) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
                border-radius: 8px !important;
                width: 26px !important;
                height: 26px !important;
                transition: all 0.3s ease !important;
            }
            
            .stCheckbox > label > div:first-child:hover {
                background: rgba(255, 255, 255, 0.12) !important;
                border-color: rgba(0, 217, 255, 0.4) !important;
=======
                background: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.4) !important;
                border-radius: 6px !important;
                width: 24px !important;
                height: 24px !important;
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            }
            
            .stCheckbox > label > div:last-child {
                color: #ffffff !important;
                font-weight: 600 !important;
                font-size: 1.1rem !important;
            }
            
<<<<<<< HEAD
=======
            /* Focus states */
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            div[data-baseweb="select"]:focus-within {
                border-color: #00d9ff !important;
                box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.3) !important;
                outline: none !important;
            }
            
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            /* Messages */
            .stSuccess {
                background: rgba(16, 185, 129, 0.1) !important;
                border-left: 4px solid #10b981 !important;
                color: #10b981 !important;
                padding: 1rem !important;
                border-radius: 8px !important;
            }
            
            .stError {
                background: rgba(239, 68, 68, 0.1) !important;
                border-left: 4px solid #ef4444 !important;
                color: #ef4444 !important;
                padding: 1rem !important;
                border-radius: 8px !important;
            }
            
            /* Footer */
            .footer {
                text-align: center;
                padding: 3rem;
                margin-top: 5rem;
                border-top: 1px solid rgba(255, 255, 255, 0.08);
                color: #6b7280;
            }
            
            /* Download button */
            .stDownloadButton > button {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
                color: #ffffff !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                padding: 1rem 2rem !important;
            }
<<<<<<< HEAD
            
            /* Mobile Responsive - Complete */
            @media (max-width: 768px) {
                /* Navigation */
                .top-nav {
                    padding: 0 1rem;
                    height: 70px;
                    flex-wrap: wrap;
                }
                
                .nav-logo-img {
                    height: 35px;
                }
                
                .nav-tagline {
                    font-size: 0.7rem;
                }
                
                .contact-info {
                    font-size: 0.75rem;
                    margin-top: 0.5rem;
                }
                
                /* Hero Section - Mobile Optimized */
                .hero-container {
                    flex-direction: column;
                    padding: 1.5rem 1rem;
                    margin-top: 70px;
                    min-height: auto;
                }
                
                .hero-left {
                    max-width: 100%;
                    text-align: center;
                }
                
                .hero-title {
                    font-size: 2rem;
                    line-height: 1.2;
                    margin-bottom: 1rem;
                }
                
                .hero-subtitle {
                    font-size: 1rem;
                    margin-bottom: 1rem;
                    line-height: 1.4;
                }
                
                .hero-description {
                    font-size: 0.9rem;
                    margin-bottom: 1.5rem;
                    line-height: 1.5;
                }
                
                .hero-right {
                    width: 100%;
                    margin-top: 1.5rem;
                }
                
                .ai-avatar {
                    width: 220px;
                    height: 220px;
                    margin: 0 auto;
                }
                
                /* Button Center - Mobile */
                .button-center {
                    margin: 1.5rem 0;
                    padding: 0 1rem;
                }
                
                /* Features Section - Mobile */
                .features-section {
                    padding: 2rem 1rem;
                }
                
                .section-title {
                    font-size: 1.6rem;
                    line-height: 1.3;
                }
                
                .section-subtitle {
                    font-size: 0.95rem;
                    margin-bottom: 2rem;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                    gap: 1.2rem;
                }
                
                .feature-card {
                    padding: 1.8rem;
                }
                
                .feature-icon {
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }
                
                .feature-title {
                    font-size: 1.1rem;
                    margin-bottom: 0.8rem;
                }
                
                .feature-text {
                    font-size: 0.9rem;
                    line-height: 1.5;
                }
                
                /* Form Title */
                .form-title {
                    font-size: 1.8rem;
                    padding: 0 1rem;
                }
                
                /* Form Inputs - Mobile Optimized */
                .main .block-container {
                    padding-top: 5rem !important;
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }
                
                /* Stacked columns on mobile */
                .row-widget.stHorizontal {
                    flex-direction: column !important;
                }
                
                .stTextInput > div > div > input,
                .stNumberInput > div > div > input {
                    font-size: 1rem !important;
                    padding: 1rem 1.2rem !important;
                    min-height: 50px !important;
                }
                
                div[data-baseweb="select"] > div {
                    font-size: 1rem !important;
                    padding: 1rem 1.2rem !important;
                    min-height: 50px !important;
                }
                
                div[data-baseweb="select"] span {
                    font-size: 1rem !important;
                }
                
                /* Labels on mobile */
                .stTextInput label,
                .stNumberInput label,
                .stSelectbox label,
                .stCheckbox label {
                    font-size: 1rem !important;
                }
                
                /* Button on mobile */
                .stButton > button {
                    font-size: 1rem !important;
                    padding: 0.9rem 2rem !important;
                    width: 100% !important;
                }
                
                div[data-testid="stFormSubmitButton"] button {
                    font-size: 1rem !important;
                    padding: 1rem 2rem !important;
                    width: 100% !important;
                }
                
                /* Footer mobile */
                .footer {
                    padding: 2rem 1rem;
                    font-size: 0.85rem;
                }
            }
            
            /* Extra small devices - Phones */
            @media (max-width: 480px) {
                .top-nav {
                    height: auto;
                    padding: 0.8rem;
                }
                
                .nav-tagline {
                    display: none;
                }
                
                .contact-info {
                    width: 100%;
                    justify-content: center;
                    font-size: 0.7rem;
                }
                
                .hero-title {
                    font-size: 1.6rem;
                }
                
                .hero-subtitle {
                    font-size: 0.9rem;
                }
                
                .hero-description {
                    font-size: 0.85rem;
                }
                
                .ai-avatar {
                    width: 180px;
                    height: 180px;
                }
                
                .section-title {
                    font-size: 1.4rem;
                }
                
                .form-title {
                    font-size: 1.5rem;
                }
                
                .feature-card {
                    padding: 1.5rem;
                }
            }
            
            /* Landscape phones */
            @media (max-width: 896px) and (orientation: landscape) {
                .hero-container {
                    margin-top: 60px;
                    padding: 1rem;
                }
                
                .ai-avatar {
                    width: 150px;
                    height: 150px;
                }
                
                .hero-title {
                    font-size: 1.5rem;
                }
            }
=======
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
        </style>
        """,
        unsafe_allow_html=True
    )