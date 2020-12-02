# 63. Unique Paths II

> A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).
>
> The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
>
> Now consider if some obstacles are added to the grids. How many unique paths would there be?
>
> An obstacle and empty space is marked as `1` and `0` respectively in the grid.

1. DP，Medium。

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0]) return 0; // 起点就不通的边界情况。
        int i, j;
        auto m=obstacleGrid.size(), n=obstacleGrid[0].size();
        vector<unsigned int> dp(n, 0);
        dp[0] = 1;
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (obstacleGrid[i][j] == 1)
                    dp[j] = 0;
                else if (j > 0)
                    dp[j] = dp[j] + dp[j-1];
            }
        }
        return dp[n-1];
    }
};
```

