# 25. Reverse Nodes in k-Group

> Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.
>
> *k* is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k* then left-out nodes in the end should remain as it is.
>
> **Example:**
>
> Given this linked list: `1->2->3->4->5`
>
> For *k* = 2, you should return: `2->1->4->3->5`
>
> For *k* = 3, you should return: `3->2->1->4->5`
>
> **Note:**
>
> - Only constant extra memory is allowed.
> - You may not alter the values in the list's nodes, only nodes itself may be changed.

1. Hard。

```cpp
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k<=1 || !head) return head;
        int n = getLen(head);
        ListNode dummy(-1), *prev=&dummy;
        prev->next = head;
        for (int i=0; i<=n-k; i+=k) { // 不足k个则不反转。
            prev = reverse(prev, k);
        }
        return dummy.next;
    }
    
    // prev是即将要反转的block的前驱结点。
    ListNode* reverse(ListNode* prev, int k) {
        // p指向已逆序好的结点，q指向即将逆序的结点。
        ListNode *p=prev, *q=p->next, *temp;
        // 注意条件，逆序k个或逆序少于k个，如果剩余长度不足的话。
        for (int i=0; i<k && q; i++) {
            temp = q->next;
            q->next = p;
            p = q;
            q = temp;
        }
        temp = prev->next;
        prev->next = p;
        temp->next = q;
        return temp; // 返回下一个待逆序的block的前驱结点。
    }
    
    int getLen(ListNode* head) {
        int n = 0;
        while (head) {
            n++;
            head = head->next;
        }
        return n;
    }
};
```

```cpp
// 递归、非常量空间复杂度实现。
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* p = head, *newHead;
        int i;
        for (i=0; i<k && p; i++) {
            newHead = p;
            p = p->next;
        }
        if (i!=k) return head; // 不足k个结点不反转。
        ListNode* tail = reverseKGroup(p, k); // 从宏观上设计递归函数，关注输入、输出，这里tail指向一个已逆序好的链表表头。
        ListNode *q = head, *temp;
        for (i=0; i<k; i++) {
            temp = q->next;
            q->next = p;
            p = q;
            q = temp;
        }
        head->next = tail;
        return newHead;
    }
};
```

