import pytesseract
from PIL import Image
import time

while True:
    start_time = time.time()

    image_pil = Image.open('text.jpg').convert('L')
    custom_config = r'--psm 6 -c tessedit_do_invert=0'
    extracted_text = pytesseract.image_to_string(image_pil, lang='rus', config=custom_config)

    print(extracted_text)
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Скрипт выполнен за {execution_time} секунд")
