import json
import random
import os
from keybert import KeyBERT

def load_keywords():
    keywords_path = os.path.join('data', 'keywords_dataset.json')
    if os.path.exists(keywords_path):
        with open(keywords_path) as f:
            return json.load(f)
    else:
        return {
            "food": ["#foodie", "#yum", "#instafood"],
            "travel": ["#wanderlust", "#travelgram", "#vacation"],
            "fitness": ["#fitlife", "#workout", "#gym"],
            "fashion": ["#style", "#ootd", "#fashionista"],
            "nature": ["#naturelover", "#scenery", "#landscape"],
            "art": ["#art", "#creative", "#design"],
            "pets": ["#dog", "#cat", "#pet"],
            "tech": ["#tech", "#technology", "#coding"]
        }

def suggest_hashtags(description, max_hashtags=15, captions=None):
    keywords = load_keywords()
    desc_lower = description.lower()
    hashtags = set()
    # Add hashtags from description keywords
    for topic, tags in keywords.items():
        if topic in desc_lower:
            hashtags.update(tags)
    # Use KeyBERT to extract keywords from captions for more hashtags
    if captions:
        kw_model = KeyBERT()
        for caption in captions:
            keys = kw_model.extract_keywords(caption, top_n=2)
            for k in keys:
                hashtags.add(f"#{k[0].replace(' ', '')}")
    # Add popular hashtags if needed
    popular_tags = [
        "#instagood", "#photooftheday", "#love", "#beautiful", "#happy",
        "#follow", "#like", "#picoftheday", "#instadaily", "#amazing",
        "#fun", "#smile", "#life", "#good", "#cool"
    ]
    while len(hashtags) < max_hashtags:
        hashtags.add(random.choice(popular_tags))
    return list(hashtags)[:max_hashtags]
