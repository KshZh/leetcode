# 61. Rotate List

> Given a linked list, rotate the list to the right by *k* places, where *k* is non-negative.
>
> **Example 1:**
>
> ```
> Input: 1->2->3->4->5->NULL, k = 2
> Output: 4->5->1->2->3->NULL
> Explanation:
> rotate 1 steps to the right: 5->1->2->3->4->NULL
> rotate 2 steps to the right: 4->5->1->2->3->NULL
> ```
>
> **Example 2:**
>
> ```
> Input: 0->1->2->NULL, k = 4
> Output: 2->0->1->NULL
> Explanation:
> rotate 1 steps to the right: 2->0->1->NULL
> rotate 2 steps to the right: 1->2->0->NULL
> rotate 3 steps to the right: 0->1->2->NULL
> rotate 4 steps to the right: 2->0->1->NULL
> ```

1. Medium，链表循环右移。
2. 因为题目给出的k可能大于N，所以算出链表长度是必须的。这也导致无法在不算出链表长度的情况下，使用“快慢指针”，即第一个指针先走`k%N`步。
3. 初始化为1，因为我们想要获得指向最后一个结点的指针，而不是nullptr。
4. 把链表首位连起来。

```cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k==0) return head;
        int n = 1; // 初始化为1，因为我们想要获得指向最后一个结点的指针，而不是nullptr。
        ListNode* p = head;
        while (p->next) {
            n++;
            p = p->next;
        }
        p->next = head;
        k %= n;
        for (int i=0; i<n-k; i++) {
            p = p->next;
        }
        ListNode* newHead = p->next;
        p->next = nullptr;
        return newHead;
    }
};
```

