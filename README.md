# OCR-HKT-INIT

This project demonstrates Optical Character Recognition (OCR) using Tesseract. It provides scripts to extract text from PDF invoices and generate synthetic documents for testing.

## Setup Instructions

1. **Install Required Python Packages:**
    - `faker`: For generating fake data.
    - `fpdf`: For creating PDF files.
    - `pdf2image`: For converting PDFs to images.
    - `pytesseract`: For performing OCR.

    Install these packages using pip:
    ```
    pip install faker fpdf pdf2image pytesseract
    ```

2. **Install Tesseract:**
    - Tesseract must be installed on your host machine. Refer to [Tesseract documentation](https://github.com/tesseract-ocr/tesseract) for installation instructions.

## Usage

- **Extracting Text from Invoices:**
  - Place your invoice PDFs in the `/docs` directory.
  - Rename them as `invoice{nb}.pdf` (e.g., `invoice1.pdf`, `invoice2.pdf`, ...).
  - Run `ocr_test.py` to extract text from these invoices.

- **Generating Test Data:**
  - If you do not have invoice PDFs, you can generate synthetic documents:
     - Run `docs_generator.py` to create fake PDF documents in `/generated_docs/`.
     - Run `ocr_test_generated_docs.py` to perform OCR on these generated documents.

## Project Structure

- `/docs`: Directory for invoice PDFs and extracted text.
- `/generated_docs`: Directory for generated test PDFs.
- `ocr_test.py`: Script for OCR on real invoices.
- `ocr_test_generated_docs.py`: Script for OCR on generated documents.
- `docs_generator.py`: Script for generating fake PDF documents.

## Author
Thekorzeremi 
I'm not responsible for the quality of the generated documents, they are just for testing purposes. Educational use only.