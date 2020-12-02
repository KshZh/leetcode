# 234. Palindrome Linked List

> Given a singly linked list, determine if it is a palindrome.
>
> **Example 1:**
>
> ```
> Input: 1->2
> Output: false
> ```
>
> **Example 2:**
>
> ```
> Input: 1->2->2->1
> Output: true
> ```
>
> **Follow up:**
> Could you do it in O(n) time and O(1) space?

1. Easy，链表。

```cpp
// O(N)空间复杂度。
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> v;
        int n=0;
        ListNode* p = head;
        while (p) {
            n++;
            p = p->next;
        }
        p = head;
        for (int i=0; i<n/2; i++) {
            v.push_back(p->val);
            p = p->next;
        }
        if (n & 1) p = p->next; // 奇数个结点，跳过最中间的结点。
        for (int i=v.size()-1; i>=0; i--) {
            if (p->val != v[i])
                return false;
            p = p->next;
        }
        return true;
    }
};
```

```cpp
// 快慢指针边遍历边反转链表，O(1)。如果需要保持参数不变的话，可以在返回前再反转回来。
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;
        ListNode *slow=head, *fast=head, *a=nullptr, *b=head->next; // ab分别指向slow指向的结点的前驱和后继结点。
        while (fast && fast->next) {
            fast = fast->next->next;
            slow->next = a;
            a = slow;
            slow = b;
            b = b->next;
        }
        if (fast) slow = slow->next; // 奇数个结点，跳过中间结点。
        while (slow) {
            if (a->val != slow->val)
                return false;
            slow = slow->next;
            a = a->next;
            
            // 如果有需要就在这里顺便把链表再反转回来。
            // 同样设置两个指针，分别为a的前驱和后继指针。
        }
        return true;
    }
};
```

