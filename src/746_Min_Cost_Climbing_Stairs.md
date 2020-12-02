# 746. Min Cost Climbing Stairs

> On a staircase, the `i`-th step has some non-negative cost `cost[i]` assigned (0 indexed).
>
> Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

1. Easy，DP。
2. 注意根据题意设计子问题，题目说了在台阶i处，花费cost[i]，就可以向上跳一个或两个台阶，又可以从台阶0或台阶1开始起跳，那么边界是`dp[0]=dp[1]=0`，即到达台阶0或台阶1花费的代价是0。

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        auto n = cost.size();
        vector<int> dp(n, 0); // dp[i]表示到达台阶i花费的代价。
        for (int i=2; i<n; i++) {
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]);
        }
        return min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2]);
    }
};
```

