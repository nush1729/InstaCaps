from transformers import pipeline
import torch
import random


generator = None

def generate_captions(image_description, creativity=0.85):
    global generator
    if generator is None:
        device = 0 if torch.cuda.is_available() else -1
        generator = pipeline('text-generation', 
                            model='gpt2-medium',
                            device=device,
                            pad_token_id=50256)
    
    
    prompt = f"Write 3 short Instagram captions for: {image_description}\n\n1."
    
    try:
        result = generator(
            prompt,
            max_new_tokens=100,  
            num_return_sequences=1,
            temperature=creativity,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2,
            do_sample=True,
            pad_token_id=50256
        )
        
        generated_text = result[0]['generated_text'].replace(prompt, "").strip()
        

        lines = generated_text.split('\n')
        captions = []
        
        for line in lines[:6]:  
            line = line.strip()
            if line and len(line) > 10 and not line.startswith('2.') and not line.startswith('3.'):
               
                caption = line.replace('1.', '').replace('2.', '').replace('3.', '').strip()
                if caption and len(caption) > 5:
                    captions.append(caption)
                    
   
        if len(captions) < 3:
            fallback_captions = [
                f"Beautiful moment captured! 📸 {random.choice(['✨', '🌟', '💫'])}",
                f"Living my best life! {random.choice(['🌈', '💝', '🎯'])}",
                f"Grateful for this view! {random.choice(['🙏', '❤️', '🌸'])}"
            ]
            captions.extend(fallback_captions[:3-len(captions)])
            
        return captions[:3]
        
    except Exception as e:
        return [
            "Amazing view! 📸✨",
            "Living the dream! 🌟💫",
            "Grateful for moments like these! 🙏❤️"
        ]
