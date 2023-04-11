from LinkedList.SLL import *

class LinkedListStack :
    def __init__(self) :
        self.__size = 0
        self.stack = SinglyLinkedList()

    def isEmpty(self):
        return self.size() == 0
    
    def size(self)->int:
        return self.__size
    
    def createNode(self, data):
        return self.stack.createNode(data)
    
    def deleteNode(self, target):
        self.stack.deleteNode(target)
    
    def push(self, NewNode):
        if type(NewNode != self.stack.Node):
            NewNode = self.createNode(NewNode)
        self.stack.insertHead(NewNode)
        self.__size += 1
    
    def pop(self):
        target = self.stack.getNodeByLocation(0)
        self.stack.removeNode(target)
        self.__size -= 1

        return target.data
    
    def top(self):
        return self.stack.getNodeByLocation(0).data
    
    def popAll(self):
        while self.size() != 0:
            target = self.stack.getNodeByLocation(0)
            print(target.data)
            self.stack.removeNode(target)
            self.__size -= 1

if __name__ == "__main__" :
    LLS = LinkedListStack()

    for i in range(5):
        NewNode = LLS.createNode(i)
        LLS.push(NewNode)

    print(LLS.top().data)

    for i in range(3):
        popped = LLS.pop()
        print(popped.data)

    print(LLS.top().data)

    LLS.popAll()
