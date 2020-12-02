# 82. Remove Duplicates from Sorted List II

> Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only *distinct* numbers from the original list.
>
> **Example 1:**
>
> ```
> Input: 1->2->3->3->4->4->5
> Output: 1->2->5
> ```
>
> **Example 2:**
>
> ```
> Input: 1->1->1->2->3
> Output: 2->3
> ```

1. Medium。

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode* p = &dummy;
        ListNode* q;
        while (p->next) {
            q = p->next;
            while (q->next && q->next->val==p->next->val)
                q = q->next;
            if (q != p->next) {
                // 这里没有释放动态内存，有内存泄漏。
                p->next = q->next;
            } else {
                p = p->next;
            }
        }
        return dummy.next;
    }
};
```

```cpp
// 递归解法。
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* p = head->next;
        while (p && p->val==head->val)
            p = p->next;
        if (p == head->next) {
            head->next = deleteDuplicates(head->next);
            return head;
        }
        return deleteDuplicates(p);
    }
};
```

