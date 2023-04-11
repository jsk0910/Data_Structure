import SLL
import DLL
import CDLL

while True:
    print('-' * 25)
    print('----- 자료구조 선택 -----')
    print('0. 종료')
    print('1. 링크드 리스트')
    print('-' * 25)
    selected = int(input('입력: '))
    if selected == 0:
        break
    elif selected == 1:
        while True:
            print('-' * 25)
            print('0. 뒤로가기')
            print('1. 싱글 링크드 리스트')
            print('2. 더블 링크드 리스트')
            print('3. 환형 링크드 리스트')
            print('-' * 25)
            selected = int(input('입력: '))
            if selected == 0:
                break
            elif selected == 1:
                list1 = SLL.SinglyLinkedList()
                print('-' * 25)
                print('생성 완료 : 싱글 링크드 리스트')

                while True:
                    print('0. 뒤로가기')
                    print('1. 노드 생성 및 삽입(append)')
                    print('2. 노드 생성 및 삽입(insert)')
                    print('3. 노드 삭제')
                    print('4. 노드 탐색')
                    print('5. 리스트 전체 출력')
                    print('-' * 25)

                    selected = int(input('입력: '))
                    
                    if selected == 0:
                        del list1
                        print('삭제 완료 : 싱글 링크드 리스트')
                        break
                    elif selected == 1:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        list1.appendNode(node)
                    elif selected == 2:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        loc = int(input('삽입할 위치: '))
                        list1.insertAfter(loc, node)
                    elif selected == 3:
                        loc = int(input('삭제할 노드 위치: '))
                        node = list1.getNodeByLocation(loc)
                        list1.removeNode(node)
                    elif selected == 4:
                        loc = int(input("찾을 위치: "))
                        node = list1.getNodeByLocation(loc)
                        print(f'{loc}위치 : {node.data}')
                    elif selected == 5:
                        size = list1.getSize()
                        for i in range(size):
                            node = list1.getNodeByLocation(i)
                            if i == 0:
                                print(f'Head : {node.data}', end="")
                            elif i == size-1:
                                print(f'Tail : {node.data}')
                                break
                            else:
                                print(f'{node.data}', end="")
                            print(f' -> ', end="")
                    print('-' * 25)
            elif selected == 2:
                list1 = DLL.DoublyLinkedList()
                print('-' * 25)
                print('생성 완료 : 더블 링크드 리스트')
                
                while True:
                    print('0. 뒤로가기')
                    print('1. 노드 생성 및 삽입(append)')
                    print('2. 노드 생성 및 삽입(insert)')
                    print('3. 노드 삭제')
                    print('4. 노드 탐색')
                    print('5. 리스트 전체 출력')
                    print('-' * 25)

                    selected = int(input('입력: '))
                    
                    if selected == 0:
                        del list1
                        print('삭제 완료 : 더블 링크드 리스트')
                        break
                    elif selected == 1:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        list1.appendNode(node)
                    elif selected == 2:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        loc = int(input('삽입할 위치: '))
                        list1.insertAfter(loc, node)
                    elif selected == 3:
                        loc = int(input('삭제할 노드 위치: '))
                        node = list1.getNodeByLocation(loc)
                        list1.removeNode(node)
                    elif selected == 4:
                        loc = int(input("찾을 위치: "))
                        node = list1.getNodeByLocation(loc)
                        print(f'{loc}위치 : {node.prev.data} << {node.data} >> {node.next.data}')
                    elif selected == 5:
                        size = list1.getSize()
                        for i in range(size):
                            node = list1.getNodeByLocation(i)
                            if i == 0:
                                if node.prev == None:
                                    print(f'Head : NULL << ', end="")
                                else:
                                    print(f'Head : {node.prev.data} << ', end="")

                                print(f'{node.data} >> ', end="")

                                if node.next == None:
                                    print(f'NULL', end="")
                                else:
                                    print(f'{node.next.data}', end="")
                            elif i == size-1:
                                if node.prev == None:
                                    print(f'Tail : NULL << ', end="")
                                else:
                                    print(f'Tail : {node.prev.data} << ', end="")

                                print(f'{node.data} >> ', end="")
                                
                                if node.next == None:
                                    print(f'NULL')
                                else:
                                    print(f'{node.next.data}')
                                break
                            else:
                                print(f'{node.prev.data} << {node.data} >> {node.next.data}', end="")
                            print(f' -> ', end="")
                    print('-' * 25)
            elif selected == 3:
                list1 = CDLL.CircularLinkedList()
                print('-' * 25)
                print('생성 완료 : 환형 링크드 리스트')
                
                while True:
                    print('0. 뒤로가기')
                    print('1. 노드 생성 및 삽입(append)')
                    print('2. 노드 생성 및 삽입(insert)')
                    print('3. 노드 삭제')
                    print('4. 노드 탐색')
                    print('5. 리스트 전체 출력')
                    print('-' * 25)

                    selected = int(input('입력: '))
                    
                    if selected == 0:
                        del list1
                        print('삭제 완료 : 환형 링크드 리스트')
                        break
                    elif selected == 1:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        list1.appendNode(node)
                    elif selected == 2:
                        data = input('삽입할 데이터: ')
                        node = list1.createNode(data)
                        loc = int(input('삽입할 위치: '))
                        list1.insertAfter(loc, node)
                    elif selected == 3:
                        loc = int(input('삭제할 노드 위치: '))
                        node = list1.getNodeByLocation(loc)
                        list1.removeNode(node)
                    elif selected == 4:
                        loc = int(input("찾을 위치: "))
                        node = list1.getNodeByLocation(loc)
                        print(f'{loc}위치 : {node.prev.data} << {node.data} >> {node.next.data}')
                    elif selected == 5:
                        size = list1.getSize()
                        for i in range(size):
                            node = list1.getNodeByLocation(i)
                            print(f'{node.prev.data} << {node.data} >> {node.next.data}', end="")
                            print(f' -> ', end="")
                        print()
                    print('-' * 25)
