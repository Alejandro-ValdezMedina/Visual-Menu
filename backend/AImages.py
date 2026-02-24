import requests
import base64
import os

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image(image_text: str) -> str:
    """
    Generate image using Hugging Face Inference API
    Args:
        image_text: Menu item text
    Returns:
        Base64 encoded image data URL
    """
    api_key = os.getenv("HF_API_KEY")
    if not api_key:
        raise ValueError("HF_API_KEY environment variable not set. Get a free key at https://huggingface.co/settings/tokens")
    
    prompt = f"{image_text}, food photography, restaurant dish, appetizing, professional, high quality"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": prompt,
    }
    
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Image generation failed: {response.text}")
    
    # Return as base64 data URL for direct use in img src
    image_base64 = base64.b64encode(response.content).decode('utf-8')
    return f"data:image/jpeg;base64,{image_base64}"


# Keep old function name for compatibility but now returns base64 data URL
def make_url(image_text: str) -> str:
    """
    Wrapper for backward compatibility
    """
    return generate_image(image_text)