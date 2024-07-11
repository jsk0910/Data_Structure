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
            self.setNodeCount(1)
            return 1
        if self.getNodeCount() < i:
            return 0
        current = self.getHead()
        while i-1 > 0:
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
            else:
                break
        prev.setNext(current.getNext())
        current.setNext(None)
        self.setNodeCount(self.getNodeCount() - 1)
    
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
    print(sll.getNodeCount())
    sll.insertAfter(1, Node(2))
    node = sll.searchNode(1)
    print(node.getItem())
    sll.removeNode(sll.getHead().getNext())
    print(sll.getNodeCount())

if __name__ == "__main__":
    test()