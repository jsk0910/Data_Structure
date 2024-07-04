from .LinkedList import *
from Node import *

class SinglyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def insertAfter(self, NewNode:Node):
        pass

    def removeNode(self, RemoveNode:Node):
        pass
    
    def searchNode(self, Location:int):
        pass

def test():
    SinglyLinkedList()

if __name__ == "__main__":
    test()