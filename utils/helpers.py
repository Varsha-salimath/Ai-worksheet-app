import base64

def get_base64_image(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def remove_emojis(text):
    """Remove emojis from text for PDF compatibility"""
    return text.encode('latin-1', errors='ignore').decode('latin-1')
