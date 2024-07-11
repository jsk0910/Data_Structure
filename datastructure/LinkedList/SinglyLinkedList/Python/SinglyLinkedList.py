from datastructure.LinkedList.BasicLinkedList import *
from datastructure.LinkedList.Node import *

class SinglyLinkedList(BasicLinkedList):
    def __init__(self):
        super().__init__()
    
    def insertAfter(self, i, NewNode:Node)->int:
        if self.isEmpty():
            if i > 0:
                return 0
            self.setHead(NewNode)
            return 1
        print(self.getNodeCount())
        if self.getNodeCount() <= i:
            return 0
        current = self.getHead()
        print(current)
        while i > 0:
            current = current.getNext()
            i -= 1
        if current.getNext() == None:
            current.setNext(NewNode)
        else:
            NewNode.setNext(current.getNext())
            current.setNext(NewNode)
        self.setNodeCount(self.getNodeCount()+1)
        return 1

    def removeNode(self, RemoveNode:Node):
        current = self.getHead()
        prev = None

        while current != None:
            if current != RemoveNode:
                prev = current
                current = current.getNext()
    
    def searchNode(self, Location:int):
        i = 0
        current = self.getHead()
        while i < Location:
            current = current.getNext()
            
            i += 1
        return current

def test():
    sll = SinglyLinkedList()
    sll.insertAfter(0, Node(1))
    sll.insertAfter(1, Node(2))
    node = sll.searchNode(1)
    print(node.getItem())

if __name__ == "__main__":
    test()