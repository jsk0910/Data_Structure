#ifndef SINGLY_LINKED_LIST_H
#define SINGLY_LINKED_LIST_H

#include <stdio.h>
#include <stdlib.h>

// 타입 선언
typedef int ElementType; // item의 타입

typedef struct Node {
    ElementType item;
    struct Node* next;
}Node;

// 노드를 관리하는 함수들
Node* createNode(ElementType item);
Node* destroyNode(Node* RemoveNode);

// 링크드리스트의 기본 함수들
void insertAfter(Node* NewNode);
void removeNode(Node* NewNode);
void searchNode(int Location);

// 링크드리스트의 추가 제공 함수들
int isEmpty(Node** LinkedList);
int GetNodeCount(Node** LinkedList);

// 링크드리스트의 인터페이스 함수들
Node** makeList();
void append(ElementType item);
void pop();

#endif