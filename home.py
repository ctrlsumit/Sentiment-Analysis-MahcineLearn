import streamlit as st
from streamlit.components.v1 import html


def load_css():
    st.markdown("""
    <style>
    /* General Reset */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
    }

    body {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        line-height: 1.6;
        overflow-x: hidden;
    }

    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        max-width: 100% !important;
        padding: 0 !important;
    }

    /* Header */
    header{
      width : 100%;
      background-color : red;
                }
    .headBox {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        color: brown;
        width : 100%;
    }

    .navi {
        display: flex;
        min-width: 40%;
        justify-content: space-around;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
        color: green;
    }

    /* Sentibox Section */
    .sentibox {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2rem;
        margin-bottom: 4rem;
        animation: fadeIn 1s ease-in-out;
        padding: 0 2rem;
    }

    .cont-box {
        flex: 1;
    }

    .title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }

    .cont {
        font-size: 1.1rem;
        color: #e0e0e0;
        margin-bottom: 2rem;
    }

    .buttonSec {
        display: flex;
        gap: 1rem;
    }

    .buttonSec button {
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .buttonSec button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(142, 84, 233, 0.4);
    }

    .picbox {
        flex: 1;
        text-align: center;
    }

    .picbox img {
        max-width: 100%;
        border-radius: 10px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        animation: float 3s ease-in-out infinite;
    }

    /* Cards Section */
    .cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        animation: fadeIn 1.5s ease-in-out;
        padding: 0 2rem;
    }

    .card1, .card2, .card3 {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card1:hover, .card2:hover, .card3:hover {
        transform: translateY(-10px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }

    .card1 .image, .card2 .image, .card3 .image {
        text-align: center;
        margin-bottom: 1rem;
    }

    .card1 img, .card2 img, .card3 img {
        max-width: 100%;
        border-radius: 10px;
    }

    .head {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #4776E6;
    }

    .descrip {
        font-size: 1rem;
        color: #e0e0e0;
    }

    /* Footer Section */
    .footer-container {
        background-color: #1a1a2e;
        color: #f0f0f0;
        padding: 60px 0 20px;
        font-family: 'Poppins', Arial, sans-serif;
        margin-top: 4rem;
    }

    .footer-row {
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 30px;
        padding: 0 2rem;
    }

    .footer-col {
        padding: 0 15px;
        margin-bottom: 30px;
    }

    .footer-col.about {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .footer-col.links,
    .footer-col.resources,
    .footer-col.contact {
        flex: 0 0 33.333333%;
        max-width: 33.333333%;
    }

    .footer-col.newsletter {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .footer-col h3 {
        position: relative;
        margin-bottom: 20px;
        font-size: 18px;
        font-weight: 600;
        color: #4776E6;
    }

    .footer-col h3::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -10px;
        width: 50px;
        height: 2px;
        background: linear-gradient(90deg, #4776E6, #8E54E9);
    }

    .footer-col p {
        line-height: 1.8;
        margin-bottom: 20px;
    }

    .footer-col ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .footer-col ul li {
        margin-bottom: 10px;
    }

    .footer-col ul li a {
        color: #cccccc;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .footer-col ul li a:hover {
        color: #ffffff;
        padding-left: 8px;
    }

    .footer-col .social-links {
        display: flex;
        margin-top: 20px;
    }

    .footer-col .social-links a {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 40px;
        width: 40px;
        margin-right: 10px;
        border-radius: 50%;
        color: #ffffff;
        background: rgba(255, 255, 255, 0.1);
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .footer-col .social-links a:hover {
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        transform: translateY(-3px);
    }

    .newsletter-form {
        display: flex;
        margin-top: 20px;
        max-width: 500px;
    }

    .newsletter-form input {
        flex-grow: 1;
        padding: 12px 15px;
        border: none;
        border-radius: 4px 0 0 4px;
        background: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        outline: none;
    }

    .newsletter-form input::placeholder {
        color: #aaaaaa;
    }

    .newsletter-form button {
        padding: 0 20px;
        border: none;
        background: linear-gradient(90deg, #4776E6, #8E54E9);
        color: #ffffff;
        font-weight: 600;
        border-radius: 0 4px 4px 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .newsletter-form button:hover {
        background: linear-gradient(90deg, #8E54E9, #4776E6);
    }

    .footer-bottom {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 20px;
        text-align: center;
    }

    .footer-bottom p {
        margin: 0;
    }

    .footer-legal {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .footer-legal a {
        color: #cccccc;
        margin: 0 10px;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .footer-legal a:hover {
        color: #ffffff;
    }

    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes float {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .sentibox {
            flex-direction: column;
            text-align: center;
        }

        .buttonSec {
            justify-content: center;
        }

        .cards {
            grid-template-columns: 1fr;
        }

        .footer-col.links,
        .footer-col.resources,
        .footer-col.contact {
            flex: 0 0 100%;
            max-width: 100%;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def display_header():
    st.markdown("""
    <div class="headBox">
        <h1 class="title">Sentalyze</h1>
        <div class="navi">
            <div class="home">Home</div>
            <div class="about">About</div>
            <div class="contact">Contact</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_main():
    st.markdown("""
    <div class="sentibox">
        <div class="cont-box">
            <div class="title">Sentimental Analysis</div>
            <div class="cont">
                We can use sentiment analysis to monitor that product’s reviews. Sentiment analysis is also efficient to use when there is a large set of unstructured data, and we want to classify that data by automatically tagging it. Net Promoter Score (NPS) surveys are used extensively to gain knowledge of how a customer perceives a product or service. Sentiment analysis also gained popularity due to its feature to process large volumes of NPS responses and obtain consistent results quickly.
            </div>
            <div class="buttonSec">
                <a href="/">Analyze Text</a>
                <a href="/">Analyze Chats</a>
            </div>
        </div>
        <div class="picbox">
            <img src="https://www.scambs.gov.uk/media/16544/customer-feedback.png" alt="random image">
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cards">
        <div class="card1">
            <div class="image">
                <img src="https://www.diariopanorama.com/fotos/notas/2022/09/25/emojis-426768-130329.jpg" alt="rand">
            </div>
            <div class="cont">
                <div class="head">Emoji Usage</div>
                <div class="descrip">Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit molestias quia quam rerum nobis modi incidunt eum assumenda eos, harum numquam magnam dolorum a pariatur impedit! Sint doloribus soluta quos!</div>
            </div>
        </div>
        <div class="card2">
            <div class="image">
                <img src="https://i.pinimg.com/736x/f2/bd/95/f2bd9589ca8987a49a36e859b0cda2d4.jpg" alt="rand">
            </div>
            <div class="cont">
                <div class="head">Build Charts</div>
                <div class="descrip">Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit molestias quia quam rerum nobis modi incidunt eum assumenda eos, harum numquam magnam dolorum a pariatur impedit! Sint doloribus soluta quos!</div>
            </div>
        </div>
        <div class="card3">
            <div class="image">
                <img src="https://th.bing.com/th/id/OIP.uJpWdg3Kj_9sAPx_KaOnKAAAAA?rs=1&pid=ImgDetMain" alt="rand">
            </div>
            <div class="cont">
                <div class="head">Word Cloud</div>
                <div class="descrip">Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit molestias quia quam rerum nobis modi incidunt eum assumenda eos, harum numquam magnam dolorum a pariatur impedit! Sint doloribus soluta quos!</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_footer():
    st.markdown("""
    <div class="footer-container">
        <div class="footer-row">
            <div class="footer-col about">
                <h3>About Us</h3>
                <p>Sentalyze provides advanced sentiment analysis tools for businesses and individuals to understand the emotional context of text data. Our mission is to help you make informed decisions through powerful text analysis.</p>
            </div>
            <div class="footer-col links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#pricing">Pricing</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </div>
            <div class="footer-col resources">
                <h3>Resources</h3>
                <ul>
                    <li><a href="#blog">Blog</a></li>
                    <li><a href="#documentation">Documentation</a></li>
                    <li><a href="#api">API</a></li>
                    <li><a href="#faq">FAQs</a></li>
                    <li><a href="#support">Support</a></li>
                </ul>
            </div>
            <div class="footer-col contact">
                <h3>Contact Us</h3>
                <p>
                    <i class="fa fa-map-marker"></i> 123 Analysis Street, Data City, 10001
                </p>
                <p>
                    <i class="fa fa-phone"></i> +1-555-123-4567
                </p>
                <p>
                    <i class="fa fa-envelope"></i> <a href="mailto:info@sentiscan.com">info@sentiscan.com</a>
                </p>
                <div class="social-links">
                    <a href="#"><i class="fa fa-facebook"></i></a>
                    <a href="#"><i class="fa fa-twitter"></i></a>
                    <a href="#"><i class="fa fa-linkedin"></i></a>
                    <a href="#"><i class="fa fa-github"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-row">
            <div class="footer-col newsletter">
                <h3>Subscribe to Our Newsletter</h3>
                <p>Stay updated with our latest features and news</p>
                <form class="newsletter-form">
                    <input type="email" placeholder="Enter your email" required>
                    <button type="submit">Subscribe</button>
                </form>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 Sentalyze. All rights reserved.</p>
            <div class="footer-legal">
                <a href="#privacy">Privacy Policy</a>
                <a href="#terms">Terms of Service</a>
                <a href="#cookies">Cookie Policy</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    load_css()
    display_header()
    display_main()
    display_footer()

if __name__ == "__main__":
    main()