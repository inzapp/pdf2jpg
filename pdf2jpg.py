import os
from glob import glob
from pdf2image import convert_from_path

for path in glob('*.pdf'):
    raw_name = os.path.basename(path)[:-4]
    print(f'start converting {path}')
    pdf_pages = convert_from_path(path)
    print(f'conversion success')
    for i in range(len(pdf_pages)):
        img_path = f'{raw_name}_{i}.jpg'
        pdf_pages[i].save(img_path, 'JPEG')
        print(f'save image => {img_path}')
    print()

