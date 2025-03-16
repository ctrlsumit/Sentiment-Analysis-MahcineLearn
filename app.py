import streamlit as st
from home import main as home_page
from chat import main as chat_page
from app1 import main as app1_page
from response import main as response_page

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Chat Analysis", "WhatsApp Chat Analyzer", "Wound Classification"])

# Routing logic
if page == "Home":
    home_page()
elif page == "Chat Analysis":
    chat_page()
elif page == "WhatsApp Chat Analyzer":
    app1_page()
elif page == "Wound Classification":
    response_page()