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
    text_data = []
    for detection in results:
        #extract text section and remove whitespace
        text = detection[1].strip()
        bounding_box = detection[0]
        y_coords = [point[1] for point in bounding_box]  #non straight text
        text_height = max(y_coords) - min(y_coords) 
        #text_height = bounding_box[2][1] - bounding_box[0][1] #straight text
        y_position = bounding_box[0][1]
        #skip very short text
        if len(text) <= 2:
            continue
        #skip calorie text
        if "Cal" in text or "cal" in text or "kcal" in text or "Kcal" in text:
            continue
        #skip price text
        if "$" in text or text.replace(".", "").replace("-", "").isdigit():
            continue
        text_data.append({
            "text": text,
            "y_position": y_position,
            "text_height": text_height,
        })

    #sort text data by y_position
    text_data = sorted(text_data, key=lambda x: x["y_position"])

    heights = [item["text_height"] for item in text_data]
    average_height = sum(heights) / len(heights)
    print(f"average height: {average_height}")
    print(f"Threshold (avg * 1.05): {average_height * 1.05}")

    menu_items = []
    current_item = None
    current_descriptions = []

    for item in text_data:
        text = item["text"]
        height = item["text_height"]
        print(f"Text: '{text[:30]}...' | Height: {height} | IsName: {height > average_height * 1.3}")
        if height > average_height * 1.05:
            if current_item is not None:
                menu_items.append({
                    "name": current_item,
                    "description": " ".join(current_descriptions),
                })
            current_item = text
            current_descriptions = []
        elif current_item:
            current_descriptions.append(text)
    if current_item is not None:
        menu_items.append({
            "name": current_item,
            "description": " ".join(current_descriptions),
        })
    return menu_items

    #need to test with multiple items