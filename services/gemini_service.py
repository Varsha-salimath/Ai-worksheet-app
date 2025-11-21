import streamlit as st
import google.generativeai as genai
import os
from rapidfuzz import process, fuzz
from utils.data import CHAPTERS
from config.settings import load_api_key, GEMINI_MODEL, get_model_pricing

# Langfuse Setup
try:
    from langfuse import Langfuse
    LANGFUSE_AVAILABLE = True
except:
    LANGFUSE_AVAILABLE = False

langfuse = None
langfuse_enabled = False

if LANGFUSE_AVAILABLE:
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST")

    if public_key and secret_key:
        try:
            langfuse = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=host
            )
            langfuse_enabled = True
        except:
            langfuse_enabled = False


def fuzzy_correct_chapter(subject, chapter_user_input):
    """Correct chapter name using fuzzy matching"""
    if subject in CHAPTERS:
        possible_chapters = CHAPTERS[subject]

        best_match, score, _ = process.extractOne(
            chapter_user_input,
            possible_chapters,
            scorer=fuzz.WRatio
        )

        if score > 70:  # threshold for correction
            return best_match

    return chapter_user_input  # accept user input as-is


def initialize_gemini():
    genai.configure(api_key=load_api_key())


def get_session_id():
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id


def generate_worksheet_content(grade, subject, chapter, difficulty, num_questions):

    diff_map = {
        "Easy": "Suitable for beginners.",
        "Medium": "Intermediate difficulty level.",
        "Hard": "Advanced analytical questions."
    }

    prompt = f"""
Generate EXACTLY {num_questions} questions.
Subject: {subject}
Chapter: {chapter}
Difficulty: {difficulty} — {diff_map[difficulty]}
Format:
Q1. question
A1. answer
...
"""

    # ONLY REMOVE worksheet_generation trace (as requested)
    trace_id = None

    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.7,
                max_output_tokens=8192
            )
        )
    except Exception as e:
        raise Exception(f"Gemini API Error: {str(e)}")

    try:
        usage = response.usage_metadata
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count
    except:
        input_tokens = output_tokens = 0

    return response.text, {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "model": GEMINI_MODEL
    }


def parse_questions_and_answers(text):
    questions, answers = [], []
    q, a = "", ""
    lines = text.split("\n")
    mode = None

    for line in lines:
        line = line.strip()

        if line.startswith("Q") and "." in line:
            if q:
                questions.append(q.strip())
            q = line.split(".", 1)[1].strip()
            mode = "Q"

        elif line.startswith("A") and "." in line:
            if a:
                answers.append(a.strip())
            a = line.split(".", 1)[1].strip()
            mode = "A"

        else:
            if mode == "Q":
                q += " " + line
            elif mode == "A":
                a += " " + line

    if q:
        questions.append(q.strip())
    if a:
        answers.append(a.strip())

    return questions, answers