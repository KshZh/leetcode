# 21. Merge Two Sorted Lists

> Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
>
> **Example:**
>
> ```
> Input: 1->2->4, 1->3->4
> Output: 1->1->2->3->4->4
> ```

1. Easy。

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(-1);
        ListNode* p = &dummy;
        while (l1 || l2) {
            if (!l1) {
                p->next = new ListNode(l2->val);
                l2 = l2->next;
            } else if (!l2) {
                p->next = new ListNode(l1->val);
                l1 = l1->next;
            } else if (l1->val <= l2->val) {
                p->next = new ListNode(l1->val);
                l1 = l1->next;
            } else {
                p->next = new ListNode(l2->val);
                l2 = l2->next;
            }
            p = p->next;
        }
        // 如果是in-place，那么直接`p->next=l1`串起来即可。
        return dummy.next;
    }
};
```

```cpp
// 递归、in-place。
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        if (l1->val <= l2->val) {
            // 对l1->next赋值表示把l1指向的结点从链表l1中分离出来，
            // 然后令该结点指向mergeTwoLists()返回的合并好的有序链表。
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};
```

