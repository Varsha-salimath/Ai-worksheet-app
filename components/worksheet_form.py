import streamlit as st
import time
from datetime import datetime
from utils.data import SUBJECTS, CHAPTERS
from services.gemini_service import (
    generate_worksheet_content,
    parse_questions_and_answers,
    get_session_id,
    fuzzy_correct_chapter,
    langfuse,
    langfuse_enabled
)
from services.pdf_service import create_worksheet_pdf
from services.analytics_service import track_event
from services.token_logger import log_token_usage, calculate_cost


def log_langfuse_event(event_name, metadata):
    """Log event to Langfuse with version compatibility"""
    if not langfuse_enabled or not langfuse:
        return

    try:
        trace = langfuse.trace(
            name=event_name,
            user_id=get_session_id(),
            metadata=metadata
        )
        print(f"✅ Langfuse v3: {event_name} tracked")
    except Exception:
        try:
            langfuse.log(
                name=event_name,
                user_id=get_session_id(),
                properties=metadata
            )
            print(f"✅ Langfuse v2: {event_name} tracked")
        except Exception as e:
            print(f"⚠️ Langfuse logging failed: {e}")


def render_worksheet_form():
    """Render worksheet generator form with animations and improved UI"""

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

        # ------------------ SUBJECT (TEXT INPUT) - FIXED PLACEHOLDER ------------------
        with col2:
            subject = st.text_input(
                "Subject (Type any subject)",
                placeholder="e.g., Physics, Mathematics",
                key="subject_input"
            )

            st.caption("Suggestions: " + ", ".join(SUBJECTS[:5]) + "...")

        # ------------------ CHAPTER (TEXT INPUT + FUZZY MATCH) - FIXED PLACEHOLDER ------------------
        with col3:
            typed_chapter = st.text_input(
                "Chapter (Type any chapter name)",
                placeholder="e.g., Motion, Fractions",
                key="chapter_input"
            )

            if subject in CHAPTERS and CHAPTERS[subject]:
                st.caption("Suggestions: " + ", ".join(CHAPTERS[subject][:3]) + "...")

        st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

        # ------------------ OTHER OPTIONS ------------------
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

        # PDF NAME
        pdf_name = st.text_input(
            "Enter PDF Name",
            value="Infinity_Learn_Worksheet",
            placeholder="Enter filename",
            key="pdf_name_input"
        )

        st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)

        # ------------------ GENERATE BUTTON (VISIBLE BLUE) ------------------
        submitted = st.form_submit_button(
            "🚀 Generate Worksheet",
            use_container_width=True
        )

    st.markdown("<div style='margin-bottom: 3rem;'></div>", unsafe_allow_html=True)

    # ------------------ SUBMIT HANDLER WITH ANIMATION ------------------
    if submitted:

        # Fix subject/chapter formatting
        subject_clean = subject.strip().title()
        chapter_clean = typed_chapter.strip().title()

        # Fuzzy correct chapter
        corrected_chapter = fuzzy_correct_chapter(subject_clean, chapter_clean)

        # LANGFUSE EVENT
        log_langfuse_event("click_generate_worksheet_final", {
            "button": "form_submit",
            "timestamp": datetime.now().isoformat(),
            "grade": grade,
            "subject_original": subject_clean,
            "chapter_original": chapter_clean,
            "chapter_corrected": corrected_chapter,
            "difficulty": difficulty,
            "num_questions": num_questions
        })

        # Analytics
        track_event("generate_form_submitted", {
            "grade": grade,
            "subject": subject_clean,
            "chapter_corrected": corrected_chapter
        })

        # LOADING ANIMATION - SPARKLE EFFECT
        progress_container = st.empty()
        progress_container.markdown("""
        <div class='loading-animation'>
            <div class='falling-stars'>
                <div class='star'>⭐</div>
                <div class='star'>✨</div>
                <div class='star'>🌟</div>
                <div class='star'>💫</div>
                <div class='star'>⭐</div>
            </div>
            <div class='sparkle-container'>
                <span class='sparkle'>✨</span>
                <p class='sparkle-text'>Generating your worksheet...</p>
                <span class='sparkle'>✨</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        try:
            # Generate using Gemini
            generated_text, token_data = generate_worksheet_content(
                grade, subject_clean, corrected_chapter, difficulty, num_questions
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

            # Parse
            questions, answers = parse_questions_and_answers(generated_text)

            # Validation
            if len(questions) < num_questions:
                st.warning(f"⚠️ Only {len(questions)} questions generated.")

            questions = questions[:num_questions]
            answers = answers[:num_questions]

            # PDF generation
            pdf_header = "Infinity Learn by Sri Chaitanya"
            pdf_output = create_worksheet_pdf(
                pdf_header,
                subject_clean,
                corrected_chapter,
                grade,
                difficulty,
                questions,
                answers,
                include_answers
            )

            st.success("🎉 Worksheet generated successfully!")

            # Preview
            with st.expander("📖 Preview Questions"):
                for i, q in enumerate(questions, 1):
                    st.markdown(f"**Q{i}.** {q}")
                    if include_answers:
                        st.markdown(f"💡 *Answer:* {answers[i-1]}")
                    st.divider()

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
            st.info("💡 Check your Gemini API key and internet connection.")