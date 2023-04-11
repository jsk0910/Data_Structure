class SinglyLinkedList:
    # 노드 클래스
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    
    def __init__(self): # 초기 상태 설정(헤드와 크기를 설정해줍니다)
        self.head = None
        self.size = 0
    
    def getSize(self): # 사이즈 변수의 getter
        return self.size
    
    def isEmpty(self)->bool: # 리스트가 비어있으면 True, 아니면 False입니다.
        return self.size == 0
    
    def createNode(self, data): # 노드를 생성하는 함수로 말그대로 생성만 하고 리스트에 넣지는 않습니다.
        NewNode = self.Node(data)
        return NewNode
    
    def deleteNode(self, target): # 노드를 삭제하는 함수입니다.
        del target
    
    def appendNode(self, NewNode): # 노드를 추가시키는 함수로 리스트의 맨 마지막 부분에 추가시킵니다.
        if self.isEmpty(): # 리스트가 비어있는 경우
            self.head = NewNode # 맨 앞에 추가
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = NewNode
        self.size += 1
    
    def insertHead(self, NewNode): # 헤더부분에 추가합니다.
        if self.isEmpty():
            self.head = NewNode
        else: # 비어있지 않은 경우
            NewNode.next = self.head # 새 노드의 포인터에 원래의 헤더를 추가시키고
            self.head = NewNode #  헤더를 새 노드로 변경해줍니다.
        self.size += 1
    
    def insertAfter(self, location, NewNode): # 특정 위치(인덱스) 다음에 새 노드를 추가시키는 함수입니다.
        Current = self.getNodeByLocation(location)
        if Current != None:
            NewNode.next = Current.next
            Current.next = NewNode
    
    def removeNode(self, target):
        if self.head == target:
            self.head = target.next
            self.deleteNode(target)
        else:
            current = self.head
            while current != None and current.next != target:
                current = current.next
            if current != None:
                current.next = target.next
                self.deleteNode(target)
        self.size -= 1
    
    def getNodeByLocation(self, location):
        if location >= self.size:
            print("location Error")
            return None
        
        if location == 0:
            return self.head
        else:
            current = self.head
            for i in range(0, location):
                current = current.next
            return current

if __name__ == "__main__":
    SLL = SinglyLinkedList() # 객체 생성

    # 노드 만들어서 리스트에 추가하기
    for i in range(5):
        NewNode = SLL.createNode(i+1)
        SLL.appendNode(NewNode)
    size = SLL.getSize() # 리스트 크기 불러오기

    # 리스트 요소 출력
    for i in range(size):
        print(f'{i}번째 : {SLL.getNodeByLocation(i).data}')

    # 헤드에 새 노드 추가
    NewNode = SLL.createNode('NewHead')
    SLL.insertHead(NewNode)
    size = SLL.getSize()

    for i in range(size):
        print(f'{i}번째 : {SLL.getNodeByLocation(i).data}')

    NewNode = SLL.createNode(3500)
    SLL.insertAfter(3, NewNode) # 인덱스 번호 3번 뒤(4번째 뒤가 됨)
    size = SLL.getSize()

    for i in range(size):
        print(f'{i}번째 : {SLL.getNodeByLocation(i).data}')

    # 노드 삭제하기
    target = SLL.getNodeByLocation(3)
    SLL.removeNode(target)
    size = SLL.getSize()

    for i in range(size):
        print(f'{i}번째 : {SLL.getNodeByLocation(i).data}')