import streamlit as st
from services.analytics_service import track_event

def render_landing_page():
    """Render landing page with hero section and features - Mobile Optimized"""
    
    # Hero Section
    st.markdown(
        """
        <div class='hero-container'>
            <div class='hero-left'>
                <h1 class='hero-title'>
                    Generate Perfect <span class='gradient-text'>AI Worksheets</span>
                </h1>
                <p class='hero-subtitle'>
                    Create custom educational worksheets in seconds using advanced AI technology
                </p>
                <p class='hero-description'>
                    Choose your grade, subject, and difficulty level. Our AI generates 
                    comprehensive worksheets with answer keys instantly. Perfect for teachers, 
                    students, and homeschooling parents.
                </p>
            </div>
            <div class='hero-right'>
                <div class='ai-avatar'>
                    <img src='https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png' alt='AI Robot' />
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CTA Button
    st.markdown("<div class='button-center'>", unsafe_allow_html=True)
    if st.button("🚀 Generate Worksheets Now", key="hero_cta", use_container_width=False):
        track_event("cta_clicked", {"location": "hero_section"})
        st.session_state.page = "form"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Features Section
    st.markdown(
        """
        <div class='features-section'>
            <h2 class='section-title'>Why Choose Infinity Sheets?</h2>
            <p class='section-subtitle'>
                Powerful features designed for modern education
            </p>
            
            <div class='features-grid'>
                <div class='feature-card'>
                    <div class='feature-icon'>⚡</div>
                    <h3 class='feature-title'>Lightning Fast</h3>
                    <p class='feature-text'>
                        Generate comprehensive worksheets in under 30 seconds with our 
                        advanced AI technology powered by Google Gemini.
                    </p>
                </div>
                
                <div class='feature-card'>
                    <div class='feature-icon'>🎯</div>
                    <h3 class='feature-title'>Fully Customizable</h3>
                    <p class='feature-text'>
                        Choose grade level, subject, chapter, difficulty, and number of 
                        questions. Perfect for any learning objective.
                    </p>
                </div>
                
                <div class='feature-card'>
                    <div class='feature-icon'>📚</div>
                    <h3 class='feature-title'>All Subjects Covered</h3>
                    <p class='feature-text'>
                        Mathematics, Science, Social Studies, Languages, and more. 
                        Supports Grades 1-12 with curriculum-aligned content.
                    </p>
                </div>
                
                <div class='feature-card'>
                    <div class='feature-icon'>✅</div>
                    <h3 class='feature-title'>Answer Keys Included</h3>
                    <p class='feature-text'>
                        Every worksheet comes with detailed answer keys. Save time on 
                        grading and provide instant feedback.
                    </p>
                </div>
                
                <div class='feature-card'>
                    <div class='feature-icon'>📄</div>
                    <h3 class='feature-title'>Professional PDFs</h3>
                    <p class='feature-text'>
                        Download print-ready PDF worksheets with clean formatting. 
                        Perfect for classroom distribution or homework.
                    </p>
                </div>
                
                <div class='feature-card'>
                    <div class='feature-icon'>🔒</div>
                    <h3 class='feature-title'>Quality Assured</h3>
                    <p class='feature-text'>
                        AI-powered content generation with educational best practices. 
                        Verified by Sri Chaitanya Educational Institutions.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Bottom CTA
    st.markdown("<div class='button-center'>", unsafe_allow_html=True)
    if st.button("🚀 Start Creating Worksheets", key="bottom_cta", use_container_width=False):
        track_event("cta_clicked", {"location": "features_section"})
        st.session_state.page = "form"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)