import pytesseract
from PIL import Image
import os

def perform_ocr(image_file_path: str, language: str = "eng") -> tuple:
    pytesseract.pytesseract.tesseract_cmd = '"C:\Program Files\Tesseract-OCR\tesseract.exe"'
    print(f'\nPerforming Optical Character Recognition: {image_file_path}')
    # Check if the image file exists
    if not os.path.exists(image_file_path):
        print(f"Error: Image file '{image_file_path}' not found.")
        return ("Error: Image file not found.", image_file_path)
    
    try:
        with Image.open(image_file_path) as source_image:
            image_text = pytesseract.image_to_string(source_image, lang=language)
        
        print("OCR Done ...")
        return (image_text, image_file_path)
    
    except Exception as e:
        print(f"Error while processing image: {e}")
        return (f"Error while processing image: {e}", image_file_path)
