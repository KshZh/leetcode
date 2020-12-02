# 328. Odd Even Linked List

> Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
>
> You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
>
> **Example 1:**
>
> ```
> Input: 1->2->3->4->5->NULL
> Output: 1->3->5->2->4->NULL
> ```
>
> **Example 2:**
>
> ```
> Input: 2->1->3->5->6->4->7->NULL
> Output: 2->3->6->7->1->5->4->NULL
> ```
>
> **Note:**
>
> - The relative order inside both the even and odd groups should remain as it was in the input.
> - The first node is considered odd, the second node even and so on ...

1. Medium。

```cpp
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        ListNode odd(-1), even(-1), *po=&odd, *pe=&even;
        for (int i=1; head; i++, head=head->next) {
            if (i&1) {
                po->next = head;
                po = po->next;
            } else {
                pe->next = head;
                pe = pe->next;
            }
        }
        pe->next = nullptr;
        po->next = even.next;
        return odd.next;
    }
};
```

```cpp
// 由于这道题的题意，所以可以这样实现：
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *odd=head, *even=head->next, *evenHead=head->next;
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
        return head;
    }
};
```

