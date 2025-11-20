import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Infinity Sheets",
        page_icon="🪐",
        layout="wide"
    )

def load_api_key():
    """Load and return Google API key"""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("❌ Gemini API key not found. Please add it to your .env file as GOOGLE_API_KEY.")
        st.stop()
    
    return api_key.strip()

# ===========================
# GEMINI MODEL CONFIGURATION
# ===========================
GEMINI_MODEL = "gemini-2.0-flash-exp"  # Change to your preferred model

# ===========================
# GEMINI PRICING (USD)
# Updated as of Nov 2024
# ===========================
# Source: https://ai.google.dev/pricing

GEMINI_PRICING = {
    "gemini-2.0-flash-exp": {
        "input_per_1k": 0.0,      # Free during preview
        "output_per_1k": 0.0      # Free during preview
    },
    "gemini-1.5-flash": {
        "input_per_1k": 0.00015,   # $0.15 per 1M tokens
        "output_per_1k": 0.0006    # $0.60 per 1M tokens
    },
    "gemini-1.5-pro": {
        "input_per_1k": 0.00125,   # $1.25 per 1M tokens
        "output_per_1k": 0.005     # $5.00 per 1M tokens
    }
}

def get_model_pricing(model_name):
    """Get pricing for specific model"""
    return GEMINI_PRICING.get(model_name, {
        "input_per_1k": 0.0,
        "output_per_1k": 0.0
    })

# ===========================
# ANALYTICS CONFIGURATION
# ===========================

# OPTION 1: UMAMI ANALYTICS (Recommended)
ANALYTICS_ENABLED = True
ANALYTICS_PROVIDER = "umami"  # Options: "umami", "plausible", "posthog"

UMAMI_CONFIG = {
    "website_id": "213f72b7-20d7-4594-ac4e-914a3695ab15",  # Your actual Umami website ID
    "script_url": "https://cloud.umami.is/script.js",
    "domain": "localhost"  # Change to your actual domain when deployed
}

# OPTION 2: PLAUSIBLE ANALYTICS
PLAUSIBLE_CONFIG = {
    "domain": "yourwebsite.com",  # Your domain
    "script_url": "https://plausible.io/js/script.js"
}

# OPTION 3: POSTHOG
POSTHOG_CONFIG = {
    "api_key": "YOUR_POSTHOG_PROJECT_KEY",
    "host": "https://app.posthog.com"  # Or your self-hosted instance
}

# ===========================
# ADMIN DASHBOARD
# ===========================
ADMIN_PASSWORD = "admin123"  # CHANGE THIS IN PRODUCTION!

# Database path for token logs
TOKEN_LOG_DB = "token_logs.db"
TOKEN_LOG_CSV = "logs/token_logs.csv"

# User location
USER_LOCATION = "Bengaluru, Karnataka, IN"
