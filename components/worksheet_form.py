import streamlit as st
import time
from datetime import datetime
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import generate_worksheet_content, parse_questions_and_answers, get_session_id, langfuse, langfuse_enabled
from services.pdf_service import create_worksheet_pdf
from services.analytics_service import track_event
from services.token_logger import log_token_usage, calculate_cost


def log_langfuse_event(event_name, metadata):
    """Log event to Langfuse with version compatibility"""
    if not langfuse_enabled or not langfuse:
        return
    
    try:
        # Try Langfuse v3 API
        trace = langfuse.trace(
            name=event_name,
            user_id=get_session_id(),
            metadata=metadata
        )
        print(f"✅ Langfuse: {event_name} tracked")
    except (AttributeError, TypeError):
        # Fallback to Langfuse v2 API
        try:
            langfuse.log(
                name=event_name,
                user_id=get_session_id(),
                properties=metadata
            )
            print(f"✅ Langfuse v2: {event_name} tracked")
        except Exception as e:
            print(f"⚠️ Langfuse event logging failed: {e}")


def render_worksheet_form():
    """Render worksheet generator form - All issues fixed"""

    st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='form-title'>Create Your AI Worksheet</h2>", unsafe_allow_html=True)
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

    # ------------------ FORM START ------------------
    with st.form("worksheet_form"):

        # Row 1: Grade, Subject, Chapter (FIXED: No duplicates)
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
                key="subject_select",
                help="Type to search subjects"
            )

        with col3:
            chapter_list = CHAPTERS.get(subject, ["General Topics"])
            chapter = st.selectbox(
                "Chapter",
                chapter_list,
                key="chapter_select",
                help="Chapters based on selected subject"
            )

        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

        # Row 2: Difficulty, Questions, Checkbox
        col4, col5, col6 = st.columns(3)

        with col4:
            difficulty = st.selectbox(
                "Worksheet Difficulty",
                ["Easy", "Medium", "Hard"],
                key="difficulty_select"
            )

        with col5:
            num_questions = st.selectbox(
                "Number of Questions",
                [5, 10, 15, 20, 25, 30],
                index=1,
                key="num_questions_select"
            )

        with col6:
            st.markdown("<div style='margin-top: 1.8rem;'></div>", unsafe_allow_html=True)
            include_answers = st.checkbox("Include Answer Key", value=True)

        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

        # Row 3: PDF Name
        pdf_name = st.text_input(
            "Enter PDF Name",
            value="Infinity_Learn_Worksheet",
            placeholder="Enter filename for download",
            key="pdf_name_input",
            help="Name of the downloaded PDF file"
        )

        st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)

        # Custom button styling
        st.markdown("""
        <style>
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
        </style>
        """, unsafe_allow_html=True)

        submitted = st.form_submit_button("🚀 Generate Worksheet", use_container_width=True)

    st.markdown("<div style='margin-bottom: 5rem;'></div>", unsafe_allow_html=True)

    if submitted:
        
        # LANGFUSE EVENT: Form button clicked
        log_langfuse_event("click_generate_worksheet_final", {
            "button": "form_submit",
            "timestamp": datetime.now().isoformat(),
            "grade": grade,
            "subject": subject,
            "chapter": chapter,
            "difficulty": difficulty,
            "num_questions": num_questions
        })

        # Analytics tracking
        track_event("generate_form_submitted", {
            "grade": grade,
            "subject": subject,
            "chapter": chapter,
            "difficulty": difficulty,
            "num_questions": num_questions
        })

        # LOADING ANIMATION
        progress_container = st.empty()
        progress_container.markdown("""
        <div style='text-align:center; padding: 3rem;'>
            <div class='loader'></div>
            <p style='color:#00d9ff; font-size:1.3rem; margin-top:1.5rem; font-weight:700;'>
                ✨ AI is generating your worksheet...
            </p>
            <p style='color:#8b92b0; font-size:0.9rem; margin-top:0.5rem;'>
                Please wait, this may take 10-30 seconds
            </p>
        </div>
        <style>
            .loader {
                margin: auto;
                border: 10px solid rgba(0,217,255,0.1);
                border-top: 10px solid #00d9ff;
                border-radius: 50%;
                width: 80px;
                height: 80px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin { 
                0% {transform: rotate(0deg);} 
                100% {transform: rotate(360deg);} 
            }
        </style>
        """, unsafe_allow_html=True)

        try:
            # Generate using Gemini
            generated_text, token_data = generate_worksheet_content(
                grade, subject, chapter, difficulty, num_questions
            )

            total_cost = calculate_cost(
                token_data["input_tokens"],
                token_data["output_tokens"],
                token_data["model"]
            )

            log_token_usage(
                input_tokens=token_data["input_tokens"],
                output_tokens=token_data["output_tokens"],
                model_name=token_data["model"],
                user_action="worksheet_generation"
            )

            progress_container.empty()

            # Parse questions
            questions, answers = parse_questions_and_answers(generated_text)

            # Validation: Ensure correct count
            if len(questions) < num_questions:
                st.warning(f"⚠️ Generated {len(questions)} questions instead of {num_questions}")
            
            # Trim if too many
            questions = questions[:num_questions]
            answers = answers[:num_questions]

            # Generate PDF
            pdf_header = "Infinity Learn by Sri Chaitanya"
            pdf_output = create_worksheet_pdf(
                pdf_header,
                subject,
                chapter,
                grade,
                difficulty,
                questions,
                answers,
                include_answers
            )

            st.success(f"✅ Worksheet with {len(questions)} questions created successfully!")

            # Preview
            with st.expander("📖 Preview Questions"):
                for idx, q in enumerate(questions, 1):
                    st.markdown(f"**Q{idx}.** {q}")
                    if include_answers and idx <= len(answers):
                        st.markdown(f"💡 *Answer:* {answers[idx-1]}")
                    st.markdown("---")

            clean_filename = pdf_name.replace(" ", "_")

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
            st.info("💡 Check your Gemini API key and internet connectivity.")