# 1290. Convert Binary Number in a Linked List to Integer

> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)
>
> ```
> Input: head = [1,0,1]
> Output: 5
> Explanation: (101) in base 2 = (5) in base 10
> ```

1. Easy，头结点是最高有效位。

```cpp
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int ans = 0;
        while (head) {
            ans = ans*2 + head->val;
            head = head->next;
        }
        return ans;
    }
};
```

