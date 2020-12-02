# 172. Factorial Trailing Zeroes

> Given an integer *n*, return the number of trailing zeroes in *n*!.
>
> **Example 1:**
>
> ```
> Input: 3
> Output: 0
> Explanation: 3! = 6, no trailing zero.
> ```
>
> **Example 2:**
>
> ```
> Input: 5
> Output: 1
> Explanation: 5! = 120, one trailing zero.
> ```
>
> **Note:** Your solution should be in logarithmic time complexity.

1. Easy。

```cpp
// 0由2的倍数乘以5的倍数产生，显然在[1, n]范围内，2的倍数总是比5的倍数多，所以只需要计算短板，也就是该区间内5的倍数的个数即可。
// 准确地说是计算5的个数，因为2*5产生一个0，故有几个5就有几个0。所以如果是5*5这种元素，算两个5。
// 25!=5*10*15*20*25=5*5*5*5*(5*5)=6*5，25/5=5，5/5=1。
class Solution {
public:
    int trailingZeroes(int n) {
        int cnt=0;
        while (n) {
            cnt += n/5; // n/5的到n中可有多少个5组成，等价于[1, n]区间内有多少个5的倍数。
            n /= 5;
        }
        return cnt;
    }
};
```

