import streamlit as st
<<<<<<< HEAD
import time
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import generate_worksheet_content, parse_questions_and_answers
from services.pdf_service import create_worksheet_pdf
from services.analytics_service import track_event
from services.token_logger import log_token_usage, calculate_cost

def render_worksheet_form():
    """Render worksheet generator form - Clean UI without token display"""
=======
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import generate_worksheet_content, parse_questions_and_answers
from services.pdf_service import create_worksheet_pdf

def render_worksheet_form():
    """Render worksheet generator form with proper spacing"""
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    
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
<<<<<<< HEAD
            # Subject - Dropdown with search capability
            subject = st.selectbox(
                "Subject",
                [""] + SUBJECTS,
                format_func=lambda x: "Type or select: Math, Science, Physics..." if x == "" else x,
                key="subject_select_dropdown"
            )
            
            # If empty, allow custom input
            if subject == "":
                subject_custom = st.text_input(
                    "Or type custom subject",
                    placeholder="Type any subject name...",
                    key="subject_custom",
                    label_visibility="collapsed"
                )
                subject = subject_custom if subject_custom else "Mathematics"
        
        with col3:
            # Chapter - Dropdown with search capability based on subject
            chapter_list = CHAPTERS.get(subject, ["General Topics"])
            
            chapter = st.selectbox(
                "Chapter",
                [""] + chapter_list,
                format_func=lambda x: "Type any chapter name..." if x == "" else x,
                key="chapter_select_dropdown"
            )
            
            # If empty, allow custom input
            if chapter == "":
                chapter_custom = st.text_input(
                    "Or type custom chapter",
                    placeholder="Type any chapter name...",
                    key="chapter_custom",
                    label_visibility="collapsed"
                )
                chapter = chapter_custom if chapter_custom else chapter_list[0]
=======
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
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
        
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
<<<<<<< HEAD
            # Number of questions - Dropdown style
            num_questions = st.selectbox(
                "Number of Questions",
                list(range(5, 51, 5)),  # 5, 10, 15, ... 50
                index=1,  # Default to 10
                key="num_questions_select"
=======
            num_questions = st.number_input(
                "Number of Questions",
                min_value=1,
                max_value=100,
                value=10,
                key="num_questions_input"
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
            )
        
        with col6:
            # Add spacing to align checkbox properly
            st.markdown("<div style='margin-top: 1.8rem;'></div>", unsafe_allow_html=True)
            include_answers = st.checkbox("Include Answer Key", value=True)
        
        # Add spacing
        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
        
<<<<<<< HEAD
        # Row 3: PDF Name (full width with BLACK text)
        pdf_name = st.text_input(
            "Enter PDF Name",
            value="Infinity Learn by Sri Chaitanya",
            placeholder="Enter the name for your PDF file",
            key="pdf_name_input",
            help="This is the filename of your downloaded PDF"
=======
        # Row 3: PDF Header/Title (full width)
        pdf_header = st.text_input(
            "Enter PDF Header/Title",
            value="Infinity Learn Sri Chaitanya",
            placeholder="Your institute name or worksheet title",
            key="pdf_header_input"
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
        )
        
        # Add spacing before button
        st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)
        
<<<<<<< HEAD
        # Submit button with custom styling
        st.markdown("""
        <style>
            /* Generate Worksheet Button - Black with White Text */
            div[data-testid="stFormSubmitButton"] button {
                background: #000000 !important;
                color: #ffffff !important;
                border: 2px solid rgba(0, 217, 255, 0.3) !important;
                border-radius: 50px !important;
                font-weight: 800 !important;
                font-size: 1.2rem !important;
                padding: 1.2rem 3rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 10px 40px rgba(0, 217, 255, 0.4) !important;
                text-transform: uppercase !important;
                letter-spacing: 1px !important;
            }
            
            div[data-testid="stFormSubmitButton"] button:hover {
                background: #1a1a1a !important;
                border-color: rgba(0, 217, 255, 0.6) !important;
                transform: translateY(-3px) !important;
                box-shadow: 0 15px 50px rgba(0, 217, 255, 0.6) !important;
            }
            
            /* PDF Name input - BLACK TEXT */
            input[aria-label="Enter PDF Name"] {
                color: #000000 !important;
                font-weight: 700 !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🚀 Generate Worksheet", use_container_width=True)
=======
        # Submit button
        submitted = st.form_submit_button("Generate Worksheet", use_container_width=True)
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    
    # Add bottom spacing
    st.markdown("<div style='margin-bottom: 5rem;'></div>", unsafe_allow_html=True)
    
    if submitted:
<<<<<<< HEAD
        # ANALYTICS: Track form button click (Button 2)
        track_event("generate_form_submitted", {
            "grade": grade,
            "subject": subject,
            "chapter": chapter,
            "difficulty": difficulty,
            "num_questions": num_questions,
            "source": "worksheet_form"
        })
        
        # LOADING ANIMATION
        progress_container = st.empty()
        progress_container.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <div class='loader'></div>
            <p style='color: #00d9ff; font-size: 1.2rem; margin-top: 1rem;'>
                ✨ AI is crafting your perfect worksheet...
            </p>
        </div>
        <style>
            .loader {
                margin: 0 auto;
                border: 8px solid rgba(0, 217, 255, 0.1);
                border-radius: 50%;
                border-top: 8px solid #00d9ff;
                width: 60px;
                height: 60px;
                animation: spin 1s linear infinite;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
        """, unsafe_allow_html=True)
        
        time.sleep(0.5)  # Brief pause for UX
        
        try:
            # Generate content using Gemini
            generated_text, token_data = generate_worksheet_content(
                grade, subject, chapter, difficulty, num_questions
            )
            
            # Calculate cost (for backend logging only)
            total_cost = calculate_cost(
                token_data["input_tokens"],
                token_data["output_tokens"],
                token_data["model"]
            )
            
            # Log token usage (ADMIN ONLY - not shown to users)
            log_token_usage(
                input_tokens=token_data["input_tokens"],
                output_tokens=token_data["output_tokens"],
                model_name=token_data["model"],
                user_action="worksheet_generation"
            )
            
            # Clear loading animation
            progress_container.empty()
            
            # Parse questions and answers
            questions_list, answers_list = parse_questions_and_answers(generated_text)
            
            # Create PDF (using "Infinity Learn by Sri Chaitanya" as header)
            pdf_output = create_worksheet_pdf(
                "Infinity Learn by Sri Chaitanya",  # Fixed header
                subject, 
                chapter, 
                grade, 
                difficulty,
                questions_list, 
                answers_list, 
                include_answers
            )
            
            # SUCCESS MESSAGE (no token info shown)
            st.success(f"✅ Worksheet with {len(questions_list)} AI-generated questions created successfully!")
            
            # Preview section
            with st.expander("📖 Preview Questions"):
                for idx, q in enumerate(questions_list, 1):
                    st.markdown(f"**Q{idx}.** {q}")
                    if include_answers and idx <= len(answers_list):
                        st.markdown(f"*💡 Answer:* {answers_list[idx-1]}")
                    st.markdown("---")
            
            # Clean filename using pdf_name
            clean_filename = pdf_name.replace(' ', '_')
            
            # Download button
            st.download_button(
                label="📥 Download Worksheet PDF",
                data=pdf_output,
                file_name=f"{clean_filename}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            
        except Exception as e:
            progress_container.empty()
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Please verify your Gemini API key and ensure you have access to the Gemini API.")
=======
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
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
