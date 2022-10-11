import os
from pdf2image import convert_from_path

file_name = 'pdf.pdf'
basename = os.path.basename(file_name)
pdf_pages = convert_from_path(file_name)

for i, pdf_page in enumerate(pdf_pages):
	pdf_page.save(f'{basename}_{i}.jpg', 'JPEG')

