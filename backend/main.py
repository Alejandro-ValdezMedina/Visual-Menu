from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pathlib import Path
from ocr import extract_text
from AImages import make_url

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], #react port
    allow_credentials=True, #cookies
    allow_methods=["*"], #allow http methods
    allow_headers=["*"], #allow http headers
)

#health check
@app.get("/")
async def root():
    return {"message": "Visual Menu API is running"}

@app.post("/api/upload-image")
async def upload_menu(file: UploadFile = File(...)):
    """
    Accepts image and extracts text using OCR
    Returns list of menu items
    """
    #create uploads directory
    upload_dir = Path("uploads") 
    upload_dir.mkdir(exist_ok=True)

    #save file path to uploads directory
    file_path = upload_dir / file.filename

    #copy uploaded file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #run OCR
    items = extract_text(str(file_path))

    #return extracted items as JSON
    return {"items": items}

@app.get("/api/generate/{item_name}")
async def generate_image(item_name: str):
    """
    Takes menu item and generates image URL for pollinations AI
    """
    #generate image URL
    image_url = make_url(item_name)

    #return item name and url as JSON
    return {
        "item": item_name,
        "image_url": image_url,
    }