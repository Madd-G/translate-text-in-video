import pytesseract
import cv2
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def video_konversi(video_file):
    video_text = cv2.VideoCapture(video_file)
    status, gambar = video_text.read()
    imgH, imgW, _ = gambar.shape
    video_baru = cv2.VideoWriter("oldVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (imgW, imgH))
    while status:
        boxes = pytesseract.image_to_data(gambar)
        translator = Translator()

        for i, b in enumerate(boxes.splitlines()):
            if i != 0:
                b = b.split()
                if len(b) == 12:
                    out = translator.translate(b[11], dest="id").text

                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(gambar, (x, y), (w + x, h + y), (0, 0, 255), 2)
                    cv2.putText(gambar, out, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        video_baru.write(gambar)

        status, gambar = video_text.read()

    # video_baru.release()


video_konversi('newVideo.mp4')
