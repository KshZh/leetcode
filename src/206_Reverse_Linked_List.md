# 206. Reverse Linked List

> Reverse a singly linked list.
>
> **Example:**
>
> ```
> Input: 1->2->3->4->5->NULL
> Output: 5->4->3->2->1->NULL
> ```
>
> **Follow up:**
>
> A linked list can be reversed either iteratively or recursively. Could you implement both?

1. Easy。

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 头插法需要一个dummy结点，或者说要逆序的block的前驱结点。
        // 头插法适用于要逆序整个链表的情况，因为此时block的前驱结点
        // 的next指针可以明显地初始化为nullptr，对于部分反转的情况，
        // 我们需要先遍历一下得到block的前驱结点的next指针的初始值，即
        // block的后继结点(successor)的地址。
        ListNode dummy(-1), *q;
        while (head) {
            q = head->next;
            head->next = dummy.next;
            dummy.next = head;
            head = q;
        }
        return dummy.next;
    }
};
```

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // 双指针，适用面比较广，不需要提前知道block的后继结点的地址。
        // p指向已逆序好的结点（该block的前驱结点（上一个逆序好的block的最后一个结点），然后循环完后再通过该block的前驱结点设置该逆序好的block的后继结点），如果是第一个block，没有前驱结点，那么p就如实为nullptr），
        // q指向即将要逆序的结点（初始时指向block的第一个结点）。
        ListNode *p=nullptr, *q=head, *temp;
        while (q) { // 该block还有待逆序的结点？
            temp = q->next;
            q->next = p;
            p = q;
            q = temp;
        }
        return p;
    }
};
```

```cpp
// 递归。
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* newHead = reverseList(head->next);
        // 此时head->next指向newHead链表的最后一个结点。 
        head->next->next = head; // 这一条语句才是真正在反转链表。
        head->next = nullptr;
        return newHead;
    }
};
```

