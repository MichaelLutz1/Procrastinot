from PIL import ImageGrab, Image
from flask import Flask, render_template, request
import pytesseract
import time
import threading
from pynput import mouse
from LinkedList import LinkedList
import Node
import Levenshtein
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

app = Flask(__name__)
stop_flag = threading.Event()
text_thread = None
top_left = (0, 0)
bottom_right = (1, 1)
textType = ""
sampleRate = 5
inactivityTimes = []
isProcrastinating = False

linkedList = LinkedList("")
linkedList.pop() #Pop the default empty node

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
    percentOfLength = len(currText) * .05
    while(currNode != None):
        #if(len(currNode.text) >= len(currText) - percentOfLength and len(currNode.text) <= len(currText) + percentOfLength): #Check the similarity between the texts if it is within +-5% of the current length
        similarity = Levenshtein.ratio(currText, currNode.text)
        print(similarity)
        currNode = currNode.next

def countConsecutiveDuplicates(linkedList):
    samplesUntilInactive = 5
    currNode = linkedList.getFirst().next
    currText = linkedList.getFirst().text
    if(currNode == None):
        return
    count = 0

    if(Levenshtein.ratio(currText, currNode.text) == 1.0): #Only count consecutive duplicates once a difference has been found, in order to determine the inativity interval (inactivity stops once there is a difference)
        return 

    currText = currNode.text
    currNode = currNode.next #itterate the node and text to start comparing the duplicate texts after the first difference
    while(currNode != None and currNode.next != None and Levenshtein.ratio(currText, currNode.text) == 1.0): #Find how many conecutive duplicates there are, and do go to the first node that has that text (the start of the inactivity period)
        count += 1
        currNode = currNode.next

    if(count >= samplesUntilInactive):
        currNode = currNode.prev
        inactivityTimes.append((currNode, linkedList.getFirst())) #Append a tuple into the array of inactivity periods, with the first node having the start of the inactivity period and the second node having the end.
    

def printInactivityIntervals(linkedList):
    for i in range(len(inactivityTimes)):
        print(inactivityTimes[i][1].timeStamp - inactivityTimes[i][0].timeStamp)
    print("\n")

def getXAxis(linkedList):
    if(linkedList.length <= 1):
        return []
    
    x = []
    currNode = linkedList.getLast()
    currNode = currNode.prev

    while(currNode != None):
        #x.append((1.0 * currNode.timeStamp.minute) + round((currNode.timeStamp.second / 60), 3)) #X axis for graph is floats in minutes, with seconds as a decimal
        #x.append(1.0 * currNode.timeStamp.hour + (currNode.timeStamp.minute / 100)) #Hours.minutes
        x.append(currNode.timeStamp)
        currNode = currNode.prev

    return x

def getYAxis(linkedList):
    if(linkedList.length <= 1):
        return []

    y = []
    currNode = linkedList.getLast()
    currNode = currNode.prev

    while(currNode != None):
        y.append(1 - (Levenshtein.ratio(currNode.text, currNode.next.text)))
        currNode = currNode.prev

    return y

def getGraph(linkedList):
    x = getXAxis(linkedList)
    y = getYAxis(linkedList)

    dates = matplotlib.dates.date2num(x)
    plt.plot_date(dates, y)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Timestamp")
    plt.ylabel("Productivity Level")
    
    plt.savefig("graph.png", bbox_inches='tight')

    #####plt.show()
    ######plt.close()

    #Uncomment to view image
    #im = Image.open("graph.png")
    #im.show()



def main():
    global linkedList
    global isProcrastinating
    linkedList = LinkedList(screen_to_text(top_left, bottom_right))
    while not stop_flag.is_set():
        currText = screen_to_text(top_left, bottom_right)
        checkChangeRevert(linkedList, currText)
        linkedList.insertFirst(currText)

        tempIntervalArrayLength = len(inactivityTimes)
        countConsecutiveDuplicates(linkedList)
        if(len(inactivityTimes) > tempIntervalArrayLength):
            isProcrastinating = True

        getGraph(linkedList)

        ##########################
        print("\n")######
        if(len(inactivityTimes) > 0):######
            printInactivityIntervals(linkedList)####
        

        #######################
        
        temp2 = ""
        temp = getXAxis(linkedList)
        for i in range(len(temp)):
            temp2 += str(temp[i]) + " "
        print(temp2 + "\n")
        
        ############################


        time.sleep(sampleRate)

    '''
    linkedList = LinkedList("Hi")
    linkedList.insertFirst("ihi")
    linkedList.insertFirst("hiiiiiiiiiiiiiii")
    linkedList.printList()
    # linkedList.pop()
    # linkedList.printList()
    checkChangeRevert(linkedList, "hi")
    '''
   
#start() ####


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
