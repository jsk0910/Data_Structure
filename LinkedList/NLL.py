import time
from time import strftime

class NewLinkedList:
    class Node: # 노드 클래스
        def __init__(self, data=None):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self, data=None): # 생성자, 더미처럼 보이는 head와 tail을 가지고 생성
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self)->int: # 리스트 크기 반환
        return self.__size
    
    def isEmpty(self)->bool: # 리스트가 비어 있는지 확인
        return self.size() == 0
    
    def createNode(self, data): # 노드 생성 -> 노드를 생성만 하고 리스트에 추가하지는 않음
        newNode = self.Node(data)
        return newNode
    
    def deleteNode(self, target): # 노드 제거, 노드를 메모리에서 제거하는 역할, 리스트에서 빼내는 것이 아님
        target.next = None
        target.prev = None

        del target

    def append(self, NewNode): # 리스트의 마지막에 노드 추가
        if self.head == None: # 리스트가 비어 있는 경우
            self.head = NewNode
            self.tail = NewNode
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.prev = self.head
        else:
            current = self.head.prev

            NewNode.next = self.head
            NewNode.prev = self.head.prev

            current.next.prev = NewNode
            current.next = NewNode

            self.tail=NewNode
        self.__size += 1
    
    def insert(self, location, NewNode): # 특정 인덱스의 뒤에 노드를 추가함
        current = self.itemOfIndex(location)

        NewNode.next = current.next
        NewNode.prev = current

        if current.next != None:
            current.next.prev = NewNode
            current.next = NewNode

        self.__size += 1

    def pop(self, location="default", args="default"): # 노드 삭제, location은 인덱스이고 args는 노드를 반환할지, 데이터 값만 반환할지 결정함 
        if location == "default":
            location = self.size() - 1
        current = self.itemOfIndex(location)

        self.remove(current)
        if args == "default":
            data = current.data
            return data
        if args == "node":
            return current
    
    def reverse(self): # 리버스 함수, 새 리스트에 마지막 노드부터 추가하여 반환
        self.result = NewLinkedList() # 반전된 리스트
        for i in reversed(range(self.size())): # 마지막 인덱스부터 시작
            element = self.itemOfIndex(i) # 노드를 받아옴
            
            next = element.next # next와 prev를 서로 바꿈
            element.next = element.prev
            element.prev = next
            self.result.append(element) # 반전 리스트의 앞부터 채워 넣음 -> 자동으로 head와 tail 설정됨
    
        return self.result # 결과 리턴
    
    def reversewithSwap(self): # for문을 이용해 데이터끼리만 교환
        for i in range(self.size()):
            if i == self.size() // 2: # 인덱스 절반까지 오면 데이터가 모두 교환되었으므로 종료
                break
            node1 = self.itemOfIndex(i) # 절반 앞쪽의 노드
            node2 = self.itemOfIndex(self.size()-1-i) # 절반 뒤쪽의 노드
            print(f'{node1.data} <-> {node2.data}')
            temp = node1.data # 교환
            node1.data = node2.data
            node2.data = temp
    
    def reversewithReculsion(self, n=0): # 재귀함수를 이용해 데이터끼리만 교환, 내용은 똑같음
        if n == self.size() // 2: # 인덱스 절반까지 오면 데이터가 모두 교환되었으므로 종료
            return
        node1 = self.itemOfIndex(n) # 현재 노드
        node2 = self.itemOfIndex(self.size()-1-n) # 교환할 목표 노드
        print(f'{node1.data} <-> {node2.data}')
        temp = node1.data # 교환
        node1.data = node2.data
        node2.data = temp
        return self.reversewithReculsion(n+1) # 재귀

    def remove(self, target): # 노드를 리스트에서 꺼내는 함수
        if type(target) != self.Node:
            if type(target) != int:
                print('TypeError')
                return None
            target = self.itemOfIndex(target)
        
        self.__size -= 1

        # problem is here
        if self.head == target:
            current = self.head
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            
            self.deleteNode(current) # 리스트에서 꺼낸 노드를 메모리에서 제거
        else:
            print('Pop')
            temp = target

            target.prev.next = temp.next
            target.next.prev = temp.prev

            self.deleteNode(target) # 리스트에서 꺼낸 노드를 메모리에서 제거

    def clear(self): # clear 함수
        for i in range(self.size()):
            pop = self.pop(0) # 모든 요소를 리스트에서 삭제

        self.head = None # 리스트 초기값으로 초기화
        self.tail = None
        self.__size = 0
    
    def sort(self): # 정렬 함수, 미완성
        pass

    def count(self, target)->int: # count함수
        if target == None:
            print('None Type Error!')
            return
        count = 0
        for i in range(self.size()):
            current = self.itemOfIndex(i)
            if current.data == target: # 데이터가 목표와 같으면 +1, 정수, 실수, 문자열 등 데이터 타입에 관계 없이 처리 가능
                count += 1
        return count

    def itemOfIndex(self, location): # 인덱스로부터 요소를 받아오는 함수(인덱스 번호를 넣으면 해당 노드가 리턴됨)
        current = self.head

        if abs(location) > self.size():
            print("index out of range")
            return None

        if location > 0:
            '''
            while(current != None and (location - 1) >= 0):
                current = current.next
                location -= 1
            '''
            for i in range(location):
                current = current.next
        
        if location < 0: # 인덱스 번호가 음수인 경우 처리
            current = self.tail
            
            '''
            while((location) != -1):
                current = current.prev
                location += 1
            '''
            for i in range(self.size(), location, -1):
                current = current.next
        
        return current

    def indexOfItem(self, target): # 노드 데이터를 넣어서 해당 노드가 몇 번 인덱스에 있는지 반환하는 함수
        current = self.head
        i = 0
        result = []

        while i != self.size():
            if current.data == target:
                result.append(i) # 여러 개인 경우에도 처리 가능
            current = current.next
            i += 1
        
        return result
    
    def __iter__(self):
        return self.NLLIterator(self)

class NLLIterator():
    def __init__(self, data:NewLinkedList):
        self.data = data.tail
        self.next = data.itemOfIndex(0)

    def __next__(self):
        if self.next == self.data:
            raise StopIteration
        else:
            item = self.next.data
            self.next = self.next.next
            return item


if __name__ == "__main__":
    NLL = NewLinkedList() # 리스트 생성
    for i in range(5):
        n = NLL.createNode(i) # 노드 생성
        NLL.append(n) # 리스트에 노드 삽입

    size = NLL.size() # 리스트 크기 가져오기
    for i in range(size):
        print(i, ':', NLL.itemOfIndex(i).data)
    result = NLL.indexOfItem(1) # 데이터 1이 있는 인덱스 불러오기
    print(result)

    '''
    print('-' * 10)
    print('reversed')
    result = NLL.reverse() # 리스트 반전 - reverse()함수 이용
    size = NLL.size()
    for i in range(size):
        print(i, ':', result.itemOfIndex(i).data)
    '''

    # for문 리버스
    start_time = time.time()
    print('-' * 10)
    print('reverse with for-swap')
    NLL.reversewithSwap()
    size = NLL.size()
    print(size // 2)
    for i in range(size):
        print(f'{i} : {NLL.itemOfIndex(i).data}')
    print()
    print(time.time() - start_time)

    # 재귀함수 리버스
    start_time = time.time()
    print('-' * 10)
    print('reverse with reculsion-swap')
    NLL.reversewithReculsion()
    size = NLL.size()
    print(size // 2)
    for i in range(size):
        print(f'{i} : {NLL.itemOfIndex(i).data}')
    print()
    print(time.time() - start_time)


    print('-' * 10)
    node = NLL.createNode(2)
    NLL.append(node)
    count = NLL.count(2) # 데이터 2가 있는 노드의 개수
    print(f'count : {count}')