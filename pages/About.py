import streamlit as st
from PIL import Image
import datetime

st.set_page_config(
    page_title="About Us - InstaCaps",
    layout="wide",
    page_icon="📸"
)

st.markdown("""
<style>
.brand-bar {
    background: #e3eafc;
    padding: 1.2rem 0.5rem 1.2rem 0.5rem;
    border-radius: 0 0 18px 18px;
    margin-bottom: 1.5rem;
    text-align: center;
    box-shadow: 0 2px 12px rgba(124, 144, 219, 0.07);
}
.brand-bar h1 {
    margin: 0;
    font-size: 2.1rem;
    font-weight: 700;
    letter-spacing: 1px;
    color: #4a6fa5;
}
.brand-bar p {
    margin: 0.2rem 0 0 0;
    font-size: 1.1rem;
    color: #6c757d;
    font-weight: 400;
}
.about-card {
    background-color: #ffffff;
    border-radius: 14px;
    box-shadow: 0 2px 12px rgba(124, 144, 219, 0.08);
    border: 1px solid #e0e6ed;
    padding: 2rem 1.5rem;
    margin-bottom: 1.5rem;
}
.feature-card {
    background: linear-gradient(135deg, #f6f8fa 0%, #e3eafc 100%);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    border-left: 4px solid #7c90db;
}
.team-card {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(124, 144, 219, 0.1);
    padding: 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
}
.stats-container {
    background: linear-gradient(135deg, #7c90db 0%, #f6e7cb 100%);
    border-radius: 14px;
    padding: 2rem;
    text-align: center;
    color: white;
    margin: 2rem 0;
}
.stats-number {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.stats-label {
    font-size: 1.1rem;
    opacity: 0.9;
}
.footer {
    text-align: center;
    padding: 2rem 0 1rem 0;
    color: #8a97b1;
    font-size: 1.05em;
    margin-top: 2.5rem;
    border-top: 1px solid #e0e6ed;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="brand-bar">
    <h1>About InstaCaps</h1>
    <p>Empowering creators with AI-powered Instagram content</p>
</div>
""", unsafe_allow_html=True)

# Navigation back to main app
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("← Back to InstaCaps", use_container_width=True):
        st.switch_page("app.py")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    # Mission Statement
    st.markdown("""
    <div class="about-card">
        <h2>🚀 Our Mission</h2>
        <p style="font-size: 1.1em; line-height: 1.6;">
            InstaCaps revolutionizes social media content creation by harnessing the power of artificial intelligence. 
            We believe every creator deserves engaging, relevant captions and hashtags that amplify their voice and 
            connect them with their audience.
        </p>
        <p style="font-size: 1.1em; line-height: 1.6;">
            Our AI-powered platform analyzes your images and generates creative, contextually-aware captions in 
            multiple languages and styles, along with trending hashtags that maximize your content's reach.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # What We Do
    st.markdown("""
    <div class="about-card">
        <h2>💡 What We Do</h2>
        <p style="font-size: 1.1em; line-height: 1.6; margin-bottom: 1.5rem;">
            InstaCaps combines cutting-edge computer vision and natural language processing to understand your images 
            and create Instagram-ready content that resonates with your audience.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Quick Stats
    st.markdown("""
    <div class="stats-container">
        <div class="stats-number">5+</div>
        <div class="stats-label">Languages Supported</div>
        <hr style="margin: 1rem 0; opacity: 0.3;">
        <div class="stats-number">6</div>
        <div class="stats-label">Caption Styles</div>
        <hr style="margin: 1rem 0; opacity: 0.3;">
        <div class="stats-number">∞</div>
        <div class="stats-label">Creative Possibilities</div>
    </div>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("## ✨ Key Features")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🎨 AI Image Analysis</h3>
        <p>Advanced computer vision technology analyzes your images to understand context, objects, and scenes for highly relevant caption generation.</p>
    </div>
    
    <div class="feature-card">
        <h3>📝 Multiple Caption Styles</h3>
        <p>Generate captions in various tones: Default, Funny, Motivational, Poetic, Minimalist, and Question-based to match your brand voice.</p>
    </div>
    
    <div class="feature-card">
        <h3>🌍 Multilingual Support</h3>
        <p>Create content in English, Spanish, French, German, and Hindi to reach global audiences with culturally appropriate messaging.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔥 Smart Hashtag Generation</h3>
        <p>AI-powered hashtag suggestions based on image content and trending topics to maximize your post's discoverability and engagement.</p>
    </div>
    
    <div class="feature-card">
        <h3>✨ Image Filters</h3>
        <p>Apply professional filters (Grayscale, Sepia, Brighten, Contrast) to enhance your images before generating content.</p>
    </div>
    
    <div class="feature-card">
        <h3>💫 Bio Generator</h3>
        <p>Create compelling Instagram bios that reflect your personality and interests, available in professional and casual tones.</p>
    </div>
    """, unsafe_allow_html=True)

# Technology Stack
st.markdown("## 🛠️ Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="about-card">
        <h4>🧠 AI & ML</h4>
        <ul>
            <li>BLIP (Vision-Language Model)</li>
            <li>Transformers (Hugging Face)</li>
            <li>PyTorch Framework</li>
            <li>spaCy NLP Pipeline</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h4>🖥️ Frontend</h4>
        <ul>
            <li>Streamlit Framework</li>
            <li>Custom CSS Styling</li>
            <li>Responsive Design</li>
            <li>Interactive Components</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="about-card">
        <h4>⚙️ Backend</h4>
        <ul>
            <li>Python 3.12</li>
            <li>PIL Image Processing</li>
            <li>RESTful Architecture</li>
            <li>Modular Code Structure</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Team Section
st.markdown("## 👥 Development Team")
st.markdown("""
<div class="team-card">
    <h3>InstaCaps Development Team</h3>
    <p style="font-size: 1.1em; margin: 1rem 0;">
        Built with passion by developers who understand the challenges of social media content creation. 
        Our team combines expertise in artificial intelligence, computer vision, and user experience design 
        to create tools that empower creators worldwide.
    </p>
    <p style="color: #7c90db; font-weight: 600;">
        "Empowering creativity through intelligent automation"
    </p>
</div>
""", unsafe_allow_html=True)

# Project Journey
st.markdown("## 🌟 Project Journey")
st.markdown("""
<div class="about-card">
    <h4>📅 Development Timeline</h4>
    <ul style="font-size: 1.1em; line-height: 1.8;">
        <li><strong>Phase 1:</strong> Research and ideation - Identified the need for AI-powered caption generation</li>
        <li><strong>Phase 2:</strong> Core development - Implemented BLIP image analysis and caption generation</li>
        <li><strong>Phase 3:</strong> Feature expansion - Added multilingual support, styles, and hashtag generation</li>
        <li><strong>Phase 4:</strong> Optimization - Enhanced performance and user experience</li>
        <li><strong>Current:</strong> Continuous improvement based on user feedback and emerging AI technologies</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Future Vision
st.markdown("## 🔮 Future Vision")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-card">
        <h4>🚀 Upcoming Features</h4>
        <ul>
            <li>Video caption generation</li>
            <li>Brand voice customization</li>
            <li>Social media scheduling</li>
            <li>Analytics and insights</li>
            <li>Collaborative workspaces</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h4>🌍 Platform Expansion</h4>
        <ul>
            <li>TikTok caption support</li>
            <li>LinkedIn post optimization</li>
            <li>Twitter thread generation</li>
            <li>YouTube description writer</li>
            <li>Mobile app development</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Contact Information
st.markdown("## 📞 Get In Touch")
st.markdown("""
<div class="about-card">
    <div style="text-align: center;">
        <h4>Connect With Us</h4>
        <p style="font-size: 1.1em; margin: 1.5rem 0;">
            Have questions, suggestions, or want to collaborate? We'd love to hear from you!
        </p>
        <p style="color: #7c90db; font-size: 1.1em;">
            📧 Email: hello@instacaps.ai<br>
            🐦 Twitter: @InstaCapsAI<br>
            💼 LinkedIn: InstaCaps<br>
            🌐 Website: www.instacaps.ai
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 InstaCaps - Empowering creators with AI-powered content generation</p>
    <p style="margin-top: 0.5rem; opacity: 0.8;">
        Built with ❤️ using Python, Streamlit, and cutting-edge AI technology
    </p>
</div>
""", unsafe_allow_html=True)
