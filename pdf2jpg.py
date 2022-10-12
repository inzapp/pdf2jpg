import os
from glob import glob
from pdf2image import convert_from_path

for path in glob('*.pdf'):
    raw_name = os.path.basename(path)[:-4]
    pdf_pages = convert_from_path(path)
    for i, pdf_page in enumerate(pdf_pages):
        pdf_page.save(f'{raw_name}_{i}.jpg', 'JPEG')

