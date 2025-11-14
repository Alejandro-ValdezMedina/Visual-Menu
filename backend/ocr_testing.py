from ocr import extract_text

items = extract_text("two item.png") # file path
print("items: ")
for item in items:
    print(f"- {item}")