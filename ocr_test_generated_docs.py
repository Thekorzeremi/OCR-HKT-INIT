from pdf2image import convert_from_path
import pytesseract
import os

def  convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    return images

def test_ocr():
    for i in range(1, 11):
        pdf_path = f"./generated_docs/{i}doc_.pdf"
        images = convert_pdf_to_image(pdf_path)
        for image in images:
            gray_image = image.convert('L')
            gray_image.save(f"./generated_docs/{i}doc_gray.png")
            text = pytesseract.image_to_string(gray_image)
            print(f"Texte extrait du document {i} :\n{text}\n{'-'*40}")
        

if __name__ == "__main__":
    test_ocr()