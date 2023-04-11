import sys
sys.path.append('D:\workspace\Python\Data_Structure\\')

from LQueue.Queue import *
from LStack.LinkedListStack import *

def isPalindrome(st:str):
    s = LinkedListStack()
    q = Queue()
    for i in st:
        q.enqueue(i)
        s.push(i)
    
    while (not q.isEmpty()) and s.pop() == q.dequeue():
        {}
    if q.isEmpty():
        return True
    else:
        return False
    
if __name__ == "__main__":
    s = input('Input String: ')
    t = isPalindrome(s)
    print(f'{s} is Palindrome? {t}')