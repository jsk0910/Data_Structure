import sys
sys.path.append('D:\workspace\Python\Data_Structure\\')

from LStack.LinkedListStack import *

if __name__ == "__main__":
    s = input().split(' ')
    stack = LinkedListStack()
    result = 0

    for i in s:
        if i == '+':
            pop2, pop1 = stack.pop(), stack.pop()
            result = int(pop1) + int(pop2)
            print(result)
            stack.push(result)
            continue
        elif i == '-':
            pop2, pop1 = stack.pop(), stack.pop()
            result = int(pop1) - int(pop2)
            print(result)
            stack.push(result)
            continue
        elif i == '*':
            pop2, pop1 = stack.pop(), stack.pop()
            result = int(pop1) * int(pop2)
            print(result)
            stack.push(result)
            continue
        elif i == '/':
            pop2, pop1 = stack.pop(), stack.pop()
            result = int(pop1) // int(pop2)
            print(result)
            stack.push(result)
            continue
        print(i)
        stack.push(i)

    print(stack.pop())
