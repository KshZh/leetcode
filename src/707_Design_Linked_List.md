# 707. Design Linked List

1. Medium。
2. 使用了尾指针可以使得在尾部插入的时间复杂度为O(1)，但也要注意其他插入或删除操作中，要随时注意是否插入新的尾结点或删除了尾结点，此时要更新尾指针。

```cpp
class MyLinkedList {
private:
    struct Node {
        Node() = default;
        // 使用默认实参，这样一个ctor就可以有两种调用实参列表，而不用写两个ctor。
        Node(int v, Node* n=nullptr): val(v), next(n) {}
        int val;
        Node* next;
    };
    Node head; // dummy;
    Node* tail;
    int N;
public:
    /** Initialize your data structure here. */
    MyLinkedList(): head(), tail(&head), N(0) {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index >= N) return -1;
        Node* p = head.next;
        for (int i=0; i<index; i++)
            p = p->next;
        return p->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        head.next = new Node(val, head.next);
        if (tail == &head)
            tail = head.next;
        N++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        tail->next = new Node(val);
        tail = tail->next;
        N++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > N) return;
        Node* p = &head; // 要在单链表中插入，所以要得到插入位置的前驱指针。
        for (int i=0; i<index; i++)
            p = p->next;
        p->next = new Node(val, p->next);
        if (p == tail)
            tail = p->next;
        N++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index >= N) return;
        Node* p = &head; // 要在单链表中删除，所以要得到删除位置的前驱指针。
        for (int i=0; i<index; i++)
            p = p->next;
        Node* temp = p->next;
        p->next = temp->next;
        if (temp == tail)
            tail = p;
        delete temp;
        N--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```



