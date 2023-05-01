from pdf2image import convert_from_path
import os
import time

POPPLER_PATH = r"poppler\poppler-0.68.0\bin"


def pdf2jpg(input, output, name, progress, loadtimes):
    pdf_path = input
    save_folder = output

    # Update progress bar (3rd time)
    time.sleep(0.3)
    progress.setValue(loadtimes[2])
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=POPPLER_PATH)

    i = 1
    # Update progress bar (4th time)
    progress.setValue(loadtimes[3])

    for page in pages:
        page.thumbnail((680, 880))
        fname = f"{name}-{i}.jpg"
        page.save(os.path.join(save_folder, fname), "JPEG")
        i += 1
    # Update progress bar (5th time)
    progress.setValue(loadtimes[4])
