import streamlit as st

def render_features_section():
    """Render features section with cards"""
    st.markdown(
        """
        <div class='features-section'>
            <h2 class='section-title'>What Can Infinity Sheets Do?</h2>
            <p class='section-subtitle'>Powerful features designed for modern educators</p>
            <div class='features-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>🎯</div>
                    <div class='feature-title'>Know Your Curriculum Inside-Out</div>
                    <div class='feature-text'>Generate questions for any grade, subject, and chapter with perfect accuracy.</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>⚡</div>
                    <div class='feature-title'>Ask Anything, Get It Generated</div>
                    <div class='feature-text'>AI-powered question generation tailored to your exact difficulty and topic requirements.</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>📊</div>
                    <div class='feature-title'>Action Steps to Improve Performance</div>
                    <div class='feature-text'>Create targeted worksheets with answer keys to help students master difficult concepts.</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>📝</div>
                    <div class='feature-title'>Tough Topics Made Simple</div>
                    <div class='feature-text'>Break down complex chapters into digestible practice questions for better understanding.</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>🎓</div>
                    <div class='feature-title'>Discover Your Teaching Style</div>
                    <div class='feature-text'>Customize worksheets to match your teaching methodology and student needs.</div>
                </div>
                <div class='feature-card'>
                    <div class='feature-icon'>🚀</div>
                    <div class='feature-title'>Instant PDF Export</div>
                    <div class='feature-text'>Download professional, print-ready worksheets with your institute branding instantly.</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )