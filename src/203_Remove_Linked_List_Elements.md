# 203. Remove Linked List Elements

> Remove all elements from a linked list of integers that have value ***val\***.
>
> **Example:**
>
> ```
> Input:  1->2->6->3->4->5->6, val = 6
> Output: 1->2->3->4->5
> ```

1. Easy。

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // 设置一个哨兵结点，这样在需要删除头节点时，才比较方便处理。
        // 且因为要在单链表中删除结点，所以必须维护一个前驱指针。
        ListNode dummy(-1), *p=&dummy, *q;
        dummy.next = head;
        while (p->next) {
            q = p->next;
            while (q && q->val==val)
                q = q->next;
            if (q != p->next)
                p->next = q; // 存在内存泄露。
            else
                p = p->next;
        }
        return dummy.next;
    }
};
```

```cpp
// 链表的递归解法。
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return head;
        head->next = removeElements(head->next, val);
        return head->val==val? head->next: head;
    }
};
```

