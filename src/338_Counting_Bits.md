# 338. Counting Bits

> Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.
>
> **Example 1:**
>
> ```
> Input: 2
> Output: [0,1,1]
> ```
>
> **Example 2:**
>
> ```
> Input: 5
> Output: [0,1,1,2,1,2]
> ```

1. Medium，DP。

```cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> dp(num+1, 0); // dp[i]表示数字i的二进制表示中有多少个1。
        for (int i=1; i<=num; i++) {
            dp[i] = dp[i>>1]+(i&1); // 高位中的1的个数 + 最低位的1的个数。
        }
        return dp;
    }
};
```

