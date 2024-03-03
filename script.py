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
stop_flag = threading.Event()
text_thread = None
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


previous_text = ""


def screen_to_text(top_left, bottom_right):
    if not top_left and not bottom_right:
        screenshot = ImageGrab.grab()
    else:
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

# If a chain of consecutive nodes has the same text, this is considered inactive time. Otherwise if a node has the same text as another node after having lots of variation in between, changes have been undone and the nodes between can be deleted.


def checkChangeRevert(linkedList, currText):
    currNode = linkedList.getFirst()
    fivePercentLength = len(currText) * .05
    while(currNode != None):
        if(len(currNode.text) >= len(currText) - fivePercentLength and len(currNode.text) <= len(currText) + fivePercentLength): #Check the similarity between the texts if it is within +-5% of the current length
            similarity = Levenshtein.ratio(currText, currNode.text)
            print(similarity)
        currNode = currNode.next

def countConsecutiveSames(linkedList):
    currNode = linkedList.getFirst()


def main():

    linkedList = LinkedList(screen_to_text(top_left, bottom_right))
    while not stop_flag.is_set():
        currText = screen_to_text(top_left, bottom_right)
        checkChangeRevert(linkedList, currText)
        linkedList.insertFirst(currText)
        #print(currText)
        time.sleep(5)

    linkedList = LinkedList("Hi")
    linkedList.insertFirst("ihi")
    linkedList.insertFirst("hiiiiiiiiiiiiiii")
    linkedList.printList()
    # linkedList.pop()
    # linkedList.printList()
    checkChangeRevert(linkedList, "hi")

    '''
    running = True
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False

        screen.blit(backSurface, (0, 0))
        font = pygame.font.Font(None, 32)
        text = font.render(screen_to_text(
            top_left, bottom_right), True, "green")
        textRect = text.get_rect()
        screen.blit(text, textRect)

        pygame.display.update()
        clock.tick(30)
    '''  # start() ####


@app.route('/', methods=['GET', 'POST'])
def home():
    if text_thread and text_thread.is_alive():
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/get_text', methods=['GET'])
def get_text():
    if (request.method == 'GET'):
        active = request.args.get('active')
        global text_thread
        if (active == "true"):
            text_thread = threading.Thread(target=main)
            text_thread.start()
            return "started"
        else:
            if (text_thread and text_thread.is_alive()):
                global stop_flag
                stop_flag.set()
                text_thread.join()
            return "stopped"
    return render_template('index.html')


@app.route('/resize', methods=['GET'])
def get_size():
    print("Resizing")
    global top_left, bottom_right
    top_left = None
    bottom_right = None
    with mouse.Listener(
            on_click=on_click,
    ) as listener:
        listener.join()
    print("Top left:", top_left, "Bottom right:", bottom_right)
    return 'resized'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2400, debug=True)
