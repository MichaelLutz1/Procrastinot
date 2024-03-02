from PIL import ImageGrab
import pytesseract
import time


def screen_to_text():
    screenshot = ImageGrab.grab()
    text = pytesseract.image_to_string(screenshot)
    print(text)


def main():
    while True:
        screen_to_text()
        time.sleep(5)


main()
