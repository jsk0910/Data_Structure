class DoublyLinkedList:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def createNode(self, data):
        NewNode = self.Node(data)
        return NewNode
    
    def deleteNode(self, target):
        del target
    
    def appendNode(self, NewNode):
        if self.head.data == None: # 헤드가 없는 경우
            self.head = NewNode # 헤드에 새 노드를 저장한다.
            self.tail = None
            
        else: # 헤드가 있는 경우
            if self.tail == None:
                self.tail = NewNode
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                NewNode.prev = self.tail
                self.tail.next = NewNode
                self.tail = NewNode

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
        if self.head == target: # 헤드가 타겟(지우고자 하는 노드)라면
            self.head = target.next # 헤드의 다음 노드를 헤드로 설정한다.
            if self.head != None: # 이 노드가 None이 아니면
                self.head.prev = None # 이 노드의 이전 노드를 설정하지 않는다.
        
            target.prev = None # 타겟(지워지는 노드)의 이전 노드, 다음 노드 포인터를 없앤다.
            target.next = None
        else:
            temp = target # 타겟 정보를 임시 저장합니다.

            if target.prev != None: # None이 아닌 경우
                target.prev.next = temp.next # 지우는 타겟의 다음 노드를 타겟의 이전 노드의 다음 노드 포인터로 지정합니다.
            
            if target.next != None:
                target.next.prev = temp.prev # 지우는 타겟의 이전 노드를 타겟의 다음 노드의 이전 노드 포인터로 지정합니다.
            
            target.prev = None
            target.next = None

        self.size -= 1 # 사이즈를 1 뺀다
        self.deleteNode(target)
    
    def getNodeByLocation(self, location):
        current = self.head

        if location >= self.size:
            print('location Error')
            return None
        
        if location == 0:
            return current
        else:
            for i in range(location):
                current = current.next
            return current

def PrintNode(node):
    if node.prev == None:
        print("Prev: NULL | ", end="")
    else:
        print(f'Prev: {node.prev.data} | ', end="")
        
    print(f'Current: {node.data} | ', end="")

    if node.next == None:
        print("Next: NULL")
    else:
        print(f'Next: {node.next.data}')

if __name__ == "__main__":      
    DLL = DoublyLinkedList() # 객체 생성

    # 노드 생성 및 추가
    for i in range(3):
        NewNode = DLL.createNode(i+1)
        DLL.appendNode(NewNode)

    # 더블 링크드 리스트 출력
    print('---------------------------------')
    size = DLL.getSize()
    print(size)
    for i in range(size):
        current = DLL.getNodeByLocation(i)
        PrintNode(current)

    # 노드 제거
    current = DLL.getNodeByLocation(1)
    DLL.removeNode(current)

    # 출력
    print('---------------------------------')
    size = DLL.getSize()
    print(size)
    for i in range(size):
        current = DLL.getNodeByLocation(i)
        PrintNode(current)

    # 노드 추가
    NewNode = DLL.createNode("NewNode")
    DLL.insertAfter(0, NewNode)

    # 출력
    print('---------------------------------')
    size = DLL.getSize()
    print(size)
    for i in range(size):
        current = DLL.getNodeByLocation(i)
        PrintNode(current)