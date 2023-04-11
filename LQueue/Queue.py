import sys
sys.path.append('D:\workspace\Python\Data_Structure\\')

from LinkedList.NLL import *

class Queue:
    def __init__(self):
        self.queue = NewLinkedList()

    def __size(self):
        return self.queue.size()
    
    def isEmpty(self):
        return self.__size() == 0
    
    def enqueue(self, data):
        
        if type(data) != self.queue.Node:
            data = self.queue.createNode(data)
        
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def front(self):
        return self.queue.itemOfIndex(0).data
    
if __name__ == "__main__":

    q = Queue()
    print(q.isEmpty())
    for i in range(10):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())
    print(f'front: {q.front()}')