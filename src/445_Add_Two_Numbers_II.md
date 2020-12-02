# 445. Add Two Numbers II

> You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
>
> You may assume the two numbers do not contain any leading zero, except the number 0 itself.
>
> **Follow up:**
> What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
>
> **Example:**
>
> ```
> Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
> Output: 7 -> 8 -> 0 -> 7
> ```

1. Medium。
2. 一个思路是反转两个链表，然后头插法创建逆序链表；另一个是使用栈间接反转链表，然后同理。
3. 注意到不需要carry这个变量的加法运算的实现。

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1, s2;
        while (l1) {
            s1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            s2.push(l2->val);
            l2 = l2->next;
        }
        int sum=0;
        ListNode dummy(-1), *p;
        // 遍历完较长的串且处理最高位进位。
        while (!s1.empty() || !s2.empty() || sum) {
            if (!s1.empty()) {
                sum += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                sum += s2.top();
                s2.pop();
            }
            p = new ListNode(sum%10);
            p->next = dummy.next;
            dummy.next = p; // 头插法创建逆序链表。
            sum /= 10;
        }
        return dummy.next;
    }
};
```

