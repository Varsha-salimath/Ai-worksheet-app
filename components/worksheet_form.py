import streamlit as st
import time
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import generate_worksheet_content, parse_questions_and_answers
from services.pdf_service import create_worksheet_pdf
from services.analytics_service import track_event
from services.token_logger import log_token_usage, calculate_cost


def render_worksheet_form():
    """Render worksheet generator form with clean UI"""

    st.markdown("<div style='margin-top: 120px;'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='form-title'>Create Your AI Worksheet</h2>", unsafe_allow_html=True)
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

    # ------------------ FORM START ------------------
    with st.form("worksheet_form"):

        col1, col2, col3 = st.columns(3)

        # ------------------ GRADE ------------------
        with col1:
            grade = st.selectbox(
                "Grade/Class",
                [f"Grade {i}" for i in range(1, 13)],
                key="grade_select"
            )

        # ------------------ SUBJECT ------------------
        with col2:
            subject = st.selectbox(
                "Subject",
                SUBJECTS,
                key="subject_select"
            )

        # ------------------ CHAPTER ------------------
        with col3:
            chapter = st.selectbox(
                "Chapter",
                CHAPTERS.get(subject, ["General"]),
                key="chapter_select"
            )

        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

        # ------------------ DIFFICULTY / QUESTIONS ------------------
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
                [5, 10, 15, 20, 25],
                key="num_questions_select"
            )

        with col6:
            st.markdown("<div style='margin-top: 1.8rem;'></div>", unsafe_allow_html=True)
            include_answers = st.checkbox("Include Answer Key", value=True)

        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

        # ------------------ PDF NAME ------------------
        pdf_name = st.text_input(
            "Enter PDF Name",
            value="Infinity Learn Worksheet",
            placeholder="Enter file name",
            key="pdf_name_input"
        )

        # ------------------ PDF HEADER ------------------
        pdf_header = st.text_input(
            "Enter PDF Header/Title",
            value="Infinity Learn by Sri Chaitanya",
            placeholder="Worksheet Header",
            key="pdf_header_input"
        )

        st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)

        submitted = st.form_submit_button("🚀 Generate Worksheet", use_container_width=True)

    # ------------------ FORM END ------------------

    # Bottom spacing
    st.markdown("<div style='margin-bottom: 5rem;'></div>", unsafe_allow_html=True)

    if submitted:

        track_event("generate_form_submitted", {
            "grade": grade,
            "subject": subject,
            "chapter": chapter,
            "difficulty": difficulty,
            "num_questions": num_questions
        })

        # LOADING ICON
        progress_container = st.empty()
        progress_container.markdown("""
        <div style='text-align:center; padding: 2rem;'>
            <div class='loader'></div>
            <p style='color:#00d9ff; font-size:1.2rem;'>✨ AI is generating your worksheet...</p>
        </div>
        <style>
            .loader {
                margin: auto;
                border: 8px solid rgba(0,217,255,0.1);
                border-top: 8px solid #00d9ff;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin { 0% {transform: rotate(0);} 100% {transform: rotate(360);} }
        </style>
        """, unsafe_allow_html=True)

        try:
            # ------------------ GENERATE USING GEMINI ------------------
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

            # ------------------ PARSE QUESTIONS ------------------
            questions, answers = parse_questions_and_answers(generated_text)

            # ------------------ GENERATE PDF ------------------
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

            st.success(f"✅ Worksheet with {len(questions)} questions created!")

            # ------------------ PREVIEW ------------------
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
