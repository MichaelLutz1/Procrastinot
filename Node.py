import time
class Node:
    text = ""
    timestamp= ""
    

    def __init__(self, text, timestamp = time.ctime()):
        self.text = text
        self.timestamp = timestamp

        self.next = None
        self.prev = None


    