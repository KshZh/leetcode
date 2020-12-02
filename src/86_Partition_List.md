# 86. Partition List

> Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.
>
> You should preserve the original relative order of the nodes in each of the two partitions.
>
> **Example:**
>
> ```
> Input: head = 1->4->3->2->5->2, x = 3
> Output: 1->2->2->4->3->5
> ```

1. Medium。

```cpp
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode l(-1), ge(-1);
        ListNode *pl=&l, *pge=&ge, *p=head;
        while (p) {
            if (p->val < x) {
                pl->next = p;
                pl = pl->next;
            } else {
                pge->next = p;
                pge = pge->next;
            }
            p = p->next;
        }
        pl->next = ge.next;
        pge->next = nullptr;
        return l.next;
    }
};
```

