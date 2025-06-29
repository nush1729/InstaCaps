from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = None
model = None

def analyze_image(image):
    global processor, model
    if processor is None or model is None:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    

    max_size = 512
    if max(image.size) > max_size:
        ratio = max_size / max(image.size)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        image = image.resize(new_size)
    
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
