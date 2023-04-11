class CircularLinkedList:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None, self.head, self.head)

        self.head.prev = self.tail # 서로 연결해둔다
        self.head.next = self.tail
        
        self.size = 0

    def isEmpty(self)->bool:
        return self.size == 0
    
    def getSize(self)->int:
        return self.size

    def createNode(self, data):
        NewNode = self.Node(data)
        return NewNode
    
    def deleteNode(self, target):
        del target

    def appendNode(self, NewNode):
        if self.head.data == None:
            self.head = NewNode
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head.prev
        else:
            current = self.head.prev

            NewNode.next = self.head
            NewNode.prev = self.head.prev

            current.next.prev = NewNode
            current.next = NewNode

            self.tail=NewNode
        self.size += 1

    def insertAfter(self, location, NewNode):
        current = self.getNodeByLocation(location)

        NewNode.next = current.next
        NewNode.prev = current

        if current.next != None:
            current.next.prev = NewNode
            current.next = NewNode

        self.size += 1

    def removeNode(self, target):
        if self.head == target:
            self.head.prev.next = target.next
            self.head.next.prev = target.prev

            self.head = target.next

            target.prev = None
            target.next = None

            self.deleteNode(target)
        else:
            temp = target

            target.prev.next = temp.next
            target.next.prev = temp.prev

            target.prev = None
            target.next = None

            self.deleteNode(target)
        self.size -= 1
    
    def getNodeByLocation(self, location):
        current = self.head

        while(current != None and (location - 1) >= 0):
            current = current.next
            location -= 1
        
        return current

if __name__ == "__main__":
    cdll = CircularLinkedList()

    for i in range(5):
        NewNode = cdll.createNode(i)
        cdll.appendNode(NewNode)

    size = cdll.getSize()
    for i in range(size):
        node = cdll.getNodeByLocation(i)
        print(f'{i} : {node.prev.data} << {node.data} >> {node.next.data}')

    print('-----------------------------')

    NewNode = cdll.createNode("NewNode")
    cdll.insertAfter(2, NewNode)

    size = cdll.getSize()
    for i in range(size):
        node = cdll.getNodeByLocation(i)
        print(f'{i} : {node.prev.data} << {node.data} >> {node.next.data}')

    print('-----------------------------')

    target = cdll.getNodeByLocation(4)
    cdll.removeNode(target)

    size = cdll.getSize()
    for i in range(size):
        node = cdll.getNodeByLocation(i)
        print(f'{i} : {node.prev.data} << {node.data} >> {node.next.data}')