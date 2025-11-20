import streamlit as st
import google.generativeai as genai
<<<<<<< HEAD
import os
from config.settings import load_api_key, GEMINI_MODEL, get_model_pricing

# Debug: Print what we're loading
print("=" * 50)
print("🔍 LANGFUSE DEBUG MODE")
print("=" * 50)

# Try to import Langfuse
try:
    from langfuse_sdk import Langfuse
    LANGFUSE_AVAILABLE = True
    print("✅ Langfuse package imported successfully")
except ImportError as e:
    LANGFUSE_AVAILABLE = False
    print(f"❌ Langfuse package not found: {e}")

# Initialize Langfuse
langfuse = None
langfuse_enabled = False

if LANGFUSE_AVAILABLE:
    print("\n🔍 Checking environment variables...")

    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

    print(f"   LANGFUSE_PUBLIC_KEY exists: {bool(public_key)}")
    if public_key:
        print(f"   LANGFUSE_PUBLIC_KEY: {public_key[:15]}...")

    print(f"   LANGFUSE_SECRET_KEY exists: {bool(secret_key)}")
    if secret_key:
        print(f"   LANGFUSE_SECRET_KEY: {secret_key[:15]}...")

    print(f"   LANGFUSE_HOST: {host}")

    if public_key and secret_key:
        try:
            print("\n🔄 Attempting to initialize Langfuse...")
            langfuse = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=host
            )
            langfuse_enabled = True
            print("✅ Langfuse initialized successfully!")
        except Exception as e:
            print(f"❌ Langfuse initialization failed: {e}")
            langfuse_enabled = False
    else:
        print("❌ Langfuse keys not found in environment variables")
else:
    print("❌ Langfuse package not available")

print("=" * 50)
print()

=======
from config.settings import load_api_key
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f

def initialize_gemini():
    """Initialize Google Gemini API"""
    api_key = load_api_key()
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"❌ Error configuring Gemini API: {str(e)}")
        st.stop()

<<<<<<< HEAD

def get_session_id():
    """Get or create unique session ID"""
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id


def generate_worksheet_content(grade, subject, chapter, difficulty, num_questions):
    """Generate worksheet with Langfuse v3 tracking"""

    difficulty_instructions = {
        "Easy": f"suitable for {grade} students who are just beginning to learn {chapter}. Basic concepts only.",
        "Medium": f"suitable for {grade} students with intermediate knowledge of {chapter}. Application-level.",
        "Hard": f"suitable for {grade} students who mastered {chapter}. Challenging, high-depth questions."
    }

=======
def generate_worksheet_content(grade, subject, chapter, difficulty, num_questions):
    """Generate worksheet questions using Gemini API"""
    
    difficulty_instructions = {
        "Easy": f"suitable for {grade} students who are just beginning to learn {chapter}. Questions should test basic understanding and fundamental concepts.",
        "Medium": f"suitable for {grade} students with intermediate knowledge of {chapter}. Questions should require application of concepts and some problem-solving.",
        "Hard": f"suitable for {grade} students who have mastered {chapter}. Questions should be challenging, requiring deep understanding, critical thinking, and advanced problem-solving skills."
    }
    
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    prompt = f"""Generate exactly {num_questions} {difficulty} difficulty questions for {grade} students on the topic: {chapter} ({subject}).

Context:
- Grade Level: {grade}
- Subject: {subject}
- Chapter: {chapter}
- Difficulty: {difficulty} - {difficulty_instructions[difficulty]}

Requirements:
<<<<<<< HEAD
- EXACTLY {num_questions} questions
- Include MCQ, short answer, long answer, numerical problems
- Each question MUST have a detailed solution

Format:
Q1. [Question]
A1. [Answer]

Q2. [Question]
A2. [Answer]

Continue till {num_questions} questions.
"""

    # Create Langfuse trace
    trace_id = None
    if langfuse_enabled and langfuse:
        try:
            print(f"\n📊 Creating Langfuse trace for {grade} {subject}")
            trace = langfuse.trace(
                name="worksheet_generation",
                user_id=get_session_id(),
                metadata={
                    "grade": grade,
                    "subject": subject,
                    "chapter": chapter,
                    "difficulty": difficulty,
                    "num_questions": num_questions
                }
            )
            trace_id = trace.id
            print(f"✅ Trace created successfully")
        except Exception as e:
            print(f"⚠️ Trace creation failed: {e}")

    # Call Gemini API
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(temperature=0.7)
    )

    # Extract usage
    try:
        usage = response.usage_metadata
        input_tokens = usage.prompt_token_count
        output_tokens = usage.candidates_token_count
        total_tokens = usage.total_token_count
    except:
        input_tokens = output_tokens = total_tokens = 0

    # Calculate cost
    pricing = get_model_pricing(GEMINI_MODEL)
    input_cost = (input_tokens / 1000) * pricing["input_per_1k"]
    output_cost = (output_tokens / 1000) * pricing["output_per_1k"]
    total_cost = input_cost + output_cost

    # Log to Langfuse using v3 API
    if langfuse_enabled and langfuse and trace_id:
        try:
            langfuse.generation(
                name="gemini_worksheet_generation",
                trace_id=trace_id,
                model=GEMINI_MODEL,
                input=prompt,
                output=response.text,
                usage={
                    "input": input_tokens,
                    "output": output_tokens,
                    "total": total_tokens,
                    "unit": "TOKENS"
                },
                metadata={
                    "provider": "google",
                    "grade": grade,
                    "subject": subject,
                    "chapter": chapter,
                    "difficulty": difficulty
                }
            )

            # Store cost inside Langfuse
            langfuse.score(
                trace_id=trace_id,
                name="total_cost_usd",
                value=total_cost
            )

            print(f"✅ Logged to Langfuse successfully")
        except Exception as e:
            print(f"⚠️ Langfuse logging failed: {e}")

    return response.text, {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "model": GEMINI_MODEL
    }


def parse_questions_and_answers(generated_text):
    """Parse Q & A into separate lists"""
    questions_list = []
    answers_list = []

    lines = generated_text.split('\n')
    current_question = ""
    current_answer = ""

=======
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
    
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    for line in lines:
        line = line.strip()
        if line.startswith('Q') and '.' in line:
            if current_question:
                questions_list.append(current_question.strip())
<<<<<<< HEAD
            current_question = line.split('.', 1)[1].strip()

        elif line.startswith('A') and '.' in line:
            if current_answer:
                answers_list.append(current_answer.strip())
            current_answer = line.split('.', 1)[1].strip()

        elif line:
            if current_answer:
                current_answer += " " + line
            elif current_question:
                current_question += " " + line

=======
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
    
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
    if current_question:
        questions_list.append(current_question.strip())
    if current_answer:
        answers_list.append(current_answer.strip())
<<<<<<< HEAD

    return questions_list, answers_list
=======
    
    return questions_list, answers_list
>>>>>>> e006eed1bcfc9cc9e5d9cab6c33fde6428640f1f
