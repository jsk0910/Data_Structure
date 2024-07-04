from Node import *

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def getHead(self):
        return self.__head
    
    def getNodeCount(self):
        return self.__count