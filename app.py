import streamlit as st
from home import main as home_page
from chat import main as chat_page
from app1 import main as app1_page
from response import main as response_page

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Multi-Page App",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Text Analysis", "Chat Analyzer"])

# Routing logic
if page == "Home":
    home_page()
elif page == "Text Analysis":
    chat_page()
elif page == "Chat Analyzer":
    app1_page()
elif page == "Wound Classification":
    response_page()