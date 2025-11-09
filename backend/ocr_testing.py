from ocr import extract_text

items = extract_text("menu.png") # file path
print("items: ")
for item in items:
    print(f"- {item}")