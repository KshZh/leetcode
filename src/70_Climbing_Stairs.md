# 70. Climbing Stairs

> You are climbing a stair case. It takes *n* steps to reach to the top.
>
> Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
>
> **Note:** Given *n* will be a positive integer.

1. Easy，DP。

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1); // dp[i]表示有多少种方式到达第i个台阶。
        // 状态转移方程：dp[i] = dp[i-1] + dp[i-2];
        // 边界。
        dp[1] = 1;
        dp[0] = 1;
        for (int i=2; i<=n; i++)
            dp[i] = dp[i-1] + dp[i-2];
        return dp[n];
    }
};
```

