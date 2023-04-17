from pdf2image import convert_from_path
import os

POPPLER_PATH = r"poppler\poppler-0.68.0\bin"


def pdf2jpg(input, output, name):
    pdf_path = input
    save_folder = output

    pages = convert_from_path(pdf_path=pdf_path, poppler_path=POPPLER_PATH)

    i = 1
    for page in pages:
        page.thumbnail((680, 880))
        fname = f"{name}-{i}.jpg"
        page.save(os.path.join(save_folder, fname), "JPEG")
        i += 1
