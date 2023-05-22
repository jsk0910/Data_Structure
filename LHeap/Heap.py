import math

class LHeap:
    def __init__(self, option="max"): # option은 max Heap / min Heap을 결정
        self.option = option
        self.heap = []

    def isEmpty(self):
        return self.heap == []
    
    def size(self):
        return len(self.heap)
    
    def root(self):
        return self.heap[0]
    
    def level(self) -> int:
        if self.isEmpty():
            print('힙에 요소가 없습니다.')
            return
        
        level = math.sqrt(self.size()+1) // 1 + 1 # 제곱근한 값을 1로 나눠서 소수점 부분을 없앰
        return int(level)
    
    def buildHeap(self): # 현재 상태의 힙을 재배치
        if self.option == "max":
            for i in range((len(self.heap) - 2) // 2, -1, -1):
                self.percolateDownMax(i)
        if self.option == "min":
            for i in range((len(self.heap) - 2) // 2, -1, -1):
                self.percolateDownMin(i)

    def insert(self, x):
        if type(x) == list:
            self.heap.extend(x)
        else:
            self.heap.append(x)
        self.percolateUp(len(self.heap) - 1)

    def percolateUp(self, index):
        parent = (index - 1) // 2
        if self.option == "max":
            if index > 0 and self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.percolateUp(parent)

        if self.option == "min":
            if index > 0 and self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.percolateUp(parent)

    def percolateDown(self):
        if self.option == "max":
            self.percolateDownMax(0)
        elif self.option == "min":
            self.percolateDownMin(0)

    def percolateDownMax(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left <= len(self.heap) - 1: # 경계 조건
            if (right <= len(self.heap) - 1 and self.heap[left] < self.heap[right]): # 오른쪽 값이 더 크면 비교할 인덱스를 바꿈
                left = right
            if self.heap[index] < self.heap[left]: # 자식 노드가 더 크면
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index] # 서로 바꾸기
                self.percolateDownMax(left) # 재귀 호출, 바꾼 노드(자식 노드)의 인덱스를 넣음

    def percolateDownMin(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        if left <= len(self.heap) - 1:
            if (right <= len(self.heap) - 1 and self.heap[left] > self.heap[right]):
                left = right
            if self.heap[index] > self.heap[left]:
                self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                self.percolateDownMin(left)

    def deleteRoot(self):
        if not self.isEmpty():
            root = self.heap.pop(0)
            self.heap[0] = self.heap.pop()
            self.percolateDown()
            return root
        else:
            return None

    def printHeap(self):
        index = 0
        for i in range(self.level()):
            print(f'Level {i}: ', end="")
            for j in range(1*(2**i)):
                if index > self.size() - 1:
                    print()
                    return
                print(f'{self.heap[index]} ', end="")
                index += 1
            print()

if __name__ == "__main__":
    h = LHeap(option="min")
    h.heap = [9, 4, 5, 10, 3, 6, 8, 9]
    h.buildHeap()
    print(h.level())
    h.printHeap()
    print(h.deleteRoot())
    h.printHeap()