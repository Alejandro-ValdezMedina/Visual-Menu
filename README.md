# Visual-Menu
This is a web app that turns text-based restaurant menus into visual experiences by generating AI food images from menu descriptions. 

# The Problem With Restaurant Menus Today
Most of the restaurant menus today are just text. There are no pictures/images of the dish for the customer to see what they will be ordering. This leaves the customer in a perdicument, either take a risk and order something based off how good it sounds, or search up images of the dish online. There exists a subproblem in the second option, however, in that the customer will have to do this for each menu item. This wastes time and also leaves the customer vulnerable to forget the first searched images.

# What Visual-Menu Does
This web app allows the user to upload a photo of any restaurant menu. The app uses OCR to read the text, seperates dish names from their descriptions, then generates an image for each item. 

# How it Works
The OCR extracts all text from the menu image along with bounding box coordinates. By analyzing text height, the algorithm determines what's a dish name (larger text) versus a description (smaller text). It filters out prices and calorie info, then uses the descriptions to generate food images via Pollinations.ai. The classification works by calculating average text height - anything 1.05x larger than average is treated as a dish name.

# Installation
In one terminal, naviage to the the Visual-Menu folder then:

cd backend

pip install -r requirements.txt

uvicorn main:app --reload

This runs on http://localhost:8000

In a sepeate terminal, navigate to the Visual-Menu folder then:

cd frontend

npm install

npm start

This runs on http://localhost:3000

# Current Limitations
Currently does not work well with multi-column menus. The reason being the algorithm sorts text by vertical postion only. 

Currently only works with English Text.

Blurry images may not work as well with the OCR. 

# Future Improvements
Improve algorithm to work with multi-column menus.

Improve OCR, and allow for different language detection.

# Keywords
FastAPI · Python · React · JavaScript · OCR · EasyOCR · Computer Vision · Image Processing · AI · Image Generation · REST API · Full Stack · Web Development · Machine Learning · Text Extraction · Classification Algorithm · Portfolio Project
