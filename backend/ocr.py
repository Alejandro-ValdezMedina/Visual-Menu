import easyocr

reader = easyocr.Reader(['en'], gpu=False) #gpu false for phone use

def extract_text(image_path: str) -> list[str]:
    """
    Extracts text from an image using EasyOCR.
    Args:
        image_path: The path to the image to extract text from.
    Returns:
        A list of strings, each representing a menu item.
    """
    #run ocr and return list of detections
    results = reader.readtext(image_path)
    filtered_results = []
    for detection in results:
        #extract text section and remove whitespace
        text = detection[1].strip()
        #skip very short text
        if len(text) <= 2:
            continue
        #skip calorie text
        if "Cal" in text or "cal" in text or "kcal" in text or "Kcal" in text:
            continue
        #skip price text
        if "$" in text or text.replace(".", "").replace("-", "").isdigit():
            continue
        filtered_results.append(text)

    return filtered_results