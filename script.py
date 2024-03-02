from PIL import ImageGrab
import pytesseract
import time
from pynput import mouse
from LinkedList import LinkedList
import Node
import Levenshtein

top_left = bottom_right = None
textType = ""
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

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

previous_text = ""

def screen_to_text(top_left, bottom_right):
    global previous_text
    screenshot = ImageGrab.grab(
        bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    extracted_text = pytesseract.image_to_string(screenshot)
    print("Extracted Text:", extracted_text)
    
    if previous_text:
        similarity = Levenshtein.jaro(extracted_text, previous_text)
        print("Similarity to Previous Text:", similarity)
    
    previous_text = extracted_text

def start():
    global textType
    # while(textType != "1" and textType != "2"):
    #     textType = input("Enter 1 if you are using a local file, and 2 if you are using an online editor\n")
    #     if(textType != "1" and textType != "2"):
    #         print("Invalid input, please try again\n")

    main()


def main():
    with mouse.Listener(
            on_click=on_click,
    ) as listener:
        listener.join()
    while True:
        screen_to_text(top_left, bottom_right)
        time.sleep(5)

    # linkedList = LinkedList("1")
    # linkedList.insertFirst("2")
    # linkedList.insertFirst("3")
    # linkedList.printList()
    # linkedList.pop()
    # linkedList.printList()


start()
