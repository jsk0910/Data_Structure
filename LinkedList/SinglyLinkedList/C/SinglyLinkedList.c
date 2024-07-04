#include "SinglyLinkedList.h"

Node* createNode(ElementType item) {
    Node* NewNode = (Node*) malloc(sizeof(Node));

    NewNode->item = item;
    NewNode->next = NULL;

    return NewNode;
}