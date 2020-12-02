# 2. Add Two Numbers

> **Example:**
>
> ```
> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
> Output: 7 -> 0 -> 8
> Explanation: 342 + 465 = 807.
> ```

1. Medium。
2. 遍历完较长的序列，较短的序列取运算中的单位元并选择性更新。

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(-1);
        ListNode* p = &head;
        int carry = 0, val, x, y;
        // 注意这里是遍历完较长的序列，较短的序列取加法运算的单位元0。
        while (l1 || l2) {
            x = l1? l1->val: 0;
            y = l2? l2->val: 0;
            val = x+y+carry;
            carry = val/10;
            p->next = new ListNode(val%10);
            p = p->next;
            if (l1) l1=l1->next;
            if (l2) l2=l2->next;
        }
        // 记得处理最高位的进位。
        if (carry)
            p->next = new ListNode(carry);
        return head.next;
    }
};
```

