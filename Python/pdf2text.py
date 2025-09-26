import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# For Windows: specify the path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your PDF
pdf_path = 'C:/Users/Admin/Desktop/bhaktamar_stotra_002453_hr6.pdf'

# Convert PDF pages to images
images = convert_from_path(pdf_path, dpi=300)

# Run OCR on each image
full_text = ""
for img in images:
    text = pytesseract.image_to_string(img, lang='hin')
    full_text += text + "\n\n"

# Save output to a text file
with open('bhaktamar_text.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("OCR completed and text saved.")
