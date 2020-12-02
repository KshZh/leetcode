# 1277. Count Square Submatrices with All Ones

> Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.
>
> **Example 1:**
>
> ```
> Input: matrix =
> [
>   [0,1,1,1],
>   [1,1,1,1],
>   [0,1,1,1]
> ]
> Output: 15
> Explanation: 
> There are 10 squares of side 1.
> There are 4 squares of side 2.
> There is  1 square of side 3.
> Total number of squares = 10 + 4 + 1 = 15.
> ```

1. Medium，DP。

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        // 使用和修改了参数，没有自己分配内存。
        auto& dp = matrix; // dp[i][j]表示以matrix[i][j]为右下角的正方形的最大边长。
        // 边界是dp[0][i]和dp[i][0]。
        int i, j;
        int m=matrix.size(), n=matrix[0].size();
        int sum = 0;
        for (i=1; i<m; i++) {
            for (j=1; j<n; j++) {
                if (matrix[i][j] == 0) // 为0要跳过，不能放入下面的通用计算中，否则考虑[[1, 2], [1, 0]]，那么会错误地得出dp[1][1]=1x。
                    continue;
                dp[i][j] = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1])) + matrix[i][j];
                sum += dp[i][j]; // 最大边长为3，那么必然存在以该点为右下角的边长为1和2的正方形，故以该点为右下角的正方形共有dp[i][j]个。
            }
        }
        for (i=1; i<n; i++) // 不从0开始，否则如果matrix[0][0]为1，那么两个循环就会加了matrix[0][0]两次。
            sum += dp[0][i];
        for (i=1; i<m; i++) // 不从0开始，否则如果matrix[0][0]为1，那么两个循环就会加了matrix[0][0]两次。
            sum += dp[i][0];
        sum += dp[0][0];
        return sum;
    }
};
```

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        // 简化了第一份代码的书写。
        auto& dp = matrix;
        int i, j;
        int m=matrix.size(), n=matrix[0].size();
        int sum = 0;
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (dp[i][j] && i && j)
                    dp[i][j] += min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1]));
                sum += dp[i][j];
            }
        }
        return sum;
    }
};
```

