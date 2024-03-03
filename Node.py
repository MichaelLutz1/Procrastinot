#import timestamp
from datetime import datetime
class Node:
    text = ""
    timestamp = ""
    

    def __init__(self, text):
        self.timeStamp = datetime.now()
        self.text = text

        self.next = None
        self.prev = None


    