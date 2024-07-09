from .LinkedList import *
from Node import *

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def insertAfter(self, i, NewNode:Node)->int:
        if self.isEmpty():
            return 0
        current = self.getHead()
        while i > 0:
            current = current.getNext()
            i -= 1
        if current.getNext() == None:
            current.setNext(NewNode)
        else:
            NewNode.setNext(current.getNext())
            current.setNext(NewNode)
        return 1

    def removeNode(self, RemoveNode:Node):
        pass
    
    def searchNode(self, Location:int):
        i = 0
        current = self.getHead()
        while i < Location:
            current = current.getNext()
            i += 1
        return current

def test():
    SinglyLinkedList()

if __name__ == "__main__":
    test()