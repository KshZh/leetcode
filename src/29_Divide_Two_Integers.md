# 29. Divide Two Integers

> Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division and mod operator.
>
> Return the quotient after dividing `dividend` by `divisor`.
>
> The integer division should truncate toward zero.
>
> **Example 1:**
>
> ```
> Input: dividend = 10, divisor = 3
> Output: 3
> ```
>
> **Example 2:**
>
> ```
> Input: dividend = 7, divisor = -3
> Output: -2
> ```
>
> **Note:**
>
> - Both dividend and divisor will be 32-bit signed integers.
> - The divisor will never be 0.
> - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

1. Medium。
2. 不能直接用乘法和除法，但可以用左移和右移位运算来乘以或除以2的次幂。
3. 一个明显的边界条件就是，32位补码，负数比正数多一个，0占了正数一个位置。所以正数无法表示`-INT_MIN`。这里利用负数可表示的数更多的特点，把被除数和除数都用负数表示。也就是不用abs了，对INT_MIN用abs，leetcode会报错。

```cpp
class Solution {
public:
    int divide(int dividend, int divisor) {
        // 几个边界情况。
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        if (divisor == 1) return dividend;
        if (dividend == divisor) return 1;
        // 设置商的符号，这样被除数和除数的符号就可以随意修改了。
        int sign = 1;
        if ((dividend>>31)^(divisor>>31)) sign = 0;
        if (dividend > 0) dividend = -dividend;
        if (divisor > 0) divisor = -divisor;
        int ans=0, x;
        while (dividend <= divisor) {
            // 16 3
            // 13能提出3*2^0，能提出3*2^1，能提出3*2^2，所以一次性减掉2^2个3，得到4。
            // 4能提出3*2^0，减掉2^0个3，得到1。
            // 被除数小于除数，结束循环。
            for (x=0; (int)((unsigned)divisor<<x<<1)<0 && (int)((unsigned)divisor<<x<<1)>=INT_MIN && dividend<=(int)((unsigned)divisor<<x<<1); x++) // 注意首先要确保扩展后的除数不会溢出才行。
                ;
            ans += 1<<x;
            dividend -= (int)((unsigned)divisor<<x);
        }
        return sign? ans: -ans;
    }
};
```



