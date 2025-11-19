"""
Admin Dashboard - View token usage and costs
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from services.token_logger import get_logs, get_daily_stats, get_all_time_stats
from config.settings import ADMIN_PASSWORD

def check_admin_access():
    """Check if user has entered correct admin password"""
    
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False
    
    if not st.session_state.admin_authenticated:
        st.markdown("## 🔐 Admin Access Required")
        
        password = st.text_input("Enter Admin Password", type="password")
        
        if st.button("Login"):
            if password == ADMIN_PASSWORD:
                st.session_state.admin_authenticated = True
                st.success("✅ Access granted!")
                st.rerun()
            else:
                st.error("❌ Incorrect password")
        
        st.stop()


def render_admin_dashboard():
    """Render the admin dashboard with token analytics"""
    
    # Check authentication
    check_admin_access()
    
    st.markdown("<h1 style='text-align: center;'>📊 Token Usage Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # Logout button
    if st.button("🚪 Logout", key="logout_btn"):
        st.session_state.admin_authenticated = False
        st.rerun()
    
    st.markdown("---")
    
    # ===== ALL-TIME STATS =====
    st.markdown("### 🌍 All-Time Statistics")
    all_time = get_all_time_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tokens", f"{all_time['total_tokens']:,}")
    
    with col2:
        st.metric("Total Cost", f"${all_time['total_cost']:.4f}")
    
    with col3:
        st.metric("API Requests", f"{all_time['request_count']:,}")
    
    with col4:
        st.metric("Unique Users", f"{all_time['unique_users']:,}")
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # ===== TODAY'S STATS =====
    st.markdown("### 📅 Today's Statistics")
    today = datetime.now().strftime("%Y-%m-%d")
    today_stats = get_daily_stats(today)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Today's Tokens", f"{today_stats['total_tokens']:,}")
    
    with col2:
        st.metric("Today's Cost", f"${today_stats['total_cost']:.4f}")
    
    with col3:
        st.metric("Today's Requests", f"{today_stats['request_count']:,}")
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # ===== DATE FILTER =====
    st.markdown("### 🔍 Filter by Date")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_date = st.date_input(
            "Select Date",
            value=datetime.now(),
            max_value=datetime.now()
        )
    
    with col2:
        num_records = st.number_input("Number of Records", min_value=10, max_value=500, value=50)
    
    date_str = selected_date.strftime("%Y-%m-%d")
    
    if st.button("🔎 Filter Logs", use_container_width=True):
        filtered_stats = get_daily_stats(date_str)
        
        st.markdown(f"#### Stats for {date_str}")
        
        fcol1, fcol2, fcol3 = st.columns(3)
        with fcol1:
            st.metric("Tokens", f"{filtered_stats['total_tokens']:,}")
        with fcol2:
            st.metric("Cost", f"${filtered_stats['total_cost']:.4f}")
        with fcol3:
            st.metric("Requests", f"{filtered_stats['request_count']:,}")
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # ===== RECENT ACTIVITY =====
    st.markdown("### 📋 Recent Activity")
    
    logs = get_logs(limit=num_records)
    
    if logs:
        df = pd.DataFrame(logs)
        
        # Format dataframe
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
        df['cost_usd'] = df['cost_usd'].apply(lambda x: f"${x:.6f}")
        
        # Reorder columns
        display_df = df[[
            'timestamp', 
            'user_action', 
            'model_name',
            'input_tokens', 
            'output_tokens', 
            'total_tokens', 
            'cost_usd'
        ]]
        
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Logs as CSV",
            data=csv,
            file_name=f"token_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.info("No logs found.")
    
    st.markdown("<div style='margin: 3rem 0;'></div>", unsafe_allow_html=True)
    
    # ===== COST BREAKDOWN =====
    st.markdown("### 💰 Cost Breakdown")
    
    if logs:
        df_cost = pd.DataFrame(logs)
        
        # Group by model
        model_costs = df_cost.groupby('model_name').agg({
            'cost_usd': 'sum',
            'total_tokens': 'sum',
            'user_action': 'count'
        }).reset_index()
        
        model_costs.columns = ['Model', 'Total Cost ($)', 'Total Tokens', 'Request Count']
        model_costs['Total Cost ($)'] = model_costs['Total Cost ($)'].apply(lambda x: f"${x:.6f}")
        
        st.dataframe(model_costs, use_container_width=True, hide_index=True)