from PIL import ImageGrab
from flask import Flask, render_template, request
import pytesseract
import pygame
import time
import threading
from pynput import mouse
from LinkedList import LinkedList
import Node
import Levenshtein
import Levenshtein

app = Flask(__name__)

top_left = bottom_right = None
textType = ""
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


'''
pygame.init()
clock = pygame.time.Clock()
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
backRect = pygame.Rect(0, 0, screenWidth, screenHeight)
backSurface = pygame.Surface((screenWidth, screenHeight))
backSurface.fill((0, 0, 0))
'''

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
    text = pytesseract.image_to_string(screenshot)
    return text


def start():
    global textType
    # while(textType != "1" and textType != "2"):
    #     textType = input("Enter 1 if you are using a local file, and 2 if you are using an online editor\n")
    #     if(textType != "1" and textType != "2"):
    #         print("Invalid input, please try again\n")

    main()

#If a chain of consecutive nodes has the same text, this is considered inactive time. Otherwise if a node has the same text as another node after having lots of variation in between, changes have been undone and the nodes between can be deleted.
def checkChangeRevert(linkedList, currText):
    currNode = linkedList.getFirst()
    while(currNode != None):
        similarity = Levenshtein.ratio(currText, currNode.text)
        print(similarity)

        currNode = currNode.next


def main():
    # with mouse.Listener(
    #         on_click=on_click,
    # ) as listener:
    #     listener.join()
    while True:
        screen_to_text(top_left, bottom_right)
        time.sleep(5)

    linkedList = LinkedList("Hi")
    linkedList.insertFirst("ihi")
    linkedList.insertFirst("hiiiiiiiiiiiiiii")
    linkedList.printList()
    #linkedList.pop()
    #linkedList.printList()
    checkChangeRevert(linkedList, "hi")

    '''
    running = True
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False

        screen.blit(backSurface, (0, 0))
        font = pygame.font.Font(None, 32)
        text = font.render(screen_to_text(top_left, bottom_right), True, "green")
        textRect = text.get_rect()
        screen.blit(text, textRect)
         
        pygame.display.update()
        clock.tick(30)
    '''
    

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        text_thread = threading.Thread(target=main)
        text_thread.start()
    return render_template('index.html', size=[top_left, bottom_right])

@app.route('/get_text', methods=['GET'])
def get_text():
    if (request.method == 'Get'):
        text_thread = threading.Thread(target=main)
        text_thread.start()
    return screen_to_text(top_left, bottom_right)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2400, debug=True)
