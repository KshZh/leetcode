# 141. Linked List Cycle

> Given a linked list, determine if it has a cycle in it.
>
> **Example 1:**
>
> ```
> Input: head = [3,2,0,-4], pos = 1
> Output: true
> Explanation: There is a cycle in the linked list, where tail connects to the second node.
> ```
>
> ![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

1. 链表、哈希表、快慢指针，Easy。

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> book;
        while (head) {
            if (book.find(head) != book.end()) return true;
            book.insert(head);
            head = head->next;
        }
        return false;
    }
};
```

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow=head, *fast=head;
        do {
            if (!fast || !fast->next) return false; // 快指针先到达终点，所以不存在环。
            slow = slow->next;
            fast = fast->next->next;
        } while (slow != fast); // 如果存在环，那么快慢指针最终会相遇。
        return true;
    }
};
```



