from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Global cache
processor = None
model = None

def analyze_image(image):
    global processor, model
    if processor is None or model is None:
        # Use BLIP with optimizations
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        
        # Move to GPU if available
        if torch.cuda.is_available():
            model = model.to("cuda")
    
    # Aggressive image resizing for speed
    max_size = 384  # Reduced from 512 for faster processing
    if max(image.size) > max_size:
        ratio = max_size / max(image.size)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    inputs = processor(image, return_tensors="pt")
    
    # Move inputs to same device as model
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
    
    # Generate with optimized settings
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=25,  # Reduced for speed
            num_beams=2,        # Reduced for speed
            early_stopping=True,
            do_sample=False
        )
    
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
