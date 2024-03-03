import Node
import time

class LinkedList:

    def __init__(self, text):
        self.first = Node.Node(text)
        self.last = self.first
        self.length = 1

    def insertFirst(self, text):
        newNode = Node.Node(text)
        newNode.next = self.first
        self.first.prev = newNode
        self.first = newNode

        self.length += 1

    def pop(self):
        if(self.first == self.last):
            self.first = None
            self.last = None
            self.length = 0
            return
        
        self.last = self.last.prev
        self.last.next = None

        self.length -= 1

    def getFirst(self):
        return self.first
    
    def getLast(self):
        return self.last
        

    def printList(self):
        curr = self.first
        while(curr != None):
            print(curr.text + " " + curr.timestamp)
            curr = curr.next
        print("\n")