import streamlit as st
from PIL import Image
from utils.image_analysis import analyze_image
from utils.caption_generator import generate_instagram_captions
from utils.hashtag_helper import suggest_hashtags
from utils.bio_generator import generate_bio
from utils.filters import apply_filter
from io import BytesIO
import torch
import warnings

def get_image_download_bytes(image, format='PNG'):
    img_bytes = BytesIO()
    image.save(img_bytes, format=format)
    img_bytes.seek(0)
    return img_bytes.getvalue()

st.set_page_config(
    page_title="InstaCaps - Instagram Caption Assistant",
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
.settings-card {
    background-color: #ffffff;
    border-radius: 14px;
    box-shadow: 0 2px 12px rgba(124, 144, 219, 0.08);
    border: 1px solid #e0e6ed;
    padding: 1.5rem 1.2rem;
    margin-bottom: 1.5rem;
}
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
.stButton>button {
    background: linear-gradient(90deg, #7c90db 0%, #f6e7cb 100%);
    color: #2c3e50;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.08em;
    padding: 0.7rem 1.5rem;
    border: none;
    margin-top: 0.6rem;
}
</style>
""", unsafe_allow_html=True)

warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")
torch.set_float32_matmul_precision('high')

st.markdown("""
<div class="brand-bar">
    <h1>InstaCaps</h1>
    <p>Fast AI-powered captions, hashtags, and bios for Instagram</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    with st.container():
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.subheader("Settings")
        creativity = st.slider("Creativity level", 0.5, 1.0, 0.85)
        num_hashtags = st.slider("Number of hashtags", 5, 20, 15)
        style = st.selectbox("Caption Style", ["Default", "Funny", "Motivational", "Minimalist", "Question"])
        language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Hindi"])
        filter_name = st.selectbox("Image Filter", ["None", "Grayscale", "Sepia", "Brighten", "Contrast"])
        st.markdown("---")
        st.markdown("**How it works:**\n1. Upload image\n2. Choose settings\n3. Generate content")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.subheader("Bio Generator")
        interests = st.text_input("Your interests (comma separated)", "travel, photography, lifestyle")
        bio_tone = st.selectbox("Bio Tone", ["professional", "casual"])
        bio_length = st.selectbox("Bio Length", ["short", "medium", "long"])
        
        if st.button("Generate Bio"):
            bio = generate_bio(interests, creativity=creativity, length=bio_length, tone=bio_tone)
            st.success(bio)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader("Select your image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file:
            image = Image.open(uploaded_file)
            if filter_name != "None":
                image = apply_filter(image, filter_name)
            st.image(image, use_column_width=True, caption="Preview")

            # Download filtered image button
            img_bytes = get_image_download_bytes(image)
            st.download_button(
                label="Download Filtered Image",
                data=img_bytes,
                file_name="filtered_image.png",
                mime="image/png",
                use_container_width=True
            )

            with st.spinner("Analyzing image..."):
                description = analyze_image(image)
            st.markdown("**Image Description:**")
            st.info(description)

            if st.button("Generate Content", use_container_width=True):
                with st.spinner("Generating captions..."):
                    captions = generate_instagram_captions(
                        image,
                        creativity=creativity,
                        style=style,
                        language=language,
                        num_captions=3
                    )
                with st.spinner("Suggesting hashtags..."):
                    hashtags = suggest_hashtags(description, max_hashtags=num_hashtags, captions=captions)
                
                st.subheader("Instagram Captions")
                for idx, caption in enumerate(captions, 1):
                    st.markdown(f'<div class="result-card"><b>Option {idx}:</b> {caption}</div>', unsafe_allow_html=True)
                
                st.markdown("**Hashtags**")
                st.markdown(f'<div class="hashtag-container">{" ".join(hashtags)}</div>', unsafe_allow_html=True)

                caption_text = "\n\n".join([f"Option {idx}: {cap}" for idx, cap in enumerate(captions, 1)])
                caption_text += f"\n\nHashtags:\n{' '.join(hashtags)}"
                st.download_button("Download Content", caption_text, file_name="instacaps_content.txt", use_container_width=True)
        else:
            st.info("Upload an image to generate Instagram-ready captions and hashtags.")

st.markdown("""
<div style="text-align: center; padding: 2rem 0 1rem 0; color: #8a97b1;">
    InstaCaps &copy; 2025 &mdash; Fast, Relevant, Ready
</div>
""", unsafe_allow_html=True)
