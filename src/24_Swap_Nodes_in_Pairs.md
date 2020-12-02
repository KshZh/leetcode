# 24. Swap Nodes in Pairs

> Given a linked list, swap every two adjacent nodes and return its head.
>
> You may **not** modify the values in the list's nodes, only nodes itself may be changed.
>
> **Example:**
>
> ```
> Given 1->2->3->4, you should return the list as 2->1->4->3.
> ```

1. Medium，反转链表。
2. **设计递归算法时，从宏观上设计/观察递归函数的输入、输出。然后具体地，再设计递归边界和子问题。如递归函数swapPairs的输入是一个普通链表，输出是一个已经两两交换过的链表。那么我们就可以从宏观上去调用/使用该函数，而不必纠结内部实现细节以及递归的繁琐的展开和求值过程，反正我们已经知道/能够保证该递归函数的接收某个输入必定产出对应的输出即可。**

```cpp
// 两两交换可看作不断反转大小为2的block。
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode* prev = &dummy;
        while (prev->next) { // 看是否还有待逆序的block。
            prev = reverse(prev, 2);
        }
        return dummy.next;
    }
    
    // 反转大小为n的block，prev是该block的前驱指针。
    ListNode* reverse(ListNode* prev, int n) {
        ListNode* p=prev; // p指向已逆序好的结点；
        ListNode* q=p->next; // q指向即将要逆序的结点；
        ListNode* temp;
        for (int i=0; i<n && q; i++) {
            temp = q->next;
            q->next = p;
            p = q;
            q = temp;
        }
        temp = prev->next;
        prev->next = p;
        temp->next = q;
        return temp; // 返回下一个逆序block的前驱结点的指针。
    }
};
```

```cpp
// 简洁的链表递归解法。
// 设计递归算法时，从宏观上设计/观察递归函数的输入、输出。然后具体地，再设计递归边界和子问题。
// 如递归函数swapPairs的输入是一个普通链表，输出是一个已经两两交换过的链表。那么我们就可以从宏观上去调用/使用该函数，而不必纠结内部实现细节以及递归的繁琐的展开和求值过程，反正我们已经知道/能够保证该递归函数的接收某个输入必定产出对应的输出即可。
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* p = head->next;
        head->next = swapPairs(head->next->next);
        p->next = head;
        return p;
    }
};
```

```cpp
// 用二级指针替代dummy结点。
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // pp第一次指向head指针，后面指向实际结点的next指针。那么解引用pp时，就可以修改head指针和结点的next指针本身，而不是副本。
        // XXX 使用二级指针pp，相当于pp指向不存在的dummy结点的next成员和其他结点的next成员。
        ListNode** pp=&head, *a, *b;
        while ((a=*pp) && (b=a->next)) {
            a->next = b->next;
            b->next = a;
            *pp = b;
            pp = &(a->next);
        }
        return head;
    }
};
```

