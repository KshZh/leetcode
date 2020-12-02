# 371. Sum of Two Integers

> Calculate the sum of two integers *a* and *b*, but you are **not allowed** to use the operator `+` and `-`.
>
> **Example 1:**
>
> ```
> Input: a = 1, b = 2
> Output: 3
> ```
>
> **Example 2:**
>
> ```
> Input: a = -2, b = 3
> Output: 1
> ```

1. Easy。

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        int carry;
        while (b) {
            // 对应位都为1的位才得到1，也就是得出加起来会进位的位。
            carry = a&b;
            // 对应都为0和1的位“加”/抑或得到0，即不考虑进位的加法。
            a ^= b;
            // 进位左移一位，这是符合加法规则的，进入下一轮，直到进位为0。
            b = (unsigned)carry<<1;
        }
        return a;
    }
};
```

