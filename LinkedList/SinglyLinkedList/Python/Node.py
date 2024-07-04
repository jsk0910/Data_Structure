class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.__item = item
        self.__next = next
        self.__prev = prev

    def getItem(self):
        return self.__item
    def getNext(self):
        return self.__next
    def getPrev(self):
        return self.__prev

    def setItem(self, item=None)
        self.__item = item
    def setNext(self, next=None)
        self.__next = next
    def setPrev(self, prev=None)
        self.__prev = prev