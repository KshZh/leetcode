# 62. Unique Paths

> A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).
>
> The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>
> How many possible unique paths are there?
>
> ![img](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

1. DP，Medium。

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0)); // dp[i][j]表示到达第i, j个格子有几种方式。
        int i, j;
        // 边界。
        for (i=0; i<m; i++)
            dp[i][0] = 1;
        for (i=0; i<n; i++)
            dp[0][i] = 1;
        for (i=1; i<m; i++) {
            for (j=1; j<n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        // O(N)空间复杂度。
        vector<int> dp(n, 0);
        int i, j;
        for (i=0; i<n; i++)
            dp[i] = 1;
        for (i=1; i<m; i++) {
            for (j=1; j<n; j++) {
                dp[j] = dp[j] + dp[j-1]; // 右边的dp[j]是旧值，也就是上一行的dp[j]，dp[j-1]是当前行的。
            }
        }
        return dp[n-1];
    }
};
```

