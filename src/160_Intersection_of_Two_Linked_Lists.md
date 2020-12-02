# 160. Intersection of Two Linked Lists

> Write a program to find the node at which the intersection of two singly linked lists begins.
>
> For example, the following two linked lists:
>
> [![img](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)
>
> begin to intersect at node c1.

1. Easy。

```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*> s;
        while (headA) {
            s.insert(headA);
            headA = headA->next;
        }
        while (headB) {
            if (s.find(headB) != s.end())
                return headB;
            headB = headB->next;
        }
        return nullptr;
    }
};
```

```cpp
// tricky.
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // 明显的边界检查。
        if (!headA || !headB) return nullptr;
        ListNode *a=headA, *b=headB;
        while (a != b) {
            a = a? a->next: headB;
            b = b? b->next: headA;
        }
        return a;
    }
};
```

