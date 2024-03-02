from PIL import ImageGrab
import pytesseract
import time
from pynput import mouse

top_left = bottom_right = None


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


def screen_to_text(top_left, bottom_right):
    screenshot = ImageGrab.grab(
        bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    text = pytesseract.image_to_string(screenshot)
    print(text)


def main():
    with mouse.Listener(
            on_click=on_click,
    ) as listener:
        listener.join()
    while True:
        screen_to_text(top_left, bottom_right)
        time.sleep(5)


main()
