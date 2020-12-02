# 92. Reverse Linked List II

> Reverse a linked list from position *m* to *n*. Do it in one-pass.
>
> **Note:** 1 ≤ *m* ≤ *n* ≤ length of list.
>
> **Example:**
>
> ```
> Input: 1->2->3->4->5->NULL, m = 2, n = 4
> Output: 1->4->3->2->5->NULL
> ```

1. Medium。

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m >= n) return head;
        ListNode dummy(-1);
        ListNode* p = &dummy;
        p->next = head;
        for (int i=0; i<m-1; i++) {
            p = p->next;
        }
        ListNode *a=p, *b=a->next, *temp;
        // a指向已逆序好的结点（初始时为前一个逆序好的block的尾结点，如果当前block是第一个block，没有前驱结点，则a如实为nullptr），
        // b指向即将要逆序的结点。
        for (int i=0; i<n-m+1 && b; i++) {
            temp = b->next;
            b->next = a;
            a = b;
            b = temp;
        }
        // 逆序好后，当前block的前驱结点指向当前block的尾结点，
        // 而第二个指针b指向后继block的第一个结点，所以可以在这里
        // 方便地设置当前block指向恰当的后继block。
        temp = p->next;
        p->next = a;
        temp->next = b;
        return dummy.next;
    }
};
```

> https://leetcode.com/fudonglai
>
> To solve the problem recursively, step by step.
>
> First, I know the classic recursive way to reverse a linked list:
>
> ```java
> ListNode reverse(ListNode head) { // 注意参数head并不指向dummy结点，下同。
>  if (head.next == null) return head;
>  ListNode last = reverse(head.next);
>  head.next.next = head; // 实际在反转链表的是这一条语句。
>  head.next = null;
>  return last;
>  }
> ```
> 
>Then I come up this way to reverse the first N elements:
> 
>```java
> ListNode successor = null;
> ListNode reverseN(ListNode head, int n) {
> if (n == 1) {
>    // 先跑到block的最后一个结点，然后回来再一个一个结点反转。
>      successor = head.next;
>      return head;
>    }
>  ListNode last = reverseN(head.next, n - 1);
>  head.next.next = head; // 实际在反转链表的是这一条语句。
>  head.next = successor;
>  return last;
>  }    
>  ```
> 
> Finally I solve this problem:
>
> ```java
>public ListNode reverseBetween(ListNode head, int m, int n) {
> if (m == 1) {
>   // You can also expand the code here to get rid of the helper function 'reverseN'
>    return reverseN(head, n);
>    }
>    head.next = reverseBetween(head.next, m - 1, n - 1);
>  return head;
>  }
>  ```