from PIL import Image, ImageGrab
import pygame
import pynput
import pytesseract
from pynput.mouse import Button, Controller

#pygame.init()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

clock = pygame.time.Clock()
screenWidth = 1000
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
backRect = pygame.Rect(0, 0, screenWidth, screenHeight)

tempImg = pygame.image.load("screenshot.png")
tempImg = pygame.transform.scale(tempImg, (screenWidth, screenHeight))

topLeft = (-100, -100)
bottomRight = (-100, -100)

textType = ""

def start():
    global textType, topLeft, bottomRight
    while(textType != "1" and textType != "2"):
        textType = input("Enter 1 if you are using a local file, and 2 if you are using an online editor\n")
        if(textType != "1" and textType != "2"):
            print("Invalid input, please try again\n")

    clickCount = 0
    while(clickCount != 2):
        #mouse = Controller()
        def on_click(x, y, button, pressed):
            if(clickCount == 0):
                topLeft = (x, y)
                clickCount += 1
            else:
                bottomRight = (x, y)
                clickCount += 1
            if not pressed:
                # Stop listener
                return False
        with pynput.mouse.Listener(on_click=on_click) as listener: listener.join()

    print(topLeft)
    print(bottomRight)

start()

    


try:
    while(False):
        currIndex = 0
        x = []
        # Take a screenshot of the entire screen
        screenshot = ImageGrab.grab()

        # Save the screenshot to a file
        screenshot.save("screenshot.png")

        # Display the screenshot
        #screenshot.show()

        imagePath = "screenshot.png"
        image = Image.open(imagePath)
        extractedText = pytesseract.image_to_string(image)
        x.append(extractedText)

        #screen.blit(tempImg, (0, 0))
        #pygame.display.update()
        #clock.tick(30)
except KeyboardInterrupt:
    pass
