import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import time
import pandas as pd
import plotly.express as px
import random
from PIL import Image
import io
import base64

# Set page configuration

# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to get base64 representation of an image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to add custom CSS
def load_css():
    st.markdown("""
    <style>
    /* General Page Styling */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #1a1a2e);
        color: white;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header and logo styling */
    .logo-text {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    
    .logo-subtext {
        font-size: 1.2rem;
        font-weight: 300;
        color: #e0e0e0;
        text-align: center;
        margin-top: 0;
    }
    
    /* Card styling */
    .card {
        border-radius: 10px;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #4776E6;
    }
    
    .card-text {
        font-size: 1rem;
        color: #e0e0e0;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #8E54E9, #4776E6);
        box-shadow: 0 5px 15px rgba(142, 84, 233, 0.4);
        transform: translateY(-2px);
    }
    
    /* Input field styling */
    .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(26, 26, 46, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
        color: #4776E6;
    }
    
    /* Animation for cards */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease forwards;
    }
    
    .delay-1 {
        animation-delay: 0.2s;
        opacity: 0;
    }
    
    .delay-2 {
        animation-delay: 0.4s;
        opacity: 0;
    }
    
    .delay-3 {
        animation-delay: 0.6s;
        opacity: 0;
    }
    
    .delay-4 {
        animation-delay: 0.8s;
        opacity: 0;
    }
    
    /* Stats counter animation */
    .counter {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #8E54E9;
    }
    
    .counter-label {
        font-size: 0.9rem;
        color: #e0e0e0;
    }
    
    /* Feature icons */
    .feature-icon {
        font-size: 2.5rem;
        color: #4776E6;
        margin-bottom: 1rem;
    }
    
    /* Call to action section */
    .cta-section {
        background: linear-gradient(90deg, rgba(71, 118, 230, 0.2), rgba(142, 84, 233, 0.2));
        border-radius: 10px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
    }
    
    .cta-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Testimonial section */
    .testimonial {
        font-style: italic;
        padding: 1rem 1.5rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .testimonial-author {
        font-weight: 500;
        color: #8E54E9;
        text-align: right;
    }
    
    /* Highlight text */
    .highlight {
        color: #8E54E9;
        font-weight: 600;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background-color: #4776E6;
    }
    
    /* Example cards */
    .example-card {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .example-positive {
        background: rgba(40, 167, 69, 0.1);
        border: 1px solid rgba(40, 167, 69, 0.2);
    }
    
    .example-negative {
        background: rgba(220, 53, 69, 0.1);
        border: 1px solid rgba(220, 53, 69, 0.2);
    }
    
    .example-neutral {
        background: rgba(108, 117, 125, 0.1);
        border: 1px solid rgba(108, 117, 125, 0.2);
    }
    
    .example-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Function to generate dummy sentiment analysis
def analyze_dummy_sentiment(text):
    # Simulate processing time
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    # Generate dummy scores
    if "excellent" in text.lower() or "amazing" in text.lower() or "love" in text.lower():
        sentiment = "Positive"
        score = random.uniform(0.7, 0.95)
        color = "#28a745"
    elif "terrible" in text.lower() or "bad" in text.lower() or "hate" in text.lower():
        sentiment = "Negative"
        score = random.uniform(-0.95, -0.7)
        color = "#dc3545"
    else:
        sentiment = "Neutral"
        score = random.uniform(-0.2, 0.2)
        color = "#6c757d"
    
    return {
        "sentiment": sentiment,
        "score": score,
        "color": color,
        "positive": max(0.05, min(0.95, 0.5 + score/2)),
        "negative": max(0.05, min(0.95, 0.5 - score/2)),
        "neutral": max(0.05, min(0.9, 0.5 - abs(score)/2))
    }

def main():
    # Load custom CSS
    load_css()
    
    # Load animations
    lottie_sentiment = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json")
    lottie_analysis = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_bdsthrsj.json")
    lottie_chart = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_gjvlm6kb.json")
    
    # Initialize session state variables
    if 'analysis_done' not in st.session_state:
        st.session_state.analysis_done = False
    if 'example_text' not in st.session_state:
        st.session_state.example_text = ""
    
    # Sidebar
    with st.sidebar:
        st.markdown("<h3>About Chatalyze</h3>", unsafe_allow_html=True)
        st.write("Chatalyze uses advanced algorithms to analyze the emotional tone of text. Get instant insights into the sentiment expressed in any piece of writing.")
        
        st.markdown("<h3>Examples</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="example-card example-positive" onclick="document.getElementById('text-input').value = 'I absolutely loved this product! It exceeded all my expectations and I would recommend it to everyone!'">
            <strong>Example (Positive):</strong> "I absolutely loved this product! It exceeded all my expectations and I would recommend it to everyone!"
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="example-card example-negative" onclick="document.getElementById('text-input').value = 'This was a terrible experience. The customer service was awful and the product didn\\'t work as advertised.'">
            <strong>Example (Negative):</strong> "This was a terrible experience. The customer service was awful and the product didn't work as advertised."
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="example-card example-neutral" onclick="document.getElementById('text-input').value = 'The meeting went as expected. We discussed the project timeline and assigned tasks to team members.'">
            <strong>Example (Neutral):</strong> "The meeting went as expected. We discussed the project timeline and assigned tasks to team members."
        </div>
        """, unsafe_allow_html=True)
        
        # Add example buttons that will work with Streamlit
        if st.button("Load Positive Example"):
            st.session_state.example_text = "I absolutely loved this product! It exceeded all my expectations and I would recommend it to everyone!"
        
        if st.button("Load Negative Example"):
            st.session_state.example_text = "This was a terrible experience. The customer service was awful and the product didn't work as advertised."
        
        if st.button("Load Neutral Example"):
            st.session_state.example_text = "The meeting went as expected. We discussed the project timeline and assigned tasks to team members."
    
    # Header section
    st.markdown('<h1 class="logo-text">Chatalyze</h1>', unsafe_allow_html=True)
    st.markdown('<p class="logo-subtext">Advanced Text Sentiment Analysis</p>', unsafe_allow_html=True)
    
    # Main content layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="fade-in delay-1">', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">Analyze Your Text</h3>', unsafe_allow_html=True)
        st.markdown('<p class="card-text">Enter your text below and discover the emotional tone behind your words.</p>', unsafe_allow_html=True)
        
        # Text input
        text_input = st.text_area("", value=st.session_state.example_text, height=150, key="text_input", placeholder="Type or paste your text here...")
        
        # Analyze button
        analyze_clicked = st.button("✨ Analyze Sentiment")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Show results if analysis is done
        if analyze_clicked and text_input:
            st.session_state.analysis_done = True
            st.session_state.results = analyze_dummy_sentiment(text_input)
        
        if st.session_state.analysis_done and hasattr(st.session_state, 'results'):
            results = st.session_state.results
            
            st.markdown('<div class="fade-in delay-2">', unsafe_allow_html=True)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<h3 class="card-title">Analysis Results</h3>', unsafe_allow_html=True)
            
            # Display sentiment result
            sentiment_color = results["color"]
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 style="color: {sentiment_color}; font-size: 2.5rem; margin-bottom: 5px;">{results["sentiment"]}</h2>
                <p style="font-size: 1.2rem;">Sentiment Score: <span style="color: {sentiment_color}; font-weight: 600;">{results["score"]:.2f}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Sentiment breakdown chart
            sentiment_data = {
                "Sentiment": ["Positive", "Negative", "Neutral"],
                "Score": [results["positive"], results["negative"], results["neutral"]]
            }
            sentiment_df = pd.DataFrame(sentiment_data)
            
            fig = px.bar(
                sentiment_df,
                x="Sentiment",
                y="Score",
                color="Sentiment",
                color_discrete_sequence=["#28a745", "#dc3545", "#6c757d"],
                labels={"Score": "Sentiment Score"},
                title="Sentiment Breakdown"
            )
            
            fig.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="fade-in delay-3">', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<h3 class="card-title">How It Works</h3>', unsafe_allow_html=True)
        st.markdown('<p class="card-text">Chatalyze uses advanced natural language processing (NLP) techniques to analyze the emotional tone of your text. Here\'s how it works:</p>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <div class="feature-icon">📝</div>
            <h4>1. Input Your Text</h4>
            <p>Enter or paste your text into the input box.</p>
        </div>
        <div style="margin-bottom: 1rem;">
            <div class="feature-icon">🔍</div>
            <h4>2. Analyze Sentiment</h4>
            <p>Click the "Analyze Sentiment" button to process your text.</p>
        </div>
        <div style="margin-bottom: 1rem;">
            <div class="feature-icon">📊</div>
            <h4>3. View Results</h4>
            <p>Get detailed insights into the sentiment expressed in your text.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Lottie animation
        if lottie_sentiment:
            st_lottie(lottie_sentiment, height=300, key="sentiment_animation")
    
    # Call to Action Section
    st.markdown('<div class="cta-section fade-in delay-4">', unsafe_allow_html=True)
    st.markdown('<h3 class="cta-title">Ready to Analyze Your Text?</h3>', unsafe_allow_html=True)
    st.markdown('<p class="card-text">Enter your text above and click the "Analyze Sentiment" button to get started.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Testimonials Section
    st.markdown('<div class="fade-in delay-4">', unsafe_allow_html=True)
    st.markdown('<h3>What Our Users Say</h3>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<div class="testimonial">', unsafe_allow_html=True)
        st.markdown('"Chatalyze is incredibly easy to use and provides accurate sentiment analysis. It has become an essential tool for my business."', unsafe_allow_html=True)
        st.markdown('<p class="testimonial-author">— John Doe, Marketing Manager</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="testimonial">', unsafe_allow_html=True)
        st.markdown('"I love how Chatalyze breaks down the sentiment into positive, negative, and neutral components. It\'s very insightful!"', unsafe_allow_html=True)
        st.markdown('<p class="testimonial-author">— Jane Smith, Content Creator</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()