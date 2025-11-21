"""
Universal Langfuse Helper - Works with all versions
"""
import os
from datetime import datetime

# Try to import Langfuse
try:
    from langfuse import Langfuse
    LANGFUSE_AVAILABLE = True
except ImportError:
    LANGFUSE_AVAILABLE = False

# Initialize
langfuse = None
langfuse_enabled = False

if LANGFUSE_AVAILABLE:
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
    
    if public_key and secret_key:
        try:
            langfuse = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=host
            )
            langfuse_enabled = True
            print("✅ Langfuse helper initialized")
        except Exception as e:
            print(f"⚠️ Langfuse init failed: {e}")


def log_button_click(button_name, metadata=None):
    """
    Universal button click tracker
    Works with Langfuse SDK v2.x and v3.x
    """
    if not langfuse_enabled or not langfuse:
        return False
    
    metadata = metadata or {}
    metadata["timestamp"] = datetime.now().isoformat()
    metadata["event_type"] = "button_click"
    
    try:
        # Try method 1: Direct event logging (v3.x)
        langfuse.event(
            name=button_name,
            metadata=metadata
        )
        print(f"✅ Langfuse: {button_name} tracked (v3)")
        return True
    except (AttributeError, TypeError):
        pass
    
    try:
        # Try method 2: Score logging (v2.x alternative)
        langfuse.score(
            name=button_name,
            value=1,
            data_type="NUMERIC",
            comment=str(metadata)
        )
        print(f"✅ Langfuse: {button_name} tracked (v2 score)")
        return True
    except (AttributeError, TypeError):
        pass
    
    try:
        # Try method 3: Observation (fallback)
        langfuse.observation(
            name=button_name,
            type="EVENT",
            metadata=metadata
        )
        print(f"✅ Langfuse: {button_name} tracked (observation)")
        return True
    except Exception as e:
        print(f"⚠️ All Langfuse methods failed: {e}")
        return False


def log_generation(trace_id, prompt, response, tokens_in, tokens_out, metadata=None):
    """
    Log generation to Langfuse
    """
    if not langfuse_enabled or not langfuse:
        return False
    
    try:
        langfuse.generation(
            name="gemini_generation",
            trace_id=trace_id,
            input=prompt,
            output=response,
            usage={
                "input": tokens_in,
                "output": tokens_out,
                "total": tokens_in + tokens_out
            },
            metadata=metadata or {}
        )
        print("✅ Langfuse: Generation logged")
        return True
    except Exception as e:
        print(f"⚠️ Generation logging failed: {e}")
        return False