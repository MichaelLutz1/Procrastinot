import timestamp
class Node:
    text = ""
    timestamp = ""
    

    def __init__(self, text):
        self.text = text
        self.timeStamp = timestamp.TimeStamp()

        self.next = None
        self.prev = None


    