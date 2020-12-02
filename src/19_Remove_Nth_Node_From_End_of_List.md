# 19. Remove Nth Node From End of List

> Given a linked list, remove the *n*-th node from the end of list and return its head.
>
> **Example:**
>
> ```
> Given linked list: 1->2->3->4->5, and n = 2.
> 
> After removing the second node from the end, the linked list becomes 1->2->3->5.
> ```
>
> **Note:**
>
> Given *n* will always be valid.
>
> **Follow up:**
>
> Could you do this in one pass?

1. Medium，快慢指针（其实不是，只是让其中一个指针先走几步）。

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode *p=&dummy, *q=&dummy;
        // 因为题目保证给出的n是有效的（即n<=链表长），所以这里没有检查p是否为nullptr。
        for (int i=0; i<n+1; i++) {
            p = p->next;
        }
        while (p) {
            p = p->next;
            q = q->next;
        }
        // q现在指向要删除的结点的前驱结点。
        p = q->next;
        q->next = p->next;
        delete p;
        return dummy.next;
    }
};
```

