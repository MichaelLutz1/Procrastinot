import Node
import time

class LinkedList:

    def __init__(self, text):
        self.first = Node.Node(text)
        self.last = self.first

    def insertFirst(self, text):
        newNode = Node.Node(text)
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

    def getFirst(self):
        return self.first
        

    def printList(self):
        curr = self.first
        while(curr != None):
            print(curr.text + " " + curr.timestamp)
            curr = curr.next
        print("\n")