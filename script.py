from PIL import ImageGrab
from flask import Flask, render_template, request
import pytesseract
import time
import threading
from pynput import mouse
from LinkedList import LinkedList
import Node

app = Flask(__name__)

top_left = bottom_right = None
textType = ""
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def on_click(x, y, button, pressed):
    global top_left, bottom_right
    if pressed and not top_left:
        top_left = (int(x), int(y))
        print('Top left:', top_left)
    elif pressed and top_left and not bottom_right:
        bottom_right = (int(x), int(y))
        print('Bottom right:', bottom_right)
        return False
    if not pressed:
        return True


def screen_to_text(top_left=None, bottom_right=None):
    screenshot = ImageGrab.grab()
    # bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    text = pytesseract.image_to_string(screenshot)
    print(text)


def start():
    global textType
    while (textType != "1" and textType != "2"):
        textType = input(
            "Enter 1 if you are using a local file, and 2 if you are using an online editor\n")
        if (textType != "1" and textType != "2"):
            print("Invalid input, please try again\n")

    main()


def main():
    while True:
        screen_to_text(top_left, bottom_right)
        time.sleep(5)

    # linkedList = LinkedList("1")
    # linkedList.insertFirst("2")
    # linkedList.insertFirst("3")
    # linkedList.printList()
    # linkedList.pop()
    # linkedList.printList()


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        text_thread = threading.Thread(target=main)
        text_thread.start()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2400, debug=True)
