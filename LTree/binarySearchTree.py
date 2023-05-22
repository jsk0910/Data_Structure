class TreeNode:
    def __init__(self, data, left, right):
        self.item = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None
    
    def getRoot(self):
        return self.__root
    # 검색
    def search(self,x) -> TreeNode:
        return self.__searchItem(self.__root, x)
    
    def __searchItem(self, tNode:TreeNode, x) -> TreeNode:
        if tNode == None:
            return None
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    # 삽입
    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)
    
    # 현 위치에 노드가 없으면 그 자리에 노드를 삽입한다.
    # 노드 데이터가 같은 경우에는 삽입하지 않는다.
    # 새 노드의 데이터가 현 위치의 데이터보다 작으면 왼쪽, 크면 오른쪽으로 보낸다.
    def __insertItem(self, tNode:TreeNode, newItem):
        if tNode == None:
            tNode = TreeNode(newItem, None, None)
        elif newItem == tNode.item:
            return None
        elif newItem < tNode.item:
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode
    
    # 삭제
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
        if tNode == None:
            return None
        elif x == tNode.item:
            tNode = self.__deleteNode(tNode)
        elif x < tNode.item:
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode
    
    def __deleteNode(self, tNode:TreeNode) -> TreeNode:
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left == None:
            return tNode.right
        elif tNode.right == None:
            return tNode.left
        else:
            (returnItem, returnNode) = self.__deleteMinItem(tNode.right)

            tNode.item = returnItem
            tNode.right = returnNode
            return tNode
    
    def __deleteMinItem(self, tNode:TreeNode) -> tuple:
        if tNode.left == None:
            return (tNode.item, tNode.right)
        else:
            (returnItem, returnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = returnNode

            return (returnItem, tNode)
        
    # 전위 순회
    def preOrder(self, tNode:TreeNode, x="root"):
        #x.append(a)
        if x == "root":
            tNode = self.__root
        if x == "left":
            print(f"left : ", end="")
        if x == "right":
            print(f"right : ", end="")
        if tNode != None:
            print(tNode.item)
            self.preOrder(tNode.left, "left")
            self.preOrder(tNode.right, "right")
        

bst1 = BinarySearchTree()

bst1.insert(10)
bst1.insert(5)
bst1.insert(20)
bst1.insert(80)
bst1.insert(90)
#bst1.insert(7750)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.search(30)
#bst1.delete(7750)

print('preOrder')
bst1.preOrder("root", "root")
#print(x)
print()