import streamlit as st
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import generate_worksheet_content, parse_questions_and_answers
from services.pdf_service import create_worksheet_pdf

def render_worksheet_form():
    """Render worksheet generator form with proper spacing"""
    
    # Add top margin to avoid header overlap
    st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='form-title'>Create Your AI Worksheet</h2>", unsafe_allow_html=True)
    
    # Add spacing
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    with st.form("worksheet_form"):
        # Row 1: Grade, Subject, Chapter
        col1, col2, col3 = st.columns(3)
        
        with col1:
            grade = st.selectbox(
                "Grade/Class",
                [f"Grade {i}" for i in range(1, 13)],
                key="grade_select"
            )
        
        with col2:
            subject = st.selectbox(
                "Subject",
                SUBJECTS,
                key="subject_select"
            )
        
        with col3:
            chapter = st.selectbox(
                "Chapter",
                CHAPTERS.get(subject, ["General"]),
                key="chapter_select"
            )
        
        # Add spacing between rows
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        # Row 2: Difficulty, Number of Questions, Checkbox
        col4, col5, col6 = st.columns([1, 1, 1])
        
        with col4:
            difficulty = st.selectbox(
                "Worksheet Difficulty",
                ["Easy", "Medium", "Hard"],
                key="difficulty_select"
            )
        
        with col5:
            num_questions = st.number_input(
                "Number of Questions",
                min_value=1,
                max_value=100,
                value=10,
                key="num_questions_input"
            )
        
        with col6:
            # Add spacing to align checkbox properly
            st.markdown("<div style='margin-top: 1.8rem;'></div>", unsafe_allow_html=True)
            include_answers = st.checkbox("Include Answer Key", value=True)
        
        # Add spacing
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
        # Row 3: PDF Header/Title (full width)
        pdf_header = st.text_input(
            "Enter PDF Header/Title",
            value="Infinity Learn Sri Chaitanya",
            placeholder="Your institute name or worksheet title",
            key="pdf_header_input"
        )
        
        # Add spacing before button
        st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)
        
        # Submit button
        submitted = st.form_submit_button("Generate Worksheet", use_container_width=True)
    
    # Add bottom spacing
    st.markdown("<div style='margin-bottom: 5rem;'></div>", unsafe_allow_html=True)
    
    if submitted:
        with st.spinner("Generating your AI-powered worksheet..."):
            try:
                # Generate content using Gemini
                generated_text = generate_worksheet_content(
                    grade, subject, chapter, difficulty, num_questions
                )
                
                # Parse questions and answers
                questions_list, answers_list = parse_questions_and_answers(generated_text)
                
                # Create PDF
                pdf_output = create_worksheet_pdf(
                    pdf_header, subject, chapter, grade, difficulty,
                    questions_list, answers_list, include_answers
                )
                
                st.success(f"✅ Worksheet with {len(questions_list)} AI-generated questions created successfully!")
                
                # Preview section
                with st.expander("📖 Preview Questions"):
                    for idx, q in enumerate(questions_list, 1):
                        st.markdown(f"**Q{idx}.** {q}")
                        if include_answers and idx <= len(answers_list):
                            st.markdown(f"*💡 Answer:* {answers_list[idx-1]}")
                        st.markdown("---")
                
                # Clean filename for download
                clean_filename = f"{subject}_{chapter}_Worksheet_{grade}_{difficulty}"
                clean_filename = clean_filename.replace(' ', '_')
                
                # Download button
                st.download_button(
                    label="📥 Download Worksheet PDF",
                    data=pdf_output,
                    file_name=f"{clean_filename}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Please verify your Gemini API key and ensure you have access to the Gemini API.")