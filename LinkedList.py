import Node
import time

class LinkedList:

    def __init__(self, text, timestamp = time.ctime()):
        self.first = Node.Node(text, timestamp)
        self.last = self.first

    def insertFirst(self, text, timestamp = time.ctime()):
        newNode = Node.Node(text, timestamp)
        newNode.next = self.first
        self.first.prev = newNode
        self.first = newNode

    def pop(self):
        if(self.first == self.last):
            self.first = None
            self.last = None
            return
        
        self.last = self.last.prev
        self.last.next = None

        

    def printList(self):
        curr = self.first
        while(curr != None):
            print(curr.text + " " + curr.timestamp)
            curr = curr.next
        print("\n")