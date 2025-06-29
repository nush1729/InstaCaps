import json
import random
import os

def load_keywords():
    keywords_path = os.path.join('data', 'keywords_dataset.json')
    if os.path.exists(keywords_path):
        with open(keywords_path) as f:
            return json.load(f)
    else:
       
        return {
            "food": ["#foodie", "#yum", "#instafood", "#delicious", "#foodporn"],
            "travel": ["#wanderlust", "#travelgram", "#vacation", "#explore", "#adventure"],
            "fitness": ["#fitlife", "#workout", "#gym", "#health", "#fitnessmotivation"],
            "fashion": ["#style", "#ootd", "#fashionista", "#trendy", "#outfit"],
            "nature": ["#naturelover", "#scenery", "#landscape", "#outdoors", "#naturephotography"],
            "art": ["#art", "#creative", "#design", "#artist", "#illustration"],
            "pets": ["#dog", "#cat", "#pet", "#pets", "#animals"],
            "tech": ["#tech", "#technology", "#gadget", "#innovation", "#coding"]
        }

def suggest_hashtags(description, max_hashtags=15):
    keywords = load_keywords()
    desc_lower = description.lower()
    hashtags = set()
    
   
    for topic, tags in keywords.items():
        if topic in desc_lower:
            hashtags.update(tags[:3])  
   
    popular_tags = [
        "#instagood", "#photooftheday", "#love", "#beautiful", "#happy", 
        "#follow", "#like", "#picoftheday", "#instadaily", "#amazing",
        "#fun", "#smile", "#life", "#good", "#cool"
    ]
    
   
    while len(hashtags) < max_hashtags:
        tag = random.choice(popular_tags)
        hashtags.add(tag)
        if len(popular_tags) == 0:
            break
    
    return list(hashtags)[:max_hashtags]
