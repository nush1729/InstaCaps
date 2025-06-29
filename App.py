import streamlit as st
from PIL import Image
from utils.image_analysis import analyze_image
from utils.caption_generator import generate_captions
from utils.hashtag_helper import suggest_hashtags
import torch
import warnings

st.set_page_config(
    page_title="InstaCaps - Instagram Caption Assistant",
    layout="wide",
    page_icon="📸"
)

st.markdown("""
<style>
:root {
    --bg-main: #f9fafc;
    --accent: #f6e7cb;
    --header: #e3eafc;
    --button: #7c90db;
    --button-hover: #4a6fa5;
    --card: #ffffff;
    --border: #e0e6ed;
    --text-main: #2c3e50;
    --text-light: #6c757d;
}

.stApp {
    background-color: var(--bg-main);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--text-main);
}

/* Brand bar */
.brand-bar {
    background: var(--header);
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
    color: var(--text-light);
    font-weight: 400;
}

/* Settings card */
.settings-card {
    background-color: var(--card);
    border-radius: 14px;
    box-shadow: 0 2px 12px rgba(124, 144, 219, 0.08);
    border: 1px solid var(--border);
    padding: 1.5rem 1.2rem;
    margin-bottom: 1.5rem;
}

/* Upload card */
.upload-card {
    background-color: var(--card);
    border-radius: 14px;
    box-shadow: 0 2px 12px rgba(124, 144, 219, 0.08);
    border: 1px solid var(--border);
    padding: 1.5rem 1.2rem;
    margin-bottom: 1.5rem;
}

/* Results card */
.result-card {
    background-color: #f6f8fa;
    border-left: 4px solid #7c90db;
    padding: 1.3rem 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(124, 144, 219, 0.07);
    font-size: 1.08em;
}

.hashtag-container {
    background-color: #e3eafc;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 0.5rem;
    font-size: 1.05em;
    color: #4a6fa5;
    letter-spacing: 0.5px;
    border: 1px solid #d3dff3;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #7c90db 0%, #f6e7cb 100%);
    color: #2c3e50;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.08em;
    padding: 0.7rem 1.5rem;
    border: none;
    margin-top: 0.6rem;
    transition: background 0.3s, color 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #4a6fa5 0%, #f6e7cb 100%);
    color: #fff;
}

/* Footer */
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

#  Numerical stability for torch 
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")
torch.set_float32_matmul_precision('high')

st.markdown("""
<div class="brand-bar">
    <h1>InstaCaps</h1>
    <p>Generate engaging captions and discover trending hashtags for your Instagram posts</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    with st.container():
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.subheader("Settings")
        creativity = st.slider("Creativity level", 0.5, 1.0, 0.85)
        num_hashtags = st.slider("Number of hashtags", 5, 20, 15)
        st.markdown("---")
        st.markdown("**How it works:**")
        st.markdown("1. Upload your image  \n2. AI analyzes content  \n3. Generate captions  \n4. Get hashtag suggestions")
        st.markdown("---")
        st.markdown("**Pro Tip:**")
        st.info("Use high-quality images with clear subjects for best results")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="upload-card">', unsafe_allow_html=True)
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader("Select your image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True, caption="Preview")

            if st.button("Generate Content", use_container_width=True):
                with st.spinner("Analyzing image..."):
                    description = analyze_image(image)
                with st.spinner("Creating captions..."):
                    captions = generate_captions(description, creativity=creativity)
                with st.spinner("Suggesting hashtags..."):
                    hashtags = suggest_hashtags(description, max_hashtags=num_hashtags)

                st.subheader("Results")
                # Captions
                st.markdown("**Captions**")
                for idx, caption in enumerate(captions, 1):
                    st.markdown(f'<div class="result-card"><b>Option {idx}:</b> {caption}</div>', unsafe_allow_html=True)
                # Hashtags
                st.markdown("**Hashtags**")
                st.markdown(f'<div class="hashtag-container">{" ".join(hashtags)}</div>', unsafe_allow_html=True)

                # Download
                caption_text = "\n\n".join([f"Option {idx}: {cap}" for idx, cap in enumerate(captions, 1)])
                content = f"{caption_text}\n\nHashtags:\n{' '.join(hashtags)}"
                st.download_button("Download Content", content, file_name="instacaps_content.txt", use_container_width=True)
        else:
            st.info("Upload an image to generate Instagram-ready captions and hashtags.")

st.markdown("""
<div class="footer">
    InstaCaps &copy; 2025 &mdash; Elevate your Instagram content
</div>
""", unsafe_allow_html=True)
