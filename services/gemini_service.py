import streamlit as st
import google.generativeai as genai
import os
from config.settings import load_api_key, GEMINI_MODEL, get_model_pricing

# ---------------------------------------------------
# LANGFUSE INITIALIZATION
# ---------------------------------------------------
print("=" * 50)
print("🔍 LANGFUSE DEBUG MODE")
print("=" * 50)

try:
    from langfuse import Langfuse
    LANGFUSE_AVAILABLE = True
    print("✅ Langfuse package imported successfully")
except ImportError as e:
    LANGFUSE_AVAILABLE = False
    print(f"❌ Langfuse package not found: {e}")

langfuse = None
langfuse_enabled = False

if LANGFUSE_AVAILABLE:
    print("\n🔍 Checking environment variables...")

    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

    print(f"   LANGFUSE_PUBLIC_KEY exists: {bool(public_key)}")
    print(f"   LANGFUSE_SECRET_KEY exists: {bool(secret_key)}")
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
        print("❌ Langfuse keys missing")
else:
    print("❌ Langfuse not available")

print("=" * 50)
print()


def initialize_gemini():
    """Initialize Google Gemini API"""
    api_key = load_api_key()
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"❌ Error configuring Gemini API: {str(e)}")
        st.stop()


def get_session_id():
    """Get or create unique session ID"""
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
    return st.session_state.session_id


def generate_worksheet_content(grade, subject, chapter, difficulty, num_questions):
    """
    Generate worksheet with EXACT question count guaranteed
    """

    difficulty_instructions = {
        "Easy": f"suitable for {grade} students who are just beginning to learn {chapter}. Basic fundamental concepts only.",
        "Medium": f"suitable for {grade} students with intermediate knowledge of {chapter}. Application-level thinking required.",
        "Hard": f"suitable for {grade} students who have mastered {chapter}. Challenging, deep analytical questions."
    }

    # IMPROVED PROMPT: Emphasize EXACT count
    prompt = f"""
YOU MUST GENERATE EXACTLY {num_questions} QUESTIONS. NO MORE, NO LESS.

Generate {difficulty} difficulty questions for {grade} students on: {chapter} ({subject})

Context:
- Grade: {grade}
- Subject: {subject}
- Chapter: {chapter}
- Difficulty: {difficulty} - {difficulty_instructions[difficulty]}

CRITICAL REQUIREMENTS:
1. GENERATE EXACTLY {num_questions} QUESTIONS (count them!)
2. Each question MUST have a detailed answer
3. Include variety: MCQ, Short Answer, Long Answer, Numerical
4. CBSE curriculum-aligned
5. No duplicate questions

FORMAT (STRICTLY FOLLOW):
Q1. [Question text here]
A1. [Detailed answer with steps]

Q2. [Question text here]
A2. [Detailed answer with steps]

...continue exactly until Q{num_questions}

REMEMBER: You must generate ALL {num_questions} questions. Double-check your count before responding.
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
            print("✅ Trace created successfully")
        except Exception as e:
            print(f"⚠️ Trace creation failed: {e}")

    # Call Gemini API with higher token limit
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.7,
            max_output_tokens=8192  # Ensure enough space for all questions
        )
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

    # Log usage to Langfuse
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
                    "difficulty": difficulty,
                    "requested_questions": num_questions
                }
            )

            langfuse.score(
                trace_id=trace_id,
                name="total_cost_usd",
                value=total_cost
            )

            print("✅ Logged to Langfuse successfully")
        except Exception as e:
            print(f"⚠️ Langfuse logging failed: {e}")

    return response.text, {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "model": GEMINI_MODEL
    }


def parse_questions_and_answers(generated_text):
    """
    Parse Q & A into separate lists
    IMPROVED: Better handling of multiline questions/answers
    """

    questions_list = []
    answers_list = []

    lines = generated_text.split("\n")
    current_question = ""
    current_answer = ""
    in_question = False
    in_answer = False

    for line in lines:
        line = line.strip()

        # Detect question start
        if line.startswith("Q") and "." in line and not line.startswith("Q."):
            # Save previous question if exists
            if current_question:
                questions_list.append(current_question.strip())
                current_question = ""
            
            # Start new question
            current_question = line.split(".", 1)[1].strip() if len(line.split(".", 1)) > 1 else ""
            in_question = True
            in_answer = False

        # Detect answer start
        elif line.startswith("A") and "." in line and not line.startswith("A."):
            # Save previous answer if exists
            if current_answer:
                answers_list.append(current_answer.strip())
                current_answer = ""
            
            # Start new answer
            current_answer = line.split(".", 1)[1].strip() if len(line.split(".", 1)) > 1 else ""
            in_answer = True
            in_question = False

        # Continue building current question or answer
        elif line:
            if in_answer:
                current_answer += " " + line
            elif in_question:
                current_question += " " + line

    # Add last question and answer
    if current_question:
        questions_list.append(current_question.strip())
    if current_answer:
        answers_list.append(current_answer.strip())

    return questions_list, answers_list