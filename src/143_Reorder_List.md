# 143. Reorder List

> You may **not** modify the values in the list's nodes, only nodes itself may be changed.
>
> **Example 1:**
>
> ```
> Given 1->2->3->4, reorder it to 1->4->2->3.
> ```
>
> **Example 2:**
>
> ```
> Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
> ```

1. Medium。
2. 思路是反转后半部分后插入前半部分。
4. 对于快慢指针遍历链表，对于偶数个结点的链表，如果从dummy结点开始走，那么结束时，slow指针指向中间两个结点中的前者，否则指向中间两个结点中的后者。对于奇数个结点的链表，则没有区别，都是结束时slow指针指向中间的那个结点。

```cpp
class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;
        ListNode *slow=head, *fast=head, *p, *q;
        // 对于快慢指针遍历链表，对于偶数个结点的链表，如果从dummy结点开始走，
        // 那么结束时，slow指针指向中间两个结点中的前者，否则指向中间两个结点中的后者。对于奇数个结点的链表，则没有区别，都是结束时slow指针指向中间的那个结点。
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        p = slow;
        slow = slow->next;
        p->next = nullptr;
        slow = reverse(slow);
        p = head;
        while (slow) {
            q = slow->next;
            slow->next = p->next;
            p->next = slow;
            slow = q;
            p = p->next->next;
        }
    }
    
    ListNode* reverse(ListNode* head) {
        // head不指向头结点。
        if (!head->next) return head;
        ListNode* newHead = reverse(head->next);
        head->next->next = head; // head->next指向newHead链表的最后一个结点。
        head->next = nullptr;
        return newHead;
    }
};
```

