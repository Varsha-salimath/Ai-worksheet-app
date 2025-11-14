import streamlit as st
import google.generativeai as genai
from config.settings import load_api_key

def initialize_gemini():
    """Initialize Google Gemini API"""
    api_key = load_api_key()
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"❌ Error configuring Gemini API: {str(e)}")
        st.stop()

def generate_worksheet_content(grade, subject, chapter, difficulty, num_questions):
    """Generate worksheet questions using Gemini API"""
    
    difficulty_instructions = {
        "Easy": f"suitable for {grade} students who are just beginning to learn {chapter}. Questions should test basic understanding and fundamental concepts.",
        "Medium": f"suitable for {grade} students with intermediate knowledge of {chapter}. Questions should require application of concepts and some problem-solving.",
        "Hard": f"suitable for {grade} students who have mastered {chapter}. Questions should be challenging, requiring deep understanding, critical thinking, and advanced problem-solving skills."
    }
    
    prompt = f"""Generate exactly {num_questions} {difficulty} difficulty questions for {grade} students on the topic: {chapter} ({subject}).

Context:
- Grade Level: {grade}
- Subject: {subject}
- Chapter: {chapter}
- Difficulty: {difficulty} - {difficulty_instructions[difficulty]}

Requirements:
- Create EXACTLY {num_questions} questions (no more, no less)
- Difficulty level: {difficulty}
- Include variety: Multiple Choice Questions (MCQ), Short Answer, Long Answer, and Numerical Problems
- CBSE curriculum-aligned for {grade} level
- Questions should be appropriate for {difficulty} difficulty
- For each question, provide a detailed, step-by-step answer

Format EXACTLY as shown below (maintain this format strictly):
Q1. [Question text]
A1. [Detailed answer with explanation]

Q2. [Question text]
A2. [Detailed answer with explanation]

Continue this pattern for all {num_questions} questions."""

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

def parse_questions_and_answers(generated_text):
    """Parse generated text into questions and answers lists"""
    questions_list = []
    answers_list = []
    
    lines = generated_text.split('\n')
    current_question = ""
    current_answer = ""
    
    for line in lines:
        line = line.strip()
        if line.startswith('Q') and '.' in line:
            if current_question:
                questions_list.append(current_question.strip())
            current_question = line.split('.', 1)[1].strip() if '.' in line else line
        elif line.startswith('A') and '.' in line:
            if current_answer:
                answers_list.append(current_answer.strip())
            current_answer = line.split('.', 1)[1].strip() if '.' in line else line
        elif line and current_question:
            if current_answer or line.startswith('A'):
                current_answer += " " + line
            else:
                current_question += " " + line
    
    if current_question:
        questions_list.append(current_question.strip())
    if current_answer:
        answers_list.append(current_answer.strip())
    
    return questions_list, answers_list