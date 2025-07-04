from PIL import Image, ImageEnhance, ImageOps

def apply_filter(image, filter_name):
    if filter_name == "Grayscale":
        return ImageOps.grayscale(image)
    elif filter_name == "Sepia":
        sepia = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0C080')
        return sepia
    elif filter_name == "Brighten":
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(1.5)
    elif filter_name == "Contrast":
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(1.5)
    else:
        return image
