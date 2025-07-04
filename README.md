# InstaCaps - AI-Powered Instagram Captions ,Hashtags & Bios Generator

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.28.0-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-Powered-green.svg" alt="AI Powered">
  <img src="https://img.shields.io/badge/Academic%20Project-2025-yellow.svg" alt="Academic Project">
</div>

<p align="center">
  <strong>A Generative AI project for automating Instagram content creation using computer vision and natural language processing</strong>
</p>

<p align="center">
  🎓 <strong>Academic Project</strong> • 🤖 <strong>First GenAI Project</strong> • 📸 <strong>Computer Vision</strong> • 🧠 <strong>NLP Integration</strong>
</p>

---

## 📚 Project Overview

**InstaCaps** is my first Generative AI project developed as part of my academic curriculum. This application demonstrates the practical implementation of AI technologies to solve real-world problems in social media content creation.

### 🎯 **Project Objectives**
- **Learn AI Integration**: Combine computer vision and natural language processing
- **Solve Real Problems**: Address the challenge of creating engaging social media content
- **Apply Course Knowledge**: Implement machine learning concepts in a practical application
- **Demonstrate Innovation**: Show creativity in AI application development

### 🚀 **What It Does**
InstaCaps analyzes uploaded images using AI and generates:
- **Smart Captions**: 3 different caption options in multiple styles
- **Relevant Hashtags**: AI-suggested hashtags for maximum reach
- **Instagram Bios**: Personalized bio generation
- **Image Filters**: Basic image enhancement options
- **Multilingual Support**: Content generation in 5 languages

---

## 🛠️ Technical Implementation

### **AI Models Used**
| Component | Model/Technology | Purpose |
|-----------|-----------------|---------|
| **Image Analysis** | BLIP (Salesforce) | Understanding image content |
| **Text Generation** | Template-based + NLP | Creating Instagram captions |
| **Translation** | MarianMT (Helsinki-NLP) | Multilingual support |
| **Keyword Extraction** | KeyBERT + spaCy | Hashtag generation |

### **Technology Stack**
- **Programming Language**: Python 3.12
- **Web Framework**: Streamlit
- **AI/ML Libraries**: Transformers, Torch, spaCy
- **Image Processing**: PIL (Pillow)
- **Version Control**: Git & GitHub

---

## 📁 Project Structure
InstaCaps/
│
├── app.py # Main application file
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
│
├── utils/ # Core functionality modules
│ ├── image_analysis.py # BLIP image processing
│ ├── caption_generator.py # AI caption generation
│ ├── hashtag_helper.py # Hashtag suggestion engine
│ ├── bio_generator.py # Bio creation system
│ └── filters.py # Image filter functions
│
├── data/ # Data files
│ └── keywords_dataset.json # Hashtag keyword mappings
│
└── pages/ # Additional pages
└── about.py # About page content


---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.12 (recommended for compatibility)
- Git for cloning the repository
- 8GB RAM minimum for AI model processing

### **Installation Steps**

1. **Clone the repository**
https://github.com/nush1729/InstaCaps.git

2. **Create virtual environment**
cd InstaCaps
python3.12 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install dependencies**
pip install --upgrade pip
pip install -r requirements.txt

4. **Download required models**
python -m spacy download en_core_web_sm

5. **Run the application**
streamlit run app.py

6. **Access the application**
- Open your browser and navigate to `http://localhost:8501`
- Upload an image and start generating content!

---

## 💡 Key Features Implemented

### 🎨 **AI-Powered Image Analysis**
- Uses BLIP (Bootstrapping Language-Image Pre-training) model
- Automatically understands image context and objects
- Generates accurate descriptions for any uploaded image

### 📝 **Intelligent Caption Generation**
- **Multiple Styles**: Default, Funny, Motivational, Poetic, Minimalist, Question
- **Template-Based Approach**: Ensures relevant and engaging captions
- **User Customization**: Adjustable creativity levels and length options

### 🌍 **Multilingual Capabilities**
- **5 Languages Supported**: English, Spanish, French, German, Hindi
- **Translation Pipeline**: Uses Helsinki-NLP MarianMT models
- **Cultural Adaptation**: Language-appropriate content generation

### 🔥 **Smart Hashtag Generation**
- **Keyword Extraction**: Uses KeyBERT and spaCy for relevant terms
- **Trending Integration**: Incorporates popular hashtag patterns
- **Customizable Quantity**: 5-20 hashtags per image

---

## 🧪 Testing & Validation

### **Testing Approach**
- **Functionality Testing**: Verified all features work as expected
- **Performance Testing**: Optimized for reasonable processing times
- **User Experience Testing**: Ensured intuitive interface design
- **Cross-Platform Testing**: Tested on different operating systems

### **Sample Results**
- **Image Processing Time**: 30-60 seconds per image
- **Caption Relevance**: High accuracy in context understanding
- **User Satisfaction**: Positive feedback on caption quality

---
## 🎯 Challenges & Solutions

### **Challenge 1: Model Performance**
- **Issue**: Initial models were too slow for real-time use
- **Solution**: Optimized BLIP parameters and image resizing

### **Challenge 2: Caption Relevance**
- **Issue**: Early captions were generic and off-topic
- **Solution**: Implemented template-based generation with AI descriptions

### **Challenge 3: Dependency Management**
- **Issue**: Complex AI model dependencies caused installation issues
- **Solution**: Simplified requirements and provided clear installation guide

---

## 🌟 Learning Outcomes

### **Technical Skills Gained**
- **AI Model Integration**: Learned to combine multiple AI models effectively
- **Computer Vision**: Understanding of image processing and analysis
- **NLP Implementation**: Hands-on experience with text generation
- **Web Development**: Created user-friendly interfaces with Streamlit
- **Version Control**: Proper Git workflow and project organization

### **Soft Skills Developed**
- **Problem Solving**: Overcame technical challenges through research and iteration
- **Project Management**: Organized development timeline and deliverables
- **Documentation**: Created comprehensive project documentation
- **User-Centric Design**: Focused on creating intuitive user experiences

---
## 📊 Project Metrics

### **Code Statistics**
- **Lines of Code**: ~800 lines
- **Files Created**: 8 Python files
- **AI Models Used**: 4 different models
- **Languages Supported**: 5 languages

## 🤝 Acknowledgments

### **Technical Resources**
- **Hugging Face**: For providing open-source AI models
- **Streamlit Community**: For web framework documentation
- **Stack Overflow**: For troubleshooting technical issues
- **GitHub Community**: For code examples and best practices

---

### **Project Links**
- **Live Demo**: None
- **Source Code**: https://github.com/nush1729/InstaCaps.git
- **Documentation**: This README.md file

---

## 📄 Academic Declaration

This project represents original work completed as part of my academic curriculum. All external resources, libraries, and references have been properly acknowledged. The implementation demonstrates understanding of generative AI concepts and their practical application.

**Academic Integrity Statement**: This work is my own and has been completed in accordance with the academic integrity policies of my institution.

---

<div align="center">
<p><strong>🎓 Academic Project - First Generative AI Implementation</strong></p>
<p>© 2025 - Academic Project </p>
</div>