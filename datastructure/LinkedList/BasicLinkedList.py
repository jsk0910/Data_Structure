from datastructure.LinkedList.Node import *

class BasicLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def getHead(self)->Node:
        return self.__head
    
    def getNodeCount(self)->int:
        return self.__count
    
    def setHead(self, NewNode: Node):
        self.__haed = NewNode
    
    def setNodeCount(self, i):
        self.__count = i
    
    def isEmpty(self):
        return self.getNodeCount() == 0
    
    def insertAfter(self, i, NewNode):
        pass

    def removeNode(self, RemoveNode):
        pass

    def searchNode(self, Location):
        pass
    
    def append(self, item):
        pass

    def pop(self):
        pass