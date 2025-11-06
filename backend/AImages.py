from urllib.parse import quote

def make_url(image_text: str) -> str:
    """
    Generate image URL
    Args:
        image_text: Menu item text
    Returns:
        A URL.
    """
    prompt = f"{image_text}, food photography, restaurant dish, appetizing, professional"
    encoded_prompt = quote(prompt) #URL encode
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    return url