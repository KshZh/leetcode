# 876. Middle of the Linked List

> Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.
>
> If there are two middle nodes, return the second middle node.

1. Easy，快慢指针。
2. 对于偶数个结点的链表，如果从dummy结点出发，则slow最终指向中间两个结点中的前者，否则指向中间两个结点中的后者；对于奇数个结点的链表，则slow总是指向中间的那个结点。

```cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *fast=head, *slow=head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;
    }
};
```

