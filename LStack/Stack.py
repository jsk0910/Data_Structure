class Stack:
    def __init__(self):
        self.size = 0
        self.stack = []
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def destroyStack(self):

        while(self.isEmpty() != True):
            Popped = self.Pop()
            print(f'Popped: {Popped}')
        
        del self
    
    
    def Push(self, data):
        self.stack.append(data)
        self.size += 1

    def Pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def Top(self):
        return self.stack[-1]
    
if __name__ == "__main__":
    stack = Stack()

    for i in range(10):
        stack.Push(i)
    
    print(stack.stack)

    print(stack.Top())

    for i in range(3):
        print(stack.Pop())

    print(stack.stack)

    print(stack.Top())

    stack.destroyStack()