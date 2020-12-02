# 147. Insertion Sort List

1. Medium。

```cpp
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        // 如果没有结点，则返回nullptr；如果只有一个结点，就返回这个结点的地址。
        if (!head || !head->next)
            return head;
        
        ListNode dummy(-1);
        ListNode* q = head;
        ListNode *p, *temp;
        while (q) {
            temp = q->next;
            p = &dummy; // 要插入，所以要有前驱指针。
            while (p->next && p->next->val<q->val) { // 找到合适的插入位置。
                p = p->next;
            }
            q->next = p->next;
            p->next = q;
            q = temp;
        }
        return dummy.next;
    }
};
```

