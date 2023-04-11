from LinkedListStack import *

def e(p:str):
    stack = LinkedListStack()
    isDigitP = False

    for i in range(len(p)):
        ch = p[i]
        if ch.isdigit():
            if isDigitP:
                tmp = stack.pop()
                tmp = 10 * tmp + (ord(ch) - ord('0'))
                stack.push(tmp)
            else:
                stack.push(ord(ch) - ord('0'))
                isDigitP = True
        elif isOper(ch):
            stack.push(operation(stack.pop(), stack.pop(), ch))
            isDigitP = False
        else:
            isDigitP = False
    return stack.pop()

def isOper(ch) -> bool:
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/')

def operation(opr2:int, opr1:int, ch) -> int:
    return {'+' : opr1 + opr2, '-' : opr1 - opr2, '*': opr1 * opr2, '/' : opr1 // opr2}[ch]

if __name__ == "__main__":
    input = input()
    answer = e(input)
    print(answer)