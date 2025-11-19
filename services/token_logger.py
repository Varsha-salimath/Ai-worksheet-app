"""
Token Logger Service - Track Gemini API usage and costs
Uses SQLite database for persistence
"""

import sqlite3
import uuid
from datetime import datetime
from config.settings import TOKEN_LOG_DB, get_model_pricing

def init_database():
    """Initialize SQLite database for token logs"""
    conn = sqlite3.connect(TOKEN_LOG_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS token_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            session_id TEXT NOT NULL,
            input_tokens INTEGER NOT NULL,
            output_tokens INTEGER NOT NULL,
            total_tokens INTEGER NOT NULL,
            cost_usd REAL NOT NULL,
            model_name TEXT NOT NULL,
            user_action TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()


def get_session_id():
    """Get or create session ID"""
    import streamlit as st
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    
    return st.session_state.session_id


def calculate_cost(input_tokens, output_tokens, model_name):
    """
    Calculate cost in USD based on token usage
    
    Returns:
        float: Total cost in USD
    """
    pricing = get_model_pricing(model_name)
    
    input_cost = (input_tokens / 1000) * pricing["input_per_1k"]
    output_cost = (output_tokens / 1000) * pricing["output_per_1k"]
    total_cost = input_cost + output_cost
    
    return round(total_cost, 6)


def log_token_usage(input_tokens, output_tokens, model_name, user_action="api_call"):
    """
    Log token usage to database
    
    Args:
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        model_name: Name of the model used
        user_action: Description of the action (e.g., "worksheet_generation")
    """
    
    # Initialize DB if not exists
    init_database()
    
    session_id = get_session_id()
    total_tokens = input_tokens + output_tokens
    cost_usd = calculate_cost(input_tokens, output_tokens, model_name)
    timestamp = datetime.now().isoformat()
    
    # Insert into database
    conn = sqlite3.connect(TOKEN_LOG_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO token_logs 
        (timestamp, session_id, input_tokens, output_tokens, total_tokens, cost_usd, model_name, user_action)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, session_id, input_tokens, output_tokens, total_tokens, cost_usd, model_name, user_action))
    
    conn.commit()
    conn.close()


def get_logs(limit=20, date_filter=None):
    """
    Retrieve logs from database
    
    Args:
        limit: Max number of logs to return
        date_filter: Filter by date (YYYY-MM-DD format)
    
    Returns:
        List of log dictionaries
    """
    init_database()
    
    conn = sqlite3.connect(TOKEN_LOG_DB)
    cursor = conn.cursor()
    
    if date_filter:
        cursor.execute("""
            SELECT * FROM token_logs 
            WHERE DATE(timestamp) = ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (date_filter, limit))
    else:
        cursor.execute("""
            SELECT * FROM token_logs 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
    
    rows = cursor.fetchall()
    conn.close()
    
    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "timestamp": row[1],
            "session_id": row[2],
            "input_tokens": row[3],
            "output_tokens": row[4],
            "total_tokens": row[5],
            "cost_usd": row[6],
            "model_name": row[7],
            "user_action": row[8]
        })
    
    return logs


def get_daily_stats(date=None):
    """
    Get aggregated stats for a specific date
    
    Args:
        date: Date in YYYY-MM-DD format (defaults to today)
    
    Returns:
        Dict with total_tokens, total_cost, request_count
    """
    init_database()
    
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    conn = sqlite3.connect(TOKEN_LOG_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            SUM(total_tokens) as total_tokens,
            SUM(cost_usd) as total_cost,
            COUNT(*) as request_count
        FROM token_logs
        WHERE DATE(timestamp) = ?
    """, (date,))
    
    row = cursor.fetchone()
    conn.close()
    
    return {
        "total_tokens": row[0] or 0,
        "total_cost": round(row[1], 6) if row[1] else 0.0,
        "request_count": row[2] or 0
    }


def get_all_time_stats():
    """Get all-time aggregated statistics"""
    init_database()
    
    conn = sqlite3.connect(TOKEN_LOG_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            SUM(total_tokens) as total_tokens,
            SUM(cost_usd) as total_cost,
            COUNT(*) as request_count,
            COUNT(DISTINCT session_id) as unique_users
        FROM token_logs
    """)
    
    row = cursor.fetchone()
    conn.close()
    
    return {
        "total_tokens": row[0] or 0,
        "total_cost": round(row[1], 6) if row[1] else 0.0,
        "request_count": row[2] or 0,
        "unique_users": row[3] or 0
    }